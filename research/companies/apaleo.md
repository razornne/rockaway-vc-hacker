# Apaleo (Germany, Munich) - Rockaway signal retrospective

**T0: 2023-03-01 (announced).** Entity: Rockaway Ventures, co-lead with Serpentine Ventures in the Series A extension (round total EUR 9m). Rockaway ticket and extension size not disclosed. No separate deal date visible. Source: https://apaleo.com/blog/apaleo-news/apaleo-series-a-extension-9m

Legal entity: Apaleo GmbH, Munich, HRB 229514 (from a Bundesanzeiger filing listing, https://www.unternehmen24.info/Handelsregister/Deutschland/Bilanz/Firma/4281209/Jahresabschluss zum Geschäftsjahr vom 01_01_2023 bis zum 31_12_2023).

## Timeline

| Date | Source type | Event | Months before T0 | Conf. |
|---|---|---|---|---|
| 2017-01 | registry_incorporation (company statement, not registry) | Founded January 2017 per [seed release](https://www.hospitalitynet.org/news/4083435.html) | 74.0 | medium |
| 2017-06-10 | website_first | Earliest 2017 Wayback capture of apaleo.com (301; domain older, other use) | 68.6 | low |
| 2017-06-26 | prior_round | Seed via "apaAngels", amount undisclosed ([Hospitality Net](https://www.hospitalitynet.org/news/4083435.html), [Munich Startup 2017-07-11](https://www.munich-startup.de/news/apaleo-seed-finanzierung)) | 68.1 | high |
| 2017-10-27 | website_first | First 200 capture of www.apaleo.com | 64.1 | medium |
| 2021-03-31 | press_round | EUR 4.5m Series A, Force Over Mass lead, Redalpine, Bayern Kapital ([Apaleo](https://apaleo.com/blog/apaleo-news/apaleo-funding-round-series-a)) | 23.0 | high |
| 2021-06-19 | hiring | Earliest capture of /careers/ (lower bound only) | 20.4 | low |
| 2023-03-01 | rockaway_announced | Series A extension to EUR 9m | 0 | high |

## Earliest public signal before T0
Earliest dated item found: seed announcement, 2017-06-26 (prior_round), 68.1 months before T0. Founding month (Jan 2017) is from the same release. For a Rockaway-relevant radar the first actionable signal is the Series A press on 2021-03-31 (23 months before), which already shows Redalpine and Force Over Mass as the investor network.

## Likely deal source
Not stated publicly. Visible only: Rockaway entered as a new growth investor alongside Serpentine Ventures, joining existing investors Redalpine and Force Over Mass. No prior Rockaway link to those investors was checked (also_coinvested_with_rockaway_elsewhere = null). Rockaway partner quoted: Andrea Lauren (General Partner).

## After T0
2024-11-10: EUR 20m growth equity led by PSG, with Redalpine, FOMCAP IV and Rockaway Ventures ([nordic9](https://nordic9.com/news/apaleo-secures-20-million-growth-equity-investment-led-by-psg-joined-by-redalpine-fomcap-iv-and-rockaway-ventures/)). No exit found.

## Registry accessibility
- Germany has a full commercial register (Handelsregister, HRB) with capital changes, officers, and annual accounts in Bundesanzeiger, so Czech-style registry signals (incorporation, Stammkapital increases, financial statements) exist in principle.
- Practical access in this run was poor: northdata.de rate-limited (HTTP 429) after two requests, openregister.de returned 403, handelsregister.de is a session/form interface and was not queried. Only the HRB number and a FY2023 filing existed via a search aggregator.
- German register entries show managing directors, not shareholders; shareholder identity needs the downloadable Gesellschafterliste. So "registry_new_shareholder" is weaker than in Czech OR.
- Government-contract and national-grant signals are low relevance for a B2B hotel SaaS. Bayern Kapital (state-backed VC) appears as an investor, not as a grant.
- Verdict: usable but not scrapable at scale without a paid/aggregator route; for a CEE+DACH radar budget for North Data-style access.

## Not found
Exact Handelsregister dates and capital figures; grants (national/EU); accelerator; customer-page and pricing history before 2020; Rockaway closing date. Details in JSON `not_found`.
