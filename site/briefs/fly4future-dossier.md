# Fly4Future — due diligence brief

fly4future\.com · Fly4Future s\.r\.o\. · IČO 06632581 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** Autonomous multi‑robot UAV platforms and services targeting industrial inspection, security/defence and delivery customers\. *(Corroborated)* ^[1](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[2](https://www.autonomyrunway.com/companies/fly4future)
- **Stage & traction.** Company is a CTU spinout \(\~40 head\), winning EU Horizon grants and multiple Czech R&amp;D contracts while actively seeking a €10–16M raise \(Series A target cited €8M for a project\)\. *(Partly verified)* ^[3](https://fly4future.com/about-us/),[4](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[5](https://cordis.europa.eu/project/id/101071270),[6](https://smlouvy.gov.cz/smlouva/31970356),[7](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[8](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- **Technology & moat.** Evidence of swarm/autonomy code published \(argentswarm and IROC repos\) plus patent filings and multiple GNSS‑resilient multi‑robot grants, suggesting non‑trivial IP and data accumulation\. *(Verified)* ^[9](https://github.com/fly4future/argentswarm_core),[10](https://github.com/fly4future/iroc_mission_handler),[11](https://patents.google.com/patent/WO2024255934A1),[12](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3)
- **Key risk.** Business appears materially dependent on public grants and a large external capital raise to scale manufacturing and meet stated production ambitions\. *(Analyst view)* ^[13](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7),[14](https://smlouvy.gov.cz/smlouva/28082567),[7](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
- **Diligence focus.** Verify verified NDAA compliance and supply‑chain claims, confirmed production economics for tens of thousands/year, and the legal strength/ownership of the patent filings\. *(Analyst view)* ^[15](https://fly4future.com/),[1](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[11](https://patents.google.com/patent/WO2024255934A1)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2026\-10\-16 · 10 až 16 milionů eur; date n/a · investor search &amp; European funds financing · 100 milionů korun \+ 100 milionů korun \+ 4\-5 milionů eur · neupřesněná firma, Sprind \(agentura\); date n/a · Series A · 8 million euros | 7, 16, 8 |
| Public money | 19 contract\(s\) in the contract register; 24 grant\(s\), 196\.8M CZK \+ 1 without published amount · by kind: 2 purchase\(s\) by public buyers \(755,152 CZK\); 12 R&amp;D project agreement\(s\), amounts are project budgets, not revenue; 2 subsidy agreement\(s\) \(14\.8M CZK\); 3 other \(1\.3M CZK\) · counterparties: Správa informačních technologií města Plzně, Eurosecur s\. r\. o\., VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ, České vysoké učení technické v Praze | 17, 18, 19, 20, 21, 22 |
| Thesis fit \(Rockaway\) | sectors: deep tech \(32 facts\); AI\-led transformative tech \(25 facts\); industrial / manufacturing AI \(18 facts\); defence / dual\-use \(7 facts\); energy \(5 facts\) · geography: CZ \(core region\) · overlaps portfolio: Vermeer \(defence, drone, navigat\) | 23, 24, 25 |
| Hiring | 3 open roles: engineering 2, sales gtm 1 | 26, 27, 28 |
| Engineering footprint | 15 public repos \(6★, last push 2026\-11\-09\); 11 subdomains; 1 docs pages; stack: Apache, Divi v\.4\.27\.9, WordPress | 29, 30, 31, 32 |
| Customers | public pricing: yes | 33 |
| Timeline | Czech entity registered 2017\-11\-27; first press 2026\-06\-15 \(16 articles collected\) | 34, 35 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the market, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** Deep\-tech / defence\-capable multi\-robot UAVs — company claims GNSS\-free autonomy and NDAA\-capable UAV platforms, supported by multi\-robot/GNSS\-resilience grants and press coverage\. *(Analyst view)* ^[36](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[2](https://www.autonomyrunway.com/companies/fly4future),[12](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[5](https://cordis.europa.eu/project/id/101071270),[1](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
  - Assumption: GNSS\-free and NDAA claims imply defence/dual\-use applicability
- **Stage & ticket:** Fundraising described as Series A / investor search with asks €8–16m \(multiple press statements\); this round size is above Rockaway’s initial ticket \(EUR 0\.5–2m\)\. *(Analyst view)* ^[8](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni),[7](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[16](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
  - Assumption: Public asks indicate target round size
- **Portfolio overlap:** Vermeer \(visual/GPS‑free navigation\) — potential overlap/synergy on GPS‑free navigation and drone autonomy; Fly4Future publicly claims GPS‑free capability\. *(Analyst view)* ^[2](https://www.autonomyrunway.com/companies/fly4future),[36](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[3](https://fly4future.com/about-us/)
  - Assumption: Vermeer identified in fund thesis; Fly4Future’s GPS‑free claim drives overlap

## Business model

- Direct sales to public buyers: Fly4Future appears to have sold sensors/consulting via purchase orders to universities/municipal IT units \(examples: CZK 658,829 and CZK 96,323 purchase orders\)\. *(Analyst view)* ^[20](https://smlouvy.gov.cz/smlouva/24070505),[37](https://smlouvy.gov.cz/smlouva/38841586)
  - Assumption: Contracts labelled supplier → represent product/service sales
- Grants and R&amp;D contracts are a major funding channel: multiple national and EU grants and TA ČR/OP‑TAK project participations totalling substantive non\-dilutive support \(examples: CZ EU AeroSTREAM contribution, TA ČR Trend/Sigma grants\)\. *(Analyst view)* ^[5](https://cordis.europa.eu/project/id/101071270),[14](https://smlouvy.gov.cz/smlouva/28082567),[38](https://smlouvy.gov.cz/smlouva/32902152),[39](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB),[12](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3)
  - Assumption: Listed grants are active and material to operations
- Unit pricing: company/press cite a high‑value unit price \~1\.5M CZK per advanced drone platform \(quoted in press for product sales\)\. *(Analyst view)* ^[33](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni),[1](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
  - Assumption: Press unit price reflects current commercial pricing

## Market

- Demand driver: company and press state strong interest in GPS‑free flying across industrial, civilian and defence customers; Fly4Future says industrial partners seek GPS‑free solutions\. *(Analyst view)* ^[36](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[2](https://www.autonomyrunway.com/companies/fly4future)
  - Assumption: Company statements reflect genuine customer interest
- Market size: no explicit TAM or market sizing figure found in supplied facts; press focuses on strategic importance and production ambitions but not a quantified market size\. *(Analyst view)* ^[1](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[25](https://adoptimal.cz/magazin/aktualita/fly4future-chysta-vyrobu-desitek-tisic-autonomnich-dronu-rocne)
  - Assumption: Absence of a cited market number implies no provided TAM in facts

## Competition

- Alpha Autonomy \(NATO DIANA cohort\): peer on autonomous UAV swarms for ISR — appears adjacent/overlapping in swarm autonomy; listed as a NATO DIANA peer candidate\. *(Analyst view)* ^[40](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
  - Assumption: Both companies working on swarm/autonomy creates product overlap
- DJI / Chinese incumbents: press frames Fly4Future as a Czech alternative to China’s DJI; incumbent reference signals market incumbency and competitive scale challenge\. *(Analyst view)* ^[2](https://www.autonomyrunway.com/companies/fly4future),[41](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890)
  - Assumption: Press comparison implies competitive positioning against DJI
- Eurosecur: frequent project counterparty \(large settlement and collaboration on collaborative‑drones projects\); functions more as partner/co‑developer than a direct competitor based on contracts\. *(Analyst view)* ^[18](https://smlouvy.gov.cz/smlouva/19121879),[22](https://smlouvy.gov.cz/smlouva/29827008)
  - Assumption: Large contractual ties imply partnership rather than pure competition

## Case for and against

- **For:** Differentiated technical IP — published patents and repeated R&amp;D grants for GNSS‑resilient multi‑robot UAVs support defensible technology moat\. *(Analyst view)* ^[11](https://patents.google.com/patent/WO2024255934A1),[42](https://patents.google.com/patent/CZ38123U1),[12](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[5](https://cordis.europa.eu/project/id/101071270)
  - Assumption: Patents \+ grants correlate with meaningful technical differentiation
- **For:** Strong non‑dilutive funding runway — multiple substantial national/EU grants and R&amp;D contracts reduce near‑term dilution and validate institutional support\. *(Analyst view)* ^[38](https://smlouvy.gov.cz/smlouva/32902152),[14](https://smlouvy.gov.cz/smlouva/28082567),[39](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB),[43](https://smlouvy.gov.cz/smlouva/31525264)
  - Assumption: Grants materially cover R&amp;D and scaling costs
- **Against:** Required round size vs fund ticket — public asks €8–16m place Fly4Future above Rockaway’s typical initial ticket, complicating a standard lead investment\. *(Analyst view)* ^[8](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni),[7](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[16](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
  - Assumption: Publicly quoted asks reflect target raise
- **Against:** Manufacturability &amp; commercial ramp risk — press claims ambitions to produce tens of thousands per year; execution and supply‑chain independence \(chip/battery\) are unproven at that scale\. *(Analyst view)* ^[25](https://adoptimal.cz/magazin/aktualita/fly4future-chysta-vyrobu-desitek-tisic-autonomnich-dronu-rocne),[1](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[41](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890)
  - Assumption: Press production claims may be aspirational absent factory evidence
- **Must be true:** Validated commercial pipeline — diligence must confirm repeatable, contracted revenue from paying customers beyond R&amp;D grants \(evidence: limited purchase orders and unit pricing references\)\. *(Analyst view)* ^[20](https://smlouvy.gov.cz/smlouva/24070505),[37](https://smlouvy.gov.cz/smlouva/38841586),[33](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
  - Assumption: Early purchase orders are indicative but insufficient for scale

# Technical due diligence

## Ownership and capital

- Incorporation and filings: Fly4Future s\.r\.o\. incorporated 2017‑11‑27; successive accounting filings 2019–2025 are present in the commercial register\. *(Verified)* ^[44](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581),[45](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597),[46](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
  - Assumption: Registry filings represent corporate continuity\.
- Funding activity: public reporting that the company is seeking €10–16M and other signalling of investor searches including a stated Series A target of €8M\. *(Corroborated)* ^[7](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[16](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro),[8](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
  - Assumption: Reported numbers reflect active fundraising, not closed rounds\.
- Public funding footprint: participant in Horizon AeroSTREAM \(org contribution ≈€165k\) and numerous Czech national grants and TA ČR contracts\. *(Verified)* ^[5](https://cordis.europa.eu/project/id/101071270),[13](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7),[47](https://smlouvy.gov.cz/smlouva/34185905)
  - Assumption: Grants materially fund R&amp;D and operations\.

## Technology profile

- Built product surfaces: research/product docs and case pages exist; site hosts a custom‑drones docs page describing lab/turnkey solutions\. *(Partly verified)* ^[32](https://fly4future.com/custom-drones/we-help-you-to-establish-flying-robots-research-lab/),[23](https://www.cnaip.cz/en/entity/fly4future)
  - Assumption: Web docs reflect actual product offerings\.
- Engineering footprint: active GitHub org with C\+\+/ROS components for mission handling, fleet manager and a published swarm core \(repos show recent pushes Oct–Nov 2026\)\. *(Verified)* ^[48](https://github.com/fly4future),[10](https://github.com/fly4future/iroc_mission_handler),[49](https://github.com/fly4future/iroc_fleet_manager),[9](https://github.com/fly4future/argentswarm_core)
  - Assumption: Public repos reflect core product software\.
- AI dependency: no named LLM vendor dependency found in facts; analytics subprocessor listed is Google Analytics \(privacy policy\)\. *(Company claim)* ^[50](https://fly4future.com/privacy-policy/)
  - Assumption: No omission of undisclosed LLM providers in supplied facts\.

## Rebuild check

- **Commodity:** Marketing site and public docs \(Divi/WordPress\) and simple ROS‑to‑WebRTC streaming utilities are rebuildable by 2–3 engineers using WordPress and the public repo rtsp\_to\_ros\. *(Analyst view)* ^[51](https://fly4future.com/),[52](https://fly4future.com/),[31](https://github.com/fly4future/rtsp_to_ros)
  - Assumption: OSS repos are functionally complete for basic features\.
- **Hard to copy:** Multi‑robot swarm autonomy and GNSS‑resilient navigation evidenced by dedicated published swarm core, mission/fleet managers, government R&amp;D grants and patent applications\. *(Analyst view)* ^[9](https://github.com/fly4future/argentswarm_core),[49](https://github.com/fly4future/iroc_fleet_manager),[12](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[11](https://patents.google.com/patent/WO2024255934A1)
  - Assumption: Grants and patents reflect non‑trivial technical progress\.
- **Verdict:** Quarter to clone core autonomy; a clone would lack production‑scale hardware, grant relationships and claimed regulatory or NDAA validation\. *(Analyst view)* ^[9](https://github.com/fly4future/argentswarm_core),[13](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7),[15](https://fly4future.com/)
  - Assumption: Access to equivalent hardware and institutional buyers is constrained\.

## Risks and caveats

- Concentration on public R&amp;D grants and TA ČR contracts; multiple large grants appear to fund core work \(exposure if grant pipeline slows\)\. *(Analyst view)* ^[13](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7),[14](https://smlouvy.gov.cz/smlouva/28082567),[12](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3)
  - Assumption: Grants represent dominant near‑term funding\.
- Production/scale claim risk: public press cites plans for tens‑of‑thousands/year manufacturing, but evidence of factory capacity or committed commercial volume is not in supplied facts\. *(Analyst view)* ^[1](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[41](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890)
  - Assumption: Press coverage may mix ambition with plan\.
- Unverified compliance claim: NDAA‑compliance stated on website is a company claim without independent confirmation in supplied facts\. *(Analyst view)* ^[15](https://fly4future.com/)
  - Assumption: No verification fact provided for NDAA status\.

## Questions for founders

- Please provide documentation proving NDAA compliance \(component traceability, third‑party audit\) cited on the site\. *(Analyst view)* ^[15](https://fly4future.com/)
  - Assumption: Claim requires supplier/component level evidence\.
- Supply‑chain and manufacturing: what contracts, partners or capex commitments underpin the press claim of tens‑of‑thousands units/year? *(Analyst view)* ^[1](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[41](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890)
  - Assumption: Production scale needs binding commitments\.
- Revenue / customer validation: request signed commercial purchase orders or letters of intent from named customers beyond R&amp;D collaborations\. *(Analyst view)* ^[53](https://smlouvy.gov.cz/smlouva/34343605),[6](https://smlouvy.gov.cz/smlouva/31970356)
  - Assumption: R&amp;D contracts ≠ commercial recurring revenue\.
- Patent ownership and scope: provide claim charts and assignment evidence for WO2024255934A1 and CZ38123U1 and any freedom‑to‑operate analyses\. *(Analyst view)* ^[11](https://patents.google.com/patent/WO2024255934A1),[42](https://patents.google.com/patent/CZ38123U1)
  - Assumption: Applications require validation to assess moat\.

## Sources

1. [cc\.cz](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/) · Independent press · Press article · 2026\-10\-16 — “Drony budou nosit jídlo i očkovat krávy\. Díky české technologii \- CzechCrunch”
2. [autonomyrunway\.com](https://www.autonomyrunway.com/companies/fly4future) · Independent press · Press article — “Fly4Future — Autonomy Runway”
3. [fly4future\.com](https://fly4future.com/about-us/) · Company's own website · Team claim — “Fly4Future was formed in 2017 as a spinout of the Multi\-Robot Systems group at the Czech Technical University in Prague \(MRS CTU\)”
4. [cc\.cz](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/) · Independent press · Team claim — “Dnes má kolem 40 zaměstnanců\.”
5. [cordis\.europa\.eu](https://cordis.europa.eu/project/id/101071270) · Official record · EU grant · 2022\-07\-01 — “Strengthening Research and Innovation Excellence in Autonomous Aerial Systems”
6. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/31970356) · Official record · Public contract · 2025\-01\-23 — “Jihočeská univerzita v Českých Budějovicích · 9 000 723 CZK · Smlouva o účasti na řešení projektu \- „Udržitelné zemědělství: Energeticky výkonné bezpilotní technologie pro precizní zemědělství" \- oprava metadat, ceny”
7. [cc\.cz](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/) · Independent press · Funding round — “Fly4future proto nyní od investorů žádá 10 až 16 milionů eur, tedy zhruba 244 až 390 milionů korun\.”
8. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni) · Independent press · Funding round — “Bereme to už jako Series A, protože máme produkt a kontrakty\. Potřebujeme zatím pro jeden projekt získat osm milionů eur \(necelých 200 milionů korun – pozn\. red\.\)\.”
9. [github\.com](https://github.com/fly4future/argentswarm_core) · Public technical artifact · GitHub repository · 2026\-10\-22 — “fly4future/argentswarm\_core · Digest of the swarm autonomy software at f4f\. · C\+\+ · last push 2026\-10\-22”
10. [github\.com](https://github.com/fly4future/iroc_mission_handler) · Public technical artifact · GitHub repository · 2026\-10\-30 — “fly4future/iroc\_mission\_handler · Action server component that manages drone flight through desired waypoints\. · C\+\+ · last push 2026\-10\-30”
11. [patents\.google\.com](https://patents.google.com/patent/WO2024255934A1) · Official record · Patent publication — “WO2024255934A1 · Method of marking bark beetle infested trees and means for executing this … · Fly4Future s\.r\.o\.”
12. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3) · Official record · National grant · 2025 — “Multi\-robotický letecký systém pro autonomní bezpečnostní dohled a inspekci rozlehlých průmyslových objektů odolný vůči výpadku komunikace a signálu GNSS · Technologická agentura ČR · 16 601 665 CZK”
13. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7) · Official record · National grant · 2021 — “Univerzální systém kolaborativních dronů · Ministerstvo průmyslu a obchodu · 10 279 779 CZK”
14. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/28082567) · Official record · National grant · 2024 — “Smlouva o poskytnutí podpory Trend 10 \(FW10\) · Technologická agentura České republiky · 19 404 800 CZK”
15. [fly4future\.com](https://fly4future.com/) · Company's own website · Technical claim — “All of our UAV platforms are fully capable of meeting NDAA compliance , ensuring that our products are free from components sourced from prohibited manufacturers as outlined in Section 889 of the U\.S\. National Defense Authorization Act \(NDAA\)”
16. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro) · Independent press · Funding round — “Od jedné firmy už máme příslib přes 100 milionů korun\. K tomu plánujeme získat dalších 100 milionů z evropských fondů\. To je budget, který potřebuji na vybudování týmu\. V úterý jedu do Německa jednat s agenturou Sprind, která by nám mohla zprostředkovat investici kolem čtyř až pěti milionů eur na vývoj autonomních rojů”
17. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/7574923) · Official record · Public contract · 2018\-12\-05 — “Správa informačních technologií města Plzně · 592 900 CZK · smlouva o obchodní spoluporáci”
18. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/19121879) · Official record · Public contract · 2022\-01\-17 — “Eurosecur s\. r\. o\. · 74 624 392 CZK · Dohoda o vypořádání závazků z neuveřejněné smlouvy o spolupráci na řešení projektu „Univerzální systém kolaborativních dronů"”
19. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/19719811) · Official record · Public contract · 2022\-02\-28 — “Správa informačních technologií města Plzně · 589 270 CZK · Smlouva o obchodní spolupráci”
20. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/24070505) · Official record · Public contract · 2023\-04\-12 — “VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ · 658 829 CZK · Kupní smlouva \- Senzorický systém pro mobilní roboty – 3D laserové skenery”
21. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/27109547) · Official record · Public contract · 2024\-01\-01 — “VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ · 2 400 000 CZK · SMLOUVA O ÚČASTI NA ŘEŠENÍ PROJEKTU A O VYUŽITÍ VÝSLEDKŮ”
22. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/29827008) · Official record · Public contract · 2024\-08\-14 — “Eurosecur s\. r\. o\. · 25 494 062 CZK · Smlouva o spolupráci na řešení projektu OP TAK „Univerzální systém kolaborativních robotů“”
23. [cnaip\.cz](https://www.cnaip.cz/en/entity/fly4future) · Independent press · Press article — “Fly4Future — CNAIP”
24. [fel\.cvut\.cz](https://fel.cvut.cz/en/what-s-on/news/36454-ctu-spinout-fly4future-wins-prestigious-ai-company-of-the-year-award-at-ai-awards-2024) · Independent press · Press article — “CTU spinout Fly4Future wins prestigious AI Company of the Year award at AI Awards 2024 \- CTU FEE”
25. [adoptimal\.cz](https://adoptimal.cz/magazin/aktualita/fly4future-chysta-vyrobu-desitek-tisic-autonomnich-dronu-rocne) · Independent press · Press article · 2026\-08\-17 — “Fly4Future chystá výrobu desítek tisíc autonomních dronů ročně”
26. [fly4future\.com](https://fly4future.com/career/) · Company's own website · Job posting — “System Engineer Specialist”
27. [fly4future\.com](https://fly4future.com/career/) · Company's own website · Job posting — “Robotics SW Engineer”
28. [fly4future\.com](https://fly4future.com/career/) · Company's own website · Job posting — “Technical Sales Engineer”
29. [github\.com](https://github.com/fly4future/spi_uwb_controller) · Public technical artifact · GitHub repository · 2025\-04\-13 — “fly4future/spi\_uwb\_controller · C · last push 2025\-04\-13”
30. [github\.com](https://github.com/fly4future/siyi_cam_executor_plugin) · Public technical artifact · GitHub repository · 2025\-08\-28 — “fly4future/siyi\_cam\_executor\_plugin · A ROS package that provides a plugin for controlling Siyi camera gimbals\. This plugin is designed to be used by the mission handler package for executing subtasks during missions\. · C\+\+ · last push 2025\-08\-28”
31. [github\.com](https://github.com/fly4future/rtsp_to_ros) · Public technical artifact · GitHub repository · 2026\-03\-20 — “fly4future/rtsp\_to\_ros · Python · last push 2026\-03\-20”
32. [fly4future\.com](https://fly4future.com/custom-drones/we-help-you-to-establish-flying-robots-research-lab/) · Company's own website · Website page — “We Help You to Establish Flying Robots’ Research/Lab \| Fly4Future”
33. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni) · Independent press · Pricing — “Nějakých 70 až 80 kusů ročně\. Jde ale o stroje až za 1,5 milionu korun s velkou přidanou hodnotou\.”
34. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581) · Official record · Registry: incorporation · 2017\-11\-27 — “registered 2017\-11\-27”
35. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/en/media-screenings/20260615-the-development-of-drones-in-the-czech-republic-will-be-ensured-by-a-darpa) · Independent press · Press article · 2026\-06\-15 — “The development of drones in the Czech Republic will be ensured by a DARPA\-like agency, a smart army and strong investors \- News service \- Czech technical university in Prague”
36. [fly4future\.com](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/) · Company's own website · Market statement — “Thanks to our participation in the competition, we have created a truly unique system that is already in demand by clients\. Several industrial partners are now focusing on flying without GPS , so this is a very hot topic now that not only the defence industry but also the civilian industry is aware of\.”
37. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/38841586) · Official record · Public contract · 2026\-07\-17 — “Vysoká škola báňská \- Technická univerzita Ostrava · 96 323 CZK · Objednávka: konzultace pro vývoj dronové platformy”
38. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/32902152) · Official record · National grant · 2025 — “Smlouva o poskytnutí podpory Trend \(FW12\) · Technologická agentura České republiky · 21 826 349 CZK”
39. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB) · Official record · National grant · 2028 — “Létající robot využívající umělou inteligencí pro bezpečný odchyt nepovolených dronů v chráněném prostoru · Ministerstvo pro místní rozvoj · 35 982 614 CZK”
40. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Alpha Autonomy: AI\-powered autonomous UAV swarms for resilient, low\-altitude ISR in denied &amp; contested environments”
41. [e15\.cz](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890) · Independent press · Press article · 2026\-08\-12 — “Češi chtějí narušit čínskou nadvládu nad drony\. Chystají výrobu desetitisíců kusů ročně \| e15\.cz”
42. [patents\.google\.com](https://patents.google.com/patent/CZ38123U1) · Official record · Patent publication — “CZ38123U1 · A drone sprayer · Fly4Future s\.r\.o\.”
43. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/31525264) · Official record · Public contract · 2024\-12\-17 — “České vysoké učení technické v Praze · 6 839 513 CZK · Smlouva o účasti na řešení projektuTQ15000370”
44. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581) · Official record · Registry: identity · 2017\-11\-27 — “Fly4Future s\.r\.o\. · s\.r\.o\. · registered 2017\-11\-27”
45. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597) · Official record · Registry: filed document · 2025\-07\-23
46. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597) · Official record · Registry: filed document · 2026\-07\-17
47. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/34185905) · Official record · Public contract · 2025\-07\-18 — “Technologická agentura České republiky · 14 761 078 CZK · Smlouva o posk\. podp\. Sigma \(TQ16\) 8\.VS DC4”
48. [github\.com](https://github.com/fly4future) · Public technical artifact · GitHub organisation · 2021\-05\-12 — “fly4future · 82 public repos”
49. [github\.com](https://github.com/fly4future/iroc_fleet_manager) · Public technical artifact · GitHub repository · 2026\-10\-30 — “fly4future/iroc\_fleet\_manager · ROS node for handling fleet mission execution, part of the "IROC\_Core" package\. · C\+\+ · last push 2026\-10\-30”
50. [fly4future\.com](https://fly4future.com/privacy-policy/) · Company's own website · Subprocessor \(privacy policy\) — “We use Google Analytics to track this information\. Find out how Google uses your data at”
51. [fly4future\.com](https://fly4future.com/) · Public technical artifact · Technology detected
52. [fly4future\.com](https://fly4future.com/) · Public technical artifact · Technology detected
53. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/34343605) · Official record · Public contract · 2025\-07\-25 — “České vysoké učení technické v Praze · 12 270 000 CZK · SMLOUVA O ÚČASTI NA ŘEŠENÍ PROJEKTU A O VYUŽITÍ VÝSLEDKŮ OZ01020024”
54. [ec\.europa\.eu](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/org-details/887136005) · Official record · EU grant — “Strengthening Research and Innovation Excellence in Autonomous Aerial Systems”
55. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/35674989) · Official record · Public contract · 2025\-11\-19 — “Česká agentura na podporu obchodu · 60 984 CZK · Smlouva o poskytnutí zvýhodněné služby Design”
56. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/35675041) · Official record · Public contract · 2025\-11\-19 — “Česká agentura na podporu obchodu · 87 120 CZK · Smlouva o spolupráci Design”
57. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Arke Telekom Mühendislik Elektronik Sanayi Ticaret Ltd\. Şti: Resilient, autonomous communication architecture for GNSS\-free tactical drone operations”
58. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Marble Aerospace Limited: Fleets of high\-speed UAVs with autonomous robotic hangars to create rapidly deployable “ISR bubbles””
59. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Drone City: Heavy\-lift UAV with advanced autonomy for extreme environments”
60. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Volta Space Technologies: Persistent drone flight and emergency power in extremely cold environments”
61. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Mara: Simultaneous 360° protection against swarms of 48\+ EW\-resistant drones at 1/20th the cost\.”
62. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “AegisX: Detecting &amp; tracking low flying fibre optic drones”
63. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “OLEDCOMM: Stealth in drone flight\. Unjammable connectivity by light”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 22 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 43 | starfos |
| EU public procurement | TED \(Tenders Electronic Daily\) API: notices naming the company; winner or tenderer by IČO, defence buyers flagged | 1 | — |
| EU funding portal | EU Funding &amp; Tenders portal: participant record matched by IČO, its projects incl\. European Defence Fund | 2 | — |
| NATO DIANA | archived cohort pages \(Wayback Machine; the live site blocks scripts\): selection and competitor candidates from the cohort list | 12 | — |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 16 | press:theintelligent\.cz, press:uava\.cz |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 24 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 18 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 16 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 2 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 2 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 46 | — |

Analysis: gpt\-5\-mini (cost $0.0258); AI extraction cost $0.0080. Full fact table: CSV export.

## Source appendix (all collected facts)

- F6596 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/06632581](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581)
- F6597 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/06632581](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581)
- F6598 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/06632581](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06632581)
- F6599 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/06632581](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06632581)
- F6600 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/06632581](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06632581)
- F6601 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/06632581](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06632581)
- F6602 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6603 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6604 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6605 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6606 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6607 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6608 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6609 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6610 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6611 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6612 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6613 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6614 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6615 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6616 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=995597](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- F6617 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=06632581&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=06632581&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F6618 · web\_page · Sourced · [https://fly4future\.com/](https://fly4future.com/)
- F6619 · web\_page · Sourced · [https://fly4future\.com/career/](https://fly4future.com/career/)
- F6620 · web\_page · Sourced · [https://fly4future\.com/privacy\-policy/](https://fly4future.com/privacy-policy/)
- F6621 · subprocessor · Medium confidence · [https://fly4future\.com/privacy\-policy/](https://fly4future.com/privacy-policy/)
- F6622 · web\_page · Sourced · [https://fly4future\.com/cookie\-policy\-eu/](https://fly4future.com/cookie-policy-eu/)
- F6623 · web\_page · Sourced · [https://fly4future\.com/career/technical\-sales\-engineer/](https://fly4future.com/career/technical-sales-engineer/)
- F6624 · web\_page · Sourced · [https://fly4future\.com/career/robotics\-sw\-engineer/](https://fly4future.com/career/robotics-sw-engineer/)
- F6625 · web\_page · Sourced · [https://fly4future\.com/career/system\-engineer\-specialist/](https://fly4future.com/career/system-engineer-specialist/)
- F6626 · web\_page · Sourced · [https://fly4future\.com/winning\-solution\-sprind\-drone\-flight\-without\-gps/](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
- F6627 · web\_page · Sourced · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-coast\-guard\-and\-maritime\-security/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-coast-guard-and-maritime-security/)
- F6628 · web\_page · Sourced · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F6629 · web\_page · Sourced · [https://fly4future\.com/custom\-drones/we\-help\-you\-to\-establish\-flying\-robots\-research\-lab/](https://fly4future.com/custom-drones/we-help-you-to-establish-flying-robots-research-lab/)
- F6630 · web\_page · Sourced · [https://fly4future\.com/about\-us/](https://fly4future.com/about-us/)
- F6631 · web\_page · Sourced · [https://fly4future\.com/development\-and\-prototyping/autonomous\-gnss\-denied\-drones\-for\-outdoor\-missions\-in\-gps\-deprived\-areas/](https://fly4future.com/development-and-prototyping/autonomous-gnss-denied-drones-for-outdoor-missions-in-gps-deprived-areas/)
- F6632 · web\_page · Sourced · [https://fly4future\.com/articles/](https://fly4future.com/articles/)
- F6633 · web\_page · Sourced · [https://fly4future\.com/news/](https://fly4future.com/news/)
- F6634 · web\_page · Sourced · [https://fly4future\.com/news/fly4future\-wins\-sprind\-funke\-competition](https://fly4future.com/news/fly4future-wins-sprind-funke-competition)
- F6635 · web\_page · Sourced · [https://dronebuilder\.fly4future\.com/](https://dronebuilder.fly4future.com/)
- F6636 · web\_page · Sourced · [https://fly4future\.com/custom\-drones/](https://fly4future.com/custom-drones/)
- F6637 · job\_post · Sourced · [https://fly4future\.com/career/](https://fly4future.com/career/)
- F6638 · job\_post · Sourced · [https://fly4future\.com/career/](https://fly4future.com/career/)
- F6639 · job\_post · Sourced · [https://fly4future\.com/career/](https://fly4future.com/career/)
- F6640 · github\_org · Medium confidence · [https://fly4future\.com/](https://fly4future.com/)
- F6641 · github\_org · Low confidence · [https://fly4future\.com/custom\-drones/](https://fly4future.com/custom-drones/)
- F6642 · tech\_stack · Medium confidence · [https://fly4future\.com/](https://fly4future.com/)
- F6643 · tech\_stack · Medium confidence · [https://fly4future\.com/](https://fly4future.com/)
- F6644 · tech\_stack · Medium confidence · [https://fly4future\.com/](https://fly4future.com/)
- F6645 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=fly4future\.com&amp;type=MX](https://dns.google/resolve?name=fly4future.com&type=MX)
- F6646 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=fly4future\.com&amp;type=TXT](https://dns.google/resolve?name=fly4future.com&type=TXT)
- F6647 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6648 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6649 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6650 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6651 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6652 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6653 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6654 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6655 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6656 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6657 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6658 · subdomain · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6659 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.fly4future\.com&amp;output=json](https://crt.sh/?q=%25.fly4future.com&output=json)
- F6660 · github\_org · Sourced · [https://github\.com/fly4future](https://github.com/fly4future)
- F6661 · repo · Sourced · [https://github\.com/fly4future/install\_script](https://github.com/fly4future/install_script)
- F6662 · repo · Sourced · [https://github\.com/fly4future/iroc\_mission\_handler](https://github.com/fly4future/iroc_mission_handler)
- F6663 · repo · Sourced · [https://github\.com/fly4future/iroc\_bridge](https://github.com/fly4future/iroc_bridge)
- F6664 · repo · Sourced · [https://github\.com/fly4future/iroc\_fleet\_manager](https://github.com/fly4future/iroc_fleet_manager)
- F6665 · repo · Sourced · [https://github\.com/fly4future/uvdar\_calibrator](https://github.com/fly4future/uvdar_calibrator)
- F6666 · repo · Sourced · [https://github\.com/fly4future/argentswarm\_core](https://github.com/fly4future/argentswarm_core)
- F6667 · repo · Sourced · [https://github\.com/fly4future/iroc\_common](https://github.com/fly4future/iroc_common)
- F6668 · repo · Sourced · [https://github\.com/fly4future/rtsp\_android\_client](https://github.com/fly4future/rtsp_android_client)
- F6669 · repo · Sourced · [https://github\.com/fly4future/\.github](https://github.com/fly4future/.github)
- F6670 · repo · Sourced · [https://github\.com/fly4future/hz\_subscriber](https://github.com/fly4future/hz_subscriber)
- F6671 · repo · Sourced · [https://github\.com/fly4future/webrtc\_ros](https://github.com/fly4future/webrtc_ros)
- F6672 · repo · Sourced · [https://github\.com/fly4future/multirobot\_planner\_template](https://github.com/fly4future/multirobot_planner_template)
- F6673 · repo · Sourced · [https://github\.com/fly4future/rtsp\_to\_ros](https://github.com/fly4future/rtsp_to_ros)
- F6674 · repo · Sourced · [https://github\.com/fly4future/siyi\_cam\_executor\_plugin](https://github.com/fly4future/siyi_cam_executor_plugin)
- F6675 · repo · Sourced · [https://github\.com/fly4future/spi\_uwb\_controller](https://github.com/fly4future/spi_uwb_controller)
- F6676 · wayback\_first · Sourced · [https://web\.archive\.org/web/20120325213234/http://fly4future\.com:80/](https://web.archive.org/web/20120325213234/http://fly4future.com:80/)
- F6677 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/fly4future\.com](https://web.archive.org/web/%2A/fly4future.com)
- F6722 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6723 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6724 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6725 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6726 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6727 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6728 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6729 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6730 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6731 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6732 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6733 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6734 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6735 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6736 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6737 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6738 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6739 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6740 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F6741 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F6742 · press\_mention · Sourced · [https://cityforthefuture\.com/en/dubai/exhibitor/fly4future](https://cityforthefuture.com/en/dubai/exhibitor/fly4future)
- F6743 · press\_mention · Sourced · [https://www\.cnaip\.cz/en/entity/fly4future](https://www.cnaip.cz/en/entity/fly4future)
- F6744 · press\_mention · Sourced · [https://fel\.cvut\.cz/en/what\-s\-on/news/36454\-ctu\-spinout\-fly4future\-wins\-prestigious\-ai\-company\-of\-the\-year\-award\-at\-ai\-awards\-2024](https://fel.cvut.cz/en/what-s-on/news/36454-ctu-spinout-fly4future-wins-prestigious-ai-company-of-the-year-award-at-ai-awards-2024)
- F6745 · press\_mention · Sourced · [https://github\.com/fly4future](https://github.com/fly4future)
- F6746 · source\_unavailable · Unavailable · [https://theintelligent\.cz/technologie/2026/cesky\-dron\-fly4future\-rozumi\-mluvenym\-pokynum\-funguje\-bez\-gps](https://theintelligent.cz/technologie/2026/cesky-dron-fly4future-rozumi-mluvenym-pokynum-funguje-bez-gps)
- F6747 · press\_mention · Sourced · [https://adoptimal\.cz/magazin/aktualita/fly4future\-chysta\-vyrobu\-desitek\-tisic\-autonomnich\-dronu\-rocne](https://adoptimal.cz/magazin/aktualita/fly4future-chysta-vyrobu-desitek-tisic-autonomnich-dronu-rocne)
- F6748 · source\_unavailable · Unavailable · [https://uava\.cz/wp\-content/uploads/2024/09/10\-f4f\.pdf](https://uava.cz/wp-content/uploads/2024/09/10-f4f.pdf)
- F6749 · press\_mention · Sourced · [https://cc\.cz/od\-univerzitniho\-projektu\-po\-milionove\-trzby\-ceske\-drony\-maji\-za\-ukol\-dorucit\-jidlo\-zachranit\-zivot\-i\-ockovat/](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
- F6750 · press\_mention · Sourced · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260414\-cesti\-vedci\-vytvorili\-letajici\-roj\-autonomnich\-dronu\-ted\-shani\-investory\-pro](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
- F6751 · source\_unavailable · Unavailable · [https://theintelligent\.cz/technologie/2026/fly4future\-chce\-masovou\-vyrobu\-autonomnich\-dronu\-jako\-evropskou\-odpoved\-na\-cinskou](https://theintelligent.cz/technologie/2026/fly4future-chce-masovou-vyrobu-autonomnich-dronu-jako-evropskou-odpoved-na-cinskou)
- F6752 · press\_mention · Sourced · [https://www\.e15\.cz/byznys/cesi\-chteji\-narusit\-cinskou\-nadvladu\-nad\-drony\-chystaji\-vyrobu\-desetitisicu\-kusu\-rocne\-1434890](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890)
- F6753 · press\_mention · Sourced · [https://czechinvest\.gov\.cz/en/Key\-sectors/Smart\-mobility\-catalog/Firmy/Fly4Future](https://czechinvest.gov.cz/en/Key-sectors/Smart-mobility-catalog/Firmy/Fly4Future)
- F6754 · press\_mention · Sourced · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260615\-rozvoj\-dronu\-v\-cesku\-zajisti\-obdoba\-agentury\-darpa\-chytra\-armada\-a\-silni](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- F6755 · press\_mention · Sourced · [https://24n\.cz/ru/cheshskie\-drony\-fly4future\-brosaiut\-vyzov\-dji\-investitsii\-avtonomnost](https://24n.cz/ru/cheshskie-drony-fly4future-brosaiut-vyzov-dji-investitsii-avtonomnost)
- F6756 · press\_mention · Sourced · [https://aktualne\.cvut\.cz/en/media\-screenings/20260615\-the\-development\-of\-drones\-in\-the\-czech\-republic\-will\-be\-ensured\-by\-a\-darpa](https://aktualne.cvut.cz/en/media-screenings/20260615-the-development-of-drones-in-the-czech-republic-will-be-ensured-by-a-darpa)
- F6757 · press\_mention · Sourced · [https://aktualne\.cvut\.cz/en/media\-screenings/20260930\-the\-czech\-answer\-to\-chinas\-dji\-a\-couple\-developed\-drones\-that\-work\-even](https://aktualne.cvut.cz/en/media-screenings/20260930-the-czech-answer-to-chinas-dji-a-couple-developed-drones-that-work-even)
- F6758 · press\_mention · Sourced · [https://aktualne\.cvut\.cz/en/media\-screenings/20260813\-the\-czechs\-want\-to\-disrupt\-chinas\-dominance\-over\-drones\-they\-plan\-to](https://aktualne.cvut.cz/en/media-screenings/20260813-the-czechs-want-to-disrupt-chinas-dominance-over-drones-they-plan-to)
- F6759 · press\_mention · Sourced · [https://www\.autonomyrunway\.com/companies/fly4future](https://www.autonomyrunway.com/companies/fly4future)
- F6760 · press\_mention · Sourced · [https://fel\.cvut\.cz/cs/aktualne/novinky/36454\-spinout\-cvut\-fly4future\-ziskal\-prestizni\-oceneni\-ai\-firma\-roku\-na\-ai\-awards\-2024](https://fel.cvut.cz/cs/aktualne/novinky/36454-spinout-cvut-fly4future-ziskal-prestizni-oceneni-ai-firma-roku-na-ai-awards-2024)
- F7070 · public\_tender · Medium confidence · [https://ted\.europa\.eu/en/notice/\-/detail/271589\-2023](https://ted.europa.eu/en/notice/-/detail/271589-2023)
- F7076 · eu\_registration · Sourced · [https://ec\.europa\.eu/info/funding\-tenders/opportunities/portal/screen/how\-to\-participate/org\-details/887136005](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/org-details/887136005)
- F7077 · grant\_eu · Sourced · [https://ec\.europa\.eu/info/funding\-tenders/opportunities/portal/screen/how\-to\-participate/org\-details/887136005](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/org-details/887136005)
- F7082 · product\_capability · Medium confidence · [https://fly4future\.com/](https://fly4future.com/)
- F7083 · product\_capability · Medium confidence · [https://fly4future\.com/](https://fly4future.com/)
- F7084 · tech\_claim · Medium confidence · [https://fly4future\.com/](https://fly4future.com/)
- F7085 · tech\_claim · Medium confidence · [https://fly4future\.com/winning\-solution\-sprind\-drone\-flight\-without\-gps/](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
- F7086 · market\_claim · Medium confidence · [https://fly4future\.com/winning\-solution\-sprind\-drone\-flight\-without\-gps/](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
- F7087 · team\_claim · Medium confidence · [https://fly4future\.com/winning\-solution\-sprind\-drone\-flight\-without\-gps/](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
- F7088 · team\_claim · Medium confidence · [https://fly4future\.com/winning\-solution\-sprind\-drone\-flight\-without\-gps/](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
- F7089 · product\_capability · Medium confidence · [https://fly4future\.com/about\-us/](https://fly4future.com/about-us/)
- F7090 · integration · Medium confidence · [https://fly4future\.com/about\-us/](https://fly4future.com/about-us/)
- F7091 · integration · Medium confidence · [https://fly4future\.com/about\-us/](https://fly4future.com/about-us/)
- F7092 · integration · Medium confidence · [https://fly4future\.com/about\-us/](https://fly4future.com/about-us/)
- F7093 · business\_model · Medium confidence · [https://fly4future\.com/about\-us/](https://fly4future.com/about-us/)
- F7094 · team\_claim · Medium confidence · [https://fly4future\.com/about\-us/](https://fly4future.com/about-us/)
- F7095 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-coast\-guard\-and\-maritime\-security/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-coast-guard-and-maritime-security/)
- F7096 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-coast\-guard\-and\-maritime\-security/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-coast-guard-and-maritime-security/)
- F7097 · funding\_round · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-coast\-guard\-and\-maritime\-security/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-coast-guard-and-maritime-security/)
- F7098 · tech\_claim · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-coast\-guard\-and\-maritime\-security/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-coast-guard-and-maritime-security/)
- F7099 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-coast\-guard\-and\-maritime\-security/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-coast-guard-and-maritime-security/)
- F7100 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F7101 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F7102 · tech\_claim · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F7103 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F7104 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F7105 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F7106 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F7107 · product\_capability · Medium confidence · [https://fly4future\.com/development\-and\-prototyping/autonomous\-drones\-for\-security\-and\-defense\-applications/](https://fly4future.com/development-and-prototyping/autonomous-drones-for-security-and-defense-applications/)
- F7108 · funding\_round · Medium confidence · [https://cc\.cz/od\-univerzitniho\-projektu\-po\-milionove\-trzby\-ceske\-drony\-maji\-za\-ukol\-dorucit\-jidlo\-zachranit\-zivot\-i\-ockovat/](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
- F7109 · team\_claim · Medium confidence · [https://cc\.cz/od\-univerzitniho\-projektu\-po\-milionove\-trzby\-ceske\-drony\-maji\-za\-ukol\-dorucit\-jidlo\-zachranit\-zivot\-i\-ockovat/](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
- F7110 · product\_capability · Medium confidence · [https://cc\.cz/od\-univerzitniho\-projektu\-po\-milionove\-trzby\-ceske\-drony\-maji\-za\-ukol\-dorucit\-jidlo\-zachranit\-zivot\-i\-ockovat/](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
- F7111 · product\_capability · Medium confidence · [https://cc\.cz/od\-univerzitniho\-projektu\-po\-milionove\-trzby\-ceske\-drony\-maji\-za\-ukol\-dorucit\-jidlo\-zachranit\-zivot\-i\-ockovat/](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
- F7112 · market\_claim · Medium confidence · [https://cc\.cz/od\-univerzitniho\-projektu\-po\-milionove\-trzby\-ceske\-drony\-maji\-za\-ukol\-dorucit\-jidlo\-zachranit\-zivot\-i\-ockovat/](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
- F7113 · funding\_round · Medium confidence · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260414\-cesti\-vedci\-vytvorili\-letajici\-roj\-autonomnich\-dronu\-ted\-shani\-investory\-pro](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
- F7114 · product\_capability · Medium confidence · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260414\-cesti\-vedci\-vytvorili\-letajici\-roj\-autonomnich\-dronu\-ted\-shani\-investory\-pro](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
- F7115 · business\_model · Medium confidence · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260414\-cesti\-vedci\-vytvorili\-letajici\-roj\-autonomnich\-dronu\-ted\-shani\-investory\-pro](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
- F7116 · product\_capability · Medium confidence · [https://czechinvest\.gov\.cz/en/Key\-sectors/Smart\-mobility\-catalog/Firmy/Fly4Future](https://czechinvest.gov.cz/en/Key-sectors/Smart-mobility-catalog/Firmy/Fly4Future)
- F7117 · product\_capability · Medium confidence · [https://czechinvest\.gov\.cz/en/Key\-sectors/Smart\-mobility\-catalog/Firmy/Fly4Future](https://czechinvest.gov.cz/en/Key-sectors/Smart-mobility-catalog/Firmy/Fly4Future)
- F7118 · product\_capability · Medium confidence · [https://czechinvest\.gov\.cz/en/Key\-sectors/Smart\-mobility\-catalog/Firmy/Fly4Future](https://czechinvest.gov.cz/en/Key-sectors/Smart-mobility-catalog/Firmy/Fly4Future)
- F7119 · product\_capability · Medium confidence · [https://czechinvest\.gov\.cz/en/Key\-sectors/Smart\-mobility\-catalog/Firmy/Fly4Future](https://czechinvest.gov.cz/en/Key-sectors/Smart-mobility-catalog/Firmy/Fly4Future)
- F7120 · funding\_round · Medium confidence · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260615\-rozvoj\-dronu\-v\-cesku\-zajisti\-obdoba\-agentury\-darpa\-chytra\-armada\-a\-silni](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- F7121 · pricing · Medium confidence · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260615\-rozvoj\-dronu\-v\-cesku\-zajisti\-obdoba\-agentury\-darpa\-chytra\-armada\-a\-silni](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- F7122 · team\_claim · Medium confidence · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260615\-rozvoj\-dronu\-v\-cesku\-zajisti\-obdoba\-agentury\-darpa\-chytra\-armada\-a\-silni](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- F7123 · market\_claim · Medium confidence · [https://aktualne\.cvut\.cz/zpravy\-z\-medii/20260615\-rozvoj\-dronu\-v\-cesku\-zajisti\-obdoba\-agentury\-darpa\-chytra\-armada\-a\-silni](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- F7124 · product\_capability · Medium confidence · [https://24n\.cz/ru/cheshskie\-drony\-fly4future\-brosaiut\-vyzov\-dji\-investitsii\-avtonomnost](https://24n.cz/ru/cheshskie-drony-fly4future-brosaiut-vyzov-dji-investitsii-avtonomnost)
- F7125 · product\_capability · Medium confidence · [https://24n\.cz/ru/cheshskie\-drony\-fly4future\-brosaiut\-vyzov\-dji\-investitsii\-avtonomnost](https://24n.cz/ru/cheshskie-drony-fly4future-brosaiut-vyzov-dji-investitsii-avtonomnost)
- F7126 · product\_capability · Medium confidence · [https://24n\.cz/ru/cheshskie\-drony\-fly4future\-brosaiut\-vyzov\-dji\-investitsii\-avtonomnost](https://24n.cz/ru/cheshskie-drony-fly4future-brosaiut-vyzov-dji-investitsii-avtonomnost)
- F7127 · competitor · Medium confidence · [https://24n\.cz/ru/cheshskie\-drony\-fly4future\-brosaiut\-vyzov\-dji\-investitsii\-avtonomnost](https://24n.cz/ru/cheshskie-drony-fly4future-brosaiut-vyzov-dji-investitsii-avtonomnost)
- F7128 · patent · Sourced · [https://patents\.google\.com/patent/WO2024255934A1](https://patents.google.com/patent/WO2024255934A1)
- F7129 · patent · Sourced · [https://patents\.google\.com/patent/CZ38123U1](https://patents.google.com/patent/CZ38123U1)
- F7219 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/35675041](https://smlouvy.gov.cz/smlouva/35675041)
- F7220 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/40295245](https://smlouvy.gov.cz/smlouva/40295245)
- F7221 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/19719811](https://smlouvy.gov.cz/smlouva/19719811)
- F7222 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/34144825](https://smlouvy.gov.cz/smlouva/34144825)
- F7223 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/39232294](https://smlouvy.gov.cz/smlouva/39232294)
- F7224 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/36574813](https://smlouvy.gov.cz/smlouva/36574813)
- F7225 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/19121879](https://smlouvy.gov.cz/smlouva/19121879)
- F7226 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/7574923](https://smlouvy.gov.cz/smlouva/7574923)
- F7227 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/27109547](https://smlouvy.gov.cz/smlouva/27109547)
- F7228 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/32841120](https://smlouvy.gov.cz/smlouva/32841120)
- F7229 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/31970356](https://smlouvy.gov.cz/smlouva/31970356)
- F7230 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/34343605](https://smlouvy.gov.cz/smlouva/34343605)
- F7231 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/38841586](https://smlouvy.gov.cz/smlouva/38841586)
- F7232 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/29827008](https://smlouvy.gov.cz/smlouva/29827008)
- F7233 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/24070505](https://smlouvy.gov.cz/smlouva/24070505)
- F7234 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/35674989](https://smlouvy.gov.cz/smlouva/35674989)
- F7235 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/34185905](https://smlouvy.gov.cz/smlouva/34185905)
- F7236 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/31525264](https://smlouvy.gov.cz/smlouva/31525264)
- F7237 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/31349768](https://smlouvy.gov.cz/smlouva/31349768)
- F7238 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-626764B017A7D48762301C3BBCF51B77EF4E2FF0362556B110DCE874BA1EF74C](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-626764B017A7D48762301C3BBCF51B77EF4E2FF0362556B110DCE874BA1EF74C)
- F7239 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-127B688EB7C71F68F8B5623AD279B485ABC73F9A979C55EBB9F2003A34C3B860](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-127B688EB7C71F68F8B5623AD279B485ABC73F9A979C55EBB9F2003A34C3B860)
- F7240 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/Eufondy\-A343AC5697667DAB84AD59B38280DF203877839274398380C0D23A22FE0A524A](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-A343AC5697667DAB84AD59B38280DF203877839274398380C0D23A22FE0A524A)
- F7241 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/Eufondy\-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB)
- F7242 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-19EA131B86F2806299503139C5574083B486D0FB4418E14FA456E61D518DEBF0](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-19EA131B86F2806299503139C5574083B486D0FB4418E14FA456E61D518DEBF0)
- F7243 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7)
- F7244 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-61879203CFBA1CC5F2290E554298A735EE0E9CAB917E2CBF95B339FD4E8F5EC0](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-61879203CFBA1CC5F2290E554298A735EE0E9CAB917E2CBF95B339FD4E8F5EC0)
- F7245 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-F940343665E2F83FB3555FEDDE2A186490FEF16884132196B49785C0BFC8198B](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F940343665E2F83FB3555FEDDE2A186490FEF16884132196B49785C0BFC8198B)
- F7246 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3)
- F7247 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-CF5DF8A4A5754E462BAE3DC0E9AA74F43E459601A19D7B4F5A3D63CE2E20AB1F](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-CF5DF8A4A5754E462BAE3DC0E9AA74F43E459601A19D7B4F5A3D63CE2E20AB1F)
- F7248 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsRed\-07206B2AC7D190C9A62D3EEAF6DF1E71B23909A126D68EDD8753809AD243AB6E](https://www.hlidacstatu.cz/Dotace/Detail/IsRed-07206B2AC7D190C9A62D3EEAF6DF1E71B23909A126D68EDD8753809AD243AB6E)
- F7249 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsRed\-F727F0B0BD373F910CA65A6D1E8DFA930B310A55DDF46B35EDC9CB6BAB703678](https://www.hlidacstatu.cz/Dotace/Detail/IsRed-F727F0B0BD373F910CA65A6D1E8DFA930B310A55DDF46B35EDC9CB6BAB703678)
- F7250 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsRed\-37A83AF70D3FE63FF340AB3B10AA7C81DB506E365757E39284777341A4FEB04A](https://www.hlidacstatu.cz/Dotace/Detail/IsRed-37A83AF70D3FE63FF340AB3B10AA7C81DB506E365757E39284777341A4FEB04A)
- F7251 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-C37E481DFF08F9C6D7DB0A6EB8DB96B80DAA067EE0CFD31F35DF85D5957BA882](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-C37E481DFF08F9C6D7DB0A6EB8DB96B80DAA067EE0CFD31F35DF85D5957BA882)
- F7252 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-EE07FCF6B7C9FF8F4928356BD995816A7A7C83F7EBC7C338F75AA9B4A43EA8AB](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-EE07FCF6B7C9FF8F4928356BD995816A7A7C83F7EBC7C338F75AA9B4A43EA8AB)
- F7253 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsRed\-E332C035F3D7296B55732B460CCCF307E362F565922E97AA9D12B4BBF4ADF351](https://www.hlidacstatu.cz/Dotace/Detail/IsRed-E332C035F3D7296B55732B460CCCF307E362F565922E97AA9D12B4BBF4ADF351)
- F7254 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-B1AA076CD28C1E5A7BEAC413845C3D70E2B2E687CEFEB55E6B422C33D6E62183](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-B1AA076CD28C1E5A7BEAC413845C3D70E2B2E687CEFEB55E6B422C33D6E62183)
- F7255 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsRed\-1519DD96B678357B9D64C4CFA5227A954A6802FB013965917E738271A27B106E](https://www.hlidacstatu.cz/Dotace/Detail/IsRed-1519DD96B678357B9D64C4CFA5227A954A6802FB013965917E738271A27B106E)
- F7256 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-FABB6D47509E746A7D3236D2A5CED6AEE7342716CA15492D85681B97AE506BD8](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-FABB6D47509E746A7D3236D2A5CED6AEE7342716CA15492D85681B97AE506BD8)
- F7257 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-9C717B54B2622718D226FA630A14F049D620A56B273EA1F0D08011E5E084B9A7](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-9C717B54B2622718D226FA630A14F049D620A56B273EA1F0D08011E5E084B9A7)
- F7258 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-0BB20EACD417951BEDBEE8CB242827A16521DF3F26B31BD25693E45B738FFF35](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-0BB20EACD417951BEDBEE8CB242827A16521DF3F26B31BD25693E45B738FFF35)
- F7259 · grant\_national · Sourced · [https://smlouvy\.gov\.cz/smlouva/28082567](https://smlouvy.gov.cz/smlouva/28082567)
- F7260 · grant\_national · Sourced · [https://smlouvy\.gov\.cz/smlouva/32902152](https://smlouvy.gov.cz/smlouva/32902152)
- F7261 · grant\_eu · Sourced · [https://cordis\.europa\.eu/project/id/101071270](https://cordis.europa.eu/project/id/101071270)
- F7262 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F7267 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7268 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7269 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7270 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7271 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7272 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7273 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7274 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7275 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7276 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7277 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7278 · peer\_company · Medium confidence · [https://web\.archive\.org/web/20261029165007id\_/https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
- F7279 · source\_check · Checked · [https://www\.diana\.nato\.int/about\-diana/2026\-cohort\-of\-companies\.html](https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
