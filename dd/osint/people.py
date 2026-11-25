"""People behind a company and their other companies, from the Czech business register.

1. ARES VR (already fetched by the registry collector, read from the HTTP cache) gives the company's officers,
   supervisory and administrative board members, proxies and natural-person shareholders, current and past.
2. The register's official open-data dumps (dataor.justice.cz, s.r.o. and a.s., all seven courts) are streamed once
   per batch to find every other company role of those people, and how those companies ended.

People are matched on first name + surname + birth date. The birth date is used in memory only: it is never written to
facts, the database or a brief (decision of 25 November 2026, docs/OSINT_PLAN.md). Stored: names, roles, dates,
shares, company names and IČOs, all public in the register.
"""
from __future__ import annotations

import gzip
import re
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from dd.config import ROOT
from dd.store import Company, Fact

NAME = "osint_people"
ARES_VR = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/{ico}"
DATAOR = "https://dataor.justice.cz/api/file/{name}"
OR_LINK = "https://or.justice.cz/ias/ui/rejstrik-$firma?ico={ico}"  # a page a reader can open; not fetched by us
DUMP_DIR = ROOT / "data" / "dataor"
COURTS = ("praha", "brno", "ostrava", "plzen", "ceske_budejovice", "hradec_kralove", "usti_nad_labem")
FORMS = ("sro", "as")
YEAR = 2026

# register entry type -> role in plain English; liquidators and insolvency administrators are professionals acting
# for a court, not people behind the company, so they are left out
ROLE_KODS = {"STATUTARNI_ORGAN_CLEN": "statutory body", "DOZORCI_RADA_CLEN": "supervisory board",
             "SPRAVNI_RADA_CLEN": "administrative board", "SPOLECNIK_OSOBA": "shareholder",
             "AKCIONAR": "sole shareholder", "PROKURA_OSOBA": "proxy (prokura)"}
EXECUTIVE = re.compile(r"jednatel|ředitel|reditel|předseda představenstva|člen představenstva|statutární|statutory|"
                       r"managing|director|ceo", re.I)


def fold(s: str | None) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s or "") if not unicodedata.combining(c)).lower().strip()


def person_key(first: str | None, last: str | None, birth: str | None) -> str | None:
    """Matching key, in memory only. None when any part is missing: without a birth date no match is attempted."""
    if not (first and last and birth):
        return None
    return f"{fold(first)}|{fold(last)}|{str(birth)[:10]}"


@dataclass
class Person:
    name: str
    first: str
    last: str
    key: str | None  # contains the birth date: never stored
    roles: list[dict] = field(default_factory=list)

    @property
    def current(self) -> bool:
        return any(not r.get("to") for r in self.roles)


def _role_from_ares(node: dict, body: str | None) -> dict:
    func = ((node.get("clenstvi") or {}).get("funkce")) or {}
    return {"role": func.get("nazev") or node.get("nazevAngazma") or body or "member", "body": body,
            "from": func.get("vznikFunkce") or node.get("datumZapisu"),
            "to": func.get("zanikFunkce") or node.get("datumVymazu")}


def people_from_vr(vr: dict) -> list[Person]:
    """Natural persons in an ARES VR record, with their roles at this company (current and past)."""
    from dd.collectors.registry import parse_fraction
    recs = (vr or {}).get("zaznamy") or []
    rec = next((z for z in recs if z.get("primarniZaznam")), recs[0] if recs else None)
    if not rec:
        return []
    found: dict[str, Person] = {}

    def add(fo: dict, role: dict):
        first, last = fo.get("jmeno"), fo.get("prijmeni")
        if not (first and last):
            return
        key = person_key(first, last, fo.get("datumNarozeni"))
        ident = key or f"{fold(first)}|{fold(last)}|?"
        p = found.setdefault(ident, Person(name=f"{first.strip().title() if first.isupper() else first.strip()} "
                                                f"{last.strip().title() if last.isupper() else last.strip()}",
                                           first=first, last=last, key=key))
        if role not in p.roles:
            p.roles.append(role)

    for k, groups in rec.items():
        if not isinstance(groups, list):
            continue
        for g in groups:
            if not isinstance(g, dict):
                continue
            body = g.get("nazevOrganu")
            for m in g.get("clenoveOrganu") or []:
                if isinstance(m, dict) and m.get("fyzickaOsoba"):
                    add(m["fyzickaOsoba"], _role_from_ares(m, body))
            for s in g.get("spolecnik") or []:
                o = (s or {}).get("osoba") or {}
                if o.get("fyzickaOsoba"):
                    pod = [x for x in s.get("podil") or [] if not x.get("datumVymazu")] or (s.get("podil") or [])[-1:]
                    share = parse_fraction(pod[-1].get("velikostPodilu")) if pod else None
                    add(o["fyzickaOsoba"], {"role": "shareholder", "body": body or "shareholders",
                                            "from": s.get("datumZapisu") or o.get("datumZapisu"),
                                            "to": s.get("datumVymazu") or o.get("datumVymazu"),
                                            "share_pct": share})
    for p in found.values():
        p.roles.sort(key=lambda r: (r.get("from") or "", r["role"]))
    return sorted(found.values(), key=lambda p: (not p.current, p.name))


def read_vr(company: Company, ctx) -> dict | None:
    """The ARES VR record, through the HTTP cache the registry collector filled."""
    if not company.ico:
        return None
    r = ctx.http.get(ARES_VR.format(ico=company.ico), company_id=company.id, kind="ares_vr")
    if not r.ok:
        return None
    try:
        return r.json()
    except ValueError:
        return None


# ------------------------------------------------------------------------------------------------ register dumps
def dump_files() -> list[Path]:
    return [DUMP_DIR / f"{f}-full-{c}-{YEAR}.xml.gz" for f in FORMS for c in COURTS]


def download_dumps() -> list[Path]:
    """Fetch the missing dumps (about 806 MB in all), one file at a time. Official bulk open data, kept as a cache."""
    import httpx

    from dd.http import UA
    DUMP_DIR.mkdir(parents=True, exist_ok=True)
    got = []
    for path in dump_files():
        if path.exists() and path.stat().st_size:
            continue
        part = path.with_suffix(".part")
        with httpx.stream("GET", DATAOR.format(name=path.name), headers={"User-Agent": UA}, timeout=600,
                          follow_redirects=True) as r:
            r.raise_for_status()
            with part.open("wb") as fh:
                for chunk in r.iter_bytes(1 << 20):
                    fh.write(chunk)
        part.replace(path)
        got.append(path)
    return got


def _t(el, path: str) -> str | None:
    x = el.find(path)
    return x.text.strip() if x is not None and x.text and x.text.strip() else None


def _status(subj) -> dict:
    """How a company stands or ended, from its register entries."""
    st: dict = {}
    if _t(subj, "vymazDatum"):
        st["deleted"] = _t(subj, "vymazDatum")
    for u in subj.find("udaje") if subj.find("udaje") is not None else []:
        kod = _t(u, "udajTyp/kod") or ""
        since = _t(u, "zapisDatum")
        if kod == "INSOLVENCE_SEKCE":
            st["insolvency"] = since
        elif kod == "KONKURS_SEKCE":
            st["bankruptcy"] = since
        elif kod == "LIKVIDATOR":
            st["liquidation"] = since
        elif kod == "ZAHAJENI_O_ZRUSENI":
            st["dissolution_proceedings"] = since
        elif kod == "PRAVNI_DUVOD_VYMAZU":
            st["deletion_reason"] = (_t(u, "hodnotaText") or "")[:200]
        elif kod == "EXEKUCE_SEKCE":
            active = [x for x in u.iter("Udaj") if _t(x, "udajTyp/kod") == "EXEKUCE" and not _t(x, "vymazDatum")]
            if active:
                st["distraint_entries"] = len(active)
    if "v likvidaci" in fold(_t(subj, "nazev")):
        st.setdefault("liquidation", "in the name")
    return st


def scan(files: Iterable[Path], wanted: set[str]) -> dict[str, list[dict]]:
    """Every company role of the wanted people (keys from person_key), one streaming pass over the dumps."""
    surnames = {k.split("|")[1] for k in wanted}
    out: dict[str, list[dict]] = {k: [] for k in wanted}
    for path in files:
        if not path.exists():
            continue
        with gzip.open(path, "rb") as fh:
            for _, el in ET.iterparse(fh, events=("end",)):
                if el.tag != "Subjekt":
                    continue
                hits = []
                for u in el.iter("Udaj"):
                    kod = _t(u, "udajTyp/kod")
                    if kod not in ROLE_KODS:
                        continue
                    o = u.find("osoba")
                    if o is None or fold(_t(o, "prijmeni")) not in surnames:
                        continue
                    key = person_key(_t(o, "jmeno"), _t(o, "prijmeni"), _t(o, "narozDatum"))
                    if key in wanted:
                        hits.append((key, kod, u))
                if hits:
                    ico, name, status = _t(el, "ico"), _t(el, "nazev"), _status(el)
                    ico = ico.zfill(8) if ico and ico.isdigit() else ico  # the dumps drop leading zeros
                    for key, kod, u in hits:
                        out[key].append({"ico": ico, "company": name, "kind": kod,
                                         "role": _t(u, "funkce") or ROLE_KODS[kod],
                                         "from": _t(u, "funkceOd") or _t(u, "zapisDatum"),
                                         "to": _t(u, "funkceDo") or _t(u, "clenstviDo") or _t(u, "vymazDatum"),
                                         "status": status, "file": path.name})
                el.clear()
    return {k: merge_roles(v) for k, v in out.items()}


def merge_roles(rows: list[dict]) -> list[dict]:
    """One row per company and role kind: a re-registered entry (new address, new title) is the same role."""
    by: dict[tuple, dict] = {}
    for r in rows:
        k = (r["ico"], r["kind"])
        cur = by.get(k)
        if not cur:
            by[k] = dict(r)
            continue
        cur["from"] = min(x for x in (cur["from"], r["from"]) if x) if (cur["from"] or r["from"]) else None
        cur["to"] = None if (cur["to"] is None or r["to"] is None) else max(cur["to"], r["to"])
        if EXECUTIVE.search(r["role"] or "") and not EXECUTIVE.search(cur["role"] or ""):
            cur["role"] = r["role"]
    return sorted(by.values(), key=lambda r: (r["to"] is not None, r["from"] or ""))


# ------------------------------------------------------------------------------------------------ facts
ENDED = ("insolvency", "bankruptcy", "liquidation", "dissolution_proceedings", "deleted")


def company_outcome(status: dict) -> str | None:
    """A short phrase for how a company ended or stands, or None when nothing is recorded."""
    bits = []
    if status.get("bankruptcy"):
        bits.append(f"bankruptcy ({status['bankruptcy'][:4]})")
    if status.get("insolvency"):  # a section can also hold a creditor's petition that was rejected
        bits.append(f"insolvency register entries ({status['insolvency'][:4]})")
    if status.get("dissolution_proceedings"):
        bits.append(f"court dissolution proceedings ({status['dissolution_proceedings'][:4]})")
    if status.get("liquidation"):
        bits.append("liquidation")
    if status.get("deleted"):
        bits.append(f"deleted from the register ({status['deleted'][:4]})")
    if status.get("distraint_entries"):
        bits.append(f"{status['distraint_entries']} active distraint entr{'y' if status['distraint_entries'] == 1 else 'ies'}")
    return ", ".join(bits) or None


def facts_for(company: Company, people: list[Person], roles: dict[str, list[dict]] | None,
              portfolio_icos: dict[str, str], scanned: list[Path]) -> list[Fact]:
    vr_url = ARES_VR.format(ico=company.ico)
    out = []
    for p in people:
        out.append(Fact(company_id=company.id, type="person", key=p.name, extractor=NAME, source_url=vr_url,
                        confidence="high",
                        value={"name": p.name, "current": p.current, "matchable": p.key is not None,
                               "roles_here": [{k: r.get(k) for k in ("role", "body", "from", "to", "share_pct")}
                                              for r in p.roles]}))
        if roles is None or not p.key:
            continue
        for r in roles.get(p.key, []):
            if r["ico"] == company.ico:
                continue
            out.append(Fact(company_id=company.id, type="person_role_elsewhere",
                            key=f"{p.name} | {r['ico']} | {r['kind']}", extractor=NAME,
                            source_url=OR_LINK.format(ico=r["ico"]) if r.get("ico") else DATAOR.format(name=r["file"]),
                            event_date=r.get("from"), date_precision="day" if r.get("from") else None,
                            confidence="high",
                            value={"person": p.name, "company": r["company"], "ico": r["ico"], "role": r["role"],
                                   "kind": r["kind"], "from": r["from"], "to": r["to"], "active": r["to"] is None,
                                   "outcome": company_outcome(r["status"]), "status": r["status"],
                                   "portfolio": portfolio_icos.get(r["ico"] or ""),
                                   "read_from": DATAOR.format(name=r["file"])}))
    own = next((r for p in people if p.key and roles for r in roles.get(p.key, []) if r["ico"] == company.ico), None)
    if own:  # the company's own entries in the same dump: insolvency, liquidation, distraint
        out.append(Fact(company_id=company.id, type="register_status", key=company.ico or company.id, extractor=NAME,
                        source_url=OR_LINK.format(ico=company.ico), confidence="high",
                        value={"status": own["status"], "outcome": company_outcome(own["status"]),
                               "read_from": DATAOR.format(name=own["file"])}))
    if roles is not None:
        out.append(Fact(company_id=company.id, type="source_check", key="register_people", extractor=NAME,
                        source_url="https://dataor.justice.cz", confidence="high",
                        value={"status": "ok", "people": len(people),
                               "matched": sum(1 for p in people if p.key),
                               "files": [f.name for f in scanned],
                               "covers": "s.r.o. and a.s. in the Czech register (other legal forms and foreign "
                                         "companies are not covered)"}))
    return out
