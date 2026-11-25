"""What a brief shows from the OSINT facts: people, company checks, hiring by year, and flags for the scorecard.

Pure code over stored facts. Wording rule: an empty result names where we looked; it never says "none".
"""
from __future__ import annotations

import re
from typing import Any

from dd.store import Fact

PENALTY = re.compile(r"penále|prominut|příslušenství daně|úrok z prodlení|pokut", re.I)
PENALTY_PROVIDERS = re.compile(r"správa sociálního zabezpečení|finanční úřad|zdravotní pojišťovna|celní", re.I)


PROFESSIONAL_ROLES = 40  # more roles than this in other companies: a formation, nominee or administration service
TROUBLE_KEYS = ("insolvency", "bankruptcy", "dissolution_proceedings")


def held_when_troubled(v: dict) -> bool:
    """Did the person hold the role when the company's insolvency, bankruptcy or dissolution was entered, or in the
    two years before it?"""
    st = v.get("status") or {}
    start, end = str(v.get("from") or "")[:10], str(v.get("to") or "9999-12-31")[:10]
    for k in TROUBLE_KEYS:
        d = str(st.get(k) or "")[:10]
        if len(d) == 10 and d[:4].isdigit() and start <= d and end >= f"{int(d[:4]) - 2}{d[4:]}":
            return True
    return False


def _outcome(f: Fact) -> str | None:
    """How the other company stands, worded from its register status at display time (wording can improve without a
    new collection run)."""
    from dd.osint.people import company_outcome
    return company_outcome(f.value.get("status") or {}) if f.value.get("status") is not None else f.value.get("outcome")


def _year(s: Any) -> str:
    return str(s or "")[:4]


def penalty_waivers(facts: list[Fact]) -> list[dict]:
    """Penalty waivers recorded as 'support' in subsidy registers: a sign of late social-security or tax payments."""
    out = []
    for f in facts:
        if f.type != "grant_national" or not isinstance(f.value, dict):
            continue
        v = f.value
        text = f"{v.get('title') or ''} {f.key or ''}"
        provider = str(v.get("provider") or "")
        if PENALTY.search(text) and (PENALTY_PROVIDERS.search(provider) or "penále" in text.lower()):
            out.append({"provider": provider, "title": v.get("title"), "year": _year(v.get("year") or f.event_date),
                        "fact_id": f.id})
    return out


def summary(facts: list[Fact], company_ico: str | None = None) -> dict:
    people = [f for f in facts if f.type == "person" and isinstance(f.value, dict)]
    roles = [f for f in facts if f.type == "person_role_elsewhere" and isinstance(f.value, dict)]
    insolv = {f.value.get("person"): f for f in facts if f.type == "person_insolvency" and isinstance(f.value, dict)}
    unavailable = {f.key: f for f in facts if f.type == "source_unavailable"}
    scan = next((f for f in facts if f.type == "source_check" and f.key == "register_people"), None)
    rows = []
    flags: list[str] = []
    for p in sorted(people, key=lambda f: (not f.value.get("current"), f.value.get("name") or "")):
        name = p.value.get("name")
        here = p.value.get("roles_here") or []
        # a role re-registered (new address, new share) appears twice in the register: show the current one, or the
        # latest one for a person who has left
        cur = [r for r in here if not r.get("to")]
        here = list({(r.get("role"), r.get("share_pct")): r for r in (cur or here[-1:])}.values())
        mine = [r for r in roles if r.value.get("person") == name]
        active = [r for r in mine if r.value.get("active")]
        ended = [r for r in mine if not r.value.get("active")]
        professional = len(mine) > PROFESSIONAL_ROLES  # formation agent, nominee or administrator: not a track record
        # a company's trouble counts only if the person held the role when it happened or in the two years before
        troubled = [] if professional else [r for r in mine if held_when_troubled(r.value)]
        ins = insolv.get(name)
        rows.append({
            "name": name, "current": p.value.get("current"),
            "here": "; ".join(f"{r.get('role')}" + (f" ({r['share_pct']:.0f}%)" if r.get("share_pct") else "")
                              + f" {_year(r.get('from'))}–{_year(r.get('to'))}".rstrip("–") for r in here[:3]),
            "active": [{"company": r.value["company"], "role": r.value["role"], "since": _year(r.value.get("from")),
                        "portfolio": r.value.get("portfolio"), "outcome": _outcome(r), "id": r.id}
                       for r in active],
            "ended": [{"company": r.value["company"], "role": r.value["role"], "from": _year(r.value.get("from")),
                       "to": _year(r.value.get("to")), "outcome": _outcome(r), "id": r.id}
                      for r in sorted(ended, key=lambda r: (not _outcome(r), r.value.get("to") or ""), reverse=False)],
            "insolvency": (None if ins is None else ins.value.get("count", 0)),
            "insolvency_unavailable": f"isir_person:{name}" in unavailable,
            "fact_ids": [p.id] + [r.id for r in mine[:6]] + ([ins.id] if ins else []),
            "matchable": p.value.get("matchable", True), "professional": professional, "roles_total": len(mine),
        })
        execs = [r for r in active if re.search(r"jednatel|ředitel|představenstv|statutory|director", r.value.get("role") or "", re.I)]
        if p.value.get("current") and not professional and len(execs) >= 3:
            flags.append(f"{name} holds {len(execs)} other active executive roles in Czech companies: ask how much "
                         "time goes to this company.")
        if p.value.get("current"):  # people who have left are shown in the table, not flagged
            seen = set()
            for r in troubled:
                if r.value.get("ico") in seen:
                    continue
                seen.add(r.value.get("ico"))
                flags.append(f"{name} was {r.value['role']} of {r.value['company']} ({_year(r.value.get('from'))}–"
                             f"{_year(r.value.get('to'))}), which has {_outcome(r)} in the register: ask what "
                             "happened.".replace("–)", "–now)"))
        for r in active:
            if r.value.get("portfolio"):
                flags.append(f"{name} also holds a role at portfolio company {r.value['portfolio']}.")
        if ins and ins.value.get("count"):
            flags.append(f"The insolvency register lists {ins.value['count']} proceeding(s) for {name}: read them "
                         "before a call.")
    own = next((f for f in facts if f.type == "register_status" and isinstance(f.value, dict)), None)
    if own and own.value.get("status", {}).get("distraint_entries"):
        flags.append(f"The register shows {own.value['status']['distraint_entries']} active distraint entr"
                     f"{'y' if own.value['status']['distraint_entries'] == 1 else 'ies'} for the company.")
    vat = [f for f in facts if f.type == "vat_status" and isinstance(f.value, dict)]
    for f in vat:
        if f.value.get("unreliable") == "ANO":
            flags.append(f"{f.value['company']} is listed as an unreliable VAT payer"
                         + (f" since {f.value['since']}" if f.value.get("since") else "") + ".")
    sanc = next((f for f in facts if f.type == "sanctions_check" and isinstance(f.value, dict)), None)
    for h in (sanc.value.get("hits") if sanc else []) or []:
        flags.append(f"Sanctions list match for {h['subject']} on the {h['list']} ({h['basis']}): verify identity.")
    waivers = penalty_waivers(facts)
    for w in waivers:
        flags.append(f"{w['provider'] or 'An authority'} waived a penalty"
                     + (f" ({w['year']})" if w.get("year") else "") + ": a sign of late payments; ask about it.")
    hiring = sorted((f for f in facts if f.type == "hiring_snapshot" and isinstance(f.value, dict)),
                    key=lambda f: (f.value.get("year") or 0, f.event_date or ""))
    return {
        "people": rows, "flags": flags,
        "scan": scan.value if scan else None,
        "scan_unavailable": (unavailable.get("register_people").value or {}).get("reason")
                            if unavailable.get("register_people") else None,
        "vat": [{"company": f.value["company"], "own": f.value.get("own"), "unreliable": f.value.get("unreliable"),
                 "id": f.id} for f in vat],
        "vat_unavailable": "adis_vat" in unavailable,
        "sanctions": ({"lists": sanc.value.get("lists"), "hits": sanc.value.get("hits"), "id": sanc.id,
                       "date": sanc.event_date} if sanc else None),
        "sanctions_unavailable": [k.split(":", 1)[1] for k in unavailable if k.startswith("sanctions:")],
        "waivers": waivers,
        "register_status": own.value if own else None, "register_status_id": own.id if own else None,
        "hiring": [{"year": f.value.get("year"), "date": f.event_date, "source": f.value.get("source"),
                    "count": f.value.get("count"), "by_function": f.value.get("by_function") or {},
                    "titles": f.value.get("titles") or [], "id": f.id} for f in hiring],
        "ran": bool(people or scan or sanc or vat or hiring),
    }
