# Rockaway Ventures portfolio: what the public data showed

16 November 2026. Raw data: `companies/*.json`, `control/*.json`, `fund/`. Tables: `signals.md` (rebuild with `python research/aggregate.py`).

The data was collected from public sources by research agents and then checked by hand for the key facts (see "Verification" below). Treat numbers not covered by that check as a first pass.

## Scope

- **Fund (n=14):** Rockaway Ventures deals 2022–2026: Apaleo, BottleCap AI, Campiri, Cruxo, CulturePulse, Filuta, FreewayCamper, Navigara, Raus, Remix, Spotawheel, ValkaAI, Valpas, Vermeer.
- **Group legacy (n=4):** Productboard, Bezrealitky, Creditas, Gjirafa. Rockaway Capital investments made before the fund existed, mostly through personal networks. Not used to judge the current fund's strategy.
- **Excluded:** Apptronik, a large US round rather than an example of finding companies in CEE.
- **Control group (n=10):** Czech rounds led by Credo, Kaya, Tensor, Reflex and J&T, 2023–2026.
- **Not researched:** Storyous, Brand Embassy, BudgetBakers, Samba.ai — possible older investments where no Rockaway entity could be confirmed.

## Main observations

**1. Rockaway is usually not the first money in.**
In 9 of the 14 fund companies, outside funding was publicly visible before Rockaway invested: a median of 28 months before T0 (range 15–73).
After verification: in all 9 cases it was **the press** about an earlier round that showed it first, not the business register. Register entries that the agents had read as "new money" at Filuta, Campiri and Cruxo turned out to be reshuffles inside the team: founders, their holding companies, partners.
Pre-seed investors seen in the data: Czech Founders VC (Filuta, Cruxo), Nation 1 (Filuta), Miton (Campiri), Speedinvest (Raus), Zero Gravity (CulturePulse).
The control group looks the same: 8 of 10, median 17 months.

**2. The register entry for the round itself does not beat the press.**
- Campiri: Rockaway Ventures Fund SCSp SICAV-RAIF was registered as a shareholder on 4 May 2022, 7 days before the announcement.
- Grid.online (control): 0.2 months before.
- Cruxo: Rockaway appeared in the register 21 months after the announcement. The 2023 seed investors (Czech Founders, Presto, ZAKA) also appear only in 2026; the money most likely came as convertible loans.
- Filuta (Delaware Inc.) and ValkaAI (Valka.AI B.V.): the Czech s.r.o. is 100% owned by a foreign holding, so the round never shows in the Czech register.

The hypothesis "a register entry may precede the press" did not hold for Rockaway's own rounds. The register is valuable for something else: it shows earlier rounds, years before T0.

**3. The 2026 AI deals work differently.**
- ValkaAI, BottleCap AI and Navigara were less than a year old and had no earlier rounds.
- The first meaningful signal was the first article in the Czech press, 9.5–11 months before T0. For Navigara no such signal was found.
- The signal here is the founder. BottleCap AI was founded by Jaroslav Beck, creator of a well-known game studio; ValkaAI's founder says investors approached him.

A register-based radar does not catch these deals.

**4. Public contracts and grants are rare in the portfolio.**
- Fund: 0 of 14 companies had a public contract before T0. Filuta's agreement with the Ministry of Industry came 3 months after T0. A national grant before T0 was found only at FreewayCamper (Germany).
- Control group: 4 of 10 had a public contract before T0 (Wultra, Delta Green, Digitoo, DYNANIC).

The Czech contract register is not a source of Rockaway deals so far. It may matter for defence and energy; that is a hypothesis.

**5. Rockaway often joins rounds led by others.**
- Lead or co-lead: Campiri, Filuta, ValkaAI, Apaleo, FreewayCamper.
- Under another lead: Spotawheel (VentureFriends), Vermeer (Draper), Valpas (Zenith), BottleCap AI (20VC), Navigara (probably Inovo), Raus.

This matches the NBER survey by Gompers et al., where about 20% of deals come through other investors. The co-investor network is a real channel. Only a few repeat co-investors were reliably found: Redalpine, PSG, Miton.

**6. Registers outside Czechia were barely readable.**
- Northdata answered 429, another aggregator 403.
- ARBK (Kosovo) is a JavaScript application.
- GEMI (Greece) was not checked.
- Delaware does not disclose shareholders.

Outside Czechia a radar would rely on press, accelerators and earlier rounds.

**7. The thesis on the website is not the same as the actual deals.**
- Fund page: late seed / Series A (elsewhere on the same page: seed to Series A), proven product and early customers.
- 2026 reality: a €12M pre-seed (ValkaAI); seed rounds in companies less than a year old.
- The deals include consumer marketplaces (Campiri, Remix, Raus), although the stated sectors are AI and deep tech.

A "thesis as code" filter has to be calibrated on the fund's real decisions, not on the website text.

## What this meant for the tool

1. **Finding companies earlier from public data does not work well** for this fund: the register rarely shows the round first, strong companies hold their shares abroad, and hot AI rounds are driven by founders and networks.
2. **Checking a company that is already on the table works well.** The same sources — register, public money, press, the company's own website and code — answer diligence questions quickly and with sources.
3. **The register has to be parsed by code.** Agents retold press articles accurately but misread the register (see below). The DD tool therefore parses structured sources deterministically and lets a language model handle only unstructured text, with a verified quote.

This is why the project moved from a sourcing radar to a due diligence tool.

## Verification (16 November 2026)

Key facts about Filuta, Cruxo, Campiri, ValkaAI and Valpas were checked against primary sources: full extracts on or.justice.cz, ARES, the articles themselves, Hlídač státu.
Articles and dates held up. The errors were in how the register had been read:
- **Campiri.** An agent wrote that Rockaway was not in the register. In fact the fund is registered as a shareholder from 4 May 2022.
- **Filuta, Campiri, Cruxo.** "New shareholder" entries were founders, their holdings and partners, not investors. The event type was corrected to `registry_other`.
- **ValkaAI.** Lupa says "last year" (2025); E15 says the round would close "by the end of June–July 2025" and that "investors come by themselves". The deal probably closed about 7 months before the announcement.
- **Valpas.** Rockaway's participation is confirmed by a tech.eu article.

Conclusion on quality: agents pass on facts from articles accurately, but read the register superficially, confusing individual shareholders with investors and skipping rows.

## Known gaps

- The Wayback Machine failed several times; job, pricing and customer pages were barely checked.
- STARFOS, CORDIS and TED were not checked for every company.
- Raus dates differ by a month (October or November 2023).
- T0 for Creditas is a low-confidence estimate.
- No LinkedIn and no paid databases were used. Facts taken from retellings of pages are marked `confidence: medium/low`.
- 14 deals are a case study, not statistics, and only deals the fund actually made are visible.
