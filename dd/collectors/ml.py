"""MLCollector: Hugging Face models/datasets by author + OpenAlex works with the company in the affiliation."""
from __future__ import annotations

import re
from urllib.parse import urlencode

from dd.collectors.base import Collector, Context
from dd.collectors.code import domain_matches, fetch
from dd.store import Company, Fact

HF = "https://huggingface.co/api"
OA = "https://api.openalex.org/works"


def slugs(company: Company) -> list[str]:
    out: list[str] = []
    gh = company.hints.get("github_org")
    base = re.sub(r"[^a-z0-9]+", "", company.name.lower())
    dash = re.sub(r"[^a-z0-9]+", "-", company.name.lower()).strip("-")
    label = (company.domain or "").split(".")[0] if company.domain else ""
    for s in [gh, company.id, dash, base, label]:
        if isinstance(s, str) and s and s.lower() not in [o.lower() for o in out]:
            out.append(s)
    return out


def hf_candidates(company: Company) -> list[tuple[str, str]]:
    """Return candidate namespaces with the evidence used to derive each one."""
    name = company.name
    candidates = [
        (company.hints.get("hf_author") or company.hints.get("huggingface_org"), "explicit_hint"),
        (company.hints.get("github_org"), "github_org_slug_guess"),
        (company.id, "company_id_guess"),
        (re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-"), "company_name_guess"),
        (re.sub(r"[^a-z0-9]+", "", name.lower()), "company_name_compact_guess"),
        ((company.domain or "").split(".")[0], "domain_label_guess"),
    ]
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for value, method in candidates:
        if isinstance(value, str) and value and value.lower() not in seen:
            out.append((value, method))
            seen.add(value.lower())
    return out


def profile_matches_domain(item: dict, company: Company) -> bool:
    profile = item.get("authorData")
    if not isinstance(profile, dict):
        return False
    for key in ("website", "webUrl", "url", "blog", "homepage"):
        value = profile.get(key)
        if isinstance(value, str) and domain_matches(value, company.domain):
            return True
    return False


def name_in(text: str, name: str) -> bool:
    n = re.escape(name.strip()).replace(r"\ ", r"[\s\-]?")
    return re.search(rf"(?<![A-Za-z0-9]){n}(?![A-Za-z0-9])", text, re.I) is not None


def _failed(r) -> bool:
    return r.status == 0 or r.status >= 500 or r.status in (403, 429)


class MLCollector(Collector):
    name = "ml"
    sources = ["Hugging Face API", "OpenAlex"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        facts: list[Fact] = []
        for fn, source, url in ((self._hf, "huggingface", HF), (self._openalex, "openalex", OA)):
            try:
                facts += fn(company, ctx)
            except Exception as e:
                facts.append(self.unavailable(company, source, url, f"{type(e).__name__}: {e}"))
        return facts

    def _hf(self, company: Company, ctx: Context) -> list[Fact]:
        facts: list[Fact] = []
        for author, candidate_method in hf_candidates(company):
            for kind in ("models", "datasets"):
                query = urlencode({"author": author, "limit": 50})
                url = f"{HF}/{kind}?{query}"
                shown = url
                r = fetch(ctx, url, company_id=company.id, kind=f"hf_{kind}")
                if _failed(r):
                    facts.append(self.unavailable(company, "huggingface", shown, f"HTTP {r.status} {r.text[:100]}"))
                    continue
                if not r.ok:
                    continue
                try:
                    items = r.json()
                except (ValueError, TypeError):
                    facts.append(self.unavailable(company, "huggingface", shown, "invalid JSON response"))
                    continue
                if not isinstance(items, list):
                    facts.append(self.unavailable(company, "huggingface", shown, "unexpected response shape"))
                    continue
                for it in items:
                    if not isinstance(it, dict):
                        continue
                    mid = it.get("id") or ""
                    if not isinstance(mid, str):
                        continue
                    if mid.split("/")[0].lower() != author.lower():  # exact author match only
                        continue
                    profile_match = profile_matches_domain(it, company)
                    verified = candidate_method == "explicit_hint" or profile_match
                    match_method = "profile_website" if profile_match else candidate_method
                    facts.append(Fact(
                        company_id=company.id, type="hf_model", key=mid, source_doc_id=r.doc_id,
                        value={"kind": kind[:-1], "author": author, "downloads": it.get("downloads"),
                               "likes": it.get("likes"), "pipeline_tag": it.get("pipeline_tag"),
                               "created_at": it.get("createdAt"), "tags": (it.get("tags") or [])[:10],
                               "match_method": match_method, "identity_unverified": not verified},
                        source_url=f"https://huggingface.co/{'datasets/' if kind == 'datasets' else ''}{mid}",
                        event_date=(it.get("createdAt") or "")[:10] or None, date_precision="day",
                        extractor=self.name, confidence="high" if verified else "medium"))
        return facts

    def _openalex(self, company: Company, ctx: Context) -> list[Fact]:
        name = company.name
        query = urlencode({"filter": f"raw_affiliation_strings.search:{name}", "per-page": 10})
        shown = f"{OA}?{query}"
        r = fetch(ctx, shown, company_id=company.id, kind="openalex")
        if _failed(r) or not r.ok:
            return [self.unavailable(company, "openalex", shown, f"HTTP {r.status} {r.text[:100]}")]
        try:
            payload = r.json()
        except (ValueError, TypeError):
            return [self.unavailable(company, "openalex", shown, "invalid JSON response")]
        if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
            return [self.unavailable(company, "openalex", shown, "unexpected response shape")]
        facts = []
        for w in payload["results"]:
            if not isinstance(w, dict):
                continue
            hit = None
            authorships = w.get("authorships", [])
            if not isinstance(authorships, list):
                continue
            for a in authorships:
                if not isinstance(a, dict):
                    continue
                affiliations = a.get("raw_affiliation_strings") or []
                if not isinstance(affiliations, list):
                    continue
                for s in affiliations:
                    if isinstance(s, str) and name_in(s, name):
                        hit = s
                        break
                if hit:
                    break
            if not hit:
                continue
            primary = w.get("primary_location")
            loc = (primary.get("source") or {}) if isinstance(primary, dict) else {}
            if not isinstance(loc, dict):
                loc = {}
            wid = w.get("id") or ""
            if not isinstance(wid, str):
                wid = ""
            doi = w.get("doi") if isinstance(w.get("doi"), str) else None
            title = w.get("title") if isinstance(w.get("title"), str) else None
            paper_key = wid.rsplit("/", 1)[-1] or doi or title or shown
            facts.append(Fact(
                company_id=company.id, type="paper", key=paper_key,
                value={"title": title, "venue": loc.get("display_name"), "year": w.get("publication_year"),
                       "doi": doi, "cited_by": w.get("cited_by_count"), "affiliation": hit},
                source_url=wid or shown,
                event_date=w.get("publication_date") if isinstance(w.get("publication_date"), str) else None,
                date_precision="day",
                snippet=hit, source_doc_id=r.doc_id, extractor=self.name, confidence="medium"))
        return facts
