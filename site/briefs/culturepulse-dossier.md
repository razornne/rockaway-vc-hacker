# CulturePulse — due diligence brief

culturepulse\.ai · SK/US · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A self‑service AI platform \(ARES\) that builds psychological digital twins and predicts social, security and business risks for clients testing messaging and trends\. *(Corroborated)* ^[1](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/),[2](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond),[3](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)
- **Stage & traction.** Raised seed \(\~$1M\) in 2023 and a $1\.5M strategic / Series A round in 2025 with Rockaway, B Ventures and Simpact; AWS Marketplace seller profile listed\. *(Corroborated)* ^[4](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[5](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/),[6](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq)
- **Technology & moat.** Published multi‑author academic papers and public code repos indicate research depth and reproducible simulations that could underpin unique modeling IP\. *(Verified)* ^[7](https://openalex.org/W4220801307),[8](https://openalex.org/W4362657727),[9](https://github.com/culturepulse/censorshipderadsim),[10](https://github.com/culturepulse)
- **Key risk.** Core performance and accuracy claims \(e\.g\., \~95% 'clinical' correlation, 200\+ languages, 93 dimensions\) are company claims with limited independent verification in the facts\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/),[12](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/),[13](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
- **Diligence focus.** Verify empirical validation \(datasets, test methodology, third‑party audits\) behind the 95% correlation and multi‑language, 93‑dimension profiling claims\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/),[12](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/),[14](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2023\-04\-20 · Seed · just south of $1 million · Zero Gravity Capital · 2 reports; 2025\-02\-06 · Series A · $1\.5 million · Rockaway Ventures \(Rockaway Capital\), B Ventures Group \(USA\), Simpact VC \(PL\), Rockaway Ve · 6 reports; 2025\-02\-10 · strategická investícia · 1,5 milióna USD · B Ventures group \(USA\), Rockaway Ventures Fund \(Česko\), Simpact Ventures \(Poľsko\) | 4, 15, 5, 16, 17, 18 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; own\-model evidence: 7 papers, 0 verified HF models, 0 ML roles, 0 own\-model claims | 7, 19, 20 |
| Engineering footprint | 7 public repos \(1★, last push 2026\-04\-06\); stack: AmazonS3 | 9, 21, 22 |
| Customers | public pricing: yes | 23 |
| Timeline | first press 2023\-04\-20 \(23 articles collected\) | 24 |

# Detailed findings

## Ownership and capital

- Seed round \~just south of $1M led by Zero Gravity Capital \(reported Apr 2023\)\. *(Corroborated)* ^[4](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[25](https://finalfrontier.vc/newsroom/3062026)
- 2025 fundraising: $1\.5M round / strategic investment reported Feb–Mar 2025 with Rockaway Ventures, B Ventures Group and Simpact among investors\. *(Corroborated)* ^[5](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/),[26](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/),[27](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html)
- AWS Marketplace seller profile exists \(seller page indexed on AWS Marketplace\)\. *(Single source)* ^[6](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq)

## Technology profile

- Core capabilities \(company claims\): multi‑language text analysis, 93‑dimension psychological profiling, behavioral digital twins, ARES risk prediction\. *(Corroborated)* ^[14](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov),[28](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[2](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)
- Product surface and go‑to‑market: company describes a self‑service SaaS platform for on‑demand insights and testing messages on digital twins\. *(Corroborated)* ^[1](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/),[29](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
- Engineering footprint: public GitHub org with multiple repos \(public\_repos listed, active pushes through 2026\), and use of Amazon S3 revealed in DNS/stack facts\. *(Verified)* ^[10](https://github.com/culturepulse),[30](https://github.com/culturepulse/frontend_assignement),[31](https://www.culturepulse.ai)

## Rebuild check

- **Commodity:** Multi‑language text scoring and basic psychological tags — a small NLP team could approximate this using off‑the‑shelf models and cloud storage\. *(Analyst view)* ^[14](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov),[31](https://www.culturepulse.ai)
  - Assumption: Assumes availability of general multilingual NLP models and cloud storage
- **Hard to copy:** Published peer‑reviewed modelling papers and public simulation code indicate non‑trivial, research‑grade simulation IP and domain expertise\. *(Analyst view)* ^[7](https://openalex.org/W4220801307),[9](https://github.com/culturepulse/censorshipderadsim),[8](https://openalex.org/W4362657727)
  - Assumption: Assumes publications reflect internal algorithms and datasets
- **Verdict:** Month — a competent 2–3 person team could replicate basic multilingual scoring quickly, but would lack the validated models, published research lineage and any proprietary dataset\-driven accuracy\. *(Analyst view)* ^[14](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov),[7](https://openalex.org/W4220801307),[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
  - Assumption: Assumes no access to their proprietary evaluation datasets

## Risks and caveats

- Unverified performance claims: the \~95% 'clinical' correlation and wide‑language/93‑dimension accuracy are asserted by the company but lack independent verification in supplied facts\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/),[12](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/),[14](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov)
- Concentration of public evidence in PR/press and company claims versus independent third‑party validations or named customers in supplied facts\. *(Analyst view)* ^[24](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[32](https://www.tehnopol.ee/en/startup-story-culturepulse-x-nato-diana-estonian-accelerator/),[33](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/)
- Thin product surface documentation: no documented public product docs/pages found in facts despite public repos and marketplace listing\. *(Analyst view)* ^[10](https://github.com/culturepulse),[6](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq),[30](https://github.com/culturepulse/frontend_assignement)

## Questions for founders

- Please provide the evaluation datasets, methodology, and third‑party audit \(if any\) that support the 95% correlation claim\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
- Which customers or pilots validate ARES in operational security contexts, and can you share NDAs or case studies? *(Analyst view)* ^[2](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond),[6](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq)
- What proprietary datasets or labelling processes underpin the 93‑dimension profiling and language coverage claims? *(Analyst view)* ^[14](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov),[12](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
- Request an architecture and data‑flow diagram showing where models run \(in‑house vs third‑party\), because no LLM vendor dependencies are documented in supplied facts\. *(Analyst view)* ^[7](https://openalex.org/W4220801307),[31](https://www.culturepulse.ai)

## Sources

1. [bird\-incubator\.com](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/) · Independent press · Product capability — “The key focus of this funding is to develop scalable products that can deliver our insights quickly and affordably \. Our AI is designed to predict large\-scale behavioral trends , so we are building a self\-service platform that allows clients to access these insights on demand\.”
2. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond) · Independent press · Technical claim — “Leveraging artificial intelligence and cognitive science, the platform’s unique ARES \(Automated Risk Estimation\) system enables the creation of precise, psychologically realistic digital twins of target audiences\.”
3. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond) · Independent press · Product capability — “CulturePulse’s platform allows clients to better understand the complexities of social dynamics and predict both security and business risks on a global scale\.”
4. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Funding round — “just south of $1 million Seed round from Zero Gravity Capital to move the AI software to a SaaS platform while 'expanding the team to bolster the sales efforts and expand to new markets'\.”
5. [cc\.cz](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/) · Independent press · Funding round — “V rámci investičního kola takzvané série A získala společnost financování ve výši 1,5 milionu dolarů \(přes 36 milionů korun\)”
6. [aws\.amazon\.com](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq) · Independent press · Press article — “CulturePulse Seller Profile \| AWS Marketplace”
7. [openalex\.org](https://openalex.org/W4220801307) · Public technical artifact · Research paper · 2022\-03\-17 — “What causes COVID\-19 vaccine hesitancy? Ignorance and the lack of bliss in the United Kingdom · Humanities and Social Sciences Communications · cited 47×”
8. [openalex\.org](https://openalex.org/W4362657727) · Public technical artifact · Research paper · 2023\-04\-06 — “Modeling nationalism, religiosity, and threat perception: During the COVID\-19 pandemic · PLoS ONE · cited 7×”
9. [github\.com](https://github.com/culturepulse/censorshipderadsim) · Public technical artifact · GitHub repository · 2021\-12\-30 — “culturepulse/censorshipderadsim · A public repository for code, analyses and information related to the models, simulations, data, results, and discussions of the paper "Social Media Censorship Can Reinforce Radicalization" · last push 2021\-12\-30”
10. [github\.com](https://github.com/culturepulse) · Public technical artifact · GitHub organisation · 2021\-12\-27 — “culturepulse · 8 public repos”
11. [en\.ain\.ua](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/) · Independent press · Product capability — “The startup also claims that its solution predicts with clinical accuracy of almost 95% correlation\.”
12. [fontech\.startitup\.sk](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/) · Independent press · Technical claim — “Technológia vyvinutá CulturePulse má podľa neho schopnosť analyzovať texty vo viac ako 200 jazykoch a vytvárať psychologické profily na 93 rôznych dimenziách\.”
13. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Product capability — “While most technologies on the market can only function in a small handful of languages, CulturePulse is unique as it works across 100\+ languages, covering 99% of digital texts without the need for historical data and training”
14. [trend\.sk](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov) · Independent press · Technical claim — “Vie analyzovať texty vo vyše 200 jazykoch, modelovať psychologické profily v 93 rôznych dimenziách a vytvárať presné digitálne dvojičky populácií a štátov\.”
15. [en\.ain\.ua](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/) · Independent press · Funding round — “On the beginning of 2023, Zero Gravity led a €1 million round for Readmio, the developer of an app with fairy tales for children\.”
16. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond) · Independent press · Funding round — “The company aims to use the $1\.5 million raised in its first investment round, which remains open to additional investors, to expand its team and accelerate product development\.”
17. [therecursive\.com](https://www.therecursive.com/rockaway-capital-invests-e1-45m-in-us-slovak-startup-culturepulse) · Independent press · Funding round — “Rockaway Capital Invests €1\.45M in US\-Slovak Startup CulturePulse”
18. [bird\-incubator\.com](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/) · Independent press · Funding round — “CulturePulse Secures $1\.5M Investment, Interview with Justin Lane 21/03/2025 We are thrilled to celebrate a major milestone for CulturePulse , one of our alumni startups, as they secure a $1\.5 million Seed investment from B Ventures Group \(USA\), Simpact VC \(PL\), and Rockaway Ventures \(CZ\)\!”
19. [openalex\.org](https://openalex.org/W4328049281) · Public technical artifact · Research paper · 2023\-03\-21 — “Paramilitaries, parochialism, and peace: The moral foundations and personality traits of Slovenskí Branci · PLoS ONE · cited 7×”
20. [openalex\.org](https://openalex.org/W3129924748) · Public technical artifact · Research paper · 2023\-04\-03 — “The Moral Foundations of Left\-Wing Authoritarianism: On the Character, Cohesion, and Clout of Tribal Equalitarian Discourse · Journal of Cognition and Culture · cited 10×”
21. [github\.com](https://github.com/culturepulse/vaccinehesitancy) · Public technical artifact · GitHub repository · 2022\-03\-07 — “culturepulse/vaccinehesitancy · A repository for data from the vaccine hesitancy study done with Kingston University\. · HTML · last push 2022\-03\-07”
22. [github\.com](https://github.com/culturepulse/LWA_supplemental_material) · Public technical artifact · GitHub repository · 2023\-03\-20 — “culturepulse/LWA\_supplemental\_material · Supplimental Material for the Lane, McCaffree, Shults publication · HTML · last push 2023\-03\-20”
23. [teraz\.sk](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html) · Independent press · Pricing — “Investícia umožní spoločnosti ďalší globálny rozvoj a nábor špičkových talentov\.”
24. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Press article · 2023\-04\-20 — “Slovakian social media analytics start\-up CulturePulse AI raises 'just shy of $1 million' to pivot to AI SaaS model \- Tech\.eu”
25. [finalfrontier\.vc](https://finalfrontier.vc/newsroom/3062026) · Independent press · Press article · 2026\-06\-30 — “Final Frontier Backs CulturePulse to Scale AI That Predicts Conflict Before It Happens”
26. [en\.ain\.ua](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/) · Independent press · Funding round — “UPD 21\.03\.25: It became known that B Ventures Group and Simpact Ventures are also among the investors in CulturePulse during its €1\.5 million Series A funding round\.”
27. [teraz\.sk](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html) · Independent press · Funding round — “Investíciu 1,5 milióna USD poskytli podľa neho tri medzinárodné investičné fondy, každý s výškou 500\.000 USD\.”
28. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Product capability — “creates a psychologically accurate digital twin of the audience and measures messages against the beliefs and values of the intended audience\.”
29. [en\.ain\.ua](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/) · Independent press · Product capability — “CulturePulse creates a behavioral and psychological digital twin of an audience that users can test content on for resonance before testing live\.”
30. [github\.com](https://github.com/culturepulse/frontend_assignement) · Public technical artifact · GitHub repository · 2026\-04\-06 — “culturepulse/frontend\_assignement · TypeScript · last push 2026\-04\-06”
31. [culturepulse\.ai](https://www.culturepulse.ai) · Public technical artifact · Technology detected
32. [tehnopol\.ee](https://www.tehnopol.ee/en/startup-story-culturepulse-x-nato-diana-estonian-accelerator/) · Independent press · Press article · 2026\-04\-02 — “Startup story: CulturePulse X NATO DIANA Estonian Accelerator”
33. [bird\-incubator\.com](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/) · Independent press · Press article · 2025\-03\-21 — “Alumni Startup CulturePulse Secures $1\.5M Investment, Interview with Justin Lane \| BIRD Incubator”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 1 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | hlidac\_statu, starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 23 | press:en\.ceo\.com\.pl, press:engineering\.sk, press:forbes\.sk, press:orsr\.sk, press:sk\.ceo\.com\.pl, press:startupfundraising\.com |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 1 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 5 | crt\_sh |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 8 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 7 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 5 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 33 | — |

Analysis: gpt\-5\-mini (cost $0.0000); AI extraction cost $0.0073. Full fact table: CSV export.

## Source appendix (all collected facts)

- F3471 · registry\_flag · Medium confidence · [https://culturepulse\.ai/](https://culturepulse.ai/)
- F3472 · web\_page · Sourced · [https://www\.culturepulse\.ai](https://www.culturepulse.ai)
- F3473 · tech\_stack · Medium confidence · [https://www\.culturepulse\.ai](https://www.culturepulse.ai)
- F3474 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=culturepulse\.ai&amp;type=MX](https://dns.google/resolve?name=culturepulse.ai&type=MX)
- F3475 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=culturepulse\.ai&amp;type=TXT](https://dns.google/resolve?name=culturepulse.ai&type=TXT)
- F3476 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=culturepulse\.ai&amp;type=TXT](https://dns.google/resolve?name=culturepulse.ai&type=TXT)
- F3477 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=culturepulse\.ai&amp;type=TXT](https://dns.google/resolve?name=culturepulse.ai&type=TXT)
- F3478 · source\_unavailable · Unavailable · [https://crt\.sh/?q=%25\.culturepulse\.ai&amp;output=json](https://crt.sh/?q=%25.culturepulse.ai&output=json)
- F3479 · github\_org · Sourced · [https://github\.com/culturepulse](https://github.com/culturepulse)
- F3480 · repo · Sourced · [https://github\.com/culturepulse/frontend\_assignement](https://github.com/culturepulse/frontend_assignement)
- F3481 · repo · Sourced · [https://github\.com/culturepulse/mkdocs\-kuma\-uptime\-badge](https://github.com/culturepulse/mkdocs-kuma-uptime-badge)
- F3482 · repo · Sourced · [https://github\.com/culturepulse/fractalzoomVR](https://github.com/culturepulse/fractalzoomVR)
- F3483 · repo · Sourced · [https://github\.com/culturepulse/community\-synchronizer](https://github.com/culturepulse/community-synchronizer)
- F3484 · repo · Sourced · [https://github\.com/culturepulse/LWA\_supplemental\_material](https://github.com/culturepulse/LWA_supplemental_material)
- F3485 · repo · Sourced · [https://github\.com/culturepulse/vaccinehesitancy](https://github.com/culturepulse/vaccinehesitancy)
- F3486 · repo · Sourced · [https://github\.com/culturepulse/censorshipderadsim](https://github.com/culturepulse/censorshipderadsim)
- F3487 · paper · Medium confidence · [https://openalex\.org/W4220801307](https://openalex.org/W4220801307)
- F3488 · paper · Medium confidence · [https://openalex\.org/W4407175057](https://openalex.org/W4407175057)
- F3489 · paper · Medium confidence · [https://openalex\.org/W4362657727](https://openalex.org/W4362657727)
- F3490 · paper · Medium confidence · [https://openalex\.org/W4381892632](https://openalex.org/W4381892632)
- F3491 · paper · Medium confidence · [https://openalex\.org/W4410568563](https://openalex.org/W4410568563)
- F3492 · paper · Medium confidence · [https://openalex\.org/W4328049281](https://openalex.org/W4328049281)
- F3493 · paper · Medium confidence · [https://openalex\.org/W3129924748](https://openalex.org/W3129924748)
- F3494 · wayback\_first · Sourced · [https://web\.archive\.org/web/20220309155022/https://www\.culturepulse\.ai/](https://web.archive.org/web/20220309155022/https://www.culturepulse.ai/)
- F3495 · wayback\_first · Sourced · [https://web\.archive\.org/web/20230324034614/https://culturepulse\.ai/pricing](https://web.archive.org/web/20230324034614/https://culturepulse.ai/pricing)
- F3496 · wayback\_first · Sourced · [https://web\.archive\.org/web/20221209214450/https://culturepulse\.ai/careers](https://web.archive.org/web/20221209214450/https://culturepulse.ai/careers)
- F3497 · wayback\_first · Sourced · [https://web\.archive\.org/web/20220315190623/https://culturepulse\.ai/blog/the\-censorship\-effect\-radicalization\-censorship\-and\-social\-media\-echo\-chambers](https://web.archive.org/web/20220315190623/https://culturepulse.ai/blog/the-censorship-effect-radicalization-censorship-and-social-media-echo-chambers)
- F3498 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/culturepulse\.ai](https://web.archive.org/web/%2A/culturepulse.ai)
- F3502 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3503 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3504 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3505 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3506 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3507 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3508 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3509 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3510 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3511 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3512 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3513 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3514 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3515 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3516 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3517 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3518 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3519 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3520 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3521 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3522 · source\_unavailable · Unavailable · [https://www\.orsr\.sk/vypis\.asp?ID=739114&amp;SID=2&amp;P=1](https://www.orsr.sk/vypis.asp?ID=739114&SID=2&P=1)
- F3523 · press\_mention · Sourced · [https://tech\.eu/2023/04/20/slovakian\-social\-media\-analytics\-start\-up\-culturepulse\-ai\-raises\-just\-shy\-of\-1\-million\-to\-pivot\-to\-ai\-saas\-model/](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
- F3524 · press\_mention · Sourced · [https://cc\.cz/vidi\-do\-hlavy\-izraelcum\-i\-palestincum\-startup\-predpovida\-hrozby\-ted\-ziskava\-dalsi\-investici/](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/)
- F3525 · press\_mention · Sourced · [https://www\.rockawaycapital\.com/en/news/rockaway\-ventures\-invests\-in\-culturepulse\-driving\-innovation\-in\-behavioral\-analysis\-and\-security\-risk\-prediction\-across\-europe\-and\-beyond](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)
- F3526 · press\_mention · Sourced · [https://www\.tehnopol\.ee/en/startup\-story\-culturepulse\-x\-nato\-diana\-estonian\-accelerator/](https://www.tehnopol.ee/en/startup-story-culturepulse-x-nato-diana-estonian-accelerator/)
- F3527 · press\_mention · Sourced · [https://www\.therecursive\.com/rockaway\-capital\-invests\-e1\-45m\-in\-us\-slovak\-startup\-culturepulse](https://www.therecursive.com/rockaway-capital-invests-e1-45m-in-us-slovak-startup-culturepulse)
- F3528 · press\_mention · Sourced · [https://aws\.amazon\.com/marketplace/seller\-profile?id=seller\-zsdzmjc7npmiq](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq)
- F3529 · press\_mention · Sourced · [https://bird\-incubator\.com/news/alumni\-startup\-culturepulse\-secures\-1\-5m\-investment\-interview\-with\-justin\-lane/](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/)
- F3530 · press\_mention · Sourced · [https://fontech\.startitup\.sk/spravy/ai\-ludske\-spravanie\-investicia/](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
- F3531 · press\_mention · Sourced · [https://en\.ain\.ua/2025/03/21/culturepulse\-raises\-eur145m/](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- F3532 · press\_mention · Sourced · [https://www\.trend\.sk/spravy/slovensko\-americky\-startup\-ziskal\-investiciu\-1\-5\-milionov\-dolarov](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov)
- F3533 · source\_unavailable · Unavailable · [https://sk\.ceo\.com\.pl/Spolo%C4%8Dnos%C5%A5\-Simpact\-Ventures\-a\-jej\-partneri\-investuj%C3%BA\-do\-platformy\-pre\-anal%C3%BDzu\-soci%C3%A1lnej\-dynamiky\-CulturePulse\-96787](https://sk.ceo.com.pl/Spolo%C4%8Dnos%C5%A5-Simpact-Ventures-a-jej-partneri-investuj%C3%BA-do-platformy-pre-anal%C3%BDzu-soci%C3%A1lnej-dynamiky-CulturePulse-96787)
- F3534 · press\_mention · Sourced · [https://www\.teraz\.sk/ekonomika/slovensko\-americky\-startup\-ziskal\-inve/855582\-clanok\.html](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html)
- F3535 · source\_unavailable · Unavailable · [https://en\.ceo\.com\.pl/simpact\-ventures\-and\-partners\-invest\-in\-social\-dynamics\-analytics\-platform\-culturepulse\-96787](https://en.ceo.com.pl/simpact-ventures-and-partners-invest-in-social-dynamics-analytics-platform-culturepulse-96787)
- F3536 · press\_mention · Sourced · [https://bestpitchdeck\.com/culturepulse](https://bestpitchdeck.com/culturepulse)
- F3537 · press\_mention · Sourced · [https://www\.therecursive\.com/deeptech\-startup\-culturepulse\-raises\-1m\-for\-al\-that\-can\-analyze\-human\-emotions](https://www.therecursive.com/deeptech-startup-culturepulse-raises-1m-for-al-that-can-analyze-human-emotions)
- F3538 · source\_unavailable · Unavailable · [https://www\.forbes\.sk/kombinacia\-ai\-a\-nabozenstva\-zaujala\-fondy\-slovensko\-americky\-startup\-culturepulse\-dostal\-novu\-investiciu/](https://www.forbes.sk/kombinacia-ai-a-nabozenstva-zaujala-fondy-slovensko-americky-startup-culturepulse-dostal-novu-investiciu/)
- F3539 · source\_unavailable · Unavailable · [https://www\.engineering\.sk/sk/aktuality/65532\-it\-slovensko\-americky\-startup\-ziskal\-investiciu\-15\-mil\-usd\-na\-dalsi\-rozvoj\-2025\-02\-10](https://www.engineering.sk/sk/aktuality/65532-it-slovensko-americky-startup-ziskal-investiciu-15-mil-usd-na-dalsi-rozvoj-2025-02-10)
- F3540 · press\_mention · Sourced · [https://en\.ain\.ua/2023/04/21/culturepulse\-secures\-1m/](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
- F3541 · source\_unavailable · Unavailable · [https://startupfundraising\.com/library/articles/culturepulse\-s\-1m\-pitch\-deck\-teardown](https://startupfundraising.com/library/articles/culturepulse-s-1m-pitch-deck-teardown)
- F3542 · press\_mention · Sourced · [https://techcrunch\.com/2023/06/09/sample\-seed\-pitch\-deck\-culturepulse](https://techcrunch.com/2023/06/09/sample-seed-pitch-deck-culturepulse)
- F3543 · press\_mention · Sourced · [https://www\.thesaasnews\.com/news/culturepulse\-closes\-1\-million\-in\-seed\-round/](https://www.thesaasnews.com/news/culturepulse-closes-1-million-in-seed-round/)
- F3544 · press\_mention · Sourced · [https://finalfrontier\.vc/newsroom/3062026](https://finalfrontier.vc/newsroom/3062026)
- F3545 · press\_mention · Sourced · [https://www\.wired\.com/story/culturepulse\-ai\-israeli\-palestinian\-crisis](https://www.wired.com/story/culturepulse-ai-israeli-palestinian-crisis)
- F3546 · press\_mention · Sourced · [https://www\.simpact\.vc/en/portfolio/culturepulse/](https://www.simpact.vc/en/portfolio/culturepulse/)
- F3547 · press\_mention · Sourced · [https://en\.ain\.ua/2023/04/25/startup\-of\-the\-day\-culturepulse\-slovak\-social\-media\-analytics\-company/](https://en.ain.ua/2023/04/25/startup-of-the-day-culturepulse-slovak-social-media-analytics-company/)
- F3548 · press\_mention · Sourced · [https://finalfrontier\.vc/portfolio/culturepulse](https://finalfrontier.vc/portfolio/culturepulse)
- F3549 · press\_mention · Sourced · [https://www\.nextech\.sk/a/Slovensko\-americky\-startup\-ziskal\-investiciu\-1\-5\-miliona\-dolarov\-na\-riesenie\-globalnych\-konfliktov](https://www.nextech.sk/a/Slovensko-americky-startup-ziskal-investiciu-1-5-miliona-dolarov-na-riesenie-globalnych-konfliktov)
- F3550 · press\_mention · Sourced · [https://startupkitchen\.community/rockaway\-ventures\-invests\-in\-culturepulse\-a\-slovak\-company\-redefining\-whats\-possible\-in\-behavioral\-analysis\-and\-risk\-prediction/](https://startupkitchen.community/rockaway-ventures-invests-in-culturepulse-a-slovak-company-redefining-whats-possible-in-behavioral-analysis-and-risk-prediction/)
- F5515 · source\_unavailable · Unavailable · [https://www\.hlidacstatu\.cz/hledat](https://www.hlidacstatu.cz/hledat)
- F5516 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27CulturePulse%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27CulturePulse%27)
- F5517 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F5950 · funding\_round · Medium confidence · [https://tech\.eu/2023/04/20/slovakian\-social\-media\-analytics\-start\-up\-culturepulse\-ai\-raises\-just\-shy\-of\-1\-million\-to\-pivot\-to\-ai\-saas\-model/](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
- F5951 · product\_capability · Medium confidence · [https://tech\.eu/2023/04/20/slovakian\-social\-media\-analytics\-start\-up\-culturepulse\-ai\-raises\-just\-shy\-of\-1\-million\-to\-pivot\-to\-ai\-saas\-model/](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
- F5952 · product\_capability · Medium confidence · [https://tech\.eu/2023/04/20/slovakian\-social\-media\-analytics\-start\-up\-culturepulse\-ai\-raises\-just\-shy\-of\-1\-million\-to\-pivot\-to\-ai\-saas\-model/](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
- F5953 · product\_capability · Medium confidence · [https://tech\.eu/2023/04/20/slovakian\-social\-media\-analytics\-start\-up\-culturepulse\-ai\-raises\-just\-shy\-of\-1\-million\-to\-pivot\-to\-ai\-saas\-model/](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
- F5954 · funding\_round · Medium confidence · [https://cc\.cz/vidi\-do\-hlavy\-izraelcum\-i\-palestincum\-startup\-predpovida\-hrozby\-ted\-ziskava\-dalsi\-investici/](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/)
- F5955 · tech\_claim · Medium confidence · [https://cc\.cz/vidi\-do\-hlavy\-izraelcum\-i\-palestincum\-startup\-predpovida\-hrozby\-ted\-ziskava\-dalsi\-investici/](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/)
- F5956 · funding\_round · Medium confidence · [https://www\.rockawaycapital\.com/en/news/rockaway\-ventures\-invests\-in\-culturepulse\-driving\-innovation\-in\-behavioral\-analysis\-and\-security\-risk\-prediction\-across\-europe\-and\-beyond](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)
- F5957 · product\_capability · Medium confidence · [https://www\.rockawaycapital\.com/en/news/rockaway\-ventures\-invests\-in\-culturepulse\-driving\-innovation\-in\-behavioral\-analysis\-and\-security\-risk\-prediction\-across\-europe\-and\-beyond](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)
- F5958 · tech\_claim · Medium confidence · [https://www\.rockawaycapital\.com/en/news/rockaway\-ventures\-invests\-in\-culturepulse\-driving\-innovation\-in\-behavioral\-analysis\-and\-security\-risk\-prediction\-across\-europe\-and\-beyond](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)
- F5959 · funding\_round · Medium confidence · [https://www\.therecursive\.com/rockaway\-capital\-invests\-e1\-45m\-in\-us\-slovak\-startup\-culturepulse](https://www.therecursive.com/rockaway-capital-invests-e1-45m-in-us-slovak-startup-culturepulse)
- F5960 · funding\_round · Medium confidence · [https://bird\-incubator\.com/news/alumni\-startup\-culturepulse\-secures\-1\-5m\-investment\-interview\-with\-justin\-lane/](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/)
- F5961 · product\_capability · Medium confidence · [https://bird\-incubator\.com/news/alumni\-startup\-culturepulse\-secures\-1\-5m\-investment\-interview\-with\-justin\-lane/](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/)
- F5962 · tech\_claim · Medium confidence · [https://bird\-incubator\.com/news/alumni\-startup\-culturepulse\-secures\-1\-5m\-investment\-interview\-with\-justin\-lane/](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/)
- F5963 · team\_claim · Medium confidence · [https://bird\-incubator\.com/news/alumni\-startup\-culturepulse\-secures\-1\-5m\-investment\-interview\-with\-justin\-lane/](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/)
- F5964 · tech\_claim · Medium confidence · [https://fontech\.startitup\.sk/spravy/ai\-ludske\-spravanie\-investicia/](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
- F5965 · tech\_claim · Medium confidence · [https://fontech\.startitup\.sk/spravy/ai\-ludske\-spravanie\-investicia/](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
- F5966 · team\_claim · Medium confidence · [https://fontech\.startitup\.sk/spravy/ai\-ludske\-spravanie\-investicia/](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
- F5967 · product\_capability · Medium confidence · [https://fontech\.startitup\.sk/spravy/ai\-ludske\-spravanie\-investicia/](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
- F5968 · funding\_round · Medium confidence · [https://en\.ain\.ua/2025/03/21/culturepulse\-raises\-eur145m/](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- F5969 · funding\_round · Medium confidence · [https://en\.ain\.ua/2025/03/21/culturepulse\-raises\-eur145m/](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- F5970 · tech\_claim · Medium confidence · [https://en\.ain\.ua/2025/03/21/culturepulse\-raises\-eur145m/](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- F5973 · team\_claim · Medium confidence · [https://en\.ain\.ua/2025/03/21/culturepulse\-raises\-eur145m/](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- F5974 · funding\_round · Medium confidence · [https://en\.ain\.ua/2025/03/21/culturepulse\-raises\-eur145m/](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- F5975 · product\_capability · Medium confidence · [https://www\.trend\.sk/spravy/slovensko\-americky\-startup\-ziskal\-investiciu\-1\-5\-milionov\-dolarov](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov)
- F5976 · tech\_claim · Medium confidence · [https://www\.trend\.sk/spravy/slovensko\-americky\-startup\-ziskal\-investiciu\-1\-5\-milionov\-dolarov](https://www.trend.sk/spravy/slovensko-americky-startup-ziskal-investiciu-1-5-milionov-dolarov)
- F5977 · funding\_round · Medium confidence · [https://www\.teraz\.sk/ekonomika/slovensko\-americky\-startup\-ziskal\-inve/855582\-clanok\.html](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html)
- F5978 · pricing · Medium confidence · [https://www\.teraz\.sk/ekonomika/slovensko\-americky\-startup\-ziskal\-inve/855582\-clanok\.html](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html)
- F5979 · product\_capability · Medium confidence · [https://www\.teraz\.sk/ekonomika/slovensko\-americky\-startup\-ziskal\-inve/855582\-clanok\.html](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html)
- F5980 · product\_capability · Medium confidence · [https://www\.therecursive\.com/deeptech\-startup\-culturepulse\-raises\-1m\-for\-al\-that\-can\-analyze\-human\-emotions](https://www.therecursive.com/deeptech-startup-culturepulse-raises-1m-for-al-that-can-analyze-human-emotions)
- F5981 · funding\_round · Medium confidence · [https://en\.ain\.ua/2023/04/21/culturepulse\-secures\-1m/](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
- F5983 · product\_capability · Medium confidence · [https://en\.ain\.ua/2023/04/21/culturepulse\-secures\-1m/](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
- F5984 · product\_capability · Medium confidence · [https://en\.ain\.ua/2023/04/21/culturepulse\-secures\-1m/](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
- F5985 · product\_capability · Medium confidence · [https://en\.ain\.ua/2023/04/21/culturepulse\-secures\-1m/](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
