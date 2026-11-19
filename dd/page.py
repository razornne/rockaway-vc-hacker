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


STAGES = ((r"pre-?seed", 1), (r"\bseed", 2), (r"series\s*a\b", 3), (r"series\s*b\b", 4), (r"series\s*c\b", 5),
          (r"growth|series\s*[d-z]\b", 6))


def _stage(name: Any) -> int:
    n = str(name or "").lower()
    return next((rank for pat, rank in STAGES if re.search(pat, n)), 0)  # first match: "pre-seed" before "seed"


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
    if closed:
        r = sorted(closed, key=lambda r: r.get("date") or "")[-1]
        tiles.append({"label": "Last closed round", "value": r.get("amount") or "amount not stated",
                      "sub": " · ".join(x for x in (r.get("round"), r.get("date"), ", ".join(r.get("investors") or [])[:60]) if x),
                      "nums": refs.add(r["fact_ids"][:3])})
    if rounds and not sought and not closed:  # older analyses: rounds without a sought/closed status
        # latest by stage, then date: a dated article can be about an earlier round
        r = sorted(rounds, key=lambda r: (_stage(r.get("round")), r.get("date") or ""))[-1]
        tiles.append({"label": "Latest reported round", "value": r.get("amount") or "amount not stated",
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
    tiles.append({"label": "Grants & subsidies (not revenue)",
                  "value": _czk(grants) if grants else ("amount not published" if pm.get("grants") else
                                                        "None found" if cz_subsidies else "Not checked"),
                  "sub": (f"{pm.get('grants', 0)} grant(s) · {(kinds.get('subsidy') or {}).get('count', 0)} subsidy agreement(s)"
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
        money_rows.append({"kind": "Grants (subsidy registers, CORDIS, EU portal)", "meaning": "public funding, not revenue",
                           "count": pm["grants"], "czk": _czk(pm.get("grants_czk")),
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
        if f.type in ("grant_national", "grant_eu") and v.get("amount_czk") and f.extractor == "public_money":
            y = _year(v.get("year") or f.event_date)
            if y:
                by_year[y]["grants"] += float(v["amount_czk"])
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
    latest = (sorted(sought, key=lambda r: r.get("date") or "")[-1:] or sorted(closed, key=lambda r: r.get("date") or "")[-1:])
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
            {"criterion": "Stage & ticket", "fund": f"{fund.get('stage')}; initial ticket EUR "
                                                     f"{fund['initial_ticket_eur'][0] / 1e6:g}–{fund['initial_ticket_eur'][1] / 1e6:g}m",
             "company": (f"{STATUS_TEXT.get(latest[0].get('status'), '')}: {latest[0].get('amount') or 'amount n/a'}"
                         f" ({latest[0].get('round') or 'round n/a'})") if latest else "no round in sources",
             "nums": refs.add(latest[0]["fact_ids"][:2]) if latest else []},
            {"criterion": "Portfolio overlap", "fund": "existing Rockaway Ventures / Rockaway Defense companies",
             "company": "; ".join(f"{p['name']} (shared terms: {', '.join(p['shared_terms'][:4])})"
                                  for p in th.get("portfolio_overlap") or []) or "none found by term overlap",
             "nums": []},
        ]
    return {"sales_checked": cz_contracts or ted, "tiles": tiles, "funding": funding_rows, "money": money_rows, "money_chart": chart, "peers": peers,
            "checks": checks, "thesis": thesis_rows, "fund_sources": fund.get("sources") or []}


# ------------------------------------------------------------------ page
CSS = """
:root{color-scheme:light;--ink:#111827;--ink2:#374151;--muted:#6b7280;--line:#e5e7eb;--soft:#f9fafb;--paper:#fff;
--accent:#1d4ed8;--s1:#2a78d6;--s2:#eb6834;
--ok:#047857;--okb:#ecfdf5;--mid:#0e7490;--midb:#ecfeff;--warn:#a16207;--warnb:#fefce8;--bad:#b42318;--badb:#fef3f2;--view:#5b21b6;--viewb:#f5f3ff}
*{box-sizing:border-box}html{background:#f3f4f6}
body{margin:0;color:var(--ink);font:15px/1.6 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased}
.page{max-width:960px;margin:32px auto;background:var(--paper);border:1px solid var(--line);border-radius:12px}
.wrap{padding:40px 56px}
header .kicker{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
h1{font-size:34px;line-height:1.15;margin:0 0 10px;letter-spacing:-.01em}
.oneliner{font-size:18px;color:var(--ink2);margin:0 0 14px;max-width:760px}
.meta{font-size:13px;color:var(--muted)}.meta span+span:before{content:"·";margin:0 8px}
.trust{margin:22px 0 0;padding:12px 16px;background:var(--soft);border:1px solid var(--line);border-radius:8px;font-size:13px;color:var(--ink2)}
.trust b{color:var(--ink)}
h2{font-size:20px;margin:44px 0 6px;letter-spacing:-.005em}
.h2note{font-size:13px;color:var(--muted);margin:0 0 16px}
h3{font-size:15px;margin:24px 0 8px}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px}
.tile{border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.tile .l{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
.tile .v{font-size:21px;font-weight:650;margin:4px 0 2px;line-height:1.25}
.tile .s{font-size:12.5px;color:var(--muted)}.tile.muted .v{color:var(--muted);font-weight:500}
.tile.warn{border-color:#fde68a;background:#fffdf5}
ul.items{list-style:none;padding:0;margin:0}ul.items li{padding:10px 0;border-top:1px solid var(--line)}
ul.items li:first-child{border-top:0}
.lab{font-weight:650}
.assume{display:block;font-size:12.5px;color:var(--muted);margin-top:2px}
.ev{display:inline-block;font-size:11px;font-weight:600;padding:1px 7px;border-radius:4px;margin-right:6px;vertical-align:1px;white-space:nowrap;cursor:help}
.ev-verified{color:var(--ok);background:var(--okb)}.ev-corroborated{color:var(--mid);background:var(--midb)}
.ev-single,.ev-mixed{color:var(--warn);background:var(--warnb)}.ev-claim{color:var(--bad);background:var(--badb)}.ev-view{color:var(--view);background:var(--viewb)}
sup.r{font-size:10.5px;margin-left:2px;white-space:nowrap}sup.r a{color:var(--accent);text-decoration:none;font-weight:600}
sup.r a:hover{text-decoration:underline}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.col{border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.col h3{margin:0 0 6px;font-size:13px;text-transform:uppercase;letter-spacing:.05em}
.col.for h3{color:var(--ok)}.col.against h3{color:var(--bad)}.col.must h3{color:var(--ink2)}
.col ul.items li{padding:8px 0;font-size:14px}
table.t{width:100%;border-collapse:collapse;font-size:13.5px;margin:6px 0 4px}
table.t th{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);text-align:left;font-weight:600;padding:8px 10px;border-bottom:1px solid var(--line)}
table.t td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
table.t td.num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.pill{font-size:11.5px;font-weight:600;padding:1px 7px;border-radius:4px;background:var(--soft);border:1px solid var(--line);white-space:nowrap}
.pill.sought{color:var(--warn);background:var(--warnb);border-color:#fde68a}.pill.closed{color:var(--ok);background:var(--okb);border-color:#a7f3d0}
.pill.contradicted{color:var(--bad);background:var(--badb);border-color:#fecdca}.pill.confirmed{color:var(--ok);background:var(--okb);border-color:#a7f3d0}
.chart{margin:10px 0 6px}.legend{display:flex;gap:16px;font-size:12.5px;color:var(--ink2);margin-bottom:8px}
.legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:-1px}
.bars{display:flex;align-items:flex-end;gap:10px;height:170px;border-bottom:1px solid #d1d5db;padding:18px 4px 0}
.tot{position:absolute;left:0;right:0;text-align:center;font-size:11.5px;color:var(--ink2);margin-bottom:2px;transform:translateY(-100%)}
.bar{flex:1;display:flex;flex-direction:column-reverse;align-items:stretch;gap:2px;height:100%;position:relative;min-width:18px}
.seg.top{border-radius:4px 4px 0 0}
.bar:hover .seg{filter:brightness(.92)}
.bar .tip{display:none;position:absolute;bottom:100%;left:50%;transform:translateX(-50%);background:#111827;color:#fff;font-size:12px;padding:6px 8px;border-radius:6px;white-space:nowrap;z-index:2;margin-bottom:6px}
.bar:hover .tip{display:block}
.years{display:flex;gap:10px;padding:4px 4px 0;font-size:11.5px;color:var(--muted)}.years span{flex:1;text-align:center;min-width:18px}
.evbar{display:flex;height:14px;border-radius:4px;overflow:hidden;gap:2px;margin:8px 0}
.evkey{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:12.5px;color:var(--ink2)}
.tech{border-top:3px solid var(--line);margin-top:48px;padding-top:4px}
ol.src{list-style:none;padding:0;margin:0;font-size:13px}
ol.src li{display:grid;grid-template-columns:30px 1fr;gap:6px;padding:8px 0;border-top:1px solid var(--line);overflow-wrap:anywhere}
ol.src .n{font-weight:700;color:var(--accent)}ol.src .m{color:var(--muted);font-size:12px}ol.src q{color:var(--ink2)}
.cls{font-size:11px;font-weight:600;color:var(--ink2);background:var(--soft);border:1px solid var(--line);padding:0 6px;border-radius:4px}
details{margin-top:14px}summary{cursor:pointer;color:var(--accent);font-size:13.5px}
.fact{padding:6px 0;border-top:1px solid var(--line);font-size:12px;overflow-wrap:anywhere}.fact code{font-size:11px}
.foot{font-size:12.5px;color:var(--muted);margin-top:28px;border-top:1px solid var(--line);padding-top:14px}
.empty{color:var(--muted);font-size:14px}
a{color:var(--accent)}
@media(max-width:760px){.wrap{padding:24px 16px}.page{margin:0;border-radius:0;border:0}.tiles,.cols{grid-template-columns:1fr}h1{font-size:28px}
table.t{display:block;overflow-x:auto}}
@media print{html{background:#fff}.page{border:0;margin:0;max-width:none}details{display:none}.tile,.col,tr{break-inside:avoid}}
"""


def render(company: Company, analysis: dict, p: dict, titles: dict, label_titles: dict, safe_href,
           extraction_cost: float, value_json, fact_status, all_facts: dict[int, Fact]) -> str:
    from dd.render import CLASS_LABELS, STRENGTH
    h = html.escape
    srcs, x = p["sources"], p.get("extras") or {}
    by_kind = {s["kind"]: s for s in p["sections"]}

    def refs(nums):
        if not nums:
            return ""
        links = []
        for n in nums:
            s = srcs[n - 1]
            tip = f"{s['host']} · {CLASS_LABELS[s['cls']]}" + (f" — {s['quote']}" if s["quote"] else "")
            links.append(f'<a href="#src-{n}" title="{h(tip, quote=True)}">{n}</a>')
        return f'<sup class="r">[{", ".join(links)}]</sup>'

    def ev(key, basis):
        lab, expl = STRENGTH[key]
        tip = expl + (f" · based on: {basis}" if basis else "")
        return f'<span class="ev ev-{key}" title="{h(tip, quote=True)}">{h(lab)}</span>'

    def item(it, label=False, badge=True):
        lab = (f'<span class="lab">{h(label_titles.get(it.get("label"), ""))}.</span> '
               if label and it.get("label") else "")
        out = f'<li>{ev(it["strength"], it["basis"]) if badge else ""}{lab}{h(it["text"])}{refs(it["nums"])}'
        out += "".join(f'<span class="assume">Assumes: {h(a)}</span>' for a in it["assumptions"])
        return out + "</li>"

    def section(kind, note=None, label=False, badge=True, title=True):
        s = by_kind.get(kind)
        if not s:
            return ""
        out = (f"<h3>{h(titles[kind])}</h3>" if title else "") + (f'<p class="h2note">{h(note)}</p>' if note else "")
        if s["no_data"]:
            return out + '<p class="empty">No sourced findings.</p>'
        return out + '<ul class="items">' + "".join(item(it, label, badge) for it in s["items"]) + "</ul>"

    def table(head, rows, num_cols=()):
        out = ['<table class="t"><tr>' + "".join(f"<th>{h(c)}</th>" for c in head) + "</tr>"]
        for r in rows:
            out.append("<tr>" + "".join(f'<td class="num">{c}</td>' if i in num_cols else f"<td>{c}</td>"
                                        for i, c in enumerate(r)) + "</tr>")
        return "".join(out) + "</table>"

    ident = p["identity"]
    product = next((it for it in p["tldr"] if it.get("label") == "product"), None)
    parts = ["<!doctype html>", '<html lang="en"><head><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<meta name="robots" content="noindex, nofollow">',
             f"<title>{h(company.name)} — due diligence brief</title><style>{CSS}</style></head><body>",
             '<div class="page"><div class="wrap"><header>',
             '<p class="kicker">Due diligence brief · outside-in, public sources</p>', f"<h1>{h(company.name)}</h1>"]
    if product:
        parts.append(f'<p class="oneliner">{h(product["text"])}{refs(product["nums"])}</p>')
    meta = [company.domain, ident.get("name"), ident.get("ico") and f"IČO {ident['ico']}", company.country,
            f"Data as of {str(analysis.get('generated_at', ''))[:10]}", f"{len(srcs)} sources"]
    parts.append('<div class="meta">' + "".join(f"<span>{h(str(m))}</span>" for m in meta if m) + "</div>")
    parts.append('<div class="trust"><b>How to read.</b> Numbers in brackets link to the source (hover to preview). '
                 "Labels show how strong the evidence is: "
                 + " ".join(f'{ev(k, "")}' for k in STRENGTH)
                 + " Key numbers, tables and charts are computed by code from official records and sources; the "
                 "written findings come from an LLM that may only cite collected facts. This brief prepares a memo; "
                 "it does not recommend an investment.</div></header>")

    if x.get("tiles"):
        parts.append('<h2>Key numbers</h2><p class="h2note">Computed by code from registries, procurement and press. '
                     "No LLM.</p><div class=tiles>")
        for t in x["tiles"]:
            parts.append(f'<div class="tile {t.get("tone", "")}"><div class="l">{h(t["label"])}</div>'
                         f'<div class="v">{h(str(t["value"]))}{refs(t["nums"])}</div><div class="s">{h(t["sub"])}</div></div>')
        parts.append("</div>")

    rest = [it for it in p["tldr"] if it.get("label") != "product"]
    if rest:
        parts.append('<h2>Summary</h2><ul class="items">' + "".join(item(it, label=True) for it in rest) + "</ul>")

    case = by_kind.get("investment_case")
    if case and not case["no_data"]:
        parts.append('<h2>For the memo</h2><p class="h2note">The strongest arguments each way and what diligence must '
                     "confirm. Judgements, each tied to its evidence.</p><div class=cols>")
        for lab, cls, title in (("for", "for", "For"), ("against", "against", "Against"), ("must_be_true", "must", "Must be true")):
            its = [it for it in case["items"] if it.get("label") == lab]
            parts.append(f'<div class="col {cls}"><h3>{title}</h3><ul class="items">'
                         + ("".join(item(it, badge=False) for it in its) or '<li class="empty">—</li>') + "</ul></div>")
        parts.append("</div>")

    invest = any(k in by_kind and not by_kind[k]["no_data"]
                 for k in ("thesis_fit", "business_model", "market", "competition", "investment_case"))
    if invest or x.get("money_chart") or x.get("money"):
        parts.append("<h2>Business</h2>")
    if not invest:
        parts.append('<p class="h2note">This brief was generated before the investment view (business model, market, '
                     "competition) existed. Public money below is computed by code.</p>")
    else:
        parts.append(section("business_model"))
    if x.get("money_chart"):
        mx = max((r["grants"] + r["sales"]) for r in x["money_chart"]) or 1
        parts.append('<h3>Public money by year</h3><p class="h2note">Grants vs. sales to public buyers, by the year '
                     "recorded in the registers (grant years can be project years). Research-project budgets are excluded: "
                     "they are not revenue.</p><div class=chart><div class=legend>"
                     '<span><i style="background:var(--s1)"></i>Grants</span>'
                     '<span><i style="background:var(--s2)"></i>Sales to public buyers</span></div><div class=bars>')
        for r in x["money_chart"]:
            g, s_ = r["grants"], r["sales"]
            vals = [(v, c) for v, c in ((g, "--s1"), (s_, "--s2")) if v]
            segs = "".join(f'<div class="seg{" top" if i == len(vals) - 1 else ""}" style="height:{v / mx * 100:.2f}%;'
                           f'background:var({c})"></div>' for i, (v, c) in enumerate(vals))
            lab = f'<div class="tot" style="bottom:{(g + s_) / mx * 100:.2f}%">{_short(g + s_)}</div>' if g + s_ else ""
            parts.append(f'<div class="bar">{segs}{lab}<div class="tip">{r["year"]}: grants {_czk(g)} · sales {_czk(s_)}</div></div>')
        tg_, ts_ = sum(r["grants"] for r in x["money_chart"]), sum(r["sales"] for r in x["money_chart"])
        parts.append('</div><div class=years>' + "".join(f"<span>{r['year']}</span>" for r in x["money_chart"]) + "</div>"
                     f'<p class="h2note" style="margin-top:8px">Total over these years: grants {_czk(tg_)}'
                     + (f"; sales to public buyers {_czk(ts_)} ({_pct(ts_ / (tg_ + ts_))} of the public money)" if ts_ else
                        ("; no sales to public buyers found" if x.get("sales_checked") else
                                                     "; sales to public buyers not checked")) + ".</p></div>")
    if x.get("money"):
        parts.append("<h3>Public money by type</h3>" + table(
            ["Type", "What it means", "Count", "Amount", "Src"],
            [[h(r["kind"]), h(r["meaning"]), str(r["count"]), h(r["czk"]), refs(r["nums"])] for r in x["money"]], (2, 3)))
    if invest:
        parts.append(section("market", "Only statements found in sources, attributed to who makes them. No market size "
                                       "is estimated here."))
    if invest or x.get("peers"):
        parts.append("<h2>Competition</h2>")
    if invest:
        parts.append(section("competition", title=False))
    if x.get("peers"):
        parts.append('<h3>Candidates from NATO DIANA cohorts</h3><p class="h2note">Companies selected by NATO DIANA '
                     "whose one-line description overlaps this company's website (matched by code). Candidates to check, "
                     "not confirmed competitors.</p>" + table(
                         ["Company", "Country", "NATO DIANA description", "Cohort", "Src"],
                         [[h(r["name"]), h(r["country"]), h(r["description"]), str(r["year"] or ""), refs(r["nums"])]
                          for r in x["peers"]]))

    if x.get("thesis") or (by_kind.get("thesis_fit") and not by_kind["thesis_fit"]["no_data"]):
        parts.append("<h2>Fit with the Rockaway thesis</h2>")
        if x.get("thesis"):
            fund_links = ", ".join(f'<a href="{h(u, quote=True)}" rel="noopener noreferrer">{i + 1}</a>'
                                   for i, u in enumerate(x.get("fund_sources") or []) if safe_href(u))
            parts.append(f'<p class="h2note">Fund profile from public statements ({fund_links}); company side computed '
                         "by code.</p>" + table(["", "Rockaway Ventures", "This company", "Src"],
                                                [[f"<b>{h(r['criterion'])}</b>", h(r["fund"]), h(r["company"]), refs(r["nums"])]
                                                 for r in x["thesis"]]))
        parts.append(section("thesis_fit", label=True).replace("<h3>Fit with the Rockaway thesis</h3>", "<h3>Assessment</h3>"))

    if x.get("funding"):
        parts.append('<h2>Funding history</h2><p class="h2note">Every reported round, as worded in the source. '
                     "<b>Sought</b> = money the company is asking for; <b>Closed</b> = money reported as received.</p>"
                     + table(["Date", "Round", "Amount (as reported)", "Investors", "Status", "Src"],
                             [[h(r["date"]), h(r["round"]), h(r["amount"]), h(r["investors"]),
                               f'<span class="pill {r["status"]}">{STATUS_TEXT.get(r["status"], r["status"])}</span>'
                               + (f' <span class="m">{r["reports"]} reports</span>' if r["reports"] > 1 else ""),
                               refs(r["nums"])] for r in x["funding"]]))

    parts.append('<div class="tech"><h2>Technical due diligence</h2><p class="h2note">What is built, who owns it, '
                 "what could be rebuilt, and what to verify.</p>")
    parts.append(section("ownership"))
    parts.append(section("tech_profile"))
    parts.append(section("rebuild_check", label=True))
    if x.get("checks"):
        parts.append("<h3>Claims checked against independent sources</h3>" + table(
            ["Check", "Result", "Detail", "Src"],
            [[h(c["check"]), f'<span class="pill {h(str(c["status"]))}">{h(CHECK_TEXT.get(c["status"], str(c["status"])))}</span>',
              h(c["detail"]), refs(c["nums"])] for c in x["checks"]]))
    parts.append(section("risk_flags"))
    parts.append(section("questions", badge=False))
    parts.append("</div>")

    # evidence quality: how much of this brief rests on what
    counts = Counter(it["strength"] for it in p["tldr"] + [it for s in p["sections"] for it in s["items"]])
    total = sum(counts.values())
    if total:
        colors = {"verified": "#047857", "corroborated": "#0e7490", "single": "#ca8a04", "mixed": "#eab308",
                  "claim": "#b42318", "view": "#7c3aed"}
        parts.append('<h2>Evidence behind this brief</h2><p class="h2note">All findings above by the strength of their '
                     "evidence. Analyst views are expected in risks, the case for and against, and questions.</p>"
                     '<div class="evbar">' + "".join(
                         f'<div style="flex:{counts[k]};background:{colors[k]}" title="{h(STRENGTH[k][0])}: {counts[k]}"></div>'
                         for k in STRENGTH if counts.get(k)) + '</div><div class="evkey">' + "".join(
                         f'<span><i style="display:inline-block;width:10px;height:10px;border-radius:2px;background:{colors[k]};'
                         f'margin-right:6px"></i>{h(STRENGTH[k][0])} {counts[k]} ({counts[k] / total:.0%})</span>'
                         for k in STRENGTH if counts.get(k)) + "</div>")

    parts.append('<h2>Sources</h2><ol class="src">')
    for s in srcs:
        url = safe_href(s["url"])
        link = (f'<a href="{h(url, quote=True)}" rel="noopener noreferrer" target="_blank">{h(s["host"])} ↗</a>'
                if url else h(s["host"]))
        date = f" · {h(s['date'])}" if s["date"] else ""
        q = f"<br><q>{h(s['quote'])}</q>" if s["quote"] else ""
        parts.append(f'<li id="src-{s["n"]}"><span class="n">{s["n"]}</span><div>{link} '
                     f'<span class="cls">{h(CLASS_LABELS[s["cls"]])}</span> <span class="m">{h(s["type"])}{date}</span>{q}</div></li>')
    parts.append("</ol>")
    parts.append('<h2>How this dossier was built</h2>' + table(
        ["Step", "What it reads", "Facts", "Unavailable this run"],
        [[f"<b>{h(n)}</b>", h(w), str(c), h(", ".join(u)) if u else "—"] for n, w, c, u in p["method"]], (2,)))
    parts.append(f'<p class="foot">Analysis model {h(str(analysis.get("model") or "unknown"))} · analysis cost '
                 f'${float(analysis.get("cost_usd") or 0):.4f} · AI extraction cost ${extraction_cost:.4f}. Structured sources '
                 "(registries, procurement, DNS, GitHub…) are parsed by code; the LLM only extracts quoted facts from text "
                 "and writes the findings, each tied to cited sources. Outside-in assessment from public data; it does "
                 "not replace access to the company's code, data, financials and contracts.</p>")
    parts.append(f"<details><summary>Source appendix — all {len(all_facts)} collected facts, incl. checks and "
                 "unavailable sources</summary>")
    for fid in sorted(all_facts):
        f = all_facts[fid]
        url = safe_href(f.source_url)
        src = (f'<a href="{h(url, quote=True)}" rel="noopener noreferrer">{h(f.source_url)}</a>' if url
               else h(f.source_url or "(no URL)"))
        parts.append(f'<div class="fact" id="fact-{fid}"><b>F{fid}</b> · {h(f.type)} · {h(fact_status(f))} · {src}'
                     f"<br><code>{h(value_json(f.value))}</code></div>")
    parts.append("</details></div></div></body></html>")
    return "\n".join(parts)
