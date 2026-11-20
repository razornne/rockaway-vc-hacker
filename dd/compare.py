"""`dd compare`: the same company analysed by several models, side by side, section by section.

The collected facts are identical for every run; only the model that writes the findings differs. Each column shows
what that model wrote, with the evidence mark computed from its cited sources, so a reader can see which model is
more specific, which overstates, and which leaves sections empty. Links open each model's full brief.
"""
from __future__ import annotations

import html
from collections import Counter
from pathlib import Path

from dd import render
from dd.page import CSS, FONTS
from dd.store import Store
from dd.writer import LABEL_TITLES, SECTION_TITLES

h = html.escape
ROWS = (("summary", "In short"), ("investment_case", "Case for and against"), ("thesis_fit", "Fit with the fund"),
        ("business_model", "Business model"), ("market", "Market"), ("competition", "Competition"),
        ("ownership", "Ownership and capital"), ("tech_profile", "What is built"),
        ("rebuild_check", "What could be rebuilt"), ("risk_flags", "Risks"), ("questions", "Questions for founders"))

EXTRA_CSS = """
.page{max-width:none;padding:0 2rem 4rem}
table.cmp{width:100%;border-collapse:collapse;table-layout:fixed;font-size:15px}
table.cmp th,table.cmp td{vertical-align:top;text-align:left;padding:.8rem 1rem .8rem 0;border-top:1px solid var(--rule)}
table.cmp th.sec{font:500 1.15rem/1.3 var(--serif);width:9rem;padding-right:1.4rem}
table.cmp thead th{font:600 14px/1.4 var(--sans);border-top:0;border-bottom:1px solid var(--ink)}
table.cmp thead .m{display:block;font-weight:400;color:var(--muted);font-size:12.5px}
.it{margin:0 0 .75rem;line-height:1.5}.it:last-child{margin-bottom:0}
.it .lab{font-weight:600}
.it .meta{display:block;font:12px/1.4 var(--sans);color:var(--muted);margin-top:.15rem}
.none{font:13px var(--sans);color:var(--brick)}
@media(max-width:900px){table.cmp,table.cmp tbody,table.cmp tr,table.cmp td,table.cmp th{display:block;width:auto}
table.cmp thead{display:none}table.cmp td:before{content:attr(data-model);display:block;font:600 12.5px var(--sans);
color:var(--accent);margin-bottom:.3rem}}
"""


def _runs(store: Store, cid: str, models: list[str]) -> list[tuple[str, str, dict]]:
    published = store.latest_analysis(cid, "dossier")
    out = []
    for m in models:
        if published and published.get("model") == m:
            out.append((m, "dossier", published))
            continue
        a = store.latest_analysis(cid, f"dossier@{m}")
        if a:
            out.append((m, f"dossier@{m}", a))
    return out


def compare_page(store: Store, cid: str, models: list[str], brief_links: dict[str, str] | None = None) -> str:
    company = store.get_company(cid)
    facts = {f.id: f for f in store.facts(cid)}
    runs = _runs(store, cid, models)
    prepared = []
    for m, kind, a in runs:
        p = render.prepare(company, a, a["sections"], facts, [])
        items = p["tldr"] + [it for s in p["sections"] for it in s["items"]]
        prepared.append((m, a, p, items))

    def mark(key):
        return f'<span class="mk mk-{key}" aria-hidden="true"></span>'

    def cell(p, kind):
        if kind == "summary":
            its = [it for it in p["tldr"] if it.get("label") != "product"]
        else:
            s = next((s for s in p["sections"] if s["kind"] == kind), None)
            its = s["items"] if s and not s["no_data"] else []
        if not its:
            return '<span class="none">Nothing accepted for this section</span>'
        out = []
        for it in its:
            lab = LABEL_TITLES.get(it.get("label"), "")
            out.append(f'<p class="it">{f"<span class=lab>{h(lab)}.</span> " if lab else ""}{h(it["text"])}'
                       f'<span class="meta">{mark(it["strength"])} {h(render.STRENGTH[it["strength"]][0])}, '
                       f'{len(it["nums"])} source(s)</span></p>')
        return "".join(out)

    head = ['<th class="sec"></th>']
    for m, a, p, items in prepared:
        words = sum(len(it["text"].split()) for it in items)
        ev = Counter(it["strength"] for it in items)
        firm = ev["verified"] + ev["corroborated"]
        link = (brief_links or {}).get(m)
        name = f'<a href="{h(link, quote=True)}">{h(m)}</a>' if link else h(m)
        head.append(f'<th>{name}<span class="m">${float(a.get("cost_usd") or 0):.3f} for this brief; {len(items)} '
                    f"statements, {words} words; {firm} verified or corroborated, {ev['view']} judgements</span></th>")
    rows = []
    for kind, title in ROWS:
        tds = "".join(f'<td data-model="{h(m)}">{cell(p, kind)}</td>' for m, a, p, items in prepared)
        rows.append(f'<tr><th class="sec">{h(title)}</th>{tds}</tr>')
    body = (f'<header><h1>{h(company.name)}: one brief, {len(prepared)} models</h1>'
            '<p class="oneliner">The same collected facts, analysed by different models. Only the written findings '
            "differ; numbers, tables and checks are computed by code and are identical. The mark after each statement "
            "shows how strong its cited evidence is.</p></header>"
            f'<table class="cmp"><thead><tr>{"".join(head)}</tr></thead><tbody>{"".join(rows)}</tbody></table>')
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            '<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">'
            f"{FONTS}<title>{h(company.name)}: model comparison</title><style>{CSS}{EXTRA_CSS}</style></head><body>"
            f'<div class="page">{body}</div></body></html>')


def write_compare(store: Store, cid: str, models: list[str], out_dir: Path) -> Path:
    from dd.writer import write_dossier
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    company = store.get_company(cid)
    links = {}
    for m, kind, _ in _runs(store, cid, models):
        suffix = "" if kind == "dossier" else f"-{m}"
        paths = write_dossier(store, company, out_dir, kind=kind, suffix=suffix)
        links[m] = Path(paths["html"]).name
    path = out_dir / f"{cid}-compare.html"
    path.write_text(compare_page(store, cid, models, links), encoding="utf-8")
    return path
