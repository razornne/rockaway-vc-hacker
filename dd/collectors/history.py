"""HistoryCollector: Wayback CDX first captures of the domain and key paths (flaky -> 60 s timeout, bounded retries)."""
from __future__ import annotations

import json
from collections import Counter
from contextlib import contextmanager
from urllib.parse import urlencode, urlparse

from dd.collectors.base import Collector, Context
from dd.collectors.code import fetch
from dd.store import Company, Fact

CDX = "https://web.archive.org/cdx/search/cdx"
PATHS = ["/pricing", "/careers", "/jobs", "/customers", "/docs", "/blog"]
MAX_FAILS = 3


@contextmanager
def timeout(ctx: Context, seconds: float):
    old = ctx.http.client.timeout
    ctx.http.client.timeout = seconds
    try:
        yield
    finally:
        ctx.http.client.timeout = old


def parse_cdx(text: str) -> list[dict]:
    try:
        rows = json.loads(text)
    except Exception:
        return []
    if not rows or not isinstance(rows, list) or not isinstance(rows[0], list):
        return []
    head, body = rows[0], rows[1:]
    if not all(isinstance(h, str) for h in head):
        return []
    return [dict(zip(head, r)) for r in body if isinstance(r, list) and len(r) == len(head)]


def ts_date(ts: str) -> str:
    return f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"


class HistoryCollector(Collector):
    name = "history"
    sources = ["Wayback Machine CDX API"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        if not company.domain:
            return []
        try:
            return self._collect(company, ctx)
        except Exception as e:
            return [self.unavailable(company, "wayback", CDX, f"{type(e).__name__}: {e}")]

    def _query(self, ctx: Context, company: Company, params: dict):
        """Returns (rows | None, shown_url, error). None means the query failed."""
        # Put the query in the URL so the shared HTTP source-doc index retains each distinct CDX request.
        shown = f"{CDX}?{urlencode(params)}"
        r = fetch(ctx, shown, company_id=company.id, kind="wayback_cdx")
        if not r.ok:
            return None, shown, f"HTTP {r.status} {r.text[:100] if r.status == 0 else ''}".strip()
        try:
            payload = json.loads(r.text)
        except (ValueError, TypeError):
            return None, shown, "invalid JSON response"
        if not isinstance(payload, list) or (payload and not isinstance(payload[0], list)):
            return None, shown, "unexpected CDX response shape"
        rows = parse_cdx(r.text)
        if payload and not rows:
            return None, shown, "malformed CDX rows"
        return rows, shown, ""

    def _collect(self, company: Company, ctx: Context) -> list[Fact]:
        raw_domain = company.domain.strip().lower()
        d = (urlparse(raw_domain).hostname if "://" in raw_domain else raw_domain) or ""
        d = d.removeprefix("www.").rstrip(".")
        if not d or "/" in d:
            return [self.unavailable(company, "wayback", CDX, "company domain is invalid")]
        facts: list[Fact] = []
        fails = 0
        targets = [("domain", d)] + [(p, f"{d}{p}*") for p in PATHS]
        with timeout(ctx, 60):
            for key, pattern in targets:
                if fails >= MAX_FAILS:
                    facts.append(self.unavailable(company, "wayback", CDX, "aborted after repeated failures"))
                    break
                best = None
                for host in (pattern, f"www.{pattern}"):
                    params = {"url": host, "output": "json", "limit": 20, "collapse": "urlkey",
                              "fl": "timestamp,original,statuscode", "filter": "statuscode:200"}
                    rows, shown, err = self._query(ctx, company, params)
                    if rows is None:
                        fails += 1
                        facts.append(self.unavailable(company, f"wayback:{key}", shown, err))
                        continue
                    fails = 0
                    for row in rows:
                        ts = row.get("timestamp", "")
                        if len(ts) < 8 or not ts[:8].isdigit() or not row.get("original"):
                            continue
                        if best is None or ts < best["timestamp"]:
                            best = row
                if best:
                    ts = best["timestamp"]
                    facts.append(Fact(
                        company_id=company.id, type="wayback_first", key=key,
                        value={"timestamp": ts, "original": best["original"]},
                        source_url=f"https://web.archive.org/web/{ts}/{best['original']}",
                        event_date=ts_date(ts), date_precision="day", extractor=self.name))
            # distinct months with a capture, per year (cheap activity proxy)
            counts: Counter = Counter()
            for host in (d, f"www.{d}"):
                rows, shown, err = self._query(ctx, company, {"url": host, "output": "json", "fl": "timestamp",
                                                              "collapse": "timestamp:6", "filter": "statuscode:200"})
                if rows is None:
                    facts.append(self.unavailable(company, "wayback:captures_by_year", shown, err))
                    continue
                counts.update(r["timestamp"][:4] for r in rows
                              if len(r.get("timestamp", "")) >= 6 and r["timestamp"][:6].isdigit())
            if counts:
                facts.append(Fact(company_id=company.id, type="wayback_first", key="captures_by_year",
                                  value={"months_with_capture": dict(sorted(counts.items()))},
                                  source_url=f"https://web.archive.org/web/*/{d}", extractor=self.name))
        return facts
