# Upheal — due diligence brief

upheal\.io · Upheal s\.r\.o\. · IČO 14138018 · CZ · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A clinician\-facing AI EHR that drafts therapy notes, offers telehealth, scheduling, billing and managed insurance billing for individual clinicians and group practices\. *(Partly verified)* ^[1](https://www.upheal.io/features/ai-assistant),[2](https://www.upheal.io/),[3](https://www.upheal.io/),[4](https://www.upheal.io/features/managed-insurance-billing),[5](https://mentalhealthinvestors.com/startups/upheal)
- **Stage & traction.** Multiple press\-reported funding rounds \(≈$4\.35M and 76M CZK reported in Feb 2024\), named commercial partners and claimed scale of 90k sessions processed in 12 months\. *(Corroborated)* ^[6](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[7](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/),[8](https://vestbee.com/insights/articles/upheal-secures-10-m),[9](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[10](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
- **Technology & moat.** Documented product surfaces, clinical templates and docs \+ managed\-billing workflow appear sticky; no public evidence of proprietary models or unique core ML IP\. *(Company claim)* ^[11](https://www.upheal.io/documentation/intake-form-template),[12](https://www.upheal.io/documentation/progress-note-template),[13](https://www.upheal.io/features/ai-clinical-notes),[14](https://www.upheal.io/features/managed-insurance-billing),[15](https://www.upheal.io/features/ai-clinical-notes)
- **Key risk.** Heavy unverified claims around SOC2/HIPAA posture and AI accuracy/volume benefits — verification is partial and depends on reviewing attestation and raw metrics\. *(Analyst view)* ^[16](https://trust.upheal.io),[17](https://www.upheal.io/),[9](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[10](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
- **Diligence focus.** Obtain SOC2 Type II report and the security attestation, and request raw session\-scaling and accuracy logs that back the 90k sessions / 21k hours claim\. *(Analyst view)* ^[16](https://trust.upheal.io),[9](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[10](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2024\-02\-28 · $4\.35 million; 2024\-11\-14 · Series Seed; 2024\-11\-18 · seed · 76,000,000 CZK | 6, 18, 7 |
| Thesis fit \(Rockaway\) | sectors: AI\-led transformative tech \(19 facts\) · geography: CZ \(core region\) | 19, 20 |
| Engineering footprint | product surfaces: auth\.upheal\.io, status\.upheal\.io; 5 docs pages; stack: Cloudflare, Webflow | 21, 22, 23, 11 |
| Customers | public pricing: yes; 1 mobile app\(s\) | 24 |
| Claims checked | SOC 2 / ISO: partly | 16 |
| Timeline | Czech entity registered 2022\-01\-10; first press 2022\-10\-18 \(19 articles collected\) | 25, 26 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the market, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** AI\-native clinical EHR / workflow automation for mental\-health clinicians — positioning matches the fund’s AI\-led transformative tech thesis\. *(Analyst view)* ^[2](https://www.upheal.io/),[15](https://www.upheal.io/features/ai-clinical-notes),[1](https://www.upheal.io/features/ai-assistant),[27](https://www.upheal.io/features/ai-assistant)
  - Assumption: Company positioning remains product\-led B2B SaaS\.

## Business model

- Primary revenue: subscription plans selling AI Notes and Assistant Pro to individual clinicians\. *(Analyst view)* ^[24](https://www.upheal.io/),[28](https://www.upheal.io/features/ai-assistant),[5](https://mentalhealthinvestors.com/startups/upheal)
  - Assumption: Pricing pages reflect actual customer billing\.
- Alternate revenue: full EHR paid per completed session \(stated $1/session\) and EHR Pro monthly fees\. *(Analyst view)* ^[29](https://www.upheal.io/pricing),[30](https://www.upheal.io/pricing),[31](https://www.upheal.io/features/ehr)
  - Assumption: Per\-session plan is commercially available\.
- Managed\-insurance billing offered as a pay\-for\-performance service \(vendor files claims and is paid when provider is paid\)\. *(Analyst view)* ^[14](https://www.upheal.io/features/managed-insurance-billing),[4](https://www.upheal.io/features/managed-insurance-billing),[32](https://www.upheal.io/features/managed-insurance-billing)
  - Assumption: Operational billing team exists at scale\.

## Market

- Customer segment: private\-practice mental\-health clinicians and group practices \(explicitly sells subscriptions to clinicians and practices\)\. *(Analyst view)* ^[33](https://mentalhealthinvestors.com/startups/upheal),[5](https://mentalhealthinvestors.com/startups/upheal)
  - Assumption: Target buyer is clinician / practice decision\-maker\.
- Demand signal: company reports processing 90,000 sessions last 12 months and \~25,000 sessions per month, claiming time savings\. *(Analyst view)* ^[9](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[10](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
  - Assumption: Company usage claims are accurate\.
- Geographic footprint claim: customers across US states and 23 countries, with 90% based in the United States \(company press release\)\. *(Analyst view)* ^[34](https://www.einpresswire.com/article/918347087/upheal-releases-2026-provider-experience-report-on-ai-documentation-and-therapist-burnout)
  - Assumption: Distribution implies US product\-market fit\.

## Competition

No sourced findings for this section.

## Case for and against

- **For:** Demonstrated usage scale — company reports 90k sessions processed in 12 months and \~25k monthly sessions, implying adoption and product utility\. *(Analyst view)* ^[9](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[10](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
  - Assumption: Reported sessions correspond to paying or active users\.
- **For:** Multiple monetisation paths — per‑session EHR, subscription AI Notes, Assistant Pro, and managed billing expand ARPU levers\. *(Analyst view)* ^[24](https://www.upheal.io/),[29](https://www.upheal.io/pricing),[28](https://www.upheal.io/features/ai-assistant),[32](https://www.upheal.io/features/managed-insurance-billing)
  - Assumption: Customers convert across multiple paid products\.
- **For:** Compliance and security claims \(HIPAA, SOC 2 Type II\) support enterprise / payer integrations and US\-market selling\. *(Analyst view)* ^[16](https://trust.upheal.io),[35](https://www.upheal.io/pricing),[27](https://www.upheal.io/features/ai-assistant)
  - Assumption: Claims correspond to verifiable attestation documents\.
- **Against:** Security attestation access limited — public pointer found but SOC2 report reportedly only shared under NDA; verification risk for enterprise buyers\. *(Analyst view)* ^[16](https://trust.upheal.io)
  - Assumption: Enterprises require direct evidence of attestation\.
- **Against:** Funding history shows multiple rounds and conflicting public reports on amounts \(several press\-notes of large seed rounds\), complicating cap‑table and runway assumptions\. *(Analyst view)* ^[6](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[7](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/),[36](https://vestbee.com/insights/articles/upheal-secures-10-m)
  - Assumption: Press reports reflect real but varying round disclosures\.
- **Must be true:** Confirm paid‑customer conversion and revenue per session/subscription \(billing data, MRR or ARR\) to validate monetisation claims\. *(Analyst view)* ^[24](https://www.upheal.io/),[31](https://www.upheal.io/features/ehr),[28](https://www.upheal.io/features/ai-assistant),[34](https://www.einpresswire.com/article/918347087/upheal-releases-2026-provider-experience-report-on-ai-documentation-and-therapist-burnout)
  - Assumption: Public pricing maps to real customer payments\.

# Technical due diligence

## Ownership and capital

- Legal: Upheal s\.r\.o\. registered in Czech Republic on 2022\-01\-10 with 20,000 CZK capital; Upheal, Inc\. \(US\) recorded as 100% shareholder since 2022\-08\-29\. *(Verified)* ^[37](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14138018),[38](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018),[39](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- Funding history \(press\-reported\): press records show a $4\.35M round and separate reports of a 76,000,000 CZK seed round in Feb 2024; later press mentions a Series Seed/€ figures\. *(Corroborated)* ^[6](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[7](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/),[18](https://vestbee.com/insights/articles/upheal-secures-10-m)

## Technology profile

- Product surfaces and docs: public documentation site with multiple clinical\-template pages and a Play Store app for session capture\. *(Partly verified)* ^[23](https://www.upheal.io/documentation),[11](https://www.upheal.io/documentation/intake-form-template),[12](https://www.upheal.io/documentation/progress-note-template),[40](https://www.upheal.io/features/session-formats)
- Capabilities claimed: AI\-generated SOAP/DAP/GIRP notes, one\-click EHR browser integration, automatic post\-session notes, AI treatment plans, compliance checker and billing automation\. *(Company claim)* ^[41](https://www.upheal.io/features/ai-clinical-notes),[15](https://www.upheal.io/features/ai-clinical-notes),[42](https://www.upheal.io/features/ai-clinical-notes),[43](https://www.upheal.io/features/ai-clinical-notes),[44](https://www.upheal.io/features/ai-clinical-notes)
- Engineering footprint and stack: site hosted via Cloudflare and built on Webflow; AWS listed as a cloud subprocessor; a public trust subdomain references a security attestation pointer\. *(Partly verified)* ^[45](https://www.upheal.io/),[46](https://www.upheal.io/),[47](https://www.upheal.io/),[48](https://www.upheal.io/privacy-and-compliance),[16](https://trust.upheal.io)

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** Clinical templates, note generation UI, and one\-click browser extension integration could be reproduced using open NLP libraries, a browser extension API, and standard EHR connectors\. *(Analyst view)* ^[13](https://www.upheal.io/features/ai-clinical-notes),[41](https://www.upheal.io/features/ai-clinical-notes),[15](https://www.upheal.io/features/ai-clinical-notes)
  - Assumption: NLP quality equal to Upheal not proven; assumes basic template logic\.
- **Edge supported by public evidence:** Claimed operational scale \(90,000 sessions processed; 25k monthly sessions\) is public evidence of usage and potential product\-market fit if logs verify it\. *(Analyst view)* ^[9](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[10](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
  - Assumption: Press\-reported numbers reflect platform\-processed sessions, not third\-party counts\.
- **Cannot be judged from outside:** AI model quality, hallucination rates, payer\-appeal success rates, and managed\-billing unit economics cannot be judged without code, raw transcripts, claims outcome data and team access\. *(Analyst view)* ^[14](https://www.upheal.io/features/managed-insurance-billing),[42](https://www.upheal.io/features/ai-clinical-notes),[9](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc)
  - Assumption: External artifacts are required to evaluate accuracy and economics\.

## Risks and caveats

- Unverified security posture: SOC2/HIPAA claims only partly corroborated by a trust subdomain pointer; full report shared only under NDA\. *(Analyst view)* ^[16](https://trust.upheal.io),[17](https://www.upheal.io/)
  - Assumption: Full attestations must be reviewed to confirm compliance\.
- Concentration: reported reliance on press\-reported funding announcements \(multiple overlapping articles\) for traction narrative; investor registry entries are not supplied here\. *(Analyst view)* ^[6](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[36](https://vestbee.com/insights/articles/upheal-secures-10-m),[49](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/)
  - Assumption: Press coverage may overstate investor composition without registry confirmation\.
- Tech/IP gap: no public evidence of proprietary models, patents, or verified model ownership in supplied facts — moat may be operational and contractual rather than technical\. *(Analyst view)* ^[11](https://www.upheal.io/documentation/intake-form-template),[13](https://www.upheal.io/features/ai-clinical-notes),[2](https://www.upheal.io/)
  - Assumption: Absence of model evidence in dataset implies need to verify IP\.

## Questions for founders

- Please provide the SOC2 Type II report and scope; verification fact shows only an attestation pointer\. *(Analyst view)* ^[16](https://trust.upheal.io)
  - Assumption: Full report will confirm controls and data processing scope\.
- Request raw logs or a third‑party audit substantiating the 90,000 sessions and 21,000 hours saved claim, which currently appears in press statements\. *(Analyst view)* ^[9](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[10](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
  - Assumption: Logs or analytics exports will show session counts and processing timestamps\.
- Ask for evidence on model provenance and vendor dependencies: does Upheal use third‑party LLM APIs or own models? No LLM vendor facts are provided\. *(Analyst view)* ^[2](https://www.upheal.io/),[50](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/)
  - Assumption: Vendor contracts or architecture diagrams will reveal dependencies\.
- Obtain managed\-billing unit economics and claims success metrics that back the pay‑when‑paid business model and asserted billing workflows\. *(Analyst view)* ^[14](https://www.upheal.io/features/managed-insurance-billing),[4](https://www.upheal.io/features/managed-insurance-billing),[32](https://www.upheal.io/features/managed-insurance-billing)
  - Assumption: Claims outcome and revenue share data are required to assess economics\.

## Sources

1. [upheal\.io](https://www.upheal.io/features/ai-assistant) · Company's own website · Product capability — “Session prep, letters, scheduling, invoices and claims\. Upheal’s AI Assistant works from your chart, calendar and billing, so it finishes the job, not just the draft\.”
2. [upheal\.io](https://www.upheal.io/) · Company's own website · Product capability — “Your AI progress note is ready in 60 seconds”
3. [upheal\.io](https://www.upheal.io/) · Company's own website · Product capability — “Your calendar, intake forms, telehealth, billing and client portal sit right next to your notes\.”
4. [upheal\.io](https://www.upheal.io/features/managed-insurance-billing) · Company's own website · Product capability — “We track and chase Status monitored, rejections corrected, denials worked, appeals filed, statements sent\.”
5. [mentalhealthinvestors\.com](https://mentalhealthinvestors.com/startups/upheal) · Independent press · Pricing — “It sells subscriptions to individual clinicians and group practices\.”
6. [en\.ain\.ua](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc) · Independent press · Funding round — “In total, Upheal raised $4\.35 million of funding\.”
7. [cc\.cz](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/) · Independent press · Funding round — “seedové investiční kolo ve výši 76 milionů korun pak Upheal oznamoval letos v únoru”
8. [vestbee\.com](https://vestbee.com/insights/articles/upheal-secures-10-m) · Independent press · Integration — “Upheal has partnered with Alma, Cartwheel Care, Author Health, Noble Health, and Insight Counseling\.”
9. [en\.ain\.ua](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc) · Independent press · Technical claim — “The company claims it has processed 90,000 sessions in the last 12 months, and saved mental health professionals 21,000 hours\.”
10. [cc\.cz](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/) · Independent press · Technical claim — “Během posledních dvanácti měsíců zpracoval 90 tisíc sezení, čímž terapeutům ušetřil 21 tisíc hodin\. Každý měsíc zpracovává nyní 25 tisíc sezení\.”
11. [upheal\.io](https://www.upheal.io/documentation/intake-form-template) · Company's own website · Website page — “Intake Form Template for Mental Health \(Updates for 2026\)”
12. [upheal\.io](https://www.upheal.io/documentation/progress-note-template) · Company's own website · Website page — “Writing great progress notes: when to use which template and why”
13. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Upheal creates AI\-generated notes in ten formats: SOAP, DAP, GIRP, BIRP, EMDR, PIRP, SIRP, PIE, Intake, and Mental Status Exam \(MSE\)\. You can use any of these as\-is, or build your own template from 170 clinically approved sections to match your preferred style and payer requirements\.”
14. [upheal\.io](https://www.upheal.io/features/managed-insurance-billing) · Company's own website · Product capability — “You sign the note\. The rest is on us\. You Finish your session Upheal drafts an insurance‑ready note from the session\. You review and sign\. Upheal We file the claim”
15. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Or use our browser extension to fill your notes into your EHR with one click\.”
16. [trust\.upheal\.io](https://trust.upheal.io) · Company's own website · Independent check of a claim — “Public attestation pointer found: subdomain trust\.upheal\.io\. The report itself is shared under NDA — request it\.”
17. [upheal\.io](https://www.upheal.io/) · Company's own website · Technical claim — “SOC 2 Type II”
18. [vestbee\.com](https://vestbee.com/insights/articles/upheal-secures-10-m) · Independent press · Funding round — “since its Series Seed funding in February 2024”
19. [cc\.cz](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/) · Independent press · Press article · 2024\-02\-27 — “Češi díky AI dávají terapeutům superchopnosti\. Nabírají 76 milionů \- CzechCrunch”
20. [tech\.eu](https://tech.eu/2022/10/19/upheal-raises-eur168-million-and-launches-ai-powered-notes-app-for-mental-health-care-professionals/) · Independent press · Press article · 2022\-10\-19 — “Upheal raises €1\.068 million and launches AI\-powered notes app for mental health care professionals \- Tech\.eu”
21. [crt\.sh](https://crt.sh/?q=%25.upheal.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-06\-09 — “auth\.upheal\.io \(first certificate 2023\-06\-09\)”
22. [crt\.sh](https://crt.sh/?q=%25.upheal.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-08\-21 — “status\.upheal\.io \(first certificate 2023\-08\-21\)”
23. [upheal\.io](https://www.upheal.io/documentation) · Company's own website · Website page — “Documentation \| Upheal”
24. [upheal\.io](https://www.upheal.io/) · Company's own website · Pricing — “AI Notes is $39/month for unlimited AI notes\.”
25. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14138018) · Official record · Registry: incorporation · 2022\-01\-10 — “registered 2022\-01\-10”
26. [cc\.cz](https://cc.cz/dava-terapeutum-superschopnosti-umela-inteligence-z-ceska-posloucha-s-lekarem-ziskala-25-milionu/) · Independent press · Press article · 2022\-10\-18 — “Umělá inteligence poslouchající s terapeutem přilákala 25 milionů \- CzechCrunch”
27. [upheal\.io](https://www.upheal.io/features/ai-assistant) · Company's own website · Technical claim — “HIPAA Compliant PHIPA Compliant SOC 2 Type II GDPR Compliant Asks before it acts”
28. [upheal\.io](https://www.upheal.io/features/ai-assistant) · Company's own website · Pricing — “Assistant Pro, with unlimited AI Assistant and session prep, is $39 per month on any paid plan, and it is included in EHR Pro at $99 per month\.”
29. [upheal\.io](https://www.upheal.io/pricing) · Company's own website · Pricing — “$1 / session Paid per session\.”
30. [upheal\.io](https://www.upheal.io/pricing) · Company's own website · Pricing — “$99 / month Flat fee”
31. [upheal\.io](https://www.upheal.io/features/ehr) · Company's own website · Pricing — “Is there an EHR for private practice under $100 per month? Yes\. Upheal's EHR is $1 per completed session, pay as you go, so a 10\-session week costs about $43 a month\. EHR Pro is $99 per month flat for unlimited sessions with Assistant Pro included”
32. [upheal\.io](https://www.upheal.io/features/managed-insurance-billing) · Company's own website · Pricing — “Pay when you get paid Your NPI, your contracts No minimums”
33. [mentalhealthinvestors\.com](https://mentalhealthinvestors.com/startups/upheal) · Independent press · Product capability — “AI therapy notes plus scheduling, billing and EHR features for mental health providers\.”
34. [einpresswire\.com](https://www.einpresswire.com/article/918347087/upheal-releases-2026-provider-experience-report-on-ai-documentation-and-therapist-burnout) · Independent press · Press article · 2026\-06\-11 — “Upheal Releases 2026 Provider Experience Report on AI Documentation and Therapist Burnout”
35. [upheal\.io](https://www.upheal.io/pricing) · Company's own website · Technical claim — “HIPAA\-compliant telehealth Upheal’s own secure, HIPAA\-compliant video calling platform\.”
36. [vestbee\.com](https://vestbee.com/insights/articles/upheal-secures-10-m) · Independent press · Press article · 2024\-11\-14 — “Czech\-US mental health platform for clinicians Upheal secures $10M\. Headline led the round \| Vestbee”
37. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14138018) · Official record · Registry: identity · 2022\-01\-10 — “Upheal s\.r\.o\. · s\.r\.o\. · registered 2022\-01\-10”
38. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018) · Official record · Registry: registered capital · 2022\-01\-10 — “20 000 CZK”
39. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018) · Official record · Registry: shareholder · 2022\-08\-29 — “Upheal, Inc\. · 100\.0% · from 2022\-08\-29”
40. [upheal\.io](https://www.upheal.io/features/session-formats) · Public technical artifact · Mobile app
41. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Upheal generates SOAP, DAP, GIRP, and other clinical note formats automatically from your sessions\.”
42. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Progress notes and transcripts are instantly created after every session, so you can stay focused on your clients\.”
43. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Insurance\-compliant Treatment Plans are generated from past sessions and automatically update as your client progresses\.”
44. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Technical claim — “Compliance Checker gives you peace of mind by flagging missing elements, aligning with payer standards, and ensuring your notes are audit\-ready\.”
45. [upheal\.io](https://www.upheal.io/) · Public technical artifact · Technology detected
46. [upheal\.io](https://www.upheal.io/) · Public technical artifact · Technology detected
47. [upheal\.io](https://www.upheal.io/) · Public technical artifact · Technology detected
48. [upheal\.io](https://www.upheal.io/privacy-and-compliance) · Company's own website · Subprocessor \(privacy policy\) — “In addition, we use AWS for our cloud infrastructure and storage, a highly secure and reliable vendor\.”
49. [cc\.cz](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/) · Independent press · Press article · 2024\-11\-18 — “Kvůli synově nemoci vyhořel\. Jeho startup teď pomáhá terapeutům \- CzechCrunch”
50. [cc\.cz](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/) · Independent press · Technical claim — “Upheal, který za ně automaticky i díky umělé inteligenci sepisuje poznámky ze sezení, třídí je a hledá v nich souvislosti”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 14 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 19 | press:akta\.pro, press:axios\.com, press:birpnotes\.com, press:siliconlegal\.com, press:trustpilot\.com |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 32 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 37 | — |
| Mobile apps | App Store \(seller must match the company\), Google Play if linked from the site | 1 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 5 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 1 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 57 | — |

Analysis: gpt\-5\-mini (cost $0.0179); AI extraction cost $0.0087. Full fact table: CSV export.

## Source appendix (all collected facts)

- F4271 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14138018)
- F4272 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14138018)
- F4273 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- F4274 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- F4275 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- F4276 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- F4277 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- F4278 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- F4279 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- F4280 · registry\_flag · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14138018](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- F4281 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145979](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145979)
- F4282 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145979](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145979)
- F4283 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145979](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145979)
- F4284 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=14138018&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=14138018&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F4285 · web\_page · Sourced · [https://www\.upheal\.io/](https://www.upheal.io/)
- F4286 · web\_page · Sourced · [https://www\.upheal\.io/privacy\-and\-compliance](https://www.upheal.io/privacy-and-compliance)
- F4287 · subprocessor · Medium confidence · [https://www\.upheal\.io/privacy\-and\-compliance](https://www.upheal.io/privacy-and-compliance)
- F4288 · web\_page · Sourced · [https://www\.upheal\.io/careers](https://www.upheal.io/careers)
- F4289 · web\_page · Sourced · [https://www\.upheal\.io/careers/head\-of\-design](https://www.upheal.io/careers/head-of-design)
- F4290 · web\_page · Sourced · [https://www\.upheal\.io/careers/full\-stack\-growth\-marketer](https://www.upheal.io/careers/full-stack-growth-marketer)
- F4291 · web\_page · Sourced · [https://www\.upheal\.io/features/ai\-assistant/jobs](https://www.upheal.io/features/ai-assistant/jobs)
- F4292 · web\_page · Sourced · [https://www\.upheal\.io/privacy\-and\-compliance/business\-associate\-agreement](https://www.upheal.io/privacy-and-compliance/business-associate-agreement)
- F4293 · web\_page · Sourced · [https://www\.upheal\.io/en\-ca/careers](https://www.upheal.io/en-ca/careers)
- F4294 · web\_page · Sourced · [https://www\.upheal\.io/en\-ie/careers](https://www.upheal.io/en-ie/careers)
- F4295 · web\_page · Sourced · [https://www\.upheal\.io/privacy\-and\-compliance/hipaa\-compliance](https://www.upheal.io/privacy-and-compliance/hipaa-compliance)
- F4296 · web\_page · Sourced · [https://www\.upheal\.io/en\-ca/privacy\-and\-compliance](https://www.upheal.io/en-ca/privacy-and-compliance)
- F4297 · subprocessor · Medium confidence · [https://www\.upheal\.io/en\-ca/privacy\-and\-compliance](https://www.upheal.io/en-ca/privacy-and-compliance)
- F4298 · web\_page · Sourced · [https://www\.upheal\.io/en\-ca/careers/head\-of\-design](https://www.upheal.io/en-ca/careers/head-of-design)
- F4299 · web\_page · Sourced · [https://www\.upheal\.io/en\-ie/careers/head\-of\-design](https://www.upheal.io/en-ie/careers/head-of-design)
- F4300 · web\_page · Sourced · [https://www\.upheal\.io/en\-ca/careers/full\-stack\-growth\-marketer](https://www.upheal.io/en-ca/careers/full-stack-growth-marketer)
- F4301 · web\_page · Sourced · [https://www\.upheal\.io/en\-ie/careers/full\-stack\-growth\-marketer](https://www.upheal.io/en-ie/careers/full-stack-growth-marketer)
- F4302 · web\_page · Sourced · [https://www\.upheal\.io/documentation](https://www.upheal.io/documentation)
- F4303 · web\_page · Sourced · [https://www\.upheal\.io/pricing](https://www.upheal.io/pricing)
- F4304 · web\_page · Sourced · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F4305 · web\_page · Sourced · [https://www\.upheal\.io/features/ehr](https://www.upheal.io/features/ehr)
- F4306 · web\_page · Sourced · [https://www\.upheal\.io/features/ai\-assistant](https://www.upheal.io/features/ai-assistant)
- F4307 · web\_page · Sourced · [https://www\.upheal\.io/features/managed\-insurance\-billing](https://www.upheal.io/features/managed-insurance-billing)
- F4308 · web\_page · Sourced · [https://www\.upheal\.io/features/growth\-audit](https://www.upheal.io/features/growth-audit)
- F4309 · web\_page · Sourced · [https://www\.upheal\.io/features/session\-formats](https://www.upheal.io/features/session-formats)
- F4310 · web\_page · Sourced · [https://www\.upheal\.io/features/treatment\-plans](https://www.upheal.io/features/treatment-plans)
- F4311 · web\_page · Sourced · [https://www\.upheal\.io/features/compliance\-checker](https://www.upheal.io/features/compliance-checker)
- F4312 · web\_page · Sourced · [https://www\.upheal\.io/documentation/intake\-form\-template](https://www.upheal.io/documentation/intake-form-template)
- F4313 · web\_page · Sourced · [https://www\.upheal\.io/documentation/progress\-note\-template](https://www.upheal.io/documentation/progress-note-template)
- F4314 · web\_page · Sourced · [https://www\.upheal\.io/documentation/soap\-note\-example\-2026](https://www.upheal.io/documentation/soap-note-example-2026)
- F4315 · web\_page · Sourced · [https://www\.upheal\.io/documentation/dap\-note\-example](https://www.upheal.io/documentation/dap-note-example)
- F4316 · web\_page · Sourced · [https://www\.upheal\.io/en\-ca/features/compliance\-checker](https://www.upheal.io/en-ca/features/compliance-checker)
- F4317 · tech\_stack · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F4318 · tech\_stack · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F4319 · tech\_stack · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F4320 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=upheal\.io&amp;type=MX](https://dns.google/resolve?name=upheal.io&type=MX)
- F4321 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=upheal\.io&amp;type=TXT](https://dns.google/resolve?name=upheal.io&type=TXT)
- F4322 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=upheal\.io&amp;type=TXT](https://dns.google/resolve?name=upheal.io&type=TXT)
- F4323 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4324 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4325 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4326 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4327 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4328 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4329 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4330 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4331 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4332 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4333 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4334 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4335 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4336 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4337 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4338 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4339 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4340 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4341 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4342 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4343 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4344 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4345 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4346 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4347 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4348 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4349 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4350 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4351 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4352 · subdomain · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4353 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.upheal\.io&amp;output=json](https://crt.sh/?q=%25.upheal.io&output=json)
- F4354 · app · Medium confidence · [https://www\.upheal\.io/features/session\-formats](https://www.upheal.io/features/session-formats)
- F4355 · wayback\_first · Sourced · [https://web\.archive\.org/web/20211222144604/https://upheal\.io/](https://web.archive.org/web/20211222144604/https://upheal.io/)
- F4356 · wayback\_first · Sourced · [https://web\.archive\.org/web/20230930103534/https://www\.upheal\.io/pricing](https://web.archive.org/web/20230930103534/https://www.upheal.io/pricing)
- F4357 · wayback\_first · Sourced · [https://web\.archive\.org/web/20231206232704/https://www\.upheal\.io/careers/data\-scientist](https://web.archive.org/web/20231206232704/https://www.upheal.io/careers/data-scientist)
- F4358 · wayback\_first · Sourced · [https://web\.archive\.org/web/20230528070242/https://www\.upheal\.io/blog](https://web.archive.org/web/20230528070242/https://www.upheal.io/blog)
- F4359 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/upheal\.io](https://web.archive.org/web/%2A/upheal.io)
- F4364 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4365 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4366 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4367 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4368 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4369 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4370 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4371 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4372 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4373 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4374 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4375 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4376 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4377 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4378 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4379 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4380 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4381 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4382 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4383 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4384 · press\_mention · Sourced · [https://en\.ain\.ua/2024/02/28/upheal\-secures\-3\-25m\-kaya\-vc](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc)
- F4385 · press\_mention · Sourced · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F4386 · press\_mention · Sourced · [https://mentalhealthinvestors\.com/startups/upheal](https://mentalhealthinvestors.com/startups/upheal)
- F4387 · press\_mention · Sourced · [https://cc\.cz/kvuli\-synove\-nemoci\-vyhorel\-jeho\-startup\-pomaha\-terapeutum\-letos\-oznamuje\-jiz\-druhou\-investici/](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/)
- F4388 · press\_mention · Sourced · [https://cc\.cz/ceska\-umela\-inteligence\-pise\-za\-psychoterapeuty\-poznamky\-ze\-sezeni\-od\-investoru\-nabrala\-pres\-70\-milionu/](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
- F4389 · source\_unavailable · Unavailable · [https://www\.siliconlegal\.com/sls\-client\-headline\-leads\-upheals\-e9\-52\-million\-series\-a\-round/](https://www.siliconlegal.com/sls-client-headline-leads-upheals-e9-52-million-series-a-round/)
- F4390 · press\_mention · Sourced · [https://cc\.cz/startupawards2024/upheal/](https://cc.cz/startupawards2024/upheal/)
- F4391 · press\_mention · Sourced · [https://funding\.tech\.eu/companies/upheal\-f8e6f63d](https://funding.tech.eu/companies/upheal-f8e6f63d)
- F4392 · source\_unavailable · Unavailable · [https://www\.axios\.com/pro/health\-tech\-deals/2024/02/27/upheal\-clinical\-therapy\-notes\-3\-million](https://www.axios.com/pro/health-tech-deals/2024/02/27/upheal-clinical-therapy-notes-3-million)
- F4393 · source\_unavailable · Unavailable · [https://www\.trustpilot\.com/review/upheal\.io](https://www.trustpilot.com/review/upheal.io)
- F4394 · press\_mention · Sourced · [https://www\.thesaasnews\.com/news/upheal\-secures\-3\-25\-million\-in\-seed\-round/](https://www.thesaasnews.com/news/upheal-secures-3-25-million-in-seed-round/)
- F4395 · press\_mention · Sourced · [https://startupkitchen\.community/czech\-healthtech\-upheal\-secures\-3\-25m\-to\-streamline\-its\-clinical\-workflows/](https://startupkitchen.community/czech-healthtech-upheal-secures-3-25m-to-streamline-its-clinical-workflows/)
- F4396 · press\_mention · Sourced · [https://tech\.eu/2022/10/19/upheal\-raises\-eur168\-million\-and\-launches\-ai\-powered\-notes\-app\-for\-mental\-health\-care\-professionals/](https://tech.eu/2022/10/19/upheal-raises-eur168-million-and-launches-ai-powered-notes-app-for-mental-health-care-professionals/)
- F4397 · press\_mention · Sourced · [https://www\.gaebler\.com/VC\-Funding\-721BA236\-FC2C\-4180\-A4A1\-ADE6911E834E\-Upheal\-10\-19\-2022](https://www.gaebler.com/VC-Funding-721BA236-FC2C-4180-A4A1-ADE6911E834E-Upheal-10-19-2022)
- F4398 · source\_unavailable · Unavailable · [https://birpnotes\.com/upheal](https://birpnotes.com/upheal)
- F4399 · press\_mention · Sourced · [https://www\.mentalyc\.com/blog/upheal\-reviews](https://www.mentalyc.com/blog/upheal-reviews)
- F4400 · press\_mention · Sourced · [https://www\.calmstorm\.vc/portfolio/upheal](https://www.calmstorm.vc/portfolio/upheal)
- F4401 · press\_mention · Sourced · [https://www\.inovia\.vc/portfolio/upheal](https://www.inovia.vc/portfolio/upheal)
- F4402 · press\_mention · Sourced · [https://www\.therecursive\.com/mental\-health\-startup\-upheal\-secures\-9\-5m\-series\-a\-after\-their\-seed\-round\-in\-february/](https://www.therecursive.com/mental-health-startup-upheal-secures-9-5m-series-a-after-their-seed-round-in-february/)
- F4403 · press\_mention · Sourced · [https://cc\.cz/dava\-terapeutum\-superschopnosti\-umela\-inteligence\-z\-ceska\-posloucha\-s\-lekarem\-ziskala\-25\-milionu/](https://cc.cz/dava-terapeutum-superschopnosti-umela-inteligence-z-ceska-posloucha-s-lekarem-ziskala-25-milionu/)
- F4404 · source\_unavailable · Unavailable · [https://akta\.pro/company\-profiles/0000hdv/upheal](https://akta.pro/company-profiles/0000hdv/upheal)
- F4405 · press\_mention · Sourced · [https://www\.einpresswire\.com/article/918347087/upheal\-releases\-2026\-provider\-experience\-report\-on\-ai\-documentation\-and\-therapist\-burnout](https://www.einpresswire.com/article/918347087/upheal-releases-2026-provider-experience-report-on-ai-documentation-and-therapist-burnout)
- F4406 · press\_mention · Sourced · [https://checkpointehr\.com/checkpointehr\-features/new\-partnership\-with\-upheal](https://checkpointehr.com/checkpointehr-features/new-partnership-with-upheal)
- F4407 · press\_mention · Sourced · [https://www\.joinheard\.com/partner/upheal](https://www.joinheard.com/partner/upheal)
- F6197 · product\_capability · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F6198 · product\_capability · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F6199 · product\_capability · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F6200 · product\_capability · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F6201 · pricing · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F6202 · pricing · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F6203 · tech\_claim · Medium confidence · [https://www\.upheal\.io/](https://www.upheal.io/)
- F6204 · pricing · Medium confidence · [https://www\.upheal\.io/pricing](https://www.upheal.io/pricing)
- F6205 · tech\_claim · Medium confidence · [https://www\.upheal\.io/pricing](https://www.upheal.io/pricing)
- F6206 · pricing · Medium confidence · [https://www\.upheal\.io/pricing](https://www.upheal.io/pricing)
- F6207 · pricing · Medium confidence · [https://www\.upheal\.io/pricing](https://www.upheal.io/pricing)
- F6208 · pricing · Medium confidence · [https://www\.upheal\.io/pricing](https://www.upheal.io/pricing)
- F6209 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F6210 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F6211 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F6212 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F6213 · pricing · Medium confidence · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F6214 · tech\_claim · Medium confidence · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F6215 · tech\_claim · Medium confidence · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F6216 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/ai\-clinical\-notes](https://www.upheal.io/features/ai-clinical-notes)
- F6217 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/ehr](https://www.upheal.io/features/ehr)
- F6218 · pricing · Medium confidence · [https://www\.upheal\.io/features/ehr](https://www.upheal.io/features/ehr)
- F6219 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/ai\-assistant](https://www.upheal.io/features/ai-assistant)
- F6220 · tech\_claim · Medium confidence · [https://www\.upheal\.io/features/ai\-assistant](https://www.upheal.io/features/ai-assistant)
- F6221 · tech\_claim · Medium confidence · [https://www\.upheal\.io/features/ai\-assistant](https://www.upheal.io/features/ai-assistant)
- F6222 · tech\_claim · Medium confidence · [https://www\.upheal\.io/features/ai\-assistant](https://www.upheal.io/features/ai-assistant)
- F6223 · pricing · Medium confidence · [https://www\.upheal\.io/features/ai\-assistant](https://www.upheal.io/features/ai-assistant)
- F6224 · pricing · Medium confidence · [https://www\.upheal\.io/features/ai\-assistant](https://www.upheal.io/features/ai-assistant)
- F6225 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/managed\-insurance\-billing](https://www.upheal.io/features/managed-insurance-billing)
- F6226 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/managed\-insurance\-billing](https://www.upheal.io/features/managed-insurance-billing)
- F6227 · pricing · Medium confidence · [https://www\.upheal\.io/features/managed\-insurance\-billing](https://www.upheal.io/features/managed-insurance-billing)
- F6228 · funding\_round · Medium confidence · [https://en\.ain\.ua/2024/02/28/upheal\-secures\-3\-25m\-kaya\-vc](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc)
- F6230 · product\_capability · Medium confidence · [https://en\.ain\.ua/2024/02/28/upheal\-secures\-3\-25m\-kaya\-vc](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc)
- F6231 · tech\_claim · Medium confidence · [https://en\.ain\.ua/2024/02/28/upheal\-secures\-3\-25m\-kaya\-vc](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc)
- F6232 · team\_claim · Medium confidence · [https://en\.ain\.ua/2024/02/28/upheal\-secures\-3\-25m\-kaya\-vc](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc)
- F6235 · funding\_round · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6237 · product\_capability · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6239 · integration · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6240 · integration · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6241 · integration · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6242 · integration · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6243 · integration · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6244 · tech\_claim · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6245 · team\_claim · Medium confidence · [https://vestbee\.com/insights/articles/upheal\-secures\-10\-m](https://vestbee.com/insights/articles/upheal-secures-10-m)
- F6246 · product\_capability · Medium confidence · [https://mentalhealthinvestors\.com/startups/upheal](https://mentalhealthinvestors.com/startups/upheal)
- F6247 · product\_capability · Medium confidence · [https://mentalhealthinvestors\.com/startups/upheal](https://mentalhealthinvestors.com/startups/upheal)
- F6248 · pricing · Medium confidence · [https://mentalhealthinvestors\.com/startups/upheal](https://mentalhealthinvestors.com/startups/upheal)
- F6249 · team\_claim · Medium confidence · [https://mentalhealthinvestors\.com/startups/upheal](https://mentalhealthinvestors.com/startups/upheal)
- F6250 · funding\_round · Medium confidence · [https://cc\.cz/kvuli\-synove\-nemoci\-vyhorel\-jeho\-startup\-pomaha\-terapeutum\-letos\-oznamuje\-jiz\-druhou\-investici/](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/)
- F6251 · tech\_claim · Medium confidence · [https://cc\.cz/kvuli\-synove\-nemoci\-vyhorel\-jeho\-startup\-pomaha\-terapeutum\-letos\-oznamuje\-jiz\-druhou\-investici/](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/)
- F6252 · tech\_claim · Medium confidence · [https://cc\.cz/ceska\-umela\-inteligence\-pise\-za\-psychoterapeuty\-poznamky\-ze\-sezeni\-od\-investoru\-nabrala\-pres\-70\-milionu/](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
- F6253 · tech\_claim · Medium confidence · [https://cc\.cz/ceska\-umela\-inteligence\-pise\-za\-psychoterapeuty\-poznamky\-ze\-sezeni\-od\-investoru\-nabrala\-pres\-70\-milionu/](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
- F6254 · team\_claim · Medium confidence · [https://cc\.cz/ceska\-umela\-inteligence\-pise\-za\-psychoterapeuty\-poznamky\-ze\-sezeni\-od\-investoru\-nabrala\-pres\-70\-milionu/](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
- F6255 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/growth\-audit](https://www.upheal.io/features/growth-audit)
- F6256 · pricing · Medium confidence · [https://www\.upheal\.io/features/growth\-audit](https://www.upheal.io/features/growth-audit)
- F6257 · pricing · Medium confidence · [https://www\.upheal\.io/features/growth\-audit](https://www.upheal.io/features/growth-audit)
- F6258 · product\_capability · Medium confidence · [https://www\.upheal\.io/features/growth\-audit](https://www.upheal.io/features/growth-audit)
- F6398 · verification · Sourced · [https://trust\.upheal\.io](https://trust.upheal.io)
- F7810 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/hledat?Q=ico%3A14138018](https://www.hlidacstatu.cz/hledat?Q=ico%3A14138018)
- F7811 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/dotace/hledat?Q=ico%3A14138018](https://www.hlidacstatu.cz/dotace/hledat?Q=ico%3A14138018)
- F7812 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Upheal%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Upheal%27)
- F7813 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
