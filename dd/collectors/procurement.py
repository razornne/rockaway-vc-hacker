"""ProcurementCollector: EU public procurement notices (TED, Tenders Electronic Daily) naming the company.

TED API v3 (anonymous search). A full-text match is not proof of a contract, so each notice gets a role:
  winner / tenderer — the company's IČO or name is in the winner / tenderer fields (eForms notices, Nov 2023+);
  mentioned         — the company appears only in the notice text (older notices do not expose these fields).
Defence buyers (ministries of defence, armed forces, NSPA, …) and CPV division 35 (security and defence
equipment) are flagged, because a government defence customer is the strongest dual-use signal there is.
Facts: public_tender, source_check, source_unavailable. Never raises.
"""
from __future__ import annotations

import re

from dd.collectors.base import Collector, Context
from dd.store import Company, Fact
from dd.verify import _core

TED = "https://api.ted.europa.eu/v3/notices/search"
FIELDS = ["publication-number", "publication-date", "notice-type", "buyer-name", "buyer-country", "notice-title",
          "winner-name", "winner-identifier", "organisation-name-tenderer", "organisation-identifier-tenderer",
          "total-value", "total-value-cur", "classification-cpv", "contract-conclusion-date"]
DEFENCE_BUYER = re.compile(
    r"obrany|defen[cs]e|armád|vojensk|military|armed forces|\bNSPA\b|\bNATO\b|european defence agency|bundeswehr|"
    r"verteidigung|ministère des armées|\bDGA\b|obrony|forsvar|puolustus|aizsardz|krašto apsaugos|kaitseministeerium",
    re.I)
NOTICE_URL = "https://ted.europa.eu/en/notice/-/detail/{}"


def _vals(x) -> list[str]:
    """TED fields are a scalar, a list, or a {language: [values]} dict."""
    if x is None:
        return []
    if isinstance(x, dict):
        for lang in ("eng", "ces"):
            if lang in x:
                return _vals(x[lang])
        return [v for vs in x.values() for v in _vals(vs)]
    if isinstance(x, list):
        return [str(v) for v in x if v not in (None, "")]
    return [str(x)]


def _title(n: dict) -> str | None:
    t = _vals(n.get("notice-title"))
    return t[0] if t else None


def role(notice: dict, company: Company) -> str:
    ico = (company.ico or "").strip()
    core = _core(company.name)
    if ico and ico in _vals(notice.get("winner-identifier")):
        return "winner"
    if core and any(_core(w) == core for w in _vals(notice.get("winner-name"))):
        return "winner"
    if ico and ico in _vals(notice.get("organisation-identifier-tenderer")):
        return "tenderer"
    if core and any(_core(w) == core for w in _vals(notice.get("organisation-name-tenderer"))):
        return "tenderer"
    return "mentioned"


def is_defence(notice: dict) -> bool:
    buyers = " ".join(_vals(notice.get("buyer-name")))
    cpv = _vals(notice.get("classification-cpv"))
    return bool(DEFENCE_BUYER.search(buyers)) or any(c.startswith("35") for c in cpv)


def parse_notices(data: dict, company: Company) -> list[Fact]:
    out = []
    for n in data.get("notices") or []:
        num = n.get("publication-number")
        if not num:
            continue
        r = role(n, company)
        date = (_vals(n.get("contract-conclusion-date")) or _vals(n.get("publication-date")) or [None])[0]
        date = date[:10] if date else None
        value = n.get("total-value") if r == "winner" else None
        cur = (_vals(n.get("total-value-cur")) or [None])[0]
        out.append(Fact(
            company_id=company.id, type="public_tender", key=num,
            value={"notice": num, "notice_type": n.get("notice-type"), "role": r,
                   "buyer": "; ".join(_vals(n.get("buyer-name"))[:2]) or None,
                   "buyer_country": (_vals(n.get("buyer-country")) or [None])[0],
                   "title": _title(n), "value": value, "currency": cur if value is not None else None,
                   "cpv": _vals(n.get("classification-cpv"))[:3], "defence_buyer": is_defence(n)},
            event_date=date, date_precision="day" if date else None,
            source_url=NOTICE_URL.format(num),
            snippet=f"{_title(n) or ''} — buyer: {'; '.join(_vals(n.get('buyer-name'))[:1])}"[:300],
            extractor="procurement", confidence="high" if r != "mentioned" else "medium"))
    return out


class ProcurementCollector(Collector):
    name = "procurement"
    sources = ["TED API v3 (EU public procurement notices)"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        terms = [f'FT~"{company.name}"'] + ([f'FT~"{company.ico}"'] if company.ico else [])
        body = {"query": " OR ".join(terms), "fields": FIELDS, "limit": 100}
        try:
            r = ctx.http.post(TED, json_body=body, company_id=company.id, kind="api", title=f"TED {company.name}")
            if not r.ok:
                return [self.unavailable(company, "ted", TED, f"HTTP {r.status}")]
            data = r.json()
        except Exception as e:
            return [self.unavailable(company, "ted", TED, f"{type(e).__name__}: {e}")]
        facts = parse_notices(data, company)
        if not facts:
            return [Fact(company_id=company.id, type="source_check", key="ted",
                         value={"source": "TED", "status": "no_records", "query": body["query"]},
                         source_url=TED, extractor=self.name)]
        return facts
