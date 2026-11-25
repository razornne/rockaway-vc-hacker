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
    "memo": "Defence and dual-use candidates",
    "showcase": "Rockaway Ventures portfolio",
    "portfolio": "Rockaway Ventures portfolio",
    "showcase-control": "Comparison companies: rounds led by other funds",
    "control": "Comparison companies: rounds led by other funds",
}
# Saying "not in your portfolio" to the fund is a negative claim: the page states only what was checked, when, and
# where (investor_check in eval/companies.json), never more.
GROUP_NOTES = {
    "Defence and dual-use candidates": "Rockaway is not named among the investors in the latest round each company "
                                       "has announced, as checked on the date shown.",
    "Comparison companies: rounds led by other funds": "Used to test the research findings. Rockaway is not named "
                                                       "among the investors in the latest round each company has "
                                                       "announced, as checked on the date shown.",
}
GROUP_ORDER = list(dict.fromkeys(GROUPS.values()))
FEATURED = ("fly4future", "dronetag")
REPO = "https://github.com/razornne/rockaway-vc-hacker"
LABELS = ROOT / "eval" / "labels" / "showcase-2026-11-20.csv"  # semantic accuracy sheet (dd label-sheet / label-score)
REMOVED_SECTIONS = ("Market",)  # labelled on 20 November, no longer shown in briefs (dd.render.HIDDEN_SECTIONS)
# eval/baseline/README.md: facts settled by official records, tool vs gpt-5-mini with web search (judged by hand)
BASELINE = {"n": 14, "tool": 14, "plain": 2, "partly": 3, "wrong": 2, "missed": 7}
# a fresh company end to end (dd add spaceti; collect, extract, verify, analyze, dossier), 20 November 2026
TIMING = {"value": "7 min · $0.03",
          "text": "A new company from nothing to a brief (Spaceti: collection 2.7 min, extraction 2 min, analysis 1.6 min "
                  "with gpt-5-mini). The plain model with web search takes 30 s and $0.02 but misses what only official "
                  "records hold. A manual first look by an analyst was not timed: that needs a person."}
N_ERRORS = 32  # docs/AUDIT.md, numbered
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


def _investor_cell(check: dict | None) -> str:
    """The latest round a company announced and who it names, with the source and the date it was checked."""
    if not check:
        return "<td>not checked</td>"
    url = check.get("source_url") or ""
    src = (f' <a class="site" href="{h(url, quote=True)}" rel="noopener noreferrer" target="_blank">source</a>'
           if url.startswith("https://") else "")
    return (f'<td>{h(check.get("latest_round") or "")}; {h(check.get("investors") or "")}.'
            f'{src}<br><span class="m">checked {h(check.get("checked") or "")}</span></td>')


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
    costs = [r["cost"] for _, r, _ in m["rows"] if r]
    n_briefs = len(costs)
    from dd.labels import summary
    lab = summary(LABELS, REMOVED_SECTIONS)

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
        '<div><dt>Source code</dt><dd><a href="https://github.com/razornne/rockaway-vc-hacker" '
        'rel="noopener noreferrer" target="_blank">github.com/razornne/rockaway-vc-hacker</a></dd></div></dl>',
        '<div class="nav"><a href="#briefs">The two showcase briefs</a><a href="#why">Why this tool</a>'
        '<a href="#trust">How far to trust it</a><a href="#all">All briefs</a><a href="method.html">Method and '
        "evaluation</a></div></header>",

        '<h2 id="briefs">Two Czech dual-use drone companies</h2>',
        '<p class="h2note">Neither has announced Rockaway as an investor (checked 25 November 2026; sources in the '
        '<a href="#all">table below</a>). The numbers next to each are computed by code from official records and '
        "press.</p>",
        cards,

        '<h2 id="why">Why a checking tool</h2>',
        '<div class="prose"><p>My first idea was to spot startups in public registers before funds find them. On 14 '
        "Rockaway Ventures deals it would not have worked: the register showed the fund's own round a week before the "
        "announcement at best, and in other cases months later or not at all; the earlier signal was press about a previous round "
        "or the founder.</p>"
        "<p>The same records are useful one step later, once a company is on the table: they quickly confirm or "
        "contradict what the company says, with every claim linked to its source. "
        f'<a href="{REPO}/blob/main/research/FINDINGS.md">The research</a>.</p></div>',

        '<h2 id="trust">How far to trust it</h2>',
        '<p class="h2note">Is each statement right, and does the tool beat simply asking a model with web search? '
        'Measured on the two showcase briefs; details on the <a href="method.html">method page</a>.</p>',
        '<div class="measure">',
        *([measure(_pct(lab["supported"], lab["n"]), f"Statements fully supported by the quotes they cite, of {lab['n']} in "
                   f"the two showcase briefs; {lab['partly']} partly, {lab['unsupported']} not at all. Labelled one by one by an AI reviewer "
                   "(Claude Opus 5.5) against the cited sources, not by a person: a human pass is still to do."),
           measure(f"{lab['numbers_right']}/{lab['numbers']}", "Statements with amounts, dates or counts that have them "
                   "right. Both misses read a price ceiling (“up to CZK 1.5M” per drone) as the price."),
           measure(f"{lab['material']} / {lab['minor']}", f"Problems that would mislead an investor / minor ones, out "
                   f"of {lab['n']} statements. The minor ones are mostly judgements that go a step beyond their "
                   "evidence.")] if lab else []),
        measure(f"{BASELINE['tool']}/{BASELINE['n']} vs {BASELINE['plain']}/{BASELINE['n']}",
                "Facts settled by official records (filed revenue and profit, grants awarded and paid, a defence "
                "tender, the round) stated right by the tool vs by a plain model with web search on the same two "
                f"companies. The plain model missed {BASELINE['missed']} and got {BASELINE['wrong']} wrong "
                f'(<a href="{REPO}/blob/main/eval/baseline/README.md">comparison</a>).'),
        measure(TIMING["value"], TIMING["text"]),
        "</div>",
        '<div class="prose"><p style="margin-top:1.2rem">Reading the output by hand remains the main quality process. '
        f'It has found {N_ERRORS} systematic errors so far, each fixed in code and covered by a test (<a '
        'href="method.html#errors">the list</a>). Guards that run on every build (hand-checked register facts '
        f"{gold_ok}/{len(m['golden'])}, quotes found in their sources {checked - missing}/{checked}) only rule out "
        "specific failures; they are on the method page. Model cost per brief: "
        f"${min(costs):.2f}–{max(costs):.2f}.</p></div>",

        f'<h2 id="all">All {n_briefs} briefs</h2>',
    ]
    for g in GROUP_ORDER:
        if table_rows.get(g):
            body.append(f"<h3>{h(g)}</h3>")
            if g in GROUP_NOTES:
                body.append(f'<p class="h2note">{h(GROUP_NOTES[g])}</p>')
            checked = g in GROUP_NOTES
            body.append('<table class="t"><tr><th>Company</th><th>What it does, from the brief</th>'
                        + ("<th>Latest round announced, investors named</th>" if checked else "")
                        + '<th class="num">Facts</th><th class="num">Sources</th></tr>'
                        + "".join(table_rows[g])
                        + "</table>")
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
        "<li><b>Financial statements.</b> Filed annual accounts are read from the Czech collection of documents when "
        "the filing has a text layer, and used only if the balance sheet balances. Scanned filings are shown as not "
        "read (no OCR yet); small companies often file a balance sheet only, so revenue is “not published”. So far "
        "only the two showcase briefs were re-run with accounts.</li>"
        "<li><b>Paid databases and LinkedIn.</b> Not used by design; team size and cap table come only from the "
        "register and public pages.</li>"
        "<li><b>Registers outside Czechia.</b> Flagged (for example a Delaware or Dutch holding), not read.</li>"
        "<li><b>NATO DIANA.</b> The live site blocks scripts, so cohorts are read from archived copies.</li>"
        "<li><b>Competitors.</b> Candidates come from text similarity with DIANA cohort descriptions and from what the "
        "company and press name; the model may reject all of them.</li>"
        "<li><b>Judgements</b> are model-written views over the collected facts. They are marked as such and meant as "
        "starting points for the memo, not conclusions.</li></ul>",
        '<p class="foot">Not indexed by search engines. Source code: <a href="https://github.com/razornne/'
        'rockaway-vc-hacker">github.com/razornne/rockaway-vc-hacker</a>. Data as '
        "collected in November 2026.</p>",
    ]
    return _shell("Due diligence briefs from public data", "".join(body))


def _accuracy_sections() -> list[str]:
    """Semantic accuracy, the baseline and timing: the measures that say whether the briefs are right and useful."""
    from dd.labels import summary
    lab = summary(LABELS, REMOVED_SECTIONS)
    out = ['<h2 id="accuracy">Is each statement right?</h2>']
    if lab:
        out.append(
            f'<p>Every one of the {lab["n"]} statements in the two showcase briefs was put in a sheet with the quotes and '
            "links it cites (<code>dd label-sheet</code>) and judged against those sources on six questions "
            f'(<a href="{REPO}/blob/main/eval/labels/showcase-2026-11-20.csv">the labelled sheet</a>; it also holds six '
            "market statements, since removed from the briefs and left out of the counts here). The reviewer was "
            "an AI model, Claude Opus 5.5, not the model that wrote the briefs and not a person; a human pass is still "
            "to do, and the sheet is built for it.</p>"
            '<table class="t"><tr><th>Question</th><th class="num">Result</th></tr>'
            f'<tr><td>The cited quotes support the statement</td><td class="num">{lab["supported"]} yes, {lab["partly"]} '
            f'partly, {lab["unsupported"]} no</td></tr>'
            f'<tr><td>Amounts, currencies, dates and counts are right</td><td class="num">{lab["numbers_right"]} of '
            f'{lab["numbers"]}</td></tr>'
            f'<tr><td>A judgement follows from its evidence</td><td class="num">{lab["follows"]} of {lab["judgements"]}'
            f' (the rest partly)</td></tr>'
            f'<tr><td>Concludes something from missing data</td><td class="num">{lab["from_absence"]} of {lab["n"]}'
            "</td></tr>"
            f'<tr><td>Would mislead an investor</td><td class="num">{lab["material"]} material, {lab["minor"]} minor'
            "</td></tr></table>"
            '<p class="h2note">The two wrong numbers read a price ceiling (“up to CZK 1.5M” per drone) as the price; the two conclusions from missing data say Dronetag has “no product surfaces” although its apps and API docs were collected. Most minor '
            "problems are in the case for and against and the thesis fit: judgements that go a step beyond what the "
            "cited facts show.</p>")
    out += [
        '<h2 id="baseline">Against a plain model with web search</h2>',
        f'<p>The same task given to <code>gpt-5-mini</code> with web search, one call per company, asked for a source '
        "for every statement (<code>eval/baseline.py</code>). Compared on the facts that official records settle "
        f'(<a href="{REPO}/blob/main/eval/baseline/README.md">fact by fact</a>):</p>'
        '<table class="t"><tr><th></th><th class="num">Tool</th><th class="num">Plain model + web search</th></tr>'
        f'<tr><td>Stated right, of {BASELINE["n"]}</td><td class="num">{BASELINE["tool"]}</td><td class="num">'
        f'{BASELINE["plain"]} (+{BASELINE["partly"]} partly)</td></tr>'
        f'<tr><td>Wrong or misleading</td><td class="num">0</td><td class="num">{BASELINE["wrong"]}</td></tr>'
        f'<tr><td>Missed</td><td class="num">0</td><td class="num">{BASELINE["missed"]}</td></tr>'
        '<tr><td>Time and model cost per company</td><td class="num">about 7 min, $0.03</td><td class="num">'
        "30 s, $0.02</td></tr></table>"
        '<p class="h2note">The plain model took Fly4Future’s revenue from a 2024 slide (≈ CZK 24M; the filed figure is '
        "CZK 45.1M), found no filed accounts for either company, missed Dronetag’s Ministry of Defence tender and cited "
        "a rejected grant application as a grant. It is fast and writes sensible founder questions. Two companies, one "
        "run each; a stronger model with more searches would do better.</p>",
        '<h2 id="time">Time</h2>',
        f'<p>{h(TIMING["text"])}</p>',
    ]
    return out


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
        '<p class="oneliner">First whether the statements are right and whether the tool beats a plain model with web '
        "search; then the guards that <code>dd eval</code> runs on every build without a model.</p></header>",

        "<h2>Sources</h2>",
        t(["Source", "What is read"], [(h(name), h(what)) for _, name, what in render.METHOD]),

        "<h2>Evidence labels</h2>",
        '<p class="h2note">Every finding in a brief carries one of these labels.</p>',
        t(["Label", "Meaning"], [(h(lab), h(expl)) for lab, expl in render.STRENGTH.values()]),

        *_accuracy_sections(),

        f"<h2>1. Hand-checked facts: {gold_ok}/{len(gold)} reproduced</h2>",
        '<p class="h2note">Sections 1–4 are guards that run on every build. They rule out specific failures; they do '
        "not say that a statement is right. That is measured above.</p>",
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
        "replicable, what edge public evidence supports, and what cannot be judged from outside.</p>"
        "<p>Building the accuracy check, the baseline and filed-accounts reading found four more, all fixed: a "
        "statement citing an official record and one press article was labelled <i>Verified</i> (a label now needs "
        "every cited source to be official or technical); amounts were shown in the source’s words (“15 milionů”) or "
        "without a currency (one format now: “15M CZK”, the original wording kept beside it); “28,000,000 CZK” was read "
        "as 28 and shown as “0k CZK” (grouped thousands now parsed); and Czech news pages served in windows-1250 were "
        "decoded as UTF-8, garbling investor names (the declared charset is now used).</p>"
        "<p>An investment analyst's review on 25 November found two more, both fixed: an empty register was shown as "
        "“None found”, which tells a fund that something does not exist (it now reads “Not visible in public records” "
        "and names what the register cannot show, such as defence-exempt contracts), and a possible portfolio conflict "
        "was shown as shared word stems without saying what the portfolio company does. The market section was "
        "removed: analysts size markets themselves.</p>",
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
            + (_investor_cell(meta.get(cid, {}).get("investor_check")) if group in GROUP_NOTES else "")
            + f'<td class="num">{r["facts"]}</td><td class="num">{r["sources"]}</td></tr>')
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
