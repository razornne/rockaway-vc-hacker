"""Screening scorecard: does a company pass to a first call? Computed by code from the brief's signals, never by a model.

Seven criteria, 0–2 points each. A criterion the public records cannot settle is *open*: it counts as 0 for the low
end of the score and 2 for the high end, so missing data widens the range instead of sinking the company (absence in
public records is not evidence). The verdict compares the range with a bar:

- low end at or above the bar: passes to a first call;
- high end below the bar: does not pass even if every open point comes out well;
- otherwise: open, and the brief says which points decide it.

The rules and the bar are written out on the page and are meant to be changed by the fund: they are a starting point
set by hand (November 2026), not fitted to outcomes. Team and founders are not scored: public records cannot judge
them, and they are the first thing to assess on the call.
"""
from __future__ import annotations

import re
from datetime import date
from typing import Any

from dd.thesis import FUND, format_money, stage_ticket

MAX_POINTS = 2
STALE_ROUND_MONTHS = 18  # an older closed round says little about the round the fund would join
BAR = 8  # of 14: at least four of seven criteria clearly met
REVENUE_STRONG_CZK = 25_000_000  # about EUR 1M, a common Series A revenue bar
EUROPE = {"AL", "AT", "BA", "BE", "BG", "CH", "CY", "CZ", "DE", "DK", "EE", "ES", "FI", "FR", "GB", "GR", "HR", "HU",
          "IE", "IS", "IT", "LT", "LU", "LV", "MD", "ME", "MK", "MT", "NL", "NO", "PL", "PT", "RO", "RS", "SE", "SI",
          "SK", "UA", "UK", "US"}  # US: the fund backs European founders there; nationality is not checked
CORE = {"CZ", "SK", "PL", "HU", "RO", "BG", "SI", "HR", "RS", "EE", "LV", "LT", "UA", "AT", "DE", "CH"}  # CEE and DACH
RULES = {
    "sector": "2: a fund sector backed by official records (defence tender, EU defence project, NATO DIANA) or by 10+ "
              "facts; 1: by 2–9 facts; open: no fund sector in the collected descriptions.",
    "geography": "2: CEE or DACH, the fund's core; 1: elsewhere in Europe, or the US; 0: elsewhere; open: country "
                 "unknown.",
    "round": "2: the round is within or overlaps the fund's initial ticket (EUR 0.5–2m), so the fund could lead; 1: "
             "larger (the fund joins a syndicate) or smaller; open: no round or amount reported, or the latest round "
             "closed more than 18 months ago.",
    "traction": "2: filed revenue of CZK 25M (about EUR 1M) or more; 1: smaller filed revenue, or paid sales to public "
                "buyers or named customers; 0: filed revenue of zero; open: revenue not published.",
    "finances": "2: profitable, or cash covers 12+ months of the latest loss; 1: 6–12 months; 0: under 6 months; "
                "open: filed accounts not read.",
    "technology": "Independent evidence that the technology exists: public code (5+ repositories), research grants, patent "
                  "publications, papers or own models. 2: two kinds or more; 1: one; open: none visible (closed code "
                  "is common).",
    "claims": "Company claims checked against independent sources. 2: confirmed and none contradicted; 1: some not "
              "confirmed; 0: any contradicted; open: nothing checkable.",
}
NAMES = {"sector": "Fund sector", "geography": "Geography", "round": "Round vs ticket", "traction": "Traction",
         "finances": "Financial position", "technology": "Technology evidence", "claims": "Claims checked"}


def _czk(x: float) -> str:
    return f"{x / 1e6:.1f}M CZK".replace(".0M", "M")


def _row(key: str, lo: int, hi: int, finding: str, ids: list[int] | None = None, ask: str = "") -> dict:
    return {"key": key, "name": NAMES[key], "rule": RULES[key], "min": lo, "max": hi, "open": lo != hi,
            "finding": finding, "fact_ids": [i for i in (ids or []) if i is not None][:4], "ask": ask}


def _sector(th: dict) -> dict:
    secs = th.get("sectors") or []
    if not secs:
        return _row("sector", 0, 2, "No fund sector matched in the collected descriptions.",
                    ask="Which of the fund's sectors does the company see itself in, and what shows it?")
    s = max(secs, key=lambda s: (bool(s.get("structured_evidence_fact_ids")), s.get("evidence", 0)))
    if s.get("structured_evidence_fact_ids"):
        return _row("sector", 2, 2, f"{s['sector']}: backed by official records.", s["structured_evidence_fact_ids"])
    pts = 2 if s.get("evidence", 0) >= 10 else 1
    return _row("sector", pts, pts, f"{s['sector']}: {s.get('evidence', 0)} facts.", s.get("fact_ids"))


def _geography(th: dict) -> dict:
    geo = th.get("geography") or {}
    c = str(geo.get("country") or "").split("/")[0].strip().upper()
    if not c:
        return _row("geography", 0, 2, "Country not established.", ask="Where is the company based and incorporated?")
    pts = 2 if c in CORE else 1 if c in EUROPE else 0
    return _row("geography", pts, pts, f"{c}" + (" (core region)" if pts == 2 else ""), geo.get("fact_ids"))


def _round(rounds: list[dict], as_of: date) -> dict:
    st = stage_ticket(rounds)
    rel = st.get("relation")
    ask = "How much are you raising, on what terms, and who else is in the round?"
    if rel in ("no_round", "unknown_amount"):
        return _row("round", 0, 2, st["text"], st.get("fact_ids"), ask=ask)
    r = st.get("round") or {}
    when = str(r.get("date") or "")
    if r.get("status") != "sought" and re.match(r"\d{4}-\d{2}", when):
        y, m = int(when[:4]), int(when[5:7])
        if (as_of.year - y) * 12 + as_of.month - m > STALE_ROUND_MONTHS:  # the fund would join the next round
            what = " ".join(x for x in (format_money(r.get("amount")) or r.get("amount"), r.get("round")) if x)
            return _row("round", 0, 2, f"Last reported round: {what} ({when[:7]}). No current round is reported.",
                        st.get("fact_ids"), ask=ask)
    pts = 2 if rel in ("within_ticket", "overlaps_ticket") else 1
    return _row("round", pts, pts, st["text"], st.get("fact_ids"))


def _traction(fu: dict, sig: dict) -> dict:
    fin = fu.get("financials") or {}
    pm = fu.get("public_money") or {}
    purchase = ((pm.get("contract_kinds") or {}).get("purchase") or {})
    tw = ((sig.get("defence") or {}).get("tenders_won") or {})
    named = ((sig.get("customers") or {}).get("named_customers") or [])
    sales_ids = (purchase.get("fact_ids") or [])[:2] + (tw.get("fact_ids") or [])[:2]
    other = []
    if purchase.get("count") or tw.get("count"):
        other.append(f"{(purchase.get('count') or 0) + (tw.get('count') or 0)} paid sale(s) to public buyers")
    if named:
        other.append(f"{len(named)} named customer(s)")
    if fin and fin.get("income_statement_published") and fin.get("revenue") is not None:
        rev = float(fin["revenue"])
        pts = 2 if rev >= REVENUE_STRONG_CZK else 1 if rev > 0 else 0
        prior = fin.get("revenue_prior")
        growth = f", {rev / prior - 1:+.0%} on the year before" if prior else ""
        return _row("traction", pts, pts, f"Filed revenue {fin.get('period')}: {_czk(rev)}{growth}.", fin.get("fact_ids"))
    lo = 1 if other else 0
    return _row("traction", lo, 2, ("Revenue not published; " + ", ".join(other) + "." if other else
                                    "Revenue not published and no paid sales visible in public records."),
                (fin.get("fact_ids") or []) + sales_ids,
                ask="What was revenue last year and this year so far, and from how many paying customers?")


def _finances(fu: dict) -> dict:
    fin = fu.get("financials") or {}
    if not fin or fin.get("net_result") is None:
        return _row("finances", 0, 2, "Filed accounts not read.",
                    ask="What is the cash position and monthly burn, and how many months of runway is that?")
    net, cash = float(fin["net_result"]), float(fin.get("cash") or 0)
    if net >= 0:
        return _row("finances", 2, 2, f"Profitable in {fin.get('period')} (net {_czk(net)}), cash {_czk(cash)}.",
                    fin.get("fact_ids"))
    months = cash / -net * 12
    pts = 2 if months >= 12 else 1 if months >= 6 else 0
    return _row("finances", pts, pts, f"Net loss {_czk(-net)} in {fin.get('period')}; cash {_czk(cash)} covers about "
                                      f"{months:.0f} months of it.", fin.get("fact_ids"))


def _technology(fu: dict, sig: dict, facts: dict) -> dict:
    eng = sig.get("engineering") or {}
    own = ((sig.get("ai_dependency") or {}).get("own_model_evidence") or {})
    pm = fu.get("public_money") or {}
    kinds, ids = [], []
    if (eng.get("public_repos") or 0) >= 5:
        kinds.append(f"{eng['public_repos']} public repositories")
        ids += (eng.get("repo_fact_ids") or [])[:1]
    # research grants only (the R&D register IS VaVaI, EU programmes): trademark or export support says nothing on tech
    rd = [f.id for f in facts.values() if f.type == "grant_eu"
          or (f.type == "grant_national" and str(f.key or "").startswith("IsVavai"))]
    if rd:
        kinds.append(f"{len(rd)} research grant(s)")
        ids += rd[:1]
    patents = [f.id for f in facts.values() if f.type == "patent"]
    if patents:
        kinds.append(f"{len(patents)} patent publication(s)")
        ids += patents[:1]
    if own.get("papers") or own.get("hf_models"):
        kinds.append("papers or published models")
    if not kinds:
        return _row("technology", 0, 2, "No public code, grants, patents or papers visible.",
                    ask="Can we see the product and the code, and who built the core technology?")
    pts = 2 if len(kinds) >= 2 else 1
    return _row("technology", pts, pts, "; ".join(kinds) + ".", ids)


def _claims(sig: dict) -> dict:
    ver = [v for v in sig.get("verification") or [] if v.get("status") in ("confirmed", "partly", "not_found",
                                                                           "contradicted")]
    if not ver:
        return _row("claims", 0, 2, "No company claim could be checked against an independent source.",
                    ask="Which customers and partners can we call as references?")
    st = [v["status"] for v in ver]
    ids = [i for v in ver for i in (v.get("fact_ids") or [])[:1]]
    words = ", ".join(f"{st.count(s)} {s.replace('_', ' ')}" for s in ("confirmed", "partly", "not_found",
                                                                         "contradicted") if s in st)
    if "contradicted" in st:
        return _row("claims", 0, 0, f"Checks: {words}.", ids, ask="Ask about each contradicted claim.")
    pts = 2 if set(st) == {"confirmed"} else 1
    return _row("claims", pts, pts, f"Checks: {words}.", ids,
                ask="" if pts == 2 else "Ask for evidence behind the claims that could not be confirmed.")


def scorecard(sig: dict | None, facts: dict, as_of: date | None = None,
              extra_flags: list[str] | None = None) -> dict[str, Any]:
    """as_of: the date the brief's data was collected (a round older than STALE_ROUND_MONTHS before it is open).
    extra_flags: findings from the OSINT checks (dd.osint.view) to read before a call."""
    sig = sig or {}
    fu, th = sig.get("funding") or {}, sig.get("thesis") or {}
    rows = [_sector(th), _geography(th), _round(fu.get("rounds") or [], as_of or date.today()), _traction(fu, sig),
            _finances(fu),
            _technology(fu, sig, facts), _claims(sig)]
    lo, hi = sum(r["min"] for r in rows), sum(r["max"] for r in rows)
    total = MAX_POINTS * len(rows)
    if lo >= BAR:
        verdict, tone = "Passes to a first call", "pass"
    elif hi < BAR:
        verdict, tone = "Below the bar, even if every open point comes out well", "below"
    else:
        verdict, tone = (f"Open: needs {BAR - lo} more point(s) from "
                         + ", ".join(r["name"].lower() for r in rows if r["open"])), "open"
    flags = []
    for p in th.get("portfolio_overlap") or []:
        flags.append(f"Possible overlap with portfolio company {str(p.get('name', '')).split(' (')[0]}: compare "
                     "product and buyer before a call.")
    ins = [f for f in facts.values() if f.type == "insolvency" and isinstance(f.value, dict)
           and (f.value.get("records_found") or 0) > 0]
    if ins:
        flags.append("Insolvency register has records for the company: read them before a call.")
    flags += [f for f in extra_flags or [] if f not in flags]
    return {"rows": rows, "min": lo, "max": hi, "total": total, "bar": BAR, "verdict": verdict, "tone": tone,
            "flags": flags, "asks": [r["ask"] for r in rows if r["ask"]],
            "fund": FUND["name"], "not_scored": "Team and founders: public records cannot judge them; assess them "
                                                "first on the call."}
