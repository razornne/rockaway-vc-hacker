# Roadmap

What I would build next, in order of value for an investment team. Each item says what problem it solves, how, and how to tell whether it worked. Nothing here is built yet.

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

**Problem.** Outside Czechia the tool only flags a foreign holding; it does not read the register. Rockaway's deals sit across CEE and DACH.

**How.** One collector per country, the same contract as the Czech one: parse structured data by code, store each fact with a URL, show *Not checked* when a source is unavailable. Candidate sources (availability and terms to verify before building):

| Country | Company register | Financial statements |
|---|---|---|
| Slovakia | ORSR | Register of Financial Statements (RÚZ), open API with structured statements |
| Poland | KRS, open API for extracts | Financial statements repository; filed electronically as structured XML since 2018 |
| Estonia | e-Business Register, open data | annual reports in structured form |
| Hungary | e-cegjegyzek | e-beszamolo (financial statements portal) |
| Romania | ONRC | Ministry of Finance publishes basic balance-sheet indicators per company |
| Slovenia | AJPES | AJPES (annual reports, basic data free) |
| Austria | Firmenbuch (paid extracts) | via Firmenbuch |
| Germany | Handelsregister (free since 2022) | Unternehmensregister |

Next to registers, each country has its own public procurement portal, grant agencies and tech press, which matter as much as the register.

**Order.** Slovakia and Poland first: structured financial statements, close to the Czech model, and many CEE deals there. Then Estonia, where data is the most open.

## 3. Compare Anthropic models with the current OpenAI setup

**Problem.** The analysis — findings, risks, investment view — is only as good as the model that writes it. The current setup (`gpt-5-nano` for extraction, `gpt-5-mini` for analysis) was chosen for cost under a hard budget.

**How.**
1. Make the LLM layer provider-neutral: the same structured-output schemas, cache, cost ledger and hard budget for OpenAI and Anthropic.
2. Run an A/B on the same collected facts, so only the model changes:
   - extraction: Claude Haiku 5.5 vs `gpt-5-nano`;
   - analysis: Claude Sonnet 5.5 vs `gpt-5-mini`.
3. Measure what the tool already measures — golden facts, quote integrity, share of Verified/Corroborated findings — plus a blind read of both versions by an investor: which brief would you rather take into a meeting, and which statements are wrong?
4. Check current prices before the run. The cost ledger gives the volume: an analysis call averages about 15.6k input and 2.6k output tokens, so cost per brief follows directly from the price list.

**Decision rule.** Switch a step only if the stronger model gives fewer wrong or unsupported statements at an acceptable cost per brief, not because it reads better.

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
