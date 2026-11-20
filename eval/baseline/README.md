# Baseline: a plain model with web search vs the tool

20 November 2026. The same task for the two showcase companies: `gpt-5-mini` with OpenAI's web search tool, one call, asked for a first-look brief with a source URL for every statement (`eval/baseline.py`; outputs in `fly4future.md`, `dronetag.md`). It is compared with the tool's brief on the facts that official records settle. "Right" means it states the fact as the record does; "wrong" means it states something the record contradicts; "missed" means it is absent or reported as not findable.

| Company | Fact settled by an official record | Tool | Plain model + web search |
|---|---|---|---|
| Fly4Future | Revenue 2025: CZK 47.8M (filed income statement) | right | **wrong**: "2024 ≈ CZK 24M" from a 2024 presentation; the filed 2024 figure is CZK 45.1M |
| Fly4Future | Net result 2025: CZK 8.8M, 2024: 16.6M | right | missed ("not available") |
| Fly4Future | Cash at end of 2025: CZK 57.1M | right | missed |
| Fly4Future | Round being raised: EUR 10–16M (press) | right | partly: says a first round is open, no amount |
| Fly4Future | Grants: CZK 138.4M awarded, 32.7M paid, 18 projects | right | missed (two programmes named, no totals) |
| Fly4Future | Sales to public buyers: 2 contracts, CZK 0.76M | right | partly: one award of about EUR 22k |
| Fly4Future | Patents: 2 applications, none granted | right | missed (asks the founders) |
| Dronetag | Net result 2025: CZK 4.2M; cash CZK 19.6M | right | missed ("no accounting filings found") |
| Dronetag | Revenue: not published (small entity, balance sheet only) | right | right ("could not find revenue") |
| Dronetag | Round: CZK 15M convertible loan from Y Soft Ventures | right | partly: Y Soft named, "$600k–640k" from secondary databases |
| Dronetag | Won a Ministry of Defence tender, CZK 27.4M (TED) | right | missed |
| Dronetag | NATO DIANA 2024 cohort | right | right |
| Dronetag | Grants: CZK 22.2M awarded, 4.1M paid | right | missed; cites a ministry grant **rejection** as a grant record |
| Dronetag | Sales to public buyers: 7 contracts, CZK 1.4M | right | missed |

**Score on these 14 facts:** the tool states 14 right; the plain model states 2 right, 3 partly, 2 wrong or misleading, and misses 7.

**What the plain model does well:** it is fast (24–35 seconds) and cheap (about $0.017 per company), finds names the tool deliberately does not store (shareholders and directors from the register), and writes sensible founder questions.

**Why the tool wins on facts:** it reads the official sources directly (filed accounts, the contract and subsidy registers, EU procurement), computes totals in code, and keeps one record per project; the web search finds summaries and secondary databases, and missed every filed financial figure.

Limits of this comparison: two companies, one run each, judged by the author's AI reviewer against the official records collected by the tool. A plain model with more searches or a stronger model would do better; the point is what the extra collectors add, not that the baseline is the best possible.

## Time

A fresh company with nothing cached (Spaceti, `dd add` then the full pipeline, 20 November 2026): collection 159 s, extraction 122 s, claim checks 16 s, analysis 98 s with `gpt-5-mini`, rendering 3 s — about 7 minutes and $0.03 of model cost. The plain model above takes 24–35 seconds and about $0.017. How long an analyst needs for the same first look was not measured; that needs a person with a stopwatch, and is the next measurement to make.
