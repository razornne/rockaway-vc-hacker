# Roadmap

What I would build next, in order of value for an investment team. Each item says what problem it solves, how, and how to tell whether it worked.

## 0. Prove that the briefs are right, and that they save time

Before adding sources, the existing output has to earn trust. Status on 20 November 2026:

- **Semantic accuracy (first pass done, human pass open).** `dd label-sheet` wrote all 72 statements of the two defence briefs into [`eval/labels/showcase-2026-11-20.csv`](../eval/labels/showcase-2026-11-20.csv) with the cited quotes and links; each was judged on six questions. Result ([score](../eval/labels/showcase-2026-11-20-score.md)): 82% fully supported by their quotes and 18% partly, 35 of 37 numbers right, 0 problems that would mislead an investor and 16 minor ones. The reviewer was an AI model (Claude Opus 5.5), not a person. Next: the same sheet labelled by an investor, and the agreement between the two.
- **Baseline (done for two companies).** `gpt-5-mini` with web search on the same task ([`eval/baseline/`](../eval/baseline/README.md)). On 14 facts settled by official records the tool states 14 right, the plain model 2 (3 partly, 2 wrong, 7 missed). Next: more companies, and a stronger baseline model with more searches.
- **Time (machine side done).** A fresh company takes about 7 minutes and $0.03 from name to brief. Not measured: how long an analyst needs for the same first look, and how long the human check of a brief takes. That needs a person and a stopwatch.
- **Fact selection (improved).** The analysis no longer takes the first 90 facts: facts are picked in turns across topics (money, claim checks, product, traction, company, press), with a larger budget for Claude (250 facts) than for `gpt-5-mini` (90). A real relevance ranking per section is still open.

## 1. Filed accounts: text PDFs done, scans and other countries open

**Done.** For a Czech company the registry collector downloads the latest annual accounts from the Collection of Deeds (Sbírka listin), reads the text layer and extracts the balance sheet and, when filed, the income statement: revenue, operating and net result, personnel costs, cash, equity, liabilities, receivables, for the year and the year before. A filing is used only if total assets equal total equity and liabilities as read, and the net result in the balance sheet must match the income statement. The unit ("v celých tisících Kč/CZK") is read from the form. Three form layouts are handled (with and without a row-number column, numbers with and without thousands spaces), each covered by a test. Results: Fly4Future revenue CZK 47.8M for 2025 (net result 8.8M, cash 57.1M); Dronetag balance sheet only (small entity: revenue "not published", net result 4.2M, cash 19.6M); Spaceti revenue 46.9M, net loss 10.4M.

**Open.**
1. **Scans.** Many filings have no text layer. They are shown as *Not read* with the reason. Next: OCR or a vision model on the page images, accepted only through the same balance check.
2. **The other 14 briefs.** They were collected before the accounts reader existed. Re-collecting the register changes fact ids, so each needs a new analysis (about $0.03 each).
3. **Notes to the accounts.** Loans, convertibles and headcount are in the notes as free text (Dronetag's CZK 15M convertible loan is there). They need model extraction with a checked quote, like press.
4. **Late filings and foreign parents.** The newest public numbers are often 1–2 years old, and a Delaware or Dutch parent's accounts are not in the Czech collection.

**How to measure.** Hand-check 10–15 filings field by field; target zero accepted numbers that are wrong, at the price of some *Not read*.

## 2. Registers of other CEE countries

**Problem.** Outside Czechia the tool only flags a foreign holding; it does not read the register. Rockaway Ventures invests across CEE and DACH and in European founders building in the US, and the VC Hacker role scouts technical founders across Europe and the US.

**How.** One collector per country, the same contract as the Czech one: parse structured data by code, store each fact with a URL, show *Not checked* when a source is unavailable. Candidate sources (availability and terms to verify before building):

| Country | Company register | Financial statements |
|---|---|---|
| Slovakia | ORSR | Register of Financial Statements (RÚZ), open API with structured statements |
| Poland | KRS, open API for extracts | Financial statements repository; filed electronically as structured XML since 2018 |
| Estonia | e-Business Register, open data | annual reports in structured form |
| Lithuania | Registrų centras (Register of Legal Entities); basic data as free open data | balance-sheet data from annual statements held since 2016; documents, bulk data and API are paid |
| Latvia | Enterprise Register (UR); bulk open data (CSV, CC0) on data.gov.lv, updated daily | financial data from annual reports reported as an open dataset; confirm the exact resource |
| Hungary | e-cegjegyzek | e-beszamolo (financial statements portal) |
| Romania | ONRC | Ministry of Finance publishes basic balance-sheet indicators per company |
| Slovenia | AJPES | AJPES (annual reports, basic data free) |
| Austria | Firmenbuch (paid extracts) | via Firmenbuch |
| Germany | Handelsregister (free since 2022) | Unternehmensregister |

Next to registers, each country has its own public procurement portal, grant agencies and tech press, which matter as much as the register.

**Order.** Slovakia and Poland first: structured financial statements, close to the Czech model, and many CEE deals there. Then the Baltics — Estonia, Latvia and Lithuania — which produce many startups and publish much of their register data openly; Lithuania's financial statements are mostly behind paid access.

## 3. Model choice: done for the showcase, open for the rest

**Done (20 November 2026).** The LLM layer is provider-neutral (same schemas, cache, cost ledger and budgets for OpenAI and Anthropic), and `dd compare` puts the same company's brief from several models side by side. On Fly4Future, with identical collected facts:

| Analysis model | Cost per brief | Read |
|---|---|---|
| OpenAI `gpt-5-mini` | $0.025 | generic phrasing ("strong technical base and IP") |
| Claude Haiku 5.5 | $0.014 at low effort, about $0.02 at medium | specific and careful with numbers; one overstated "for" |
| Claude Sonnet 5.5 | $0.24 | the most specific (staff, unit volumes, patent topics, round discrepancies), every specific checked against the facts; one section came back empty |

Haiku 5.5 became the analysis model, at medium effort. At low effort it once returned a one-sided case for and against (only "for"); the investment view now retries once when one side is missing, and Claude gets a larger output limit because adaptive thinking counts against it.

**Open.** The two showcase briefs use Haiku; the other 14 still use `gpt-5-mini` until there is Anthropic credit for them (about $0.02 each). The decision should be confirmed by the hand-labelled accuracy sheet (item 0), not by one read. Extraction stays on `gpt-5-nano`; a Haiku extraction test is the next comparison.

## 4. An export the fund can edit

**Problem.** An HTML page is good for reading, not for working. An analyst wants to correct a number, add a comment and paste into a memo.

**How (draft, to be shaped with an investor's feedback).** An Excel workbook, one sheet per question, like a financial model:

| Sheet | Question it answers |
|---|---|
| Summary | What is it, and what are the key numbers? |
| Ownership & funding | Who owns it, which rounds, who invested? |
| Financials | What do the filed accounts show? (after item 1) |
| Public money | Grants, subsidies and public contracts, by type and year |
| Customers & traction | Which customers are confirmed, and by whom? |
| Team & hiring | Who runs it, and what is being hired? |
| Technology | Stack, own models vs APIs, could it be rebuilt? |
| Claims checked | What the company says vs what independent sources say |
| Risks & questions | What to ask the founder |
| Sources | Every fact: value, URL, quote, date, evidence label |

Every row keeps its source and evidence label, plus an empty "analyst comment / override" column, so edits are visible next to the original. A Markdown or Word memo draft with footnoted sources is the second format.

## 5. A gap-closing research agent

**Problem.** Fixed search templates miss things: Filuta's customer HISD stayed unconfirmed because the literal query found nothing; the Texas vendor listing was found almost by chance.

**How.** A bounded agent on top of the deterministic core. It takes the brief's open questions ("not found", "not checkable"), may run about ten searches per company, and returns only a URL plus a quote; code then checks that the quote is on the page and applies the same category rules as extraction. It has no write tools, a hard budget, and every step is logged as a source document.

**How to measure.** Gaps closed per company, share of found facts that turn out wrong, cost.

## 6. From a showcase to a tool the team can use

**Problem.** The site is a set of static briefs. A partner cannot type a new company and get a brief.

**How.** The pipeline already runs end to end from `dd add`; what is missing is a front door with a budget. The smallest honest version: a form on the site that files a request (name, IČO or domain) into a queue; a worker on a small server or a scheduled job runs `dd add` → `collect` → `extract` → `verify` → `analyze` → `dossier` with a per-request and a monthly spending cap, and publishes the brief behind a login (the briefs name people and are not for search engines). About 7 minutes and $0.03 per company makes this cheap; the hard parts are polite crawling under load and keeping keys off the client. A serverless function is a poor fit, because a run takes minutes.

**How to measure.** Time from request to brief, failures per 100 requests, cost per brief, and whether people come back to use it.

## 7. Smaller items

- **Competitors.** Today candidates come from text similarity with NATO DIANA cohorts, and the model may reject all of them (Dronetag). Add procurement co-bidders and EU project consortium partners as sources.
- **Investment view for every brief.** Older portfolio briefs were generated before the investment view existed; regenerate them (about $0.3 in total).
- **Portfolio monitoring.** Alerts on register changes, insolvency, missing filings, hiring spikes and new public contracts.
- **Design.** The brief and showcase are a prototype; a proper design pass after investor feedback on what to show first.
- **Ambiguous names.** Detect them automatically (a `<name>.com` domain that is not the company's) instead of hand-written context terms.
