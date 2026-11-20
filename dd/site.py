"""`dd site`: a static, read-only showcase (index, method & evaluation, all briefs).

Every number on the pages comes from the same code as the briefs and `dd eval`; nothing is typed in by hand
except the prose. The output folder can be served by any static host; pages carry noindex.
"""
from __future__ import annotations

import html
import json
import os
import re
from pathlib import Path

from dd.config import ROOT
from dd.store import Store

h = html.escape

GROUPS = {  # tier in eval/companies.json -> group on the site
    "memo": "Defence and dual-use, outside the Rockaway portfolio",
    "showcase": "Rockaway Ventures portfolio",
    "portfolio": "Rockaway Ventures portfolio",
    "showcase-control": "Comparison companies (not in the Rockaway portfolio)",
    "control": "Comparison companies (not in the Rockaway portfolio)",
}
GROUP_ORDER = list(dict.fromkeys(GROUPS.values()))
FEATURED = ("fly4future", "dronetag")
CARD_TILES = ("Raising now (per press)", "Last closed round", "Latest reported round", "Funding rounds",
              "Sales to public buyers", "Grants & subsidies awarded (not revenue)", "Defence evidence (official sources)")

SITE_CSS = """
.feature{display:grid;grid-template-columns:minmax(0,43rem) var(--margin);column-gap:var(--gap);padding:1.4rem 0;
border-top:1px solid var(--rule)}
.feature:first-of-type{border-top:0}
.feature h3{font:500 2rem/1.1 var(--serif);margin:0 0 .5rem;letter-spacing:-.01em}
.feature h3 a{color:var(--ink);text-decoration:none}.feature h3 a:hover{text-decoration:underline}
.feature p{margin:0 0 .7rem}
.feature .open{font:500 14px var(--sans)}
.feature .logo{height:2.2rem;max-width:11rem;margin:0 0 1rem}
a.site{font:400 13px var(--sans);color:var(--muted);margin-left:1.2rem}a.site:hover{color:var(--accent)}
table.t a.site{margin-left:0}
.mini{font:13px/1.35 var(--sans);color:var(--muted);padding-top:.4rem}
.mini div{padding:.35rem 0;border-top:1px solid var(--rule)}.mini div:first-child{border-top:0;padding-top:0}
.mini b{display:block;font:600 15px/1.3 var(--sans);color:var(--ink);font-variant-numeric:tabular-nums}
ol.steps{margin:.4rem 0 0;padding:0;list-style:none;counter-reset:s;max-width:43rem}
ol.steps li{counter-increment:s;display:grid;grid-template-columns:2rem minmax(0,1fr);padding:.7rem 0;border-top:1px solid var(--rule)}
ol.steps li:before{content:counter(s);font:600 15px/1.62 var(--sans);color:var(--accent)}
ul.plain{margin:.4rem 0 0;padding-left:1.2rem;max-width:43rem}ul.plain li{margin:.45rem 0}
.prose{max-width:43rem}.prose p{margin:0 0 1rem}
.measure .row{align-items:baseline}
.measure .val{font:600 1.45rem/1.2 var(--sans);font-variant-numeric:tabular-nums}
.measure .txt{font-size:16px}
.nav{font:500 14px var(--sans);display:flex;flex-wrap:wrap;gap:.4rem 1.4rem;margin-top:1.4rem}.nav a{text-decoration:none}
.nav a:hover{text-decoration:underline}
@media(max-width:900px){.feature{grid-template-columns:minmax(0,1fr)}.mini{display:flex;flex-wrap:wrap;gap:.4rem 1.4rem}
.mini div{border-top:0;padding:0}}
"""

NOINDEX = '<meta name="robots" content="noindex, nofollow">'


def _companies_meta() -> dict[str, dict]:
    rows = json.loads((ROOT / "eval" / "companies.json").read_text(encoding="utf-8"))
    return {r["id"]: r for r in rows}


def _shell(title: str, body: str) -> str:
    from dd.page import CSS, FONTS
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            '<meta name="viewport" content="width=device-width, initial-scale=1">' + NOINDEX + FONTS +
            f"<title>{h(title)}</title><style>{CSS}{SITE_CSS}</style></head><body>"
            f'<div class="page">{body}</div></body></html>')


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


LOGOS = ROOT / "assets" / "logos"  # company logos supplied by hand, made transparent: <company id>.png
AUTHOR_URL = os.getenv("DD_AUTHOR_URL", "")  # the author's public profile, linked from the name on the home page


def _logo(cid: str, prefix: str = "") -> str:
    return (f'<img class="logo" src="{prefix}logos/{h(cid)}.png" alt="">' if (LOGOS / f"{cid}.png").exists() else "")


def _card(cid: str, d: dict, meta: dict) -> str:
    tiles = [t for t in d["tiles"] if t["label"] in CARD_TILES][:4]
    mini = "".join(f'<div>{h(t["label"])}<b>{h(str(t["value"]).replace(" · ", ", "))}</b></div>' for t in tiles)
    c = d["company"]
    site = (f' <a class="site" href="https://{h(c.domain, quote=True)}" rel="noopener noreferrer" target="_blank">'
            f"{h(c.domain)}</a>" if c.domain else "")
    return (f'<div class="feature"><div>{_logo(cid)}<h3><a href="briefs/{h(cid)}-dossier.html">{h(c.name)}</a></h3>'
            f'<p>{h(d["product"])}</p><a class="open" href="briefs/{h(cid)}-dossier.html">Read the {h(c.name)} brief</a>'
            f'{site}</div><div class="mini">{mini}</div></div>')


def _index(m: dict, cards: str, table_rows: dict[str, list[str]], n_collectors: int) -> str:
    gold_ok = sum(ok for _, _, ok, _ in m["golden"])
    checked = sum(r[1] for r in m["integrity"])
    missing = sum(r[2] for r in m["integrity"])
    fo = m["facts_only"]
    fo_n = sum(fo.values())
    costs = [r["cost"] for _, r, _ in m["rows"] if r]
    n_briefs = len(costs)

    def measure(value, text):
        return f'<div class="row"><div class="txt">{text}</div><div class="val">{value}</div></div>'

    body = [
        "<header><h1>Due diligence briefs from public data</h1>",
        '<p class="oneliner">Give it a company: a name, a Czech company ID or a domain. It collects public evidence, '
        "keeps every fact with its source and the exact quote, computes the numbers in code, and writes a brief an "
        "investor can check line by line. The investment memo stays with a human.</p>",
        '<dl class="facts"><div><dt>Built by</dt><dd>'
        + (f'<a href="{h(AUTHOR_URL, quote=True)}" rel="noopener noreferrer" target="_blank">Mykyta Bulatnikov</a>'
           if AUTHOR_URL.startswith("https://") else "Mykyta Bulatnikov") + "</dd></div>"
        "<div><dt>For</dt><dd>VC Hacker application, Rockaway Ventures</dd></div>"
        "<div><dt>Data collected</dt><dd>November 2026</dd></div>"
        "<div><dt>Source code</dt><dd>available on request</dd></div></dl>",
        '<div class="nav"><a href="#briefs">The two showcase briefs</a><a href="#why">Why this tool</a>'
        '<a href="#trust">How far to trust it</a><a href="#all">All briefs</a><a href="method.html">Method and '
        "evaluation</a></div></header>",

        '<h2 id="briefs">Two Czech dual-use drone companies</h2>',
        '<p class="h2note">Neither is in the Rockaway portfolio. The numbers next to each are computed by code from '
        "official records and press.</p>",
        cards,

        '<h2 id="why">Why a diligence tool, not a sourcing radar</h2>',
        '<div class="prose"><p>I first tested the obvious idea: could public data have found Rockaway Ventures deals '
        "earlier than the fund did? I traced 14 Rockaway Ventures deals from 2022–2026 and 10 comparison rounds back "
        "through register records and press.</p></div>",
        '<ul class="plain">'
        "<li>In 9 of the 14 deals, outside funding was publicly visible before Rockaway invested; in all 9 the first "
        "public trace was press coverage of an earlier round, not the business register.</li>"
        "<li>The register did not announce Rockaway's own rounds early: Campiri appeared 7 days before the "
        "announcement, Cruxo 21 months after it, and Filuta and ValkaAI are held through foreign companies, so their "
        "rounds are not visible in the Czech register at all.</li>"
        "<li>The 2026 AI deals (ValkaAI, BottleCap AI, Navigara) had no earlier rounds; where there was a visible "
        "signal, it was the founder.</li></ul>",
        '<div class="prose"><p style="margin-top:1rem">A radar built on public registers would not have found these '
        "deals sooner. That tests one idea, public registers as an early signal, on deals the fund made; it says nothing "
        "about deals the fund passed on or never saw. The same public data clearly helps after a company is on the "
        "table: checking it quickly, with every claim traceable to its source.</p></div>",

        '<h2 id="trust">How far to trust it</h2>',
        '<p class="h2note">These are guards against specific failures, not an accuracy score. Computed by '
        '<code>dd eval</code> over all briefs on this site; details on the <a href="method.html">method page</a>.</p>',
        '<div class="measure">',
        measure(f"{gold_ok}/{len(m['golden'])}", "Hand-checked register, grant and infrastructure facts reproduced. A "
                "small regression set: official records are parsed correctly, which says nothing yet about every brief."),
        measure(f"{checked - missing}/{checked}", "Quotes behind model-extracted facts found in the saved source. This "
                "rules out invented quotes; a real quote can still be misread."),
        measure(_pct(fo["verified"] + fo["corroborated"], fo_n), f"Of {fo_n} factual statements rest on an official "
                f"record or two independent outlets; {_pct(fo['claim'], fo_n)} only on the company's word. This describes "
                "the evidence, not whether conclusions are right."),
        measure(f"${min(costs):.2f}–{max(costs):.2f}", "Model cost per brief. Extraction with OpenAI gpt-5-nano; analysis with Claude Haiku 5.5 for the two showcase "
                "briefs and OpenAI gpt-5-mini for the others."),
        "</div>",
        '<div class="prose"><p style="margin-top:1.2rem">The real quality process is reading the output by hand. That '
        'has found 26 systematic errors so far, each fixed in code and covered by a test (<a href="method.html#errors">'
        "the list</a>). Not measured yet: the share of statements that are actually correct (a hand-labelled sample is "
        "in progress), the time saved against a manual first look, and a comparison with a plain model plus web search "
        "on the same companies.</p></div>",

        f'<h2 id="all">All {n_briefs} briefs</h2>',
    ]
    for g in GROUP_ORDER:
        if table_rows.get(g):
            body.append(f"<h3>{h(g)}</h3>")
            body.append('<table class="t"><tr><th>Company</th><th>What it does, from the brief</th>'
                        '<th class="num">Facts</th><th class="num">Sources</th></tr>'
                        + "".join(table_rows[g]) + "</table>")
    body += [
        '<h2 id="how">How a brief is made</h2>',
        '<ol class="steps">'
        f"<li><span><b>Collect.</b> {n_collectors} collectors read official records (the Czech business register and "
        "ARES, public contracts and subsidies, EU procurement, the EU funding portal, NATO DIANA cohorts), the company "
        "website, public code, certificate logs and press. Every response is saved with its URL and date.</span></li>"
        "<li><span><b>Extract.</b> A language model proposes facts from unstructured pages only. A fact is kept only if "
        "its exact quote is found in the saved source and it passes category rules.</span></li>"
        "<li><span><b>Compute and check.</b> Code computes the numbers (public money by type, grants awarded and paid, "
        "funding rounds, round size against the fund's ticket) and checks company claims against independent "
        "sources.</span></li>"
        "<li><span><b>Analyse.</b> A second model call writes the findings and the investment view. It may cite only "
        "collected facts, and every statement carries a mark for how strong its evidence is.</span></li>"
        "<li><span><b>Brief.</b> One page with sources and quotes, a Markdown copy and a CSV of all facts. No "
        "investment recommendation.</span></li></ol>",

        '<h2 id="limits">What it cannot see</h2>',
        '<ul class="plain">'
        "<li><b>Financial statements.</b> Revenue and profit from filed accounts are not read yet; sales to public "
        "buyers are the only revenue figure, and only for the public sector.</li>"
        "<li><b>Paid databases and LinkedIn.</b> Not used by design; team size and cap table come only from the "
        "register and public pages.</li>"
        "<li><b>Registers outside Czechia.</b> Flagged (for example a Delaware or Dutch holding), not read.</li>"
        "<li><b>NATO DIANA.</b> The live site blocks scripts, so cohorts are read from archived copies.</li>"
        "<li><b>Competitors.</b> Candidates come from text similarity with DIANA cohort descriptions and from what the "
        "company and press name; the model may reject all of them.</li>"
        "<li><b>Judgements</b> are model-written views over the collected facts. They are marked as such and meant as "
        "starting points for the memo, not conclusions.</li></ul>",
        '<p class="foot">Private preview, not indexed by search engines. Source code is available on request. Data as '
        "collected in November 2026.</p>",
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
        '<nav class="crumb"><a href="index.html">← Overview</a></nav>',
        '<header><h1>How the briefs are built and checked</h1>',
        '<p class="oneliner">All numbers on this page are produced by <code>dd eval</code> from the same database as the '
        "briefs. No language model is involved in the evaluation.</p></header>",

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
    (out / "logos").mkdir(exist_ok=True)
    for logo in LOGOS.glob("*.png"):
        (out / "logos" / logo.name).write_bytes(logo.read_bytes())
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
        text = text.replace('<div class="page"><header>',
                            '<div class="page"><nav class="crumb"><a href="../index.html">← All briefs</a></nav><header>'
                            + _logo(cid, "../"), 1)
        page.write_text(text, encoding="utf-8")
        written += [Path(p) for p in paths.values()]
        d = _brief_data(store, cid)
        group = GROUPS.get(meta.get(cid, {}).get("tier"), GROUP_ORDER[-1])
        table_rows.setdefault(group, []).append(
            f'<tr><td><a href="briefs/{h(cid)}-dossier.html">{h(comp.name)}</a>'
            + (f'<br><a class="site" href="https://{h(comp.domain, quote=True)}" rel="noopener noreferrer" '
               f'target="_blank">{h(comp.domain)}</a>' if comp.domain else "") + '</td>'
            f'<td>{h(_one_line((d or {}).get("product", "")))}</td>'
            f'<td class="num">{r["facts"]}</td><td class="num">{r["sources"]}</td></tr>')
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
