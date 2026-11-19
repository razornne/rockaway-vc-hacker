"""EUFundingCollector: the company's record in the EU Funding & Tenders portal (SEDIA search API).

Matched by registration number (IČO) or VAT, never by name alone when an IČO is known. The record lists every
EU-funded project the organisation takes part in, across programmes: Horizon Europe, European Defence Fund (EDF),
EDIDP, Digital Europe, … CORDIS (public_money) covers only research framework programmes; EDF grants show up here.
Facts: eu_registration, grant_eu (key = project number, same key as CORDIS so signals can de-duplicate),
source_check, source_unavailable. Never raises.
"""
from __future__ import annotations

import json

from dd.collectors.base import Collector, Context
from dd.store import Company, Fact
from dd.verify import _core

SEDIA = "https://api.tech.ec.europa.eu/search-api/prod/rest/search"
ORG_URL = "https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/org-details/{}"
DEFENCE_PROGRAMMES = {"EDF", "EDIDP", "PADR", "EDIRPA", "ASAP", "EDIP"}
VALIDATED = "31042522"


def _first(m: dict, k: str):
    v = m.get(k)
    return v[0] if isinstance(v, list) and v else v


def matches(meta: dict, company: Company) -> bool:
    ico = (company.ico or "").strip()
    if ico:
        reg = str(_first(meta, "esIN_registrationNum") or "").replace(" ", "")
        vat = str(_first(meta, "esST_vat") or "").replace(" ", "")
        return reg == ico or vat.endswith(ico)
    return _core(str(_first(meta, "esIN_name") or "")) == _core(company.name)


def parse_org(meta: dict, company: Company) -> list[Fact]:
    pic = str(_first(meta, "esIN_pic") or "")
    url = ORG_URL.format(pic)
    try:
        projects = json.loads(_first(meta, "esBI_publicProjects") or "[]")
    except (TypeError, ValueError):
        projects = []
    out = [Fact(company_id=company.id, type="eu_registration", key=pic,
                value={"pic": pic, "legal_name": _first(meta, "esIN_name"),
                       "validated": _first(meta, "esST_validationStatus") == VALIDATED,
                       "projects": int(_first(meta, "esNU_noOfProjects") or 0),
                       "first_seen": str(_first(meta, "esDA_FirstIngestDate") or "")[:10] or None},
                source_url=url, extractor="eu_funding")]
    for p in projects if isinstance(projects, list) else []:
        prog = p.get("program") or {}
        abbr = (prog.get("abbreviation") or "").upper()
        num = str(p.get("number") or "")
        if not num:
            continue
        out.append(Fact(
            company_id=company.id, type="grant_eu", key=num,
            value={"programme": abbr or None, "programme_name": prog.get("description"), "acronym": p.get("acronym"),
                   "title": p.get("title"), "call": (p.get("call") or {}).get("abbreviation"),
                   "status": p.get("status"), "defence": abbr in DEFENCE_PROGRAMMES
                   or "defence" in (prog.get("description") or "").lower()},
            source_url=url, snippet=f"{p.get('acronym')}: {p.get('title')} ({abbr})"[:300],
            extractor="eu_funding"))
    return out


class EUFundingCollector(Collector):
    name = "eu_funding"
    sources = ["EU Funding & Tenders portal (SEDIA search API): participant record and projects incl. EDF"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        params = {"apiKey": "SEDIA", "text": company.name, "pageSize": 20, "pageNumber": 1}
        try:
            r = ctx.http.post(SEDIA, params=params, company_id=company.id, kind="api",
                              title=f"EU F&T portal {company.name}")
            if not r.ok:
                return [self.unavailable(company, "eu_ft_portal", SEDIA, f"HTTP {r.status}")]
            results = r.json().get("results") or []
        except Exception as e:
            return [self.unavailable(company, "eu_ft_portal", SEDIA, f"{type(e).__name__}: {e}")]
        orgs = [x.get("metadata") or {} for x in results
                if "ORGANISATION" in ((x.get("metadata") or {}).get("type") or [])]
        hit = [m for m in orgs if matches(m, company)]
        if len(hit) != 1:
            return [Fact(company_id=company.id, type="source_check", key="eu_ft_portal",
                         value={"source": "EU Funding & Tenders portal",
                                "status": "no_records" if not hit else "ambiguous", "candidates": len(hit)},
                         source_url=SEDIA, extractor=self.name)]
        return parse_org(hit[0], company)
