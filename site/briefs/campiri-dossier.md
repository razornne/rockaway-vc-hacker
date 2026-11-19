# Campiri — due diligence brief

campiri\.com · Campiri s\.r\.o\. · IČO 09283447 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A digital RV/caravan rental marketplace and fleet operator serving renters and private owners via a booking platform and investor programs\. *(Partly verified)* ^[1](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri),[2](https://www.campiri.com/cs-cz),[3](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
- **Stage & traction.** Multiple funding rounds totalling \~€4\.64m / 100\+M CZK with confirmed strategic investors \(Miton, Rockaway\); claims of 400–600 listed vehicles and a 25‑vehicle owned fleet\. *(Verified)* ^[4](https://shorttermrentalz.com/news/campiri-funding-expansion/),[5](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[6](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[7](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
- **Technology & moat.** No public ML or research IP; apparent moat is marketplace supply \(fleet \+ owner networks\) and investor\-backed capital for fleet growth, not proprietary engineering\. *(Verified)* ^[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[9](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri),[10](https://github.com/campiri)
- **Key risk.** Capital intensity and product promises \(6–8% guaranteed returns, debt for fleet\) expose unit economics to fleet utilization and financing costs\. *(Analyst view)* ^[11](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[12](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
- **Diligence focus.** Verify contract terms and mechanics of investor guarantees and the fleet P&amp;L \(utilization, maintenance, insurance, breakage rates\)\. *(Analyst view)* ^[11](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[13](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2021\-01 · 14 milionů Kč · Petr Jahn, Miton, Paul Tesar · 2 reports; 2022\-05\-11 · equity · 67 million CZK · Rockaway Capital, Miton, Eva Janečková, Olda Bajer, Purple Ventures, Oldřich Bajer, Petr J · 4 reports; 2022\-05\-11 · debt · 32 million CZK; 2022\-05\-12 · €4\.64 million; date n/a · 1–2 mil\. Kč | 14, 15, 5, 16, 17, 18 |
| Investors in registry | Rockaway Ventures Fund SCSp SICAV\-RAIF \(from 2022\-05\-04, 10\.43%\); Rockaway Ventures Fund SCSp \(from 2023\-11\-09, 11\.16%\); Breyer Invest UG \(from 2026\-07\-22, 16\.25%\) | 19, 20, 21 |
| Engineering footprint | product surfaces: api\.staging\.campiri\.com, docs\.campiri\.com; stack: Next\.js | 22, 23 |
| Customers | public pricing: yes | 24 |
| Claims checked | Investors vs registry \(MITON Happy Campers s\.r\.o\., Rockaway Ventures Fund SCSp\): confirmed | 6, 7 |
| Timeline | Czech entity registered 2020\-06\-26; first press 2021\-01 \(13 articles collected\) | 25, 26 |

# Detailed findings

## Ownership and capital

- Equity and debt raises reported: initial 14M CZK \(Miton, Paul Tesar, Petr Jahn\), later equity c\.67M CZK and debt 32M CZK; press reports total \~€4\.64M \(\~100M\+ CZK\) across rounds\. *(Verified)* ^[15](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/),[5](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[12](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[4](https://shorttermrentalz.com/news/campiri-funding-expansion/),[17](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri)
  - Assumption: Press\-reported sums represent combined closings and tranches\.
- Registry confirms strategic shareholders: MITON Happy Campers and Rockaway Ventures listed as shareholders in filings\. *(Verified)* ^[27](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[20](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[6](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[7](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
  - Assumption: Registry entries reflect recorded shareholder stakes\.
- Recent registry shareholder changes show multiple transfers and foreign corporate owners in filings \(Rockaway, FWC \- FreewayCamper GmbH, Breyer Invest UG entries\)\. *(Verified)* ^[28](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[21](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[20](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447),[29](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447)
  - Assumption: Registry filing dates indicate ownership events\.

## Technology profile

- Customer product capabilities: marketplace listing \(400–600 vehicles\), booking, vouchers, dynamic pricing, optional add‑ons, reservation protections and insurance\. *(Partly verified)* ^[9](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri),[2](https://www.campiri.com/cs-cz),[30](https://shop.campiri.com/),[31](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/),[32](https://www.campiri.com/cs-cz)
  - Assumption: All listed capabilities are customer\-facing product claims\.
- Engineering footprint: public GitHub org shows 0 public repos; product exposes subdomains including docs\.campiri\.com and api\.staging\.campiri\.com; site uses Next\.js markers\. *(Verified)* ^[10](https://github.com/campiri),[22](https://crt.sh/?q=%25.campiri.com&output=json),[23](https://crt.sh/?q=%25.campiri.com&output=json),[33](https://www.campiri.com/cs-cz)
  - Assumption: Absence of public repos indicates limited public OSS exposure\.
- AI dependency/evidence: no verified use of external LLM vendors, no own\-model papers or ML hires in supplied facts; technical claims are web/product features\. *(Verified)* ^[10](https://github.com/campiri),[34](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/),[35](https://shorttermrentalz.com/news/campiri-funding-expansion/)
  - Assumption: Lack of ML facts implies low documented AI dependency\.

## Rebuild check

- **Commodity:** Core booking site, vouchers, search and dynamic pricing can be rebuilt by a small team using common booking APIs and e‑commerce plugins\. *(Analyst view)* ^[30](https://shop.campiri.com/),[31](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/),[23](https://crt.sh/?q=%25.campiri.com&output=json)
  - Assumption: Standard booking/payment APIs are available to a rebuild team\.
- **Hard to copy:** Fleet ownership, investor programs with guaranteed returns, and full\-service vehicle operations are capital and operations intensive and harder to clone quickly\. *(Analyst view)* ^[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[3](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[11](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[12](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/)
  - Assumption: Guaranteed returns require committed capital and legal terms\.
- **Verdict:** Month — a functioning booking clone is feasible within weeks, but a credible competitor lacking fleet, investor programs and existing owner supply would miss core distribution and financial guarantees\. *(Analyst view)* ^[30](https://shop.campiri.com/),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[11](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/)
  - Assumption: Supply and guaranteed returns are primary differentiation\.

## Risks and caveats

- Guaranteed investor returns \(6–8%\) versus fleet utilization: risk to cashflow if utilization or maintenance costs deviate from projections\. *(Analyst view)* ^[11](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[13](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
  - Assumption: Guarantees are contractual and affect cash outflows\.
- Capital intensity and leverage: a reported 32M CZK debt tranche for fleet purchase increases sensitivity to financing costs and seasonality\. *(Analyst view)* ^[12](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[17](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri),[4](https://shorttermrentalz.com/news/campiri-funding-expansion/)
  - Assumption: Debt funds are used for fleet capex and operations\.
- Limited public engineering trace: GitHub org shows 0 public repos and limited documented dev resources, raising verification needs for platform maturity\. *(Analyst view)* ^[10](https://github.com/campiri),[22](https://crt.sh/?q=%25.campiri.com&output=json),[23](https://crt.sh/?q=%25.campiri.com&output=json)
  - Assumption: Public repos correlate with observable engineering output\.

## Questions for founders

- Provide investor contract templates for the 6–8% guaranteed return program and explain indemnities and recourse \(we saw the guaranteed return claim\)\. *(Analyst view)* ^[11](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/),[13](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
  - Assumption: Contracts exist that implement advertised guarantees\.
- Deliver verified supply figures and reconciliation: please reconcile 400 vs 600\+ vehicle claims and list owned vs third‑party vehicles by country\. *(Analyst view)* ^[9](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri),[2](https://www.campiri.com/cs-cz),[36](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/)
  - Assumption: Discrepancy affects gross booking volume estimates\.
- Share fleet unit economics \(utilization, ARPU per vehicle, maintenance, insurance, CAC payback\) underpinning profitability claims such as 20M CZK first‑year turnover\. *(Analyst view)* ^[37](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038),[8](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/),[13](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038)
  - Assumption: Turnover and fleet figures link to unit economics\.
- Provide API/docs access and architecture overview \(api\.staging and docs subdomains detected\) and list production integrations used for payments, insurance and dynamic pricing\. *(Analyst view)* ^[23](https://crt.sh/?q=%25.campiri.com&output=json),[22](https://crt.sh/?q=%25.campiri.com&output=json),[33](https://www.campiri.com/cs-cz)
  - Assumption: Subdomains imply API/docs surfaces exist for review\.

## Sources

1. [borovan\.cz](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri) · Independent press · Product capability — “Start\-up Campiri , který digitalizuje pronájem obytných vozů a který nabízí paletu obytných vozů a karavanů z půjčoven i od soukromých majitelů, získal nové silné investory\.”
2. [campiri\.com](https://www.campiri.com/cs-cz) · Company's own website · Product capability — “Vybírejte ze 600\+ ověřených obytných vozů s garancemi Campiri\.”
3. [euro\.cz](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/) · Independent press · Product capability — “Campiri Campers Clubu, jenž zahrnuje dva rozdílné investiční programy”
4. [shorttermrentalz\.com](https://shorttermrentalz.com/news/campiri-funding-expansion/) · Independent press · Funding round — “To date, Campiri has raised €4\.64 million which will be used to establish the company in new markets\.”
5. [cc\.cz](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/) · Independent press · Funding round — “67 milionů korun je ve formě investičního kola”
6. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Independent check of a claim · 2022\-05\-04 — “Press \(borovan\.cz, cc\.cz, itkey\.media, miton\.cz, shorttermrentalz\.com\) names Miton as an investor; the commercial register lists MITON Happy Campers s\.r\.o\. as a shareholder from 2022\-05\-04 \(17\.04%\)\.”
7. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Independent check of a claim · 2023\-11\-09 — “Press \(borovan\.cz, cc\.cz, itkey\.media, shorttermrentalz\.com\) names Rockaway Capital as an investor; the commercial register lists Rockaway Ventures Fund SCSp as a shareholder from 2023\-11\-09 \(11\.16%\)\.”
8. [cc\.cz](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/) · Independent press · Product capability — “vlastní flotila, jež dnes čítá 25 vozů”
9. [borovan\.cz](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri) · Independent press · Product capability — “Aktuálně umožňuje pronájem více než 400 vozů od přímých majitelů, ale i karavanových půjčoven\.”
10. [github\.com](https://github.com/campiri) · Public technical artifact · GitHub organisation · 2021\-04\-07 — “campiri · 0 public repos”
11. [euro\.cz](https://www.euro.cz/clanky/platforma-campiri-otevira-investice-do-obytnych-vozu-v-oblasti-karavaningu-chce-pokryt-tretinu-ceskeho-trhu/) · Independent press · Pricing — “garantovaný výnos šest až osm procent za rok”
12. [cc\.cz](https://cc.cz/ceske-campiri-ve-velkem-rozjizdi-pronajem-karavanu-po-evrope-115-milionu-mu-posila-rockaway-i-miton/) · Independent press · Funding round — “32 milionů získal ve formě dluhového financování na nákup flotily vozů\.”
13. [startupinsider\.cz](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038) · Independent press · Product capability — “Postará se o parkování, údržbu, mytí, předávání a přebírání od zákazníků, aby to pro investory bylo zcela bez starostí”
14. [miton\.cz](https://www.miton.cz/en/blog/campiri-is-set-to-digitalise-recreational-vehicle-rental-and-were-in-for-the-ride/) · Independent press · Funding round — “Jahn invested in Campiri in mid\-January together with the investment group Miton\.”
15. [cc\.cz](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/) · Independent press · Funding round — “Na vývoj platformy má v tuto chvíli 14 milionů korun, přičemž kromě Janouška projekt zafinancovala také investiční skupina Miton, podnikatel Paul Tesar a angel investor Petr Jahn\.”
16. [shorttermrentalz\.com](https://shorttermrentalz.com/news/campiri-funding-expansion/) · Independent press · Funding round — “The recent funding, led by Rockaway Ventures Fund, injected €2\.7 million into the startup\. Miton and Purple Ventures also participated in the round\.”
17. [borovan\.cz](https://www.borovan.cz/57193/skupina-rockaway-capital-investuje-do-start-upu-campiri) · Independent press · Funding round — “Novým spolumajitelem Campiri se stala investiční skupina Rockaway Capital , ve které největší podíl drží Jakub Havrlant \. Rockaway má ve start\-upu nyní 10,6 procenta\. Dalšími investory se staly Purple Holding \(5,4 procenta\) a multimilionář Oldřich Bajer \(2,1 procenta; ex\- Zoot , ex\- Centrum Holdings \)\. Dohromady měli v…”
18. [itkey\.media](https://itkey.media/motorhome-rental-company-campiri-raises-e4-64-million-for-further-expansion) · Independent press · Funding round — “The recent funding was led by Rockaway Ventures Fund , with the participation of Miton and Purple Ventures”
19. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2022\-05\-04 — “Rockaway Ventures Fund SCSp SICAV\-RAIF · 10\.43% · from 2022\-05\-04 · to 2023\-11\-09”
20. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2023\-11\-09 — “Rockaway Ventures Fund SCSp · 11\.16% · from 2023\-11\-09 · to 2024\-05\-14”
21. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2026\-07\-22 — “Breyer Invest UG · 16\.25% · from 2026\-07\-22 · to 2026\-09\-18”
22. [crt\.sh](https://crt.sh/?q=%25.campiri.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2022\-10\-04 — “docs\.campiri\.com \(first certificate 2022\-10\-04\)”
23. [crt\.sh](https://crt.sh/?q=%25.campiri.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-08\-03 — “api\.staging\.campiri\.com \(first certificate 2023\-08\-03\)”
24. [shop\.campiri\.com](https://shop.campiri.com/) · Company's own website · Pricing — “Běžná cena Od 3,000 Kč”
25. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09283447) · Official record · Registry: incorporation · 2020\-06\-26 — “registered 2020\-06\-26”
26. [miton\.cz](https://www.miton.cz/en/blog/campiri-is-set-to-digitalise-recreational-vehicle-rental-and-were-in-for-the-ride/) · Independent press · Press article · 2021\-01 — “Campiri is set to digitalise recreational vehicle rental, and we’re in for the ride · Blog · Miton”
27. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2022\-05\-04 — “MITON Happy Campers s\.r\.o\. · 17\.04% · from 2022\-05\-04 · to 2024\-05\-14”
28. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2024\-05\-14 — “FWC \- FreewayCamper GmbH · 100\.0% · from 2024\-05\-14 · to 2025\-12\-16”
29. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09283447) · Official record · Registry: shareholder · 2025\-12\-16 — “Nomiverse s\.r\.o\. · 83\.75% · from 2025\-12\-16”
30. [shop\.campiri\.com](https://shop.campiri.com/) · Company's own website · Product capability — “Dárkový voucher na pronájem karavanu 3 000 Kč”
31. [cc\.cz](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/) · Independent press · Product capability — “Díky zkušenostem, které má tým v oblasti marketingu, fintechu a především budování rezervačních systémů, bude digitální řešení venku již v březnu\. Zahrnovat má přehled dostupných vozů, dynamicky nastavené ceníky a možnost doplňkových služeb k pronájmu, jako je půjčení kola či pojištění\.”
32. [campiri\.com](https://www.campiri.com/cs-cz) · Company's own website · Product capability — “Garance vrácení peněz”
33. [campiri\.com](https://www.campiri.com/cs-cz) · Public technical artifact · Technology detected
34. [cc\.cz](https://cc.cz/2021/02/svobodne-cestovani-v-obytnaku-lukas-janousek-spolu-s-mitonem-spousti-sluzbu-pro-sdileni-karavanu/) · Independent press · Product capability — “Zákazník například u každého vozu uvidí ekologické skóre a podle toho si bude moci vybírat\.”
35. [shorttermrentalz\.com](https://shorttermrentalz.com/news/campiri-funding-expansion/) · Independent press · Technical claim — “What attracted us to Campiri was the digital business model that connects motorhome owners with those interested in renting them\.”
36. [techfundingnews\.com](https://techfundingnews.com/prague-based-campiri-the-airbnb-for-campers-scores-e4-64m-fueling-expansion/) · Independent press · Product capability — “After just a single season of operation, the Campiri platform already boasts the largest fleet of RVs for rent in Czechia which is comprised of a broad selection of 400 vehicles in total\.”
37. [startupinsider\.cz](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038) · Independent press · Technical claim — “Platforma Campiri dosáhla první rok od svého spuštění obratu 20 milionů korun”
38. [startupinsider\.cz](https://www.startupinsider.cz/transport/pronajem-karavanu-campiri-spousti-investicni-programy-souvisejici-s-nakupem-obytnych-vozu-529038) · Independent press · Funding round — “Investor startupu poskytne finance ve výši jednoho až dvou milionů korun na nákup nového obytného vozu s garantovaným ročním výnosem 6–8 %\.”

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

Analysis: gpt\-5\-mini (cost $0.0103); AI extraction cost $0.0095. Full fact table: CSV export.

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
- F5508 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/hledat?Q=ico%3A09283447](https://www.hlidacstatu.cz/hledat?Q=ico%3A09283447)
- F5509 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/dotace/hledat?Q=ico%3A09283447](https://www.hlidacstatu.cz/dotace/hledat?Q=ico%3A09283447)
- F5510 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Campiri%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Campiri%27)
- F5511 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
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
