# Architecture

How the due diligence tool is built, as of November 2026. Why it exists is in the [README](../README.md) and in [`research/FINDINGS.md`](../research/FINDINGS.md).

## 1. What it does and for whom

**User:** an investment team at a Seed to Series A fund. For Rockaway Ventures: AI, B2B software and industrial tech (VC Hacker posting), with deep tech, defence / dual-use and energy also named on the fund page; CEE, DACH and European founders building in the US.

**Job:** from a company name, domain or Czech IČO, produce in minutes a brief that tells a partner whether to spend an hour on a meeting and what to ask. The technical part — product, code, models, defensibility — is what a "VC hacker" would otherwise do by hand.

**Output per company:**
1. **Brief** (HTML, plus a Markdown copy): a screening scorecard computed by code (`dd/scorecard.py`: seven criteria, 0–2 points each; what the records cannot settle is open and widens the range instead of scoring 0; the verdict is *passes to a first call*, *open* or *below the bar*), then what the company is, who owns it, money in (rounds, grants awarded and paid, public contracts), customers, technical profile, what could be rebuilt and what cannot be judged from outside, risks, founder questions, and the investment view (thesis fit, business model, competition, case for and against; market statements are collected but not shown).
2. **Fact table** (CSV): every fact with its source URL, quote and retrieval date.

**Not a goal:** finding companies before the fund does (tested and rejected, see `research/FINDINGS.md`), or recommending an investment. The memo stays with a human.

## 2. Principles

1. **Every fact has a URL and a retrieval date.** No source, no fact.
2. **Structured sources are parsed by code.** Registers, procurement, grants, GitHub, certificate logs and app stores are read by deterministic parsers. In the portfolio research, agents that "read" the register confused founders with investors.
3. **The language model does two narrow jobs:** (a) proposes facts from unstructured text, each with an exact quote; (b) writes findings that may cite only collected facts.
4. **A quote must exist in the saved source.** Extraction is rejected if the quote is not found in the cached page or breaks category rules.
5. **Say what the data cannot see.** Flags such as "holding abroad", "a.s./SE — shareholders not published", "no Czech entity". A source that was not read is shown as *Not checked*; one that was read and is empty, as *Not visible in public records*, with what it cannot show. Never *None found*.
6. **Web content is data, not instructions.** Page text goes to the model only as a document to extract from; the model has no tools that change anything.
7. **Minimal personal data.** People: name, role, dates and share from public registers. Birth dates are used in memory only to match a person across registers (never stored or shown); no addresses; no LinkedIn.
8. **Cheap and capped.** Every LLM call is cached; a hard budget refuses a call whose worst-case cost would exceed it.

## 3. Pipeline

```
input: name | domain | IČO
        │
        ▼
 resolver ── ARES search, website imprint → IČO; ambiguous names need context terms
        │
        ▼
 collectors (fetch → raw cache → facts), 12 in total
   registry      ARES + ARES VR (identity, shareholders, capital), or.justice.cz filings and annual accounts (dd/accounts.py), ISIR
   public_money  Hlídač státu API: Czech public contracts and subsidies (needs an IČO)
   procurement   TED: EU tenders won
   eu_funding    EU Funding & Tenders portal: EU-funded projects
   diana         NATO DIANA cohorts (archived copies via the Wayback Machine)
   press         Tavily + Exa search, press articles about rounds, customers, product
   web           the company's own site (≤30 pages): product, pricing, careers, privacy/subprocessors
   techfp        HTTP headers, HTML/JS, DNS, crt.sh → stack, SaaS tools, subdomains
   code          GitHub API: organisation, repositories, activity
   ml            Hugging Face, OpenAlex, patents
   apps          App Store / Google Play
   history       Wayback CDX: first snapshots of the site and key pages
        │
        ▼
 extract  (LLM, gpt-5-nano) → facts from unstructured pages, quote checked against the cached text
        │
        ▼
 verify   (code) → company claims checked against independent sources:
           patents, IAB vendor list, register vs press investors, security pages,
           named customers, public-sector vendor listings
        │
        ▼
 signals  (code) → public money by type, funding rounds, defence evidence, thesis fit, AI dependency
        │
        ▼
 analyze  (LLM, Claude Haiku 5.5) → findings and the investment view; may cite only fact ids;
           every finding gets an evidence label computed from its sources
        │
        ▼
 osint    (code, after analysis; dd/osint/, docs/OSINT_PLAN.md) → claims against records (AI, team size,
           revenue, public buyers); people from ARES VR and their other companies from the register's
           open-data dumps; ISIR web service for people; unreliable VAT payer (ADIS); EU and Czech
           sanctions lists; job boards and archived careers pages. Never sent to the model and left out
           of the analysis hash, so it does not make a brief stale.
        │
        ▼
 dossier  → brief.html, brief.md, facts.csv          eval → report without LLM calls
                                                     site → static showcase in site/
```

## 4. Data model (SQLite, `.dd/dd.sqlite`)

```
company(id, name, domain, ico, country, ...)
source_doc(id, company_id, url, kind, fetched_at, sha256, path)    -- raw cache on disk
fact(id, company_id, type, key, value_json, event_date, date_precision,
     source_url, snippet, extractor, confidence, created_at)
analysis(id, company_id, kind, output_json, model, prompt_version, fact_ids, cost_usd, created_at)
llm_call(model, prompt_hash, response, tokens_in, tokens_out, cost_usd, created_at)
```

## 5. Evidence labels

Computed by code from a finding's cited facts, not chosen by the model:

| Label | Meaning |
|---|---|
| Verified | backed by an official record or a public technical artifact |
| Corroborated | reported by two or more independent outlets |
| Single source | one independent outlet, not yet corroborated |
| Partly verified | combines independent evidence with the company's own statements |
| Company claim | only the company's own website says so — verify in diligence |
| Analyst view | a judgement drawn from the cited evidence, not a fact (risks, rebuild verdict, investment view) |

## 6. Technical due diligence: questions and signals

| Partner's question | Signals | Sources |
|---|---|---|
| What is actually sold? | product pages, docs, API reference, changelog, subdomains | web, crt.sh |
| Is the product alive? | releases, new subdomains, engineering hiring, GitHub activity | web, crt.sh, Wayback, GitHub |
| Own models or an API wrapper? | subprocessors in the privacy policy, ML job posts, Hugging Face, papers | web, ml, careers |
| How strong is engineering? | engineering job posts, public code, talks and papers | careers, GitHub, OpenAlex |
| Could it be rebuilt? | what off-the-shelf parts could reproduce (named), what edge public evidence supports, what cannot be judged without code, models, data or field results — no time-to-clone estimate | analysis over facts |
| What protects it? | own data, integrations, network effects, certifications, hardware, public-sector buyers | all modules |

## 7. Stack

- Python 3.12, `uv`, `httpx`, `selectolax`, `pydantic`, SQLite.
- Structured output on both providers: OpenAI `gpt-5-nano` for extraction; Claude Haiku 5.5 (Anthropic API, medium effort, adaptive thinking) for analysis, chosen after a side-by-side comparison (`dd compare`); `gpt-5-mini` still runs where Claude credit is not available. Models, prices and hard budgets (overall and Anthropic) are set in `.env`.
- CLI: `dd seed | collect | extract | verify | analyze | dossier | eval | site | spent`.
- Secrets in `.env` (git-ignored): `OPENAI_API_KEY`, `HLIDAC_TOKEN`, `GITHUB_TOKEN`, `TAVILY_API_KEY`, `EXA_API_KEY`.

## 8. Evaluation

`dd eval` writes `eval/report.md` without calling an LLM:

| Metric | How |
|---|---|
| Fact accuracy | hand-checked facts in `eval/golden.json` (register shareholders, grants, foreign holdings) must be reproduced |
| Quote integrity | every LLM-extracted quote must be found in the saved source text |
| Evidence strength | share of findings that are Verified or Corroborated, by section |
| Coverage | which sections and signals are filled per company |
| Cost | LLM spend per brief |

These are guards against specific failures, not an accuracy score: a quote found in its source rules out invented quotes but not a misreading, and evidence labels describe where the evidence comes from, not whether a conclusion is right. The errors found by reading the output by hand are logged in [`AUDIT.md`](AUDIT.md); a hand-labelled accuracy check is the next step (`ROADMAP.md`).

Numbers that a partner compares — round size against the fund's ticket, public money by type, grants awarded versus paid — are computed in code. The model is told not to redo that arithmetic.

## 9. Known limits

- Without access to the code, technical DD is an outside view: it answers "is it worth digging and what to ask", not "is the code good".
- The register does not see most strong startups' rounds (2 of 14 fund deals).
- Filed accounts are read from text PDFs only and used only if the balance sheet balances and the net result agrees between the statements; scans are shown as *Not read* (see [`ROADMAP.md`](ROADMAP.md)).
- Registers outside Czechia are flagged, not read.
- The fund's memo template, CRM and process are unknown, so there is no CRM export.
