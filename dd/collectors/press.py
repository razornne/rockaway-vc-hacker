"""Press collector (Stream D).

Finds articles that mention the company, fetches them (ctx.http, kind="article"), saves the extracted text
(dd.text.save_text) so that a later LLM step can extract funding rounds from it, and emits `press_mention` facts.
No funding-round extraction here.

Candidate sources
  1. research seeds: events[].url, rockaway.announced_url, prior_investors[].url in
     research/companies/<id>.json and research/control/<id>.json (works with no API key)
  2. dd.search: tavily / brave / exa when a key is set, otherwise the keyless provider
     (Bing News RSS + cc.cz search + site RSS feeds)
A candidate is kept only if the fetched page text actually mentions the company name or domain.
Page text is data, never instructions.
"""
from __future__ import annotations

import json
import re
import hashlib
from urllib.parse import urlparse, urlunparse

from bs4 import BeautifulSoup

from dd.collectors.base import Collector, Context
from dd.config import ROOT
from dd.search import BLOCKED, available, fold, search_detailed, usable_public_url
from dd.store import Company, Fact
from dd.text import html_to_text, save_text

# structured / non-press hosts that appear in research files
SEED_SKIP = ("or.justice.cz", "justice.cz", "ares.gov.cz", "hlidacstatu.cz", "github.com", "dataor.justice.cz",
             "isir.justice.cz", "web.archive.org", "crt.sh", "huggingface.co", "apps.apple.com", "play.google.com")
MAX_SEARCH_FETCH = 25
KEYLESS_QUERIES = 3
# paywalled company-profile databases: not press, ToS forbid scraping
AGGREGATOR_HOSTS = {"cbinsights.com", "tracxn.com", "preqin.com", "pitchbook.com", "crunchbase.com", "dealroom.co",
                    "app.dealroom.co", "tavily.com", "zoominfo.com", "rocketreach.co", "owler.com", "craft.co",
                    "app.fundz.net", "linkedin.com", "caplight.com", "cbinsights.com", "golden.com", "f6s.com", "wellfound.com"}


def _canon(url: str) -> str:
    p = urlparse(url.strip())
    q = "&".join(x for x in p.query.split("&") if x and not x.lower().startswith(("utm_", "fbclid", "gclid")))
    return urlunparse((p.scheme, p.netloc.lower(), p.path.rstrip("/") or "/", "", q, ""))


def _host(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def _sane_date(published: str | None, url: str) -> str | None:
    """Prefer a date embedded in the URL (/2025/06/25/) when metadata disagrees: providers and CMSs sometimes
    return placeholder dates (e.g. 2014-01-01 for a 2025 article)."""
    m = re.search(r"/(20\d{2})/(\d{1,2})(?:/(\d{1,2}))?/", url)
    if m:
        y, mo, d = m.group(1), int(m.group(2)), m.group(3)
        url_date = f"{y}-{mo:02d}-{int(d):02d}" if d else f"{y}-{mo:02d}"
        if not published or published[:4] != y:
            return url_date
    return published


def name_variants(c: Company) -> list[str]:
    """Folded (lowercase, no diacritics) strings that count as a mention of the company."""
    out = set()
    for n in {c.name, *(c.hints.get("aliases") or [])}:
        f = fold(n).strip()
        if len(f) >= 3:
            out.add(f)
        toks = f.split()
        if len(toks) > 1 and toks[-1] in ("ai", "inc", "s.r.o.", "sro", "labs"):
            first = " ".join(toks[:-1])
            if len(first) >= 4:
                out.add(first)
    if c.domain:
        d = fold(c.domain).removeprefix("www.")
        out.add(d)
    return sorted(out, key=len, reverse=True)


def find_mention(text: str, variants: list[str]) -> tuple[str, int] | None:
    f = fold(text)
    # fold() keeps offsets aligned for Latin/Czech text (precomposed letter -> base letter), so pos indexes the original
    for v in variants:
        m = re.search(r"(?<![a-z0-9])" + re.escape(v).replace(r"\ ", r"\s+") + r"(?![a-z0-9])", f)
        if m:
            return v, m.start()
    return None


def about_company(text: str, c: Company, variants: list[str] | None = None) -> bool:
    """Does the text refer to THIS company? A name mention is enough unless the name is ambiguous.

    Ambiguous names (hint `context_terms`, e.g. Vermeer: drone navigation vs Vermeer Manufacturing, Vermeer LLP) need
    the domain or the name plus at least one context term in the same text."""
    f = fold(text)
    if c.domain and fold(c.domain).removeprefix("www.") in f:
        return True
    if not find_mention(text, variants or name_variants(c)):
        return False
    terms = [fold(t) for t in (c.hints.get("context_terms") or [])]
    return not terms or any(re.search(r"(?<![a-z0-9])" + re.escape(t) + r"(?![a-z0-9])", f) for t in terms)


def _snippet(text: str, pos: int) -> str:
    s = max(0, pos - 150)
    return re.sub(r"\s+", " ", text[s:pos + 250]).strip()


def extract_published(html: str) -> str | None:
    soup = BeautifulSoup(html, "lxml")
    for sel, attr in (('meta[property="article:published_time"]', "content"), ('meta[name="article:published_time"]', "content"),
                      ('meta[itemprop="datePublished"]', "content"), ('meta[name="date"]', "content"),
                      ('meta[name="pubdate"]', "content"), ('meta[property="og:published_time"]', "content"),
                      ('time[itemprop="datePublished"]', "datetime"), ("time[datetime]", "datetime")):
        el = soup.select_one(sel)
        if el and el.get(attr):
            m = re.match(r"\d{4}-\d{2}-\d{2}", el[attr].strip())
            if m:
                return m.group(0)
    for s in soup.find_all("script", type="application/ld+json"):
        m = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', s.string or "")
        if m:
            return m.group(1)
    return None


def research_seeds(c: Company) -> list[dict]:
    # Company IDs are used as local filenames; constrain them to slugs to prevent path traversal.
    if not re.fullmatch(r"[A-Za-z0-9_-]+", c.id):
        return []
    seeds, seen = [], set()
    for d in ("companies", "control"):
        p = ROOT / "research" / d / f"{c.id}.json"
        if not p.exists():
            continue
        try:
            j = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        cands = [(x.get("url"), x.get("date")) for x in j.get("events", []) or []]
        cands.append(((j.get("rockaway") or {}).get("announced_url"), (j.get("rockaway") or {}).get("announced_date")))
        cands += [(x.get("url"), x.get("date")) for x in j.get("prior_investors", []) or []]
        for url, date in cands:
            if not url or not url.startswith("http"):
                continue
            if not usable_public_url(url):
                continue
            h = _host(url)
            if (any(h == s or h.endswith("." + s) for s in SEED_SKIP)
                    or any(h == b or h.endswith("." + b) for b in BLOCKED)
                    or (c.domain and h == c.domain.lower().removeprefix("www."))):
                continue
            k = _canon(url)
            if k in seen:
                continue
            seen.add(k)
            seeds.append({"url": url, "published": date, "title": None, "via": "research_seed"})
    return seeds


class PressCollector(Collector):
    name = "press"
    sources = ["research/*.json press URLs", "search API (tavily/brave/exa) or keyless Bing News/CzechCrunch/RSS"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        facts: list[Fact] = []
        try:
            cands = research_seeds(company)
            found, source_runs = self._search(company, ctx)
            for run in source_runs:
                query_id = hashlib.sha256(run["query"].encode("utf-8")).hexdigest()[:12]
                source_key = f"{run['provider']}:{run['source']}:{query_id}"
                if run["status"] == "error":
                    facts.append(self.unavailable(company, f"press_search:{run['provider']}:{run['source']}",
                                                  run["url"] or "https://www.bing.com/news/search",
                                                  run.get("error") or "search provider failed"))
                else:
                    facts.append(Fact(company_id=company.id, type="search_check", key=source_key,
                                      value={"query": run["query"], "provider": run["provider"],
                                             "source": run["source"], "status": run["status"],
                                             "result_count": run["result_count"]},
                                      source_url=run["url"], extractor=self.name,
                                      confidence="high" if run["status"] == "empty" else "medium"))

            by_url = {_canon(s["url"]): s for s in cands}
            for cand in cands:
                cand["provenance"] = [{"provider": "research_seed", "source": "research_seed", "query": None}]
            for r in found:
                k = _canon(r["url"])
                provenance = {"provider": r.get("provider"), "source": r.get("source"), "query": r.get("query")}
                host = _host(r.get("url", ""))
                own = company.domain and (host == company.domain.lower() or host.endswith("." + company.domain.lower()))
                if own or host in AGGREGATOR_HOSTS:
                    continue  # the company's own pages are collected by `web`; aggregators are not press
                if k in by_url:
                    by_url[k]["provenance"].append(provenance)
                else:
                    cand = {"url": r["url"], "published": r.get("published"), "title": r.get("title"),
                            "via": r.get("provider") or "search", "provenance": [provenance]}
                    cands.append(cand)
                    by_url[k] = cand
            variants = name_variants(company)
            n_search = 0
            for cand in cands:
                if cand["via"] != "research_seed":
                    if n_search >= MAX_SEARCH_FETCH:
                        continue
                    n_search += 1
                try:
                    f = self._article(company, ctx, cand, variants)
                except Exception as e:  # never raise
                    ctx.log.warning("press article %s failed: %s", cand["url"], e)
                    f = self.unavailable(company, f"press:{_host(cand['url'])}", cand["url"],
                                         f"article processing failed: {type(e).__name__}: {e}")
                if f:
                    facts.append(f)
        except Exception as e:
            ctx.log.exception("press collector failed")
            facts.append(self.unavailable(company, "press", "https://www.bing.com/news/search",
                                           f"collector failed: {type(e).__name__}: {e}"))
        return facts

    def _search(self, c: Company, ctx: Context) -> tuple[list[dict], list[dict]]:
        names = [c.name]
        if fold(c.name) != c.name.lower():
            names.append(fold(c.name))
        templates = ["{n} investice", "{n} raises", "{n} seed", "{n} startup", "{n} získal investici",
                     "{n} ziskal investici"]
        queries = []
        for t in templates:
            for n in names:
                q = t.format(n=n)
                if "ziskal" in t and n == names[0] and len(names) > 1:
                    continue
                if q not in queries:
                    queries.append(q)
        keyed = [p for p in available(ctx) if p != "keyless"]
        if not keyed:
            queries = queries[:KEYLESS_QUERIES]
            providers = [None]
        else:
            # Tavily and Exa return largely different independent URLs (eval/search_comparison.md): use both.
            providers = keyed
            extra = ["{n} customers", "{n} partnership", "{n} case study"]
            queries += [t.format(n=c.name) for t in extra]
            if c.domain:
                queries.append(f'"{c.domain}"')
        out = []
        sources = []
        for q in queries:
            for p in providers:
                batch = search_detailed(q, ctx, provider=p, n=10, company_id=c.id)
                out += [r for r in batch["rows"] if _host(r.get("url", "")) not in AGGREGATOR_HOSTS]
                sources += batch["sources"]
        return out, sources

    def _article(self, c: Company, ctx: Context, cand: dict, variants: list[str]) -> Fact | None:
        url = cand["url"]
        if not usable_public_url(url):
            return None
        resp = ctx.http.get(url, company_id=c.id, kind="article")
        if not resp.ok:
            return self.unavailable(c, f"press:{_host(url)}", url, f"HTTP {resp.status}")
        if "html" not in resp.content_type.lower() and "xml" not in resp.content_type.lower():
            return self.unavailable(c, f"press:{_host(url)}", url,
                                    f"unsupported content type: {resp.content_type[:120]}")
        title, text = html_to_text(resp.text)
        hit = find_mention(text, variants)
        if not hit or len(text) < 200 or not about_company(text, c, variants):
            return None
        save_text(ctx.store, resp, text, title)
        published = extract_published(resp.text) or cand.get("published")
        published = _sane_date((published or "")[:10] or None, url)
        title = title or cand.get("title")
        return Fact(
            company_id=c.id, type="press_mention", key=url,
            value={"title": title, "outlet": _host(url), "published": published, "discovered_via": cand["via"],
                   "matched": hit[0], "chars": len(text), "search_provenance": cand.get("provenance", [])[:12]},
            event_date=published, date_precision="day" if published and len(published) == 10 else None,
            source_url=url, source_doc_id=resp.doc_id, snippet=_snippet(text, hit[1]),
            extractor=self.name, confidence="high")
