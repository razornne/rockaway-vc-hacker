"""`dd osint`: run the OSINT checks for one or more companies. One pass over the register dumps serves the batch."""
from __future__ import annotations

import json
import logging
import time

from dd.config import ROOT
from dd.osint import EXTRACTORS, checks, claims, hiring, people

log = logging.getLogger(__name__)
MAX_PEOPLE_CHECKED = 12  # ISIR and sanctions per company: current people first, then the most recent past ones
MAX_VAT_COMPANIES = 8  # other active companies of the company's people whose VAT status is checked


def _portfolio_icos() -> dict[str, str]:
    rows = json.loads((ROOT / "eval" / "companies.json").read_text(encoding="utf-8"))
    return {r["ico"]: r["name"] for r in rows if r.get("ico") and r.get("tier") in ("showcase", "portfolio")}


def _own_facts(store, cid: str) -> list:
    return [f for f in store.facts(cid) if f.extractor not in EXTRACTORS]


def run(store, ctx, ids: list[str], network: bool = True) -> dict[str, dict[str, int]]:
    from dd.signals import funding
    summary: dict[str, dict[str, int]] = {}
    companies = [store.get_company(i) for i in ids]
    companies = [c for c in companies if c]

    # A. claims against records: code only
    for c in companies:
        facts = _own_facts(store, c.id)
        fin = claims.financials_source(facts, funding(facts).get("financials"))
        out = claims.run(c, facts, fin)
        store.replace_facts(c.id, claims.NAME, out)
        summary.setdefault(c.id, {})["claims"] = len(out)
    if not network:
        return summary

    # B. people, one dump pass for the whole batch
    plist = {c.id: people.people_from_vr(people.read_vr(c, ctx) or {}) for c in companies if c.ico}
    wanted = {p.key for ps in plist.values() for p in ps if p.key}
    files = [f for f in people.dump_files() if f.exists()]
    roles = None
    if wanted and files:
        t = time.monotonic()
        roles = people.scan(files, wanted)
        log.warning("register dumps scanned for %d people in %.0f s", len(wanted), time.monotonic() - t)
    portfolio = _portfolio_icos()
    for c in companies:
        if c.id not in plist:
            continue
        out = people.facts_for(c, plist[c.id], roles, portfolio, files)
        if roles is None:
            out.append(people.Fact(company_id=c.id, type="source_unavailable", key="register_people",
                                   source_url="https://dataor.justice.cz", extractor=people.NAME,
                                   value={"reason": "register dumps not downloaded (data/dataor/)"}))
        store.replace_facts(c.id, people.NAME, out)
        summary[c.id]["people"] = sum(1 for f in out if f.type == "person")
        summary[c.id]["roles_elsewhere"] = sum(1 for f in out if f.type == "person_role_elsewhere")

    # C + D. insolvency of people, VAT status, sanctions
    for c in companies:
        facts = _own_facts(store, c.id)
        ps = plist.get(c.id, [])
        ps = sorted(ps, key=lambda p: (not p.current, -max(int((r.get("to") or "9999")[:4]) for r in p.roles)))
        ps = ps[:MAX_PEOPLE_CHECKED]
        out = []
        for p in ps:
            out += checks.isir_person(c, p, ctx)
        vat = [(checks.dic_of(facts), c.name, c.ico)] if checks.dic_of(facts) else []
        if roles is not None:
            others = []
            for p in ps:
                for r in roles.get(p.key or "", []):
                    if r["to"] is None and r["ico"] and r["ico"] != c.ico and not r["status"].get("deleted"):
                        others.append((r["ico"], r["company"]))
            for ico, name in list(dict.fromkeys(others))[:MAX_VAT_COMPANIES]:
                b = ctx.http.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}",
                                 company_id=c.id, kind="ares_basic")
                try:
                    dic = "".join(ch for ch in str((b.json() or {}).get("dic") or "") if ch.isdigit()) if b.ok else ""
                except ValueError:
                    dic = ""
                if dic:
                    vat.append((dic, name, ico))
        out += checks.vat_status(c, vat, ctx)
        out += checks.sanctions(c, ps, c.name, ctx)
        store.replace_facts(c.id, checks.NAME, out)
        summary[c.id]["checks"] = len(out)

    # E. hiring
    for c in companies:
        facts = _own_facts(store, c.id)
        out = hiring.board_jobs(c, facts, ctx) + hiring.careers_history(c, facts, ctx)
        store.replace_facts(c.id, hiring.NAME, out)
        summary[c.id]["hiring"] = len(out)
    return summary
