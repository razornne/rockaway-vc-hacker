# CulturePulse — due diligence brief

culturepulse\.ai · SK/US · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A self\-service SaaS platform \(ARES\) that builds psychologically realistic 'digital twins' from text to predict social, security and business risks for enterprise/governmental analysts and planners\. *(Corroborated)* ^[1](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/),[2](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[3](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- **Stage & traction.** Reported Seed \(\~$1M\) in 2023 and a follow\-on €1\.45–$1\.5M round reported in 2025 with Rockaway and other VCs; AWS Marketplace seller profile and multiple press mentions\. *(Corroborated)* ^[4](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[5](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/),[6](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond),[7](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq)
- **Technology & moat.** Public evidence shows domain expertise — multiple peer‑reviewed papers and public simulation/code repositories — but no disclosed proprietary model weights or certifications\. *(Verified)* ^[8](https://openalex.org/W4220801307),[9](https://openalex.org/W4407175057),[10](https://github.com/culturepulse/censorshipderadsim)
- **Key risk.** Core accuracy and multilingual claims \(≈95% correlation; 80–200\+ languages, 93 dimensions\) are company\-reported and appear unverified externally\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/),[12](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[13](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
- **Diligence focus.** First verify the empirical basis for the 95% correlation and multilingual performance \(datasets, evaluation protocol, holdout results\), as this underpins commercial defensibility\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/),[12](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[13](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2023\-04\-20 · Seed · just south of $1 million · Zero Gravity Capital · 2 reports; 2025\-02\-06 · Series A · $1\.5 million · Rockaway Ventures \(Rockaway Capital\), B Ventures Group \(USA\), Simpact VC \(PL\), Rockaway Ve · 6 reports; 2025\-02\-10 · strategická investícia · 1,5 milióna USD · B Ventures group \(USA\), Rockaway Ventures Fund \(Česko\), Simpact Ventures \(Poľsko\) | 4, 14, 5, 15, 16, 17 |
| Thesis fit \(Rockaway\) | sectors: AI\-led transformative tech \(19 facts\); defence / dual\-use \(3 facts\) · geography: SK/US \(core region\) · overlaps portfolio: BudgetBakers \(finance, persona\) | 9, 18, 19, 20 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; own\-model evidence: 7 papers, 0 verified HF models, 0 ML roles, 0 own\-model claims | 8, 21, 22 |
| Engineering footprint | 7 public repos \(1★, last push 2026\-04\-06\); stack: AmazonS3 | 10, 23, 24 |
| Customers | public pricing: yes | 25 |
| Timeline | first press 2023\-04\-20 \(23 articles collected\) | 18 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the market, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** AI\-led transformative tech — company sells AI behavioral models, multilingual text analysis and psychological digital twins for audience simulation\. *(Analyst view)* ^[2](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[13](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/),[26](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
  - Assumption: Product claims map to the fund's AI thesis\.
- **Portfolio overlap:** BudgetBakers — CulturePulse's capabilities \(audience digital twins, behavioral analytics\) differ from personal\-finance product, so likely no direct product conflict; potential marketing/customer overlap is possible\. *(Analyst view)* ^[2](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[27](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
  - Assumption: BudgetBakers is a personal finance product \(DERIVED\)\.

## Business model

- Primary monetization described as a self\-service SaaS platform delivering on‑demand behavioral insights to clients\. *(Analyst view)* ^[1](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/)
  - Assumption: Self\-service implies subscription or usage pricing\.
- Go\-to\-market channels include AWS Marketplace \(seller profile listed\), indicating a route to commercial procurement and enterprise buyers\. *(Analyst view)* ^[7](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq)
  - Assumption: AWS Marketplace listing implies commercial availability\.
- Current cash runway effects: company completed seed and Series A equity financings \(2023 seed; 2025 Series A\), not grants — these are investor capital, not operational revenue\. *(Analyst view)* ^[4](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[5](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/)
  - Assumption: Fundraises were used for product and team expansion\.

## Market

- Stated demand drivers: governments and organisations seeking security‑risk prediction and social\-dynamics insights \(Rockaway press release frames security/business risk use cases\)\. *(Analyst view)* ^[28](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond),[6](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)
  - Assumption: Investor messaging reflects intended buyers\.
- Stated demand drivers: commercial applications include marketing strategy and urban planning, per company statements about broad industry applications\. *(Analyst view)* ^[29](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
  - Assumption: Press relays company market targets\.
- Defence interest signal: participation in a NATO DIANA Estonian accelerator suggests explicit defence/dual\-use market pathways\. *(Analyst view)* ^[19](https://www.tehnopol.ee/en/startup-story-culturepulse-x-nato-diana-estonian-accelerator/)
  - Assumption: Accelerator involvement implies defence engagement\.

## Competition

No sourced findings for this section.

## Case for and against

- **For:** Differentiated technical claims — multilingual analysis \(100\+ / 200 languages\), 93‑dimension psychological profiling and population\-level digital twins\. *(Analyst view)* ^[12](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[13](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/),[26](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
  - Assumption: Claims are technically deliverable as stated\.
- **For:** Early validation / traction signals — AWS Marketplace presence and recent institutional Series A lead by Rockaway Ventures indicate investor and channel interest\. *(Analyst view)* ^[7](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq),[5](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/)
  - Assumption: Marketplace listing and lead investment imply commercial intent\.
- **Against:** Core accuracy claims \(≈95% correlation\) are material to product credibility; these are company\-claimed and require independent validation\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
  - Assumption: Adoption depends on third‑party validation\.
- **Against:** Dual\-use and defence positioning raises reputational, regulatory and procurement risks that could limit commercial routes or require compliance work\. *(Analyst view)* ^[3](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/),[19](https://www.tehnopol.ee/en/startup-story-culturepulse-x-nato-diana-estonian-accelerator/)
  - Assumption: Defence use increases governance scrutiny\.
- **Must be true:** Third‑party validation of predictive accuracy \(benchmarks, peer review or independent audits\) must exist and be shareable\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/),[2](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
  - Assumption: Validation results are documented and accessible\.
- **Must be true:** Evidence of paying customers or executed contracts \(marketplace sales, enterprise pilots or public procurement wins\) that demonstrate commercial demand\. *(Analyst view)* ^[7](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq),[1](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/)
  - Assumption: Marketplace listing and self‑service product should yield customers\.

# Technical due diligence

## Ownership and capital

- Reported financing: Seed 'just south of $1M' led by Zero Gravity \(2023\) and a 2025 round reported at $1\.5M / €1\.45M led/backed by Rockaway Ventures with B Ventures and Simpact noted\. *(Corroborated)* ^[4](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[5](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/),[30](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/),[31](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- Company states it will use proceeds to expand headcount and accelerate product development and go‑to‑market\. *(Corroborated)* ^[29](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/),[32](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html)

## Technology profile

- Product capabilities \(company claims\): multilingual text analysis, 93‑dimension psychological profiling, behavioral digital twins for testing messaging and risk prediction \(ARES branding cited\)\. *(Corroborated)* ^[27](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[12](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[3](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
  - Assumption: These are company/press claims, not independent verifications\.
- Engineering footprint: public GitHub org with multiple repos \(research and tooling\), several active pushes including a 2026 frontend repo; cloud usage indicated \(Amazon S3\)\. *(Verified)* ^[33](https://github.com/culturepulse),[34](https://github.com/culturepulse/frontend_assignement),[10](https://github.com/culturepulse/censorshipderadsim),[35](https://www.culturepulse.ai)
- AI dependency: no supplied facts name third‑party LLM vendors as required subprocessors or integrations; evidence primarily shows academic papers and in‑house modeling claims\. *(Verified)* ^[8](https://openalex.org/W4220801307),[9](https://openalex.org/W4407175057),[36](https://openalex.org/W4381892632)

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** Linguistic feature extraction and 93‑dimension psychological profiling could be reproduced using open NLP libraries and standard psychometric scales if datasets are available \(public repos show relevant research code\)\. *(Analyst view)* ^[10](https://github.com/culturepulse/censorshipderadsim),[27](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
  - Assumption: Access to the same training/labelled datasets is required\.
- **Edge supported by public evidence:** Peer‑reviewed papers and published simulation code indicate academic credibility and domain expertise, supporting a research edge rather than a proven production moat\. *(Analyst view)* ^[8](https://openalex.org/W4220801307),[9](https://openalex.org/W4407175057),[10](https://github.com/culturepulse/censorshipderadsim)
  - Assumption: Papers represent affiliated research but not deployed model weights\.
- **Cannot be judged from outside:** True production accuracy, multilingual generalization, data pipelines, and model robustness cannot be judged from public papers and repos alone without held‑out evaluations and code/models\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/),[34](https://github.com/culturepulse/frontend_assignement)
  - Assumption: External test datasets and internal evaluations are unavailable publicly\.

## Risks and caveats

- Unverified performance claim: the '≈95% clinical accuracy correlation' figure is asserted in press coverage but lacks independent verification in supplied facts\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/),[18](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/)
- Concentration risk in investor base for recent round: reported reliance on a small number of lead VCs for the 2025 round\. *(Analyst view)* ^[5](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/),[30](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/),[31](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/)
- Commercial validation gap: no named paying customers were found in the supplied facts despite an AWS Marketplace seller profile and repeated press coverage\. *(Analyst view)* ^[7](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq),[6](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)

## Questions for founders

- Request: provide held‑out evaluation datasets, evaluation protocol and confusion matrices underpinning the '95% correlation' claim referenced in press\. *(Analyst view)* ^[11](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/)
- Request: list paying customers or signed purchase contracts and provide redacted references for enterprise pilots versus R&amp;D collaborations\. *(Analyst view)* ^[7](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq),[6](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond)
- Request: supply details on multilingual training—corpora, annotation methodology, and out‑of‑language evaluations supporting 80–200\+ language claims\. *(Analyst view)* ^[12](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/),[13](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/)
- Request: codebase maturity and deployment architecture evidence \(CI, model serving, data retention/compliance\) beyond public GitHub repos\. *(Analyst view)* ^[34](https://github.com/culturepulse/frontend_assignement),[10](https://github.com/culturepulse/censorshipderadsim),[35](https://www.culturepulse.ai)

## Sources

1. [bird\-incubator\.com](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/) · Independent press · Product capability — “The key focus of this funding is to develop scalable products that can deliver our insights quickly and affordably \. Our AI is designed to predict large\-scale behavioral trends , so we are building a self\-service platform that allows clients to access these insights on demand\.”
2. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Product capability — “creates a psychologically accurate digital twin of the audience and measures messages against the beliefs and values of the intended audience\.”
3. [en\.ain\.ua](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/) · Independent press · Technical claim — “ARES allows clients to better understand the complexities of social dynamics and predict both security and business risks on a global scale\.”
4. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Funding round — “just south of $1 million Seed round from Zero Gravity Capital to move the AI software to a SaaS platform while 'expanding the team to bolster the sales efforts and expand to new markets'\.”
5. [cc\.cz](https://cc.cz/vidi-do-hlavy-izraelcum-i-palestincum-startup-predpovida-hrozby-ted-ziskava-dalsi-investici/) · Independent press · Funding round — “V rámci investičního kola takzvané série A získala společnost financování ve výši 1,5 milionu dolarů \(přes 36 milionů korun\)”
6. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond) · Independent press · Press article · 2025\-02\-07 — “Rockaway Ventures Invests in CulturePulse: Driving Innovation in Behavioral Analysis and Security Risk Prediction Across Europe and Beyond – Rockaway Capital”
7. [aws\.amazon\.com](https://aws.amazon.com/marketplace/seller-profile?id=seller-zsdzmjc7npmiq) · Independent press · Press article — “CulturePulse Seller Profile \| AWS Marketplace”
8. [openalex\.org](https://openalex.org/W4220801307) · Public technical artifact · Research paper · 2022\-03\-17 — “What causes COVID\-19 vaccine hesitancy? Ignorance and the lack of bliss in the United Kingdom · Humanities and Social Sciences Communications · cited 47×”
9. [openalex\.org](https://openalex.org/W4407175057) · Public technical artifact · Research paper · 2025\-02\-05 — “Simulating theory and society: How multi\-agent artificial intelligence modeling contributes to renewal and critique in social theory · Theory and Society · cited 16×”
10. [github\.com](https://github.com/culturepulse/censorshipderadsim) · Public technical artifact · GitHub repository · 2021\-12\-30 — “culturepulse/censorshipderadsim · A public repository for code, analyses and information related to the models, simulations, data, results, and discussions of the paper "Social Media Censorship Can Reinforce Radicalization" · last push 2021\-12\-30”
11. [en\.ain\.ua](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/) · Independent press · Product capability — “The startup also claims that its solution predicts with clinical accuracy of almost 95% correlation\.”
12. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Product capability — “While most technologies on the market can only function in a small handful of languages, CulturePulse is unique as it works across 100\+ languages, covering 99% of digital texts without the need for historical data and training”
13. [fontech\.startitup\.sk](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/) · Independent press · Technical claim — “Technológia vyvinutá CulturePulse má podľa neho schopnosť analyzovať texty vo viac ako 200 jazykoch a vytvárať psychologické profily na 93 rôznych dimenziách\.”
14. [en\.ain\.ua](https://en.ain.ua/2023/04/21/culturepulse-secures-1m/) · Independent press · Funding round — “On the beginning of 2023, Zero Gravity led a €1 million round for Readmio, the developer of an app with fairy tales for children\.”
15. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond) · Independent press · Funding round — “The company aims to use the $1\.5 million raised in its first investment round, which remains open to additional investors, to expand its team and accelerate product development\.”
16. [therecursive\.com](https://www.therecursive.com/rockaway-capital-invests-e1-45m-in-us-slovak-startup-culturepulse) · Independent press · Funding round — “Rockaway Capital Invests €1\.45M in US\-Slovak Startup CulturePulse”
17. [bird\-incubator\.com](https://bird-incubator.com/news/alumni-startup-culturepulse-secures-1-5m-investment-interview-with-justin-lane/) · Independent press · Funding round — “CulturePulse Secures $1\.5M Investment, Interview with Justin Lane 21/03/2025 We are thrilled to celebrate a major milestone for CulturePulse , one of our alumni startups, as they secure a $1\.5 million Seed investment from B Ventures Group \(USA\), Simpact VC \(PL\), and Rockaway Ventures \(CZ\)\!”
18. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Press article · 2023\-04\-20 — “Slovakian social media analytics start\-up CulturePulse AI raises 'just shy of $1 million' to pivot to AI SaaS model \- Tech\.eu”
19. [tehnopol\.ee](https://www.tehnopol.ee/en/startup-story-culturepulse-x-nato-diana-estonian-accelerator/) · Independent press · Press article · 2026\-04\-02 — “Startup story: CulturePulse X NATO DIANA Estonian Accelerator”
20. [finalfrontier\.vc](https://finalfrontier.vc/newsroom/3062026) · Independent press · Press article · 2026\-06\-30 — “Final Frontier Backs CulturePulse to Scale AI That Predicts Conflict Before It Happens”
21. [openalex\.org](https://openalex.org/W4328049281) · Public technical artifact · Research paper · 2023\-03\-21 — “Paramilitaries, parochialism, and peace: The moral foundations and personality traits of Slovenskí Branci · PLoS ONE · cited 7×”
22. [openalex\.org](https://openalex.org/W3129924748) · Public technical artifact · Research paper · 2023\-04\-03 — “The Moral Foundations of Left\-Wing Authoritarianism: On the Character, Cohesion, and Clout of Tribal Equalitarian Discourse · Journal of Cognition and Culture · cited 10×”
23. [github\.com](https://github.com/culturepulse/vaccinehesitancy) · Public technical artifact · GitHub repository · 2022\-03\-07 — “culturepulse/vaccinehesitancy · A repository for data from the vaccine hesitancy study done with Kingston University\. · HTML · last push 2022\-03\-07”
24. [github\.com](https://github.com/culturepulse/LWA_supplemental_material) · Public technical artifact · GitHub repository · 2023\-03\-20 — “culturepulse/LWA\_supplemental\_material · Supplimental Material for the Lane, McCaffree, Shults publication · HTML · last push 2023\-03\-20”
25. [teraz\.sk](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html) · Independent press · Pricing — “Investícia umožní spoločnosti ďalší globálny rozvoj a nábor špičkových talentov\.”
26. [fontech\.startitup\.sk](https://fontech.startitup.sk/spravy/ai-ludske-spravanie-investicia/) · Independent press · Technical claim — “Tento nástroj dokáže modelovať tzv\. digitálne dvojičky populácií a krajín, čo poskytuje detailný pohľad na spoločenské dynamiky\.”
27. [tech\.eu](https://tech.eu/2023/04/20/slovakian-social-media-analytics-start-up-culturepulse-ai-raises-just-shy-of-1-million-to-pivot-to-ai-saas-model/) · Independent press · Product capability — “quantifies anger, anxiety, personality, morality, family, friends, finances, inclusivity, racism, hate speech, and 80\+ cultural categories\.”
28. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/rockaway-ventures-invests-in-culturepulse-driving-innovation-in-behavioral-analysis-and-security-risk-prediction-across-europe-and-beyond) · Independent press · Product capability — “CulturePulse’s platform allows clients to better understand the complexities of social dynamics and predict both security and business risks on a global scale\.”
29. [en\.ain\.ua](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/) · Independent press · Funding round — “CulturePulse will use new funding to expand the team and accelerate product development to broaden applications across industries such as marketing strategies and urban planning\.”
30. [en\.ain\.ua](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/) · Independent press · Funding round — “CulturePulse, a US\-Slovak startup specializing in advanced behavioral modeling, has raised €1\.5 million in Series A funding\. The round was backed by Czech\-founded Rockaway Ventures, and remains open to additional investors\.”
31. [en\.ain\.ua](https://en.ain.ua/2025/03/21/culturepulse-raises-eur145m/) · Independent press · Funding round — “UPD 21\.03\.25: It became known that B Ventures Group and Simpact Ventures are also among the investors in CulturePulse during its €1\.5 million Series A funding round\.”
32. [teraz\.sk](https://www.teraz.sk/ekonomika/slovensko-americky-startup-ziskal-inve/855582-clanok.html) · Independent press · Funding round — “Investíciu 1,5 milióna USD poskytli podľa neho tri medzinárodné investičné fondy, každý s výškou 500\.000 USD\.”
33. [github\.com](https://github.com/culturepulse) · Public technical artifact · GitHub organisation · 2021\-12\-27 — “culturepulse · 8 public repos”
34. [github\.com](https://github.com/culturepulse/frontend_assignement) · Public technical artifact · GitHub repository · 2026\-04\-06 — “culturepulse/frontend\_assignement · TypeScript · last push 2026\-04\-06”
35. [culturepulse\.ai](https://www.culturepulse.ai) · Public technical artifact · Technology detected
36. [openalex\.org](https://openalex.org/W4381892632) · Public technical artifact · Research paper · 2023\-06\-22 — “Computation of identity and social volatility in the ritual animal · Religion Brain &amp; Behavior”

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

Analysis: gpt\-5\-mini (cost $0.0180); AI extraction cost $0.0073. Full fact table: CSV export.

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
- F7703 · source\_unavailable · Unavailable · [https://www\.hlidacstatu\.cz/hledat](https://www.hlidacstatu.cz/hledat)
- F7704 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27CulturePulse%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27CulturePulse%27)
- F7705 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
