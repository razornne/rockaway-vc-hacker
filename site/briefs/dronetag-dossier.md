# Dronetag — due diligence brief

dronetag\.com · Dronetag s\.r\.o\. · IČO 08198519 · CZ · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** Hardware \+ software Remote ID receivers, transmitters and visualization sold to public safety, pilots and integrators via shop and APIs\. *(Company claim)* ^[1](https://www.dronetag.com/products/rider),[2](https://shop.dronetag.com/),[3](https://www.dronetag.com/),[4](https://help.dronetag.com/),[5](https://www.dronetag.com/)
- **Stage & traction.** Closed convertible loan from Y Soft Ventures; multiple public\-sector purchase orders and R&amp;D grants, plus NATO DIANA accelerator participation\. *(Verified)* ^[6](https://cc.cz/cesky-startup-dronetag-zajistuje-bezpecne-letani-s-drony-od-brnenskeho-fondu-ziskava-15-milionu/),[7](https://smlouvy.gov.cz/smlouva/14335472),[8](https://smlouvy.gov.cz/smlouva/19531615),[9](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56),[10](https://web.archive.org/web/20250811133329id_/https://www.diana.nato.int/about-diana/2024-cohort-of-companies.html)
- **Technology & moat.** Public repos, mobile apps and a REST API are visible; hard\-to\-copy elements \(claimed large receiver network and protocol authorship\) are company statements with limited independent proof\. *(Partly verified)* ^[11](https://github.com/dronetag),[12](https://apps.apple.com/us/app/drone-scanner-gen-2/id6742736434?uo=4),[13](https://help.dronetag.com/developers/data-pull/getting-started-rest),[14](https://www.dronetag.com/),[15](https://www.dronetag.com/)
- **Key risk.** Material claims about scale, approvals and performance \(50k devices, FAA approval, 3,000\+ receivers\) are unverified in public records\. *(Analyst view)* ^[15](https://www.dronetag.com/),[16](https://startuply.vc/article/dronetag-s-faa-approved-hardware-serves-15-military-forces-and-40-countries-1gv9lf),[14](https://www.dronetag.com/)
- **Diligence focus.** Verify shipped units, named paying customers and contract margin profiles first, because revenue concentration and stated scale drive valuation\. *(Analyst view)* ^[15](https://www.dronetag.com/),[17](https://www.dronetag.com/),[18](https://shop.dronetag.com/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2022\-06\-27 · convertible loan · 15 milionů · Y Soft Ventures · 2 reports | 6, 19 |
| Public money | 14 contract\(s\) in the contract register; 8 grant project\(s\) awarded 22\.2M CZK, 4\.1M CZK paid so far · by kind: 7 purchase\(s\) by public buyers \(1\.4M CZK\); 5 R&amp;D project agreement\(s\), amounts are project budgets, not revenue; 2 device loan\(s\) \(372,979 CZK\) · counterparties: Správa informačních technologií města Plzně, TECHNISERV, spol\. s r\.o\.,, České vysoké učení technické v Praze, Česká republika \- Ministerstvo obrany | 7, 20, 8, 21, 22, 23 |
| Defence signals | 1 EU\-procurement award\(s\), 1 from defence buyers \(27\.4M CZK\): Ministerstvo obrany; NATO DIANA 2024 \(Secure Information Sharing\) | 24, 10 |
| Thesis fit \(Rockaway\) | sectors: defence / dual\-use \(6 facts, incl\. structured defence evidence\); deep tech \(7 facts\); energy \(5 facts\); industrial / manufacturing AI \(4 facts\) · geography: CZ \(core region\) | 16, 25, 26, 27, 28 |
| Hiring | 4 open roles: engineering 2, sales gtm 2 | 29, 30, 31, 32 |
| Engineering footprint | 13 public repos \(56★, last push 2026\-11\-16\); 37 subdomains; 5 docs pages; stack: Cloudflare, Webflow | 33, 34, 35, 36, 37 |
| Customers | public pricing: yes; 2 mobile app\(s\) | 38 |
| Timeline | Czech entity registered 2019\-06\-07; first press 2022\-01\-31 \(20 articles collected\) | 39, 40 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the market, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** Evidence supports defence / dual\-use and deep\-tech positioning \(tenders, NATO DIANA, press on military customers and Remote ID hardware\)\. *(Analyst view)* ^[24](https://ted.europa.eu/en/notice/-/detail/436033-2026),[10](https://web.archive.org/web/20250811133329id_/https://www.diana.nato.int/about-diana/2024-cohort-of-companies.html),[16](https://startuply.vc/article/dronetag-s-faa-approved-hardware-serves-15-military-forces-and-40-countries-1gv9lf),[25](http://www.unmannedairspace.info/uncategorized/dronetag-drone-detection-system-chosen-for-eudis-business-accelerator-funding/),[41](https://technologickainkubace.org/en/news/czech-startup-conquers-america-and-expands-further-makes-drone-tracking-devices/)
  - Assumption: Public defence tender and DIANA listing indicate meaningful defence relevance

## Business model

- Primary revenue: hardware device sales \(shop SKUs for RIDER, Scout, Mini, Beacon\) and one\-off device purchases by public buyers\. *(Partly verified)* ^[18](https://shop.dronetag.com/),[42](https://www.dronetag.com/products/scout),[43](https://shop.dronetag.com/),[44](https://shop.dronetag.com/),[45](https://smlouvy.gov.cz/smlouva/35562893)
  - Assumption: Shop prices reflect core product revenue
- Recurring revenue: monthly connectivity / subscription plans for devices \(published starting price €15/month\)\. *(Company claim)* ^[46](https://www.dronetag.com/products/mini-4g),[38](https://help.dronetag.com/)
  - Assumption: Subscription shown applies to deployed devices
- Public\-sector sales and paid contracts: multiple supplier roles and a won defence tender \(Ministerstvo obrany\) worth CZK 27,440,000\. *(Verified)* ^[24](https://ted.europa.eu/en/notice/-/detail/436033-2026),[7](https://smlouvy.gov.cz/smlouva/14335472),[21](https://smlouvy.gov.cz/smlouva/21293531),[47](https://smlouvy.gov.cz/smlouva/39280395)
  - Assumption: Listed gov contracts reflect real sales to public buyers
- Non\-revenue public support: multiple awarded grants and R&amp;D project contracts \(awarded and paid amounts listed separately\)\. *(Verified)* ^[9](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56),[48](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-BD75A4A2C5439114B888DAC35F1644BA5C96325258C41AD6051E7A4D5F730B62),[49](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-229B4E8F4048EBD1C3D113AAD9B5204574DE1F45FA3D70E1D6B35696BE338613)
  - Assumption: Grants are project support, not sales revenue

## Market

- Company market claim: '10\+ million active drones worldwide' and accelerating global drone activity \(company\-stated\)\. *(Company claim)* ^[50](https://www.dronetag.com/)
  - Assumption: This is a company\-provided market driver
- Procurement demand signal: a won Czech defence tender \(Ministerstvo obrany\) for commercial UAS detection service indicates defence buyer demand\. *(Verified)* ^[24](https://ted.europa.eu/en/notice/-/detail/436033-2026)
  - Assumption: Tender win signals procurement appetite
- Other demand evidence: multiple Czech public buyers \(fire service, airports, hospitals\) bought or borrowed Scout/Rider devices per public contract records\. *(Verified)* ^[47](https://smlouvy.gov.cz/smlouva/39280395),[51](https://smlouvy.gov.cz/smlouva/34910865),[52](https://smlouvy.gov.cz/smlouva/38661160)
  - Assumption: Contracts reflect real institutional customers

## Competition

- DroneTector Limited — listed as NATO DIANA peer; overlaps on small\-drone detection sensors and tracking capabilities \(found in DIANA cohort list\)\. *(Analyst view)* ^[53](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
  - Assumption: Shared DIANA listing implies product overlap
- AegisX — DIANA\-listed peer focused on low\-flying drone detection; operational overlap in 'detect &amp; track' capability\. *(Analyst view)* ^[54](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
  - Assumption: Shared detection focus suggests competitive overlap
- Broader CUAS/Remote ID incumbents and directories reference Dronetag among global vendors; press directories note crowded C\-UAS market\. *(Analyst view)* ^[25](http://www.unmannedairspace.info/uncategorized/dronetag-drone-detection-system-chosen-for-eudis-business-accelerator-funding/),[55](https://globaldronehq.com/blogs/guides/dronetag-rider-review)
  - Assumption: Industry directories indicate many competing vendors

## Case for and against

- **For:** Defence validation and pipeline — won Czech Ministry of Defence tender and multiple public\-supplier contracts showing government procurement traction\. *(Analyst view)* ^[24](https://ted.europa.eu/en/notice/-/detail/436033-2026),[21](https://smlouvy.gov.cz/smlouva/21293531),[45](https://smlouvy.gov.cz/smlouva/35562893)
  - Assumption: Tender win reflects repeatable public procurement capability
- **For:** Product\-market fit signal — published shop SKUs, device sales and customer counts claimed on company site plus mobile apps in stores\. *(Analyst view)* ^[15](https://www.dronetag.com/),[17](https://www.dronetag.com/),[56](https://apps.apple.com/us/app/drone-scanner/id1644548782?uo=4)
  - Assumption: Site claims reflect real unit sales
- **Against:** Market concentration risk — reliance on public grants and R&amp;D project funding \(large R&amp;D project agreements\) could mask commercial margins\. *(Analyst view)* ^[20](https://smlouvy.gov.cz/smlouva/19558935),[8](https://smlouvy.gov.cz/smlouva/19531615),[9](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56)
  - Assumption: Significant RD projects may indicate dependency on public R&amp;D
- **Against:** Competitive pressure — multiple DIANA\-listed peers and global C\-UAS directories suggest crowded competition for defence and public\-safety buyers\. *(Analyst view)* ^[53](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[54](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[25](http://www.unmannedairspace.info/uncategorized/dronetag-drone-detection-system-chosen-for-eudis-business-accelerator-funding/)
  - Assumption: DIANA peer list reflects relevant competition
- **Must be true:** Verify margins and unit economics on device sales plus subscription ARPU to confirm self\-sustaining commercial model\. *(Analyst view)* ^[18](https://shop.dronetag.com/),[46](https://www.dronetag.com/products/mini-4g),[45](https://smlouvy.gov.cz/smlouva/35562893)
  - Assumption: Published prices and contract values can be used to model unit economics
- **Must be true:** Confirm pipeline reproducibility beyond Czech public buyers and that the Ministry\-of\-Defence tender scales to further defence contracts\. *(Analyst view)* ^[24](https://ted.europa.eu/en/notice/-/detail/436033-2026),[47](https://smlouvy.gov.cz/smlouva/39280395),[57](https://smlouvy.gov.cz/smlouva/39254662)
  - Assumption: Current public contracts are representative of future pipeline

# Technical due diligence

## Ownership and capital

- Closed convertible loan \(reported CZK 15 million\) from Y Soft Ventures; corroborating press coverage\. *(Corroborated)* ^[6](https://cc.cz/cesky-startup-dronetag-zajistuje-bezpecne-letani-s-drony-od-brnenskeho-fondu-ziskava-15-milionu/),[19](https://www.monitoruji.cz/domaci/1916288/ceske-krabicky-zajistuji-viditelnost-dronu-dronetag-nyni-ziskal-investici-od-y-softu),[58](https://www.investujeme.cz/tiskove-zpravy/y-soft-ventures-investuje-do-dronetag-poskytne-vyrobu-i-logistiku/)
  - Assumption: Reported amount currency is CZK as stated in sources
- Company incorporated 2019\-06\-07; multiple filings and recent annual reports present in commercial register\. *(Verified)* ^[39](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/08198519),[59](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249),[60](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
  - Assumption: Public filings reflect corporate existence
- Significant public\-money involvement: a mix of purchase orders, R&amp;D project agreements and awarded grants are visible in public registers\. *(Verified)* ^[7](https://smlouvy.gov.cz/smlouva/14335472),[8](https://smlouvy.gov.cz/smlouva/19531615),[9](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56),[48](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-BD75A4A2C5439114B888DAC35F1644BA5C96325258C41AD6051E7A4D5F730B62),[61](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-1C7C01F80F12B968633E05C67F7301F971385B5C0EBD08AD010525B0084D81CD)
  - Assumption: Each cited entry represents one awarded agreement

## Technology profile

- Product surfaces: mobile apps \(Drone Scanner gen\.2 and Drone Scanner\), REST API and visualization platform documented in help pages\. *(Partly verified)* ^[12](https://apps.apple.com/us/app/drone-scanner-gen-2/id6742736434?uo=4),[56](https://apps.apple.com/us/app/drone-scanner/id1644548782?uo=4),[13](https://help.dronetag.com/developers/data-pull/getting-started-rest),[3](https://www.dronetag.com/)
  - Assumption: Docs reflect live product surfaces
- Device portfolio: RIDER, Scout, Mini and Beacon hardware lines sold via shop with listed prices and battery\-life claims\. *(Company claim)* ^[1](https://www.dronetag.com/products/rider),[42](https://www.dronetag.com/products/scout),[43](https://shop.dronetag.com/),[62](https://www.dronetag.com/products/beacon)
- Engineering footprint: public GitHub organization with active repos \(sensor demos, Flutter OpenDroneID plugin\) and developer docs\. *(Partly verified)* ^[11](https://github.com/dronetag),[63](https://github.com/dronetag/scout-sensor-demo-map),[64](https://github.com/dronetag/flutter-opendroneid),[36](https://help.dronetag.com/)
  - Assumption: Public repos indicate in\-house engineering work

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** REST API and device data ingestion can be reproduced using standard REST tooling and open OpenDroneID stacks \(docs and plugins available\)\. *(Analyst view)* ^[13](https://help.dronetag.com/developers/data-pull/getting-started-rest),[64](https://github.com/dronetag/flutter-opendroneid),[65](https://github.com/dronetag/opendronelist)
  - Assumption: Open\- source OpenDroneID implementations suffice for basic ingestion
- **Edge supported by public evidence:** Awarded R&amp;D grants and a public defence tender win show institutional validation for specific projects, not product performance metrics\. *(Analyst view)* ^[9](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56),[48](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-BD75A4A2C5439114B888DAC35F1644BA5C96325258C41AD6051E7A4D5F730B62),[24](https://ted.europa.eu/en/notice/-/detail/436033-2026)
  - Assumption: Grants and tender award imply institutional interest
- **Cannot be judged from outside:** True operational detection accuracy, network scale \(3,000\+ receivers\) and claimed FAA approvals cannot be judged from public repos, docs or press\. *(Analyst view)* ^[14](https://www.dronetag.com/),[15](https://www.dronetag.com/),[16](https://startuply.vc/article/dronetag-s-faa-approved-hardware-serves-15-military-forces-and-40-countries-1gv9lf)
  - Assumption: Requires internal telemetry, certificates, and customer contracts

## Risks and caveats

- Reliance on public funding and R&amp;D projects for tech development could mask product\-market revenue if purchases are limited\. *(Analyst view)* ^[9](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56),[8](https://smlouvy.gov.cz/smlouva/19531615),[7](https://smlouvy.gov.cz/smlouva/14335472)
  - Assumption: Grant/R&amp;D receipts support development more than sales
- Material scale and approval claims \(50k devices, FAA approval, 3,000\+ receivers\) lack direct independent verification in public registers\. *(Analyst view)* ^[15](https://www.dronetag.com/),[16](https://startuply.vc/article/dronetag-s-faa-approved-hardware-serves-15-military-forces-and-40-countries-1gv9lf),[14](https://www.dronetag.com/)
  - Assumption: Public press is not independent certification
- Customer concentration risk unclear: public buyer purchases visible but named commercial customers are not listed in public registers\. *(Analyst view)* ^[45](https://smlouvy.gov.cz/smlouva/35562893),[47](https://smlouvy.gov.cz/smlouva/39280395),[17](https://www.dronetag.com/)
  - Assumption: Public tenders partly offset but do not equal broad commercial revenue

## Questions for founders

- Please provide audited shipment and invoiced\-customer lists to substantiate the '50,000\+ sold devices' claim\. *(Analyst view)* ^[15](https://www.dronetag.com/)
- Please share documentation \(FAA certificates or approvals\) supporting the press claim of 'FAA\-approved hardware'\. *(Analyst view)* ^[16](https://startuply.vc/article/dronetag-s-faa-approved-hardware-serves-15-military-forces-and-40-countries-1gv9lf)
- Provide representative commercial contracts and margin data for purchase orders vs\. R&amp;D grants to clarify revenue mix\. *(Analyst view)* ^[7](https://smlouvy.gov.cz/smlouva/14335472),[8](https://smlouvy.gov.cz/smlouva/19531615),[9](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56)
- Request performance benchmarks and raw detection telemetry to validate claimed network scale and detection accuracy\. *(Analyst view)* ^[14](https://www.dronetag.com/),[64](https://github.com/dronetag/flutter-opendroneid),[63](https://github.com/dronetag/scout-sensor-demo-map)

## Sources

1. [dronetag\.com](https://www.dronetag.com/products/rider) · Company's own website · Product capability — “A compact, wireless, battery\-powered Remote ID receiver designed for public safety organizations and professional pilots, providing instant situational awareness in the field\.”
2. [shop\.dronetag\.com](https://shop.dronetag.com/) · Company's own website · Product capability — “Remote ID Transmitters Make drones digitally visible and compliant across operations\.”
3. [dronetag\.com](https://www.dronetag.com/) · Company's own website · Product capability — “Take command with the Dronetag App, the central hub of our ecosystem\. Manage devices, inspect airspace, and analyze flight data from a single, intuitive interface on mobile and web\.”
4. [help\.dronetag\.com](https://help.dronetag.com/) · Company's own website · Integration — “Use our API services to receive air traffic data, share your data or learn how to integrate our platform services into your application\.”
5. [dronetag\.com](https://www.dronetag.com/) · Company's own website · Integration — “Seamless Integration Our hardware and software are designed to work in perfect harmony\. With over 15 UTM integration partners and a seamless API, our solutions easily integrate into your existing workflow\.”
6. [cc\.cz](https://cc.cz/cesky-startup-dronetag-zajistuje-bezpecne-letani-s-drony-od-brnenskeho-fondu-ziskava-15-milionu/) · Independent press · Funding round — “Aktuální investice je strukturovaná jako konvertibilní půjčka”
7. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/14335472) · Official record · Public contract · 2020\-11\-03 — “Správa informačních technologií města Plzně · 120 000 CZK · objednávka”
8. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/19531615) · Official record · Public contract · 2022\-01\-05 — “České vysoké učení technické v Praze · 6 802 393 CZK · Smlouva o účasti na řešení projektu č\. FW04020025”
9. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56) · Official record · National grant · 2022 — “IoT zařízení pro digitální identifikaci pilotovaného letectví v U\-space · Technologická agentura ČR · 4 102 946 CZK”
10. [web\.archive\.org](https://web.archive.org/web/20250811133329id_/https://www.diana.nato.int/about-diana/2024-cohort-of-companies.html) · Official record · Accelerator selection · 2024 — “DRONETAG — Secure Information Sharing”
11. [github\.com](https://github.com/dronetag) · Public technical artifact · GitHub organisation · 2019\-07\-16 — “dronetag · 31 public repos”
12. [apps\.apple\.com](https://apps.apple.com/us/app/drone-scanner-gen-2/id6742736434?uo=4) · Public technical artifact · Mobile app · 2025\-05\-30 — “Drone Scanner \(gen\.2\)”
13. [help\.dronetag\.com](https://help.dronetag.com/developers/data-pull/getting-started-rest) · Company's own website · Website page — “Getting Started with the REST API \| Dronetag Help”
14. [dronetag\.com](https://www.dronetag.com/) · Company's own website · Technical claim — “Dronetag founders co\-authored the technical white paper for the Remote ID protocol\. We work directly with authorities in the EU, the US, and Asia to shape the future of drone regulation\.”
15. [dronetag\.com](https://www.dronetag.com/) · Company's own website · Revenue / traction figure — “Sold devices 50,000 \+”
16. [startuply\.vc](https://startuply.vc/article/dronetag-s-faa-approved-hardware-serves-15-military-forces-and-40-countries-1gv9lf) · Independent press · Press article · 2026\-05\-22 — “Dronetag's FAA\-Approved Hardware Serves 15 Military Forces and 40 Countries”
17. [dronetag\.com](https://www.dronetag.com/) · Company's own website · Revenue / traction figure — “Customers 25,000 \+”
18. [shop\.dronetag\.com](https://shop.dronetag.com/) · Company's own website · Pricing — “Dronetag RIDER 24,990 Kč”
19. [monitoruji\.cz](https://www.monitoruji.cz/domaci/1916288/ceske-krabicky-zajistuji-viditelnost-dronu-dronetag-nyni-ziskal-investici-od-y-softu) · Independent press · Funding round — “Český startup Dronetag získal investici 15 milionů korun od brněnského fondu Y Soft Ventures spadajícího pod společnost Y Soft\.”
20. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/19558935) · Official record · Public contract · 2021\-12\-21 — “TECHNISERV, spol\. s r\.o\., · 18 646 872 CZK · Smlouva o účasti na řešení projektu CK03000054 a využití výsledků”
21. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/21293531) · Official record · Public contract · 2022\-08\-08 — “Česká republika \- Ministerstvo obrany · 68 970 CZK · 22373/2022\-VLCH Zažízení pro dálkovou identifikaci dronů, č\. spec\. 36896/22, pro projekt AIROPS \(DZRO AIROPS\), Účtování dle bodu usměrnění VaV č\.1\.”
22. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/27898271) · Official record · Public contract · 2024\-03\-05 — “UpVision s\.r\.o\., · 20 119 961 CZK · Smlouva o účasti na řešení projektu CL01000047”
23. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/31992832) · Official record · Public contract · 2025\-02\-03 — “TECHNISERV, spol\. s r\.o\. · 0 CZK · Smlouva o využití výsledků projektu CK03000054”
24. [ted\.europa\.eu](https://ted.europa.eu/en/notice/-/detail/436033-2026) · Official record · EU procurement notice \(TED\) · 2026\-06\-23 — “Czechia – Electronic message and information services – Detekce komerčních UAS pomocí RID \- služba — buyer: Ministerstvo obrany”
25. [unmannedairspace\.info](http://www.unmannedairspace.info/uncategorized/dronetag-drone-detection-system-chosen-for-eudis-business-accelerator-funding/) · Independent press · Press article · 2026\-03\-18 — “Dronetag drone detection system chosen for EUDIS Business Accelerator funding \- Unmanned airspace”
26. [esa\-bic\.cz](https://www.esa-bic.cz/startups/dronetag/) · Independent press · Press article — “Dronetag – ESA BIC Czech Republic”
27. [euro\.cz](https://www.euro.cz/clanky/uz-zadne-ufo-y-soft-investuje-15-milionu-do-startupu-dronetag-ktery-se-zabyva-dalkovou-identifikaci-dronu/) · Independent press · Press article · 2022\-06\-28 — “Už žádné UFO\. Y Soft investuje 15 milionů do startupu Dronetag, který se zabývá dálkovou identifikací dronů \- Euro\.cz”
28. [dronetag\.com](https://www.dronetag.com/) · Company's own website · Product capability — “Portable, battery\-powered drone detection”
29. [dronetag\.com](https://www.dronetag.com/careers) · Company's own website · Job posting — “Engineering Hardware Engineer Prague, Czech Republic Full\-Time On\-Site”
30. [dronetag\.com](https://www.dronetag.com/careers) · Company's own website · Job posting — “Engineering Hardware Engineer Prague, Czech Republic Full\-Time On\-Site See more”
31. [dronetag\.com](https://www.dronetag.com/careers) · Company's own website · Job posting — “Sales Partnership Development Manager Prague, Czech Republic Full\-Time Hybrid”
32. [dronetag\.com](https://www.dronetag.com/careers) · Company's own website · Job posting — “Sales Partnership Development Manager Prague, Czech Republic Full\-Time Hybrid See more”
33. [github\.com](https://github.com/dronetag/pre-commit-hooks) · Public technical artifact · GitHub repository · 2025\-07\-24 — “dronetag/pre\-commit\-hooks · Python · last push 2025\-07\-24”
34. [github\.com](https://github.com/dronetag/device-configuration-sample) · Public technical artifact · GitHub repository · 2025\-09\-19 — “dronetag/device\-configuration\-sample · Sample scripts to control configuration settings of Dronetag devices · Python · last push 2025\-09\-19”
35. [github\.com](https://github.com/dronetag/mavsniff) · Public technical artifact · GitHub repository · 2025\-09\-29 — “dronetag/mavsniff · Python · last push 2025\-09\-29”
36. [help\.dronetag\.com](https://help.dronetag.com/) · Company's own website · Website page — “Dronetag Help”
37. [dronetag\.com](https://www.dronetag.com/reference-installations) · Company's own website · Website page — “Drone Detection Installations by Dronetag”
38. [help\.dronetag\.com](https://help.dronetag.com/) · Company's own website · Pricing — “Find out more about our subscription plans and how to manage your subscription”
39. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/08198519) · Official record · Registry: incorporation · 2019\-06\-07 — “registered 2019\-06\-07”
40. [business\.esa\.int](https://business.esa.int/news/aspiring-to-new-heights-drone-remote-id-device) · Independent press · Press article · 2022\-01\-31 — “Aspiring to new heights with drone Remote ID device”
41. [technologickainkubace\.org](https://technologickainkubace.org/en/news/czech-startup-conquers-america-and-expands-further-makes-drone-tracking-devices/) · Independent press · Press article · 2025\-01\-22 — “Czech startup conquers America and expands further\. Makes drone tracking devices \- Technologická Inkubace”
42. [dronetag\.com](https://www.dronetag.com/products/scout) · Company's own website · Pricing — “From €3,099 / $3,499”
43. [shop\.dronetag\.com](https://shop.dronetag.com/) · Company's own website · Pricing — “Dronetag Mini 7,030 Kč”
44. [shop\.dronetag\.com](https://shop.dronetag.com/) · Company's own website · Pricing — “Dronetag Beacon 3,499 Kč”
45. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/35562893) · Official record · Public contract · 2025\-11\-11 — “LOM PRAHA s\.p\. · 578 709 CZK · Kupní smlouva \- detekční zařízení”
46. [dronetag\.com](https://www.dronetag.com/products/mini-4g) · Company's own website · Pricing — “Plans start at €15 / $15 per month, and you get the first 2 months on us\.”
47. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/39280395) · Official record · Public contract · 2026\-08\-27 — “MV \- generální ředitelství HZS ČR · 198 439 CZK · Nákup stacionárního přijímače dálkové identifikace Dronetag Scout s příslušenstvím”
48. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-BD75A4A2C5439114B888DAC35F1644BA5C96325258C41AD6051E7A4D5F730B62) · Official record · National grant · 2024 — “Zkušební implementace U\-space v České republice · Technologická agentura ČR · 3 696 180 CZK”
49. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-229B4E8F4048EBD1C3D113AAD9B5204574DE1F45FA3D70E1D6B35696BE338613) · Official record · National grant · 2022 — “Digitalizace poskytování služeb AFIS a Radio · Technologická agentura ČR · 4 363 875 CZK”
50. [dronetag\.com](https://www.dronetag.com/) · Company's own website · Market statement — “With 10\+ millions active drones worldwide and exponential market growth, the skies are becoming increasingly complex\.”
51. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/34910865) · Official record · Public contract · 2025\-09\-17 — “České vysoké učení technické v Praze · 140 617 CZK · Dronetag Scout \- 2xOmni \+ 2x90° Sector”
52. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/38661160) · Official record · Public contract · 2026\-07\-07 — “Karlovarská krajská nemocnice a\.s\. · 131 390 CZK · Smlouva o výpůjčce \- 1 x Dronetag Scout v konfiguraci 4x směrová anténa s LTE modulem”
53. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “DroneTector Limited: High\-resolution sensors to detect and track small drones”
54. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “AegisX: Detecting &amp; tracking low flying fibre optic drones”
55. [globaldronehq\.com](https://globaldronehq.com/blogs/guides/dronetag-rider-review) · Independent press · Press article · 2026\-06\-20 — “Dronetag RIDER Review 2026: Remote ID Detector – Global Drone HQ”
56. [apps\.apple\.com](https://apps.apple.com/us/app/drone-scanner/id1644548782?uo=4) · Public technical artifact · Mobile app · 2022\-09\-11 — “Drone Scanner”
57. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/39254662) · Official record · Public contract · 2026\-08\-25 — “Hasičský záchranný sbor Pardubického kraje · 181 322 CZK · objednávka: nákup 1 ks zařízení pro dálkovou identifikaci dronů Dronetag Scout \+4x90°”
58. [investujeme\.cz](https://www.investujeme.cz/tiskove-zpravy/y-soft-ventures-investuje-do-dronetag-poskytne-vyrobu-i-logistiku/) · Independent press · Press article · 2022\-06\-27 — “Y Soft Ventures investuje do Dronetag, poskytne výrobu i logistiku \- Investujeme\.cz \- odborný server společnosti Swiss Life Select a\.s\.”
59. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249) · Official record · Registry: filed document · 2024\-07\-13
60. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249) · Official record · Registry: filed document · 2026\-10\-12
61. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-1C7C01F80F12B968633E05C67F7301F971385B5C0EBD08AD010525B0084D81CD) · Official record · National grant · 2019 — “Podpora byla udělena na základě výběru do programu ESA BIC Prague\. · Agentura pro podporu podnikání a investic CzechInvest · 1 351 788 CZK”
62. [dronetag\.com](https://www.dronetag.com/products/beacon) · Company's own website · Product capability — “Up to 8\-hour battery”
63. [github\.com](https://github.com/dronetag/scout-sensor-demo-map) · Public technical artifact · GitHub repository · 2026\-08\-14 — “dronetag/scout\-sensor\-demo\-map · Example application of consuming data from the sensor mode of the Dronetag Scout · Jinja · last push 2026\-08\-14”
64. [github\.com](https://github.com/dronetag/flutter-opendroneid) · Public technical artifact · GitHub repository · 2026\-11\-02 — “dronetag/flutter\-opendroneid · Flutter plugin for receiving Bluetooth advertising/WiFi NAN signals/beacons · Dart · last push 2026\-11\-02”
65. [github\.com](https://github.com/dronetag/opendronelist) · Public technical artifact · GitHub repository · 2025\-10\-16 — “dronetag/opendronelist · A public community\-driven list of drones and their common properties · HTML · last push 2025\-10\-16”
66. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-E2B306E7B38FFA8D069A99E770C3DD3ABF062E17AAF092CBC25134F2F0570D30) · Official record · National grant · 2020 — “Účast v projektu CzechStarter \(projekt Podpora start\-upů, reg\. č\. CZ\.01\.2\.111/0\.0/0\.0/15\_022/0005661\), VI\. výzva · Agentura pro podporu podnikání a investic CzechInvest · 797 171 CZK”
67. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/39744521) · Official record · Public contract · 2026\-09\-25 — “Státní pokladna Centrum sdílených služeb, s\. p\. · 241 589 CZK · Smlouva o výpůjčce\_zařízení Dronetag Scout”
68. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “OLEDCOMM: Stealth in drone flight\. Unjammable connectivity by light”
69. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “VISS: Hardware\-enforced endpoint protection making remote cyber compromise physically impossible”
70. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “DATAMBIT Limited: AI deepfake detection securing operational integrity and strengthening strategic decisions”
71. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Ca nadian Strategic Missions Corporation: Remote monitoring for Micro Modular Reactors \(MMRs\)”
72. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “SolarinBlue: Fast \(re\)\-deployment of floating solar farms in remote locations”
73. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Volta Space Technologies: Persistent drone flight and emergency power in extremely cold environments”
74. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/08198519) · Official record · Registry: identity · 2019\-06\-07 — “Dronetag s\.r\.o\. · s\.r\.o\. · registered 2019\-06\-07”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 19 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 22 | starfos |
| EU public procurement | TED \(Tenders Electronic Daily\) API: notices naming the company; winner or tenderer by IČO, defence buyers flagged | 1 | — |
| EU funding portal | EU Funding &amp; Tenders portal: participant record matched by IČO, its projects incl\. European Defence Fund | 1 | — |
| NATO DIANA | archived cohort pages \(Wayback Machine; the live site blocks scripts\): selection and competitor candidates from the cohort list | 13 | — |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 20 | press:lupa\.cz, press:pine\.plzen\.eu, press:vcbacked\.co |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 37 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 45 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 14 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 0 | openalex |
| Mobile apps | App Store \(seller must match the company\), Google Play if linked from the site | 2 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 3 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 60 | — |

Analysis: gpt\-5\-mini (cost $0.0217); AI extraction cost $0.0081. Full fact table: CSV export.

## Source appendix (all collected facts)

- F6405 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/08198519](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/08198519)
- F6406 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/08198519](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/08198519)
- F6407 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/08198519](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08198519)
- F6408 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/08198519](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08198519)
- F6409 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/08198519](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08198519)
- F6410 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6411 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6412 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6413 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6414 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6415 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6416 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6417 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6418 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6419 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6420 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6421 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6422 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1053249](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1053249)
- F6423 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=08198519&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=08198519&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F6424 · web\_page · Sourced · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F6425 · web\_page · Sourced · [https://www\.dronetag\.com/careers](https://www.dronetag.com/careers)
- F6426 · web\_page · Sourced · [https://www\.dronetag\.com/privacy\-policy](https://www.dronetag.com/privacy-policy)
- F6427 · subprocessor · Medium confidence · [https://www\.dronetag\.com/privacy\-policy](https://www.dronetag.com/privacy-policy)
- F6428 · web\_page · Sourced · [https://www\.dronetag\.com/careers/3d\-printing\-technologist\-materials\-specialist](https://www.dronetag.com/careers/3d-printing-technologist-materials-specialist)
- F6429 · web\_page · Sourced · [https://www\.dronetag\.com/careers/hardware\-engineer](https://www.dronetag.com/careers/hardware-engineer)
- F6430 · web\_page · Sourced · [https://www\.dronetag\.com/careers/open\-application](https://www.dronetag.com/careers/open-application)
- F6431 · web\_page · Sourced · [https://www\.dronetag\.com/careers/partnership\-development\-manager](https://www.dronetag.com/careers/partnership-development-manager)
- F6432 · web\_page · Sourced · [https://www\.dronetag\.com/careers/senior\-sales\-specialist\-business\-development](https://www.dronetag.com/careers/senior-sales-specialist-business-development)
- F6433 · web\_page · Sourced · [https://help\.dronetag\.com/](https://help.dronetag.com/)
- F6434 · web\_page · Sourced · [https://www\.dronetag\.com/remote\-id\-compliance](https://www.dronetag.com/remote-id-compliance)
- F6435 · subprocessor · Medium confidence · [https://www\.dronetag\.com/remote\-id\-compliance](https://www.dronetag.com/remote-id-compliance)
- F6436 · web\_page · Sourced · [https://www\.dronetag\.com/fleet\-coordination](https://www.dronetag.com/fleet-coordination)
- F6437 · web\_page · Sourced · [https://www\.dronetag\.com/reference\-installations](https://www.dronetag.com/reference-installations)
- F6438 · web\_page · Sourced · [https://help\.dronetag\.com/knowledge\-base/](https://help.dronetag.com/knowledge-base/)
- F6439 · web\_page · Sourced · [https://www\.dronetag\.com/products/rider](https://www.dronetag.com/products/rider)
- F6440 · web\_page · Sourced · [https://www\.dronetag\.com/products/scout](https://www.dronetag.com/products/scout)
- F6441 · web\_page · Sourced · [https://www\.dronetag\.com/products/mini\-4g](https://www.dronetag.com/products/mini-4g)
- F6442 · web\_page · Sourced · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F6443 · web\_page · Sourced · [https://www\.dronetag\.com/products/bs](https://www.dronetag.com/products/bs)
- F6444 · web\_page · Sourced · [https://help\.dronetag\.com/developers/integrations/getting\-started](https://help.dronetag.com/developers/integrations/getting-started)
- F6445 · web\_page · Sourced · [https://help\.dronetag\.com/developers/data\-pull/getting\-started\-rest](https://help.dronetag.com/developers/data-pull/getting-started-rest)
- F6446 · web\_page · Sourced · [https://www\.dronetag\.com/case\-studies](https://www.dronetag.com/case-studies)
- F6447 · web\_page · Sourced · [https://www\.dronetag\.com/company/about\-us](https://www.dronetag.com/company/about-us)
- F6448 · web\_page · Sourced · [https://www\.dronetag\.com/company/partners](https://www.dronetag.com/company/partners)
- F6449 · web\_page · Sourced · [https://www\.dronetag\.com/resources\-case\-studies/helsinki\-case\-study\-\-\-drone\-monitoring](https://www.dronetag.com/resources-case-studies/helsinki-case-study---drone-monitoring)
- F6450 · web\_page · Sourced · [https://www\.dronetag\.com/resources\-case\-studies/drone\-visual\-cntrl\-b\-v\-secure\-festival\-airspace\-with\-dronetag\-scout](https://www.dronetag.com/resources-case-studies/drone-visual-cntrl-b-v-secure-festival-airspace-with-dronetag-scout)
- F6451 · web\_page · Sourced · [https://www\.dronetag\.com/news](https://www.dronetag.com/news)
- F6452 · web\_page · Sourced · [https://www\.dronetag\.com/news/scout\-gen\-2\-is\-shipping\-tracking\-a\-skydio\-out\-to\-5\-miles](https://www.dronetag.com/news/scout-gen-2-is-shipping-tracking-a-skydio-out-to-5-miles)
- F6453 · web\_page · Sourced · [https://www\.dronetag\.com/news/blog\-dronetag\-detection\-airwise\-nexus](https://www.dronetag.com/news/blog-dronetag-detection-airwise-nexus)
- F6454 · web\_page · Sourced · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F6455 · web\_page · Sourced · [https://www\.dronetag\.com/drone\-detection](https://www.dronetag.com/drone-detection)
- F6456 · job\_post · Sourced · [https://www\.dronetag\.com/careers](https://www.dronetag.com/careers)
- F6457 · job\_post · Sourced · [https://www\.dronetag\.com/careers](https://www.dronetag.com/careers)
- F6458 · job\_post · Sourced · [https://www\.dronetag\.com/careers](https://www.dronetag.com/careers)
- F6459 · job\_post · Sourced · [https://www\.dronetag\.com/careers](https://www.dronetag.com/careers)
- F6460 · github\_org · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F6461 · tech\_stack · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F6462 · tech\_stack · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F6463 · tech\_stack · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F6464 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=dronetag\.com&amp;type=MX](https://dns.google/resolve?name=dronetag.com&type=MX)
- F6465 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=dronetag\.com&amp;type=TXT](https://dns.google/resolve?name=dronetag.com&type=TXT)
- F6466 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=dronetag\.com&amp;type=TXT](https://dns.google/resolve?name=dronetag.com&type=TXT)
- F6467 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6468 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6469 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6470 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6471 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6472 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6473 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6474 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6475 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6476 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6477 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6478 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6479 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6480 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6481 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6482 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6483 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6484 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6485 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6486 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6487 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6488 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6489 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6490 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6491 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6492 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6493 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6494 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6495 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6496 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6497 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6498 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6499 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6500 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6501 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6502 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6503 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6504 · subdomain · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6505 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.dronetag\.com&amp;output=json](https://crt.sh/?q=%25.dronetag.com&output=json)
- F6506 · github\_org · Sourced · [https://github\.com/dronetag](https://github.com/dronetag)
- F6507 · repo · Sourced · [https://github\.com/dronetag/meta\-mender\-kernel\-rpi](https://github.com/dronetag/meta-mender-kernel-rpi)
- F6508 · repo · Sourced · [https://github\.com/dronetag/gha\-shared](https://github.com/dronetag/gha-shared)
- F6509 · repo · Sourced · [https://github\.com/dronetag/flutter\-opendroneid](https://github.com/dronetag/flutter-opendroneid)
- F6510 · repo · Sourced · [https://github\.com/dronetag/actions](https://github.com/dronetag/actions)
- F6511 · repo · Sourced · [https://github\.com/dronetag/gira](https://github.com/dronetag/gira)
- F6512 · repo · Sourced · [https://github\.com/dronetag/scout\-sensor\-demo\-map](https://github.com/dronetag/scout-sensor-demo-map)
- F6513 · repo · Sourced · [https://github\.com/dronetag/rider\-connect\-demo](https://github.com/dronetag/rider-connect-demo)
- F6514 · repo · Sourced · [https://github\.com/dronetag/secretservice\-fetcher](https://github.com/dronetag/secretservice-fetcher)
- F6515 · repo · Sourced · [https://github\.com/dronetag/dt\-cert\-uploader](https://github.com/dronetag/dt-cert-uploader)
- F6516 · repo · Sourced · [https://github\.com/dronetag/opendronelist](https://github.com/dronetag/opendronelist)
- F6517 · repo · Sourced · [https://github\.com/dronetag/mavsniff](https://github.com/dronetag/mavsniff)
- F6518 · repo · Sourced · [https://github\.com/dronetag/device\-configuration\-sample](https://github.com/dronetag/device-configuration-sample)
- F6519 · repo · Sourced · [https://github\.com/dronetag/pre\-commit\-hooks](https://github.com/dronetag/pre-commit-hooks)
- F6520 · source\_unavailable · Unavailable · [https://api\.openalex\.org/works?filter=raw\_affiliation\_strings\.search%3ADronetag&amp;per\-page=10](https://api.openalex.org/works?filter=raw_affiliation_strings.search%3ADronetag&per-page=10)
- F6521 · app · Sourced · [https://apps\.apple\.com/us/app/drone\-scanner\-gen\-2/id6742736434?uo=4](https://apps.apple.com/us/app/drone-scanner-gen-2/id6742736434?uo=4)
- F6522 · app · Sourced · [https://apps\.apple\.com/us/app/drone\-scanner/id1644548782?uo=4](https://apps.apple.com/us/app/drone-scanner/id1644548782?uo=4)
- F6523 · wayback\_first · Sourced · [https://web\.archive\.org/web/20240419070336/https://dronetag\.com/](https://web.archive.org/web/20240419070336/https://dronetag.com/)
- F6524 · wayback\_first · Sourced · [https://web\.archive\.org/web/20260124023644/https://www\.dronetag\.com/careers/technical\-product\-manager](https://web.archive.org/web/20260124023644/https://www.dronetag.com/careers/technical-product-manager)
- F6525 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/dronetag\.com](https://web.archive.org/web/%2A/dronetag.com)
- F6553 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6554 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6555 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6556 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6557 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6558 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6559 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6560 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6561 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6562 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6563 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6564 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6565 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6566 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6567 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6568 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6569 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6570 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6571 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6572 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6573 · press\_mention · Sourced · [https://czechinvest\.gov\.cz/en/Key\-sectors/Smart\-mobility\-catalog/Firmy/DRONETAG](https://czechinvest.gov.cz/en/Key-sectors/Smart-mobility-catalog/Firmy/DRONETAG)
- F6574 · press\_mention · Sourced · [https://www\.dronewatch\.eu/startup\-dronetag\-launched\-the\-smallest\-and\-most\-affordable\-remote\-id\-device\-for\-all\-drones](https://www.dronewatch.eu/startup-dronetag-launched-the-smallest-and-most-affordable-remote-id-device-for-all-drones)
- F6575 · press\_mention · Sourced · [https://cc\.cz/cesky\-startup\-dronetag\-zajistuje\-bezpecne\-letani\-s\-drony\-od\-brnenskeho\-fondu\-ziskava\-15\-milionu/](https://cc.cz/cesky-startup-dronetag-zajistuje-bezpecne-letani-s-drony-od-brnenskeho-fondu-ziskava-15-milionu/)
- F6576 · press\_mention · Sourced · [https://www\.euro\.cz/clanky/uz\-zadne\-ufo\-y\-soft\-investuje\-15\-milionu\-do\-startupu\-dronetag\-ktery\-se\-zabyva\-dalkovou\-identifikaci\-dronu/](https://www.euro.cz/clanky/uz-zadne-ufo-y-soft-investuje-15-milionu-do-startupu-dronetag-ktery-se-zabyva-dalkovou-identifikaci-dronu/)
- F6577 · press\_mention · Sourced · [https://www\.monitoruji\.cz/domaci/1916288/ceske\-krabicky\-zajistuji\-viditelnost\-dronu\-dronetag\-nyni\-ziskal\-investici\-od\-y\-softu](https://www.monitoruji.cz/domaci/1916288/ceske-krabicky-zajistuji-viditelnost-dronu-dronetag-nyni-ziskal-investici-od-y-softu)
- F6578 · press\_mention · Sourced · [https://www\.esa\-bic\.cz/startups/dronetag/](https://www.esa-bic.cz/startups/dronetag/)
- F6579 · source\_unavailable · Unavailable · [https://www\.vcbacked\.co/company/dronetag](https://www.vcbacked.co/company/dronetag)
- F6580 · press\_mention · Sourced · [https://startuply\.vc/article/dronetag\-s\-faa\-approved\-hardware\-serves\-15\-military\-forces\-and\-40\-countries\-1gv9lf](https://startuply.vc/article/dronetag-s-faa-approved-hardware-serves-15-military-forces-and-40-countries-1gv9lf)
- F6581 · press\_mention · Sourced · [https://czechinvest\.gov\.cz/cz/Homepage/Novinky/Kveten\-2022/CzechInvest\-Startup\-Challenge\-vyhral\-Dronetag\-zamereny\-na\-bezpecny\-provoz\-dronu](https://czechinvest.gov.cz/cz/Homepage/Novinky/Kveten-2022/CzechInvest-Startup-Challenge-vyhral-Dronetag-zamereny-na-bezpecny-provoz-dronu)
- F6582 · press\_mention · Sourced · [https://help\.dronetag\.cz/dronetag\-rider](https://help.dronetag.cz/dronetag-rider)
- F6583 · press\_mention · Sourced · [https://globaldronehq\.com/blogs/guides/dronetag\-rider\-review](https://globaldronehq.com/blogs/guides/dronetag-rider-review)
- F6584 · press\_mention · Sourced · [http://www\.unmannedairspace\.info/uncategorized/dronetag\-drone\-detection\-system\-chosen\-for\-eudis\-business\-accelerator\-funding/](http://www.unmannedairspace.info/uncategorized/dronetag-drone-detection-system-chosen-for-eudis-business-accelerator-funding/)
- F6585 · press\_mention · Sourced · [https://www\.investujeme\.cz/tiskove\-zpravy/y\-soft\-ventures\-investuje\-do\-dronetag\-poskytne\-vyrobu\-i\-logistiku/](https://www.investujeme.cz/tiskove-zpravy/y-soft-ventures-investuje-do-dronetag-poskytne-vyrobu-i-logistiku/)
- F6586 · source\_unavailable · Unavailable · [https://www\.lupa\.cz/aktuality/ceske\-krabicky\-zajistuji\-viditelnost\-dronu\-dronetag\-nyni\-ziskal\-investici\-od\-y\-softu/](https://www.lupa.cz/aktuality/ceske-krabicky-zajistuji-viditelnost-dronu-dronetag-nyni-ziskal-investici-od-y-softu/)
- F6587 · press\_mention · Sourced · [https://apps\.apple\.com/us/app/dronetag/id1527565210](https://apps.apple.com/us/app/dronetag/id1527565210)
- F6588 · press\_mention · Sourced · [https://help\.dronetag\.cz/cs/dronetag\-scout](https://help.dronetag.cz/cs/dronetag-scout)
- F6589 · press\_mention · Sourced · [https://startuply\.vc/startup/dronetag\-yshvr3](https://startuply.vc/startup/dronetag-yshvr3)
- F6590 · press\_mention · Sourced · [https://leadiq\.com/c/yuneec\-europe/5a1d82d924000024005dad71](https://leadiq.com/c/yuneec-europe/5a1d82d924000024005dad71)
- F6591 · press\_mention · Sourced · [https://technologickainkubace\.org/en/news/czech\-startup\-conquers\-america\-and\-expands\-further\-makes\-drone\-tracking\-devices/](https://technologickainkubace.org/en/news/czech-startup-conquers-america-and-expands-further-makes-drone-tracking-devices/)
- F6592 · press\_mention · Sourced · [https://business\.esa\.int/news/aspiring\-to\-new\-heights\-drone\-remote\-id\-device](https://business.esa.int/news/aspiring-to-new-heights-drone-remote-id-device)
- F6593 · press\_mention · Sourced · [https://ambit\.law/blog/zastupovali\-jsme\-cesky\-startup\-dronetag\-pri\-investici\-15\-milionu\-korun](https://ambit.law/blog/zastupovali-jsme-cesky-startup-dronetag-pri-investici-15-milionu-korun)
- F6594 · source\_unavailable · Unavailable · [https://pine\.plzen\.eu/clanek/cesky\-startup\-dronetag\-ziskal\-vyznamnou\-investici\-qtnz](https://pine.plzen.eu/clanek/cesky-startup-dronetag-ziskal-vyznamnou-investici-qtnz)
- F6595 · press\_mention · Sourced · [https://www\.systemonline\.cz/zpravy/y\-soft\-ventures\-investuje\-do\-dronetag\-poskytne\-vyrobu\-i\-logistiku\-z\.htm](https://www.systemonline.cz/zpravy/y-soft-ventures-investuje-do-dronetag-poskytne-vyrobu-i-logistiku-z.htm)
- F7073 · public\_tender · Sourced · [https://ted\.europa\.eu/en/notice/\-/detail/436033\-2026](https://ted.europa.eu/en/notice/-/detail/436033-2026)
- F7079 · eu\_registration · Sourced · [https://ec\.europa\.eu/info/funding\-tenders/opportunities/portal/screen/how\-to\-participate/org\-details/895667834](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/org-details/895667834)
- F7132 · product\_capability · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7133 · product\_capability · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7134 · product\_capability · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7135 · product\_capability · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7136 · product\_capability · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7137 · integration · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7138 · tech\_claim · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7139 · team\_claim · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7140 · revenue\_claim · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7141 · revenue\_claim · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7142 · revenue\_claim · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7143 · market\_claim · Medium confidence · [https://www\.dronetag\.com/](https://www.dronetag.com/)
- F7144 · product\_capability · Medium confidence · [https://help\.dronetag\.com/](https://help.dronetag.com/)
- F7145 · integration · Medium confidence · [https://help\.dronetag\.com/](https://help.dronetag.com/)
- F7146 · pricing · Medium confidence · [https://help\.dronetag\.com/](https://help.dronetag.com/)
- F7147 · product\_capability · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7148 · product\_capability · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7149 · product\_capability · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7150 · pricing · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7151 · pricing · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7152 · pricing · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7153 · pricing · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7154 · pricing · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7155 · pricing · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7156 · pricing · Medium confidence · [https://shop\.dronetag\.com/](https://shop.dronetag.com/)
- F7157 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/rider](https://www.dronetag.com/products/rider)
- F7158 · tech\_claim · Medium confidence · [https://www\.dronetag\.com/products/rider](https://www.dronetag.com/products/rider)
- F7159 · business\_model · Medium confidence · [https://www\.dronetag\.com/products/rider](https://www.dronetag.com/products/rider)
- F7160 · market\_claim · Medium confidence · [https://www\.dronetag\.com/products/rider](https://www.dronetag.com/products/rider)
- F7161 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/scout](https://www.dronetag.com/products/scout)
- F7162 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/scout](https://www.dronetag.com/products/scout)
- F7163 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/scout](https://www.dronetag.com/products/scout)
- F7164 · pricing · Medium confidence · [https://www\.dronetag\.com/products/scout](https://www.dronetag.com/products/scout)
- F7165 · integration · Medium confidence · [https://www\.dronetag\.com/products/scout](https://www.dronetag.com/products/scout)
- F7166 · market\_claim · Medium confidence · [https://www\.dronetag\.com/products/scout](https://www.dronetag.com/products/scout)
- F7167 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/scout](https://www.dronetag.com/products/scout)
- F7168 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/mini\-4g](https://www.dronetag.com/products/mini-4g)
- F7169 · pricing · Medium confidence · [https://www\.dronetag\.com/products/mini\-4g](https://www.dronetag.com/products/mini-4g)
- F7170 · tech\_claim · Medium confidence · [https://www\.dronetag\.com/products/mini\-4g](https://www.dronetag.com/products/mini-4g)
- F7171 · tech\_claim · Medium confidence · [https://www\.dronetag\.com/products/mini\-4g](https://www.dronetag.com/products/mini-4g)
- F7172 · tech\_claim · Medium confidence · [https://www\.dronetag\.com/products/mini\-4g](https://www.dronetag.com/products/mini-4g)
- F7173 · integration · Medium confidence · [https://www\.dronetag\.com/products/mini\-4g](https://www.dronetag.com/products/mini-4g)
- F7174 · market\_claim · Medium confidence · [https://www\.dronetag\.com/products/mini\-4g](https://www.dronetag.com/products/mini-4g)
- F7175 · product\_capability · Medium confidence · [https://czechinvest\.gov\.cz/en/Key\-sectors/Smart\-mobility\-catalog/Firmy/DRONETAG](https://czechinvest.gov.cz/en/Key-sectors/Smart-mobility-catalog/Firmy/DRONETAG)
- F7176 · market\_claim · Medium confidence · [https://czechinvest\.gov\.cz/en/Key\-sectors/Smart\-mobility\-catalog/Firmy/DRONETAG](https://czechinvest.gov.cz/en/Key-sectors/Smart-mobility-catalog/Firmy/DRONETAG)
- F7177 · funding\_round · Medium confidence · [https://cc\.cz/cesky\-startup\-dronetag\-zajistuje\-bezpecne\-letani\-s\-drony\-od\-brnenskeho\-fondu\-ziskava\-15\-milionu/](https://cc.cz/cesky-startup-dronetag-zajistuje-bezpecne-letani-s-drony-od-brnenskeho-fondu-ziskava-15-milionu/)
- F7178 · product\_capability · Medium confidence · [https://cc\.cz/cesky\-startup\-dronetag\-zajistuje\-bezpecne\-letani\-s\-drony\-od\-brnenskeho\-fondu\-ziskava\-15\-milionu/](https://cc.cz/cesky-startup-dronetag-zajistuje-bezpecne-letani-s-drony-od-brnenskeho-fondu-ziskava-15-milionu/)
- F7179 · tech\_claim · Medium confidence · [https://cc\.cz/cesky\-startup\-dronetag\-zajistuje\-bezpecne\-letani\-s\-drony\-od\-brnenskeho\-fondu\-ziskava\-15\-milionu/](https://cc.cz/cesky-startup-dronetag-zajistuje-bezpecne-letani-s-drony-od-brnenskeho-fondu-ziskava-15-milionu/)
- F7180 · product\_capability · Medium confidence · [https://www\.euro\.cz/clanky/uz\-zadne\-ufo\-y\-soft\-investuje\-15\-milionu\-do\-startupu\-dronetag\-ktery\-se\-zabyva\-dalkovou\-identifikaci\-dronu/](https://www.euro.cz/clanky/uz-zadne-ufo-y-soft-investuje-15-milionu-do-startupu-dronetag-ktery-se-zabyva-dalkovou-identifikaci-dronu/)
- F7181 · tech\_claim · Medium confidence · [https://www\.euro\.cz/clanky/uz\-zadne\-ufo\-y\-soft\-investuje\-15\-milionu\-do\-startupu\-dronetag\-ktery\-se\-zabyva\-dalkovou\-identifikaci\-dronu/](https://www.euro.cz/clanky/uz-zadne-ufo-y-soft-investuje-15-milionu-do-startupu-dronetag-ktery-se-zabyva-dalkovou-identifikaci-dronu/)
- F7182 · funding\_round · Medium confidence · [https://www\.monitoruji\.cz/domaci/1916288/ceske\-krabicky\-zajistuji\-viditelnost\-dronu\-dronetag\-nyni\-ziskal\-investici\-od\-y\-softu](https://www.monitoruji.cz/domaci/1916288/ceske-krabicky-zajistuji-viditelnost-dronu-dronetag-nyni-ziskal-investici-od-y-softu)
- F7183 · product\_capability · Medium confidence · [https://czechinvest\.gov\.cz/cz/Homepage/Novinky/Kveten\-2022/CzechInvest\-Startup\-Challenge\-vyhral\-Dronetag\-zamereny\-na\-bezpecny\-provoz\-dronu](https://czechinvest.gov.cz/cz/Homepage/Novinky/Kveten-2022/CzechInvest-Startup-Challenge-vyhral-Dronetag-zamereny-na-bezpecny-provoz-dronu)
- F7184 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F7185 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F7186 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F7187 · product\_capability · Medium confidence · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F7188 · integration · Medium confidence · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F7189 · customer · Medium confidence · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F7190 · customer · Medium confidence · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F7191 · pricing · Medium confidence · [https://www\.dronetag\.com/products/beacon](https://www.dronetag.com/products/beacon)
- F7280 · accelerator · Sourced · [https://web\.archive\.org/web/20250811133329id\_/https://www\.diana\.nato\.int/about\-diana/2024\-cohort\-of\-companies\.html](https://web.archive.org/web/20250811133329id_/https://www.diana.nato.int/about-diana/2024-cohort-of-companies.html)
- F7281 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7282 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7283 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7284 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7285 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7286 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7287 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7288 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7289 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7290 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7291 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7292 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7706 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/19558935](https://smlouvy.gov.cz/smlouva/19558935)
- F7707 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/38661160](https://smlouvy.gov.cz/smlouva/38661160)
- F7708 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/34910865](https://smlouvy.gov.cz/smlouva/34910865)
- F7709 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/19531615](https://smlouvy.gov.cz/smlouva/19531615)
- F7710 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/14335472](https://smlouvy.gov.cz/smlouva/14335472)
- F7711 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/27898271](https://smlouvy.gov.cz/smlouva/27898271)
- F7712 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/38977950](https://smlouvy.gov.cz/smlouva/38977950)
- F7713 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/35562893](https://smlouvy.gov.cz/smlouva/35562893)
- F7714 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/39254662](https://smlouvy.gov.cz/smlouva/39254662)
- F7715 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/39744521](https://smlouvy.gov.cz/smlouva/39744521)
- F7716 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/38998074](https://smlouvy.gov.cz/smlouva/38998074)
- F7717 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/31992832](https://smlouvy.gov.cz/smlouva/31992832)
- F7718 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/21293531](https://smlouvy.gov.cz/smlouva/21293531)
- F7719 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/39280395](https://smlouvy.gov.cz/smlouva/39280395)
- F7720 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-E2B306E7B38FFA8D069A99E770C3DD3ABF062E17AAF092CBC25134F2F0570D30](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-E2B306E7B38FFA8D069A99E770C3DD3ABF062E17AAF092CBC25134F2F0570D30)
- F7721 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-CB620BAAB8F876B73CB37E46F22B3EA45A7011A6D4B0075BEC74064FA6A5BC56)
- F7722 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-1C7C01F80F12B968633E05C67F7301F971385B5C0EBD08AD010525B0084D81CD](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-1C7C01F80F12B968633E05C67F7301F971385B5C0EBD08AD010525B0084D81CD)
- F7723 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-91075F6ADF3C7044F2C9EAB555A8EF91899AB5777654CB3A43D68FEACBF48DDD](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-91075F6ADF3C7044F2C9EAB555A8EF91899AB5777654CB3A43D68FEACBF48DDD)
- F7724 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-B76EB829109BFE3A239D615E978613CC5F70E191270DD6000FCD8F68FEC287C3](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-B76EB829109BFE3A239D615E978613CC5F70E191270DD6000FCD8F68FEC287C3)
- F7725 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/Eufondy\-D2A8FFBB8D0398366E44EA3D58A40667E5A51A3B1DB5EE6D621F4BA30527B367](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-D2A8FFBB8D0398366E44EA3D58A40667E5A51A3B1DB5EE6D621F4BA30527B367)
- F7726 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-BD75A4A2C5439114B888DAC35F1644BA5C96325258C41AD6051E7A4D5F730B62](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-BD75A4A2C5439114B888DAC35F1644BA5C96325258C41AD6051E7A4D5F730B62)
- F7727 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-229B4E8F4048EBD1C3D113AAD9B5204574DE1F45FA3D70E1D6B35696BE338613](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-229B4E8F4048EBD1C3D113AAD9B5204574DE1F45FA3D70E1D6B35696BE338613)
- F7728 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Dronetag%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Dronetag%27)
- F7729 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
