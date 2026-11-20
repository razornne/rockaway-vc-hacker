# Roadmap

What I would build next, in order of value for an investment team. Each item says what problem it solves, how, and how to tell whether it worked.

## 0. Prove that the briefs are right, and that they save time

Before adding sources, the existing output has to earn trust.

- **Semantic accuracy (started).** `dd label-sheet` writes every statement of chosen briefs into a CSV with the cited quotes and links; an investor marks for each one whether the quotes support it, whether numbers and names are right, whether a judgement follows, and whether it concludes something from missing data. `dd label-score` counts the answers per question and per section. First target: the two defence briefs (about 100 statements), labelled by someone other than the author.
- **Baseline.** The same companies and questions given to one capable model with web search. Same labelling. This shows what the collectors, quote checks and code-computed numbers add, or do not.
- **Time.** From company name to a brief usable for a founder call, including the human check, against a manual first look by an analyst.
- **Fact selection.** The analysis sees at most 90 facts (plus those cited by code-computed signals), chosen by fact type and order. For companies with 200+ facts this should rank by relevance to each section.

## 1. Read the filed accounts (revenue, profit, cash)

**Problem.** For a Czech company the tool already lists every document in the Collection of Deeds (Sbírka listin): type, year, filing date and link. It does not read them, so a brief has no revenue, profit or cash — the first thing an investor asks for. Reading them is hard for four reasons:

1. **Format.** The accounts are PDFs; many are scans with no text layer, so the numbers need OCR. A single misread digit or a missed "in thousands of CZK" changes a number by orders of magnitude — the same class of error as the 10,000× decimal bug found in the public-money audit.
2. **Small companies may hide the profit and loss statement.** Under Czech accounting law, micro and small entities without a statutory audit do not have to publish the income statement. For most startups the public filing is a balance sheet only: no revenue, but total assets, equity, cash and liabilities.
3. **Late or missing filings.** The deadline is up to 12 months after year end and many companies file late or never, so the newest public numbers are often 1–2 years old.
4. **Foreign holdings.** When the operating company belongs to a Delaware or Dutch parent, the Czech accounts show only the subsidiary.

**How.**
- Download only the latest one or two annual accounts per company, politely and cached.
- If the PDF has a text layer, parse it; if it is a scan, read the page images with OCR or a vision-capable model.
- Extract a small fixed set of fields from the standard Czech forms: revenue (if published), operating result, net result, total assets, equity, cash, liabilities, headcount (if stated). Record the unit and the page.
- Check every statement by code before accepting it: assets = liabilities + equity; subtotals add up; the prior-year column matches the previous year's filing. A number that fails a check is shown as "unreadable", not guessed.
- In the brief: "Revenue: not published (small-entity exemption)" is a fact with a source; it is never shown as zero. Derived numbers (equity burn per year as a proxy for losses, cash at year end) are labelled as estimates.

**How to measure.** Hand-check 10–15 statements (text PDFs and scans) and compare field by field; target zero accepted numbers that are wrong, at the price of some "unreadable".

**Shortcut to compare against.** Paid Czech data providers have already digitised these statements. They could serve as a cross-check, or as the source if the fund already pays for one.

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

## 6. Smaller items

- **Competitors.** Today candidates come from text similarity with NATO DIANA cohorts, and the model may reject all of them (Dronetag). Add procurement co-bidders and EU project consortium partners as sources.
- **Investment view for every brief.** Older portfolio briefs were generated before the investment view existed; regenerate them (about $0.3 in total).
- **Portfolio monitoring.** Alerts on register changes, insolvency, missing filings, hiring spikes and new public contracts.
- **Design.** The brief and showcase are a prototype; a proper design pass after investor feedback on what to show first.
- **Ambiguous names.** Detect them automatically (a `<name>.com` domain that is not the company's) instead of hand-written context terms.
