# Fly4Future — due diligence brief

fly4future\.com · Fly4Future s\.r\.o\. · IČO 06632581 · CZ · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** Sells autonomous drones, company\-claimed to fly without GPS, at up to 1\.5M CZK per unit; contract counterparties are mostly universities\. *(Verified)* ^[1](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni),[2](https://aktualne.cvut.cz/en/media-screenings/20260813-the-czechs-want-to-disrupt-chinas-dominance-over-drones-they-plan-to),[3](https://smlouvy.gov.cz/smlouva/24070505)
- **Stage & traction.** No closed round is evidenced; three raises are sought\. Public money is R&amp;D\-heavy: 12 R&amp;D agreements versus 2 purchase contracts\. No public\-sector listing check is supplied\. *(Verified)* ^[4](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[5](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro),[6](https://smlouvy.gov.cz/smlouva/38841586),[3](https://smlouvy.gov.cz/smlouva/24070505)
- **Technology & moat.** Public code is ROS\-based mission and bridge software, and the two patent filings are not granted\. Little is publicly hard to copy; the swarm autonomy code is not public\. *(Verified)* ^[7](https://github.com/fly4future/iroc_bridge),[8](https://github.com/fly4future/argentswarm_core),[9](https://patents.google.com/patent/WO2024255934A1),[10](https://patents.google.com/patent/CZ38123U1)
- **Key risk.** The unclosed 10\-16M EUR round sits above the fund's 0\.5\-2M initial ticket, so the investment depends on syndicate formation and undocumented runway\. *(Analyst view)* ^[4](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[11](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- **Diligence focus.** Verify first whether revenue comes from customer purchases or R&amp;D pass\-through; request the filed 2024 and 2025 accounts and the signed customer list\. *(Analyst view)* ^[12](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597),[13](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597),[14](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2026\-10\-16 · 10 až 16 milionů eur; date n/a · investor search &amp; European funds financing · 100 milionů korun \+ 100 milionů korun \+ 4\-5 milionů eur · neupřesněná firma, Sprind \(agentura\); date n/a · Series A · 8 million euros | 4, 5, 11 |
| Public money | 17 contract\(s\) in the contract register; 18 grant project\(s\) awarded 138\.4M CZK \+ 1 without published amount, 32\.7M CZK paid so far · by kind: 2 purchase\(s\) by public buyers \(755,152 CZK\); 12 R&amp;D project agreement\(s\), amounts are project budgets, not revenue; 3 other \(1\.3M CZK\) · counterparties: Správa informačních technologií města Plzně, Eurosecur s\. r\. o\., VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ, České vysoké učení technické v Praze | 15, 16, 17, 3, 18, 19 |
| Thesis fit \(Rockaway\) | sectors: deep tech \(30 facts\); AI\-led transformative tech \(23 facts\); industrial / manufacturing AI \(15 facts\); defence / dual\-use \(6 facts\); energy \(4 facts\) · geography: CZ \(core region\) · overlaps portfolio: Vermeer \(defence, drone, navigat\) | 20, 21, 22 |
| Hiring | 3 open roles: engineering 2, sales gtm 1 | 23, 24, 25 |
| Engineering footprint | 15 public repos \(6★, last push 2026\-11\-09\); 11 subdomains; 1 docs pages; stack: Apache, Divi v\.4\.27\.9, WordPress | 26, 27, 28, 29 |
| Customers | public pricing: yes | 1 |
| Timeline | Czech entity registered 2017\-11\-27; first press 2026\-06\-15 \(16 articles collected\) | 30, 31 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the market, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** Deep tech and energy evidence is substantive: grant\-funded drone systems for photovoltaic plant monitoring and grid inspection\. Defence evidence is company wording only \(an NDAA\-compliant claim\); no won defence tender or EU defence project appears in the facts\. *(Analyst view)* ^[32](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F940343665E2F83FB3555FEDDE2A186490FEF16884132196B49785C0BFC8198B),[33](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-0BB20EACD417951BEDBEE8CB242827A16521DF3F26B31BD25693E45B738FFF35),[34](https://fly4future.com/),[35](https://ted.europa.eu/en/notice/-/detail/271589-2023)
  - Assumption: Grant\-funded projects reflect current product direction
- **Portfolio overlap:** Vermeer, a Rockaway portfolio company, also offers GPS\-free drone navigation for defence and dual\-use\. Fly4Future's GPS\-free flight claims suggest a possible overlap, but a shared buyer is not shown in the facts, so conflict is unconfirmed\. *(Analyst view)* ^[2](https://aktualne.cvut.cz/en/media-screenings/20260813-the-czechs-want-to-disrupt-chinas-dominance-over-drones-they-plan-to),[14](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
  - Assumption: Both companies sell to the same drone\-navigation buyers

## Business model

- Product sales are thin in the facts: two purchase contracts total about 0\.76M CZK \(a 2023 university buyer for 3D laser scanners; a 2026 university consultation order\)\. A press article gives 1\.5M CZK per drone unit and 70\-80 units a year, with unclear period\. *(Verified)* ^[3](https://smlouvy.gov.cz/smlouva/24070505),[6](https://smlouvy.gov.cz/smlouva/38841586),[1](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- Grants are support, not revenue: about 138M CZK is awarded across 18 grants for multi\-year projects, but only about 32\.7M CZK is recorded as paid, across five grants with payment data\. *(Verified)* ^[36](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[37](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-9C717B54B2622718D226FA630A14F049D620A56B273EA1F0D08011E5E084B9A7),[38](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-C37E481DFF08F9C6D7DB0A6EB8DB96B80DAA067EE0CFD31F35DF85D5957BA882),[39](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-FABB6D47509E746A7D3236D2A5CED6AEE7342716CA15492D85681B97AE506BD8),[40](https://www.hlidacstatu.cz/Dotace/Detail/IsRed-F727F0B0BD373F910CA65A6D1E8DFA930B310A55DDF46B35EDC9CB6BAB703678)
- Twelve research\-consortium agreements \(about 130\.6M CZK\) are project budgets for university\-led research, not customer revenue or sales to public buyers\. *(Analyst view)* ^[16](https://smlouvy.gov.cz/smlouva/19121879),[19](https://smlouvy.gov.cz/smlouva/29827008),[41](https://smlouvy.gov.cz/smlouva/34343605)

## Market

- Fly4Future states that industry and civilian users want flying without GPS and that clients already use its system\. A founder quoted in a 2026 press article says most drones are sold abroad, with about 10% of output staying in Czechia\. *(Partly verified)* ^[14](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[42](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
- No sourced market size exists in the supplied facts\. The only market context is an unquantified press remark about drone\-industry and defence investment, so sizing needs separate research\. *(Analyst view)* ^[43](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- The only public procurement notice is a 2023 Brno industrial\-machinery tender where a university is the buyer\. It is flagged as not a defence buyer, so it shows no defence procurement\. *(Verified)* ^[35](https://ted.europa.eu/en/notice/-/detail/271589-2023)

## Competition

- Arke Telekom \(Türkiye\) lists GNSS\-free tactical drone communications, the closest stated overlap with Fly4Future's GPS\-free flight claims\. Found via the NATO DIANA 2026 cohort list; a candidate, not a confirmed competitor\. *(Analyst view)* ^[44](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[2](https://aktualne.cvut.cz/en/media-screenings/20260813-the-czechs-want-to-disrupt-chinas-dominance-over-drones-they-plan-to)
  - Assumption: Listing description reflects current product
- Alpha Autonomy \(Greece\) offers AI\-powered UAV swarms for ISR in contested environments, overlapping Fly4Future's stated autonomous drone swarm work\. Found via the NATO DIANA 2026 cohort list; candidate only\. *(Analyst view)* ^[45](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[5](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
- Mara \(US, swarm protection\) and AegisX \(Sweden, low\-flying fibre\-optic drone detection\) overlap with Fly4Future's counter\-drone capture grant project\. Both come from the NATO DIANA 2026 list; candidates, with overlap low\. *(Analyst view)* ^[46](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[47](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[48](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB)
  - Assumption: Fly4Future's capture project reaches the market
- Marble Aerospace \(UK\) fields high\-speed UAVs with autonomous robotic hangars for ISR\. Overlap with Fly4Future is weaker, mainly in autonomy and robotics\. Found via the NATO DIANA 2026 cohort list; candidate only\. *(Analyst view)* ^[49](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html),[5](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)

## Case for and against

- **For:** Demand signal: Fly4Future says clients already use its GPS\-free system and several industrial partners focus on GPS\-free flight\. This is an unverified company claim; named customers are needed to confirm it\. *(Analyst view)* ^[14](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[2](https://aktualne.cvut.cz/en/media-screenings/20260813-the-czechs-want-to-disrupt-chinas-dominance-over-drones-they-plan-to)
- **For:** External validation: technology\-agency awards, including a 2025 GNSS\-resistant multi\-robot project, and an EU Horizon grant support the research base, though this is not revenue\. *(Analyst view)* ^[36](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[50](https://cordis.europa.eu/project/id/101071270)
- **Against:** Revenue is unproven: two purchase contracts total about 0\.76M CZK and no named customers appear in the facts\. Grant money is support, not sales\. *(Analyst view)* ^[3](https://smlouvy.gov.cz/smlouva/24070505),[6](https://smlouvy.gov.cz/smlouva/38841586)
- **Against:** Funding is unclosed: a 10\-16M EUR raise is being sought, an 8M EUR Series A is planned for one project, and the investors named so far are unidentified\. *(Analyst view)* ^[4](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[11](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni),[5](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
- **Against:** Kill risk: the company plans tens of thousands of units a year, while it reports about 40 staff and a stated 70\-80 units a year\. Failure to fund scale\-up would leave that plan unexecuted\. *(Analyst view)* ^[2](https://aktualne.cvut.cz/en/media-screenings/20260813-the-czechs-want-to-disrupt-chinas-dominance-over-drones-they-plan-to),[51](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[1](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- **Must be true:** Diligence must confirm invoiced revenue from paying buyers and actual unit pricing, since only two purchase contracts and one press\-quoted price are sourced\. *(Analyst view)* ^[1](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni),[3](https://smlouvy.gov.cz/smlouva/24070505),[6](https://smlouvy.gov.cz/smlouva/38841586)
  - Assumption: Quoted pricing reflects actual sales

# Technical due diligence

## Ownership and capital

- Ostrava\-seated s\.r\.o\. registered in 2017; no registry investor entries were supplied; the company describes itself as a CTU Prague spinout\. *(Partly verified)* ^[52](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581),[53](https://fly4future.com/about-us/)
- Rounds sought: 10\-16M EUR from investors \(article dated 2026\-10\-16\)\. The founder states 100M CZK is already promised by one unnamed firm, with Sprind mediating 4\-5M EUR\. *(Corroborated)* ^[4](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/),[5](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro)
- Public money: 17 contracts \(12 R&amp;D, 2 purchase, 3 other\); 18 awarded grants total 138\.4M CZK, with 32\.7M CZK paid on the 5 grants that have payment data\. Awards are not revenue\. *(Verified)* ^[16](https://smlouvy.gov.cz/smlouva/19121879),[3](https://smlouvy.gov.cz/smlouva/24070505),[6](https://smlouvy.gov.cz/smlouva/38841586),[37](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-9C717B54B2622718D226FA630A14F049D620A56B273EA1F0D08011E5E084B9A7)

## Technology profile

- Built: ROS\-based C\+\+ mission handler, ROS\-to\-backend bridge and Siyi gimbal plugin\. Public code shows autonomy plumbing, not a shipped product\. *(Verified)* ^[54](https://github.com/fly4future/iroc_mission_handler),[7](https://github.com/fly4future/iroc_bridge),[27](https://github.com/fly4future/siyi_cam_executor_plugin)
- Public engineering is thin: 15 repos with 6 stars in total, one docs page, and a WordPress marketing site that does not show the product stack\. *(Partly verified)* ^[55](https://github.com/fly4future/install_script),[29](https://fly4future.com/custom-drones/we-help-you-to-establish-flying-robots-research-lab/),[56](https://fly4future.com/)
- AI dependency: no LLM vendor is named as a tool or subprocessor, only Google Analytics\. No papers, verified models or ML roles are supplied, so own\-model capability is unevidenced\. *(Company claim)* ^[57](https://fly4future.com/privacy-policy/),[23](https://fly4future.com/career/)

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** Mission handling and ROS\-to\-backend bridging map to ROS 2 nodes with pluginlib, and WebRTC streaming maps to open\-source WebRTC libraries; off\-the\-shelf parts could reproduce these components\. *(Analyst view)* ^[7](https://github.com/fly4future/iroc_bridge),[58](https://github.com/fly4future/webrtc_ros),[27](https://github.com/fly4future/siyi_cam_executor_plugin)
  - Assumption: Assumes public repos reflect the shipped stack\.
- **Edge supported by public evidence:** Public evidence shows Horizon Europe SME participation, Czech agency R&amp;D support agreements, and two published drone applications, none of them granted patents\. *(Analyst view)* ^[50](https://cordis.europa.eu/project/id/101071270),[36](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3),[9](https://patents.google.com/patent/WO2024255934A1),[10](https://patents.google.com/patent/CZ38123U1)
  - Assumption: Assumes public registers are complete for the company\.

## Risks and caveats

- Public\-money concentration: R&amp;D agreements dominate the contract register at 130\.6M CZK, and payment data is visible for only 5 of 18 grants\. *(Analyst view)* ^[16](https://smlouvy.gov.cz/smlouva/19121879),[37](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-9C717B54B2622718D226FA630A14F049D620A56B273EA1F0D08011E5E084B9A7)
- Unverified claims: GPS\-free flight, own batteries and chip, and NDAA compliance appear only as company statements, and no verification check is supplied\. *(Analyst view)* ^[2](https://aktualne.cvut.cz/en/media-screenings/20260813-the-czechs-want-to-disrupt-chinas-dominance-over-drones-they-plan-to),[34](https://fly4future.com/),[14](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/)
- Thin engineering footprint: 2 open engineering roles and 6 repo stars against a company of about 40 people\. *(Analyst view)* ^[23](https://fly4future.com/career/),[24](https://fly4future.com/career/),[51](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/)

## Questions for founders

- What share of 2025\-2026 income is customer purchases versus R&amp;D pass\-through, given purchase contracts total only 0\.76M CZK? *(Analyst view)* ^[6](https://smlouvy.gov.cz/smlouva/38841586),[3](https://smlouvy.gov.cz/smlouva/24070505),[12](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597)
- Which named clients support the 'already in demand' claim and the 1\.5M CZK per\-unit price for 70\-80 units a year, and what are the unit gross margins? *(Analyst view)* ^[14](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/),[1](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni)
- Can the team share the swarm autonomy code and flight logs to test the GPS\-free claim, plus evidence for NDAA compliance? *(Analyst view)* ^[8](https://github.com/fly4future/argentswarm_core),[34](https://fly4future.com/)

## Sources

1. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni) · Independent press · Pricing — “Nějakých 70 až 80 kusů ročně\. Jde ale o stroje až za 1,5 milionu korun s velkou přidanou hodnotou\.”
2. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/en/media-screenings/20260813-the-czechs-want-to-disrupt-chinas-dominance-over-drones-they-plan-to) · Independent press · Press article · 2026\-08\-13 — “The Czechs want to disrupt China's dominance over drones\. They plan to produce tens of thousands of units per year \- News service \- Czech technical university in Prague”
3. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/24070505) · Official record · Public contract · 2023\-04\-12 — “VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ · 658 829 CZK · Kupní smlouva \- Senzorický systém pro mobilní roboty – 3D laserové skenery”
4. [cc\.cz](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/) · Independent press · Funding round — “Fly4future proto nyní od investorů žádá 10 až 16 milionů eur, tedy zhruba 244 až 390 milionů korun\.”
5. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro) · Independent press · Funding round — “Od jedné firmy už máme příslib přes 100 milionů korun\. K tomu plánujeme získat dalších 100 milionů z evropských fondů\. To je budget, který potřebuji na vybudování týmu\. V úterý jedu do Německa jednat s agenturou Sprind, která by nám mohla zprostředkovat investici kolem čtyř až pěti milionů eur na vývoj autonomních rojů”
6. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/38841586) · Official record · Public contract · 2026\-07\-17 — “Vysoká škola báňská \- Technická univerzita Ostrava · 96 323 CZK · Objednávka: konzultace pro vývoj dronové platformy”
7. [github\.com](https://github.com/fly4future/iroc_bridge) · Public technical artifact · GitHub repository · 2026\-10\-30 — “fly4future/iroc\_bridge · Node to translate messages from ROS to backend and back · C\+\+ · last push 2026\-10\-30”
8. [github\.com](https://github.com/fly4future/argentswarm_core) · Public technical artifact · GitHub repository · 2026\-10\-22 — “fly4future/argentswarm\_core · Digest of the swarm autonomy software at f4f\. · C\+\+ · last push 2026\-10\-22”
9. [patents\.google\.com](https://patents.google.com/patent/WO2024255934A1) · Official record · Patent publication — “WO2024255934A1 · Method of marking bark beetle infested trees and means for executing this … · Fly4Future s\.r\.o\.”
10. [patents\.google\.com](https://patents.google.com/patent/CZ38123U1) · Official record · Patent publication — “CZ38123U1 · A drone sprayer · Fly4Future s\.r\.o\.”
11. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni) · Independent press · Funding round — “Bereme to už jako Series A, protože máme produkt a kontrakty\. Potřebujeme zatím pro jeden projekt získat osm milionů eur \(necelých 200 milionů korun – pozn\. red\.\)\.”
12. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597) · Official record · Registry: filed document · 2026\-07\-17
13. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=995597) · Official record · Registry: filed document · 2025\-07\-23
14. [fly4future\.com](https://fly4future.com/winning-solution-sprind-drone-flight-without-gps/) · Company's own website · Market statement — “Thanks to our participation in the competition, we have created a truly unique system that is already in demand by clients\. Several industrial partners are now focusing on flying without GPS , so this is a very hot topic now that not only the defence industry but also the civilian industry is aware of\.”
15. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/7574923) · Official record · Public contract · 2018\-12\-05 — “Správa informačních technologií města Plzně · 592 900 CZK · smlouva o obchodní spoluporáci”
16. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/19121879) · Official record · Public contract · 2022\-01\-17 — “Eurosecur s\. r\. o\. · 74 624 392 CZK · Dohoda o vypořádání závazků z neuveřejněné smlouvy o spolupráci na řešení projektu „Univerzální systém kolaborativních dronů"”
17. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/19719811) · Official record · Public contract · 2022\-02\-28 — “Správa informačních technologií města Plzně · 589 270 CZK · Smlouva o obchodní spolupráci”
18. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/27109547) · Official record · Public contract · 2024\-01\-01 — “VYSOKÉ UČENÍ TECHNICKÉ V BRNĚ · 2 400 000 CZK · SMLOUVA O ÚČASTI NA ŘEŠENÍ PROJEKTU A O VYUŽITÍ VÝSLEDKŮ”
19. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/29827008) · Official record · Public contract · 2024\-08\-14 — “Eurosecur s\. r\. o\. · 25 494 062 CZK · Smlouva o spolupráci na řešení projektu OP TAK „Univerzální systém kolaborativních robotů“”
20. [cnaip\.cz](https://www.cnaip.cz/en/entity/fly4future) · Independent press · Press article — “Fly4Future — CNAIP”
21. [fel\.cvut\.cz](https://fel.cvut.cz/en/what-s-on/news/36454-ctu-spinout-fly4future-wins-prestigious-ai-company-of-the-year-award-at-ai-awards-2024) · Independent press · Press article — “CTU spinout Fly4Future wins prestigious AI Company of the Year award at AI Awards 2024 \- CTU FEE”
22. [adoptimal\.cz](https://adoptimal.cz/magazin/aktualita/fly4future-chysta-vyrobu-desitek-tisic-autonomnich-dronu-rocne) · Independent press · Press article · 2026\-08\-17 — “Fly4Future chystá výrobu desítek tisíc autonomních dronů ročně”
23. [fly4future\.com](https://fly4future.com/career/) · Company's own website · Job posting — “System Engineer Specialist”
24. [fly4future\.com](https://fly4future.com/career/) · Company's own website · Job posting — “Robotics SW Engineer”
25. [fly4future\.com](https://fly4future.com/career/) · Company's own website · Job posting — “Technical Sales Engineer”
26. [github\.com](https://github.com/fly4future/spi_uwb_controller) · Public technical artifact · GitHub repository · 2025\-04\-13 — “fly4future/spi\_uwb\_controller · C · last push 2025\-04\-13”
27. [github\.com](https://github.com/fly4future/siyi_cam_executor_plugin) · Public technical artifact · GitHub repository · 2025\-08\-28 — “fly4future/siyi\_cam\_executor\_plugin · A ROS package that provides a plugin for controlling Siyi camera gimbals\. This plugin is designed to be used by the mission handler package for executing subtasks during missions\. · C\+\+ · last push 2025\-08\-28”
28. [github\.com](https://github.com/fly4future/rtsp_to_ros) · Public technical artifact · GitHub repository · 2026\-03\-20 — “fly4future/rtsp\_to\_ros · Python · last push 2026\-03\-20”
29. [fly4future\.com](https://fly4future.com/custom-drones/we-help-you-to-establish-flying-robots-research-lab/) · Company's own website · Website page — “We Help You to Establish Flying Robots’ Research/Lab \| Fly4Future”
30. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581) · Official record · Registry: incorporation · 2017\-11\-27 — “registered 2017\-11\-27”
31. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/en/media-screenings/20260615-the-development-of-drones-in-the-czech-republic-will-be-ensured-by-a-darpa) · Independent press · Press article · 2026\-06\-15 — “The development of drones in the Czech Republic will be ensured by a DARPA\-like agency, a smart army and strong investors \- News service \- Czech technical university in Prague”
32. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F940343665E2F83FB3555FEDDE2A186490FEF16884132196B49785C0BFC8198B) · Official record · National grant · 2025 — “Systém pro automatizované monitorování a údržbu fotovoltaických elektráren využívající umělou inteligenci a bezpilotní letecké platformy · Technologická agentura ČR · 8 470 372 CZK”
33. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-0BB20EACD417951BEDBEE8CB242827A16521DF3F26B31BD25693E45B738FFF35) · Official record · National grant · 2022 — “Systém pro automatizovanou inspekci prvků přenosové soustavy elektrické energie s využitím bezpilotních prostředků · Technologická agentura ČR · 5 855 742 CZK”
34. [fly4future\.com](https://fly4future.com/) · Company's own website · Technical claim — “All of our UAV platforms are fully capable of meeting NDAA compliance , ensuring that our products are free from components sourced from prohibited manufacturers as outlined in Section 889 of the U\.S\. National Defense Authorization Act \(NDAA\)”
35. [ted\.europa\.eu](https://ted.europa.eu/en/notice/-/detail/271589-2023) · Official record · EU procurement notice \(TED\) · 2023\-05\-08 — “Czechia\-Brno: Industrial machinery — buyer: Vysoké učení technické v Brně, Středoevropský technologický institut”
36. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-591970AB3CA3161135465C224B2E4C4522AEC0FE7906E2A4F31ACAFBFFE9F8D3) · Official record · National grant · 2025 — “Multi\-robotický letecký systém pro autonomní bezpečnostní dohled a inspekci rozlehlých průmyslových objektů odolný vůči výpadku komunikace a signálu GNSS · Technologická agentura ČR · 21 826 349 CZK”
37. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-9C717B54B2622718D226FA630A14F049D620A56B273EA1F0D08011E5E084B9A7) · Official record · National grant · 2024 — “Letecká platforma pro autonomní inspekce v členitém indoor prostředí · Technologická agentura ČR · 19 404 800 CZK”
38. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-C37E481DFF08F9C6D7DB0A6EB8DB96B80DAA067EE0CFD31F35DF85D5957BA882) · Official record · National grant · 2025 — “Udržitelné zemědělství: Energeticky výkonné bezpilotní technologie pro precizní zemědělství · Technologická agentura ČR · 14 761 078 CZK”
39. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-FABB6D47509E746A7D3236D2A5CED6AEE7342716CA15492D85681B97AE506BD8) · Official record · National grant · 2024 — “Rozhraní pro intuitivní a spolehlivou obsluhu heterogenní skupiny robotů s monitoringem stavu a bezpečným systémem řešení poruch · Technologická agentura ČR · 4 879 000 CZK”
40. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsRed-F727F0B0BD373F910CA65A6D1E8DFA930B310A55DDF46B35EDC9CB6BAB703678) · Official record · National grant · 2025 — “Registrace ochranné známky · Ministerstvo průmyslu a obchodu · 50 550 CZK”
41. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/34343605) · Official record · Public contract · 2025\-07\-25 — “České vysoké učení technické v Praze · 12 270 000 CZK · SMLOUVA O ÚČASTI NA ŘEŠENÍ PROJEKTU A O VYUŽITÍ VÝSLEDKŮ OZ01020024”
42. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260414-cesti-vedci-vytvorili-letajici-roj-autonomnich-dronu-ted-shani-investory-pro) · Independent press · Press article — “Čeští vědci vytvořili létající roj autonomních dronů\. Teď shání investory pro jejich sériovou výrobu \- Zpravodajský servis \- České vysoké učení technické v Praze”
43. [aktualne\.cvut\.cz](https://aktualne.cvut.cz/zpravy-z-medii/20260615-rozvoj-dronu-v-cesku-zajisti-obdoba-agentury-darpa-chytra-armada-a-silni) · Independent press · Market statement — “Otevřeli jsme první investiční kolo a zájem je velký\. Rád bych postupně s pomocí investorů vybudoval v Česku významnou firmu, která bude jednou i globálním hráčem\.”
44. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Arke Telekom Mühendislik Elektronik Sanayi Ticaret Ltd\. Şti: Resilient, autonomous communication architecture for GNSS\-free tactical drone operations”
45. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Alpha Autonomy: AI\-powered autonomous UAV swarms for resilient, low\-altitude ISR in denied &amp; contested environments”
46. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Mara: Simultaneous 360° protection against swarms of 48\+ EW\-resistant drones at 1/20th the cost\.”
47. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “AegisX: Detecting &amp; tracking low flying fibre optic drones”
48. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-93510F1C93F6AA6B9F1C335DE7BF3F07C0C08252A5D581995B6192C10DC090FB) · Official record · National grant · 2028 — “Létající robot využívající umělou inteligencí pro bezpečný odchyt nepovolených dronů v chráněném prostoru · Ministerstvo pro místní rozvoj · 35 982 614 CZK”
49. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Marble Aerospace Limited: Fleets of high\-speed UAVs with autonomous robotic hangars to create rapidly deployable “ISR bubbles””
50. [cordis\.europa\.eu](https://cordis.europa.eu/project/id/101071270) · Official record · EU grant · 2022\-07\-01 — “Strengthening Research and Innovation Excellence in Autonomous Aerial Systems”
51. [cc\.cz](https://cc.cz/od-univerzitniho-projektu-po-milionove-trzby-ceske-drony-maji-za-ukol-dorucit-jidlo-zachranit-zivot-i-ockovat/) · Independent press · Team claim — “Dnes má kolem 40 zaměstnanců\.”
52. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/06632581) · Official record · Registry: identity · 2017\-11\-27 — “Fly4Future s\.r\.o\. · s\.r\.o\. · registered 2017\-11\-27”
53. [fly4future\.com](https://fly4future.com/about-us/) · Company's own website · Team claim — “Fly4Future was formed in 2017 as a spinout of the Multi\-Robot Systems group at the Czech Technical University in Prague \(MRS CTU\)”
54. [github\.com](https://github.com/fly4future/iroc_mission_handler) · Public technical artifact · GitHub repository · 2026\-10\-30 — “fly4future/iroc\_mission\_handler · Action server component that manages drone flight through desired waypoints\. · C\+\+ · last push 2026\-10\-30”
55. [github\.com](https://github.com/fly4future/install_script) · Public technical artifact · GitHub repository · 2026\-11\-09 — “fly4future/install\_script · Shell · last push 2026\-11\-09”
56. [fly4future\.com](https://fly4future.com/) · Public technical artifact · Technology detected
57. [fly4future\.com](https://fly4future.com/privacy-policy/) · Company's own website · Subprocessor \(privacy policy\) — “We use Google Analytics to track this information\. Find out how Google uses your data at”
58. [github\.com](https://github.com/fly4future/webrtc_ros) · Public technical artifact · GitHub repository · 2026\-05\-12 — “fly4future/webrtc\_ros · Streaming of ROS Image Topics using WebRTC · C\+\+ · last push 2026\-05\-12”
59. [ec\.europa\.eu](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/org-details/887136005) · Official record · EU grant — “Strengthening Research and Innovation Excellence in Autonomous Aerial Systems”
60. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-F18344B307BC4432CB8F25BAAC42A590132AC88F6987535F4F0180DD521530E7) · Official record · National grant · 2021 — “Univerzální systém kolaborativních dronů · Ministerstvo průmyslu a obchodu · 10 279 779 CZK”
61. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/35675041) · Official record · Public contract · 2025\-11\-19 — “Česká agentura na podporu obchodu · 87 120 CZK · Smlouva o spolupráci Design”
62. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Drone City: Heavy\-lift UAV with advanced autonomy for extreme environments”
63. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “Volta Space Technologies: Persistent drone flight and emergency power in extremely cold environments”
64. [web\.archive\.org](https://web.archive.org/web/20261029165007id_/https://www.diana.nato.int/about-diana/2026-cohort-of-companies.html) · Official record · NATO DIANA cohort company — “OLEDCOMM: Stealth in drone flight\. Unjammable connectivity by light”

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

Analysis: claude\-haiku\-5\-5 (cost $0.0216); AI extraction cost $0.0080. Full fact table: CSV export.

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
