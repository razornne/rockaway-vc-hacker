# Due diligence briefs from public data

Built by Mykyta Bulatnikov for the VC Hacker application at Rockaway Ventures, November 2026.

**Live showcase:** https://dd-briefs.vercel.app (unlisted, not indexed). The same pages are in [`site/`](site/index.html) and open offline.

Give the tool a company — a name, a Czech company ID (IČO) or a domain. It collects public evidence, keeps every fact with its source URL and the exact quote, computes the numbers in code, and writes a brief an investor can check line by line. It does not recommend an investment; the memo stays with a human.

## The story

### 1. Start from the fund, not from the tool

Before building anything I studied the fund itself: 14 Rockaway Ventures deals from 2022–2026 and, as a control group, 10 Czech rounds led by other funds. For each company I rebuilt the public timeline before the investment and asked one question: **could public data have found these deals earlier?** A "sourcing radar" was the obvious thing to build, so I tested it first.

Method and data: [`research/SPEC.md`](research/SPEC.md), one file per company in [`research/companies/`](research/companies/), tables in [`research/signals.md`](research/signals.md).

### 2. What the research showed

- **Rockaway is rarely the first money.** In 9 of 14 deals, outside funding was already in the press a median of 28 months before Rockaway invested.
- **The register does not announce the round early.** Rockaway's own entry appeared first only once (Campiri, 7 days before the announcement). At Cruxo it appeared 21 months after. Filuta and ValkaAI are held through a Delaware and a Dutch company, so their rounds never show in the Czech register.
- **Most deals are invisible in the open register data.** I parsed the full open-data dump of the Prague register (312,713 companies): only 2 of the 14 deals can be seen there.
- **The 2026 AI deals had no history to find.** ValkaAI, BottleCap AI and Navigara were under a year old; the signal was the founder, not a document.
- **Agents misread the register.** They retold press articles accurately, but confused founders' holding companies with investors.

Details: [`research/FINDINGS.md`](research/FINDINGS.md), [`research/DATA_LAYER.md`](research/DATA_LAYER.md).

### 3. The pivot: check, don't search

A radar would not have found these deals sooner. But the same sources — the register, public money, press, the company's own website and code — answer **diligence** questions well: who owns the company, where its money came from, whether its customers and claims hold up, what its technology really is. The bottleneck for a fund that joins competitive rounds is deciding quickly and on evidence, not finding the company. See [`research/PIPELINE.md`](research/PIPELINE.md).

The research also set the rules for the tool: structured sources are parsed by code, the language model only extracts from text with a quote that is checked, and anything the data cannot see is said out loud.

### 4. The showcase: defence

Rockaway now has a defence fund, and defence / dual-use is where official public data is richest: NATO DIANA cohorts, EU defence and research funding, public procurement. The two main briefs are Czech defence companies outside the Rockaway portfolio — **Fly4Future** and **Dronetag**. Fourteen more briefs cover Rockaway portfolio companies and control companies, so the output can be checked against what the fund already knows.

## What a brief contains

- Key numbers computed by code: latest round, sales to public buyers, grants (kept apart from revenue), defence evidence from official sources.
- For the memo: the case for, the case against, and what must be true.
- Ownership, funding rounds, public money by year, customers, technical profile, "could it be rebuilt?", competition, fit with the Rockaway thesis.
- Risks and questions for the founder.
- Every statement carries an evidence label — *Verified*, *Corroborated*, *Single source*, *Partly verified*, *Company claim* or *Analyst view* — and links to its sources and quotes.

## How it works

1. **Collect.** Twelve collectors read the Czech business register (ARES, or.justice.cz), Czech public contracts and subsidies (Hlídač státu), EU procurement (TED), the EU Funding & Tenders portal, NATO DIANA cohorts (archived copies), the company website and job boards, GitHub, certificate transparency logs, app stores, research databases and the press. Every response is cached with its URL and date.
2. **Extract.** A small model (OpenAI `gpt-5-nano`) proposes facts from unstructured pages only. A fact is kept only if its exact quote is found in the saved source and passes category rules.
3. **Compute and verify.** Code computes public money by type, funding rounds and thesis fit, and checks company claims against independent sources: patents, the register, the IAB vendor list, security pages, named customers, government vendor lists.
4. **Analyse.** A second model (`gpt-5-mini`) writes findings and the investment view. It may cite only collected facts; evidence labels are computed from the sources, not chosen by the model.
5. **Brief.** One HTML page with sources and quotes, a Markdown copy, and a CSV of all facts.

More: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## How I know it works

`uv run dd eval` writes [`eval/report.md`](eval/report.md) without calling a model:

- **18 of 18** hand-checked facts reproduced (register shareholders, grants, foreign holdings).
- **811 of 811** quotes behind model-extracted facts found in the saved sources.
- Of 140 factual statements in the briefs, **55%** are verified or corroborated by independent sources; 16% rest on the company's word alone and are labelled so.
- **$0.01–0.03** of model cost per brief; about $1.07 for the whole project, including development runs.

Reading every extracted fact by hand found 24 systematic errors — a subsidy counted as a customer contract, one grant counted twice, a namesake company taken for the target, a failed patent search reported as "no patents", a decimal misread that inflated a total 10,000 times. Each was fixed in code and covered by a test: [`docs/AUDIT.md`](docs/AUDIT.md).

## What it cannot do yet

- Revenue and profit from filed accounts are not read yet: the filings are listed, not parsed.
- Registers outside Czechia are flagged (a Delaware or Dutch holding), not read.
- NATO DIANA's live site blocks scripts, so cohorts come from archived copies.
- Competitor candidates are text-similarity matches; the model may reject all of them.
- Analyst views are model-written opinions over collected facts, labelled as such.

## What's next

[`docs/ROADMAP.md`](docs/ROADMAP.md): reading filed accounts, registers of other CEE countries, an A/B of Anthropic models against the current setup, an editable export for the fund (an Excel workbook, one sheet per question), and a bounded research agent that closes gaps.

## Repository

| Path | What it is |
|---|---|
| `research/` | The portfolio analysis that came first: fund deals, control group, defence landscape, findings. |
| `prototype/` | The parser for the open-data register dump used in the research. |
| `dd/` | The tool: CLI, collectors, extraction, verification, analysis, rendering (Python 3.12, SQLite). |
| `eval/` | Companies, hand-checked facts (`golden.json`), evaluation report. |
| `tests/` | Unit tests (no network by default). |
| `site/` | The built showcase (static HTML, not indexed). Rebuilt with `uv run dd site`. |
| `docs/` | Architecture, audit of data errors, roadmap. |

## Run it

Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run dd seed                      # companies from eval/companies.json
uv run dd collect fly4future        # public sources, cached in .dd/
uv run dd extract fly4future        # model extraction (paid, cached)
uv run dd verify fly4future         # claim checks, no model
uv run dd analyze fly4future        # model analysis (paid, cached)
uv run dd dossier fly4future        # HTML + Markdown + CSV
uv run dd eval                      # evaluation report
uv run dd site                      # rebuild the showcase in site/
uv run pytest -q -m "not network"
```

Copy `.env.example` to `.env` for the API keys, model names, prices and a hard spending limit (`LLM_BUDGET_USD`). Collectors work without a model. `dd spent` shows the spend so far.

## Rules the tool follows

- No LinkedIn, and no scraping of Crunchbase, Dealroom or PitchBook.
- Personal data limited to names and roles from public sources; no birth dates or addresses from the register.
- Web content is data, never instructions to the model.
- A source that was not read is shown as *Not checked*, never as *None found*.
- Polite to websites: cache, timeouts, no mass crawling.
