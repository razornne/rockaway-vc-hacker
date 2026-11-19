# BottleCap AI — due diligence brief

bottlecapai\.com · BottleCap SE · IČO 23012854 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** Enterprise\-facing model\-evaluation and risk\-management SaaS \(AI Scan\) and an iOS consumer app \(Pulse\) built on their CAP1 LLM\. *(Company claim)* ^[1](https://bottlecapai.com/),[2](https://scan.bottlecapai.com/),[3](https://bottlecapai.com/post/bottlecap-ai-announcement/)
- **Stage & traction.** Announced $7\.5M seed led by 20VC with multiple strategic backers; first public iOS product \(Pulse\) launched alongside funding\. *(Partly verified)* ^[4](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/),[5](https://bottlecapai.com/blog/),[6](https://bottlecapai.com/post/bottlecap-ai-announcement/),[7](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- **Technology & moat.** Claimed proprietary efficiency techniques and CAP1 model family; public technical details limited to company claims and a small open repo footprint\. *(Partly verified)* ^[8](https://bottlecapai.com/),[9](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/),[10](https://bottlecapai.com/),[11](https://github.com/BottleCapAI/ThinkingCap-Test)
- **Key risk.** Core efficiency and detection claims remain company assertions without independent benchmarks or audit evidence\. *(Analyst view)* ^[10](https://bottlecapai.com/),[12](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/),[2](https://scan.bottlecapai.com/)
- **Diligence focus.** Verify CAP1, ThinkingCap benchmark methodology and reproducibility, and AI Scan’s detection efficacy against independent datasets—these define defensibility and enterprise sell\-through\. *(Analyst view)* ^[9](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/),[10](https://bottlecapai.com/),[2](https://scan.bottlecapai.com/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2026\-01\-29 · seed · 7\.5 million USD · 20VC, Canva founders and managers, ElevenLabs, Datadog, Hugging Face, Synthesia, Rockaway · 5 reports; date n/a · Rockaway Ventures, 20VC | 4, 13, 14, 15, 5, 16 |
| Investors in registry | Beck Adventures Incubator s\.r\.o\. \(from 2025\-04\-10\) | 17 |
| Hiring | 2 open roles: other 1, ml research 1 | 18, 19 |
| AI dependency | relies on \(subprocessor / own claims\): Hugging Face; own\-model evidence: 0 papers, 0 verified HF models, 2 ML roles, 2 own\-model claims | 20, 1, 3, 18 |
| Engineering footprint | 1 public repos \(31★, last push 2026\-11\-06\); 4 subdomains; stack: Cloudflare, Next\.js | 11 |
| Timeline | Czech entity registered 2025\-03\-03; first press 2013\-09\-23 \(22 articles collected\) | 21, 22 |

# Detailed findings

## Ownership and capital

- Registered entity BottleCap SE incorporated 2025\-03\-03; joint\-stock form hides shareholder details in registry\. *(Verified)* ^[23](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23012854),[24](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854)
- Registry shows early shareholders changes: The Godfather SE \(from incorporation\) then Beck Adventures Incubator s\.r\.o\. \(2025\-04\-10 to 2025\-05\-13\)\. *(Verified)* ^[25](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854),[17](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854)
- Documented paid\-in capital entries: EUR 120,000 \(2025\-03\-03\) increasing to EUR 139,489 \(2026\-01\-05\) in filings\. *(Verified)* ^[26](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854),[27](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854),[28](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1268674)

## Technology profile

- Product surfaces: AI Scan \(model\-behavior scanning/audit\) marketed as enterprise audit evidence generator; Pulse iOS app built on CAP1\. *(Partly verified)* ^[29](https://scan.bottlecapai.com/),[30](https://scan.bottlecapai.com/),[3](https://bottlecapai.com/post/bottlecap-ai-announcement/),[7](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- Model claims: CAP1 and ThinkingCap families claim substantial token/use efficiency gains; company publishes comparative percentages but technical detail is proprietary\. *(Partly verified)* ^[10](https://bottlecapai.com/),[9](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/),[31](https://bottlecapai.com/blog/),[32](https://bottlecapai.com/blog/)
- Engineering footprint: public GitHub org with two active repos \(public\_repos=2; recent pushes\), small open\-source presence only\. *(Verified)* ^[33](https://github.com/BottleCapAI),[11](https://github.com/BottleCapAI/ThinkingCap-Test),[34](https://github.com/BottleCapAI/NoCap-Test)

## Rebuild check

- **Commodity:** AI Scan's tagline — testing thousands of prompts and generating audit evidence — is functionally reproducible using standard model evaluation APIs and PostHog/GA telemetry\. *(Analyst view)* ^[35](https://scan.bottlecapai.com/),[30](https://scan.bottlecapai.com/),[36](https://bottlecapai.com/policy/),[37](https://bottlecapai.com/cookies-policy/)
  - Assumption: Assume access to off\-the\-shelf LLMs and evaluation tooling\.
- **Hard to copy:** CAP1/ThinkingCap efficiency claims and any proprietary training architecture would be hard to copy without internal research IP, staff \(Mikolov\-level\), or access to undisclosed optimizations\. *(Analyst view)* ^[9](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/),[8](https://bottlecapai.com/),[12](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/),[38](https://bottlecapai.com/)
  - Assumption: Assume proprietary training methods are not fully public\.
- **Verdict:** Month — a 2–3 person team can replicate scanning/audit UX and dashboards in about a month, but would lack claimed CAP1 efficiency and proprietary model artifacts\. *(Analyst view)* ^[30](https://scan.bottlecapai.com/),[35](https://scan.bottlecapai.com/),[9](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/),[11](https://github.com/BottleCapAI/ThinkingCap-Test)
  - Assumption: Assume available public LLMs for baseline scans\.

## Risks and caveats

- Unverified performance claims: major efficiency and post\-training\-detection claims are company statements without independent benchmark evidence\. *(Analyst view)* ^[10](https://bottlecapai.com/),[31](https://bottlecapai.com/blog/),[2](https://scan.bottlecapai.com/),[12](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- LLM vendor and infra dependency: AI Scan is run on Google Cloud \(us\-east4\), creating single\-cloud exposure for core product execution\. *(Analyst view)* ^[39](https://bottlecapai.com/cookies-policy/),[40](https://bottlecapai.com/policy/)
- Thin public engineering signal: only two public repos and limited docs despite big model claims, raising reproducibility and hiring/velocity questions\. *(Analyst view)* ^[33](https://github.com/BottleCapAI),[11](https://github.com/BottleCapAI/ThinkingCap-Test),[34](https://github.com/BottleCapAI/NoCap-Test),[19](https://bottlecapai.com/careers/)

## Questions for founders

- Can the team provide independent benchmark datasets and raw evaluation traces for ThinkingCap/CAP1 efficiency claims to validate token\-savings percentages? *(Analyst view)* ^[10](https://bottlecapai.com/),[31](https://bottlecapai.com/blog/),[32](https://bottlecapai.com/blog/)
- Share the architectural technical report or reproducible recipe for CAP1 training/inference optimizations and any patents or trade secrets that block replication\. *(Analyst view)* ^[9](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/),[12](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/),[41](https://patents.google.com/patent/WO2014165983A1)
- Quantify production dependency risk: is AI Scan operable outside Google Cloud \(region us\-east4\), and what is mitigation for cloud\-provider outages or data residency needs? *(Analyst view)* ^[39](https://bottlecapai.com/cookies-policy/),[40](https://bottlecapai.com/policy/)
- Provide enterprise references or signed pilot results showing AI Scan generated audit\-ready evidence accepted by a regulator or security/compliance audit\. *(Analyst view)* ^[30](https://scan.bottlecapai.com/),[29](https://scan.bottlecapai.com/)

## Sources

1. [bottlecapai\.com](https://bottlecapai.com/) · Company's own website · Product capability — “Frontier AI built by the pioneers of the space\. Custom benchmarks, real\-time alerts, security audits, and behavior alignment for organizations that depend on AI\. We evaluate models against your specific workflows, fine\-tune them for your exact use cases, and ensure strict compliance with the EU AI Act and DORA\.”
2. [scan\.bottlecapai\.com](https://scan.bottlecapai.com/) · Company's own website · Technical claim — “AI Scan detects post\-training modifications — changes made by model authors after the initial training\.”
3. [bottlecapai\.com](https://bottlecapai.com/post/bottlecap-ai-announcement/) · Company's own website · Product capability — “And today, we're launching our first product on iOS called “Pulse: Community News”, all built on top of CAP1, our own foundational model\.”
4. [lupa\.cz](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/) · Independent press · Funding round — “BottleCap AI , za kterým stojí AI vědec Tomáš Mikolov, tvůrce hitu Beat Saber Jaroslav Beck a AI výzkumník David Herel, získal v seed investičním kole 7,5 milionu dolarů, tedy zhruba 152 milionů korun\. Kolo vedl fond 20VC a připojila se k němu skupina zakladatelů a manažerů velkých technologických firem, mimo jiné z Ca…”
5. [bottlecapai\.com](https://bottlecapai.com/blog/) · Company's own website · Funding round — “We raised $7\.5M to build efficient AI in Europe”
6. [bottlecapai\.com](https://bottlecapai.com/post/bottlecap-ai-announcement/) · Company's own website · Technical claim — “Pulse already runs on our efficiency focused foundational model CAP1, and it's just the first of many applications we plan to build on top of our own technology\.”
7. [lupa\.cz](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/) · Independent press · Product capability — “Na vlastní technologii už BottleCap AI staví i první konkrétní produkt, o němž zveřejnil informace současně s investicí\.”
8. [bottlecapai\.com](https://bottlecapai.com/) · Company's own website · Technical claim — “architecture\-first foundational models including algorithms for training efficiency, inference efficiency”
9. [cc\.cz](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/) · Independent press · Technical claim — “Tento efektivní základní jazykový model bude pohánět širokou škálu našich budoucích aplikací,”
10. [bottlecapai\.com](https://bottlecapai.com/) · Company's own website · Technical claim — “ThinkingCap: Gemma\-4\-26B\-A4B — up to 69% and on average 39% less thinking, at unchanged accuracy”
11. [github\.com](https://github.com/BottleCapAI/ThinkingCap-Test) · Public technical artifact · GitHub repository · 2026\-11\-06 — “BottleCapAI/ThinkingCap\-Test · Open Test for BottleCapAI · Python · last push 2026\-11\-06”
12. [lupa\.cz](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/) · Independent press · Technical claim — “Společnost uvádí, že dokáže zrychlit trénování jazykových modelů a snížit jejich výpočetní náročnost díky změnám v samotné architektuře modelů\. V minulosti popsala , že v rámci interního výzkumu dosáhla výrazného zrychlení fáze pretrainingu\. Technické detaily zatím nezveřejňuje\.”
13. [havelpartners\.com](https://www.havelpartners.com/legal-advice-for-20vc-on-its-investment-in-bottlecap-ai/) · Independent press · Funding round — “HAVEL &amp; PARTNERS assisted the prominent British venture capital fund 20VC, acting as the lead investor, in connection with its investment in the Czech startup BottleCap AI\.”
14. [bottlecapai\.com](https://bottlecapai.com/) · Company's own website · Funding round — “More about our $7\.5M seed round”
15. [wolvessummit\.com](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round) · Independent press · Funding round — “BottleCap AI lands 7\.5 milllion euro round”
16. [wolvessummit\.com](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round) · Independent press · Funding round — “Rockaway Ventures invested in BottleCap AI , a European AI company founded by Jaroslav Beck , Tomas Mikolov and David Herel , alongside 20VC and founders from tech stars such as Lovable , Hugging Face , ElevenLabs , Canva , and many more\.”
17. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854) · Official record · Registry: shareholder · 2025\-04\-10 — “Beck Adventures Incubator s\.r\.o\. · from 2025\-04\-10 · to 2025\-05\-13”
18. [bottlecapai\.com](https://bottlecapai.com/careers/) · Company's own website · Job posting — “Natural Language Processing Researcher”
19. [bottlecapai\.com](https://bottlecapai.com/careers/) · Company's own website · Job posting — “Machine Learning Engineer”
20. [wolvessummit\.com](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round) · Independent press · Technical claim — “founders from tech stars such as Lovable , Hugging Face , ElevenLabs , Canva , and many more”
21. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23012854) · Official record · Registry: incorporation · 2025\-03\-03 — “registered 2025\-03\-03”
22. [cnbc\.com](https://www.cnbc.com/2013/09/23/coca-cola-apologizes-for-offensive-vitamin-bottlecap-promo.html) · Independent press · Press article · 2013\-09\-23 — “Coca\-cola apologizes for offensive vitamin bottlecap promo”
23. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23012854) · Official record · Registry: identity · 2025\-03\-03 — “BottleCap SE · SE · registered 2025\-03\-03”
24. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854) · Official record · Registry: structure
25. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854) · Official record · Registry: shareholder · 2025\-03\-03 — “The Godfather SE · from 2025\-03\-03 · to 2025\-04\-10”
26. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854) · Official record · Registry: registered capital · 2025\-03\-03
27. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854) · Official record · Registry: registered capital · 2026\-01\-05
28. [or\.justice\.cz](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1268674) · Official record · Registry: filed document · 2026\-01\-05
29. [scan\.bottlecapai\.com](https://scan.bottlecapai.com/) · Company's own website · Product capability — “AI Scan measures how your model's behavior changes\.”
30. [scan\.bottlecapai\.com](https://scan.bottlecapai.com/) · Company's own website · Product capability — “Get a custom scan tailored to your business and generate audit\-ready evidence automatically\.”
31. [bottlecapai\.com](https://bottlecapai.com/blog/) · Company's own website · Technical claim — “ThinkingCap: Gemma\-4\-26B\-A4B — up to 69% and on average 39% less thinking, at unchanged accuracy”
32. [bottlecapai\.com](https://bottlecapai.com/blog/) · Company's own website · Technical claim — “ThinkingCap: Qwen3\.8\-Flash\-Next — up to 51% and on average 39% less thinking, comparable benchmark accuracy”
33. [github\.com](https://github.com/BottleCapAI) · Public technical artifact · GitHub organisation · 2025\-03\-30 — “BottleCapAI · 2 public repos”
34. [github\.com](https://github.com/BottleCapAI/NoCap-Test) · Public technical artifact · GitHub repository · 2026\-02\-03 — “BottleCapAI/NoCap\-Test · Open Test for BottleCapAI · Python · last push 2026\-02\-03”
35. [scan\.bottlecapai\.com](https://scan.bottlecapai.com/) · Company's own website · Technical claim — “We test thousands of prompts across multiple risk dimensions and measure where a model's answers diverge from its baseline behavior\.”
36. [bottlecapai\.com](https://bottlecapai.com/policy/) · Company's own website · Subprocessor \(privacy policy\) — “Analytics, session replay \(PostHog\) and marketing cookies and similar technologies”
37. [bottlecapai\.com](https://bottlecapai.com/cookies-policy/) · Company's own website · Subprocessor \(privacy policy\) — “Google Analytics \(\_ga, \_ga\_\*\) Analytics Traffic measurement and statistics”
38. [bottlecapai\.com](https://bottlecapai.com/) · Company's own website · Team claim — “David Herel is Co\-founder and AI Researcher at BottleCap AI, where he works on making large language models significantly faster and more efficient\. His research focuses on LLM reasoning and model architecture, with publications at leading AI conferences including ICLR and ECAI\.”
39. [bottlecapai\.com](https://bottlecapai.com/cookies-policy/) · Company's own website · Subprocessor \(privacy policy\) — “AI Scan runs on Google Cloud infrastructure located in the United States \(region us\-east4\), while product\-analytics data collected via PostHog is processed in the European Union\. Some cookies are also set by third parties \(e\.g\.”
40. [bottlecapai\.com](https://bottlecapai.com/policy/) · Company's own website · Subprocessor \(privacy policy\) — “Google Cloud \(Google LLC\) — AI Scan runs on Google Cloud Run, Cloud SQL and Cloud Storage;”
41. [patents\.google\.com](https://patents.google.com/patent/WO2014165983A1) · Official record · Patent publication — “WO2014165983A1 · Dispenser having pierceable membrane · Bottlecap Holdings Ltd\.”
42. [patents\.google\.com](https://patents.google.com/patent/USD839100S1) · Official record · Patent publication — “USD839100S1 · Bottle · Bottlecap Holdings Ltd\.”
43. [patents\.google\.com](https://patents.google.com/patent/US20120308357A1) · Official record · Patent publication — “US20120308357A1 · Stackable container · Bottlecap Holdings Ltd\.”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 15 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 22 | press:seedtable\.com, press:sifted\.eu |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 23 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 11 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 3 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 21 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 4 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 9 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 33 | — |

Analysis: gpt\-5\-mini (cost $0.0078); AI extraction cost $0.0080. Full fact table: CSV export.

## Source appendix (all collected facts)

- F3123 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/23012854](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23012854)
- F3124 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/23012854](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23012854)
- F3125 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23012854](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854)
- F3126 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23012854](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854)
- F3127 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23012854](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854)
- F3128 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23012854](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854)
- F3129 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23012854](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854)
- F3130 · registry\_flag · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23012854](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23012854)
- F3131 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1268674](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1268674)
- F3132 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1268674](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1268674)
- F3133 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1268674](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1268674)
- F3134 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1268674](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1268674)
- F3135 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1268674](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1268674)
- F3136 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1268674](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1268674)
- F3137 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=23012854&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=23012854&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F3138 · web\_page · Sourced · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F3139 · web\_page · Sourced · [https://bottlecapai\.com/careers/](https://bottlecapai.com/careers/)
- F3140 · web\_page · Sourced · [https://bottlecapai\.com/policy/](https://bottlecapai.com/policy/)
- F3141 · subprocessor · Medium confidence · [https://bottlecapai\.com/policy/](https://bottlecapai.com/policy/)
- F3142 · subprocessor · Medium confidence · [https://bottlecapai\.com/policy/](https://bottlecapai.com/policy/)
- F3143 · subprocessor · Medium confidence · [https://bottlecapai\.com/policy/](https://bottlecapai.com/policy/)
- F3144 · subprocessor · Medium confidence · [https://bottlecapai\.com/policy/](https://bottlecapai.com/policy/)
- F3145 · web\_page · Sourced · [https://bottlecapai\.com/cookies\-policy/](https://bottlecapai.com/cookies-policy/)
- F3146 · subprocessor · Medium confidence · [https://bottlecapai\.com/cookies\-policy/](https://bottlecapai.com/cookies-policy/)
- F3147 · subprocessor · Medium confidence · [https://bottlecapai\.com/cookies\-policy/](https://bottlecapai.com/cookies-policy/)
- F3148 · subprocessor · Medium confidence · [https://bottlecapai\.com/cookies\-policy/](https://bottlecapai.com/cookies-policy/)
- F3149 · subprocessor · Medium confidence · [https://bottlecapai\.com/cookies\-policy/](https://bottlecapai.com/cookies-policy/)
- F3150 · web\_page · Sourced · [https://bottlecapai\.com/careers/natural\-language\-processing\-researcher/](https://bottlecapai.com/careers/natural-language-processing-researcher/)
- F3151 · web\_page · Sourced · [https://bottlecapai\.com/careers/machine\-learning\-engineer/](https://bottlecapai.com/careers/machine-learning-engineer/)
- F3152 · web\_page · Sourced · [https://bottlecapai\.com/privacy\-policy/](https://bottlecapai.com/privacy-policy/)
- F3153 · subprocessor · Medium confidence · [https://bottlecapai\.com/privacy\-policy/](https://bottlecapai.com/privacy-policy/)
- F3154 · web\_page · Sourced · [https://bottlecapai\.com/post/bottlecap\-ai\-announcement/](https://bottlecapai.com/post/bottlecap-ai-announcement/)
- F3155 · web\_page · Sourced · [https://bottlecapai\.com/blog/](https://bottlecapai.com/blog/)
- F3156 · web\_page · Sourced · [https://scan\.bottlecapai\.com/](https://scan.bottlecapai.com/)
- F3157 · web\_page · Sourced · [https://bottlecapai\.com/enterprise/](https://bottlecapai.com/enterprise/)
- F3158 · job\_post · Sourced · [https://bottlecapai\.com/careers/](https://bottlecapai.com/careers/)
- F3159 · job\_post · Sourced · [https://bottlecapai\.com/careers/](https://bottlecapai.com/careers/)
- F3160 · github\_org · Medium confidence · [https://bottlecapai\.com/careers/natural\-language\-processing\-researcher/](https://bottlecapai.com/careers/natural-language-processing-researcher/)
- F3161 · tech\_stack · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F3162 · tech\_stack · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F3163 · tech\_stack · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F3164 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=bottlecapai\.com&amp;type=MX](https://dns.google/resolve?name=bottlecapai.com&type=MX)
- F3165 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=bottlecapai\.com&amp;type=TXT](https://dns.google/resolve?name=bottlecapai.com&type=TXT)
- F3166 · subdomain · Sourced · [https://crt\.sh/?q=%25\.bottlecapai\.com&amp;output=json](https://crt.sh/?q=%25.bottlecapai.com&output=json)
- F3167 · subdomain · Sourced · [https://crt\.sh/?q=%25\.bottlecapai\.com&amp;output=json](https://crt.sh/?q=%25.bottlecapai.com&output=json)
- F3168 · subdomain · Sourced · [https://crt\.sh/?q=%25\.bottlecapai\.com&amp;output=json](https://crt.sh/?q=%25.bottlecapai.com&output=json)
- F3169 · subdomain · Sourced · [https://crt\.sh/?q=%25\.bottlecapai\.com&amp;output=json](https://crt.sh/?q=%25.bottlecapai.com&output=json)
- F3170 · subdomain · Sourced · [https://crt\.sh/?q=%25\.bottlecapai\.com&amp;output=json](https://crt.sh/?q=%25.bottlecapai.com&output=json)
- F3171 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.bottlecapai\.com&amp;output=json](https://crt.sh/?q=%25.bottlecapai.com&output=json)
- F3172 · github\_org · Sourced · [https://github\.com/BottleCapAI](https://github.com/BottleCapAI)
- F3173 · repo · Sourced · [https://github\.com/BottleCapAI/ThinkingCap\-Test](https://github.com/BottleCapAI/ThinkingCap-Test)
- F3174 · repo · Sourced · [https://github\.com/BottleCapAI/NoCap\-Test](https://github.com/BottleCapAI/NoCap-Test)
- F3175 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-27B)
- F3176 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-27B\-FP8](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-27B-FP8)
- F3177 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-27B\-GGUF](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-27B-GGUF)
- F3178 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-27B\-NVFP4](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-27B-NVFP4)
- F3179 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-Flash\-Next](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-Flash-Next)
- F3180 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.6\-27B\-GGUF](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B-GGUF)
- F3181 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.6\-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B)
- F3182 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-NVIDIA\-Nemotron\-3\.5\-Lightning\-30B\-A3B](https://huggingface.co/bottlecapai/ThinkingCap-NVIDIA-Nemotron-3.5-Lightning-30B-A3B)
- F3183 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-gemma\-4\-26B\-A4B\-it](https://huggingface.co/bottlecapai/ThinkingCap-gemma-4-26B-A4B-it)
- F3184 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.6\-27B\-FP8](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B-FP8)
- F3185 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.6\-27B\-NVFP4](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.6-27B-NVFP4)
- F3186 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-27B\-NVFP4A4\-AWQ](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-27B-NVFP4A4-AWQ)
- F3187 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-27B\-MLX\-4bit\-DWQ](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-27B-MLX-4bit-DWQ)
- F3188 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-27B\-GGUF\-RCO\-4\.2bpw](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-27B-GGUF-RCO-4.2bpw)
- F3189 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-NVIDIA\-Nemotron\-3\.5\-Lightning\-30B\-A3B\-FP8](https://huggingface.co/bottlecapai/ThinkingCap-NVIDIA-Nemotron-3.5-Lightning-30B-A3B-FP8)
- F3190 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-NVIDIA\-Nemotron\-3\.5\-Lightning\-30B\-A3B\-GGUF](https://huggingface.co/bottlecapai/ThinkingCap-NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF)
- F3191 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-Flash\-Next\-FP8](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-Flash-Next-FP8)
- F3192 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-Flash\-Next\-NVFP4](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-Flash-Next-NVFP4)
- F3193 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-Flash\-Next\-GGUF](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-Flash-Next-GGUF)
- F3194 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-gemma\-4\-26B\-A4B\-it\-GGUF](https://huggingface.co/bottlecapai/ThinkingCap-gemma-4-26B-A4B-it-GGUF)
- F3195 · hf\_model · Identity unverified · [https://huggingface\.co/bottlecapai/ThinkingCap\-Qwen3\.8\-Flash\-Next\-GGUF\-RCO\-3\.8bpw](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-Flash-Next-GGUF-RCO-3.8bpw)
- F3196 · wayback\_first · Sourced · [https://web\.archive\.org/web/20250302130538/https://www\.bottlecapai\.com/](https://web.archive.org/web/20250302130538/https://www.bottlecapai.com/)
- F3197 · wayback\_first · Sourced · [https://web\.archive\.org/web/20260721004631/https://bottlecapai\.com/careers/](https://web.archive.org/web/20260721004631/https://bottlecapai.com/careers/)
- F3198 · wayback\_first · Sourced · [https://web\.archive\.org/web/20260721004633/https://bottlecapai\.com/blog/\_\_next\.\_head\.txt?\_rsc=VzuyVqu8VLmqiDAW](https://web.archive.org/web/20260721004633/https://bottlecapai.com/blog/__next._head.txt?_rsc=VzuyVqu8VLmqiDAW)
- F3199 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/bottlecapai\.com](https://web.archive.org/web/%2A/bottlecapai.com)
- F3204 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3205 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3206 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3207 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3208 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3209 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3210 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3211 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3212 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3213 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3214 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3215 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3216 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3217 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3218 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3219 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3220 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3221 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3222 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3223 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3224 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/tomas\-mikolov\-a\-spolutvurce\-beat\-saberu\-rozjizdi\-startup\-pro\-radikakni\-zefektivneni\-ai\-modelu/](https://www.lupa.cz/aktuality/tomas-mikolov-a-spolutvurce-beat-saberu-rozjizdi-startup-pro-radikakni-zefektivneni-ai-modelu/)
- F3225 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/cesi\-vyrazne\-zrychlili\-trenink\-umele\-inteligence\-uz\-by\-nemusel\-stat\-tolik\-penez\-a\-zrat\-hromadu\-energie/](https://www.lupa.cz/aktuality/cesi-vyrazne-zrychlili-trenink-umele-inteligence-uz-by-nemusel-stat-tolik-penez-a-zrat-hromadu-energie/)
- F3226 · press\_mention · Sourced · [https://cc\.cz/jaroslav\-beck\-a\-tomas\-mikolov\-ziskavaji\-150\-milionu\-pro\-svuj\-ai\-startup\-investuje\-do\-nej\-i\-ivo\-lukacovic/](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/)
- F3227 · press\_mention · Sourced · [https://www\.wolvessummit\.com/bottlecap\-ai\-lands\-7\-5\-milllion\-euro\-round](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round)
- F3228 · source\_unavailable · Unavailable · [https://sifted\.eu/articles/bottlecap\-ai\-seed\-round](https://sifted.eu/articles/bottlecap-ai-seed-round)
- F3229 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/bottlecap\-uspornejsi\-umela\-inteligence\-od\-mikolova\-a\-becka\-ziskala\-investici\-pres\-150\-milionu\-korun/](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- F3230 · press\_mention · Sourced · [https://www\.havelpartners\.com/legal\-advice\-for\-20vc\-on\-its\-investment\-in\-bottlecap\-ai/](https://www.havelpartners.com/legal-advice-for-20vc-on-its-investment-in-bottlecap-ai/)
- F3231 · press\_mention · Sourced · [https://www\.hrot24\.cz/clanek/bottlecapai\-jaroslav\-beck\-tomas\-mikolov\-ivo\-lukacovic\-investice\-ai\-startup\-HnRwb](https://www.hrot24.cz/clanek/bottlecapai-jaroslav-beck-tomas-mikolov-ivo-lukacovic-investice-ai-startup-HnRwb)
- F3232 · press\_mention · Sourced · [https://nordic9\.com/news/bottlecap\-raised\-a\-75m\-seed\-round\-led\-by\-20vc/](https://nordic9.com/news/bottlecap-raised-a-75m-seed-round-led-by-20vc/)
- F3233 · press\_mention · Sourced · [https://startupintros\.com/news/2026\-01\-29\-bottlecap\-ai\-seed](https://startupintros.com/news/2026-01-29-bottlecap-ai-seed)
- F3234 · source\_unavailable · Unavailable · [https://seedtable\.com/companies/bottlecap\-ai/funding\-rounds/seed\-2026\-01](https://seedtable.com/companies/bottlecap-ai/funding-rounds/seed-2026-01)
- F3235 · press\_mention · Sourced · [https://euronomy\.eu/e/resilience/ai\-startups/bottlecap\-ai/](https://euronomy.eu/e/resilience/ai-startups/bottlecap-ai/)
- F3236 · press\_mention · Sourced · [https://czechbusinessreview\.com/startups/bottlecap\-ai\-jaroslav\-beck\-tomas\-mikolov\-david\-herel\-prague](https://czechbusinessreview.com/startups/bottlecap-ai-jaroslav-beck-tomas-mikolov-david-herel-prague)
- F3237 · press\_mention · Sourced · [https://www\.wired\.cz/clanky/novy\-startup\-jaroslava\-becka\-chce\-zvysit\-efektivitu\-ai\-az\-stonasobne](https://www.wired.cz/clanky/novy-startup-jaroslava-becka-chce-zvysit-efektivitu-ai-az-stonasobne)
- F3238 · press\_mention · Sourced · [https://huggingface\.co/bottlecapai](https://huggingface.co/bottlecapai)
- F3239 · press\_mention · Sourced · [https://www\.havelpartners\.cz/pravni\-poradenstvi\-pro\-20vc\-pri\-investici\-do\-startupu\-bottlecap\-ai/](https://www.havelpartners.cz/pravni-poradenstvi-pro-20vc-pri-investici-do-startupu-bottlecap-ai/)
- F3240 · press\_mention · Sourced · [https://trust\.mycroft\.io/bottlecap\-ai](https://trust.mycroft.io/bottlecap-ai)
- F3241 · press\_mention · Sourced · [https://www\.cnaip\.cz/en/entity/bottlecapai](https://www.cnaip.cz/en/entity/bottlecapai)
- F3242 · press\_mention · Sourced · [https://felloai\.com/bottlecap\-ai/](https://felloai.com/bottlecap-ai/)
- F3243 · press\_mention · Sourced · [https://davidherel\.com](https://davidherel.com)
- F3244 · press\_mention · Sourced · [https://www\.cnbc\.com/2013/09/23/coca\-cola\-apologizes\-for\-offensive\-vitamin\-bottlecap\-promo\.html](https://www.cnbc.com/2013/09/23/coca-cola-apologizes-for-offensive-vitamin-bottlecap-promo.html)
- F3245 · press\_mention · Sourced · [https://www\.eurohpc\-ju\.europa\.eu/europes\-ai\-efficiency\-frontier\-bottlecap\-se\-supercomputing\-initiative\_en](https://www.eurohpc-ju.europa.eu/europes-ai-efficiency-frontier-bottlecap-se-supercomputing-initiative_en)
- F3246 · press\_mention · Sourced · [https://brandsit\.pl/en/the\-czech\-start\-up\-bottlecap\-shows\-how\-to\-reduce\-the\-cost\-of\-running\-ai/](https://brandsit.pl/en/the-czech-start-up-bottlecap-shows-how-to-reduce-the-cost-of-running-ai/)
- F3247 · press\_mention · Sourced · [https://cc\.cz/ma\-robota\-jarmila\-rozhoduje\-za\-nej\-digitalni\-mozek\-bob\-a\-jeho\-startup\-zrychluje\-ai\-nikdo\-nechce\-cekat\-rika/](https://cc.cz/ma-robota-jarmila-rozhoduje-za-nej-digitalni-mozek-bob-a-jeho-startup-zrychluje-ai-nikdo-nechce-cekat-rika/)
- F5488 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/hledat?Q=ico%3A23012854](https://www.hlidacstatu.cz/hledat?Q=ico%3A23012854)
- F5489 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/dotace/hledat?Q=ico%3A23012854](https://www.hlidacstatu.cz/dotace/hledat?Q=ico%3A23012854)
- F5490 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27BottleCap%20AI%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27BottleCap%20AI%27)
- F5491 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F5853 · funding\_round · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F5854 · tech\_claim · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F5855 · tech\_claim · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F5856 · tech\_claim · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F5857 · team\_claim · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F5858 · team\_claim · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F5859 · product\_capability · Medium confidence · [https://bottlecapai\.com/](https://bottlecapai.com/)
- F5860 · product\_capability · Medium confidence · [https://scan\.bottlecapai\.com/](https://scan.bottlecapai.com/)
- F5861 · product\_capability · Medium confidence · [https://scan\.bottlecapai\.com/](https://scan.bottlecapai.com/)
- F5862 · tech\_claim · Medium confidence · [https://scan\.bottlecapai\.com/](https://scan.bottlecapai.com/)
- F5863 · tech\_claim · Medium confidence · [https://scan\.bottlecapai\.com/](https://scan.bottlecapai.com/)
- F5864 · tech\_claim · Medium confidence · [https://bottlecapai\.com/policy/](https://bottlecapai.com/policy/)
- F5865 · product\_capability · Medium confidence · [https://bottlecapai\.com/post/bottlecap\-ai\-announcement/](https://bottlecapai.com/post/bottlecap-ai-announcement/)
- F5866 · tech\_claim · Medium confidence · [https://bottlecapai\.com/post/bottlecap\-ai\-announcement/](https://bottlecapai.com/post/bottlecap-ai-announcement/)
- F5867 · tech\_claim · Medium confidence · [https://cc\.cz/jaroslav\-beck\-a\-tomas\-mikolov\-ziskavaji\-150\-milionu\-pro\-svuj\-ai\-startup\-investuje\-do\-nej\-i\-ivo\-lukacovic/](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/)
- F5868 · team\_claim · Medium confidence · [https://cc\.cz/jaroslav\-beck\-a\-tomas\-mikolov\-ziskavaji\-150\-milionu\-pro\-svuj\-ai\-startup\-investuje\-do\-nej\-i\-ivo\-lukacovic/](https://cc.cz/jaroslav-beck-a-tomas-mikolov-ziskavaji-150-milionu-pro-svuj-ai-startup-investuje-do-nej-i-ivo-lukacovic/)
- F5869 · funding\_round · Medium confidence · [https://www\.wolvessummit\.com/bottlecap\-ai\-lands\-7\-5\-milllion\-euro\-round](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round)
- F5870 · team\_claim · Medium confidence · [https://www\.wolvessummit\.com/bottlecap\-ai\-lands\-7\-5\-milllion\-euro\-round](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round)
- F5871 · tech\_claim · Medium confidence · [https://www\.wolvessummit\.com/bottlecap\-ai\-lands\-7\-5\-milllion\-euro\-round](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round)
- F5872 · funding\_round · Medium confidence · [https://www\.wolvessummit\.com/bottlecap\-ai\-lands\-7\-5\-milllion\-euro\-round](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round)
- F5873 · tech\_claim · Medium confidence · [https://www\.wolvessummit\.com/bottlecap\-ai\-lands\-7\-5\-milllion\-euro\-round](https://www.wolvessummit.com/bottlecap-ai-lands-7-5-milllion-euro-round)
- F5874 · funding\_round · Medium confidence · [https://www\.lupa\.cz/aktuality/bottlecap\-uspornejsi\-umela\-inteligence\-od\-mikolova\-a\-becka\-ziskala\-investici\-pres\-150\-milionu\-korun/](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- F5875 · tech\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/bottlecap\-uspornejsi\-umela\-inteligence\-od\-mikolova\-a\-becka\-ziskala\-investici\-pres\-150\-milionu\-korun/](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- F5876 · product\_capability · Medium confidence · [https://www\.lupa\.cz/aktuality/bottlecap\-uspornejsi\-umela\-inteligence\-od\-mikolova\-a\-becka\-ziskala\-investici\-pres\-150\-milionu\-korun/](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- F5877 · team\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/bottlecap\-uspornejsi\-umela\-inteligence\-od\-mikolova\-a\-becka\-ziskala\-investici\-pres\-150\-milionu\-korun/](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- F5878 · tech\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/bottlecap\-uspornejsi\-umela\-inteligence\-od\-mikolova\-a\-becka\-ziskala\-investici\-pres\-150\-milionu\-korun/](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- F5879 · product\_capability · Medium confidence · [https://www\.lupa\.cz/aktuality/bottlecap\-uspornejsi\-umela\-inteligence\-od\-mikolova\-a\-becka\-ziskala\-investici\-pres\-150\-milionu\-korun/](https://www.lupa.cz/aktuality/bottlecap-uspornejsi-umela-inteligence-od-mikolova-a-becka-ziskala-investici-pres-150-milionu-korun/)
- F5880 · funding\_round · Medium confidence · [https://www\.havelpartners\.com/legal\-advice\-for\-20vc\-on\-its\-investment\-in\-bottlecap\-ai/](https://www.havelpartners.com/legal-advice-for-20vc-on-its-investment-in-bottlecap-ai/)
- F5881 · funding\_round · Medium confidence · [https://bottlecapai\.com/blog/](https://bottlecapai.com/blog/)
- F5882 · tech\_claim · Medium confidence · [https://bottlecapai\.com/blog/](https://bottlecapai.com/blog/)
- F5883 · tech\_claim · Medium confidence · [https://bottlecapai\.com/blog/](https://bottlecapai.com/blog/)
- F5884 · tech\_claim · Medium confidence · [https://bottlecapai\.com/blog/](https://bottlecapai.com/blog/)
- F5885 · tech\_claim · Medium confidence · [https://bottlecapai\.com/blog/](https://bottlecapai.com/blog/)
- F6375 · patent · Sourced · [https://patents\.google\.com/patent/WO2014165983A1](https://patents.google.com/patent/WO2014165983A1)
- F6376 · patent · Sourced · [https://patents\.google\.com/patent/USD839100S1](https://patents.google.com/patent/USD839100S1)
- F6377 · patent · Sourced · [https://patents\.google\.com/patent/US20120308357A1](https://patents.google.com/patent/US20120308357A1)
- F6378 · patent · Sourced · [https://patents\.google\.com/patent/USD791605S1](https://patents.google.com/patent/USD791605S1)
- F6379 · patent · Sourced · [https://patents\.google\.com/patent/US20130105522A1](https://patents.google.com/patent/US20130105522A1)
- F6380 · patent · Sourced · [https://patents\.google\.com/patent/WO2012155249A1](https://patents.google.com/patent/WO2012155249A1)
- F6381 · patent · Sourced · [https://patents\.google\.com/patent/CA2776580A1](https://patents.google.com/patent/CA2776580A1)
- F6382 · patent · Sourced · [https://patents\.google\.com/patent/CA165836S](https://patents.google.com/patent/CA165836S)
- F6383 · patent · Sourced · [https://patents\.google\.com/patent/WO2014089667A1](https://patents.google.com/patent/WO2014089667A1)
