# Audit of collected data and claim checks

Started 17 November 2026. Goal: before running all companies, find and fix systematic errors by reading the output by hand. A quote that exists in the source is necessary but not sufficient: the category and meaning must match it too.

## 1. What was checked

- Every model-extracted fact for three showcase companies (Navigara, Filuta, Cruxo), about 150 facts, read by hand: does the category and meaning match the quote, not only "is the quote in the source".
- Deterministic public-money data (Hlídač státu) checked by contract subject and amount.

## 2. Errors found and fixed (first pass)

| # | Error | Example | Cause | Fix |
|---|---|---|---|---|
| 1 | Subsidy counted as a public contract | Filuta: "contract with the Ministry of Industry, CZK 35.7M" is a subsidy agreement ("Poskytnutí účelové podpory"), not a purchase from Filuta | the contract register also holds subsidy agreements | `public_money`: an agreement whose subject is support/subsidy is a grant; if the same project is already among subsidies, the agreement is attached to it, not counted again |
| 2 | One grant counted twice | Cruxo: the same CZK 2,449,765 project appears in two subsidy databases → 8.2M instead of 5.8M | the project is listed in two databases | `dedupe_subsidies`: same amount and similar title → one record (`also_listed_as`) |
| 3 | Demo numbers taken as team size | Navigara: "350 engineers" (dashboard screenshot), "OpenAI 571 engineers" (ranking example) | real quote, wrong category | `team_claim` accepted only if the quote names the company, its founders, "we / our team", CEO/CTO etc. |
| 4 | Pricing from a blog | Navigara: "moved off per-seat pricing" is about customers' AI bills, not Navigara's prices | commentary read as a price list | prices from `/blog/`, `/news/` are rejected |
| 5 | Legal boilerplate as a technical claim | Filuta: "no decision-making based on automated processing" (privacy policy) | privacy page in the sample | claims from privacy / terms / cookie pages are rejected |
| 6 | EU grant as a funding round | Filuta: "AIPlan4EU project funded by the European Commission" | category `funding_round` | a "round" without amount, stage or investors but with project / grant / H2020 → `grant_eu` / `grant_national` |
| 7 | Ranking taken as customers | Navigara: "Graded live: Microsoft, OpenAI…" | — | `customer` accepted only with a customer relationship in the quote or on a case-study page |
| 8 | Integration taken as dependency | Navigara: OpenAI and Anthropic in "Connects to" | — | signals separate `llm_vendors_used` from `llm_vendors_integrated` |

After rules 3–6, about 15 more wrong facts were rejected from cached model answers without new paid calls.

## 3. Claim checks (`dd verify`)

Code, without an LLM, checks company claims against independent sources.

| Check | Source | Navigara | Filuta | Cruxo |
|---|---|---|---|---|
| Patents | Google Patents (by assignee) | — (no claims) | **confirmed:** 6 published applications (US, EP, AU, CA), none granted. **Contradiction:** CzechCrunch says it "owns patents", there are only applications | — |
| IAB TCF | IAB Global Vendor List v185 (1,237 vendors) | — | — | **not found:** Cruxo is not on the list; may mean it uses a TCF-compatible consent platform — a DD question |
| Investors in press vs register | Czech business register | — (no Czech entity) | — (Delaware holding) | **confirmed:** Czech Founders, Presto, ZAKA and Rockaway are shareholders from 24 Aug 2026 (Rockaway 3.85%) |
| SOC 2 / ISO 27001 | security / trust pages, subdomains | **not checkable:** no trust portal, auditor or compliance platform; the report must be requested | — | — |
| Customers | news search | — (no named customers) | HISD: not found in news | **Lékárna.cz confirmed** by a news article |

A confirmed company claim gets the label **Verified**. Contradictions and "not found" appear in "Claims checked" and feed the risks and founder questions.

## 4. Web search: Tavily and Exa

Comparison on 9 identical queries (`eval/compare_search.py`, result in `eval/search_comparison.md`):

| Provider | Results | About the company | Independent (not the company's site) | Unique to it | Latency |
|---|---|---|---|---|---|
| Tavily | 80 | 58 | 51 | 46 | 1.3 s |
| Exa | 75 | 70 | 43 | 35 | 2.3 s |
| No key (news) | 84 | 4 | 4 | 1 | 5.9 s |

- Without a key, search is almost useless. Tavily finds more external sources, Exa is more on topic. They overlap little, so **both are used**.
- Aggregator profiles (CB Insights, Tracxn, Preqin, Caplight…) and the company's own pages are not counted as press.
- New check **`public_sector_vendor`**: the company on government sites. Filuta is listed as a vendor of the Texas Department of Information Resources — an official, independent sign of a route to public buyers in Texas.
- Cruxo: both named customers confirmed independently (Lékárna.cz, Dr. Max).
- Navigara: 21 articles instead of 6.
- Fixed along the way: a metadata date "2014-01-01" on a `/2025/06/25/` URL (the URL year now wins when they disagree); an undated report of a round now merges with the same round by amount and investors.

## 5. Full run over 14 companies (17 November)

Everything ran on the first attempt: 14 of 14 briefs, golden set 18/18, every quote of LLM-extracted facts found in the saved source text. Errors that appeared only on new companies:

| # | Error | Example | Fix |
|---|---|---|---|
| 9 | An ATS provider's site taken as the company's careers page | Vermeer: `vermeer.homerun.co` links to `homerun.co`; Homerun's marketing pages and its clients became "Vermeer customers" | `ats_tenant()`: from ATS pages only the company's own board is used |
| 10 | Someone else's job board on a shared ATS | ValkaAI links to `jobs.lever.co/oddin`; Oddin.gg jobs appeared under "Hiring" | same rule; the row stays empty rather than false |
| 11 | Name collision | "Vermeer" is also Vermeer Manufacturing (hay-press patents, public contracts), Vermeer LLP, Vermeer Capital, Dura Vermeer | `context_terms` in `eval/companies.json`: for an ambiguous name, a page counts only if it has the domain, or the name plus a context word |
| 12 | Other companies' patents via a substring of the assignee | Valpas: "V. P. VALPAS VALVOLE S.r.l." (valves), a private individual | `assignee_matches()`: the assignee must **start** with the company name |
| 13 | A Google Patents failure (HTTP 503) cached and shown as "no patents" | Duvo, ValkaAI, BottleCap | temporary errors are not cached; one polite retry; on failure only `source_unavailable`, no conclusion |
| 14 | Aggregator profile as customer evidence | Wultra: CB Insights page | aggregator hosts excluded from customer checks |
| 15 | One round split into two | Apaleo: "PSG" and "PSG Equity…" a day apart | investors match when one name contains the other |
| 16 | Factual items labelled "Analyst view" | "Series A €9M, Rockaway and Serpentine" | in factual sections the label is computed from sources; "Analyst view" stays for risks, rebuild verdict and questions |
| 17 | Empty bold prefix in Markdown | `****Series A…` | renderer fixed |
| 18 | The company became its own customer | Wultra: "Customers: OTP Bank Moldova, Wultra" | the company's own name is excluded |
| 19 | A contract without a price shown as "0 CZK" | Wultra: framework agreement with Česká pošta | shown as "amount not published", with counterparties |
| 20 | Covid-era wage compensation counted as a public contract | Wultra: "Antivirus" programme agreement | recognised as a subsidy and attached to the programme |
| 21 | Duplicate in the stack | "Cloudflare, cloudflare" | case-insensitive |
| 22 | Discarded pages still used in extraction | Vermeer after fixes 9 and 11 | extraction uses only documents referenced by current `web` and `press` facts |

## 6. Defence briefs (18 November)

Checks of the Fly4Future and Dronetag briefs found two more:
- R&D consortium budgets counted as contracts with the company;
- a decimal misread that inflated a public-money total 10,000 times.

Both are fixed in code and covered by tests. Later the key-number tiles were changed so that a source that was not read shows *Not checked* with the reason, not *None found*.

## 7. Outside review (20 November)

An outside code review of the repository and the published briefs found two more errors and one design problem.

| # | Error | Example | Fix |
|---|---|---|---|
| 25 | The model did arithmetic on round size vs ticket, and got it wrong | Dronetag: "round size exceeds Rockaway initial ticket" for a CZK 15M round (≈ €0.6m) against a €0.5–2m ticket; it also treated the round as if it were the fund's cheque | `thesis.stage_ticket()` compares the round with the ticket in code (currency converted at stated approximate rates) and says that a round is the total from all investors; the model is told not to restate the comparison, and older model statements on it are dropped at render time. Regression test on the Dronetag case |
| 26 | Grants added up across registers that list the same project | Fly4Future: CZK 211.6M shown. The same TA ČR project appears as an award in IS VaVaI and as payments in IsRed; signed support agreements in the contract register were added as further grants; EU-fund records carry a register year of 2027–2028 that was drawn on the chart as if money arrived then | `merge_projects()`: one record per project (by project code, CZ code in the title, or a long title across registers); `amount_czk` = awarded to the company (the signed agreement when it is larger than the register's figure, never less than what was paid); `paid_czk` / `paid_by_year` only from payment records. The chart shows payments only. Fly4Future: CZK 134.3M awarded, 32.7M paid so far |

Design change from the same review: the rebuild check no longer gives a time-to-clone verdict ("a quarter to clone core autonomy" cannot be known from public pages). It now has three parts — what off-the-shelf parts could reproduce, what edge public evidence supports, and what cannot be judged from outside — and items containing a time estimate are dropped.

The review also pointed out that the headline metrics are guards, not accuracy: quotes found in sources rule out invented quotes but not misreadings; evidence labels describe where evidence comes from, not whether a conclusion is right. The showcase now says so, and a hand-labelled accuracy check is the next step (see `ROADMAP.md`).

## 8. Accuracy check, baseline and filed accounts (20 November)

A second outside review asked whether the evidence labels overstate compound statements, whether amounts are written one way, and whether the tool is better than a plain model. Answering it found four more errors.

| # | Error | Example | Fix |
|---|---|---|---|
| 27 | A statement was labelled *Verified* when only part of its evidence was official | A finding citing a register record and one press article showed *Verified* | `render.item_strength()`: *Verified* only if every cited source is official or technical; official plus one outlet is *Partly verified*; official plus two or more outlets is *Corroborated*. Tests in `test_evidence.py` |
| 28 | Amounts in the source's words, or without a currency | Dronetag: "15 milionů korun" in a table; the showcase card showed the round with no currency | `thesis.format_money()`: one format everywhere ("15M CZK", "10–16M EUR"), the original wording kept beside it as "as reported"; compound amounts ("100M CZK + 4–5M EUR") are not turned into one number |
| 29 | Grouped thousands read as a decimal | Spaceti: "28,000,000 CZK" parsed as 28 and shown as "0k CZK" | `thesis._num()`: "28,000,000" and "28.000.000" are thousands; a single comma group ("28,000") is thousands unless a word like "million" follows. Test cases in `test_ticket.py` |
| 30 | Czech news pages in windows-1250 decoded as UTF-8 | Spaceti: investor "Radomír Čech" stored as "Radom�r �ech" | `Resp.text` uses the charset from the header or the page's meta tag, then UTF-8, then windows-1250. Test in `test_http_text.py`. Briefs collected before the fix keep the garbled text until re-collected |

**Semantic accuracy.** All 72 statements of the two defence briefs were judged against their cited sources (`eval/labels/`). No material errors; two wrong numbers (a price ceiling, "up to CZK 1.5M" per drone, read as the price) and two conclusions from missing data (Dronetag "has no product surfaces", although its apps and API docs were collected — the facts were in the database but not in what the analysis cited). Both are model errors, not fixed in code; the prompt already forbids conclusions from absence. The labels were made by an AI reviewer, not a person.

**Filed accounts.** The new reader rejects a filing unless total assets equal total equity and liabilities and the net result agrees between the two statements. Building it surfaced three form layouts (row-number column or not, thousands spaces or not, "Kč" or "CZK"); each is handled and tested. Scanned filings are shown as *Not read*.

## 9. What remains a limit

- An ambiguous company name has to be marked by hand (`context_terms`); it is not detected automatically.
- SOC 2 cannot be checked publicly; the report is shared under NDA. The brief says "not checkable".
- Testimonials on a website are linked to a customer by nearby text; the quote itself does not name the customer.
- Round merging uses a 60-day window and shared investors; an old round restated in a new article can merge with a new round.
