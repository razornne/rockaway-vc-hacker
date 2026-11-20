"""Public money collector (Stream D): state contracts, national grants, EU projects.

Sources
  Hlídač státu  contracts (registr smluv) + subsidies (dotace, incl. de minimis, IS VaVaI, MPO ...) by IČO.
                With HLIDAC_TOKEN → official API v2 (Authorization: Token ...); otherwise the public HTML
                search pages (https://www.hlidacstatu.cz/hledat?Q=ico:<ico>, /dotace/hledat?Q=ico:<ico>).
  CORDIS        EU projects (Horizon, EIC ...) by organisation name; only clear name / VAT / domain matches.
  STARFOS       TA ČR projects: no documented public API (the SPA's /api/starfos/* is internal and undocumented),
                so a source_unavailable fact is emitted. TA ČR projects are largely visible via Hlídač dotace (IS VaVaI).

Facts: gov_contract, grant_national, grant_eu, source_unavailable. Never raises.
"""
from __future__ import annotations

import re
import unicodedata
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from urllib.parse import quote, urlparse

from bs4 import BeautifulSoup

from dd.collectors.base import Collector, Context
from dd.search import fold
from dd.store import Company, Fact

HS = "https://www.hlidacstatu.cz"
CORDIS = "https://cordis.europa.eu/search/en"
MAX_PAGES = 5


HS_API = "https://api.hlidacstatu.cz"  # the API lives on its own host (www.* returns 404)


def _czk(s) -> int | None:
    if isinstance(s, (int, float)) and not isinstance(s, bool):  # API numbers are numbers, not formatted text
        return int(round(s))
    s = unicodedata.normalize("NFKC", str(s or "")).replace("\u00a0", " ")
    m = re.search(r"-?\d[\d\s.,]*", s)
    if not m:
        return None
    raw = re.sub(r"\s+", "", m.group(0))
    sign = "-" if raw.startswith("-") else ""
    raw = raw.lstrip("+-")
    comma, dot = raw.rfind(","), raw.rfind(".")
    decimal_sep = None
    if comma >= 0 and dot >= 0:
        last = max(comma, dot)
        if len(raw) - last - 1 in (1, 2):
            decimal_sep = raw[last]
    elif comma >= 0 and (len(raw) - comma - 1 in (1, 2) or (raw.count(",") == 1 and len(raw) - comma - 1 > 3)):
        decimal_sep = ","
    elif dot >= 0 and (len(raw) - dot - 1 in (1, 2) or (raw.count(".") == 1 and len(raw) - dot - 1 > 3)):
        decimal_sep = "."  # '1351788.1146' (an API value with VAT) is 1.35M, not 13.5bn
    if decimal_sep:
        other = "." if decimal_sep == "," else ","
        normalized = raw.replace(other, "").replace(decimal_sep, ".")
    else:
        normalized = re.sub(r"[.,]", "", raw)
    try:
        amount = Decimal(sign + normalized)
        multiplier = 1_000_000_000 if re.search(r"\b(?:mld|miliard(?:a|y)?|billion)\b", s, re.I) else (
            1_000_000 if re.search(r"\b(?:mil|milion(?:u|y)?|mln|million)\b", s, re.I) else 1)
        return int((amount * multiplier).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    except (InvalidOperation, ValueError):
        return None


def _cz_date(s: str) -> str | None:
    s = (s or "").strip()
    try:
        return datetime.strptime(s, "%d.%m.%Y").date().isoformat()
    except ValueError:
        pass
    m = re.match(r"\d{4}(-\d{2}(-\d{2})?)?", s)
    return m.group(0) if m else None


def _txt(el) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", el.get_text(" ", strip=True))).strip() if el else ""


# --- Hlídač HTML parsers ---------------------------------------------------------
def parse_contracts_html(html: str, ico: str) -> list[dict]:
    """Rows of the 'Nalezené smlouvy' table: each contract = <tr class=bg first> + <tr class=bg last> (subject)."""
    soup = BeautifulSoup(html, "lxml")
    out = []
    for first in soup.select("table.hs-results tr.first"):
        tds = first.find_all("td")
        if len(tds) < 5:
            continue
        a = tds[0].select_one('a[href*="/Detail/"]')
        if not a:
            continue
        cid = re.search(r"/Detail/(\d+)", a["href"]).group(1)
        payer_a, supp_a = tds[2].select('a[href*="/Subjekt/"]')[-1:], tds[3].select('a[href*="/Subjekt/"]')
        payer_ico = re.search(r"/Subjekt/(\d+)", payer_a[0]["href"]).group(1) if payer_a else None
        supp_ico = re.search(r"/Subjekt/(\d+)", supp_a[0]["href"]).group(1) if supp_a else None
        price = tds[4].find("span")
        nxt = first.find_next_sibling("tr")
        subject = ""
        if nxt is not None and "last" in (nxt.get("class") or []):
            full = nxt.select_one("td.hs-full")
            if full:
                sub = full.find("span")
                if sub:
                    sub.extract()
                subject = _txt(full)
        out.append({
            "id": cid, "signed": _cz_date(_txt(tds[1])), "payer": _txt(tds[2]), "payer_ico": payer_ico,
            "supplier": _txt(tds[3]), "supplier_ico": supp_ico,
            "amount_czk": _czk(_txt(price) if price else _txt(tds[4])), "subject": subject,
            "url": f"{HS}/Detail/{cid}",
        })
    return out


def parse_subsidies_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    out = []
    for tr in soup.select("table tr"):
        a = tr.select_one('a[href*="/Dotace/Detail/"]')
        if not a:
            continue
        tds = tr.find_all("td")
        if len(tds) < 6:
            continue
        did = a["href"].split("/Dotace/Detail/")[1].split("?")[0]
        prov_a = tds[2].find("a")
        out.append({
            "id": did, "recipient": _txt(tds[1]), "provider": _txt(tds[2]),
            "provider_ico": re.sub(r"\D", "", prov_a["href"]) if prov_a and prov_a.get("href") else None,
            "title": _txt(tds[3]), "year": _txt(tds[4]), "amount_czk": _czk(_txt(tds[5])),
            "url": f"{HS}/Dotace/Detail/{did}",
        })
    return out


# --- Hlídač API (token) ------------------------------------------------------------
SUBSIDY_SUBJECT = re.compile(r"podpor|podp\.|dotac|grant|účelov|investiční pobídk|poskytnutí\s+(?:účelové\s+)?podpory|"
                             r"poskytnutí\s+příspěvku|příspěvku\s+z|antivirus|zvýhodněn\w*\s+služ", re.I)
# "Smlouva o posk. podp. Sigma (TQ16)" is a TA ČR support agreement written in abbreviations


def _title_key(title: str) -> str:
    t = re.sub(r"CZ\.\d[\w./-]*", " ", title or "")          # programme codes
    t = re.sub(r"\b\d{6,}\b", " ", t)
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower())


def _close(a, b, tol=0.1) -> bool:
    try:
        a, b = float(a), float(b)
    except (TypeError, ValueError):
        return False
    return a > 0 and b > 0 and abs(a - b) <= tol * max(a, b)


CZ_CODE = re.compile(r"CZ\.\d{2}\.\d{2}\.\d{2}/\d{2}/\d{2}_\d{3}/\d{7}")
# Which record of a project states the amount awarded to the company: the R&D register (IS VaVaI) first, then EU
# funds, then the payments register (IsRed), then de-minimis records (the value of the aid).
AWARD_ORDER = ("IsVavai", "Eufondy", "IsRed", "DeMinimis")


def _codes(r: dict) -> set[str]:
    codes = set(CZ_CODE.findall(r.get("title") or ""))
    if r.get("project_code"):
        codes.add(re.sub(r"\s+", "", str(r["project_code"])).upper())
    return codes


def _same_project(a: dict, b: dict) -> bool:
    if _codes(a) & _codes(b):
        return True
    ka, kb = _title_key(a.get("title")), _title_key(b.get("title"))
    if not ka or not kb:
        return False
    same_title = ka == kb or (min(len(ka), len(kb)) >= 12 and (ka in kb or kb in ka))
    if not same_title:
        return False
    # a long, specific project title is the same project ACROSS registers even when the amounts differ (awarded in
    # IS VaVaI vs paid in IsRed). Within one register, repeated titles are separate aid (incubator support every
    # year), and a short generic title ("Registrace ochranné známky") is never enough: both need the same amount.
    across = bool(a.get("dataset") and b.get("dataset") and a["dataset"] != b["dataset"])
    return (across and min(len(ka), len(kb)) >= 30) or _close(a.get("amount_czk"), b.get("amount_czk"), 0.001)


def _rank(r: dict) -> int:
    ds = r.get("dataset") or ""
    return AWARD_ORDER.index(ds) if ds in AWARD_ORDER else len(AWARD_ORDER)


def merge_projects(rows: list[dict]) -> list[dict]:
    """One record per subsidised project. The same project appears in several Czech registers with different
    meanings: IS VaVaI states the support awarded, IsRed the payments by year, EU funds and de-minimis records the
    value of the aid. Summing them double-counts (Fly4Future: CZK 212M shown, about 123M awarded). Each project keeps
    `awarded_czk` (from the most authoritative record), `paid_czk` / `paid_by_year` (only from actual payment records)
    and the other listings in `also_listed_as`."""
    groups: list[list[dict]] = []
    for r in rows:
        g = next((g for g in groups if any(_same_project(r, x) for x in g)), None)
        if g is None:
            groups.append([dict(r)])
        else:
            g.append(dict(r))
    out = []
    for g in groups:
        g.sort(key=_rank)
        main = dict(g[0])
        awarded = next((x.get("awarded_czk") or x.get("amount_czk") for x in g if x.get("awarded_czk") or x.get("amount_czk")), None)
        paid_years: dict[int, float] = {}
        for x in g:
            for p in x.get("disbursed") or []:
                if p.get("year") and p.get("amount"):
                    paid_years[int(p["year"])] = paid_years.get(int(p["year"]), 0.0) + float(p["amount"])
        main["amount_czk"] = awarded
        main["awarded_czk"] = awarded
        main["awarded_from"] = main.get("dataset")
        main["paid_czk"] = int(round(sum(paid_years.values()))) if paid_years else None
        main["paid_by_year"] = [{"year": y, "amount_czk": int(round(a))} for y, a in sorted(paid_years.items())]
        main.pop("disbursed", None)
        others = [{"provider": x.get("provider"), "url": x.get("url"), "year": x.get("year"),
                   "dataset": x.get("dataset"), "amount_czk": x.get("amount_czk")} for x in g[1:]]
        if others:
            main["also_listed_as"] = (main.get("also_listed_as") or []) + others
        out.append(main)
    return out


def reconcile_award(r: dict) -> dict:
    """The registers disagree on what was awarded: IS VaVaI can state less than the signed support agreement, and
    payments can already exceed it (Fly4Future TQ03: IS VaVaI 3.35M, agreement 4.879M, paid 4.879M). The signed
    agreement with the company is the award; payments made are a floor. The register's own figure is kept."""
    agreed = max((a.get("amount_czk") or 0 for a in r.get("agreements") or []), default=0)
    paid = r.get("paid_czk") or 0
    base = r.get("awarded_czk") or r.get("amount_czk") or 0
    if base:
        r["register_award_czk"] = base
    for amount, source in ((agreed, "support agreement (contract register)"), (paid, "payments made (IsRed)")):
        if amount and amount > (r.get("amount_czk") or 0):
            r["amount_czk"] = r["awarded_czk"] = amount
            r["awarded_from"] = source
    return r


def dedupe_subsidies(rows: list[dict]) -> list[dict]:
    """Kept for callers of the old name: the same project in several subsidy datasets becomes one record."""
    return merge_projects(rows)


PROGRAMME_IN_SUBJECT = re.compile(r"\(([A-Z]{2}\d{2})\)")


def _matching_subsidy(contract: dict, subsidies: list[dict]) -> dict | None:
    # "Smlouva o poskytnutí podpory Trend 10 (FW10)" belongs to the TA ČR project whose code starts with FW10
    m = PROGRAMME_IN_SUBJECT.search(contract.get("subject") or "")
    if m:
        hits = [s for s in subsidies if any(c.startswith(m.group(1)) for c in _codes(s))]
        if len(hits) == 1:
            return hits[0]
    year = (contract.get("signed") or "")[:4]
    for s in subsidies:
        same_year = not year or not s.get("year") or abs(int(year) - int(str(s["year"])[:4])) <= 1
        if same_year and _close(contract.get("amount_czk"), s.get("amount_czk"), 0.1):
            return s
        # no comparable amounts (agreement without price, subsidy without amount): match on the programme name
        if same_year and not (contract.get("amount_czk") and s.get("amount_czk")):
            words = [w for w in re.findall(r"\w{5,}", (s.get("title") or "").lower())]
            if words and all(w in (contract.get("subject") or "").lower() for w in words[:3]):
                return s
    return None


def _g(d: dict, *names, default=None):
    low = {k.lower(): v for k, v in d.items()}
    for n in names:
        if n.lower() in low and low[n.lower()] not in (None, ""):
            return low[n.lower()]
    return default


def parse_contracts_api(obj: dict) -> list[dict]:
    out = []
    for r in obj.get("results", []) or []:
        payer = _g(r, "platce", default={}) or {}
        recips = _g(r, "prijemce", default=[]) or []
        recips = [recips] if isinstance(recips, dict) else recips
        sup = recips[0] if recips else {}
        cid = str(_g(r, "id", "identifikator", default=""))
        out.append({
            "id": cid, "signed": _cz_date(str(_g(r, "datumUzavreni", default=""))),
            "payer": _g(payer, "nazev", "jmeno", default=""), "payer_ico": _g(payer, "ico"),
            "supplier": _g(sup, "nazev", "jmeno", default=""), "supplier_ico": _g(sup, "ico"),
            "amount_czk": _czk(_g(r, "calculatedPriceWithVATinCZK", "hodnotaVcetneDph", "hodnotaBezDph", default="")),
            "subject": _g(r, "predmet", default=""),
            "url": _g(r, "odkaz", default=f"{HS}/Detail/{cid}"),
        })
    return out


def parse_subsidies_api(obj: dict) -> list[dict]:
    """Hlídač API v2 /dotace/hledat (field names verified on live responses, 2026-11-17).

    Hlídač marks cross-dataset duplicates in `hints` (isOriginal / originalSubsidyId); only originals are kept.
    """
    out = []
    for r in obj.get("results", []) or []:
        hints = r.get("hints") or {}
        if hints.get("isOriginal") is False or hints.get("originalSubsidyId"):
            continue
        rec = r.get("recipient") or {}
        did = str(r.get("id") or "")
        ds = r.get("primaryDataSource") or did.split("-")[0]
        # subsidyAmount = support awarded; payedAmount is a payment only in IsRed (with per-year `cerpani`);
        # elsewhere (EU funds, de minimis) it restates the aid value, sometimes for a year that has not happened yet
        awarded = next((r.get(k) for k in ("subsidyAmount", "assumedAmount", "payedAmount") if r.get(k)), None)
        disbursed = [{"year": c.get("year"), "amount": c.get("amount")} for c in (r.get("cerpani") or [])
                     if isinstance(c, dict)] if ds == "IsRed" else []
        if ds == "IsRed" and not disbursed and r.get("payedAmount"):
            disbursed = [{"year": r.get("approvedYear"), "amount": r.get("payedAmount")}]
        out.append({
            "id": did, "recipient": rec.get("name") or rec.get("displayName") or "",
            "provider": r.get("subsidyProvider") or r.get("primaryDataSource") or "",
            "provider_ico": r.get("subsidyProviderIco"),
            "title": r.get("projectName") or r.get("displayProject") or "",
            "year": str(r.get("approvedYear") or ""),
            "dataset": ds, "project_code": r.get("projectCode"),
            "amount_czk": int(round(float(awarded))) if awarded else None,
            "awarded_czk": int(round(float(awarded))) if awarded else None,
            "disbursed": disbursed,
            "program": r.get("programName") or r.get("programCode"),
            "duplicates": len(hints.get("duplicates") or []),
            "url": f"{HS}/Dotace/Detail/{quote(did)}",
        })
    return out


class PublicMoneyCollector(Collector):
    name = "public_money"
    sources = ["Hlídač státu (smlouvy, dotace)", "CORDIS", "STARFOS (unavailable)"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        facts: list[Fact] = []
        for step in (self._hlidac, self._cordis, self._starfos):
            try:
                facts += step(company, ctx)
            except Exception as e:  # never raise
                ctx.log.exception("public_money step %s failed", step.__name__)
                facts.append(self.unavailable(company, step.__name__.lstrip("_"), HS, f"crash: {e}"))
        return facts

    # --- Hlídač --------------------------------------------------------------
    def _hlidac(self, c: Company, ctx: Context) -> list[Fact]:
        if not c.ico:
            return [self.unavailable(c, "hlidac_statu", f"{HS}/hledat", "no Czech IČO known for this company")]
        ico = c.ico
        contracts, via_contracts, err_contracts = self._hlidac_source(
            c, ctx, "smlouvy", parse_contracts_api, f"{HS}/hledat", parse_contracts_html)
        subsidies, via_subsidies, err_subsidies = self._hlidac_source(
            c, ctx, "dotace", parse_subsidies_api, f"{HS}/dotace/hledat", lambda h, _i: parse_subsidies_html(h))
        out: list[Fact] = []
        q = f"ico:{ico}"
        checks = (("contracts", contracts, via_contracts, err_contracts, f"{HS}/hledat?Q=ico%3A{quote(ico)}"),
                  ("subsidies", subsidies, via_subsidies, err_subsidies,
                   f"{HS}/dotace/hledat?Q=ico%3A{quote(ico)}"))
        for source, rows, via, error, url in checks:
            if error:
                out.append(self.unavailable(c, f"hlidac_{source}", url, error))
            elif not rows:
                out.append(Fact(company_id=c.id, type="source_check", key=f"hlidac_{source}_empty",
                                value={"source": "hlidac_statu", "dataset": source, "status": "empty",
                                       "query": q, "via": via}, source_url=url,
                                extractor=self.name, confidence="high"))
        subsidy_rows = dedupe_subsidies(subsidies)
        for r in contracts:
            amt = r["amount_czk"]
            role = "supplier" if r.get("supplier_ico") == ico else "payer" if r.get("payer_ico") == ico else "party"
            if SUBSIDY_SUBJECT.search(r.get("subject") or ""):
                # registr smluv also holds subsidy agreements ("Poskytnutí účelové podpory"): the state is a funder,
                # not a customer. Attach to the matching subsidy record, or record it as a grant.
                match = _matching_subsidy(r, subsidy_rows)
                agreement = {"url": r["url"], "signed": r["signed"], "amount_czk": amt, "subject": r["subject"]}
                if match is not None:
                    match.setdefault("agreements", []).append(agreement)
                    continue
                subsidy_rows.append({"id": f"agreement-{r['id']}", "provider": r["payer"], "title": r["subject"],
                                     "year": (r["signed"] or "")[:4], "amount_czk": amt, "url": r["url"],
                                     "from_contract_register": True, "agreements": [agreement]})
                continue
            out.append(Fact(
                company_id=c.id, type="gov_contract", key=str(r["id"]),
                value={"counterparty": r["payer"] if role == "supplier" else r["supplier"],
                       "company_role": role, "amount_czk": amt, "subject": r["subject"], "signed": r["signed"],
                       "via": via_contracts},
                event_date=r["signed"], date_precision="day" if r["signed"] and len(r["signed"]) == 10 else None,
                source_url=r["url"], snippet=f"{r['payer']} → {r['supplier']}: {amt} Kč; {r['subject']}"[:300],
                extractor=self.name, confidence="high"))
        for r in subsidy_rows:
            reconcile_award(r)
            value = {"provider": r["provider"], "title": r["title"], "year": r["year"],
                     # amount_czk = support awarded to the company for the whole project (not paid, not revenue)
                     "amount_czk": r["amount_czk"], "amount_kind": "awarded",
                     "amount_is_estimate": via_subsidies == "html" and not r.get("from_contract_register"),
                     "via": via_subsidies}
            for extra in ("dataset", "project_code", "awarded_from", "register_award_czk", "paid_czk", "paid_by_year",
                          "agreements", "also_listed_as", "from_contract_register"):
                if r.get(extra) not in (None, [], ""):
                    value[extra] = r[extra]
            if r.get("from_contract_register"):
                # an agreement total in the contract register may cover the whole research consortium
                value["amount_kind"] = "agreement_total"
            paid = f"; paid {r['paid_czk']} Kč" if r.get("paid_czk") else ""
            out.append(Fact(
                company_id=c.id, type="grant_national", key=str(r["id"]),
                value=value,
                event_date=r["year"] or None, date_precision="year" if r["year"] else None,
                source_url=r["url"],
                snippet=f"{r['provider']}: {r['title']} ({r['year']}), awarded {r['amount_czk']} Kč{paid}"[:300],
                extractor=self.name, confidence="high"))
        return out

    def _hlidac_source(self, c, ctx, dataset, api_parser, html_path, html_parser):
        """Fetch contracts or subsidies independently, falling back from API to public HTML."""
        if ctx.settings.hlidac_token:
            try:
                return self._api_pages(ctx, c, dataset, api_parser), "api", None
            except Exception as e:
                ctx.log.warning("Hlídač API %s failed; trying HTML fallback: %s", dataset, e)
        rows, error = self._html_pages(ctx, c, html_path, html_parser, c.ico)
        return rows, "html", error

    def _api_pages(self, ctx, c, what, parser):
        rows, token = [], ctx.settings.hlidac_token
        for page in range(1, MAX_PAGES + 1):
            r = ctx.http.get(f"{HS_API}/api/v2/{what}/hledat", params={"dotaz": f"ico:{c.ico}", "strana": page},
                             headers={"Authorization": f"Token {token}"}, company_id=c.id, kind="api")
            if not r.ok:
                raise RuntimeError(f"Hlídač API {what} HTTP {r.status}")
            got = parser(r.json())
            rows += got
            if len(got) < 25:
                break
        return rows

    def _html_pages(self, ctx, c, base, parser, ico):
        rows, seen = [], set()
        for page in range(1, MAX_PAGES + 1):
            r = ctx.http.get(base, params={"Q": f"ico:{ico}", "Page": page}, company_id=c.id, kind="article",
                             title=f"Hlídač státu ico:{ico} p{page}")
            if not r.ok:
                return rows, f"Hlídač HTML HTTP {r.status} at {base}"
            got = [x for x in parser(r.text, ico) if x["id"] not in seen]
            if not got:
                break
            seen.update(x["id"] for x in got)
            rows += got
        return rows, None

    # --- CORDIS ----------------------------------------------------------------
    def _cordis(self, c: Company, ctx: Context) -> list[Fact]:
        names = {c.name, *(c.hints.get("aliases") or [])}
        url = f"{CORDIS}?q=" + quote(f"contenttype='project' AND '{c.name}'")
        r = ctx.http.get(CORDIS, params={"q": f"contenttype='project' AND '{c.name}'", "format": "json", "num": 25},
                         company_id=c.id, kind="api", title=f"CORDIS {c.name}")
        if not r.ok:
            return [self.unavailable(c, "cordis", url, f"HTTP {r.status}")]
        try:
            data = r.json()
        except ValueError:
            return [self.unavailable(c, "cordis", url, "non-JSON response")]
        if not isinstance(data, dict):
            return [self.unavailable(c, "cordis", url, "unexpected JSON response")]
        hit_obj = data.get("hits") or {}
        if not isinstance(hit_obj, dict):
            return [self.unavailable(c, "cordis", url, "unexpected hits shape")]
        hits = hit_obj.get("hit") or []
        hits = [hits] if isinstance(hits, dict) else hits
        if not isinstance(hits, list):
            return [self.unavailable(c, "cordis", url, "unexpected project list")]
        out = []
        for h in hits:
            if not isinstance(h, dict):
                continue
            p = h.get("project") or {}
            if not isinstance(p, dict):
                continue
            org = next((o for o in _orgs(p) if org_matches(o, names, c)), None)
            if not org:
                continue
            attrs = org.get("@attributes", {})
            pid = str(p.get("id") or p.get("rcn"))
            if pid in {"", "None"}:
                continue
            start = str(p.get("startDate") or "")
            event_date = start[:10] or None
            precision = "day" if event_date and len(event_date) == 10 else "month" if event_date and len(event_date) == 7 else "year" if event_date else None
            out.append(Fact(
                company_id=c.id, type="grant_eu", key=pid,
                value={"acronym": p.get("acronym"), "title": p.get("title"), "start": p.get("startDate"),
                       "end": p.get("endDate"), "project_total_cost_eur": _num(p.get("totalCost")),
                       "ec_max_contribution_eur": _num(p.get("ecMaxContribution")),
                       "org_legal_name": org.get("legalName"), "role": attrs.get("type"),
                       "org_ec_contribution_eur": _num(attrs.get("ecContribution")), "sme": attrs.get("sme"),
                       "framework": (p.get("frameworkProgramme") or p.get("programme") or None)
                       if isinstance(p.get("frameworkProgramme") or p.get("programme"), str) else None},
                event_date=event_date, date_precision=precision,
                source_url=f"https://cordis.europa.eu/project/id/{pid}",
                snippet=f"{p.get('acronym')}: {p.get('title')} — {org.get('legalName')}"[:300],
                extractor=self.name, confidence="high"))
        if not out:
            out.append(Fact(company_id=c.id, type="source_check", key="cordis_no_match",
                            value={"source": "cordis", "status": "empty", "query": c.name,
                                   "candidate_projects": len(hits)},
                            source_url=url, extractor=self.name, confidence="high"))
        return out

    # --- STARFOS ---------------------------------------------------------------
    def _starfos(self, c: Company, ctx: Context) -> list[Fact]:
        return [self.unavailable(
            c, "starfos", "https://starfos.tacr.cz",
            "no documented public API (SPA with internal /api/starfos/*); TA ČR/IS VaVaI subsidies are covered via "
            "Hlídač dotace instead. Manual check: https://starfos.tacr.cz")]


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _orgs(node) -> list[dict]:
    """All 'organization' nodes anywhere in a CORDIS project record (dict or list shapes)."""
    found = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "organization":
                found += v if isinstance(v, list) else [v]
            else:
                found += _orgs(v)
    elif isinstance(node, list):
        for i in node:
            found += _orgs(i)
    return [o for o in found if isinstance(o, dict)]


_LEGAL = {"sro", "as", "se", "gmbh", "inc", "ltd", "llc", "bv", "ag", "sa", "spol", "cz", "czech", "republic",
          "sk", "slovakia", "limited", "oy", "ab", "zoo", "kft", "srl"}


def _toks(s: str) -> list[str]:
    s = fold(s).replace(".", "")
    return [t for t in re.split(r"[^a-z0-9]+", s) if t]


def org_matches(org: dict, names: set[str], c: Company) -> bool:
    """Accept only clear matches: VAT = CZ+IČO, same web domain, or legal/short name equals company name (+legal suffix)."""
    if c.ico and re.sub(r"\s", "", str(org.get("vatNumber") or "")).upper() == f"CZ{c.ico.lstrip('0')}":
        return True
    if c.ico and re.sub(r"\s", "", str(org.get("vatNumber") or "")).upper() == f"CZ{c.ico}":
        return True
    if c.domain:
        u = ((org.get("address") or {}).get("url") or "").lower()
        host = urlparse(u if "//" in u else "//" + u).netloc.removeprefix("www.")
        if host and host == c.domain.lower().removeprefix("www."):
            return True
    variants = []
    for n in names:
        t = _toks(n)
        variants.append(t)
        if len(t) > 1 and t[-1] == "ai":
            variants.append(t[:-1])
    for key in ("legalName", "shortName"):
        ot = _toks(str(org.get(key) or ""))
        core = [t for t in ot if t not in _LEGAL]
        for v in variants:
            vc = [t for t in v if t not in _LEGAL]
            if vc and core == vc:
                return True
    return False
