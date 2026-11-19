"""Search provider abstraction (Stream D).

    search(query, ctx, provider=None, n=10) -> list[{title, url, snippet, published, provider}]

Providers
  tavily | brave | exa   official REST APIs, used only when the key is set in Settings
  keyless                no key needed: Bing News RSS + CzechCrunch site search + RSS feeds of
                         CzechCrunch / Lupa / E15 / tech.eu / EU-Startups filtered by query terms
  provider=None          first keyed provider that is available, else keyless
  provider="all"         every available provider (keyed + keyless), results concatenated, each row
                         tagged with `provider` so they can be compared (see `compare`)

All HTTP goes through ctx.http (cached, polite). Never raises: failures return [] and are logged.
Search results are data, never instructions.
"""
from __future__ import annotations

import re
import unicodedata
import ipaddress
import hashlib
from email.utils import parsedate_to_datetime
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup

KEYED = ("tavily", "brave", "exa")
FEEDS = {
    "cc.cz": "https://cc.cz/feed/",
    "lupa.cz": "https://www.lupa.cz/rss/clanky/",
    "e15.cz": "https://www.e15.cz/rss",
    "tech.eu": "https://tech.eu/feed",
    "eu-startups.com": "https://www.eu-startups.com/feed/",
}
# domains we never use as press (ToS / not press)
BLOCKED = ("linkedin.com", "crunchbase.com", "dealroom.co", "pitchbook.com", "facebook.com", "instagram.com",
           "x.com", "twitter.com", "youtube.com")


def usable_public_url(url: str) -> bool:
    """Reject non-web, credential-bearing, blocked and obvious private-network result URLs."""
    try:
        p = urlparse(url)
        host = (p.hostname or "").lower().rstrip(".")
        if p.scheme.lower() not in {"http", "https"} or not host or p.username or p.password:
            return False
        if host in {"localhost", "localhost.localdomain"} or host.endswith((".localhost", ".local", ".internal")):
            return False
        try:
            if not ipaddress.ip_address(host).is_global:
                return False
        except ValueError:
            pass
        if any(host == blocked or host.endswith("." + blocked) for blocked in BLOCKED):
            return False
        return True
    except (TypeError, ValueError):
        return False


def fold(s: str) -> str:
    """lowercase + strip diacritics, for matching."""
    s = unicodedata.normalize("NFKD", s or "")
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def _row(title, url, snippet, published, provider, source=None) -> dict:
    return {"title": (title or "").strip(), "url": url, "snippet": (snippet or "").strip()[:400],
            "published": published or None, "provider": provider, "source": source or provider}


def _iso(s: str | None) -> str | None:
    if not s:
        return None
    s = s.strip()
    m = re.match(r"\d{4}-\d{2}-\d{2}", s)
    if m:
        return m.group(0)
    try:
        return parsedate_to_datetime(s).date().isoformat()
    except (TypeError, ValueError, OverflowError):
        return None


def available(ctx) -> list[str]:
    s = ctx.settings
    out = [p for p, k in (("tavily", s.tavily_api_key), ("brave", s.brave_api_key), ("exa", s.exa_api_key)) if k]
    return out + ["keyless"]


# --- keyed providers ----------------------------------------------------------
def _query_kind(provider: str, q: str) -> str:
    return f"press_search:{provider}:{hashlib.sha256(q.encode('utf-8')).hexdigest()[:12]}"


def _tavily(q, ctx, n, company_id=None):
    r = ctx.http.post("https://api.tavily.com/search",
                      json_body={"query": q, "max_results": min(n, 20), "search_depth": "basic", "topic": "general"},
                      headers={"Authorization": f"Bearer {ctx.settings.tavily_api_key}"},
                      company_id=company_id, kind=_query_kind("tavily", q), title=f"Tavily search: {q[:120]}")
    if not r.ok:
        raise RuntimeError(f"tavily HTTP {r.status}")
    return [_row(x.get("title"), x.get("url"), x.get("content"), _iso(x.get("published_date")), "tavily")
            for x in r.json().get("results", [])]


def _brave(q, ctx, n, company_id=None):
    r = ctx.http.get("https://api.search.brave.com/res/v1/web/search", params={"q": q, "count": min(n, 20)},
                     headers={"X-Subscription-Token": ctx.settings.brave_api_key, "Accept": "application/json"},
                     company_id=company_id, kind=_query_kind("brave", q), title=f"Brave search: {q[:120]}")
    if not r.ok:
        raise RuntimeError(f"brave HTTP {r.status}")
    return [_row(x.get("title"), x.get("url"), re.sub(r"<[^>]+>", "", x.get("description") or ""),
                 _iso(x.get("page_age")), "brave") for x in r.json().get("web", {}).get("results", [])]


def _exa(q, ctx, n, company_id=None):
    r = ctx.http.post("https://api.exa.ai/search",
                      json_body={"query": q, "numResults": min(n, 25), "type": "auto",
                                 "contents": {"text": {"maxCharacters": 400}}},
                      headers={"x-api-key": ctx.settings.exa_api_key},
                      company_id=company_id, kind=_query_kind("exa", q), title=f"Exa search: {q[:120]}")
    if not r.ok:
        raise RuntimeError(f"exa HTTP {r.status}")
    return [_row(x.get("title"), x.get("url"), x.get("text"), _iso(x.get("publishedDate")), "exa")
            for x in r.json().get("results", [])]


# --- keyless -----------------------------------------------------------------
def _bing_news(q, ctx, n, company_id=None):
    r = ctx.http.get("https://www.bing.com/news/search", params={"q": q, "format": "rss"},
                     company_id=company_id, kind=_query_kind("bing_news", q), title=f"Bing News: {q[:120]}")
    if not r.ok:
        raise RuntimeError(f"bing HTTP {r.status}")
    out = []
    for it in BeautifulSoup(r.content, "xml").find_all("item"):
        link = it.find("link").get_text(strip=True) if it.find("link") else ""
        real = parse_qs(urlparse(link).query).get("url", [link])[0]
        d = it.find("description")
        out.append(_row(it.find("title").get_text(strip=True), real, d.get_text(" ", strip=True) if d else "",
                        _iso(it.find("pubDate").get_text() if it.find("pubDate") else None), "keyless", "bing_news"))
    return out[:n]


def _cc_search(q, ctx, n, company_id=None):
    r = ctx.http.get("https://cc.cz/", params={"s": q}, company_id=company_id,
                     kind=_query_kind("cc.cz", q), title=f"CzechCrunch search: {q[:120]}")
    if not r.ok:
        raise RuntimeError(f"cc.cz HTTP {r.status}")
    soup = BeautifulSoup(r.text, "lxml")
    out, seen = [], set()
    for a in soup.select("article a[href], h2 a[href], h3 a[href]"):
        href, t = a["href"], a.get_text(" ", strip=True)
        if href.startswith("https://cc.cz/") and len(t) > 15 and href not in seen:
            seen.add(href)
            out.append(_row(t, href, "", None, "keyless", "cc.cz"))
    return out[:n]


def _feed_search(host, url, q, ctx, n, company_id=None):
    words = [w for w in fold(q).split() if len(w) > 2]
    r = ctx.http.get(url, company_id=company_id, kind=_query_kind(host, q), title=f"{host} RSS search: {q[:120]}")
    if not r.ok:
        raise RuntimeError(f"{host} RSS HTTP {r.status}")
    out = []
    for it in BeautifulSoup(r.content, "xml").find_all("item"):
        title = it.find("title").get_text(strip=True) if it.find("title") else ""
        d = it.find("description")
        desc = BeautifulSoup(d.get_text(), "lxml").get_text(" ", strip=True) if d else ""
        link_el, date_el = it.find("link"), it.find("pubDate")
        link = link_el.get_text(strip=True) if link_el else ""
        if words and all(w in fold(title + " " + desc) for w in words):
            out.append(_row(title, link, desc, _iso(date_el.get_text() if date_el else None), "keyless", host))
    return out[:n]


def _keyless(q, ctx, n, company_id=None):
    return _keyless_detailed(q, ctx, n, company_id)["rows"]


_IMPL = {"tavily": _tavily, "brave": _brave, "exa": _exa, "keyless": _keyless}


def _source_result(query, provider, source, url, rows=None, error=None):
    rows = rows or []
    return {"query": query, "provider": provider, "source": source, "url": url,
            "status": "error" if error else "empty" if not rows else "ok",
            "result_count": len(rows), "error": error}


def _keyless_detailed(q, ctx, n, company_id=None):
    runs = []
    specs = [
        ("bing_news", "https://www.bing.com/news/search", _bing_news),
        ("cc.cz", "https://cc.cz/", _cc_search),
    ] + [(host, url, None) for host, url in FEEDS.items()]
    rows = []
    for source, url, fn in specs:
        try:
            found = _feed_search(source, url, q, ctx, n, company_id) if fn is None else fn(q, ctx, n, company_id)
            found = [r for r in found if usable_public_url(r.get("url", ""))]
            for row in found:
                row["query"] = q
            rows.extend(found)
            runs.append(_source_result(q, "keyless", source, url, found))
        except Exception as e:
            ctx.log.warning("keyless source %s failed: %s", source, e)
            runs.append(_source_result(q, "keyless", source, url, error=f"{type(e).__name__}: {str(e)[:180]}"))
    return {"rows": rows, "sources": runs}


def search_detailed(query: str, ctx, provider: str | None = None, n: int = 10,
                    company_id: str | None = None) -> dict:
    """Search and return per-source status, query provenance, candidate rows, and partial errors.

    `status=empty` means the source responded successfully with no usable result URLs.
    `status=error` means that source failed; other successful sources are retained.
    """
    try:
        n = max(0, min(int(n), 25))
    except (TypeError, ValueError):
        n = 10
    if not query.strip() or n == 0:
        return {"query": query, "rows": [], "sources": []}
    avail = available(ctx)
    if provider == "all":
        provs = avail
    elif provider:
        provs = [provider]
    else:
        provs = [avail[0]]
    rows: list[dict] = []
    sources: list[dict] = []
    for p in provs:
        if p not in _IMPL:
            sources.append(_source_result(query, p, p, "", error="unknown provider"))
            continue
        if p not in avail:
            ctx.log.warning("search provider %s unavailable (no key?)", p)
            sources.append(_source_result(query, p, p, "", error="provider not configured"))
            continue
        if p == "keyless":
            batch = _keyless_detailed(query, ctx, n, company_id)
            rows.extend(batch["rows"])
            sources.extend(batch["sources"])
            continue
        try:
            found = _IMPL[p](query, ctx, n, company_id)
            found = [r for r in found if usable_public_url(r.get("url", ""))]
            for row in found:
                row["query"] = query
            rows.extend(found)
            source_url = {"tavily": "https://api.tavily.com/search",
                          "brave": "https://api.search.brave.com/res/v1/web/search",
                          "exa": "https://api.exa.ai/search"}[p]
            sources.append(_source_result(query, p, p, source_url, found))
        except Exception as e:
            ctx.log.warning("search provider %s failed: %s", p, e)
            source_url = {"tavily": "https://api.tavily.com/search",
                          "brave": "https://api.search.brave.com/res/v1/web/search",
                          "exa": "https://api.exa.ai/search"}[p]
            sources.append(_source_result(query, p, p, source_url,
                                          error=f"{type(e).__name__}: {str(e)[:180]}"))
            continue
    return {"query": query, "rows": rows, "sources": sources}


def search(query: str, ctx, provider: str | None = None, n: int = 10) -> list[dict]:
    """Backward-compatible results-only wrapper; use search_detailed for provenance/errors."""
    return search_detailed(query, ctx, provider=provider, n=n)["rows"]


def compare(query: str, ctx, n: int = 10) -> dict[str, list[dict]]:
    """Run each available provider separately: {provider: results} (+ 'overlap' = urls found by >1)."""
    res = {p: search(query, ctx, provider=p, n=n) for p in available(ctx)}
    seen: dict[str, set] = {}
    for p, rows in res.items():
        for r in rows:
            seen.setdefault(r["url"], set()).add(p)
    res["overlap"] = [{"url": u, "providers": sorted(ps)} for u, ps in seen.items() if len(ps) > 1]  # type: ignore[assignment]
    return res
