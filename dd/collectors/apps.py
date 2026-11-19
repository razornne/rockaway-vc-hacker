"""AppsCollector: iTunes Search API (seller must match the company); Google Play only if the site links to it."""
from __future__ import annotations

import re
from urllib.parse import urlencode

from dd.collectors.base import Collector, Context
from dd.collectors.code import domain_matches, fetch
from dd.store import Company, Fact

ITUNES = "https://itunes.apple.com/search"


def _norm(s: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower()) if isinstance(s, str) else ""


def seller_matches(item: dict, company: Company) -> bool:
    return _seller_match_confidence(item, company) is not None


def _seller_match_confidence(item: dict, company: Company) -> str | None:
    """Return confidence only for exact publisher identity or a verified company domain."""
    seller = _norm(item.get("sellerName") or item.get("artistName"))
    explicit_seller = _norm(company.hints.get("app_seller"))
    if seller and explicit_seller and seller == explicit_seller:
        return "high"
    if domain_matches(item.get("sellerUrl"), company.domain):
        return "high"
    # An exact company-name match is useful fallback evidence, but legal suffixes and
    # arbitrary prefixes are not normalized away because they cause false positives.
    if seller and seller == _norm(company.name):
        return "medium"
    return None


class AppsCollector(Collector):
    name = "apps"
    sources = ["iTunes Search API", "Google Play (only when linked from the company site)"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        facts: list[Fact] = []
        for fn in (self._itunes, self._play):
            try:
                facts += fn(company, ctx)
            except Exception as e:
                facts.append(self.unavailable(company, fn.__name__.strip("_"), ITUNES, f"{type(e).__name__}: {e}"))
        return facts

    def _itunes(self, company: Company, ctx: Context) -> list[Fact]:
        query = urlencode({"term": company.name, "entity": "software", "limit": 25})
        shown = f"{ITUNES}?{query}"
        r = fetch(ctx, shown, company_id=company.id, kind="itunes")
        if not r.ok:
            return [self.unavailable(company, "itunes", shown, f"HTTP {r.status} {r.text[:100]}")]
        try:
            payload = r.json()
        except (ValueError, TypeError):
            return [self.unavailable(company, "itunes", shown, "invalid JSON response")]
        if not isinstance(payload, dict) or not isinstance(payload.get("results", []), list):
            return [self.unavailable(company, "itunes", shown, "unexpected response shape")]
        facts = []
        for it in payload.get("results", []):
            if not isinstance(it, dict):
                continue
            match_confidence = _seller_match_confidence(it, company)
            if not match_confidence:
                continue
            facts.append(Fact(
                company_id=company.id, type="app", key=f"ios:{it.get('trackId')}",
                value={"name": it.get("trackName"), "seller": it.get("sellerName"), "store": "ios",
                       "released": it.get("releaseDate"), "updated": it.get("currentVersionReleaseDate"),
                       "rating": it.get("averageUserRating"), "ratings_count": it.get("userRatingCount"),
                       "genre": it.get("primaryGenreName"), "bundle_id": it.get("bundleId"),
                       "price": it.get("price"), "version": it.get("version")},
                source_url=it.get("trackViewUrl") or shown, event_date=(it.get("releaseDate") or "")[:10] or None,
                date_precision="day", source_doc_id=r.doc_id, extractor=self.name, confidence=match_confidence))
        return facts

    def _play(self, company: Company, ctx: Context) -> list[Fact]:
        ids: dict[str, tuple[str, int | None]] = {}
        for d in ctx.store.source_docs(company.id):
            if not domain_matches(d["url"], company.domain):
                continue
            p = d["raw_path"]
            if not p or "play.google.com" in (d["url"] or "") or "html" not in (d["content_type"] or ""):
                continue
            try:
                with open(p, "rb") as fh:
                    body = fh.read().decode("utf-8", "replace")
            except OSError:
                continue
            for m in re.finditer(r"play\.google\.com/store/apps/details\?id=([A-Za-z0-9_.]+)", body):
                ids.setdefault(m.group(1), (d["url"], d["id"]))
        facts = []
        for pkg, (found_on, found_doc_id) in ids.items():
            url = f"https://play.google.com/store/apps/details?id={pkg}"
            name = None
            r = fetch(ctx, url, company_id=company.id, kind="play")
            if r.ok:
                m = re.search(r"<title>(.*?)</title>", r.text, re.S)
                name = re.sub(r"\s*-\s*Apps on Google Play.*", "", m.group(1)).strip() if m else None
            else:
                facts.append(self.unavailable(company, "google_play", url, f"HTTP {r.status}"))
            facts.append(Fact(company_id=company.id, type="app", key=f"play:{pkg}",
                              value={"name": name, "store": "play", "package": pkg, "store_url": url,
                                     "linked_from": found_on},
                              # The company's own page supports the existence of the link even if Play blocks us.
                              source_url=url if r.ok and name else found_on,
                              source_doc_id=r.doc_id if r.ok and name else found_doc_id, extractor=self.name,
                              confidence="high" if r.ok and name else "medium"))
        return facts
