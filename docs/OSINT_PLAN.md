# OSINT checks: plan

25 November 2026. From an investment analyst's review: the useful part of a brief is not what a company says about
itself (PitchBook and Tracxn parse that too) but whether indirect public traces confirm it, and what the people behind
it have done elsewhere. This plan says where each piece of data comes from, how it is read, and what is stored.

Principles carried over from the rest of the tool: every finding has a source URL; an empty result says where we looked
and what that source cannot show, never "none"; structured sources are parsed by code; no LLM calls are needed for any
of the checks below (cost: zero model spend).

## 1. Data sources (checked on 25 November 2026)

| Source | What it gives | Access | Verified |
|---|---|---|---|
| ARES VR (`ares.gov.cz/.../ekonomicke-subjekty-vr/{ico}`) | officers and natural-person shareholders of the company, with role, dates, share; first name, surname, birth date | JSON API, already used | yes, fields seen in cache |
| Register open data (`dataor.justice.cz/api/file/{sro,as}-full-{court}-2026.xml.gz`) | every s.r.o. and a.s. in Czechia with officers, shareholders (name, birth date), and sections INSOLVENCE, KONKURS, LIKVIDATOR, ZAHAJENI_O_ZRUSENI, EXEKUCE | official bulk open data; 14 files, about 806 MB compressed | yes, sizes and fields seen |
| ISIR web service (`isir.justice.cz:8443/isir_cuzk_ws/IsirWsCuzkService`) | insolvency proceedings by IČO, or by surname + first name + birth date | SOAP, no key | WSDL and fields read; not called yet |
| ADIS `rozhraniCRPDPH` (`adisrws.mfcr.cz/.../rozhraniCRPDPH.rozhraniCRPDPHSOAP`) | unreliable VAT payer status by DIČ (up to 100 per call) | SOAP, no key | WSDL read; endpoint host to be confirmed on first call |
| EU consolidated sanctions list (`webgate.ec.europa.eu/fsd/fsf/public/files/csvFullSanctionsList_1_1/content?token=dG9rZW4tMjAxNw`) | persons (with birth dates) and entities under EU financial sanctions | CSV, 25 MB, public token | yes, downloaded |
| Czech national sanctions list (`mzv.gov.cz/file/6248997/Vnitrostatni_sankcni_seznam_2026_07_23.csv`) | national list | CSV from MZV open data | link seen |
| Hlídač státu subsidies (already collected) | penalty waivers by ČSSZ or tax offices, recorded as "support" | already in facts | yes (Fly4Future: ČSSZ "prominutí penále") |
| Job boards: Greenhouse, Lever, Ashby, Personio public APIs | open roles with team and location | JSON/XML, no key | docs read |
| Wayback Machine (already used) | earlier versions of the careers page | CDX + raw snapshots | yes |

Not used, and why:
- `or.justice.cz/ias/*` person search and `isir.justice.cz` web pages: robots.txt disallows automated access (the
  ISIR form also has a captcha). See section 4 for what this means for collectors we already have.
- LinkedIn, PitchBook, Crunchbase, Dealroom: excluded by project rules.
- Central register of distraints (paid per query), beneficial-owner register (access restricted since 2024), court
  decisions (names of individuals are anonymised): no usable free route.

## 2. Checks

### A. Claims against records (code only, on facts we already collect)

| Check | Claim (from extracted facts) | Record it is compared with | Result |
|---|---|---|---|
| AI | the company says it builds AI or its own models | own-model evidence (papers, published models, ML repositories), ML job posts, LLM vendors it lists | confirmed (own models or ML hires) / partly (uses third-party models only) / not visible |
| Team size | a stated headcount | personnel costs in filed accounts, converted to a range of full-time staff at stated cost assumptions; open roles | consistent / higher than the accounts support |
| Revenue | a revenue figure for a year | filed revenue for that year | confirmed within 15% / contradicted beyond 30% |
| Public and defence customers | "we supply the army / ministries / cities" | contracts register, TED, procurement facts | confirmed / not visible (with the note that defence purchases are often unpublished) |

Results are `verification` facts, so they feed the existing "Claims checked" table and the scorecard.

### B. People and their other companies

1. From ARES VR take current and past officers, proxies, supervisory board members and natural-person shareholders:
   name, role, from, to, share.
2. Stream the 14 register dumps once per batch, matching people by first name + surname + birth date. The birth date
   is used in memory only and never stored. Collect for each person every other company role: company, IČO, role,
   from, to, and whether that company has an insolvency, bankruptcy, liquidation or dissolution entry.
3. Derived signals:
   - focus: number of other active executive roles (director, board) held now;
   - track record: earlier companies that ended in insolvency, bankruptcy or court dissolution, with years;
   - connections: people shared with Rockaway portfolio companies or Rockaway entities;
   - distraint entries (EXEKUCE) on the company's own shares.

Stored: names, roles, dates, shares, company names and IČOs, all public in the register. Not stored: birth dates,
addresses. The dumps cover s.r.o. and a.s. only (other legal forms and foreign companies are named as not covered).

### C. Insolvency of people and companies

ISIR web service, one call per person (surname, first name, birth date) and one per company IČO. Result: number of
proceedings and their state, with a link to the proceeding.

### D. Tax and sanctions

- Unreliable VAT payer: the company and the other active companies of its people (by DIČ from ARES).
- Sanctions: the company (name, IČO) and its people (name + birth date in memory) against the EU consolidated list and
  the Czech national list. These are complete lists, so "not on the list as of <date>" is a statement about the list.
- Penalty waivers already in the subsidy data (ČSSZ, tax offices) become a flag, no longer a grant.

### E. Hiring over time

- Public job-board APIs when the careers page links to Greenhouse, Lever, Ashby or Personio.
- Up to one Wayback snapshot of the careers page per year for the last three years, parsed with the existing job
  extractor: roles by function per year, to show where the company is heading.

## 3. Where it shows

- A brief section **People and background**: one row per person (role, since, other active roles, earlier companies
  and how they ended, insolvency, sanctions), every cell with its source.
- **Claims checked** moves into the decision layer, after risks and questions.
- New flags feed the scorecard's "Before or on the call" list: penalty waivers, unreliable VAT payer, insolvency of a
  person or of an earlier company, many active roles elsewhere, a person shared with the portfolio, distraint on
  shares, sanctions hit. Team stays unscored.
- Hiring by year appears under Open roles.

## 4. Decisions (Mykyta, 25 November 2026)

1. People are matched on first name + surname + birth date; the birth date is used in memory only and never stored.
   Stored: names, roles, dates, shares, company names and IČOs.
2. robots.txt on `or.justice.cz/ias/` and `isir.justice.cz` disallows automated access. The registry collector reads
   filed accounts from `or.justice.cz/ias/ui` and the company insolvency count from the ISIR web pages (a few targeted
   requests per company); these stay as they are. New person checks use the ISIR web service, not the web pages.
3. The register dumps (about 806 MB) are downloaded once into `data/dataor/` (git-ignored) and kept as a cache.

## 5. Order of work

1. A (claims against records) and the penalty-waiver flag: code only, no new network.
2. D (tax and sanctions).
3. B (people, other companies, connections) and C (insolvency via the web service).
4. E (hiring over time).
5. Brief section, scorecard flags, site, docs, tests; re-collect the new sources for the 16 companies and rebuild.

## 6. Implementation (25 November 2026)

`dd/osint/`: `claims.py` (A), `people.py` (B), `checks.py` (C, D), `hiring.py` (E), `view.py` (what a brief shows and
the flags passed to the scorecard), `run.py` (`uv run dd osint IDS|--all [--offline] [--download-dumps]`).

- OSINT facts are stored with extractors `osint_*`; `dd.analyze.fact_snapshot_sha256` skips them and the analysis
  never sends them to the model, so adding them does not make a brief stale and costs no model spend.
- Claim checks are recomputed from all facts at render time, so they reach the "Claims against records" table and the
  scorecard without a new analysis.
- Headcounts that are plans ("the goal is a team of 60 to 100", "we should reach 43") are skipped: the first run read
  Fly4Future's hiring target as its team and would have called it contradicted.
- Person lookups (ISIR) are made without the HTTP cache. ARES VR responses in the cache are raw register copies and
  contain birth dates and addresses, as before; nothing from them beyond names, roles, dates and shares reaches facts.
- The EU consolidated list endpoint sometimes answers with an error page under HTTP 200; that is recorded as
  *not checked*, never as "not on the list".
