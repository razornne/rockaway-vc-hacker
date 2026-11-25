# Campiri — due diligence brief

campiri\.com · Campiri s\.r\.o\. · IČO 09283447 · CZ · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — part of it rests on an official or independent source, part on one outlet or the company's own words; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A digital RV/caravan rental marketplace connecting private owners and rental fleets to consumers, plus investor\-facing programs and full\-service handling\. *(Corroborated)* ^[1](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri),[2](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion),[3](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- **Stage & traction.** Multiple press\-reported financings totaling €4\.64M \(reported\), confirmed registry shareholders include Rockaway and Miton; claims of 400–600 listed vehicles and own fleet \~25\. *(Corroborated)* ^[4](https://shorttermrentalz.com/news/campiri-funding-expansion/),[5](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[6](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[7](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
- **Technology & moat.** Limited public technical differentiation — customer guarantees and service operations are the main claimed differentiators, not disclosed proprietary models or unique stack\. *(Partly verified)* ^[9](https://www.campiri.com/cs-cz),[10](https://www.campiri.com/cs-cz),[11](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/),[12](https://www.campiri.com/cs-cz)
- **Key risk.** Investor\-facing guarantees and fixed\-yield investment products \(6–8% claimed\) combined with debt for fleet financing create contingent obligations that require validating unit economics\. *(Analyst view)* ^[13](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[14](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[15](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
- **Diligence focus.** First verify true fleet size/composition and utilization, the cashflows supporting the 6–8% guaranteed returns, and the terms of the reported debt and investor commitments\. *(Analyst view)* ^[7](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/),[13](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[14](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2021\-01 · 14M CZK · Petr Jahn, Miton, Paul Tesar · 2 reports; 2022\-05\-11 · equity · 67M CZK · Rockaway Capital, Miton, Eva Janečková, Olda Bajer, Purple Ventures, Oldřich Bajer, Petr J · 4 reports; 2022\-05\-11 · debt · 32M CZK; 2022\-05\-12 · 4\.64M EUR; date n/a · 1–2M CZK | 16, 17, 18, 19, 20, 21 |
| Investors in registry | Rockaway Ventures Fund SCSp SICAV\-RAIF \(from 2022\-05\-04, 10\.43%\); Rockaway Ventures Fund SCSp \(from 2023\-11\-09, 11\.16%\); Breyer Invest UG \(from 2026\-07\-22, 16\.25%\) | 22, 23, 24 |
| Thesis fit \(Rockaway\) | sectors: AI\-led transformative tech \(3 facts\) · geography: CZ \(core region\) · overlaps portfolio: Spotawheel \(greece, operati, poland\), FreewayCamper \(campiri, rental\), Creditas \(fintech, secured\) | 25, 26 |
| Engineering footprint | product surfaces: api\.staging\.campiri\.com, docs\.campiri\.com; stack: Next\.js | 27, 28 |
| Customers | public pricing: yes | 29 |
| Claims checked | Investors vs registry \(MITON Happy Campers s\.r\.o\., Rockaway Ventures Fund SCSp\): confirmed | 6, 5 |
| Timeline | Czech entity registered 2020\-06\-26; first press 2021\-01 \(13 articles collected\) | 30, 25 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** Consumer marketplace / travel tech with a digital rental marketplace and platform\-led expansion claims, aligning with Rockaway’s interest in AI\-led transformative and industrial/consumer platform plays\. *(Analyst view)* ^[31](https://shorttermrentalz.com/news/campiri-funding-expansion/),[32](https://podmaz.sk/podcast/jiri-rostecky/4242929872-100-milionu-za-3-roky--jak-roste-campiri-lukas-janousek),[33](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion)
  - Assumption: Platform\-led expansion implies transformative\-tech thesis relevance
- **Portfolio overlap:** FreewayCamper \(linked publicly to Campiri\) — appears adjacent \(camper rental marketplace\); could be synergy in product/market or channel overlap depending on geographic/customer segmentation\. *(Analyst view)* ^[34](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[32](https://podmaz.sk/podcast/jiri-rostecky/4242929872-100-milionu-za-3-roky--jak-roste-campiri-lukas-janousek),[35](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Overlap judged from shared camper\-rental business model

## Business model

- Primary revenue: commissioned marketplace rental business connecting motorhome owners \(private and fleets\) with renters; company markets &gt;400 vehicles and claims platform transaction volume\. *(Corroborated)* ^[36](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri),[7](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/),[31](https://shorttermrentalz.com/news/campiri-funding-expansion/)
- Ancillary revenue and investor products: two investor programs \(passive secured loan and purchase/revenue\-share\), plus retail voucher sales and add‑ons \(insurance, bike rental\)\. *(Partly verified)* ^[15](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[37](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[38](https://shop.campiri.com/),[11](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/)

## Competition

No sourced findings for this section.

## Case for and against

- **For:** Product\-market traction — reported 20M CZK first‑year turnover, &gt;400 vehicles on platform and own fleet \(25 vehicles\), indicating supply depth and monetizable bookings\. *(Analyst view)* ^[39](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038),[7](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Revenue and fleet claims reflect sustainable demand
- **For:** Institutional validation — repeated financings and Rockaway participation \(registered shareholder, multiple press reports of €4\.64m total raised\) provide investor validation and capital for expansion\. *(Analyst view)* ^[23](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[4](https://shorttermrentalz.com/news/campiri-funding-expansion/),[21](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion)
  - Assumption: Reported rounds reflect committed capital
- **Against:** Financial promise risk — retail investor products promise guaranteed 6–8% returns and revenue\-sharing, which can create performance/liability risk if fleet utilization/maintenance costs underperform\. *(Analyst view)* ^[13](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[15](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[3](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
  - Assumption: Guaranteed returns depend on future utilization
- **Against:** Capital intensity and leverage — company used \~32M CZK debt for fleet purchases and maintains owned fleet, exposing it to asset financing risk and working\-capital strain if bookings dip\. *(Analyst view)* ^[14](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[21](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion)
  - Assumption: Debt is tied to fleet acquisition
- **Must be true:** Investor\-program unit economics — diligence must confirm that guaranteed 6–8% returns and revenue\-share terms are historically met at scale and stress\-tested across seasons\. *(Analyst view)* ^[13](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[15](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[39](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
  - Assumption: Historical seasonality data is available for review
- **Must be true:** Legal and operational compliance for investor products and cross\-border operations — confirm regulatory compliance in target markets and contractual clarity for investor protections and insurance coverage\. *(Analyst view)* ^[15](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[35](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[3](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
  - Assumption: Cross\-border product rollouts involve differing regulations

# Technical due diligence

## Ownership and capital

- Press and filings report equity/debt financings: €4\.64M total reported funding round \(2022\) and a 32M CZK debt tranche for fleet purchase\. *(Corroborated)* ^[4](https://shorttermrentalz.com/news/campiri-funding-expansion/),[14](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Press summaries reflect aggregated rounds\.
- Registry shows named shareholders and changes: MITON Happy Campers s\.r\.o\. registered 17\.04% \(from 2022\-05\-04\) and Rockaway Ventures Fund SCSp at \~11\.16% \(from 2023\-11\-09\)\. *(Verified)* ^[40](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[23](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
  - Assumption: Registry snapshots reflect ownership at those dates\.
- Later registry entries include FWC \- FreewayCamper GmbH recorded as a shareholder \(100% at 2024\-05\-14 in the dataset\)\. *(Verified)* ^[34](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
  - Assumption: Registry filing correctly records share transfers\.

## Technology profile

- Product capabilities \(company claims\): marketplace with dynamic pricing, add‑ons, vouchers, reservation guarantees, cancellation/damage insurance and investor service programs\. *(Partly verified)* ^[11](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/),[38](https://shop.campiri.com/),[9](https://www.campiri.com/cs-cz),[41](https://www.campiri.com/cs-cz),[15](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
  - Assumption: Site and press reflect live product features\.
- Engineering footprint: public web surfaces and staging API subdomains \(docs\.campiri\.com, api\.staging\.campiri\.com\) and public evidence of Next\.js on the site\. *(Verified)* ^[27](https://crt.sh/?q=%25.campiri.com&output=json),[28](https://crt.sh/?q=%25.campiri.com&output=json),[12](https://www.campiri.com/cs-cz)
  - Assumption: Subdomains indicate deployed web services\.
- Team / hiring: company claims rapid growth \(6→40 employees\) and plans to recruit senior staff to support expansion and product development\. *(Corroborated)* ^[42](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038),[43](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[33](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion)
  - Assumption: Press staff claims reflect recent hiring\.

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** Customer\-facing marketplace UI, voucher shop and dynamic pricing can be reproduced using Next\.js frontend, common payment providers and basic reservation APIs\. *(Analyst view)* ^[12](https://www.campiri.com/cs-cz),[27](https://crt.sh/?q=%25.campiri.com&output=json),[11](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/)
  - Assumption: No proprietary backend or ML required\.
- **Edge supported by public evidence:** Independent registry\+press verification shows Rockaway and Miton as active investors, supporting market credibility and capital access\. *(Analyst view)* ^[5](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[6](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
  - Assumption: Investor backing helps scaling and credibility\.
- **Cannot be judged from outside:** True unit economics, insured\-claim performance, fleet utilization and the sustainability of guaranteed investor returns cannot be judged externally without financials, contracts and operational telemetry\. *(Analyst view)* ^[39](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038),[13](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[3](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
  - Assumption: Internal metrics are needed for assessment\.

## Risks and caveats

- Product\-level contingent liabilities: public claims of 6–8% guaranteed returns to investors expose the company to payout risk if rental yields or resale values disappoint\. *(Analyst view)* ^[13](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[15](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
  - Assumption: Guarantees may be contractually binding\.
- Fleet financing concentration: a reported 32M CZK debt tranche earmarked for fleet purchase creates leverage tied to vehicle utilization and residual values\. *(Analyst view)* ^[14](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Debt service depends on operational cashflow\.
- Inconsistent fleet claims in public sources \(400 vs 600\+ listings and 25 owned vehicles\) require reconciliation before sizing TAM and revenue forecasts\. *(Analyst view)* ^[7](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/),[44](https://www.campiri.com/cs-cz),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Public numbers mix owned and marketplace inventory\.

## Questions for founders

- Please provide audited unit economics and fleet utilization metrics underpinning the 6–8% guaranteed investor return claim\. *(Analyst view)* ^[13](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[14](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Guarantee economics are material to valuation\.
- Clarify current effective fleet: reconcile 400–600\+ marketplace listings versus the stated owned fleet of 25 and show revenue per vehicle\. *(Analyst view)* ^[7](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/),[44](https://www.campiri.com/cs-cz),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Accurate fleet sizing materially affects growth plan\.
- Share debt documentation and covenants for the 32M CZK financing and any other secured obligations affecting cash runway\. *(Analyst view)* ^[14](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Debt terms could constrain strategy\.
- Provide customer/channel validation: named signed contracts, top customers, and verification of claimed investor support from Rockaway/Miton reflected in registry\. *(Analyst view)* ^[5](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[6](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
  - Assumption: Public investor confirmation supports credibility\.

## Sources

1. [borovan\.cz](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri) · Independent press · Product capability — “Start\-up Campiri , který digitalizuje pronájem obytných vozů a který nabízí paletu obytných vozů a karavanů z půjčoven i od soukromých majitelů, získal nové silné investory\.”
2. [itkey\.media](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion) · Independent press · Product capability — “Our main focus is positioning the platform as ‘caravanning from people to people’\.”
3. [startupinsider\.cz](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038) · Independent press · Product capability — “Postará se o parkování, údržbu, mytí, předávání a přebírání od zákazníků, aby to pro investory bylo zcela bez starostí”
4. [shorttermrentalz\.com](https://shorttermrentalz.com/news/campiri-funding-expansion/) · Independent press · Funding round — “To date, Campiri has raised €4\.64 million which will be used to establish the company in new markets\.”
5. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Independent check of a claim · 2023\-11\-09 — “Press \(borovan\.cz, cc\.cz, itkey\.media, shorttermrentalz\.com\) names Rockaway Capital as an investor; the commercial register lists Rockaway Ventures Fund SCSp as a shareholder from 2023\-11\-09 \(11\.16%\)\.”
6. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Independent check of a claim · 2022\-05\-04 — “Press \(borovan\.cz, cc\.cz, itkey\.media, miton\.cz, shorttermrentalz\.com\) names Miton as an investor; the commercial register lists MITON Happy Campers s\.r\.o\. as a shareholder from 2022\-05\-04 \(17\.04%\)\.”
7. [techfundingnews\.com](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/) · Independent press · Product capability — “After just a single season of operation, the Campiri platform already boasts the largest fleet of RVs for rent in Czechia which is comprised of a broad selection of 400 vehicles in total\.”
8. [cc\.cz](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/) · Independent press · Product capability — “vlastní flotila, jež dnes čítá 25 vozů”
9. [campiri\.com](https://www.campiri.com/cs-cz) · Company's own website · Product capability — “Garance vrácení peněz”
10. [campiri\.com](https://www.campiri.com/cs-cz) · Company's own website · Product capability — “Záruka ochrany rezervace”
11. [cc\.cz](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/) · Independent press · Product capability — “Díky zkušenostem, které má tým v oblasti marketingu, fintechu a především budování rezervačních systémů, bude digitální řešení venku již v březnu\. Zahrnovat má přehled dostupných vozů, dynamicky nastavené ceníky a možnost doplňkových služeb k pronájmu, jako je půjčení kola či pojištění\.”
12. [campiri\.com](https://www.campiri.com/cs-cz) · Public technical artifact · Technology detected
13. [euro\.cz](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/) · Independent press · Pricing — “garantovaný výnos šest až osm procent za rok”
14. [cc\.cz](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/) · Independent press · Funding round — “32 milionů získal ve formě dluhového financování na nákup flotily vozů\.”
15. [euro\.cz](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/) · Independent press · Product capability — “Campiri Campers Clubu, jenž zahrnuje dva rozdílné investiční programy”
16. [miton\.cz](https://www.miton.cz/en/blog/campiri-is-set-to-digitalise-recreational-vehicle-rental-and-were-in-for-the-ride/) · Independent press · Funding round — “Jahn invested in Campiri in mid\-January together with the investment group Miton\.”
17. [cc\.cz](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/) · Independent press · Funding round — “Na vývoj platformy má v tuto chvíli 14 milionů korun, přičemž kromě Janouška projekt zafinancovala také investiční skupina Miton, podnikatel Paul Tesar a angel investor Petr Jahn\.”
18. [cc\.cz](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/) · Independent press · Funding round — “67 milionů korun je ve formě investičního kola”
19. [shorttermrentalz\.com](https://shorttermrentalz.com/news/campiri-funding-expansion/) · Independent press · Funding round — “The recent funding, led by Rockaway Ventures Fund, injected €2\.7 million into the startup\. Miton and Purple Ventures also participated in the round\.”
20. [borovan\.cz](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri) · Independent press · Funding round — “Novým spolumajitelem Campiri se stala investiční skupina Rockaway Capital , ve které největší podíl drží Jakub Havrlant \. Rockaway má ve start\-upu nyní 10,6 procenta\. Dalšími investory se staly Purple Holding \(5,4 procenta\) a multimilionář Oldřich Bajer \(2,1 procenta; ex\- Zoot , ex\- Centrum Holdings \)\. Dohromady měli v…”
21. [itkey\.media](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion) · Independent press · Funding round — “The recent funding was led by Rockaway Ventures Fund , with the participation of Miton and Purple Ventures”
22. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2022\-05\-04 — “Rockaway Ventures Fund SCSp SICAV\-RAIF · 10\.43% · from 2022\-05\-04 · to 2023\-11\-09”
23. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2023\-11\-09 — “Rockaway Ventures Fund SCSp · 11\.16% · from 2023\-11\-09 · to 2024\-05\-14”
24. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2026\-07\-22 — “Breyer Invest UG · 16\.25% · from 2026\-07\-22 · to 2026\-09\-18”
25. [miton\.cz](https://www.miton.cz/en/blog/campiri-is-set-to-digitalise-recreational-vehicle-rental-and-were-in-for-the-ride/) · Independent press · Press article · 2021\-01 — “Campiri is set to digitalise recreational vehicle rental, and we’re in for the ride · Blog · Miton”
26. [miton\.cz](https://www.miton.cz/blog/campiri-zdigitalizuje-pronajem-obytnych-vozu-a-my-ho-v-tom-podporime/) · Independent press · Press article — “Campiri zdigitalizuje pronájem obytných vozů a my ho v tom podpoříme · Blog · Miton”
27. [crt\.sh](https://crt.sh/?q=%25.campiri.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2022\-10\-04 — “docs\.campiri\.com \(first certificate 2022\-10\-04\)”
28. [crt\.sh](https://crt.sh/?q=%25.campiri.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-08\-03 — “api\.staging\.campiri\.com \(first certificate 2023\-08\-03\)”
29. [shop\.campiri\.com](https://shop.campiri.com/) · Company's own website · Pricing — “Běžná cena Od 3,000 Kč”
30. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09283447) · Official record · Registry: incorporation · 2020\-06\-26 — “registered 2020\-06\-26”
31. [shorttermrentalz\.com](https://shorttermrentalz.com/news/campiri-funding-expansion/) · Independent press · Technical claim — “What attracted us to Campiri was the digital business model that connects motorhome owners with those interested in renting them\.”
32. [podmaz\.sk](https://podmaz.sk/podcast/jiri-rostecky/4242929872-100-milionu-za-3-roky--jak-roste-campiri-lukas-janousek) · Independent press · Product capability — “Campiri je půjčovna karavanů a obytných vozů\.”
33. [itkey\.media](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion) · Independent press · Team claim — “Hence, most of the received funding is expanding into other European markets\. Campiri is also looking to expand the teams with new talents to support the growth, product development, and improvement with new features and tools\.”
34. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2024\-05\-14 — “FWC \- FreewayCamper GmbH · 100\.0% · from 2024\-05\-14 · to 2025\-12\-16”
35. [cc\.cz](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/) · Independent press · Product capability — “startup začátkem letoška už vstoupil do Polska, Řecka a na Slovensko”
36. [borovan\.cz](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri) · Independent press · Product capability — “Aktuálně umožňuje pronájem více než 400 vozů od přímých majitelů, ale i karavanových půjčoven\.”
37. [euro\.cz](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/) · Independent press · Product capability — “První je čistě pasivní půjčka zajištěná obytným vozem s atraktivním pevným výnosem z úroku, druhá je chytrý nákup obytného vozu \.”
38. [shop\.campiri\.com](https://shop.campiri.com/) · Company's own website · Product capability — “Dárkový voucher na pronájem karavanu 3 000 Kč”
39. [startupinsider\.cz](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038) · Independent press · Technical claim — “Platforma Campiri dosáhla první rok od svého spuštění obratu 20 milionů korun”
40. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2022\-05\-04 — “MITON Happy Campers s\.r\.o\. · 17\.04% · from 2022\-05\-04 · to 2024\-05\-14”
41. [campiri\.com](https://www.campiri.com/cs-cz) · Company's own website · Product capability — “Pojištění storna a poškození”
42. [startupinsider\.cz](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038) · Independent press · Team claim — “rozšířila se z původních šesti zaměstnanců na současných čtyřicet”
43. [euro\.cz](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/) · Independent press · Team claim — “Ambice startupu, který za rok vyrostl z šesti členů na tým čtyřiceti lidí”
44. [campiri\.com](https://www.campiri.com/cs-cz) · Company's own website · Product capability — “Vybírejte ze 600\+ ověřených obytných vozů s garancemi Campiri\.”
45. [startupinsider\.cz](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038) · Independent press · Funding round — “Investor startupu poskytne finance ve výši jednoho až dvou milionů korun na nákup nového obytného vozu s garantovaným ročním výnosem 6–8 %\.”
46. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09283447) · Official record · Registry: identity · 2020\-06\-26 — “Campiri s\.r\.o\. · s\.r\.o\. · registered 2020\-06\-26”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 45 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 13 | press:etsy\.com, press:komoraplus\.cz, press:lilysgardenstore\.com, press:phocuswire\.com |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 2 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 43 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 1 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 2 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 2 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 46 | — |

Analysis: gpt\-5\-mini (cost $0.0190); AI extraction cost $0.0095. Full fact table: CSV export.

## Source appendix (all collected facts)

- F3282 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09283447)
- F3283 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09283447)
- F3284 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3285 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3286 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3287 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3288 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3289 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3290 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3291 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3292 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3293 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3294 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3295 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3296 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3297 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3298 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3299 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3300 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3301 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3302 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3303 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3304 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3305 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3306 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3307 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F3308 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3309 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3310 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3311 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3312 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3313 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3314 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3315 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3316 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3317 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3318 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3319 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3320 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3321 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3322 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3323 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3324 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3325 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1089068](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1089068)
- F3326 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=09283447&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=09283447&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F3327 · web\_page · Sourced · [https://www\.campiri\.com/cs\-cz](https://www.campiri.com/cs-cz)
- F3328 · web\_page · Sourced · [https://shop\.campiri\.com/](https://shop.campiri.com/)
- F3329 · tech\_stack · Medium confidence · [https://www\.campiri\.com/cs\-cz](https://www.campiri.com/cs-cz)
- F3330 · tech\_stack · Medium confidence · [https://www\.campiri\.com/cs\-cz](https://www.campiri.com/cs-cz)
- F3331 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=campiri\.com&amp;type=MX](https://dns.google/resolve?name=campiri.com&type=MX)
- F3332 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=campiri\.com&amp;type=TXT](https://dns.google/resolve?name=campiri.com&type=TXT)
- F3333 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=campiri\.com&amp;type=TXT](https://dns.google/resolve?name=campiri.com&type=TXT)
- F3334 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=campiri\.com&amp;type=TXT](https://dns.google/resolve?name=campiri.com&type=TXT)
- F3335 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3336 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3337 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3338 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3339 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3340 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3341 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3342 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3343 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3344 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3345 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3346 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3347 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3348 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3349 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3350 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3351 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3352 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3353 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3354 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3355 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3356 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3357 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3358 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3359 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3360 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3361 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3362 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3363 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3364 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3365 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3366 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3367 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3368 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3369 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3370 · subdomain · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3371 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.campiri\.com&amp;output=json](https://crt.sh/?q=%25.campiri.com&output=json)
- F3372 · github\_org · Sourced · [https://github\.com/campiri](https://github.com/campiri)
- F3373 · wayback\_first · Sourced · [https://web\.archive\.org/web/20041126181907/http://www\.campiri\.com:80/](https://web.archive.org/web/20041126181907/http://www.campiri.com:80/)
- F3374 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/campiri\.com](https://web.archive.org/web/%2A/campiri.com)
- F3379 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3380 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3381 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3382 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3383 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3384 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3385 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3386 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3387 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3388 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3389 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3390 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3391 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3392 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3393 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3394 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3395 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3396 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3397 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3398 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3399 · press\_mention · Sourced · [https://cc\.cz/2021/02/svobodne\-cestovani\-v\-obytnaku\-lukas\-janousek\-spolu\-s\-mitonem\-spousti\-sluzbu\-pro\-sdileni\-karavanu/](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/)
- F3400 · press\_mention · Sourced · [https://cc\.cz/ceske\-campiri\-ve\-velkem\-rozjizdi\-pronajem\-karavanu\-po\-evrope\-115\-milionu\-mu\-posila\-rockaway\-i\-miton/](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
- F3401 · press\_mention · Sourced · [https://www\.miton\.cz/en/blog/campiri\-is\-set\-to\-digitalise\-recreational\-vehicle\-rental\-and\-were\-in\-for\-the\-ride/](https://www.miton.cz/en/blog/campiri-is-set-to-digitalise-recreational-vehicle-rental-and-were-in-for-the-ride/)
- F3402 · source\_unavailable · Unavailable · [https://www\.phocuswire\.com/czech\-camper\-van\-rental\-marketplace\-adds\-3m\-to\-seed\-round](https://www.phocuswire.com/czech-camper-van-rental-marketplace-adds-3m-to-seed-round)
- F3403 · press\_mention · Sourced · [https://www\.startupinsider\.cz/transport/pronajem\-karavanu\-campiri\-spousti\-investicni\-programy\-souvisejici\-s\-nakupem\-obytnych\-vozu\-529038](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- F3404 · press\_mention · Sourced · [https://www\.borovan\.cz/57193/skupina\-rockaway\-capital\-investuje\-do\-start\-upu\-campiri](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri)
- F3405 · press\_mention · Sourced · [https://rockawayventures\.com/rockaway\-ventures\-bets\-on\-czech\-startup\-campiri/](https://rockawayventures.com/rockaway-ventures-bets-on-czech-startup-campiri/)
- F3406 · press\_mention · Sourced · [https://www\.miton\.cz/blog/campiri\-zdigitalizuje\-pronajem\-obytnych\-vozu\-a\-my\-ho\-v\-tom\-podporime/](https://www.miton.cz/blog/campiri-zdigitalizuje-pronajem-obytnych-vozu-a-my-ho-v-tom-podporime/)
- F3407 · press\_mention · Sourced · [https://www\.euro\.cz/clanky/platforma\-campiri\-otevira\-investice\-do\-obytnych\-vozu\-v\-oblasti\-karavaningu\-chce\-pokryt\-tretinu\-ceskeho\-trhu/](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
- F3408 · press\_mention · Sourced · [https://podmaz\.sk/podcast/jiri\-rostecky/4242929872\-100\-milionu\-za\-3\-roky\-\-jak\-roste\-campiri\-lukas\-janousek](https://podmaz.sk/podcast/jiri-rostecky/4242929872-100-milionu-za-3-roky--jak-roste-campiri-lukas-janousek)
- F3409 · press\_mention · Sourced · [https://techfundingnews\.com/prague\-based\-campiri\-the\-airbnb\-for\-campers\-scores\-e4\-64m\-fueling\-expansion/](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/)
- F3410 · press\_mention · Sourced · [https://itkey\.media/motorhome\-rental\-company\-campiri\-raises\-e4\-64\-million\-for\-further\-expansion](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion)
- F3411 · press\_mention · Sourced · [https://shorttermrentalz\.com/news/campiri\-funding\-expansion/](https://shorttermrentalz.com/news/campiri-funding-expansion/)
- F3412 · press\_mention · Sourced · [https://www\.dlahandlu\.pl/e\-commerce/udzialowiec\-twisto\-wierzy\-w\-campiri\-platforma\-pozyskala\-2\-7\-mln\-euro\-od\-inwestorow,108271\.html](https://www.dlahandlu.pl/e-commerce/udzialowiec-twisto-wierzy-w-campiri-platforma-pozyskala-2-7-mln-euro-od-inwestorow%2C108271.html)
- F3413 · source\_unavailable · Unavailable · [https://www\.etsy\.com/market/campari\_tomato\_seed](https://www.etsy.com/market/campari_tomato_seed)
- F3414 · source\_unavailable · Unavailable · [https://lilysgardenstore\.com/products/tomato\-campari\-20\-seeds](https://lilysgardenstore.com/products/tomato-campari-20-seeds)
- F3415 · source\_unavailable · Unavailable · [https://komoraplus\.cz/2022/05/13/campiri\-se\-chce\-stat\-evropskym\-lidrem/](https://komoraplus.cz/2022/05/13/campiri-se-chce-stat-evropskym-lidrem/)
- F5895 · product\_capability · Medium confidence · [https://shop\.campiri\.com/](https://shop.campiri.com/)
- F5896 · pricing · Medium confidence · [https://shop\.campiri\.com/](https://shop.campiri.com/)
- F5897 · pricing · Medium confidence · [https://shop\.campiri\.com/](https://shop.campiri.com/)
- F5898 · pricing · Medium confidence · [https://shop\.campiri\.com/](https://shop.campiri.com/)
- F5899 · pricing · Medium confidence · [https://shop\.campiri\.com/](https://shop.campiri.com/)
- F5900 · product\_capability · Medium confidence · [https://www\.campiri\.com/cs\-cz](https://www.campiri.com/cs-cz)
- F5901 · pricing · Medium confidence · [https://www\.campiri\.com/cs\-cz](https://www.campiri.com/cs-cz)
- F5902 · product\_capability · Medium confidence · [https://www\.campiri\.com/cs\-cz](https://www.campiri.com/cs-cz)
- F5903 · product\_capability · Medium confidence · [https://www\.campiri\.com/cs\-cz](https://www.campiri.com/cs-cz)
- F5904 · product\_capability · Medium confidence · [https://www\.campiri\.com/cs\-cz](https://www.campiri.com/cs-cz)
- F5905 · funding\_round · Medium confidence · [https://cc\.cz/ceske\-campiri\-ve\-velkem\-rozjizdi\-pronajem\-karavanu\-po\-evrope\-115\-milionu\-mu\-posila\-rockaway\-i\-miton/](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
- F5906 · funding\_round · Medium confidence · [https://cc\.cz/ceske\-campiri\-ve\-velkem\-rozjizdi\-pronajem\-karavanu\-po\-evrope\-115\-milionu\-mu\-posila\-rockaway\-i\-miton/](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
- F5907 · product\_capability · Medium confidence · [https://cc\.cz/ceske\-campiri\-ve\-velkem\-rozjizdi\-pronajem\-karavanu\-po\-evrope\-115\-milionu\-mu\-posila\-rockaway\-i\-miton/](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
- F5908 · product\_capability · Medium confidence · [https://cc\.cz/ceske\-campiri\-ve\-velkem\-rozjizdi\-pronajem\-karavanu\-po\-evrope\-115\-milionu\-mu\-posila\-rockaway\-i\-miton/](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
- F5909 · funding\_round · Medium confidence · [https://www\.startupinsider\.cz/transport/pronajem\-karavanu\-campiri\-spousti\-investicni\-programy\-souvisejici\-s\-nakupem\-obytnych\-vozu\-529038](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- F5910 · funding\_round · Medium confidence · [https://www\.startupinsider\.cz/transport/pronajem\-karavanu\-campiri\-spousti\-investicni\-programy\-souvisejici\-s\-nakupem\-obytnych\-vozu\-529038](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- F5911 · team\_claim · Medium confidence · [https://www\.startupinsider\.cz/transport/pronajem\-karavanu\-campiri\-spousti\-investicni\-programy\-souvisejici\-s\-nakupem\-obytnych\-vozu\-529038](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- F5912 · product\_capability · Medium confidence · [https://www\.startupinsider\.cz/transport/pronajem\-karavanu\-campiri\-spousti\-investicni\-programy\-souvisejici\-s\-nakupem\-obytnych\-vozu\-529038](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- F5913 · product\_capability · Medium confidence · [https://www\.startupinsider\.cz/transport/pronajem\-karavanu\-campiri\-spousti\-investicni\-programy\-souvisejici\-s\-nakupem\-obytnych\-vozu\-529038](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- F5914 · product\_capability · Medium confidence · [https://www\.startupinsider\.cz/transport/pronajem\-karavanu\-campiri\-spousti\-investicni\-programy\-souvisejici\-s\-nakupem\-obytnych\-vozu\-529038](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- F5915 · tech\_claim · Medium confidence · [https://www\.startupinsider\.cz/transport/pronajem\-karavanu\-campiri\-spousti\-investicni\-programy\-souvisejici\-s\-nakupem\-obytnych\-vozu\-529038](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
- F5916 · funding\_round · Medium confidence · [https://www\.borovan\.cz/57193/skupina\-rockaway\-capital\-investuje\-do\-start\-upu\-campiri](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri)
- F5917 · product\_capability · Medium confidence · [https://www\.borovan\.cz/57193/skupina\-rockaway\-capital\-investuje\-do\-start\-upu\-campiri](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri)
- F5918 · product\_capability · Medium confidence · [https://www\.borovan\.cz/57193/skupina\-rockaway\-capital\-investuje\-do\-start\-upu\-campiri](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri)
- F5919 · team\_claim · Medium confidence · [https://www\.borovan\.cz/57193/skupina\-rockaway\-capital\-investuje\-do\-start\-upu\-campiri](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri)
- F5920 · product\_capability · Medium confidence · [https://www\.euro\.cz/clanky/platforma\-campiri\-otevira\-investice\-do\-obytnych\-vozu\-v\-oblasti\-karavaningu\-chce\-pokryt\-tretinu\-ceskeho\-trhu/](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
- F5921 · pricing · Medium confidence · [https://www\.euro\.cz/clanky/platforma\-campiri\-otevira\-investice\-do\-obytnych\-vozu\-v\-oblasti\-karavaningu\-chce\-pokryt\-tretinu\-ceskeho\-trhu/](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
- F5922 · team\_claim · Medium confidence · [https://www\.euro\.cz/clanky/platforma\-campiri\-otevira\-investice\-do\-obytnych\-vozu\-v\-oblasti\-karavaningu\-chce\-pokryt\-tretinu\-ceskeho\-trhu/](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
- F5923 · product\_capability · Medium confidence · [https://www\.euro\.cz/clanky/platforma\-campiri\-otevira\-investice\-do\-obytnych\-vozu\-v\-oblasti\-karavaningu\-chce\-pokryt\-tretinu\-ceskeho\-trhu/](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
- F5924 · product\_capability · Medium confidence · [https://podmaz\.sk/podcast/jiri\-rostecky/4242929872\-100\-milionu\-za\-3\-roky\-\-jak\-roste\-campiri\-lukas\-janousek](https://podmaz.sk/podcast/jiri-rostecky/4242929872-100-milionu-za-3-roky--jak-roste-campiri-lukas-janousek)
- F5925 · funding\_round · Medium confidence · [https://techfundingnews\.com/prague\-based\-campiri\-the\-airbnb\-for\-campers\-scores\-e4\-64m\-fueling\-expansion/](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/)
- F5926 · product\_capability · Medium confidence · [https://techfundingnews\.com/prague\-based\-campiri\-the\-airbnb\-for\-campers\-scores\-e4\-64m\-fueling\-expansion/](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/)
- F5928 · team\_claim · Medium confidence · [https://techfundingnews\.com/prague\-based\-campiri\-the\-airbnb\-for\-campers\-scores\-e4\-64m\-fueling\-expansion/](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/)
- F5931 · funding\_round · Medium confidence · [https://itkey\.media/motorhome\-rental\-company\-campiri\-raises\-e4\-64\-million\-for\-further\-expansion](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion)
- F5932 · product\_capability · Medium confidence · [https://itkey\.media/motorhome\-rental\-company\-campiri\-raises\-e4\-64\-million\-for\-further\-expansion](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion)
- F5935 · team\_claim · Medium confidence · [https://itkey\.media/motorhome\-rental\-company\-campiri\-raises\-e4\-64\-million\-for\-further\-expansion](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion)
- F5937 · funding\_round · Medium confidence · [https://shorttermrentalz\.com/news/campiri\-funding\-expansion/](https://shorttermrentalz.com/news/campiri-funding-expansion/)
- F5938 · funding\_round · Medium confidence · [https://shorttermrentalz\.com/news/campiri\-funding\-expansion/](https://shorttermrentalz.com/news/campiri-funding-expansion/)
- F5939 · tech\_claim · Medium confidence · [https://shorttermrentalz\.com/news/campiri\-funding\-expansion/](https://shorttermrentalz.com/news/campiri-funding-expansion/)
- F5940 · team\_claim · Medium confidence · [https://shorttermrentalz\.com/news/campiri\-funding\-expansion/](https://shorttermrentalz.com/news/campiri-funding-expansion/)
- F5941 · funding\_round · Medium confidence · [https://cc\.cz/2021/02/svobodne\-cestovani\-v\-obytnaku\-lukas\-janousek\-spolu\-s\-mitonem\-spousti\-sluzbu\-pro\-sdileni\-karavanu/](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/)
- F5942 · product\_capability · Medium confidence · [https://cc\.cz/2021/02/svobodne\-cestovani\-v\-obytnaku\-lukas\-janousek\-spolu\-s\-mitonem\-spousti\-sluzbu\-pro\-sdileni\-karavanu/](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/)
- F5943 · product\_capability · Medium confidence · [https://cc\.cz/2021/02/svobodne\-cestovani\-v\-obytnaku\-lukas\-janousek\-spolu\-s\-mitonem\-spousti\-sluzbu\-pro\-sdileni\-karavanu/](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/)
- F5944 · product\_capability · Medium confidence · [https://cc\.cz/2021/02/svobodne\-cestovani\-v\-obytnaku\-lukas\-janousek\-spolu\-s\-mitonem\-spousti\-sluzbu\-pro\-sdileni\-karavanu/](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/)
- F5945 · funding\_round · Medium confidence · [https://www\.miton\.cz/en/blog/campiri\-is\-set\-to\-digitalise\-recreational\-vehicle\-rental\-and\-were\-in\-for\-the\-ride/](https://www.miton.cz/en/blog/campiri-is-set-to-digitalise-recreational-vehicle-rental-and-were-in-for-the-ride/)
- F5946 · product\_capability · Medium confidence · [https://www\.miton\.cz/en/blog/campiri\-is\-set\-to\-digitalise\-recreational\-vehicle\-rental\-and\-were\-in\-for\-the\-ride/](https://www.miton.cz/en/blog/campiri-is-set-to-digitalise-recreational-vehicle-rental-and-were-in-for-the-ride/)
- F6384 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F6385 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09283447](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
- F7693 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/hledat?Q=ico%3A09283447](https://www.hlidacstatu.cz/hledat?Q=ico%3A09283447)
- F7694 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/dotace/hledat?Q=ico%3A09283447](https://www.hlidacstatu.cz/dotace/hledat?Q=ico%3A09283447)
- F7695 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Campiri%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Campiri%27)
- F7696 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
