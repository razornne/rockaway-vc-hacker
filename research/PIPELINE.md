# From sourcing to investment memo: where a tool can help

> An overview of the deal funnel, written right after the portfolio analysis (`FINDINGS.md`). The chosen direction — due diligence briefs — is described in `docs/ARCHITECTURE.md`. The data-layer check is in `DATA_LAYER.md`.

Draft, 16 November 2026. How the process actually works inside Rockaway is not known from the outside; that is the main untested part.

## What is known about how deals reach Rockaway

- 9 of the 14 fund companies had already been funded by other investors, on average about 2 years before Rockaway.
- In many rounds Rockaway participates under another lead: Draper, 20VC, VentureFriends, Zenith, Inovo.
- The recent AI deals are hot rounds of repeat founders. ValkaAI's founder says "investors come by themselves".

Hypothesis: **the bottleneck is not finding the company, but deciding quickly and on evidence, and getting into the round in time.**

## The funnel and what can be automated

| Stage | What happens | What can be automated | Data | Can it be tested on the portfolio? |
|---|---|---|---|---|
| 1. Deal flow | co-investor emails, inbound, press | parse emails and decks into a CRM card; deduplicate | email, the fund's CRM | no (needs access) |
| 2. Watch list | "who will raise soon" | map of companies with VC shareholders; time since last round; repeat founders | register open data, press | partly: only Czech s.r.o. without a foreign holding |
| 3. Screening | is it worth an hour | **a brief in minutes**; a thesis filter calibrated on past decisions | register, filed accounts, Hlídač státu, press, website | yes: 14 fund deals + 10 control |
| 4. First meeting | preparation | questions for the founder from the gaps in the brief | the brief | — |
| 5. Technical DD | code, models, defensibility | "could it be rebuilt over a weekend?": product, stack, public code | website, docs, GitHub, papers | partly: on the public products of the portfolio |
| 6. Memo | text for the investment committee | a draft in the fund's template with sources | everything above | no (needs the fund's template) |
| 7. Portfolio | monitoring | alerts: register changes, insolvency (ISIR), missing filings, hiring, public contracts | register, ISIR, filed accounts | could be tested on FreewayCamper (bankruptcy 2025) |

Stages 3–5 are where public data is strong and testable, so that is what the prototype covers.

## Proposed architecture

One backbone — the company card (IČO / domain) — with modules around it:

```
sources ──► collectors ──► company card ──► outputs
 register (open data)       ownership history      brief (one page)
 ARES, filed accounts       finances               memo draft
 Hlídač státu / ISIR        contracts, grants      portfolio alerts
 press                      event timeline         watch list
 website / GitHub           technical profile      export to the fund's CRM
```

Principles:
1. **The register is parsed by code, not by an LLM.** The verification showed that agents confuse individual shareholders with investors.
2. **The LLM writes text only from collected facts**, with a source for every statement.
3. **A "the register cannot see this" flag:** foreign holding, convertible loans, a.s. without a shareholder list. Better to say honestly what the data will not show.
4. **The thesis filter is calibrated on the fund's real decisions** (14 deals), not on the website text.

## Other leads worth testing

- **CEE co-investor graph.** Deals come through syndicates, so it helps to know who invests with whom. Source: VC shareholders in the register and the press.
- **Defence as a separate vertical.** Public data is richer here: EDF participants, NATO DIANA cohorts, defence procurement. Global databases read them poorly. See `research/defense/`.
- **Early warning in the portfolio.** Insolvency register, late filings, staff outflow. Test cases: FreewayCamper and Campiri.
