# Fly4Future — due diligence brief

fly4future\.com · Fly4Future s\.r\.o\. · IČO 06632581 · CZ · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** Fly4Future develops autonomous multirobot UAV platforms and sells drones and integration services to industry, research labs and public research partners\. *(Partly verified)* ^[1](https://fly4future.com/custom-drones/we-help-you-to-establish-flying-robots-research-lab/),[2](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[3](https://smlouvy.gov.cz/smlouva/31525264),[4](https://smlouvy.gov.cz/smlouva/27109547),[5](https://fly4future.com/development-and-prototyping/autonomous-drones-for-coast-guard-and-maritime-security/)
- **Stage & traction.** Multiple R&amp;D grants and collaborative public\-project contracts \(large TAČR/OP TAK awards\) and university partners; early commercial purchase contracts with public bodies are small\. *(Verified)* ^[6](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[7](https://smlouvy.gov.cz/smlouva/34343605),[8](https://smlouvy.gov.cz/smlouva/24070505),[9](https://smlouvy.gov.cz/smlouva/35675041),[4](https://smlouvy.gov.cz/smlouva/27109547)
- **Technology & moat.** Modest—public patent applications and active OSS ROS\-based stack plus swarm/autonomy repos provide reproducible building blocks, but independent proof of superior autonomy is limited in public evidence\. *(Verified)* ^[10](https://patents.google.com/patent/WO2024255934A1),[11](https://patents.google.com/patent/CZ38123U1),[12](https://github.com/fly4future/argentswarm_core),[13](https://github.com/fly4future/iroc_fleet_manager),[14](https://github.com/fly4future/iroc_bridge)
- **Key risk.** Revenue and program concentration toward public R&amp;D and university collaborations could leave limited commercial reference customers and uncertain unit\-economics at scale\. *(Analyst view)* ^[6](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[7](https://smlouvy.gov.cz/smlouva/34343605),[9](https://smlouvy.gov.cz/smlouva/35675041),[8](https://smlouvy.gov.cz/smlouva/24070505)
- **Diligence focus.** First: verify autonomous navigation performance and flight\-test logs \(GPS‑free claims\) because product claims drive market differentiation and manufacturability assumptions\. *(Analyst view)* ^[15](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[12](https://github.com/fly4future/argentswarm_core),[2](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2026\-10\-16 · 10 až 16 milionů eur; date n/a · investor search &amp; European funds financing · 100 milionů korun \+ 100 milionů korun \+ 4\-5 milionů eur · neupřesněná firma, Sprind \(agentura\); date n/a · Series A · 8 million euros | 16, 17, 18 |
| Public money | 17 contract\(s\) in the contract register; 18 grant project\(s\) awarded 138\.4M CZK \+ 1 without published amount, 32\.7M CZK paid so far · by kind: 2 purchase\(s\) by public buyers \(755,152 CZK\); 12 R&amp;D project agreement\(s\), amounts are project budgets, not revenue; 3 other \(1\.3M CZK\) · counterparties: Správa informačních technologií města Plzně, Eurosecur s\. r\. o\., VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ, České vysoké učení technické v Praze | 19, 20, 21, 8, 4, 22 |
| Thesis fit \(Rockaway\) | sectors: deep tech \(30 facts\); AI\-led transformative tech \(23 facts\); industrial / manufacturing AI \(15 facts\); defence / dual\-use \(6 facts\); energy \(4 facts\) · geography: CZ \(core region\) · overlaps portfolio: Vermeer \(defence, drone, navigat\) | 23, 24, 25 |
| Hiring | 3 open roles: engineering 2, sales gtm 1 | 26, 27, 28 |
| Engineering footprint | 15 public repos \(6★, last push 2026\-11\-09\); 11 subdomains; 1 docs pages; stack: Apache, Divi v\.4\.27\.9, WordPress | 29, 30, 31, 1 |
| Customers | public pricing: yes | 32 |
| Timeline | Czech entity registered 2017\-11\-27; first press 2026\-06\-15 \(16 articles collected\) | 33, 34 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the market, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** Fly4Future matches Rockaway theses in deep\-tech autonomy, industrial/mfg AI and defence/dual\-use \(claims of GPS‑free flight, swarm autonomy and academic spinout pedigree\)\. *(Analyst view)* ^[23](https://www.cnaip.cz/en/entity/fly4future),[24](https://fel.cvut.cz/en/what-s-on/news/36454-ctu-spinout-fly4future-wins-prestigious-ai-company-of-the-year-award-at-ai-awards-2024),[15](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[12](https://github.com/fly4future/argentswarm_core),[35](https://fly4future.com/about-us/)
  - Assumption: Company claims reflect product capability\.
- **Portfolio overlap:** Vermeer \(vision\-based GPS\-free navigation for drones\) appears complementary rather than direct conflict; both target GPS\-free navigation and defence/dual\-use buyers, suggesting possible synergy on sensor/navigation stacks\. *(Analyst view)* ^[15](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[12](https://github.com/fly4future/argentswarm_core),[23](https://www.cnaip.cz/en/entity/fly4future)
  - Assumption: Vermeer’s presence in fund portfolio is relevant to Fly4Future’s GPS\-free claim\.

## Business model

- Direct product sales: company lists unit pricing \~1\.5M Kč per advanced drone \(high\-value platform sales\)\. *(Analyst view)* ^[32](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
  - Assumption: Pricing reflects current commercial offering\.
- Public\-sector R&amp;D and purchase revenue: multiple national R&amp;D contracts and two recorded public purchase contracts \(examples: 3D laser scanner sale and university orders\)\. *(Analyst view)* ^[8](https://smlouvy.gov.cz/smlouva/24070505),[4](https://smlouvy.gov.cz/smlouva/27109547),[36](https://smlouvy.gov.cz/smlouva/38841586)
  - Assumption: Contract entries indicate paid work or deliveries\.
- Substantial grant funding: participant in Horizon Europe AeroSTREAM and several Czech TAČR/IsVavai grants supporting multi‑robot autonomy and industry projects\. *(Analyst view)* ^[37](https://cordis.europa.eu/project/id/101071270),[6](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[38](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-61879203CFBA1CC5F2290E554298A735EE0E9CAB917E2CBF95B339FD4E8F5EC0)
  - Assumption: Grants fund R&amp;D separate from commercial revenue\.

## Market

- Fly4Future claims industrial and civilian demand for GPS‑free flight; they report industrial partners and media note plans for mass production and export focus\. *(Analyst view)* ^[15](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[2](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[39](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890)
  - Assumption: Company and press reporting reflect real partner interest\.
- Company positions products for defence/dual‑use surveillance, industrial inspection, precision agriculture and delivery use\-cases \(stated in press and project descriptions\)\. *(Analyst view)* ^[2](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[40](https://smlouvy.gov.cz/smlouva/32841120),[41](https://smlouvy.gov.cz/smlouva/31970356)
  - Assumption: Project descriptions map to target verticals\.

## Competition

- Alpha Autonomy \(NATO DIANA cohort\): offers autonomous UAV swarms in contested environments — overlaps on swarm autonomy and denied‑GPS use\-cases \(found in DIANA cohort list\)\. *(Analyst view)* ^[42](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[15](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
  - Assumption: DIANA descriptions reflect product focus\.
- Arke Telekom \(NATO DIANA\): builds resilient comms/architecture for GNSS‑free tactical drone ops — direct technical overlap on GNSS‑free operations\. *(Analyst view)* ^[43](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[15](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
  - Assumption: Both target GNSS‑free capabilities\.
- Marble Aerospace \(NATO DIANA\): autonomous UAV fleets for rapid ISR — overlaps on fleet/mission orchestration and rapid deployable ISR concepts\. *(Analyst view)* ^[44](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[13](https://github.com/fly4future/iroc_fleet_manager)
  - Assumption: Fleet software capabilities are comparable\.
- Mara \(NATO DIANA\): counter‑drone/defensive systems targeting swarm threats — competitive from the defence protection side rather than platform manufacturing\. *(Analyst view)* ^[45](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html)
  - Assumption: Defensive systems compete for defence budgets\.

## Case for and against

- **For:** Strong technical base and IP — CTU spinout with multiple autonomy repos, swarm stack and patent publications supporting unique capabilities\. *(Analyst view)* ^[35](https://fly4future.com/about-us/),[12](https://github.com/fly4future/argentswarm_core),[10](https://patents.google.com/patent/WO2024255934A1)
  - Assumption: Academic spinout tech is productisable\.
- **For:** Diversified public funding and contracts de‑risks R&amp;D: Horizon Europe participation and multiple TAČR/IsVavai grants and public contracts\. *(Analyst view)* ^[37](https://cordis.europa.eu/project/id/101071270),[6](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[3](https://smlouvy.gov.cz/smlouva/31525264)
  - Assumption: Grants materially fund development roadmap\.
- **Against:** Capital intensity and scale plan — company publicly seeks €10–16M and separately mentions larger public/corporate budget lines for serial production, implying heavy capex and execution risk\. *(Analyst view)* ^[16](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[17](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro),[25](https://adoptimal.cz/magazin/aktualita/fly4future-chysta-vyrobu-desitek-tisic-autonomnich-dronu-rocne)
  - Assumption: Raised amount is needed for planned scaling\.
- **Against:** Commercial traction unclear — pricing and press indicate unit economics, but named commercial customers beyond academic/public partners are limited in supplied facts\. *(Analyst view)* ^[32](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni),[8](https://smlouvy.gov.cz/smlouva/24070505),[4](https://smlouvy.gov.cz/smlouva/27109547)
  - Assumption: Public contracts do not equal broad commercial demand\.
- **Must be true:** Product‑level validation with paying commercial/defence customers at scale — confirm repeat orders or signed purchase contracts beyond R&amp;D collaborations\. *(Analyst view)* ^[8](https://smlouvy.gov.cz/smlouva/24070505),[36](https://smlouvy.gov.cz/smlouva/38841586),[32](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
  - Assumption: Purchase contracts indicate commercial product fit\.
- **Must be true:** Manufacturing and supply‑chain plan to reach tens‑of‑thousands volumes \(or credible intermediary milestones\) given public production claims and unit price\. *(Analyst view)* ^[2](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[39](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890),[32](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
  - Assumption: Press production claims require supply‑chain validation\.

# Technical due diligence

## Ownership and capital

- Incorporation and filings: Fly4Future s\.r\.o\. incorporated 2017\-11\-27 with registry filings and recent annual accounts on file\. *(Verified)* ^[46](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581),[33](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581),[47](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- Funding signals: multiple press reports describe fundraising activity and rounds being sought \(10–16M EUR round and other stated targets\)\. *(Corroborated)* ^[16](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[17](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro),[18](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- Public money: numerous grants and contracts \(see TAČR and other national/EU awards\); both purchase contracts \(2\) and many R&amp;D project agreements and subsidy agreements present\. *(Verified)* ^[37](https://cordis.europa.eu/project/id/101071270),[6](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[8](https://smlouvy.gov.cz/smlouva/24070505),[9](https://smlouvy.gov.cz/smlouva/35675041),[48](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-19EA131B86F2806299503139C5574083B486D0FB4418E14FA456E61D518DEBF0)

## Technology profile

- Product surfaces and code: public GitHub with ROS nodes, fleet manager, mission handler and swarm core indicating in\-house autonomy development\. *(Verified)* ^[14](https://github.com/fly4future/iroc_bridge),[13](https://github.com/fly4future/iroc_fleet_manager),[12](https://github.com/fly4future/argentswarm_core),[49](https://github.com/fly4future/iroc_mission_handler),[50](https://github.com/fly4future/webrtc_ros)
- Engineering footprint: 15 public repos \(active pushes through 2026\-11\), one docs page and website; site uses WordPress/Divi and Google Analytics\. *(Partly verified)* ^[51](https://github.com/fly4future/install_script),[1](https://fly4future.com/custom-drones/we-help-you-to-establish-flying-robots-research-lab/),[52](https://fly4future.com/),[53](https://fly4future.com/),[54](https://fly4future.com/privacy-policy/)
- AI dependency: no verified LLM vendor dependency or own\-model HF evidence in facts; autonomy appears robotics/ROS‑centric rather than LLM\-reliant\. *(Verified)* ^[12](https://github.com/fly4future/argentswarm_core),[13](https://github.com/fly4future/iroc_fleet_manager),[14](https://github.com/fly4future/iroc_bridge)

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** ROS\-based mission handler, fleet manager and WebRTC ROS bridges are public and could be reproduced using ROS, C\+\+/Python and WebRTC libraries\. *(Analyst view)* ^[49](https://github.com/fly4future/iroc_mission_handler),[13](https://github.com/fly4future/iroc_fleet_manager),[50](https://github.com/fly4future/webrtc_ros)
  - Assumption: Public repos include functional, buildable code and documentation\.
- **Edge supported by public evidence:** Patent applications and EU Horizon participation provide documented IP and funded research roles, showing formal R&amp;D outputs rather than commercial dominance\. *(Analyst view)* ^[10](https://patents.google.com/patent/WO2024255934A1),[11](https://patents.google.com/patent/CZ38123U1),[37](https://cordis.europa.eu/project/id/101071270)
  - Assumption: Patent publications and EU project listing reflect unique R&amp;D deliverables\.
- **Cannot be judged from outside:** Real\-world autonomy robustness, production\-grade hardware readiness and end\-to\-end safety/performance cannot be judged from repos, patents or press alone\. *(Analyst view)* ^[12](https://github.com/fly4future/argentswarm_core),[2](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
  - Assumption: Operational metrics and manufacturing QA are not publicly posted\.

## Risks and caveats

- High public\-R&amp;D concentration: multiple large TAČR and national grants and project contracts represent a substantial funding/engagement source versus confirmed commercial buyers\. *(Analyst view)* ^[6](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[7](https://smlouvy.gov.cz/smlouva/34343605),[38](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-61879203CFBA1CC5F2290E554298A735EE0E9CAB917E2CBF95B339FD4E8F5EC0),[3](https://smlouvy.gov.cz/smlouva/31525264)
  - Assumption: Grant/contract portfolio materially supports current R&amp;D budget\.
- Unverified performance claims: GPS‑free and NDAA‑compliant platform statements exist as company claims but lack independent flight\-test evidence in public records\. *(Analyst view)* ^[15](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[55](https://fly4future.com/),[12](https://github.com/fly4future/argentswarm_core)
  - Assumption: Public repos and press do not include independent test reports\.
- Manufacturing scaling gap: press statements on large\-scale production lack corroborating supply‑chain or manufacturing\-capacity evidence in technical or contracts data\. *(Analyst view)* ^[25](https://adoptimal.cz/magazin/aktualita/fly4future-chysta-vyrobu-desitek-tisic-autonomnich-dronu-rocne),[51](https://github.com/fly4future/install_script),[2](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)
  - Assumption: No supplier/manufacturing contracts are posted in facts\.

## Questions for founders

- Provide independent flight\-test logs and metrics proving GPS‑free navigation performance cited in press\. *(Analyst view)* ^[15](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[12](https://github.com/fly4future/argentswarm_core)
  - Assumption: Logs would show repeatable performance under contested conditions\.
- Share customer purchase contracts and references beyond research partners to validate commercial demand behind cited pricing \(1\.5M Kč\) and scale claims\. *(Analyst view)* ^[32](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni),[8](https://smlouvy.gov.cz/smlouva/24070505),[9](https://smlouvy.gov.cz/smlouva/35675041)
  - Assumption: Commercial purchase contracts exist separate from RD projects\.
- Detail manufacturing readiness: suppliers, BOM, and any signed manufacturing or supply agreements supporting tens\-of\-thousands production claims\. *(Analyst view)* ^[25](https://adoptimal.cz/magazin/aktualita/fly4future-chysta-vyrobu-desitek-tisic-autonomnich-dronu-rocne),[51](https://github.com/fly4future/install_script)
  - Assumption: Press claims imply planned high\-volume manufacturing\.
- Validate NDAA\-compliance claim with bill\-of\-materials audit or third‑party compliance report referenced on site\. *(Analyst view)* ^[55](https://fly4future.com/)
  - Assumption: Compliance requires component\-level evidence\.

## Sources

1. [fly4future\.com](https://fly4future.com/custom-drones/we-help-you-to-establish-flying-robots-research-lab/) · Company's own website · Website page — “We Help You to Establish Flying Robots’ Research/Lab \| Fly4Future”
2. [cc\.cz](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/) · Independent press · Press article · 2026\-10\-16 — “Drony budou nosit jídlo i očkovat krávy\. Díky české technologii \- CzechCrunch”
3. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/31525264) · Official record · Public contract · 2024\-12\-17 — “České vysoké učení technické v Praze · 6 839 513 CZK · Smlouva o účasti na řešení projektuTQ15000370”
4. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/27109547) · Official record · Public contract · 2024\-01\-01 — “VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ · 2 400 000 CZK · SMLOUVA O ÚČASTI NA ŘEŠENÍ PROJEKTU A O VYUŽITÍ VÝSLEDKŮ”
5. [fly4future\.com](https://fly4future.com/development-and-prototyping/autonomous-drones-for-coast-guard-and-maritime-security/) · Company's own website · Funding round — “The smart sensory buoy solution was developed within the Koldro project in collaboration with Eurosecur \. The project was supported by the Ministry of Industry and Trade of the Czech Republic, funded by the European Union’s Horizon Europe research and innovation program under grant agreement No\. 101071270\.”
6. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3) · Official record · National grant · 2025 — “Multi\-robotický letecký systém pro autonomní bezpečnostní dohled a inspekci rozlehlých průmyslových objektů odolný vůči výpadku komunikace a signálu GNSS · Technologická agentura ČR · 21 826 349 CZK”
7. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/34343605) · Official record · Public contract · 2025\-07\-25 — “České vysoké učení technické v Praze · 12 270 000 CZK · SMLOUVA O ÚČASTI NA ŘEŠENÍ PROJEKTU A O VYUŽITÍ VÝSLEDKŮ OZ01020024”
8. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/24070505) · Official record · Public contract · 2023\-04\-12 — “VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ · 658 829 CZK · Kupní smlouva \- Senzorický systém pro mobilní roboty – 3D laserové skenery”
9. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/35675041) · Official record · Public contract · 2025\-11\-19 — “Česká agentura na podporu obchodu · 87 120 CZK · Smlouva o spolupráci Design”
10. [patents\.google\.com](https://patents.google.com/patent/WO2024255934A1) · Official record · Patent publication — “WO2024255934A1 · Method of marking bark beetle infested trees and means for executing this … · Fly4Future s\.r\.o\.”
11. [patents\.google\.com](https://patents.google.com/patent/CZ38123U1) · Official record · Patent publication — “CZ38123U1 · A drone sprayer · Fly4Future s\.r\.o\.”
12. [github\.com](https://github.com/fly4future/argentswarm_core) · Public technical artifact · GitHub repository · 2026\-10\-22 — “fly4future/argentswarm\_core · Digest of the swarm autonomy software at f4f\. · C\+\+ · last push 2026\-10\-22”
13. [github\.com](https://github.com/fly4future/iroc_fleet_manager) · Public technical artifact · GitHub repository · 2026\-10\-30 — “fly4future/iroc\_fleet\_manager · ROS node for handling fleet mission execution, part of the "IROC\_Core" package\. · C\+\+ · last push 2026\-10\-30”
14. [github\.com](https://github.com/fly4future/iroc_bridge) · Public technical artifact · GitHub repository · 2026\-10\-30 — “fly4future/iroc\_bridge · Node to translate messages from ROS to backend and back · C\+\+ · last push 2026\-10\-30”
15. [fly4future\.com](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/) · Company's own website · Market statement — “Thanks to our participation in the competition, we have created a truly unique system that is already in demand by clients\. Several industrial partners are now focusing on flying without GPS , so this is a very hot topic now that not only the defence industry but also the civilian industry is aware of\.”
16. [cc\.cz](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/) · Independent press · Funding round — “Fly4future proto nyní od investorů žádá 10 až 16 milionů eur, tedy zhruba 244 až 390 milionů korun\.”
17. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro) · Independent press · Funding round — “Od jedné firmy už máme příslib přes 100 milionů korun\. K tomu plánujeme získat dalších 100 milionů z evropských fondů\. To je budget, který potřebuji na vybudování týmu\. V úterý jedu do Německa jednat s agenturou Sprind, která by nám mohla zprostředkovat investici kolem čtyř až pěti milionů eur na vývoj autonomních rojů”
18. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni) · Independent press · Funding round — “Bereme to už jako Series A, protože máme produkt a kontrakty\. Potřebujeme zatím pro jeden projekt získat osm milionů eur \(necelých 200 milionů korun – pozn\. red\.\)\.”
19. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/7574923) · Official record · Public contract · 2018\-12\-05 — “Správa informačních technologií města Plzně · 592 900 CZK · smlouva o obchodní spoluporáci”
20. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/19121879) · Official record · Public contract · 2022\-01\-17 — “Eurosecur s\. r\. o\. · 74 624 392 CZK · Dohoda o vypořádání závazků z neuveřejněné smlouvy o spolupráci na řešení projektu „Univerzální systém kolaborativních dronů"”
21. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/19719811) · Official record · Public contract · 2022\-02\-28 — “Správa informačních technologií města Plzně · 589 270 CZK · Smlouva o obchodní spolupráci”
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
32. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni) · Independent press · Pricing — “Nějakých 70 až 80 kusů ročně\. Jde ale o stroje až za 1,5 milionu korun s velkou přidanou hodnotou\.”
33. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581) · Official record · Registry: incorporation · 2017\-11\-27 — “registered 2017\-11\-27”
34. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/en/media-screenings/20260615-the-development-of-drones-in-the-czech-republic-will-be-ensured-by-a-darpa) · Independent press · Press article · 2026\-06\-15 — “The development of drones in the Czech Republic will be ensured by a DARPA\-like agency, a smart army and strong investors \- News service \- Czech technical university in Prague”
35. [fly4future\.com](https://fly4future.com/about-us/) · Company's own website · Team claim — “Fly4Future was formed in 2017 as a spinout of the Multi\-Robot Systems group at the Czech Technical University in Prague \(MRS CTU\)”
36. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/38841586) · Official record · Public contract · 2026\-07\-17 — “Vysoká škola báňská \- Technická univerzita Ostrava · 96 323 CZK · Objednávka: konzultace pro vývoj dronové platformy”
37. [cordis\.europa\.eu](https://cordis.europa.eu/project/id/101071270) · Official record · EU grant · 2022\-07\-01 — “Strengthening Research and Innovation Excellence in Autonomous Aerial Systems”
38. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-61879203CFBA1CC5F2290E554298A735EE0E9CAB917E2CBF95B339FD4E8F5EC0) · Official record · National grant · 2025 — “Multirobotický systém pro autonomní terénní operace s vícezdrojovou navigací · Technologická agentura ČR · 6 000 000 CZK”
39. [e15\.cz](https://www.e15.cz/byznys/cesi-chteji-narusit-cinskou-nadvladu-nad-drony-chystaji-vyrobu-desetitisicu-kusu-rocne-1434890) · Independent press · Press article · 2026\-08\-12 — “Češi chtějí narušit čínskou nadvládu nad drony\. Chystají výrobu desetitisíců kusů ročně \| e15\.cz”
40. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/32841120) · Official record · Public contract · 2025\-04\-04 — “České vysoké učení technické v Praze · 0 CZK · Projekt FW12010288: Multi\-robotický letecký systém pro autonomní bezpečnostní dohled a inspekci rozlehlých průmyslových objektů odolný vůči výpadku komunikace a signálu GNSS”
41. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/31970356) · Official record · Public contract · 2025\-01\-23 — “Jihočeská univerzita v Českých Budějovicích · 9 000 723 CZK · Smlouva o účasti na řešení projektu \- „Udržitelné zemědělství: Energeticky výkonné bezpilotní technologie pro precizní zemědělství" \- oprava metadat, ceny”
42. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Alpha Autonomy: AI\-powered autonomous UAV swarms for resilient, low\-altitude ISR in denied &amp; contested environments”
43. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Arke Telekom Mühendislik Elektronik Sanayi Ticaret Ltd\. Şti: Resilient, autonomous communication architecture for GNSS\-free tactical drone operations”
44. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Marble Aerospace Limited: Fleets of high\-speed UAVs with autonomous robotic hangars to create rapidly deployable “ISR bubbles””
45. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Mara: Simultaneous 360° protection against swarms of 48\+ EW\-resistant drones at 1/20th the cost\.”
46. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581) · Official record · Registry: identity · 2017\-11\-27 — “Fly4Future s\.r\.o\. · s\.r\.o\. · registered 2017\-11\-27”
47. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597) · Official record · Registry: filed document · 2025\-07\-23
48. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-19EA131B86F2806299503139C5574083B486D0FB4418E14FA456E61D518DEBF0) · Official record · National grant · 2024 — “Univerzální systém kolaborativních robotů · Ministerstvo průmyslu a obchodu · 6 711 348 CZK”
49. [github\.com](https://github.com/fly4future/iroc_mission_handler) · Public technical artifact · GitHub repository · 2026\-10\-30 — “fly4future/iroc\_mission\_handler · Action server component that manages drone flight through desired waypoints\. · C\+\+ · last push 2026\-10\-30”
50. [github\.com](https://github.com/fly4future/webrtc_ros) · Public technical artifact · GitHub repository · 2026\-05\-12 — “fly4future/webrtc\_ros · Streaming of ROS Image Topics using WebRTC · C\+\+ · last push 2026\-05\-12”
51. [github\.com](https://github.com/fly4future/install_script) · Public technical artifact · GitHub repository · 2026\-11\-09 — “fly4future/install\_script · Shell · last push 2026\-11\-09”
52. [fly4future\.com](https://fly4future.com/) · Public technical artifact · Technology detected
53. [fly4future\.com](https://fly4future.com/) · Public technical artifact · Technology detected
54. [fly4future\.com](https://fly4future.com/privacy-policy/) · Company's own website · Subprocessor \(privacy policy\) — “We use Google Analytics to track this information\. Find out how Google uses your data at”
55. [fly4future\.com](https://fly4future.com/) · Company's own website · Technical claim — “All of our UAV platforms are fully capable of meeting NDAA compliance , ensuring that our products are free from components sourced from prohibited manufacturers as outlined in Section 889 of the U\.S\. National Defense Authorization Act \(NDAA\)”
56. [ec\.europa\.eu](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/org-details/887136005) · Official record · EU grant — “Strengthening Research and Innovation Excellence in Autonomous Aerial Systems”
57. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7) · Official record · National grant · 2021 — “Univerzální systém kolaborativních dronů · Ministerstvo průmyslu a obchodu · 10 279 779 CZK”
58. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Drone City: Heavy\-lift UAV with advanced autonomy for extreme environments”
59. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Volta Space Technologies: Persistent drone flight and emergency power in extremely cold environments”
60. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “AegisX: Detecting &amp; tracking low flying fibre optic drones”
61. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “OLEDCOMM: Stealth in drone flight\. Unjammable connectivity by light”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 22 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 35 | starfos |
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

Analysis: gpt\-5\-mini (cost $0.0247); AI extraction cost $0.0080. Full fact table: CSV export.

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
- F7739 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/35675041](https://smlouvy.gov.cz/smlouva/35675041)
- F7740 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/40295245](https://smlouvy.gov.cz/smlouva/40295245)
- F7741 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/19719811](https://smlouvy.gov.cz/smlouva/19719811)
- F7742 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/34144825](https://smlouvy.gov.cz/smlouva/34144825)
- F7743 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/39232294](https://smlouvy.gov.cz/smlouva/39232294)
- F7744 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/36574813](https://smlouvy.gov.cz/smlouva/36574813)
- F7745 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/19121879](https://smlouvy.gov.cz/smlouva/19121879)
- F7746 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/7574923](https://smlouvy.gov.cz/smlouva/7574923)
- F7747 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/27109547](https://smlouvy.gov.cz/smlouva/27109547)
- F7748 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/32841120](https://smlouvy.gov.cz/smlouva/32841120)
- F7749 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/31970356](https://smlouvy.gov.cz/smlouva/31970356)
- F7750 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/34343605](https://smlouvy.gov.cz/smlouva/34343605)
- F7751 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/38841586](https://smlouvy.gov.cz/smlouva/38841586)
- F7752 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/29827008](https://smlouvy.gov.cz/smlouva/29827008)
- F7753 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/24070505](https://smlouvy.gov.cz/smlouva/24070505)
- F7754 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/31525264](https://smlouvy.gov.cz/smlouva/31525264)
- F7755 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/31349768](https://smlouvy.gov.cz/smlouva/31349768)
- F7756 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-626764B017A7D48762301C3BBCF51B77EF4E2FF0362556B110DCE874BA1EF74C](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-626764B017A7D48762301C3BBCF51B77EF4E2FF0362556B110DCE874BA1EF74C)
- F7757 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/Eufondy\-A871230311380E8E9DC4DA2B151CF2A79BE8344CCA002B0170A09AD003BAA291](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-A871230311380E8E9DC4DA2B151CF2A79BE8344CCA002B0170A09AD003BAA291)
- F7758 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/Eufondy\-A343AC5697667DAB84AD59B38280DF203877839274398380C0D23A22FE0A524A](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-A343AC5697667DAB84AD59B38280DF203877839274398380C0D23A22FE0A524A)
- F7759 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/Eufondy\-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB)
- F7760 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-19EA131B86F2806299503139C5574083B486D0FB4418E14FA456E61D518DEBF0](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-19EA131B86F2806299503139C5574083B486D0FB4418E14FA456E61D518DEBF0)
- F7761 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7)
- F7762 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-61879203CFBA1CC5F2290E554298A735EE0E9CAB917E2CBF95B339FD4E8F5EC0](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-61879203CFBA1CC5F2290E554298A735EE0E9CAB917E2CBF95B339FD4E8F5EC0)
- F7763 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-F940343665E2F83FB3555FEDDE2A186490FEF16884132196B49785C0BFC8198B](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F940343665E2F83FB3555FEDDE2A186490FEF16884132196B49785C0BFC8198B)
- F7764 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3)
- F7765 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-9C717B54B2622718D226FA630A14F049D620A56B273EA1F0D08011E5E084B9A7](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-9C717B54B2622718D226FA630A14F049D620A56B273EA1F0D08011E5E084B9A7)
- F7766 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsRed\-F727F0B0BD373F910CA65A6D1E8DFA930B310A55DDF46B35EDC9CB6BAB703678](https://www.hlidacstatu.cz/Dotace/Detail/IsRed-F727F0B0BD373F910CA65A6D1E8DFA930B310A55DDF46B35EDC9CB6BAB703678)
- F7767 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-C37E481DFF08F9C6D7DB0A6EB8DB96B80DAA067EE0CFD31F35DF85D5957BA882](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-C37E481DFF08F9C6D7DB0A6EB8DB96B80DAA067EE0CFD31F35DF85D5957BA882)
- F7768 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-EE07FCF6B7C9FF8F4928356BD995816A7A7C83F7EBC7C338F75AA9B4A43EA8AB](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-EE07FCF6B7C9FF8F4928356BD995816A7A7C83F7EBC7C338F75AA9B4A43EA8AB)
- F7769 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-B1AA076CD28C1E5A7BEAC413845C3D70E2B2E687CEFEB55E6B422C33D6E62183](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-B1AA076CD28C1E5A7BEAC413845C3D70E2B2E687CEFEB55E6B422C33D6E62183)
- F7770 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-FABB6D47509E746A7D3236D2A5CED6AEE7342716CA15492D85681B97AE506BD8](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-FABB6D47509E746A7D3236D2A5CED6AEE7342716CA15492D85681B97AE506BD8)
- F7771 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-0BB20EACD417951BEDBEE8CB242827A16521DF3F26B31BD25693E45B738FFF35](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-0BB20EACD417951BEDBEE8CB242827A16521DF3F26B31BD25693E45B738FFF35)
- F7772 · grant\_national · Sourced · [https://smlouvy\.gov\.cz/smlouva/35674989](https://smlouvy.gov.cz/smlouva/35674989)
- F7773 · grant\_eu · Sourced · [https://cordis\.europa\.eu/project/id/101071270](https://cordis.europa.eu/project/id/101071270)
- F7774 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
