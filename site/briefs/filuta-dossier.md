# Filuta AI — due diligence brief

filuta\.ai · Filuta AI CZ s\.r\.o\. · IČO 09745424 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** An enterprise 'Composite AI' platform that runs autonomous agents to map, test and monitor interactive systems \(QA, procurement compliance, HMI\), sold to large enterprises and public\-sector buyers\. *(Company claim)* ^[1](https://filuta.ai/company),[2](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem),[3](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount),[4](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount),[5](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- **Stage & traction.** Multiple public grants \(≈44\.1M CZK\), pre\-seed and seed reporting \(record C ZK pre\-seed; $4\.2M seed\), pilot customers including Bohemia Interactive and Liftago, and a Texas government vendor listing\. *(Verified)* ^[6](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-977DD2CC67E299D573718EC1C9228BB34E4FC92089EF8F2FC763FD0E69BE5D82),[7](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-C8BA33B8412EA7002E07855E4ECA1F13263945F6C836AD28D9FBEA85FA85F1D0),[8](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/),[9](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/),[10](https://dir.texas.gov/contracts/vendors/filuta-ai-inc)
- **Technology & moat.** Emerging protection via six published patent applications around domain\-model synthesis, and multiple academic papers showing research output and domain expertise\. *(Verified)* ^[11](https://patents.google.com/?assignee=filuta),[12](https://patents.google.com/patent/US20250005318A1),[13](https://openalex.org/W4392019524),[14](https://openalex.org/W4403792769),[15](https://openalex.org/W7222012453)
- **Key risk.** Several company claims \(e\.g\., 'owns several patented solutions' and large pre\-seed amounts\) are contradicted or inconsistent with patent status and varying press reports, creating credibility risk\. *(Analyst view)* ^[16](https://patents.google.com/?assignee=filuta),[17](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million),[8](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/)
- **Diligence focus.** Verify which patent claims are granted vs applications and confirm paid customer contracts \(HISD vs\. confirmed pilots\) because both materially affect defensibility and revenue runway\. *(Analyst view)* ^[11](https://patents.google.com/?assignee=filuta),[16](https://patents.google.com/?assignee=filuta),[18](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount),[19](https://czechfounders.vc/our-portfolio/filuta-ai)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2023\-01\-23 · pre\-seed · 56 milionů korun · Nation 1, Czech Founders, SPM Invest, Microsoft Startup Program, Horizon Europe, Microsoft · 2 reports; 2025\-06\-24 · seed · 4\.2 million USD · Rockaway Ventures, Tarpan Capital, Lion Beat Capital; 2025\-06\-24 · pre\-seed · nearly $56 million | 8, 20, 9, 17 |
| Public money | 4 grant\(s\), 44\.1M CZK \+ 1 without published amount | 21, 7, 22, 6 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; own\-model evidence: 9 papers, 0 verified HF models, 0 ML roles, 5 own\-model claims | 23, 24, 25 |
| Engineering footprint | 3 public repos \(3★, last push 2026\-03\-25\); product surfaces: api\.demo\.arrow\.filuta\.ai, api\.demo\.edison\.filuta\.ai, api\.demo\.hangout\.filuta\.ai, api\.dev\.internal\.filuta\.ai, api\.hiring\.demo\.filuta\.ai, docs\.filuta\.ai; stack: Nuxt | 26, 27, 28, 29, 30, 31 |
| Customers | 3 named: Houston Independent School District \(HISD\), Bohemia Interactive, Liftago; public pricing: not found | 4, 32, 33 |
| Claims checked | Patents: contradicted; Customer \(Bohemia Interactive, Liftago\): confirmed; Patents: confirmed; Government listing: confirmed; Customer \(Houston Independent School District \(HISD\)\): not found | 16, 19, 34, 11, 10, 18 |
| Timeline | Czech entity registered 2020\-12\-11; first press 2023\-01\-23 \(25 articles collected\) | 35, 36 |

# Detailed findings

## Ownership and capital

- Registry: Filuta AI CZ s\.r\.o\. incorporated 2020\-12\-11; 100% foreign holding by Filuta AI Inc\. \(US\) recorded 2022\-10\-20\. *(Verified)* ^[37](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09745424),[35](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09745424),[38](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09745424)
  - Assumption: Registry entries accurately reflect ownership structure\.
- Funding: reported pre\-seed \~56 million CZK with Nation 1, Czech Founders, SPM Invest and Microsoft program \(press\), and a seed round reported at $4\.2M led by Rockaway Ventures\. *(Corroborated)* ^[8](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/),[20](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy),[9](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/)
  - Assumption: Press summaries match underlying funding announcements\.
- Public money: four grants totaling ≈44,136,967 CZK, including CzechInvest support and a 36\.7M CZK Ministry of Industry award for 'AI planning agents'\. *(Partly verified)* ^[7](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-C8BA33B8412EA7002E07855E4ECA1F13263945F6C836AD28D9FBEA85FA85F1D0),[22](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-4D6C0E515DB6A36794427267495D3E563288718003989E1A7E9203A334A4F31B),[6](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-977DD2CC67E299D573718EC1C9228BB34E4FC92089EF8F2FC763FD0E69BE5D82),[21](https://filuta.ai/)
  - Assumption: Grant records represent awarded public funds\.

## Technology profile

- Product capabilities \(company\-described\): autonomous agents for system mapping, exhaustive state exploration, coverage metrics, reproducible traces, regulator\-oriented proofs, and CI integration for OEMs\. *(Company claim)* ^[39](https://filuta.ai/),[40](https://filuta.ai/),[23](https://filuta.ai/company),[41](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem),[5](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
  - Assumption: Descriptions are company statements unless otherwise verified\.
- Engineering footprint: public GitHub org with three active repos and multiple product subdomains \(api\.demo\.\*, docs\.filuta\.ai, platform\.on\.filuta\.ai\) indicating web/API surfaces\. *(Verified)* ^[42](https://github.com/FilutaAI),[28](https://github.com/FilutaAI/KeyFramer),[27](https://github.com/FilutaAI/synthesis-benchmarks),[43](https://crt.sh/?q=%25.filuta.ai&output=json),[44](https://crt.sh/?q=%25.filuta.ai&output=json)
  - Assumption: Public repos and subdomains reflect engineering output\.
- AI dependency and claims: company positions a neurosymbolic 'Composite AI' engine at core, multiple research papers authored by Filuta, and patent\-pending engine—no vendor\-LLM usage or customer\-account integrations reported\. *(Partly verified)* ^[1](https://filuta.ai/company),[14](https://openalex.org/W4403792769),[11](https://patents.google.com/?assignee=filuta),[25](https://filuta.ai/company),[13](https://openalex.org/W4392019524)
  - Assumption: No supplied facts list external LLM vendors used or integrated\.

## Rebuild check

- **Commodity:** Basic UI automation and CI integration — a 2–3 person team can rebuild test automation and CI hooks using Selenium/Appium and CI APIs\. *(Analyst view)* ^[5](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem),[2](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem),[41](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
  - Assumption: Coverage and traceability beyond basic automation are not included here\.
- **Hard to copy:** Composite neurosymbolic engine combining symbolic planning, model synthesis and published patent applications and academic papers — evidence of nontrivial R&amp;D and IP\. *(Analyst view)* ^[45](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem),[11](https://patents.google.com/?assignee=filuta),[14](https://openalex.org/W4403792769),[15](https://openalex.org/W7222012453)
  - Assumption: Patent applications and papers reflect nontrivial proprietary research\.
- **Verdict:** Month — a competent small team could reproduce basic autonomous testing and CI integration in weeks; cloning the patent\-pending composite engine and research outputs would take a quarter or longer and still lack the published IP and papers\. *(Analyst view)* ^[5](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem),[11](https://patents.google.com/?assignee=filuta),[14](https://openalex.org/W4403792769)
  - Assumption: Access to equivalent research talent and time is constrained\.

## Risks and caveats

- Credibility mismatch: company marketing claims 'owns several patented solutions' but verification shows six published applications and zero grants, flagged as contradicted\. *(Analyst view)* ^[46](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/),[16](https://patents.google.com/?assignee=filuta),[11](https://patents.google.com/?assignee=filuta)
  - Assumption: Marketing language exceeds verified patent status\.
- Customer confirmation gap: HISD listed as a case study on company site but independent corroboration not found; public\-sector listing exists for Texas DIR, creating mixed evidence on contract scale\. *(Analyst view)* ^[18](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount),[4](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount),[10](https://dir.texas.gov/contracts/vendors/filuta-ai-inc)
  - Assumption: Case study presence differs from independently verifiable contracts\.
- Funding reporting inconsistencies: multiple press sources report differing pre\-seed figures \(56M CZK vs\. nearly $56M\), requiring clarity on actual amounts and capitalization\. *(Analyst view)* ^[8](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/),[17](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million),[20](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy)
  - Assumption: Press discrepancies reflect ambiguous reporting\.

## Questions for founders

- Patents: which of the six published patent applications \(e\.g\. US20250005318A1\) have claims granted or are licensed, and provide prosecution history to assess enforceability? *(Analyst view)* ^[11](https://patents.google.com/?assignee=filuta),[12](https://patents.google.com/patent/US20250005318A1)
  - Assumption: Prosecution status materially affects moat strength\.
- Revenue/Contracts: provide signed contract copies or reference numbers for HISD and the OEM HMI CI integration to confirm scope, MRR, and renewal terms\. *(Analyst view)* ^[4](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount),[5](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem),[18](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
  - Assumption: Contracts will validate traction and revenue quality\.
- Funding clarity: reconcile public reporting on pre\-seed amounts \(56M CZK vs 'nearly $56M'\) and provide cap table post\-seed including dilution and investor rights\. *(Analyst view)* ^[8](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/),[17](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million),[9](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/)
  - Assumption: Accurate funding history is needed for valuation\.
- Technology reproducibility: request reproducibility package for a published paper \(code/data/benchmarks\) that demonstrates the claimed composite AI capabilities and tests\. *(Analyst view)* ^[27](https://github.com/FilutaAI/synthesis-benchmarks),[14](https://openalex.org/W4403792769),[13](https://openalex.org/W4392019524)
  - Assumption: Repro package would evidence technical substance\.

## Sources

1. [filuta\.ai](https://filuta.ai/company) · Company's own website · Technical claim — “At the heart of Filuta is a neurosymbolic engine — Gartner's name for the category is Composite AI\.”
2. [filuta\.ai](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem) · Company's own website · Product capability — “Filuta's agents began by autonomously mapping the infotainment system — discovering screens, menus, controls, and transitions without any pre\-built model or manual configuration\.”
3. [filuta\.ai](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount) · Company's own website · Product capability — “Every solicitation and contract is automatically checked against current federal \(FAR/DFARS\), state \(Texas Education Code\), and local regulations\.”
4. [filuta\.ai](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount) · Company's own website · Customer — “The largest school district in Texas partnered with Filuta to automate compliance monitoring, and turned their procurement operation into a model for public\-sector efficiency\.”
5. [filuta\.ai](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem) · Company's own website · Integration — “The OEM integrated Filuta's autonomous agents into their continuous integration pipeline\. Every build is now validated automatically, with results available within hours rather than weeks\.”
6. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-977DD2CC67E299D573718EC1C9228BB34E4FC92089EF8F2FC763FD0E69BE5D82) · Official record · National grant · 2025 — “Samoobslužní AI plánovací agenti · Ministerstvo průmyslu a obchodu · 36 790 550 CZK”
7. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-C8BA33B8412EA7002E07855E4ECA1F13263945F6C836AD28D9FBEA85FA85F1D0) · Official record · National grant · 2022 — “Podpora z projektu Technologické inkubace\. · Agentura pro podporu podnikání a investic CzechInvest · 4 826 918 CZK”
8. [lupa\.cz](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/) · Independent press · Funding round — “investoři vedení zdejším fondem Nation 1 \. Připojila se organizace Czech Founders , fond SPM Invest spolumajitelů Bohemia Interactive Marka Španěla a Slavomíra Pavlíčka , startupový program Microsoftu a eurounijní program Horizon Europe\.”
9. [cc\.cz](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/) · Independent press · Funding round — “Vedoucím investorem současného, takzvaného seed kola byl fond Rockaway Ventures zakladatele Jakuba Havrlanta s přispěním společnosti Tarpan Capital či fondu Lion Beat Capital\.”
10. [dir\.texas\.gov](https://dir.texas.gov/contracts/vendors/filuta-ai-inc) · Official record · Independent check of a claim — “Filuta AI Inc\. \| Texas Department of Information Resources \# Filuta AI Inc\. \#\# Vendor Information Explore what this Vendor has to offer through the contracts listed below\. Contracts are competitively bid, saving you time and money\. For the latest pricing information and to negotiate further, ple”
11. [patents\.google\.com](https://patents.google.com/?assignee=filuta) · Official record · Independent check of a claim — “6 published patent applications \(none granted yet\), e\.g\. US20250005318A1, US20250005328A1\.”
12. [patents\.google\.com](https://patents.google.com/patent/US20250005318A1) · Official record · Patent publication — “US20250005318A1 · System and method for automated data\-driven domain model synthesis · Filuta Ai Inc\.”
13. [openalex\.org](https://openalex.org/W4392019524) · Public technical artifact · Research paper · 2024\-02\-16 — “On Automating Video Game Regression Testing by Planning and Learning · arXiv \(Cornell University\) · cited 6×”
14. [openalex\.org](https://openalex.org/W4403792769) · Public technical artifact · Research paper · 2024\-10\-26 — “Planning Domain Model Acquisition from State Traces without Action Parameters · Principles of Knowledge Representation and Reasoning · cited 15×”
15. [openalex\.org](https://openalex.org/W7222012453) · Public technical artifact · Research paper · 2026\-10\-13 — “Graph\-Based Orchestration of Heterogeneous AI Models: A Control Node Approach to Composite Intelligence · arXiv \(Cornell University\)”
16. [patents\.google\.com](https://patents.google.com/?assignee=filuta) · Official record · Independent check of a claim — “Claim implies owned/granted patents, but only published applications were found \(6 publications, 0 granted\): US20250005318A1, US20250005328A1\.”
17. [czechstartups\.gov\.cz](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million) · Official record · Funding round — “Filuta AI was founded in 2022 and just a year later raised a record investment of nearly $56 million in a pre\-seed round\.”
18. [filuta\.ai](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount) · Company's own website · Independent check of a claim
19. [czechfounders\.vc](https://czechfounders.vc/our-portfolio/filuta-ai) · Independent press · Independent check of a claim — “based on composite AI, a method of combining different AI approaches to achieve better results\. This allows Filuta AI to create, operate, maintain, and improve autonomous systems efficiently\. Filuta AI has global ambitions and is currently piloting its technology with companies like Liftago and MyFo”
20. [focuson\.cz](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy) · Independent press · Funding round — “Společnost Filuta AI v pre\-seed kole získala investice v rekordní výši téměř 56 milionů korun\.”
21. [filuta\.ai](https://filuta.ai/) · Company's own website · EU grant — “The AIPlan4EU project is funded by the European Commission \- H2020 research and innovation programme under grant agreement No 101016442 CzechInvest We were supported by the system project Technological Incubation and Internationalisation\.”
22. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-4D6C0E515DB6A36794427267495D3E563288718003989E1A7E9203A334A4F31B) · Official record · National grant · 2025 — “Účast v programu Internacionalizace v rámci NPO, číslo projektu 2425000002, KA R&amp;D Expanze · Agentura pro podporu podnikání a investic CzechInvest · 2 519 499 CZK”
23. [filuta\.ai](https://filuta.ai/company) · Company's own website · Product capability — “Every action is explained, every finding reproduces on demand, and every run ends with a coverage number and a statement of exactly what was proven — from a single feature to a full release train, without losing traceability\.”
24. [filuta\.ai](https://filuta.ai/) · Company's own website · Technical claim — “Patent\-pending core US applications 18/761,037 and 18/761,015 \(filed 1 July 2024\) — composite\-AI specification and domain\-model synthesis\.”
25. [filuta\.ai](https://filuta.ai/company) · Company's own website · Technical claim — “Pending Patent applications on the core engine”
26. [github\.com](https://github.com/FilutaAI/painter-challenge) · Public technical artifact · GitHub repository · 2023\-12\-12 — “FilutaAI/painter\-challenge · An encoding challenge · Python · last push 2023\-12\-12”
27. [github\.com](https://github.com/FilutaAI/synthesis-benchmarks) · Public technical artifact · GitHub repository · 2025\-03\-07 — “FilutaAI/synthesis\-benchmarks · This repository contains benchmark instances for evaluating planning action model learning algorithms\. · PDDL · last push 2025\-03\-07”
28. [github\.com](https://github.com/FilutaAI/KeyFramer) · Public technical artifact · GitHub repository · 2026\-03\-25 — “FilutaAI/KeyFramer · Key frame determinations for YouTube, local, and uploaded videos · Python · last push 2026\-03\-25”
29. [crt\.sh](https://crt.sh/?q=%25.filuta.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-03\-03 — “platform\.on\.filuta\.ai \(first certificate 2023\-03\-03\)”
30. [crt\.sh](https://crt.sh/?q=%25.filuta.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-08\-15 — “api\.dev\.internal\.filuta\.ai \(first certificate 2025\-08\-15\)”
31. [crt\.sh](https://crt.sh/?q=%25.filuta.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-08\-27 — “api\.hiring\.demo\.filuta\.ai \(first certificate 2025\-08\-27\)”
32. [focuson\.cz](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy) · Independent press · Customer — “Už nyní Filuta pilotuje svůj byznys například pro Bohemia Interactive nebo Liftago\.”
33. [focuson\.cz](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy) · Independent press · Customer — “Už nyní Filuta pilotuje svůj byznys například pro Bohemia Interactive nebo Liftago\.”
34. [czechfounders\.vc](https://czechfounders.vc/our-portfolio/filuta-ai) · Independent press · Independent check of a claim — “based on composite AI, a method of combining different AI approaches to achieve better results\. This allows Filuta AI to create, operate, maintain, and improve autonomous systems efficiently\. Filuta AI has global ambitions and is currently piloting its technology with companies like Liftago and MyFo”
35. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09745424) · Official record · Registry: incorporation · 2020\-12\-11 — “registered 2020\-12\-11”
36. [lupa\.cz](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/) · Independent press · Press article · 2023\-01\-23 — “Filuta AI: Startup Čechů z Microsoftu či Googlu získal největší tuzemskou pre\-seed investici \- Lupa\.cz”
37. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09745424) · Official record · Registry: identity · 2020\-12\-11 — “Filuta AI CZ s\.r\.o\. · s\.r\.o\. · registered 2020\-12\-11”
38. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09745424) · Official record · Registry: shareholder · 2022\-10\-20 — “Filuta AI Inc\. · 100\.0% · from 2022\-10\-20”
39. [filuta\.ai](https://filuta.ai/) · Company's own website · Product capability — “The engine learns a model of the system and explores every state and path inside that scope — then reports what share of it was reached, not how many tests were run\.”
40. [filuta\.ai](https://filuta.ai/) · Company's own website · Product capability — “hands you a coverage number, a reproducible trace for every finding, and a statement of exactly what was proven”
41. [filuta\.ai](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem) · Company's own website · Product capability — “Complete auditability — every test action, finding, and system state was logged with full traceability, meeting the OEM's documentation requirements for safety\-adjacent systems”
42. [github\.com](https://github.com/FilutaAI) · Public technical artifact · GitHub organisation · 2022\-08\-16 — “FilutaAI · 6 public repos”
43. [crt\.sh](https://crt.sh/?q=%25.filuta.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-08\-28 — “api\.demo\.arrow\.filuta\.ai \(first certificate 2025\-08\-28\)”
44. [crt\.sh](https://crt.sh/?q=%25.filuta.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-11\-18 — “docs\.filuta\.ai \(first certificate 2025\-11\-18\)”
45. [filuta\.ai](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem) · Company's own website · Technical claim — “Filuta AI deployed autonomous testing agents directly on the OEM's infotainment hardware\. Rather than executing predefined test scripts, the agents used Composite AI — combining symbolic planning with machine learning — to autonomously explore the system\.”
46. [cc\.cz](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/) · Independent press · Technical claim — “Startup již zároveň vlastní i několik patentovaných řešení, která jeho technologie chrání například v segmentu gamingu a elektronických hraček, v leteckém nebo automobilovém průmyslu, v obranném průmyslu u vojenských simulátorů či v dalších oblastech\.”
47. [patents\.google\.com](https://patents.google.com/patent/AU2024310242A1) · Official record · Patent publication — “AU2024310242A1 · Automated data\-driven domain model synthesis · Filuta Ai Inc\.”
48. [patents\.google\.com](https://patents.google.com/patent/US20250005328A1) · Official record · Patent publication — “US20250005328A1 · System and method for specification, codification, and deployment of composite … · Filuta Ai Inc\.”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 18 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 3 | starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 25 | press:technologickainkubace\.org |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 14 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 48 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 4 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 9 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 3 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 11 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 53 | — |

Analysis: gpt\-5\-mini (cost $0.0098); AI extraction cost $0.0100. Full fact table: CSV export.

## Source appendix (all collected facts)

- F2292 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/09745424](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09745424)
- F2293 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/09745424](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/09745424)
- F2294 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09745424](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09745424)
- F2295 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09745424](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09745424)
- F2296 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09745424](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09745424)
- F2297 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09745424](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09745424)
- F2298 · registry\_flag · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/09745424](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09745424)
- F2299 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2300 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2301 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2302 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2303 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2304 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2305 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2306 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2307 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2308 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1103788](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1103788)
- F2309 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=09745424&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=09745424&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F2310 · web\_page · Sourced · [https://filuta\.ai/](https://filuta.ai/)
- F2311 · web\_page · Sourced · [https://filuta\.ai/privacy\-policy](https://filuta.ai/privacy-policy)
- F2312 · web\_page · Sourced · [https://filuta\.ai/research](https://filuta.ai/research)
- F2313 · web\_page · Sourced · [https://filuta\.ai/case\-studies/how\-hisd\-s\-procurement\-team\-scaled\-compliance\-without\-scaling\-headcount](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
- F2314 · web\_page · Sourced · [https://filuta\.ai/company](https://filuta.ai/company)
- F2315 · web\_page · Sourced · [https://filuta\.ai/team](https://filuta.ai/team)
- F2316 · web\_page · Sourced · [https://filuta\.ai/case\-studies](https://filuta.ai/case-studies)
- F2317 · web\_page · Sourced · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F2318 · web\_page · Sourced · [https://filuta\.ai/case\-studies/scaling\-qa\-open\-world\-rpg](https://filuta.ai/case-studies/scaling-qa-open-world-rpg)
- F2319 · web\_page · Sourced · [https://filuta\.ai/blog](https://filuta.ai/blog)
- F2320 · web\_page · Sourced · [https://filuta\.ai/blog/why\-scripted\-tests\-fail\-modern\-automotive\-software](https://filuta.ai/blog/why-scripted-tests-fail-modern-automotive-software)
- F2321 · web\_page · Sourced · [https://filuta\.ai/blog/the\-qa\-bottleneck\-impacting\-your\-game\-launch](https://filuta.ai/blog/the-qa-bottleneck-impacting-your-game-launch)
- F2322 · web\_page · Sourced · [https://filuta\.ai/hmi\-testing](https://filuta.ai/hmi-testing)
- F2323 · web\_page · Sourced · [https://filuta\.ai/game\-qa](https://filuta.ai/game-qa)
- F2324 · tech\_stack · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F2325 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=filuta\.ai&amp;type=MX](https://dns.google/resolve?name=filuta.ai&type=MX)
- F2326 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=filuta\.ai&amp;type=TXT](https://dns.google/resolve?name=filuta.ai&type=TXT)
- F2327 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2328 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2329 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2330 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2331 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2332 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2333 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2334 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2335 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2336 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2337 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2338 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2339 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2340 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2341 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2342 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2343 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2344 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2345 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2346 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2347 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2348 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2349 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2350 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2351 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2352 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2353 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2354 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2355 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2356 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2357 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2358 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2359 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2360 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2361 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2362 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2363 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2364 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2365 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2366 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2367 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2368 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2369 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2370 · subdomain · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2371 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.filuta\.ai&amp;output=json](https://crt.sh/?q=%25.filuta.ai&output=json)
- F2372 · github\_org · Sourced · [https://github\.com/FilutaAI](https://github.com/FilutaAI)
- F2373 · repo · Sourced · [https://github\.com/FilutaAI/KeyFramer](https://github.com/FilutaAI/KeyFramer)
- F2374 · repo · Sourced · [https://github\.com/FilutaAI/synthesis\-benchmarks](https://github.com/FilutaAI/synthesis-benchmarks)
- F2375 · repo · Sourced · [https://github\.com/FilutaAI/painter\-challenge](https://github.com/FilutaAI/painter-challenge)
- F2376 · paper · Medium confidence · [https://openalex\.org/W4403792769](https://openalex.org/W4403792769)
- F2377 · paper · Medium confidence · [https://openalex\.org/W4414360803](https://openalex.org/W4414360803)
- F2378 · paper · Medium confidence · [https://openalex\.org/W4414359881](https://openalex.org/W4414359881)
- F2379 · paper · Medium confidence · [https://openalex\.org/W7222012453](https://openalex.org/W7222012453)
- F2380 · paper · Medium confidence · [https://openalex\.org/W4392019524](https://openalex.org/W4392019524)
- F2381 · paper · Medium confidence · [https://openalex\.org/W7213511603](https://openalex.org/W7213511603)
- F2382 · paper · Medium confidence · [https://openalex\.org/W4391947855](https://openalex.org/W4391947855)
- F2383 · paper · Medium confidence · [https://openalex\.org/W7220722178](https://openalex.org/W7220722178)
- F2384 · paper · Medium confidence · [https://openalex\.org/W7225419358](https://openalex.org/W7225419358)
- F2385 · wayback\_first · Sourced · [https://web\.archive\.org/web/20230123102450/https://filuta\.ai/](https://web.archive.org/web/20230123102450/https://filuta.ai/)
- F2386 · wayback\_first · Sourced · [https://web\.archive\.org/web/20231211045815/https://filuta\.ai/blog](https://web.archive.org/web/20231211045815/https://filuta.ai/blog)
- F2387 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/filuta\.ai](https://web.archive.org/web/%2A/filuta.ai)
- F2393 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2394 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2395 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2396 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2397 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2398 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2399 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2400 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2401 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2402 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2403 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2404 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2405 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2406 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2407 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2408 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2409 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2410 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2411 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2412 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2413 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/filuta\-ai\-startup\-cechu\-z\-microsoftu\-ci\-googlu\-ziskal\-nejvetsi\-tuzemskou\-pre\-seed\-investici/](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/)
- F2414 · press\_mention · Sourced · [https://cc\.cz/budeme\-jeden\-z\-nejsilnejsich\-tymu\-pro\-vyvoj\-umele\-inteligence\-v\-cesku\-veri\-ziskal\-na\-to\-sto\-milionu/](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/)
- F2415 · press\_mention · Sourced · [https://cc\.cz/ceske\-startupy\-maji\-novy\-rekord\-projekt\-filuta\-funguje\-paty\-mesic\-a\-prave\-ziskal\-56\-milionu/](https://cc.cz/ceske-startupy-maji-novy-rekord-projekt-filuta-funguje-paty-mesic-a-prave-ziskal-56-milionu/)
- F2416 · press\_mention · Sourced · [https://czechstartups\.gov\.cz/en/novinky/investors\-believe\-in\-ai\-investment\-seed\-round\-brings\-filuta\-ai\-startup\-4\-2\-million](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million)
- F2417 · press\_mention · Sourced · [https://www\.focuson\.cz/jen\-co\-vznikl\-uz\-ma\-56\-milionu\-cesky\-startup\-prepisuje\-rekordy](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy)
- F2418 · press\_mention · Sourced · [https://vestbee\.com/insights/articles/filuta\-ai\-secures\-4\-2\-m](https://vestbee.com/insights/articles/filuta-ai-secures-4-2-m)
- F2419 · press\_mention · Sourced · [https://rockawayventures\.com/rockaway\-ventures\-leads\-4\-2m\-seed\-round\-in\-czech\-ai\-startup\-filuta\-ai](https://rockawayventures.com/rockaway-ventures-leads-4-2m-seed-round-in-czech-ai-startup-filuta-ai)
- F2420 · press\_mention · Sourced · [https://czechfounders\.vc/our\-portfolio/filuta\-ai](https://czechfounders.vc/our-portfolio/filuta-ai)
- F2421 · press\_mention · Sourced · [https://czechstartups\.gov\.cz/novinky/investori\-veri\-ai\-investicni\-seed\-kolo\-prineslo\-startupu\-filuta\-ai\-42\-mil\-dolaru/](https://czechstartups.gov.cz/novinky/investori-veri-ai-investicni-seed-kolo-prineslo-startupu-filuta-ai-42-mil-dolaru/)
- F2422 · press\_mention · Sourced · [https://siliconcanals\.com/pragues\-filuta\-ai\-secures\-3\-6m/](https://siliconcanals.com/pragues-filuta-ai-secures-3-6m/)
- F2423 · press\_mention · Sourced · [https://ambit\.law/blog/zastupovali\-jsme\-startup\-filuta\-ai\-pri\-rekordni\-preseedove\-investici](https://ambit.law/blog/zastupovali-jsme-startup-filuta-ai-pri-rekordni-preseedove-investici)
- F2424 · press\_mention · Sourced · [https://ekonomickydenik\.cz/filuta\-ai\-vybral\-miliony\-dolaru/](https://ekonomickydenik.cz/filuta-ai-vybral-miliony-dolaru/)
- F2425 · press\_mention · Sourced · [https://czechstartups\.gov\.cz/novinky/filuta\-ai\-ziska\-30\-mil\-kc\-na\-vyvoj\-samoobsluznych\-ai\-agentu/](https://czechstartups.gov.cz/novinky/filuta-ai-ziska-30-mil-kc-na-vyvoj-samoobsluznych-ai-agentu/)
- F2426 · press\_mention · Sourced · [https://www\.investujeme\.cz/tiskove\-zpravy/novy\-rok\-zacina\-nejvetsi\-ceskou\-pre\-seed\-investici\-umela\-inteligence\-filuta\-filipa\-dvoraka\-ziskava\-temer\-56\-milionu\-korun/](https://www.investujeme.cz/tiskove-zpravy/novy-rok-zacina-nejvetsi-ceskou-pre-seed-investici-umela-inteligence-filuta-filipa-dvoraka-ziskava-temer-56-milionu-korun/)
- F2427 · press\_mention · Sourced · [https://deeptechnews\.eu/2025/06/25/filuta\-ai\-raises\-e3\-7m\-to\-build\-composite\-ai\-solutions\-for\-gaming/](https://deeptechnews.eu/2025/06/25/filuta-ai-raises-e3-7m-to-build-composite-ai-solutions-for-gaming/)
- F2428 · press\_mention · Sourced · [https://en\.ain\.ua/2025/06/25/filuta\-ai\-raises\-42m/](https://en.ain.ua/2025/06/25/filuta-ai-raises-42m/)
- F2429 · press\_mention · Sourced · [https://www\.vestbee\.com/insights/articles/filuta\-ai\-secures\-4\-2\-m](https://www.vestbee.com/insights/articles/filuta-ai-secures-4-2-m)
- F2430 · press\_mention · Sourced · [https://www\.thesaasnews\.com/news/filuta\-ai\-raises\-4\-2\-million\-in\-seed\-round/](https://www.thesaasnews.com/news/filuta-ai-raises-4-2-million-in-seed-round/)
- F2431 · press\_mention · Sourced · [https://www\.therecursive\.com/filuta\-ai\-seed\-rockaway\-ventures\-composite\-ai\-game\-testing/](https://www.therecursive.com/filuta-ai-seed-rockaway-ventures-composite-ai-game-testing/)
- F2432 · press\_mention · Sourced · [https://nordic9\.com/news/filuta\-ai\-closed\-a\-42m\-seed\-round\-led\-by\-rockaway\-ventures\-with\-participation\-from\-lionbeat\-capital\-and\-tarpan\-partners/](https://nordic9.com/news/filuta-ai-closed-a-42m-seed-round-led-by-rockaway-ventures-with-participation-from-lionbeat-capital-and-tarpan-partners/)
- F2433 · press\_mention · Sourced · [https://czechstartups\.gov\.cz/en/novinky/we\-come\-where\-the\-mental\-capacity\-of\-man\-no\-longer\-keeps\-up\-says\-filip\-dvorak\-of\-startup\-filuta\-ai](https://czechstartups.gov.cz/en/novinky/we-come-where-the-mental-capacity-of-man-no-longer-keeps-up-says-filip-dvorak-of-startup-filuta-ai)
- F2434 · press\_mention · Sourced · [https://technologickainkubace\.org/en/startupy/filuta\-ai](https://technologickainkubace.org/en/startupy/filuta-ai)
- F2435 · source\_unavailable · Unavailable · [https://technologickainkubace\.org/wp\-content/uploads/2025/07/TI\_Case\-Study\_TI\-FILUTA\-AI\_online\_ENG\.pdf](https://technologickainkubace.org/wp-content/uploads/2025/07/TI_Case-Study_TI-FILUTA-AI_online_ENG.pdf)
- F2436 · press\_mention · Sourced · [https://czechstartups\.gov\.cz/en/novinky/filuta\-ai\-will\-receive\-30\-mil\-czk\-for\-the\-development\-of\-self\-service\-ai\-agents/](https://czechstartups.gov.cz/en/novinky/filuta-ai-will-receive-30-mil-czk-for-the-development-of-self-service-ai-agents/)
- F2437 · press\_mention · Sourced · [https://cc\.cz/firma\-z\-karlina\-pouziva\-ai\-z\-pruzkumu\-marsu\-pro\-testovani\-her\-usetrime\-miliardy\-dolaru\-hlasi/](https://cc.cz/firma-z-karlina-pouziva-ai-z-pruzkumu-marsu-pro-testovani-her-usetrime-miliardy-dolaru-hlasi/)
- F2438 · press\_mention · Sourced · [https://www\.hybrid\.cz/cesky\-start\-up\-filuta\-ai\-vyviji\-novou\-generaci\-kompozitni\-umele\-inteligence\-ziskal\-tucnou\-investici/](https://www.hybrid.cz/cesky-start-up-filuta-ai-vyviji-novou-generaci-kompozitni-umele-inteligence-ziskal-tucnou-investici/)
- F5437 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-C8BA33B8412EA7002E07855E4ECA1F13263945F6C836AD28D9FBEA85FA85F1D0](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-C8BA33B8412EA7002E07855E4ECA1F13263945F6C836AD28D9FBEA85FA85F1D0)
- F5438 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-4D6C0E515DB6A36794427267495D3E563288718003989E1A7E9203A334A4F31B](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-4D6C0E515DB6A36794427267495D3E563288718003989E1A7E9203A334A4F31B)
- F5439 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/IsVavai\-977DD2CC67E299D573718EC1C9228BB34E4FC92089EF8F2FC763FD0E69BE5D82](https://www.hlidacstatu.cz/Dotace/Detail/IsVavai-977DD2CC67E299D573718EC1C9228BB34E4FC92089EF8F2FC763FD0E69BE5D82)
- F5440 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Filuta%20AI%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Filuta%20AI%27)
- F5441 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F5626 · tech\_claim · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5627 · product\_capability · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5628 · product\_capability · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5629 · tech\_claim · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5630 · team\_claim · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5631 · team\_claim · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5632 · tech\_claim · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5633 · tech\_claim · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5634 · grant\_eu · Medium confidence · [https://filuta\.ai/](https://filuta.ai/)
- F5635 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/how\-hisd\-s\-procurement\-team\-scaled\-compliance\-without\-scaling\-headcount](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
- F5636 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/how\-hisd\-s\-procurement\-team\-scaled\-compliance\-without\-scaling\-headcount](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
- F5637 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/how\-hisd\-s\-procurement\-team\-scaled\-compliance\-without\-scaling\-headcount](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
- F5638 · tech\_claim · Medium confidence · [https://filuta\.ai/case\-studies/how\-hisd\-s\-procurement\-team\-scaled\-compliance\-without\-scaling\-headcount](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
- F5639 · customer · Medium confidence · [https://filuta\.ai/case\-studies/how\-hisd\-s\-procurement\-team\-scaled\-compliance\-without\-scaling\-headcount](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
- F5640 · tech\_claim · Medium confidence · [https://filuta\.ai/case\-studies/how\-hisd\-s\-procurement\-team\-scaled\-compliance\-without\-scaling\-headcount](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
- F5641 · customer · Medium confidence · [https://filuta\.ai/case\-studies](https://filuta.ai/case-studies)
- F5642 · tech\_claim · Medium confidence · [https://filuta\.ai/case\-studies](https://filuta.ai/case-studies)
- F5643 · tech\_claim · Medium confidence · [https://filuta\.ai/case\-studies](https://filuta.ai/case-studies)
- F5644 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F5645 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F5646 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F5647 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F5648 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F5649 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F5650 · integration · Medium confidence · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F5651 · tech\_claim · Medium confidence · [https://filuta\.ai/case\-studies/autonomous\-hmi\-testing\-european\-automotive\-oem](https://filuta.ai/case-studies/autonomous-hmi-testing-european-automotive-oem)
- F5652 · tech\_claim · Medium confidence · [https://filuta\.ai/case\-studies/scaling\-qa\-open\-world\-rpg](https://filuta.ai/case-studies/scaling-qa-open-world-rpg)
- F5653 · product\_capability · Medium confidence · [https://filuta\.ai/case\-studies/scaling\-qa\-open\-world\-rpg](https://filuta.ai/case-studies/scaling-qa-open-world-rpg)
- F5654 · customer · Medium confidence · [https://filuta\.ai/case\-studies/scaling\-qa\-open\-world\-rpg](https://filuta.ai/case-studies/scaling-qa-open-world-rpg)
- F5655 · tech\_claim · Medium confidence · [https://filuta\.ai/case\-studies/scaling\-qa\-open\-world\-rpg](https://filuta.ai/case-studies/scaling-qa-open-world-rpg)
- F5656 · tech\_claim · Medium confidence · [https://filuta\.ai/company](https://filuta.ai/company)
- F5657 · tech\_claim · Medium confidence · [https://filuta\.ai/company](https://filuta.ai/company)
- F5658 · product\_capability · Medium confidence · [https://filuta\.ai/company](https://filuta.ai/company)
- F5659 · team\_claim · Medium confidence · [https://filuta\.ai/company](https://filuta.ai/company)
- F5660 · funding\_round · Medium confidence · [https://www\.lupa\.cz/aktuality/filuta\-ai\-startup\-cechu\-z\-microsoftu\-ci\-googlu\-ziskal\-nejvetsi\-tuzemskou\-pre\-seed\-investici/](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/)
- F5662 · product\_capability · Medium confidence · [https://www\.lupa\.cz/aktuality/filuta\-ai\-startup\-cechu\-z\-microsoftu\-ci\-googlu\-ziskal\-nejvetsi\-tuzemskou\-pre\-seed\-investici/](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/)
- F5663 · tech\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/filuta\-ai\-startup\-cechu\-z\-microsoftu\-ci\-googlu\-ziskal\-nejvetsi\-tuzemskou\-pre\-seed\-investici/](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/)
- F5664 · team\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/filuta\-ai\-startup\-cechu\-z\-microsoftu\-ci\-googlu\-ziskal\-nejvetsi\-tuzemskou\-pre\-seed\-investici/](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/)
- F5665 · team\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/filuta\-ai\-startup\-cechu\-z\-microsoftu\-ci\-googlu\-ziskal\-nejvetsi\-tuzemskou\-pre\-seed\-investici/](https://www.lupa.cz/aktuality/filuta-ai-startup-cechu-z-microsoftu-ci-googlu-ziskal-nejvetsi-tuzemskou-pre-seed-investici/)
- F5666 · funding\_round · Medium confidence · [https://cc\.cz/budeme\-jeden\-z\-nejsilnejsich\-tymu\-pro\-vyvoj\-umele\-inteligence\-v\-cesku\-veri\-ziskal\-na\-to\-sto\-milionu/](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/)
- F5667 · team\_claim · Medium confidence · [https://cc\.cz/budeme\-jeden\-z\-nejsilnejsich\-tymu\-pro\-vyvoj\-umele\-inteligence\-v\-cesku\-veri\-ziskal\-na\-to\-sto\-milionu/](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/)
- F5668 · product\_capability · Medium confidence · [https://cc\.cz/budeme\-jeden\-z\-nejsilnejsich\-tymu\-pro\-vyvoj\-umele\-inteligence\-v\-cesku\-veri\-ziskal\-na\-to\-sto\-milionu/](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/)
- F5669 · tech\_claim · Medium confidence · [https://cc\.cz/budeme\-jeden\-z\-nejsilnejsich\-tymu\-pro\-vyvoj\-umele\-inteligence\-v\-cesku\-veri\-ziskal\-na\-to\-sto\-milionu/](https://cc.cz/budeme-jeden-z-nejsilnejsich-tymu-pro-vyvoj-umele-inteligence-v-cesku-veri-ziskal-na-to-sto-milionu/)
- F5670 · team\_claim · Medium confidence · [https://cc\.cz/ceske\-startupy\-maji\-novy\-rekord\-projekt\-filuta\-funguje\-paty\-mesic\-a\-prave\-ziskal\-56\-milionu/](https://cc.cz/ceske-startupy-maji-novy-rekord-projekt-filuta-funguje-paty-mesic-a-prave-ziskal-56-milionu/)
- F5671 · product\_capability · Medium confidence · [https://czechstartups\.gov\.cz/en/novinky/investors\-believe\-in\-ai\-investment\-seed\-round\-brings\-filuta\-ai\-startup\-4\-2\-million](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million)
- F5672 · funding\_round · Medium confidence · [https://czechstartups\.gov\.cz/en/novinky/investors\-believe\-in\-ai\-investment\-seed\-round\-brings\-filuta\-ai\-startup\-4\-2\-million](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million)
- F5673 · tech\_claim · Medium confidence · [https://czechstartups\.gov\.cz/en/novinky/investors\-believe\-in\-ai\-investment\-seed\-round\-brings\-filuta\-ai\-startup\-4\-2\-million](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million)
- F5674 · team\_claim · Medium confidence · [https://czechstartups\.gov\.cz/en/novinky/investors\-believe\-in\-ai\-investment\-seed\-round\-brings\-filuta\-ai\-startup\-4\-2\-million](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million)
- F5675 · funding\_round · Medium confidence · [https://www\.focuson\.cz/jen\-co\-vznikl\-uz\-ma\-56\-milionu\-cesky\-startup\-prepisuje\-rekordy](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy)
- F5676 · tech\_claim · Medium confidence · [https://www\.focuson\.cz/jen\-co\-vznikl\-uz\-ma\-56\-milionu\-cesky\-startup\-prepisuje\-rekordy](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy)
- F5677 · product\_capability · Medium confidence · [https://www\.focuson\.cz/jen\-co\-vznikl\-uz\-ma\-56\-milionu\-cesky\-startup\-prepisuje\-rekordy](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy)
- F5678 · customer · Medium confidence · [https://www\.focuson\.cz/jen\-co\-vznikl\-uz\-ma\-56\-milionu\-cesky\-startup\-prepisuje\-rekordy](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy)
- F5679 · customer · Medium confidence · [https://www\.focuson\.cz/jen\-co\-vznikl\-uz\-ma\-56\-milionu\-cesky\-startup\-prepisuje\-rekordy](https://www.focuson.cz/jen-co-vznikl-uz-ma-56-milionu-cesky-startup-prepisuje-rekordy)
- F6353 · patent · Sourced · [https://patents\.google\.com/patent/US20250005318A1](https://patents.google.com/patent/US20250005318A1)
- F6354 · patent · Sourced · [https://patents\.google\.com/patent/AU2024310242A1](https://patents.google.com/patent/AU2024310242A1)
- F6355 · patent · Sourced · [https://patents\.google\.com/patent/US20250005328A1](https://patents.google.com/patent/US20250005328A1)
- F6356 · patent · Sourced · [https://patents\.google\.com/patent/EP4720840A1](https://patents.google.com/patent/EP4720840A1)
- F6357 · patent · Sourced · [https://patents\.google\.com/patent/CA3292812A1](https://patents.google.com/patent/CA3292812A1)
- F6358 · verification · Sourced · [https://patents\.google\.com/?assignee=filuta](https://patents.google.com/?assignee=filuta)
- F6359 · verification · Sourced · [https://patents\.google\.com/?assignee=filuta](https://patents.google.com/?assignee=filuta)
- F6360 · verification · Sourced · [https://filuta\.ai/case\-studies/how\-hisd\-s\-procurement\-team\-scaled\-compliance\-without\-scaling\-headcount](https://filuta.ai/case-studies/how-hisd-s-procurement-team-scaled-compliance-without-scaling-headcount)
- F6361 · verification · Sourced · [https://czechfounders\.vc/our\-portfolio/filuta\-ai](https://czechfounders.vc/our-portfolio/filuta-ai)
- F6362 · verification · Sourced · [https://czechfounders\.vc/our\-portfolio/filuta\-ai](https://czechfounders.vc/our-portfolio/filuta-ai)
- F6363 · verification · Sourced · [https://dir\.texas\.gov/contracts/vendors/filuta\-ai\-inc](https://dir.texas.gov/contracts/vendors/filuta-ai-inc)
