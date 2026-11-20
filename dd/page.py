"""The dossier as a page an investor can read in two minutes and verify in ten.

Reading order: what the company does → key numbers (code) → summary → the case for and against → business model,
market, competition, thesis fit → funding history → technical diligence → questions → sources. Every number and
statement keeps its source reference; tables and charts are computed by code from facts, never by the LLM.
"""
from __future__ import annotations

import html
import re
from collections import Counter, defaultdict
from typing import Any

from dd.store import Company, Fact

KIND_TEXT = {
    "purchase": ("Purchases by public buyers", "a public body paid for a product or service"),
    "rd_project": ("R&D project agreements", "research consortium / results agreements; the amount is a project "
                                             "budget, not the company's revenue"),
    "subsidy": ("Subsidy agreements", "support or subsidised services"),
    "loan": ("Device loans", "equipment lent for testing; no sale"),
    "other": ("Other contracts", "purpose not clear from the subject line"),
}
STATUS_TEXT = {"sought": "Sought", "closed": "Closed", "reported": "Reported"}
CHECK_TEXT = {"confirmed": "Confirmed", "partly": "Partly confirmed", "contradicted": "Contradicted",
              "not_found": "Not found", "not_checkable": "Not checkable", "info": "Info"}


def _czk(x: float | int | None) -> str:
    if not x:
        return "—"
    x = float(x)
    if x >= 1e6:
        return f"{x / 1e6:,.1f}M CZK"
    return f"{x:,.0f} CZK".replace(",", " ")


def _pct(x: float) -> str:
    return f"{x:.1%}" if 0 < x < 0.1 else f"{x:.0%}"


def _short(x: float) -> str:
    return f"{x / 1e6:.1f}M" if x >= 1e5 else f"{x / 1e3:.0f}k"


from dd.thesis import last_round, stage_rank as _stage, stage_ticket  # noqa: E402,F401  (round choice lives with the ticket logic)


def _year(s: Any) -> int | None:
    m = re.search(r"(19|20)\d\d", str(s or ""))
    return int(m.group(0)) if m else None


# ------------------------------------------------------------------ data (called from render.prepare)
def extras(sig: dict, facts: dict[int, Fact], refs, company: Company) -> dict:
    sig = sig or {}
    fu, de = sig.get("funding") or {}, sig.get("defence") or {}
    pm = fu.get("public_money") or {}
    kinds = pm.get("contract_kinds") or {}
    tg, tl, th = sig.get("team_gtm") or {}, sig.get("timeline") or {}, sig.get("thesis") or {}
    rounds = fu.get("rounds") or []
    tiles = []

    sought = [r for r in rounds if r.get("status") == "sought"]
    closed = [r for r in rounds if r.get("status") == "closed"]
    if sought:
        r = sorted(sought, key=lambda r: r.get("date") or "")[-1]
        n = len({str(x.get("amount")) for x in sought if x.get("amount")})
        tiles.append({"label": "Raising now (per press)", "value": r.get("amount") or "amount not stated",
                      "sub": (f"{n} different figures reported — see funding table" if n > 1 else
                              f"{r.get('round') or 'round'} · {r.get('date') or 'undated'}"),
                      "nums": refs.add([i for x in sought for i in x["fact_ids"]][:4]), "tone": "warn" if n > 1 else ""})
    r = last_round(rounds)  # stage first: a later article can restate an earlier round (see dd.thesis.last_round)
    if r:
        tiles.append({"label": "Last closed round" if r.get("status") == "closed" else "Latest reported round",
                      "value": r.get("amount") or "amount not stated",
                      "sub": " · ".join(x for x in (r.get("round"), r.get("date"), ", ".join(r.get("investors") or [])[:60]) if x),
                      "nums": refs.add(r["fact_ids"][:3])})
    if not rounds:
        tiles.append({"label": "Funding rounds", "value": "None found", "sub": "no round reported in collected sources",
                      "nums": [], "tone": "muted"})

    tw = de.get("tenders_won") or {}
    pur = kinds.get("purchase") or {}
    acc = de.get("accelerators") or []
    edf = de.get("eu_defence_projects") or {}
    has = {f.type for f in facts.values()} | {f.key for f in facts.values() if f.type == "source_check"}
    checked = [n for k, n in (("ted", "TED (EU procurement)"), ("eu_ft_portal", "EU funding portal"), ("nato_diana", "NATO DIANA"))
               if k in (de.get("checks") or {}) or k in has
               or (k == "ted" and "public_tender" in has) or (k == "eu_ft_portal" and "eu_registration" in has)
               or (k == "nato_diana" and ({"accelerator", "peer_company"} & has))]
    # A source that was not read must never show as "None found" (truthfulness): Czech public money needs an IČO.
    unavail = {f.key: (f.value or {}).get("reason", "") if isinstance(f.value, dict) else ""
               for f in facts.values() if f.type == "source_unavailable"}
    cz_reason = unavail.get("hlidac_statu")
    cz_contracts = cz_reason is None and "hlidac_contracts" not in unavail
    cz_subsidies = cz_reason is None and "hlidac_subsidies" not in unavail
    why = f"Czech public money not checked: {cz_reason or 'source unavailable'}"
    ted = "TED (EU procurement)" in checked

    sales = float(pur.get("czk") or 0) + float((tw.get("value_by_currency") or {}).get("CZK") or 0)
    sub = [f"{pur.get('count', 0)} purchase contract(s)" if cz_contracts else "Czech contracts not checked",
           f"{tw.get('count', 0)} won EU tender(s)" if ted else "EU tenders not checked"]
    tiles.append({"label": "Sales to public buyers",
                  "value": _czk(sales) if sales else ("None found" if cz_contracts or ted else "Not checked"),
                  "sub": " · ".join(sub) if cz_contracts or ted else why,
                  "nums": refs.add((pur.get("fact_ids") or [])[:3] + (tw.get("fact_ids") or [])[:2]),
                  "tone": "" if sales else "muted"})
    sub_czk = float((kinds.get("subsidy") or {}).get("czk") or 0)
    grants = float(pm.get("grants_czk") or 0) + sub_czk
    paid = float(pm.get("grants_paid_czk") or 0)
    tiles.append({"label": "Grants & subsidies awarded (not revenue)",
                  "value": _czk(grants) if grants else ("amount not published" if pm.get("grants") else
                                                        "None found" if cz_subsidies else "Not checked"),
                  "sub": ((f"{pm.get('grants', 0)} project(s), multi-year · "
                           + (f"{_czk(paid)} paid out so far per payment records" if paid else "payments by year not published"))
                          if cz_subsidies or grants else why),
                  "nums": refs.add([f.id for f in facts.values() if f.type in ("grant_national", "grant_eu")][:3]),
                  "tone": "" if grants else "muted"})

    bits = ([f"{tw['defence_buyer']} defence-ministry contract(s)"] if tw.get("defence_buyer") else [])         + [f"{a.get('programme')} {a.get('year')}" for a in acc] + ([f"{edf['count']} EDF project(s)"] if edf.get("count") else [])
    tiles.append({"label": "Defence evidence (official sources)",
                  "value": " · ".join(bits) if bits else ("None found" if checked else "Not checked"),
                  "sub": "checked: " + ", ".join(checked) if checked else "TED, EU funding portal and NATO DIANA not run for this brief",
                  "nums": refs.add((tw.get("fact_ids") or [])[:2] + [i for a in acc for i in a.get("fact_ids", [])]
                                   + (edf.get("fact_ids") or [])[:2]), "tone": "" if bits else "muted"})
    if tg.get("open_roles"):
        by = tg.get("by_function") or {}
        tiles.append({"label": "Open roles", "value": str(tg["open_roles"]),
                      "sub": ", ".join(f"{k.replace('_', ' ')} {v['count']}" for k, v in by.items()),
                      "nums": refs.add([i for v in by.values() for i in v.get("fact_ids", [])][:3])})
    if tl.get("incorporated"):
        tiles.append({"label": "Registered", "value": str(tl["incorporated"])[:4],
                      "sub": f"Czech registry · first press {tl.get('first_press') or 'n/a'}",
                      "nums": refs.add(tl.get("incorporated_fact_ids") or [])})

    funding_rows = [{"date": r.get("date") or "undated", "round": r.get("round") or "—", "amount": r.get("amount") or "—",
                     "investors": ", ".join(r.get("investors") or []) or "—", "status": r.get("status", "reported"),
                     "reports": r.get("reports", 1), "nums": refs.add(r["fact_ids"][:4])}
                    for r in sorted(rounds, key=lambda r: r.get("date") or "9999")]

    money_rows = []
    for k in ("purchase", "rd_project", "subsidy", "loan", "other"):
        if k in kinds:
            money_rows.append({"kind": KIND_TEXT[k][0], "meaning": KIND_TEXT[k][1], "count": kinds[k]["count"],
                               "czk": "budget, not revenue" if k == "rd_project" else _czk(kinds[k].get("czk")),
                               "nums": refs.add(kinds[k].get("fact_ids", [])[:3])})
    if pm.get("grants"):
        money_rows.append({"kind": "Grants (subsidy registers, CORDIS, EU portal)",
                           "meaning": "public funding awarded to the company for whole projects, not revenue; one row per "
                                      "project even when several registers list it",
                           "count": pm["grants"],
                           "czk": f"awarded {_czk(pm.get('grants_czk'))}"
                                  + (f"; paid so far {_czk(pm.get('grants_paid_czk'))}" if pm.get("grants_paid_czk") else ""),
                           "nums": refs.add([f.id for f in facts.values() if f.type in ("grant_national", "grant_eu")][:3])})
    if tw.get("count"):
        money_rows.append({"kind": "Won EU public tenders (TED)", "meaning": "the company won a public procurement; "
                           + ("buyer: " + ", ".join(tw.get("buyers") or []) if tw.get("buyers") else ""),
                           "count": tw["count"], "czk": _czk((tw.get("value_by_currency") or {}).get("CZK")),
                           "nums": refs.add((tw.get("fact_ids") or [])[:3])})

    from dd.signals import contract_kind
    by_year: dict[int, dict[str, float]] = defaultdict(lambda: {"grants": 0.0, "sales": 0.0})
    for f in facts.values():
        v = f.value if isinstance(f.value, dict) else {}
        if f.type in ("grant_national", "grant_eu") and f.extractor == "public_money":
            # only actual payments have a year: an award's register year can be a programme year (even 2028)
            for p in v.get("paid_by_year") or []:
                if _year(p.get("year")) and p.get("amount_czk"):
                    by_year[_year(p["year"])]["grants"] += float(p["amount_czk"])
        elif f.type == "gov_contract" and contract_kind(f) == "purchase" and v.get("amount_czk"):
            y = _year(v.get("signed") or f.event_date)
            if y:
                by_year[y]["sales"] += float(v["amount_czk"])
        elif f.type == "public_tender" and v.get("role") == "winner" and v.get("currency") == "CZK" and v.get("value"):
            y = _year(f.event_date)
            if y:
                by_year[y]["sales"] += float(v["value"])
    years = sorted(by_year)
    chart = [{"year": y, "grants": by_year[y]["grants"] if y in by_year else 0.0,
              "sales": by_year[y]["sales"] if y in by_year else 0.0}
             for y in range(years[0], years[-1] + 1)] if years else []

    peers = [{"name": f.value.get("name"), "country": f.value.get("country") or "—",
              "description": f.value.get("description") or "—", "year": f.value.get("year"),
              "nums": refs.add([f.id])}
             for f in sorted((f for f in facts.values() if f.type == "peer_company" and isinstance(f.value, dict)),
                             key=lambda f: -float(f.value.get("overlap") or 0))[:8]]

    checks = [{"check": str(c.get("check") or "").replace("_", " "), "status": c.get("status"),
               "detail": c.get("detail") or c.get("subject") or "", "nums": refs.add((c.get("fact_ids") or [])[:3])}
              for c in sig.get("verification") or []]

    fund = th.get("fund") or {}
    secs = th.get("sectors") or []
    st = stage_ticket(rounds)  # recomputed at render time, so briefs analysed earlier get the same arithmetic
    thesis_rows = []
    if fund:
        thesis_rows = [
            {"criterion": "Sector", "fund": ", ".join(fund.get("sectors") or []),
             "company": "; ".join(f"{s['sector']} ({s['evidence']} facts"
                                  + (", incl. official defence records" if s.get("structured_evidence_fact_ids") else "") + ")"
                                  for s in secs) or "no thesis sector evidenced",
             "nums": refs.add([i for s in secs[:3] for i in s.get("fact_ids", [])[:2]])},
            {"criterion": "Geography", "fund": fund.get("geography", ""),
             "company": ((th.get("geography") or {}).get("country") or "unknown")
                        + (" — core region" if (th.get("geography") or {}).get("in_core_region") else ""),
             "nums": refs.add((th.get("geography") or {}).get("fact_ids") or [])},
            {"criterion": "Stage & ticket (computed by code)",
             "fund": f"{fund.get('stage')}; initial ticket EUR "
                     f"{fund['initial_ticket_eur'][0] / 1e6:g}–{fund['initial_ticket_eur'][1] / 1e6:g}m",
             "company": st["text"], "nums": refs.add(st.get("fact_ids", [])[:2])},
            {"criterion": "Portfolio overlap", "fund": "existing Rockaway Ventures / Rockaway Defense companies",
             "company": "; ".join(f"{p['name']} (shared terms: {', '.join(p['shared_terms'][:4])})"
                                  for p in th.get("portfolio_overlap") or []) or "none found by term overlap",
             "nums": []},
        ]
    return {"grants_awarded": grants, "grants_paid": paid, "sales_checked": cz_contracts or ted, "tiles": tiles, "funding": funding_rows, "money": money_rows, "money_chart": chart, "peers": peers,
            "checks": checks, "thesis": thesis_rows, "fund_sources": fund.get("sources") or []}


# ------------------------------------------------------------------ page
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;'
         '0,6..72,500;0,6..72,600;1,6..72,400&family=Public+Sans:wght@400;500;600&display=swap">')

# Design: an outside-in research brief. The argument runs down the left column in a reading serif; every statement's
# evidence (a Harvey-ball mark for how strong it is, and its source numbers) sits level with it in a right margin,
# so a reader can follow the story and check any line without leaving it. Numbers and tables are set in Public Sans.
CSS = """
:root{color-scheme:light;--paper:#fff;--ink:#1e242b;--ink2:#3d4650;--muted:#6a737d;--rule:#dcdfe3;--wash:#f4f5f6;
--accent:#1b5e63;--brick:#9e3b2a;--ochre:#8a6a12;--s1:#2f6fa8;--s2:#b97a1a;
--serif:"Newsreader",Georgia,"Times New Roman",serif;--sans:"Public Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
--margin:13.5rem;--gap:2.5rem}
*{box-sizing:border-box}
html{background:var(--paper)}
body{margin:0;color:var(--ink);background:var(--paper);font:400 17px/1.62 var(--serif);font-optical-sizing:auto;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:var(--accent);text-underline-offset:2px;text-decoration-thickness:1px}
a:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}
.page{max-width:calc(43rem + var(--margin) + var(--gap) + 6rem);margin:0 auto;padding:0 3rem 5rem}
.crumb{font:500 14px/1 var(--sans);padding:1.6rem 0 0}.crumb a{text-decoration:none}
header{padding:3.2rem 0 1.4rem}
h1{font:500 3rem/1.04 var(--serif);letter-spacing:-.015em;margin:0 0 .9rem;font-variation-settings:"opsz" 72}
.oneliner{font-size:1.32rem;line-height:1.42;color:var(--ink2);margin:0 0 1.6rem;max-width:40rem}
dl.facts{display:flex;flex-wrap:wrap;gap:.4rem 2.2rem;margin:0;font:14px/1.4 var(--sans)}
dl.facts div{display:flex;flex-direction:column}
dl.facts dt{color:var(--muted);font-size:12.5px}dl.facts dd{margin:0;color:var(--ink)}
.key{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1.4rem;margin:2rem 0 0;padding:.9rem 0 0;
border-top:1px solid var(--rule);font:13px/1.4 var(--sans);color:var(--ink2)}
.key .k{display:inline-flex;align-items:center;gap:.45rem}
.key p{flex-basis:100%;margin:.2rem 0 0;color:var(--muted)}
h2{font:500 1.75rem/1.2 var(--serif);letter-spacing:-.01em;margin:3.6rem 0 .3rem;padding-top:1.2rem;border-top:1px solid var(--ink)}
.h2note{font:14px/1.5 var(--sans);color:var(--muted);margin:0 0 1.2rem;max-width:43rem}
h3{font:600 15px/1.3 var(--sans);margin:2rem 0 .5rem;color:var(--ink)}
h3.against{color:var(--brick)}h3.must{color:var(--accent)}
.row{display:grid;grid-template-columns:minmax(0,43rem) var(--margin);column-gap:var(--gap);padding:.75rem 0;
border-top:1px solid var(--rule)}
.row:first-of-type{border-top:0}
.txt{max-width:43rem}
.lead{font-weight:600}
.assume{display:block;font:italic 400 14.5px/1.45 var(--serif);color:var(--muted);margin-top:.25rem}
.proof{font:12.5px/1.45 var(--sans);color:var(--muted);padding-top:.32rem}
.proof .ev{color:var(--ink2);margin-left:.4rem}
.proof .src{display:block;margin:.1rem 0 0 1.25rem}
.src a{font-weight:500;text-decoration:none}.src a:hover{text-decoration:underline}
.mk{display:inline-block;width:.78rem;height:.78rem;border-radius:50%;border:1.5px solid var(--ink);vertical-align:-1px;flex:none}
.mk-verified{background:var(--ink)}
.mk-corroborated{background:conic-gradient(var(--ink) 0 75%,transparent 0)}
.mk-mixed{background:conic-gradient(var(--ink) 0 25%,transparent 0)}
.mk-single{background:conic-gradient(var(--ink) 0 50%,transparent 0)}
.mk-claim{background:transparent}
.mk-view{border-radius:1px;transform:rotate(45deg) scale(.8);border-color:var(--muted)}
.empty{font:14px var(--sans);color:var(--muted)}
.ledger .row{align-items:baseline}
.ledger .lab{font:14px/1.35 var(--sans);color:var(--ink2)}
.ledger .val{font:600 1.45rem/1.2 var(--sans);font-variant-numeric:tabular-nums;letter-spacing:-.01em;margin:.15rem 0 .1rem}
.ledger .note{font:13.5px/1.45 var(--sans);color:var(--muted)}
.ledger .muted .val{color:var(--muted);font-weight:500}
.ledger .warn .val{color:var(--ochre)}
.lgrid{display:grid;grid-template-columns:minmax(0,14rem) minmax(0,1fr);column-gap:1.6rem}
table.t{width:100%;border-collapse:collapse;font:14px/1.45 var(--sans);margin:.4rem 0 .6rem}
table.t th{text-align:left;font-weight:600;font-size:13px;color:var(--ink2);padding:.5rem .8rem .5rem 0;border-bottom:1px solid var(--ink)}
table.t td{padding:.6rem .8rem .6rem 0;border-bottom:1px solid var(--rule);vertical-align:top}
table.t td.num,table.t th.num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
table.t td:last-child,table.t th:last-child{padding-right:0}
.st{font-weight:600;white-space:nowrap}.st-sought{color:var(--ochre)}.st-closed,.st-confirmed{color:var(--accent)}
.st-contradicted{color:var(--brick)}.st-not_found,.st-not_checkable,.st-reported{color:var(--muted)}
.m{color:var(--muted);font-size:12.5px}
.chart{margin:.6rem 0 .4rem;max-width:43rem;font-family:var(--sans)}
.legend{display:flex;gap:1.4rem;font-size:13px;color:var(--ink2);margin-bottom:.6rem}
.legend i{display:inline-block;width:.7rem;height:.7rem;margin-right:.4rem;vertical-align:-1px}
.bars{display:flex;align-items:flex-end;gap:.7rem;height:170px;border-bottom:1px solid var(--ink);padding:1.4rem .2rem 0}
.bar{flex:1;display:flex;flex-direction:column-reverse;align-items:stretch;gap:2px;height:100%;position:relative;min-width:18px}
.tot{position:absolute;left:0;right:0;text-align:center;font-size:12px;color:var(--ink2);transform:translateY(-100%);
font-variant-numeric:tabular-nums}
.seg:last-child{border-radius:3px 3px 0 0}
.bar .tip{display:none;position:absolute;bottom:100%;left:50%;transform:translateX(-50%);background:var(--ink);color:#fff;
font-size:12px;padding:.35rem .5rem;white-space:nowrap;z-index:2;margin-bottom:1.4rem}
.bar:hover .tip{display:block}.bar:hover .seg{filter:brightness(.9)}
.years{display:flex;gap:.7rem;padding:.3rem .2rem 0;font-size:12px;color:var(--muted)}.years span{flex:1;text-align:center;min-width:18px}
.chartnote{font:13.5px/1.5 var(--sans);color:var(--ink2);margin:.6rem 0 0}
.rests{font:14px/1.5 var(--sans);color:var(--ink2);display:flex;flex-wrap:wrap;gap:.4rem 1.6rem}
.rests span{display:inline-flex;align-items:center;gap:.45rem}
ol.sources{list-style:none;padding:0;margin:0;font:13.5px/1.5 var(--sans)}
ol.sources li{display:grid;grid-template-columns:2.4rem minmax(0,1fr);padding:.55rem 0;border-top:1px solid var(--rule);overflow-wrap:anywhere}
ol.sources .n{font-weight:600;color:var(--accent);font-variant-numeric:tabular-nums}
ol.sources .m{display:block}ol.sources q{display:block;color:var(--ink2);font-family:var(--serif);font-size:15px;margin-top:.15rem}
ol.sources li:target{background:var(--wash)}
details{margin-top:1.4rem;font:13.5px var(--sans)}summary{cursor:pointer;color:var(--accent)}
.fact{padding:.4rem 0;border-top:1px solid var(--rule);font-size:12px;overflow-wrap:anywhere}.fact code{font-size:11px}
.foot{font:13px/1.55 var(--sans);color:var(--muted);margin-top:2.4rem;border-top:1px solid var(--rule);padding-top:1rem;max-width:43rem}
@media(max-width:900px){:root{--margin:0;--gap:0}.page{padding:0 1rem 3rem}
.row{grid-template-columns:minmax(0,1fr)}.proof{padding-top:.3rem}.proof .src{display:inline;margin-left:.5rem}
h1{font-size:2.3rem}.oneliner{font-size:1.15rem}h2{font-size:1.45rem;margin-top:2.6rem}
.lgrid{grid-template-columns:minmax(0,1fr)}
table.t{display:block;overflow-x:auto}}
@media print{.page{max-width:none;padding:0}details,.crumb{display:none}.row,tr{break-inside:avoid}a{color:var(--ink)}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
"""


def render(company: Company, analysis: dict, p: dict, titles: dict, label_titles: dict, safe_href,
           extraction_cost: float, value_json, fact_status, all_facts: dict[int, Fact]) -> str:
    from dd.render import CLASS_LABELS, STRENGTH
    h = html.escape
    srcs, x = p["sources"], p.get("extras") or {}
    by_kind = {s["kind"]: s for s in p["sections"]}

    def refs(nums, cls="src"):
        if not nums:
            return ""
        links = []
        for n in nums:
            s = srcs[n - 1]
            tip = f"{s['host']} ({CLASS_LABELS[s['cls']]})" + (f": {s['quote']}" if s["quote"] else "")
            links.append(f'<a href="#src-{n}" title="{h(tip, quote=True)}">{n}</a>')
        return f'<span class="{cls}">Sources {", ".join(links)}</span>'

    def mark(key):
        return f'<span class="mk mk-{key}" aria-hidden="true"></span>'

    def proof(it=None, key=None, basis="", nums=()):
        key = key or it["strength"]
        nums = nums or (it["nums"] if it else ())
        basis = basis or (it.get("basis", "") if it else "")
        lab, expl = STRENGTH[key]
        tip = expl + (f". Based on: {basis}" if basis else "")
        return (f'<div class="proof" title="{h(tip, quote=True)}">{mark(key)}<span class="ev">{h(lab)}</span>'
                f'{refs(nums)}</div>')

    def claim(it, label=False):
        lead = (f'<span class="lead">{h(label_titles.get(it.get("label"), ""))}.</span> '
                if label and it.get("label") else "")
        body = f'{lead}{h(it["text"])}' + "".join(f'<span class="assume">Assumes {h(a[:1].lower() + a[1:])}</span>'
                                                  for a in it["assumptions"])
        return f'<div class="row"><div class="txt">{body}</div>{proof(it)}</div>'

    def block(kind, title=None, note=None, label=False, level="h3"):
        s = by_kind.get(kind)
        if not s:
            return ""
        out = (f"<{level}>{h(title or titles[kind])}</{level}>" if title is not False else "")
        out += f'<p class="h2note">{h(note)}</p>' if note else ""
        if s["no_data"]:
            return out + '<p class="empty">No sourced findings.</p>'
        return out + "".join(claim(it, label) for it in s["items"])

    def table(head, rows, num_cols=()):
        out = ['<table class="t"><tr>' + "".join(f'<th{" class=num" if i in num_cols else ""}>{h(c)}</th>'
                                                 for i, c in enumerate(head)) + "</tr>"]
        for r in rows:
            out.append("<tr>" + "".join(f'<td class="num">{c}</td>' if i in num_cols else f"<td>{c}</td>"
                                        for i, c in enumerate(r)) + "</tr>")
        return "".join(out) + "</table>"

    def tref(nums):  # source numbers inside a table cell
        return refs(nums).replace("Sources ", "") if nums else ""

    ident = p["identity"]
    product = next((it for it in p["tldr"] if it.get("label") == "product"), None)
    generated = str(analysis.get("generated_at", ""))[:10]
    parts = ["<!doctype html>", '<html lang="en"><head><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<meta name="robots" content="noindex, nofollow">', FONTS,
             f"<title>{h(company.name)}: due diligence brief</title><style>{CSS}</style></head><body>",
             '<div class="page"><header>', f"<h1>{h(company.name)}</h1>"]
    if product:
        parts.append(f'<p class="oneliner">{h(product["text"])}</p>')
    facts_row = [("Website", company.domain), ("Legal entity", ident.get("name")),
                 ("Company ID (IČO)", ident.get("ico")), ("Country", company.country),
                 ("Data as of", generated), ("Sources cited", str(len(srcs)))]
    parts.append('<dl class="facts">' + "".join(f"<div><dt>{h(k)}</dt><dd>{h(str(v))}</dd></div>"
                                                for k, v in facts_row if v) + "</dl>")
    parts.append('<div class="key">' + "".join(f'<span class="k">{mark(k)}{h(STRENGTH[k][0])}</span>' for k in STRENGTH)
                 + "<p>Each statement shows on its right how strong its evidence is and which sources it rests on; hover "
                 "for the quote. Numbers, tables and charts are computed by code from official records and sources. "
                 "The written findings come from a language model that may only cite collected facts. This brief "
                 "prepares a memo; it does not recommend an investment.</p></div></header>")

    rest = [it for it in p["tldr"] if it.get("label") != "product"]
    if rest:
        parts.append("<h2>In short</h2>" + "".join(claim(it, label=True) for it in rest))

    case = by_kind.get("investment_case")
    if case and not case["no_data"]:
        parts.append('<h2>For the memo</h2><p class="h2note">The strongest arguments each way, and what diligence has '
                     "to confirm. These are judgements, each tied to its evidence.</p>")
        for lab, cls, title in (("for", "for", "For"), ("against", "against", "Against"),
                                ("must_be_true", "must", "Must be true")):
            its = [it for it in case["items"] if it.get("label") == lab]
            if its:
                parts.append(f'<h3 class="{cls}">{title}</h3>' + "".join(claim(it) for it in its))

    if x.get("tiles"):
        parts.append('<h2>Key numbers</h2><p class="h2note">Computed by code from registers, procurement records and '
                     "press. Amounts from the press are quoted as written.</p><div class=ledger>")
        for t in x["tiles"]:
            tone = {"muted": " muted", "warn": " warn"}.get(t.get("tone", ""), "")
            parts.append(f'<div class="row{tone}"><div class="lgrid"><div class="lab">{h(t["label"])}</div>'
                         f'<div><div class="val">{h(str(t["value"]))}</div>'
                         f'<div class="note">{h(str(t["sub"]).replace(" · ", "; "))}</div></div>'
                         f'</div><div class="proof">{refs(t["nums"])}</div></div>')
        parts.append("</div>")

    invest = any(k in by_kind and not by_kind[k]["no_data"]
                 for k in ("thesis_fit", "business_model", "market", "competition", "investment_case"))
    if invest or x.get("money_chart") or x.get("money"):
        parts.append("<h2>Business and public money</h2>")
    if not invest:
        parts.append('<p class="h2note">This brief was generated before the investment view (business model, market, '
                     "competition) existed. Public money below is computed by code.</p>")
    else:
        parts.append(block("business_model"))
    if x.get("money_chart"):
        mx = max((r["grants"] + r["sales"]) for r in x["money_chart"]) or 1
        unpaid = max(float(x.get("grants_awarded") or 0) - float(x.get("grants_paid") or 0), 0)
        parts.append('<h3>Public money received by year</h3><p class="h2note">Grant payments recorded in the Czech '
                     "subsidy payments register (IsRed), and sales to public buyers by contract year. Research-project "
                     "budgets are left out: they are not revenue."
                     + (f" Awarded support without published payments ({_czk(unpaid)}) has no year and is not shown." if unpaid else "")
                     + '</p><div class=chart><div class=legend>'
                     '<span><i style="background:var(--s1)"></i>Grant payments</span>'
                     '<span><i style="background:var(--s2)"></i>Sales to public buyers</span></div><div class=bars>')
        for r in x["money_chart"]:
            g, s_ = r["grants"], r["sales"]
            vals = [(v, c) for v, c in ((g, "--s1"), (s_, "--s2")) if v]
            segs = "".join(f'<div class="seg" style="height:{v / mx * 100:.2f}%;background:var({c})"></div>' for v, c in vals)
            lab = f'<div class="tot" style="bottom:{(g + s_) / mx * 100:.2f}%">{_short(g + s_)}</div>' if g + s_ else ""
            parts.append(f'<div class="bar">{segs}{lab}<div class="tip">{r["year"]}: grant payments {_czk(g)}, '
                         f'sales {_czk(s_)}</div></div>')
        tg_, ts_ = sum(r["grants"] for r in x["money_chart"]), sum(r["sales"] for r in x["money_chart"])
        parts.append('</div><div class=years>' + "".join(f"<span>{r['year']}</span>" for r in x["money_chart"]) + "</div>"
                     f'<p class="chartnote">Over these years: grant payments {_czk(tg_)}'
                     + (f", sales to public buyers {_czk(ts_)} ({_pct(ts_ / (tg_ + ts_))} of the public money)" if ts_ else
                        (", no sales to public buyers found" if x.get("sales_checked") else
                         ", sales to public buyers not checked")) + ".</p></div>")
    if x.get("money"):
        parts.append("<h3>Public money by type</h3>" + table(
            ["Type", "What it means", "Count", "Amount", "Sources"],
            [[h(r["kind"]), h(r["meaning"]), str(r["count"]), h(r["czk"]), tref(r["nums"])] for r in x["money"]], (2,)))

    own = by_kind.get("ownership")
    if x.get("funding") or (own and not own["no_data"]):
        parts.append("<h2>Funding and ownership</h2>")
        if x.get("funding"):
            parts.append('<p class="h2note">Every reported round, worded as in the source. Sought means money the '
                         "company is asking for; closed means money reported as received.</p>"
                         + table(["Date", "Round", "Amount, as reported", "Investors", "Status", "Sources"],
                                 [[h(r["date"]), h(r["round"]), h(r["amount"]), h(r["investors"]),
                                   f'<span class="st st-{r["status"]}">{STATUS_TEXT.get(r["status"], r["status"])}</span>'
                                   + (f' <span class="m">{r["reports"]} reports</span>' if r["reports"] > 1 else ""),
                                   tref(r["nums"])] for r in x["funding"]]))
        parts.append(block("ownership", title="What the register and press show"))

    if invest or x.get("peers"):
        parts.append("<h2>Market and competition</h2>")
    if invest:
        parts.append(block("market", title="Market", note="Only statements found in sources, attributed to who makes "
                                                           "them. No market size is estimated here."))
        parts.append(block("competition", title="Competitors named or found"))
    if x.get("peers"):
        parts.append('<h3>Candidates from NATO DIANA cohorts</h3><p class="h2note">Companies selected by NATO DIANA whose '
                     "one-line description overlaps this company's website, matched by code. Candidates to check, not "
                     "confirmed competitors.</p>" + table(
                         ["Company", "Country", "NATO DIANA description", "Cohort", "Sources"],
                         [[h(r["name"]), h(r["country"]), h(r["description"]), str(r["year"] or ""), tref(r["nums"])]
                          for r in x["peers"]]))

    if x.get("thesis") or (by_kind.get("thesis_fit") and not by_kind["thesis_fit"]["no_data"]):
        parts.append("<h2>Fit with the Rockaway thesis</h2>")
        if x.get("thesis"):
            fund_links = ", ".join(f'<a href="{h(u, quote=True)}" rel="noopener noreferrer">{i + 1}</a>'
                                   for i, u in enumerate(x.get("fund_sources") or []) if safe_href(u))
            parts.append(f'<p class="h2note">The fund side is taken from public statements ({fund_links}); the company '
                         "side is computed by code.</p>" + table(["", "Rockaway Ventures", "This company", "Sources"],
                                                                 [[f"<b>{h(r['criterion'])}</b>", h(r["fund"]), h(r["company"]),
                                                                   tref(r["nums"])] for r in x["thesis"]]))
        parts.append(block("thesis_fit", title="Assessment", label=True))

    parts.append("<h2>Technology</h2>"
                 '<p class="h2note">What is built, what could be rebuilt, and which claims hold up against independent '
                 "sources. An outside view: it says what to ask, not whether the code is good.</p>")
    parts.append(block("tech_profile", title="What is built"))
    parts.append(block("rebuild_check", label=True))
    if x.get("checks"):
        parts.append("<h3>Claims checked against independent sources</h3>" + table(
            ["Check", "Result", "Detail", "Sources"],
            [[h(c["check"]), f'<span class="st st-{h(str(c["status"]))}">{h(CHECK_TEXT.get(c["status"], str(c["status"])))}</span>',
              h(c["detail"]), tref(c["nums"])] for c in x["checks"]]))

    parts.append("<h2>Risks and questions for the founders</h2>")
    parts.append(block("risk_flags", title="Risks"))
    parts.append(block("questions", title="Questions"))

    counts = Counter(it["strength"] for it in p["tldr"] + [it for s in p["sections"] for it in s["items"]])
    total = sum(counts.values())
    if total:
        parts.append('<h2>What this brief rests on</h2><p class="h2note">All statements above by the strength of their '
                     "evidence. Judgements are expected in the case for and against, the rebuild check, risks and "
                     'questions.</p><div class="rests">' + "".join(
                         f"<span>{mark(k)}{h(STRENGTH[k][0])}: {counts[k]} ({counts[k] / total:.0%})</span>"
                         for k in STRENGTH if counts.get(k)) + "</div>")

    parts.append('<h2>Sources</h2><ol class="sources">')
    for s in srcs:
        url = safe_href(s["url"])
        link = (f'<a href="{h(url, quote=True)}" rel="noopener noreferrer" target="_blank">{h(s["host"])}</a>'
                if url else h(s["host"]))
        date = f", {h(s['date'])}" if s["date"] else ""
        q = f"<q>{h(s['quote'])}</q>" if s["quote"] else ""
        parts.append(f'<li id="src-{s["n"]}"><span class="n">{s["n"]}</span><div>{link} '
                     f'<span class="m">{h(CLASS_LABELS[s["cls"]])}, {h(s["type"])}{date}</span>{q}</div></li>')
    parts.append("</ol>")
    parts.append('<h2>How this brief was built</h2>' + table(
        ["Step", "What it reads", "Facts", "Unavailable this run"],
        [[f"<b>{h(n)}</b>", h(w), str(c), h(", ".join(u)) if u else "—"] for n, w, c, u in p["method"]], (2,)))
    parts.append(f'<p class="foot">Analysis model {h(str(analysis.get("model") or "unknown"))}; analysis cost '
                 f'${float(analysis.get("cost_usd") or 0):.4f}; extraction cost ${extraction_cost:.4f}. Structured sources '
                 "(registers, procurement, DNS, GitHub) are parsed by code; the language model only extracts quoted facts "
                 "from text and writes the findings, each tied to cited sources. An outside-in assessment from public "
                 "data: it does not replace access to the company's code, data, financials and contracts.</p>")
    parts.append(f"<details><summary>All {len(all_facts)} collected facts, including checks and unavailable sources"
                 "</summary>")
    for fid in sorted(all_facts):
        f = all_facts[fid]
        url = safe_href(f.source_url)
        src = (f'<a href="{h(url, quote=True)}" rel="noopener noreferrer">{h(f.source_url)}</a>' if url
               else h(f.source_url or "(no URL)"))
        parts.append(f'<div class="fact" id="fact-{fid}"><b>F{fid}</b> {h(f.type)}, {h(fact_status(f))}: {src}'
                     f"<br><code>{h(value_json(f.value))}</code></div>")
    parts.append("</details></div></body></html>")
    return "\n".join(parts)
