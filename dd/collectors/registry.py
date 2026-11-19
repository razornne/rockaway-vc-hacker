"""Czech registry collector: ARES (basic + VR with history), Sbírka listin, ISIR.

Personal data policy: only legal-entity shareholders are stored (name/IČO/country/dates).
Statutory-body changes carry role + dates only. Natural persons' names, birth dates and
addresses are never read into facts.
"""
from __future__ import annotations

import html as _html
import re
from datetime import date
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from dd.collectors.base import Collector, Context
from dd.resolver import ARES, LEGAL_FORMS, icos_from_domain, normalize_ico, ico_valid
from dd.store import Company, Fact

OR = "https://or.justice.cz/ias/ui"
ISIR = "https://isir.justice.cz/isir/ueu/vysledek_lustrace.do"

AS_FORMS = {"121", "932", "933"}  # a.s., SE, SCE: shareholders not public
_FOREIGN_SUFFIX = re.compile(
    r"(?<!\w)(inc\.?|incorporated|ltd\.?|limited|llc|corp\.?|corporation|b\.v\.?|bv|n\.v\.?|gmbh|ug|ag|"
    r"s\.à r\.l\.|sarl|scsp|sicav|sca|sas|plc|oy|aps|spa|s\.r\.l\.|j\. s\. a\.|sp\. z o\.o\.)(?!\w)", re.I)
_CZ_SUFFIX = re.compile(r"(s\.\s?r\.\s?o\.|a\.\s?s\.|v\.\s?o\.\s?s\.|k\.\s?s\.|z\.\s?s\.)", re.I)


# ---------------------------------------------------------------------------
# pure parsing helpers (unit-tested with saved JSON)
# ---------------------------------------------------------------------------
def parse_amount(v: dict | None) -> tuple[float | None, str | None]:
    if not v:
        return None, None
    h = str(v.get("hodnota", "")).replace(",", ".")
    try:
        amt = float(h)
    except ValueError:
        return None, None
    cur = {"KORUNY": "CZK", "EURA": "EUR", "DOLARY": "USD"}.get(v.get("typObnos"), v.get("typObnos"))
    return (int(amt) if amt == int(amt) else amt), cur


def parse_fraction(v: dict | None) -> float | None:
    """velikostPodilu -> percent. PROCENTA '12;30' = 12.30 %, ZLOMEK '554;14384' = 3.85 %."""
    if not v:
        return None
    h = str(v.get("hodnota", ""))
    try:
        if v.get("typObnos") == "ZLOMEK":
            a, b = h.split(";")
            return 100.0 * float(a) / float(b)
        return float(h.replace(";", "."))
    except (ValueError, ZeroDivisionError):
        return None


def holder_country(po: dict) -> tuple[str | None, bool | None]:
    """(country code, is_foreign) of a legal-entity holder; guessed from the name when no address."""
    code = ((po.get("adresa") or {}).get("kodStatu")) or None
    if code:
        return code, code != "CZ"
    name = po.get("obchodniJmeno") or ""
    if _CZ_SUFFIX.search(name):
        return "CZ", False
    if _FOREIGN_SUFFIX.search(name):
        return None, True
    return None, None


def _active_pct(podily: list[dict], end: str | None) -> float | None:
    """Sum of share sizes valid at the end of the holding (current if end is None)."""
    if not podily:
        return None
    if end is None:
        act = [p for p in podily if not p.get("datumVymazu")]
    else:
        last = max((p.get("datumVymazu") or "") for p in podily)
        act = [p for p in podily if (p.get("datumVymazu") or "") == last]
    pcts = [parse_fraction(p.get("velikostPodilu")) for p in act]
    pcts = [x for x in pcts if x is not None]
    return round(sum(pcts), 2) if pcts else None


def iter_holders(vr_record: dict):
    """Yield (person node, podily) for společníci (s.r.o.) and akcionáři (a.s./SE)."""
    for grp in vr_record.get("spolecnici", []) or []:
        for s in grp.get("spolecnik", []) or []:
            yield s.get("osoba") or {}, s.get("podil") or []
    for grp in vr_record.get("akcionari", []) or []:
        for o in grp.get("clenoveOrganu", []) or []:
            yield o, o.get("podil") or []


def parse_shareholders(vr_record: dict) -> list[dict]:
    """Legal-entity holders only. Natural persons are skipped entirely."""
    out = []
    for o, podily in iter_holders(vr_record):
        po = o.get("pravnickaOsoba")
        if not po or not po.get("obchodniJmeno"):
            continue
        country, foreign = holder_country(po)
        to = o.get("datumVymazu")
        out.append({"name": po["obchodniJmeno"].strip(), "ico": po.get("ico"), "country": country,
                    "foreign": foreign, "from": o.get("datumZapisu"), "to": to,
                    "share_pct": _active_pct(podily, to)})
    out.sort(key=lambda h: (h["from"] or "", h["name"]))
    return out


def parse_capital(vr_record: dict) -> list[dict]:
    out = []
    for c in vr_record.get("zakladniKapital", []) or []:
        amt, cur = parse_amount(c.get("vklad"))
        if amt is None:
            continue
        out.append({"amount": amt, "currency": cur, "amount_czk": amt if cur == "CZK" else None,
                    "from": c.get("datumZapisu"), "to": c.get("datumVymazu")})
    out.sort(key=lambda c: c["from"] or "")
    return out


def parse_officer_changes(vr_record: dict) -> list[dict]:
    """Statutory body members as role + dates ONLY (no names, no birth dates, no addresses)."""
    out = []
    for org in vr_record.get("statutarniOrgany", []) or []:
        for m in org.get("clenoveOrganu", []) or []:
            func = ((m.get("clenstvi") or {}).get("funkce")) or {}
            role = func.get("nazev") or m.get("nazevAngazma") or org.get("nazevOrganu") or "člen"
            out.append({"role": role, "from": func.get("vznikFunkce") or m.get("datumZapisu"),
                        "to": func.get("zanikFunkce") or m.get("datumVymazu"),
                        "body": org.get("nazevOrganu")})
    out.sort(key=lambda c: (c["from"] or "", c["role"]))
    return out


def structural_flags(holders: list[dict], legal_form: str | None, vr_name: str | None = None) -> dict[str, str]:
    """flag -> evidence text."""
    flags: dict[str, str] = {}
    current = [h for h in holders if not h["to"]]
    # Natural-person holders are deliberately omitted, so a sole legal entity is not necessarily a sole holder.
    for h in current:
        pct = h["share_pct"]
        if h["foreign"] and pct is not None and pct > 50:
            size = f"{pct:.1f}%"
            flags["foreign_holding"] = f"{h['name']} ({h['country'] or 'foreign'}) holds {size} since {h['from']}"
            break
    if legal_form in AS_FORMS or (vr_name and re.search(r"(a\.\s?s\.|\bSE)\s*$", vr_name)):
        flags["legal_form_as"] = "joint-stock form (a.s./SE): shareholders are not public in the registry"
    return flags


def cz_date(s: str) -> str | None:
    m = re.search(r"(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{4})", s or "")
    return f"{int(m.group(3)):04d}-{int(m.group(2)):02d}-{int(m.group(1)):02d}" if m else None


def parse_filings(page_html: str, base_url: str) -> list[dict]:
    """Sbírka listin 'Přehled listin' table."""
    soup = BeautifulSoup(page_html, "lxml")
    out = []
    for tbl in soup.select("table.list"):
        for tr in tbl.select("tbody tr"):
            tds = tr.find_all("td")
            if len(tds) < 5:
                continue
            a = tds[0].find("a")
            num = re.sub(r"\s+", " ", tds[0].get_text(" ", strip=True).replace("\xa0", " "))
            sym = tds[1].select_one(".symbol")
            raw_type = re.sub(r"\s+", " ", (sym or tds[1]).get_text(" ", strip=True))
            m = re.match(r"^(.*?)\s*\[(.*)\]\s*$", raw_type)
            doc_type, bracket = (m.group(1), m.group(2)) if m else (raw_type, None)
            period = bracket if bracket and re.fullmatch(r"\d{4}(\D+\d{4})?", bracket.strip()) else None
            out.append({"number": num, "doc_type": doc_type, "period": period,
                        "reference": bracket if bracket and not period else None,
                        "created": cz_date(tds[2].get_text()), "received": cz_date(tds[3].get_text()),
                        "filed": cz_date(tds[4].get_text()),
                        "url": urljoin(base_url, _html.unescape(a["href"])) if a and a.get("href") else None})
    return out


def parse_subjekt_id(page_html: str) -> str | None:
    m = re.search(r"subjektId=(\d+)", page_html)
    return m.group(1) if m else None


def parse_isir_count(page_html: str) -> int | None:
    text = BeautifulSoup(page_html, "html.parser").get_text(" ", strip=True)
    m = re.search(r"POČET NALEZENÝCH DLUŽNÍKŮ\s*(\d+)", text)
    return int(m.group(1)) if m else None


def nace_codes(basic: dict) -> list[str]:
    return list(basic.get("czNace2008") or basic.get("czNace") or [])


# ---------------------------------------------------------------------------
class RegistryCollector(Collector):
    name = "registry"
    sources = ["ARES (ekonomické subjekty + VR)", "or.justice.cz (Sbírka listin)", "ISIR"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        facts: list[Fact] = []
        ico = company.ico
        resolved_via = None
        if not ico:
            ico = self._resolve_ico(company, ctx)
            resolved_via = "domain" if ico else None
        if not ico:
            facts.append(Fact(
                company_id=company.id, type="registry_flag", key="no_cz_entity",
                value={"evidence": "no IČO set and none found on the company website (impressum/contacts)"},
                source_url=(f"https://{company.domain}/" if company.domain else f"{ARES}/ekonomicke-subjekty/vyhledat"),
                extractor=self.name, confidence="medium"))
            return facts
        ico = normalize_ico(ico) or ico
        if not ico_valid(ico):
            return [self.unavailable(company, "ares_basic", f"{ARES}/ekonomicke-subjekty/vyhledat", "invalid Czech IČO")]

        basic, vr = self._ares(company, ico, ctx, facts, resolved_via)
        legal_form = str(basic.get("pravniForma")) if basic else None
        try:
            rec = self._vr_record(vr)
            if rec:
                # Keep a malformed VR section from discarding already collected identity/other sources.
                vr_facts: list[Fact] = []
                self._vr_facts(company, ico, rec, legal_form, vr_facts)
                facts.extend(vr_facts)
        except (AttributeError, TypeError, ValueError, KeyError) as e:
            facts.append(self.unavailable(company, "ares_vr", f"{ARES}/ekonomicke-subjekty-vr/{ico}",
                                          f"unexpected registry structure: {type(e).__name__}"))
        subjekt_id = self._subjekt_id(company, ico, ctx, facts)
        if subjekt_id:
            self._filings(company, subjekt_id, ctx, facts)
        self._isir(company, ico, ctx, facts)
        return facts

    # --- resolve ------------------------------------------------------------
    def _resolve_ico(self, company: Company, ctx: Context) -> str | None:
        if not company.domain:
            return None
        try:
            found = icos_from_domain(company.domain, ctx, company_id=company.id)
        except Exception as e:  # network / parse: treat as unresolved
            ctx.log.debug("domain resolve failed: %s", e)
            return None
        return found[0] if len(found) == 1 else None

    # --- ARES ---------------------------------------------------------------
    def _ares(self, company, ico, ctx, facts, resolved_via):
        basic_url = f"{ARES}/ekonomicke-subjekty/{ico}"
        vr_url = f"{ARES}/ekonomicke-subjekty-vr/{ico}"
        basic = vr = None
        r = ctx.http.get(basic_url, company_id=company.id, kind="ares_basic")
        if r.ok:
            try:
                basic = r.json()
                if not isinstance(basic, dict):
                    raise ValueError("expected ARES object")
            except ValueError:
                basic = None
                facts.append(self.unavailable(company, "ares_basic", basic_url, "invalid JSON"))
        else:
            facts.append(self.unavailable(company, "ares_basic", basic_url, f"HTTP {r.status}"))
        if basic:
            sidlo = basic.get("sidlo") or {}
            pf = str(basic.get("pravniForma") or "")
            facts.append(Fact(
                company_id=company.id, type="identity", key=ico, extractor=self.name, source_url=basic_url,
                source_doc_id=r.doc_id, event_date=basic.get("datumVzniku"), date_precision="day",
                confidence="high" if not resolved_via else "medium",
                value={"name": basic.get("obchodniJmeno"), "ico": ico, "legal_form_code": pf,
                       "legal_form": LEGAL_FORMS.get(pf, pf), "seat_city": sidlo.get("nazevObce"),
                       "seat_country": sidlo.get("kodStatu"), "cz_nace": nace_codes(basic),
                       "dic": basic.get("dic"), "registered": basic.get("datumVzniku"),
                       "resolved_via": resolved_via}))
            if basic.get("datumVzniku"):
                facts.append(Fact(company_id=company.id, type="registry_incorporation", key=ico, extractor=self.name,
                                  source_url=basic_url, source_doc_id=r.doc_id, event_date=basic["datumVzniku"],
                                  date_precision="day", value={"registered": basic["datumVzniku"]}))
        r2 = ctx.http.get(vr_url, company_id=company.id, kind="ares_vr")
        if r2.ok:
            try:
                vr = r2.json()
                if not isinstance(vr, dict):
                    raise ValueError("expected ARES VR object")
            except ValueError:
                vr = None
                facts.append(self.unavailable(company, "ares_vr", vr_url, "invalid JSON"))
        elif r2.status == 404:
            facts.append(self.unavailable(company, "ares_vr", vr_url, "not in commercial register (VR)"))
        else:
            facts.append(self.unavailable(company, "ares_vr", vr_url, f"HTTP {r2.status}"))
        return basic, vr

    @staticmethod
    def _vr_record(vr: dict | None) -> dict | None:
        if not vr:
            return None
        recs = vr.get("zaznamy") or []
        for z in recs:
            if z.get("primarniZaznam") and z.get("rejstrik") == "OR":
                return z
        return recs[0] if recs else None

    def _vr_facts(self, company, ico, rec, legal_form, facts) -> None:
        url = f"{ARES}/ekonomicke-subjekty-vr/{ico}"
        base = dict(company_id=company.id, extractor=self.name, source_url=url, date_precision="day")
        holders = parse_shareholders(rec)
        seen: dict[str, int] = {}
        for h in holders:
            key = h["name"] if h["name"] not in seen else f"{h['name']} ({h['from']})"
            seen[h["name"]] = seen.get(h["name"], 0) + 1
            facts.append(Fact(type="registry_shareholder", key=key, event_date=h["from"],
                              value={k: h[k] for k in ("name", "ico", "country", "from", "to", "share_pct", "foreign")},
                              **base))
        for c in parse_capital(rec):
            facts.append(Fact(type="registry_capital", key=c["from"], event_date=c["from"], value=c, **base))
        for i, o in enumerate(parse_officer_changes(rec)):
            facts.append(Fact(type="registry_officer_change", key=f"{o['role']} {o['from']} #{i}",
                              event_date=o["from"], value=o, **base))
        cur = [n for n in (rec.get("obchodniJmeno") or []) if not n.get("datumVymazu")]
        vr_name = cur[-1].get("hodnota") if cur else None
        for flag, evidence in structural_flags(holders, legal_form, vr_name).items():
            facts.append(Fact(type="registry_flag", key=flag, value={"evidence": evidence}, **base))

    # --- Sbírka listin ------------------------------------------------------
    def _subjekt_id(self, company, ico, ctx, facts) -> str | None:
        url = f"{OR}/rejstrik-$firma?ico={ico}"
        r = ctx.http.get(url, company_id=company.id, kind="or_search")
        if not r.ok:
            facts.append(self.unavailable(company, "or_justice", url, f"HTTP {r.status}"))
            return None
        sid = parse_subjekt_id(r.text)
        if not sid:
            facts.append(self.unavailable(company, "or_justice", url, "subjektId not found (not in OR?)"))
        return sid

    def _filings(self, company, sid, ctx, facts) -> None:
        url = f"{OR}/vypis-sl-firma?subjektId={sid}"
        r = ctx.http.get(url, company_id=company.id, kind="or_sl")
        if not r.ok:
            facts.append(self.unavailable(company, "sbirka_listin", url, f"HTTP {r.status}"))
            return
        try:
            docs = parse_filings(r.text, url)
        except Exception as e:
            facts.append(self.unavailable(company, "sbirka_listin", url, f"parse error: {e}"))
            return
        for d in docs:
            facts.append(Fact(company_id=company.id, type="filing", key=d["number"], extractor=self.name,
                              source_url=url, source_doc_id=r.doc_id, event_date=d["filed"], date_precision="day",
                              value={"doc_type": d["doc_type"], "period": d["period"], "reference": d["reference"],
                                     "filed": d["filed"], "created": d["created"], "received": d["received"],
                                     "url": d["url"]}))

    # --- ISIR ---------------------------------------------------------------
    def _isir(self, company, ico, ctx, facts) -> None:
        url = f"{ISIR}?ic={ico}&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50"
        r = ctx.http.get(url, company_id=company.id, kind="isir")
        if not r.ok:
            facts.append(self.unavailable(company, "isir", url, f"HTTP {r.status}"))
            return
        n = parse_isir_count(r.text)
        if n is None:
            facts.append(self.unavailable(company, "isir", url, "could not parse result count"))
            return
        today = date.today().isoformat()
        facts.append(Fact(company_id=company.id, type="insolvency", key="isir_lustrace", extractor=self.name,
                          source_url=url, source_doc_id=r.doc_id, event_date=today, date_precision="day",
                          value={"records_found": n, "checked": today}))
