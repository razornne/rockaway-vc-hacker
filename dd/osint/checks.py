"""Insolvency of people (ISIR web service), unreliable VAT payer (ADIS), sanctions lists (EU, Czech).

All three are official sources. Person lookups pass the birth date only inside the request and are made with
use_cache=False, so nothing about a person is left on disk; results are stored as names and counts only.
An answer that could not be read is `source_unavailable` (shown as Not checked), never "no record".
"""
from __future__ import annotations

import csv
import html
import io
import re
import xml.etree.ElementTree as ET
from datetime import date

from dd.osint.people import Person, fold
from dd.store import Company, Fact

NAME = "osint_checks"
ISIR_WS = "https://isir.justice.cz:8443/isir_cuzk_ws/IsirWsCuzkService"
ISIR_HUMAN = "https://isir.justice.cz/isir/common/index.do"
ADIS = "https://mojedane.gov.cz/dpr/axis2/services/rozhraniCRPDPH.rozhraniCRPDPHSOAP"
EU_LIST = "https://webgate.ec.europa.eu/fsd/fsf/public/files/csvFullSanctionsList_1_1/content?token=dG9rZW4tMjAxNw"
CZ_LIST = "https://mzv.gov.cz/file/6248997/Vnitrostatni_sankcni_seznam_2026_07_23.csv"
SOAP_HEADERS = {"Content-Type": "text/xml; charset=utf-8"}


def _fact(company: Company, ftype: str, key: str, value: dict, url: str) -> Fact:
    return Fact(company_id=company.id, type=ftype, key=key, value=value, source_url=url, extractor=NAME,
                confidence="high", event_date=date.today().isoformat(), date_precision="day")


def _unavailable(company: Company, source: str, url: str, reason: str) -> Fact:
    return Fact(company_id=company.id, type="source_unavailable", key=source, value={"reason": reason[:300]},
                source_url=url, extractor=NAME, confidence="high")


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _find_all(root, name: str):
    return [e for e in root.iter() if _local(e.tag) == name]


# ------------------------------------------------------------------------------------------------ ISIR
def isir_envelope(**fields) -> str:
    body = "".join(f"<{k}>{html.escape(str(v))}</{k}>" for k, v in fields.items() if v not in (None, ""))
    return ('<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" '
            'xmlns:typ="http://isirws.cca.cz/types/"><soapenv:Body><typ:getIsirWsCuzkDataRequest>'
            f"{body}</typ:getIsirWsCuzkDataRequest></soapenv:Body></soapenv:Envelope>")


def parse_isir(xml_text: str) -> dict | None:
    """{'count': n, 'proceedings': [...]} or None when the answer is not a valid result. WS2 = empty result."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return None
    err = next((e.text for e in _find_all(root, "kodChyby")), None)
    if err == "WS2":
        return {"count": 0, "proceedings": []}
    if err:
        return None
    out = []
    for d in _find_all(root, "data"):
        g = {_local(c.tag): (c.text or "").strip() for c in d}
        out.append({"case": f"{g.get('druhVec', '')} {g.get('bcVec', '')}/{g.get('rocnik', '')}".strip(),
                    "state": g.get("druhStavKonkursu") or None, "started": g.get("datumPmZahajeniUpadku") or None,
                    "ended": g.get("datumPmUkonceniUpadku") or None, "url": g.get("urlDetailRizeni") or None,
                    # who the record is about: used to keep exact matches only, never stored
                    "_last": g.get("nazevOsoby") or "", "_first": g.get("jmeno") or "",
                    "_birth": (g.get("datumNarozeni") or "")[:10], "_ic": g.get("ic") or ""})
    if not out and not _find_all(root, "stav"):
        return None
    return {"count": len(out), "proceedings": out}


def isir_person(company: Company, p: Person, ctx) -> list[Fact]:
    if not p.key:
        return []
    birth = p.key.split("|")[2]
    r = ctx.http.post(ISIR_WS, content=isir_envelope(nazevOsoby=p.last, jmeno=p.first, datumNarozeni=birth,
                                                     maxPocetVysledku=50, vyhledatPresnouShoduJmen="T"),
                      headers=SOAP_HEADERS, use_cache=False)
    res = parse_isir(r.text) if r.status in (200, 500) else None
    if res is None:
        return [_unavailable(company, f"isir_person:{p.name}", ISIR_HUMAN, f"HTTP {r.status} or unreadable answer")]
    # The service also returns similar names and other birth dates (a co-founder got 58 "proceedings" on the first
    # run). Only a record with the same surname, first name and birth date is about this person.
    res["proceedings"] = exact_matches(res["proceedings"], p.first, p.last, birth)
    res["count"] = len(res["proceedings"])
    first_url = next((x["url"] for x in res["proceedings"] if x.get("url")), None)
    return [_fact(company, "person_insolvency", p.name,
                  {"person": p.name, "count": res["count"],
                   "proceedings": [{k: x[k] for k in ("case", "state", "started", "ended", "url")}
                                   for x in res["proceedings"][:10]],
                   "searched": "surname, first name and birth date (exact match)"},
                  first_url or ISIR_HUMAN)]


def exact_matches(rows: list[dict], first: str, last: str, birth: str) -> list[dict]:
    return [r for r in rows if fold(r.get("_last")) == fold(last) and fold(r.get("_first")) == fold(first)
            and r.get("_birth") == birth]


# ------------------------------------------------------------------------------------------------ VAT
def adis_envelope(dics: list[str]) -> str:
    inner = "".join(f"<roz:dic>{d}</roz:dic>" for d in dics)
    return ('<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" '
            'xmlns:roz="http://adis.mfcr.cz/rozhraniCRPDPH/"><soapenv:Body><roz:StatusNespolehlivyPlatceRequest>'
            f"{inner}</roz:StatusNespolehlivyPlatceRequest></soapenv:Body></soapenv:Envelope>")


def parse_adis(xml_text: str) -> dict[str, dict] | None:
    """dic -> {'unreliable': 'ANO'|'NE'|'NENALEZEN', 'since': date}; bank accounts in the answer are ignored."""
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return None
    st = next(iter(_find_all(root, "status")), None)
    if st is None or st.get("statusCode") != "0":
        return None
    return {e.get("dic"): {"unreliable": e.get("nespolehlivyPlatce"), "since": e.get("datumZverejneniNespolehlivosti")}
            for e in _find_all(root, "statusPlatceDPH")}


def vat_status(company: Company, targets: list[tuple[str, str, str | None]], ctx) -> list[Fact]:
    """targets: (DIČ digits, company name, IČO). One call for up to 100."""
    targets = [t for t in targets if t[0]][:100]
    if not targets:
        return []
    r = ctx.http.post(ADIS, content=adis_envelope([t[0] for t in targets]),
                      headers={**SOAP_HEADERS, "SOAPAction": '"http://adis.mfcr.cz/rozhraniCRPDPH/getStatusNespolehlivyPlatce"'},
                      company_id=company.id, kind="adis_vat")
    res = parse_adis(r.text) if r.ok else None
    if res is None:
        return [_unavailable(company, "adis_vat", ADIS, f"HTTP {r.status} or unreadable answer")]
    out = []
    for dic, name, ico in targets:
        v = res.get(dic)
        if not v:
            continue
        out.append(_fact(company, "vat_status", f"{name} ({dic})",
                         {"company": name, "ico": ico, "dic": dic, "unreliable": v["unreliable"], "since": v["since"],
                          "own": ico == company.ico},
                         "https://adisspr.mfcr.cz/dpr/DphReg"))
    return out


def dic_of(facts: list[Fact]) -> str | None:
    ident = next((f for f in facts if f.type == "identity" and isinstance(f.value, dict)), None)
    d = re.sub(r"\D", "", str((ident.value or {}).get("dic") or "")) if ident else ""
    return d or None


# ------------------------------------------------------------------------------------------------ sanctions
def _norm(s: str) -> str:
    """'GUNĎAJEV' and 'Gundajev' compare equal: accents, case and punctuation removed."""
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", fold(s)).split())


def load_eu(text: str) -> list[dict] | None:
    """[{'name', 'birth', 'type'}] from the EU consolidated CSV, or None if it is not that file."""
    if not text.lstrip("﻿").startswith("fileGenerationDate"):
        return None
    rows = list(csv.DictReader(io.StringIO(text.lstrip("﻿")), delimiter=";"))
    if not rows:
        return None
    cols = rows[0].keys()
    whole = next((c for c in cols if c.endswith("WholeName")), None)
    birth = next((c for c in cols if c.endswith("BirthDate_BirthDate")), None)
    typ = next((c for c in cols if c.endswith("SubjectType")), None)
    if not whole:
        return None
    return [{"name": _norm(r.get(whole) or ""), "birth": (r.get(birth) or "")[:10] if birth else "",
             "type": (r.get(typ) or "").lower() if typ else ""} for r in rows if r.get(whole)]


def load_cz(text: str) -> list[dict] | None:
    rows = list(csv.reader(io.StringIO(text.lstrip("﻿"))))
    if len(rows) < 2 or "Příjmení" not in rows[0][0]:
        return None
    out = []
    for r in rows[1:]:
        if len(r) < 5:
            continue
        b = r[4].strip()
        m = re.match(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", b)
        birth = f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}" if m else ""
        for last in r[0].split("/"):
            for first in (r[1].split("/") if r[1].strip() else [""]):
                out.append({"name": _norm(f"{first} {last}".strip()), "birth": birth,
                            "type": "person" if r[1].strip() else "entity", "active": "platn" in fold(r[2])})
    return out


def sanctions(company: Company, people: list[Person], company_name: str, ctx) -> list[Fact]:
    lists = {}
    for label, url, loader in (("EU consolidated list", EU_LIST, load_eu), ("Czech national list", CZ_LIST, load_cz)):
        r = ctx.http.get(url, company_id=company.id, kind="sanctions_list")
        parsed = loader(r.text) if r.ok else None
        lists[label] = (url, parsed)
    out = []
    checked = {k: v for k, v in lists.items() if v[1] is not None}
    for label, (url, parsed) in lists.items():
        if parsed is None:
            out.append(_unavailable(company, f"sanctions:{label}", url, "list could not be downloaded or read"))
    if not checked:
        return out
    cname = _norm(re.sub(r"\b(s\.?\s?r\.?\s?o\.?|a\.?\s?s\.?|se|spol\.)\b", " ", company_name or "", flags=re.I))
    hits = []
    for label, (url, rows) in checked.items():
        for row in rows:
            if row["type"] != "person" and cname and len(cname) > 3 and row["name"] == cname:
                hits.append({"subject": company_name, "list": label, "basis": "same name"})
        for p in people:
            n = _norm(f"{p.first} {p.last}")
            birth = p.key.split("|")[2] if p.key else ""
            for row in rows:
                if row["name"] == n and (not row["birth"] or not birth or row["birth"] == birth):
                    hits.append({"subject": p.name, "list": label,
                                 "basis": "same name and birth date" if row["birth"] and birth else "same name only"})
    out.append(_fact(company, "sanctions_check", "sanctions",
                     {"lists": sorted(checked), "people": len(people), "hits": hits[:10]},
                     next(iter(checked.values()))[0]))
    return out
