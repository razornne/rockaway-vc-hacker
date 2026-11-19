# Upheal — due diligence brief

upheal\.io · Upheal s\.r\.o\. · IČO 14138018 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** An AI\-first EHR and practice stack that drafts clinical therapy notes, offers telehealth, scheduling, billing, and a client portal for individual clinicians and group practices\. *(Partly verified)* ^[1](https://www.upheal.io/features/ai-clinical-notes),[2](https://www.upheal.io/),[3](https://www.upheal.io/),[4](https://mentalhealthinvestors.com/startups/upheal)
- **Stage & traction.** Multiple press\-reported seed rounds \(\~$4\.35M and 76M CZK\) and announced partnerships with several provider groups; company reports 90k sessions processed in last 12 months\. *(Corroborated)* ^[5](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[6](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/),[7](https://vestbee.com/insights/articles/upheal-secures-10-m),[8](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
- **Technology & moat.** Limited — core features \(AI note drafting, templates, EHR integration\) are productized via docs and browser extension, while claimed scale \(90k sessions\) and managed\-billing operations are the harder\-to\-copy elements\. *(Partly verified)* ^[9](https://www.upheal.io/features/ai-clinical-notes),[10](https://www.upheal.io/features/ai-clinical-notes),[8](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
- **Key risk.** Key decision risk: compliance and security claims \(SOC 2, HIPAA\) are presented on site but the SOC 2 attestation is only a public pointer and shared under NDA \(partly verified\)\. *(Analyst view)* ^[11](https://www.upheal.io/),[12](https://www.upheal.io/features/ai-assistant),[13](https://trust.upheal.io)
- **Diligence focus.** First verify independent security/compliance artifacts \(full SOC2 report, HIPAA controls\), then validate monthly sessions and customer references that underpin claimed scale and billing revenue model\. *(Analyst view)* ^[13](https://trust.upheal.io),[8](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/),[14](https://www.upheal.io/features/managed-insurance-billing)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2024\-02\-28 · $4\.35 million; 2024\-11\-14 · Series Seed; 2024\-11\-18 · seed · 76,000,000 CZK | 5, 15, 6 |
| Engineering footprint | product surfaces: auth\.upheal\.io, status\.upheal\.io; 5 docs pages; stack: Cloudflare, Webflow | 16, 17, 18, 19 |
| Customers | public pricing: yes; 1 mobile app\(s\) | 20 |
| Claims checked | SOC 2 / ISO: partly | 13 |
| Timeline | Czech entity registered 2022\-01\-10; first press 2022\-10\-18 \(19 articles collected\) | 21, 22 |

# Detailed findings

## Ownership and capital

- Registry: Upheal s\.r\.o\. incorporated 2022\-01\-10, capital CZK 20,000, and 100% foreign holding by Upheal, Inc\. \(US\) since 2022\-08\-29\. *(Verified)* ^[23](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14138018),[24](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018),[25](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018)
- Funding history \(press\-reported\): \~$4\.35M total reported; separate reports of a 76,000,000 CZK seed round and a Series Seed mention in 2024/Nov press\. *(Corroborated)* ^[5](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc),[6](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/),[15](https://vestbee.com/insights/articles/upheal-secures-10-m)
- Recent filings: annual/accounting filings for 2022 and 2023 visible in justice registry \(filed 2023\-10\-24 and 2024\-05\-19\)\. *(Verified)* ^[26](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145979),[27](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018),[28](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145979)

## Technology profile

- Product surfaces and docs: public documentation hub and multiple detailed docs pages showing templates and note guidance\. *(Company claim)* ^[18](https://www.upheal.io/documentation),[19](https://www.upheal.io/documentation/intake-form-template),[29](https://www.upheal.io/documentation/progress-note-template),[30](https://www.upheal.io/documentation/soap-note-example-2026),[31](https://www.upheal.io/documentation/dap-note-example)
- Core product capabilities: automated AI clinical notes \(SOAP, DAP, GIRP, etc\.\), one\-click EHR browser\-extension integration, automated treatment plans, telehealth and billing features\. *(Company claim)* ^[32](https://www.upheal.io/features/ai-clinical-notes),[9](https://www.upheal.io/features/ai-clinical-notes),[33](https://www.upheal.io/features/ai-clinical-notes),[2](https://www.upheal.io/),[34](https://www.upheal.io/pricing)
- Engineering footprint: public subdomains \(auth\., status\.\), Webflow \+ Cloudflare front\-end hosting, and a mobile Android app package listed in Play Store\. *(Verified)* ^[16](https://crt.sh/?q=%25.upheal.io&output=json),[17](https://crt.sh/?q=%25.upheal.io&output=json),[35](https://www.upheal.io/),[36](https://www.upheal.io/),[37](https://www.upheal.io/features/session-formats)

## Rebuild check

- **Commodity:** AI note drafting and templates — publicly documented, browser\-extension EHR fill, and configurable templates; a small team could reproduce basic drafting using standard LLM APIs and browser automation\. *(Analyst view)* ^[32](https://www.upheal.io/features/ai-clinical-notes),[9](https://www.upheal.io/features/ai-clinical-notes),[29](https://www.upheal.io/documentation/progress-note-template)
  - Assumption: Use off\-the\-shelf LLM APIs and browser extension tooling\.
- **Hard to copy:** Managed insurance billing operations, claims tracking and appeals, plus reported processing scale \(90k sessions\) — these require operational processes, payer relationships and claimed historical data\. *(Analyst view)* ^[14](https://www.upheal.io/features/managed-insurance-billing),[38](https://www.upheal.io/features/managed-insurance-billing),[8](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
  - Assumption: Billing requires payer contracts and operational staff\.
- **Verdict:** Month — a functional UI and AI\-note MVP could be cloned within a month; a clone would lack Upheal's claimed session volume, payer relationships, and managed\-billing operations\. *(Analyst view)* ^[32](https://www.upheal.io/features/ai-clinical-notes),[9](https://www.upheal.io/features/ai-clinical-notes),[14](https://www.upheal.io/features/managed-insurance-billing)
  - Assumption: Clone uses public LLM APIs and standard web hosting\.

## Risks and caveats

- Unverified compliance stack: site claims SOC 2 Type II / HIPAA but SOC2 attestation is only a pointer; full report shared under NDA \(partly verified\)\. *(Analyst view)* ^[11](https://www.upheal.io/),[12](https://www.upheal.io/features/ai-assistant),[13](https://trust.upheal.io)
  - Assumption: Full attestation must be reviewed to confirm controls\.
- Reliance on claimed scale and time\-savings: key commercial claims \(90k sessions processed; 14 minutes saved per note\) drive go\-to\-market economics but are from company/press statements needing independent validation\. *(Analyst view)* ^[8](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/),[39](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/)
  - Assumption: Metrics currently reported in press, not third\-party audited\.

## Questions for founders

- Can the company produce the full SOC 2 Type II report and evidence of HIPAA controls referenced on site \(trust\.upheal\.io\) for investor review? *(Analyst view)* ^[13](https://trust.upheal.io),[11](https://www.upheal.io/)
  - Assumption: Report is currently behind NDA per public pointer\.
- Please provide audited customer references and billing volume that substantiate the 90,000 sessions and 25k/month figures cited in press\. *(Analyst view)* ^[8](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/),[40](https://mentalhealthinvestors.com/startups/upheal)
  - Assumption: Press cites company\-reported numbers without independent audit\.
- Which LLM vendors or in\-house models power AI note drafting and where are they contractually declared as subprocessors \(we saw only AWS listed\)? *(Analyst view)* ^[41](https://www.upheal.io/privacy-and-compliance),[42](https://vestbee.com/insights/articles/upheal-secures-10-m)
  - Assumption: AWS is listed as cloud subprocessor; LLM vendors not named\.
- Request evidence of payer integrations and sample claims lifecycle logs to validate managed\-insurance billing capabilities and collection timing\. *(Analyst view)* ^[14](https://www.upheal.io/features/managed-insurance-billing),[38](https://www.upheal.io/features/managed-insurance-billing)
  - Assumption: Managed billing implies payer\-level operations and records\.

## Sources

1. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Progress notes and transcripts are instantly created after every session, so you can stay focused on your clients\.”
2. [upheal\.io](https://www.upheal.io/) · Company's own website · Product capability — “Yes \. Upheal includes built\-in HIPAA\-compliant telehealth with video sessions\.”
3. [upheal\.io](https://www.upheal.io/) · Company's own website · Product capability — “Your calendar, intake forms, telehealth, billing and client portal sit right next to your notes\.”
4. [mentalhealthinvestors\.com](https://mentalhealthinvestors.com/startups/upheal) · Independent press · Pricing — “It sells subscriptions to individual clinicians and group practices\.”
5. [en\.ain\.ua](https://en.ain.ua/2024/02/28/upheal-secures-3-25m-kaya-vc) · Independent press · Funding round — “In total, Upheal raised $4\.35 million of funding\.”
6. [cc\.cz](https://cc.cz/kvuli-synove-nemoci-vyhorel-jeho-startup-pomaha-terapeutum-letos-oznamuje-jiz-druhou-investici/) · Independent press · Funding round — “seedové investiční kolo ve výši 76 milionů korun pak Upheal oznamoval letos v únoru”
7. [vestbee\.com](https://vestbee.com/insights/articles/upheal-secures-10-m) · Independent press · Integration — “Upheal has partnered with Alma, Cartwheel Care, Author Health, Noble Health, and Insight Counseling\.”
8. [cc\.cz](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/) · Independent press · Technical claim — “Během posledních dvanácti měsíců zpracoval 90 tisíc sezení, čímž terapeutům ušetřil 21 tisíc hodin\. Každý měsíc zpracovává nyní 25 tisíc sezení\.”
9. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Or use our browser extension to fill your notes into your EHR with one click\.”
10. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Upheal creates AI\-generated notes in ten formats: SOAP, DAP, GIRP, BIRP, EMDR, PIRP, SIRP, PIE, Intake, and Mental Status Exam \(MSE\)\. You can use any of these as\-is, or build your own template from 170 clinically approved sections to match your preferred style and payer requirements\.”
11. [upheal\.io](https://www.upheal.io/) · Company's own website · Technical claim — “SOC 2 Type II”
12. [upheal\.io](https://www.upheal.io/features/ai-assistant) · Company's own website · Technical claim — “HIPAA Compliant PHIPA Compliant SOC 2 Type II GDPR Compliant Asks before it acts”
13. [trust\.upheal\.io](https://trust.upheal.io) · Company's own website · Independent check of a claim — “Public attestation pointer found: subdomain trust\.upheal\.io\. The report itself is shared under NDA — request it\.”
14. [upheal\.io](https://www.upheal.io/features/managed-insurance-billing) · Company's own website · Product capability — “You sign the note\. The rest is on us\. You Finish your session Upheal drafts an insurance‑ready note from the session\. You review and sign\. Upheal We file the claim”
15. [vestbee\.com](https://vestbee.com/insights/articles/upheal-secures-10-m) · Independent press · Funding round — “since its Series Seed funding in February 2024”
16. [crt\.sh](https://crt.sh/?q=%25.upheal.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-06\-09 — “auth\.upheal\.io \(first certificate 2023\-06\-09\)”
17. [crt\.sh](https://crt.sh/?q=%25.upheal.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-08\-21 — “status\.upheal\.io \(first certificate 2023\-08\-21\)”
18. [upheal\.io](https://www.upheal.io/documentation) · Company's own website · Website page — “Documentation \| Upheal”
19. [upheal\.io](https://www.upheal.io/documentation/intake-form-template) · Company's own website · Website page — “Intake Form Template for Mental Health \(Updates for 2026\)”
20. [upheal\.io](https://www.upheal.io/) · Company's own website · Pricing — “AI Notes is $39/month for unlimited AI notes\.”
21. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14138018) · Official record · Registry: incorporation · 2022\-01\-10 — “registered 2022\-01\-10”
22. [cc\.cz](https://cc.cz/dava-terapeutum-superschopnosti-umela-inteligence-z-ceska-posloucha-s-lekarem-ziskala-25-milionu/) · Independent press · Press article · 2022\-10\-18 — “Umělá inteligence poslouchající s terapeutem přilákala 25 milionů \- CzechCrunch”
23. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14138018) · Official record · Registry: identity · 2022\-01\-10 — “Upheal s\.r\.o\. · s\.r\.o\. · registered 2022\-01\-10”
24. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018) · Official record · Registry: registered capital · 2022\-01\-10 — “20 000 CZK”
25. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018) · Official record · Registry: shareholder · 2022\-08\-29 — “Upheal, Inc\. · 100\.0% · from 2022\-08\-29”
26. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145979) · Official record · Registry: filed document · 2023\-10\-24
27. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14138018) · Official record · Registry: structure
28. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145979) · Official record · Registry: filed document · 2024\-05\-19
29. [upheal\.io](https://www.upheal.io/documentation/progress-note-template) · Company's own website · Website page — “Writing great progress notes: when to use which template and why”
30. [upheal\.io](https://www.upheal.io/documentation/soap-note-example-2026) · Company's own website · Website page — “SOAP note example: how to write one \(free template\)”
31. [upheal\.io](https://www.upheal.io/documentation/dap-note-example) · Company's own website · Website page — “How to write a DAP note – a real\-life example”
32. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Upheal generates SOAP, DAP, GIRP, and other clinical note formats automatically from your sessions\.”
33. [upheal\.io](https://www.upheal.io/features/ai-clinical-notes) · Company's own website · Product capability — “Insurance\-compliant Treatment Plans are generated from past sessions and automatically update as your client progresses\.”
34. [upheal\.io](https://www.upheal.io/pricing) · Company's own website · Pricing — “Invoicing, superbills, and online client payments”
35. [upheal\.io](https://www.upheal.io/) · Public technical artifact · Technology detected
36. [upheal\.io](https://www.upheal.io/) · Public technical artifact · Technology detected
37. [upheal\.io](https://www.upheal.io/features/session-formats) · Public technical artifact · Mobile app
38. [upheal\.io](https://www.upheal.io/features/managed-insurance-billing) · Company's own website · Product capability — “We track and chase Status monitored, rejections corrected, denials worked, appeals filed, statements sent\.”
39. [cc\.cz](https://cc.cz/ceska-umela-inteligence-pise-za-psychoterapeuty-poznamky-ze-sezeni-od-investoru-nabrala-pres-70-milionu/) · Independent press · Technical claim — “Podle vyjádření firmy v průměru ušetří terapeutům 14 minut \(z průměrných 22 minut\) na jednu poznámku za sezení\.”
40. [mentalhealthinvestors\.com](https://mentalhealthinvestors.com/startups/upheal) · Independent press · Press article — “Upheal: funding, last round &amp; investors · Mental Health Investors”
41. [upheal\.io](https://www.upheal.io/privacy-and-compliance) · Company's own website · Subprocessor \(privacy policy\) — “In addition, we use AWS for our cloud infrastructure and storage, a highly secure and reliable vendor\.”
42. [vestbee\.com](https://vestbee.com/insights/articles/upheal-secures-10-m) · Independent press · Technical claim — “enhance its AI\-driven tools”

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

Analysis: gpt\-5\-mini (cost $0.0088); AI extraction cost $0.0087. Full fact table: CSV export.

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
- F5541 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/hledat?Q=ico%3A14138018](https://www.hlidacstatu.cz/hledat?Q=ico%3A14138018)
- F5542 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/dotace/hledat?Q=ico%3A14138018](https://www.hlidacstatu.cz/dotace/hledat?Q=ico%3A14138018)
- F5543 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Upheal%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Upheal%27)
- F5544 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
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
