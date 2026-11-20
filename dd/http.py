"""Polite HTTP client with on-disk cache. Every fetch can be recorded as a SourceDoc.

Use `Http.get(...)` from collectors instead of httpx directly so that:
  - responses are cached (re-runs are free and offline-friendly),
  - each host gets a small delay between requests,
  - the raw bytes are kept for audit (snippet verification).
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
# with 5xx: never served from cache. 401/403 too: the cache key ignores request headers, so an answer given
# without (or with a wrong) token must not outlive a later request that has the right one.
TRANSIENT = (0, 401, 403, 408, 425, 429)

RECORDED_HEADERS = ("server", "x-powered-by", "x-generator", "x-vercel-id", "x-nf-request-id", "cf-ray",
                    "x-served-by", "x-wix-request-id")


@dataclass
class Resp:
    url: str
    status: int
    content: bytes
    content_type: str
    from_cache: bool
    sha256: str
    raw_path: str
    doc_id: int | None = None
    # A safe allowlist only: never persist Set-Cookie or other potentially sensitive headers.
    headers: dict[str, str] = field(default_factory=dict)

    @property
    def text(self) -> str:
        """Decoded with the page's declared charset: Czech news sites still serve windows-1250, which read as UTF-8
        turns names into 'Radom�r �ech'. Falls back to UTF-8, then windows-1250 if UTF-8 does not fit."""
        declared = re.search(r"charset=[\"']?([\w-]+)", self.content_type or "", re.I) \
            or re.search(rb"<meta[^>]{0,200}charset=[\"']?([\w-]+)", self.content[:4096], re.I)
        if declared:
            name = declared.group(1)
            name = name.decode("ascii", "ignore") if isinstance(name, bytes) else name
            try:
                return self.content.decode(name, errors="replace")
            except LookupError:
                pass
        try:
            return self.content.decode("utf-8")
        except UnicodeDecodeError:
            return self.content.decode("cp1250", errors="replace")

    def json(self) -> Any:
        return json.loads(self.content)

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 300


class Http:
    def __init__(self, cache_dir: Path, store=None, min_delay: float = 1.0, timeout: float = 30.0):
        self.cache_dir = cache_dir
        self.store = store
        self.min_delay = min_delay
        self.client = httpx.Client(timeout=timeout, follow_redirects=True, headers={"User-Agent": UA})
        self._last: dict[str, float] = {}

    def _key(self, method: str, url: str, params: Any, body: Any) -> str:
        blob = json.dumps([method, url, params, body], sort_keys=True, default=str).encode()
        return hashlib.sha256(blob).hexdigest()

    def request(self, method: str, url: str, *, params: dict | None = None, json_body: Any = None,
                headers: dict | None = None, use_cache: bool = True, company_id: str | None = None,
                kind: str | None = None, title: str | None = None) -> Resp:
        """Fetch (or load from cache). If company_id and kind are given, records a SourceDoc."""
        key = self._key(method, url, params, json_body)
        raw = self.cache_dir / key[:2] / f"{key}.bin"
        meta = raw.with_suffix(".json")
        m = json.loads(meta.read_text(encoding="utf-8")) if use_cache and raw.exists() and meta.exists() else None
        if m is not None and (m["status"] in TRANSIENT or m["status"] >= 500):
            m = None  # a cached outage/rate limit is not an answer: fetch again
        if m is not None:
            content = raw.read_bytes()
            resp = Resp(m["url"], m["status"], content, m.get("content_type", ""), True,
                        hashlib.sha256(content).hexdigest(), str(raw), headers=m.get("headers", {}))
        else:
            host = urlparse(url).netloc
            wait = self.min_delay - (time.monotonic() - self._last.get(host, 0))
            if wait > 0:
                time.sleep(wait)
            try:
                r = self.client.request(method, url, params=params, json=json_body, headers=headers)
                status, content, ctype, final = r.status_code, r.content, r.headers.get("content-type", ""), str(r.url)
                recorded_headers = {name: r.headers[name] for name in RECORDED_HEADERS if name in r.headers}
            except httpx.HTTPError as e:
                status, content, ctype, final = 0, str(e).encode(), "error", url
                recorded_headers = {}
            self._last[host] = time.monotonic()
            raw.parent.mkdir(parents=True, exist_ok=True)
            raw.write_bytes(content)
            meta.write_text(json.dumps({"url": final, "status": status, "content_type": ctype,
                                        "headers": recorded_headers}), encoding="utf-8")
            resp = Resp(final, status, content, ctype, False, hashlib.sha256(content).hexdigest(), str(raw))
            resp.headers = recorded_headers
        if self.store is not None and company_id and kind:
            source_url = str(httpx.URL(url).copy_merge_params(params)) if params else url
            resp.doc_id = self.store.add_source_doc(company_id=company_id, url=source_url, kind=kind, status=resp.status,
                                                    content_type=resp.content_type, sha256=resp.sha256,
                                                    raw_path=resp.raw_path, title=title)
        return resp

    def get(self, url: str, **kw) -> Resp:
        return self.request("GET", url, **kw)

    def post(self, url: str, json_body: Any = None, **kw) -> Resp:
        return self.request("POST", url, json_body=json_body, **kw)
