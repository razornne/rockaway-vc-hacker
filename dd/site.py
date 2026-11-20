"""`dd site`: a static, read-only showcase (index, method & evaluation, all briefs).

Every number on the pages comes from the same code as the briefs and `dd eval`; nothing is typed in by hand
except the prose. The output folder can be served by any static host; pages carry noindex.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from dd.config import ROOT
from dd.store import Store

h = html.escape

GROUPS = {  # tier in eval/companies.json -> group on the site
    "memo": "Defence / dual-use · outside the Rockaway portfolio",
    "showcase": "Rockaway Ventures portfolio",
    "portfolio": "Rockaway Ventures portfolio",
    "showcase-control": "Comparison companies (not in the Rockaway portfolio)",
    "control": "Comparison companies (not in the Rockaway portfolio)",
}
GROUP_ORDER = list(dict.fromkeys(GROUPS.values()))
FEATURED = ("fly4future", "dronetag")
CARD_TILES = ("Raising now (per press)", "Last closed round", "Funding rounds", "Sales to public buyers",
              "Grants & subsidies (not revenue)", "Defence evidence (official sources)")

SITE_CSS = """
.page{max-width:1000px}
.lead{font-size:18px;color:var(--ink2);max-width:780px;margin:0 0 14px}
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:14px}
.card{border:1px solid var(--line);border-radius:12px;padding:18px 20px;display:flex;flex-direction:column}
.card h3{margin:0;font-size:19px}.card .tag{font-size:12px;color:var(--muted);margin:2px 0 8px}
.card p.one{font-size:14px;color:var(--ink2);margin:0 0 12px}
.card .tiles{grid-template-columns:repeat(2,1fr);gap:8px;margin:0 0 14px}
.card .tile{padding:10px 12px}.card .tile .v{font-size:16px}.card .tile .l{font-size:11px}
.card .go{margin-top:auto;font-weight:600;text-decoration:none}
.steps{margin-top:14px;counter-reset:s;border:1px solid var(--line);border-radius:10px}
.step{display:grid;grid-template-columns:170px 1fr;gap:12px;padding:12px 16px;font-size:14px;color:var(--ink2);border-top:1px solid var(--line)}
.step:first-child{border-top:0}
.step b{color:var(--ink);font-size:14px}
table.t th.num{text-align:right}
.step b:before{counter-increment:s;content:counter(s) ". ";color:var(--muted)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px}
.stat{border:1px solid var(--line);border-radius:10px;padding:14px 16px}
.stat .v{font-size:26px;font-weight:650;line-height:1.2}.stat .l{font-size:13px;color:var(--ink2);margin-top:4px}
ul.plain{margin:8px 0 0;padding-left:20px}ul.plain li{margin:6px 0}
.crumb{max-width:1000px;margin:20px auto -16px;font-size:13.5px}
.nav{font-size:13.5px;margin-bottom:18px}.nav a{margin-right:16px}
@media(max-width:760px){.cards,.stats,.step{grid-template-columns:1fr}.card .tiles{grid-template-columns:1fr}}
"""

NOINDEX = '<meta name="robots" content="noindex, nofollow">'


def _companies_meta() -> dict[str, dict]:
    rows = json.loads((ROOT / "eval" / "companies.json").read_text(encoding="utf-8"))
    return {r["id"]: r for r in rows}


def _shell(title: str, body: str) -> str:
    from dd.page import CSS
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            '<meta name="viewport" content="width=device-width, initial-scale=1">' + NOINDEX +
            f"<title>{h(title)}</title><style>{CSS}{SITE_CSS}</style></head><body>"
            f'<div class="page"><div class="wrap">{body}</div></div></body></html>')


def _one_line(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _pct(a: int, b: int) -> str:
    return f"{a / b:.0%}" if b else "—"


def _brief_data(store: Store, cid: str) -> dict | None:
    from dd import render
    from dd.writer import _load_and_validate, glance_rows
    comp = store.get_company(cid)
    try:
        analysis, sections, facts = _load_and_validate(store, comp)
    except ValueError:
        return None
    p = render.prepare(comp, analysis, sections, facts, glance_rows(analysis.get("signals")))
    product = next((it for it in p["tldr"] if it.get("label") == "product"), None)
    return {"company": comp, "product": product["text"] if product else "", "tiles": p["extras"]["tiles"]}


def _card(cid: str, d: dict, meta: dict) -> str:
    tiles = [t for t in d["tiles"] if t["label"] in CARD_TILES][:4]
    t_html = "".join(f'<div class="tile{" " + t["tone"] if t.get("tone") else ""}"><div class="l">{h(t["label"])}</div>'
                     f'<div class="v">{h(str(t["value"]))}</div><div class="s">{h(t.get("sub") or "")}</div></div>'
                     for t in tiles)
    c = d["company"]
    return (f'<div class="card"><h3>{h(c.name)}</h3><div class="tag">{h(c.domain or "")}'
            f'{" · IČO " + h(meta.get("ico")) if meta.get("ico") else ""}</div>'
            f'<p class="one">{h(d["product"])}</p><div class="tiles">{t_html}</div>'
            f'<a class="go" href="briefs/{h(cid)}-dossier.html">Open the brief →</a></div>')


def _index(m: dict, cards: str, table_rows: dict[str, list[str]], n_collectors: int) -> str:
    gold_ok = sum(ok for _, _, ok, _ in m["golden"])
    checked = sum(r[1] for r in m["integrity"])
    missing = sum(r[2] for r in m["integrity"])
    fo = m["facts_only"]
    fo_n = sum(fo.values())
    costs = [r["cost"] for _, r, _ in m["rows"] if r]
    n_briefs = len(costs)
    body = [
        '<header><p class="kicker">Prototype · application for VC Hacker, Rockaway Ventures · Mykyta Bulatnikov</p>',
        "<h1>Due diligence briefs from public data</h1>",
        '<p class="lead">Give it a company: a name, a Czech IČO or a domain. It collects public evidence, keeps every '
        "fact with its source and the exact quote, computes the numbers in code and writes a brief that an investor "
        "can check line by line. The investment memo stays with a human.</p>",
        '<div class="nav"><a href="#briefs">Briefs</a><a href="#how">How it works</a><a href="#quality">Quality</a>'
        '<a href="#limits">Limits</a><a href="method.html">Method &amp; evaluation</a></div></header>',

        "<h2>Two Czech defence / dual-use companies</h2>",
        '<p class="h2note">Neither is in the Rockaway portfolio. The tiles are computed by code from official records '
        "and press; amounts from the press are quoted as written in the source.</p>",
        f'<div class="cards">{cards}</div>',

        '<h2 id="briefs">All briefs</h2>',
        f'<p class="h2note">{n_briefs} companies.'
        + ("" if all(r.get("invest") for _, r, _ in m["rows"] if r) else
           " Briefs without an investment view were generated before that section existed.") + "</p>",
    ]
    for g in GROUP_ORDER:
        if table_rows.get(g):
            body.append(f"<h3>{h(g)}</h3>")
            body.append('<table class="t"><tr><th>Company</th><th>What it does (from the brief)</th>'
                        '<th class="num">Facts</th><th class="num">Sources</th><th>Investment view</th></tr>'
                        + "".join(table_rows[g]) + "</table>")
    body += [
        '<h2 id="how">How it works</h2>',
        '<div class="steps">'
        f"<div class=\"step\"><b>Collect</b>{n_collectors} collectors read official records (Czech business "
        "register, ARES, public contracts and subsidies, EU procurement, EU funding portal, NATO DIANA cohorts), the "
        "company website, public code, certificate logs and press. Every response is saved with its URL and date.</div>"
        "<div class=\"step\"><b>Extract</b>An LLM proposes facts from unstructured pages only. A fact is kept only if "
        "its exact quote is found in the saved source and it passes category rules.</div>"
        "<div class=\"step\"><b>Compute &amp; check</b>Code computes the numbers (public money by type, funding rounds, "
        "fit with the Rockaway thesis) and checks company claims against independent sources.</div>"
        "<div class=\"step\"><b>Analyse</b>A second LLM call writes findings and the investment view. It may cite only "
        "collected facts; every finding carries an evidence label.</div>"
        "<div class=\"step\"><b>Brief</b>One HTML page with sources and quotes, a Markdown copy and a CSV of all "
        "facts. No investment recommendation.</div></div>",
        '<ul class="plain">'
        "<li>Structured sources (registers, procurement, grants, GitHub, certificate logs) are parsed by code, not "
        "by the LLM.</li>"
        "<li>Facts are separated from claims and opinions: <i>Verified</i>, <i>Corroborated</i>, <i>Company claim</i>, "
        "<i>Analyst view</i>.</li>"
        "<li>No LinkedIn, Crunchbase, Dealroom or PitchBook. Personal data is limited to names and roles from public "
        "sources.</li>"
        "<li>Web pages are treated as data, never as instructions to the model.</li></ul>",

        '<h2 id="quality">Quality: what is checked, and what is not yet</h2>',
        '<p class="h2note">These are guards against specific failures, not an accuracy score. From <code>dd eval</code> '
        'over all briefs on this site; details on the <a href="method.html">method page</a>.</p>',
        '<div class="stats">'
        f'<div class="stat"><div class="v">{gold_ok}/{len(m["golden"])}</div><div class="l">hand-checked register, '
        "grant and infrastructure facts reproduced. A small regression set: it shows official records are parsed "
        "correctly, not that every brief is right.</div></div>"
        f'<div class="stat"><div class="v">{checked - missing}/{checked}</div><div class="l">quotes behind '
        "model-extracted facts found in the saved source. This rules out invented quotes; a real quote can still be "
        "misread.</div></div>"
        f'<div class="stat"><div class="v">{_pct(fo["verified"] + fo["corroborated"], fo_n)}</div><div class="l">of '
        f"{fo_n} factual statements rest on an official record or two independent outlets; {_pct(fo['claim'], fo_n)} "
        "only on the company's word. This describes the evidence, not whether conclusions are right.</div></div>"
        f'<div class="stat"><div class="v">${min(costs):.2f}–{max(costs):.2f}</div><div class="l">model cost per brief '
        f"(OpenAI gpt-5-nano and gpt-5-mini)</div></div></div>",
        '<p><b>The real quality process</b> is reading the output by hand: that found 26 systematic errors so far, each '
        'fixed in code and covered by a test (<a href="method.html#errors">list</a>). <b>Not measured yet:</b> the share '
        "of statements that are actually correct (a hand-labelled sample: does the quote support the fact, are numbers "
        "and entities right, does the conclusion follow), the time saved against a manual first look, and a comparison "
        "with a plain model plus web search on the same companies.</p>",

        "<h2>Why a diligence tool, not a sourcing radar</h2>",
        '<p>I first tested a different idea: could public data have found Rockaway Ventures deals earlier than the '
        "fund did? I traced 14 Rockaway Ventures deals from 2022–2026 and 10 comparison rounds back through registry "
        "records and press.</p>",
        '<ul class="plain">'
        "<li>In 9 of the 14 deals, outside funding was publicly visible before Rockaway invested; in all 9 the first "
        "public trace was press coverage of an earlier round, not the business register.</li>"
        "<li>The register did not announce Rockaway's own rounds early: Campiri appeared 7 days before the "
        "announcement, Cruxo 21 months after it, and Filuta and ValkaAI are held through foreign companies, so the "
        "round is not visible in the Czech register at all.</li>"
        "<li>The 2026 AI deals (ValkaAI, BottleCap AI, Navigara) had no earlier rounds; where there was a visible "
        "signal, it was the founder.</li>"
        "</ul>",
        "<p>A radar built on public registers would not have found these deals sooner. This tests one idea — public "
        "registers as an early signal — on deals the fund made; it says nothing about deals the fund passed on or never "
        "saw, or about sourcing tools built on other signals. The step where the same public data clearly helps is "
        "after a company is on the table: checking it quickly, with every claim traceable to its source.</p>",

        '<h2 id="limits">What it cannot see</h2>',
        '<ul class="plain">'
        "<li><b>Financial statements.</b> Revenue and profit from filed accounts (Sbírka listin) are not extracted yet; "
        "sales to public buyers are the only revenue figure, and only for the public sector.</li>"
        "<li><b>Paid databases and LinkedIn.</b> Not used by design; team size and cap table come only from the "
        "register and public pages.</li>"
        "<li><b>Registers outside Czechia.</b> Only flagged (for example a Delaware or Dutch holding), not read.</li>"
        "<li><b>NATO DIANA.</b> The live site blocks scripts, so cohorts are read from archived copies; a year that "
        "could not be read is shown as “no data”, not as “not selected”.</li>"
        "<li><b>Competitors.</b> Candidates come from text similarity with DIANA cohort descriptions and from what the "
        "company and press name; the model may reject all of them.</li>"
        "<li><b>Analyst views</b> are model-written opinions over the collected facts. They are labelled and meant as "
        "starting points for the memo, not conclusions.</li></ul>",
        '<p class="foot">Private preview, not indexed by search engines. Source code is available on request. '
        "Data as collected in November 2026.</p>",
    ]
    return _shell("Due diligence briefs from public data", "".join(body))


def _method(m: dict) -> str:
    from dd import render
    gold = m["golden"]
    gold_ok = sum(ok for _, _, ok, _ in gold)
    keys = list(render.STRENGTH)
    s = m["strengths"]
    n = sum(s.values()) or 1
    fo = m["facts_only"]
    fo_n = sum(fo.values())
    t = lambda head, rows, num=(): (  # noqa: E731
        '<table class="t"><tr>' + "".join(f'<th{" class=num" if i in num else ""}>{h(c)}</th>'
                                          for i, c in enumerate(head)) + "</tr>"
        + "".join("<tr>" + "".join(f'<td class="num">{c}</td>' if i in num else f"<td>{c}</td>"
                                   for i, c in enumerate(r)) + "</tr>" for r in rows) + "</table>")
    body = [
        '<header><div class="nav"><a href="index.html">← Overview</a></div>',
        '<p class="kicker">Method &amp; evaluation</p><h1>How the briefs are built and checked</h1>',
        '<p class="lead">All numbers on this page are produced by <code>dd eval</code> from the same database as the '
        "briefs. No LLM is involved in the evaluation.</p></header>",

        "<h2>Sources</h2>",
        t(["Source", "What is read"], [(h(name), h(what)) for _, name, what in render.METHOD]),

        "<h2>Evidence labels</h2>",
        '<p class="h2note">Every finding in a brief carries one of these labels.</p>',
        t(["Label", "Meaning"], [(h(lab), h(expl)) for lab, expl in render.STRENGTH.values()]),

        f"<h2>1. Hand-checked facts: {gold_ok}/{len(gold)} reproduced</h2>",
        '<p class="h2note">Registry, grant and infrastructure facts verified by hand against primary sources '
        "(full extract from or.justice.cz, ARES, Hlídač státu) and stored in <code>eval/golden.json</code>.</p>",
        t(["Company", "Check", "Result"], [(h(c), h(name), "✅" if ok else "❌ " + h(note)) for c, name, ok, note in gold]),

        "<h2>2. Quote integrity</h2>",
        '<p class="h2note">For every fact the LLM extracted, its quote must be found in the saved source text.</p>',
        t(["Company", "Facts checked", "Quote not found"], [(h(c), str(a), str(b)) for c, a, b, _ in m["integrity"]],
          (1, 2)),

        "<h2>3. Evidence strength</h2>",
        f'<p class="h2note">{fo_n} factual statements (everything except analyst views): '
        f"{_pct(fo['verified'] + fo['corroborated'], fo_n)} verified or corroborated, {_pct(fo['mixed'], fo_n)} partly "
        f"verified, {_pct(fo['single'], fo_n)} from a single outlet, {_pct(fo['claim'], fo_n)} company claim only. "
        "Analyst views are expected in risks, the rebuild check and questions. The labels describe where the evidence "
        "comes from; they do not measure whether a conclusion is right.</p>",
        t(["Label", "Findings", "Share"], [(h(render.STRENGTH[k][0]), str(s.get(k, 0)), _pct(s.get(k, 0), n))
                                          for k in keys], (1, 2)),
        t(["Section"] + [render.STRENGTH[k][0] for k in keys],
          [[h(sec)] + [str(c.get(k, 0)) for k in keys] for sec, c in m["by_section"].items()],
          tuple(range(1, len(keys) + 1))),

        "<h2>4. Coverage and cost per brief</h2>",
        t(["Company", "Sections filled", "Facts", "Cited sources", "Verified / corroborated findings", "LLM cost"],
          [(h(cid), r["sections"], str(r["facts"]), str(r["sources"]), r["verified"], f"${r['cost']:.4f}")
           for cid, r, _ in m["rows"] if r], (2, 3, 5)),
        f'<p class="h2note">LLM cost of all briefs on this site: ${m["total_cost"]:.2f}; all runs since the start of '
        f"the project, including re-runs after fixes: ${m['ledger']:.2f}.</p>",

        '<h2 id="errors">5. Errors found and fixed</h2>',
        "<p>Before the full run every model-extracted fact of three companies was read by hand, and the run over all "
        "companies was audited the same way. 22 systematic errors were found and fixed in code, for example: a "
        "subsidy agreement counted as a customer contract, one grant counted twice because it appears in two "
        "databases, demo numbers on a dashboard screenshot taken as team size, a company with the same name taken "
        "for the target, and a failed patent search reported as “no patents”. Checks of the defence briefs found two "
        "more: R&amp;D consortium budgets counted as contracts, and a decimal misread that inflated a public-money total "
        "10,000 times.</p>"
        "<p>An outside review on 20 November found two more, both fixed: the model compared a round of CZK 15M with a "
        "€0.5–2m ticket and called it too large (round size versus ticket is now arithmetic in code, and the model is "
        "told not to restate it), and grants were added up across registers that list the same project — the award in "
        "one, the payments in another — which overstated Fly4Future's grants by about 77M CZK. Grants are now one row "
        "per project, with the amount awarded and the amount actually paid shown apart, and only payments are placed "
        "on a timeline. The rebuild check no longer estimates how long a clone would take: it names what is "
        "replicable, what edge public evidence supports, and what cannot be judged from outside.</p>",
        '<p class="foot"><a href="index.html">← Overview</a></p>',
    ]
    return _shell("Method and evaluation", "".join(body))


def build_site(store: Store, out: Path) -> list[Path]:
    from dd.collectors import load
    from dd.evaluate import metrics
    from dd.writer import write_dossier

    out = Path(out).resolve()
    briefs = out / "briefs"
    briefs.mkdir(parents=True, exist_ok=True)
    for old in briefs.glob("*"):
        if old.suffix in (".html", ".md", ".csv"):
            old.unlink()
    meta = _companies_meta()
    m = metrics(store)
    written: list[Path] = []
    table_rows: dict[str, list[str]] = {}
    cards = []
    for cid, r, _ in m["rows"]:
        if not r:
            continue
        comp = store.get_company(cid)
        paths = write_dossier(store, comp, briefs)
        page = Path(paths["html"])
        text = page.read_text(encoding="utf-8")
        text = text.replace("<body>", '<body><div style="max-width:960px;margin:20px auto -12px;padding:0 4px;'
                            'font-size:13.5px"><a href="../index.html">← All briefs</a></div>', 1)
        page.write_text(text, encoding="utf-8")
        written += [Path(p) for p in paths.values()]
        d = _brief_data(store, cid)
        group = GROUPS.get(meta.get(cid, {}).get("tier"), GROUP_ORDER[-1])
        table_rows.setdefault(group, []).append(
            f'<tr><td><a href="briefs/{h(cid)}-dossier.html">{h(comp.name)}</a></td>'
            f'<td>{h(_one_line((d or {}).get("product", "")))}</td>'
            f'<td class="num">{r["facts"]}</td><td class="num">{r["sources"]}</td>'
            f'<td>{"yes" if r["invest"] else "—"}</td></tr>')
    for cid in FEATURED:
        d = _brief_data(store, cid)
        if d:
            cards.append(_card(cid, d, meta.get(cid, {})))
    (out / "index.html").write_text(_index(m, "".join(cards), table_rows, len(load())), encoding="utf-8")
    (out / "method.html").write_text(_method(m), encoding="utf-8")
    (out / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    (out / "vercel.json").write_text(json.dumps({"headers": [{"source": "/(.*)", "headers": [
        {"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}]}, indent=2) + "\n", encoding="utf-8")
    return written + [out / n for n in ("index.html", "method.html", "robots.txt", "vercel.json")]
