# Wultra — due diligence brief

wultra\.com · Wultra s\.r\.o\. · IČO 03643174 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** Commercial authentication products \(PowerAuth, mobile SDKs, FIDO2 tokens, post‑quantum authentication\) sold to banks and enterprises via licensing and per‑active‑user pricing\. *(Partly verified)* ^[1](https://github.com/wultra/powerauth-crypto),[2](https://github.com/wultra/powerauth-mobile-sdk),[3](https://www.wultra.com/products/talisman-fido2-hardware-token),[4](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/),[5](https://www.wultra.com/products/single-sign-on-sso)
- **Stage & traction.** Multiple funding events \(press: €3M 2025; Series A €6\.8M\), named banking customers and at least one government contract \(Česká pošta\) per public records\. *(Verified)* ^[4](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/),[6](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html),[7](https://cdn.prod.website-files.com/64fcce0d2e203c1c077a8c04/65c3aad8f10872792c8a7013_Wultra_CaseStudy_OTP_Bank.pdf),[8](https://smlouvy.gov.cz/smlouva/39855369)
- **Technology & moat.** Long‑running open PowerAuth crypto repos \(extensive, public\) plus a published patent application for security tokens—moat likely from protocol IP and customer integrations rather than closed proprietary code\. *(Verified)* ^[1](https://github.com/wultra/powerauth-crypto),[2](https://github.com/wultra/powerauth-mobile-sdk),[9](https://patents.google.com/patent/EM150508630001S)
- **Key risk.** Commercial claims about scale and revenue quality \("70 clients across 25 countries"\) appear in press but lack independent corroboration in registry or sales filings\. *(Analyst view)* ^[10](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html),[6](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html)
- **Diligence focus.** First verify enterprise customer contracts \(top 10 clients, ARR per client\) because technical IP is partly open‑source and valuation will hinge on contract stickiness and pricing\. *(Analyst view)* ^[3](https://www.wultra.com/products/talisman-fido2-hardware-token),[10](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html),[5](https://www.wultra.com/products/single-sign-on-sso)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2025\-01\-15 · €3M · Tensor Ventures, Elevator Ventures, J&amp;T Ventures; 2026\-06\-29 · Series A · 6,8 milionu eur · Seventure Partners, Ariadnex, J&amp;T Ventures, Elevator Ventures, Marc Norlain, Guillaume Des · 2 reports | 4, 11, 6 |
| Investors in registry | J&amp;T Ventures CG SICAV a\.s\. \(from 2021\-11\-26, 15\.0%\); J&amp;T Ventures CG SICAV a\.s\. \(from 2022\-01\-01, 17\.68%\); Tensor Co\-Investment Fund \(from 2025\-12\-03, 5\.44%\); SEVENTURE PARTNERS, SA à directoire \(from 2026\-06\-22, 5\.71%\); SEVENTURE PARTNERS, SA à directoire \(from 2026\-06\-22, 2\.45%\) | 12, 13, 14, 15, 16 |
| Public money | 1 contract\(s\), amount not published; 1 grant\(s\), amount not published · counterparties: Česká pošta, s\.p\. | 8, 17 |
| Hiring | 14 open roles: other 7, sales gtm 4, engineering 3 | 18, 19, 20, 21, 22, 23 |
| Engineering footprint | 15 public repos \(156★, last push 2026\-11\-16\); 3 subdomains; 3 docs pages; stack: Cloudflare, Webflow | 24, 25, 26, 27, 28 |
| Customers | 1 named: OTP Bank Moldova; public pricing: yes; 1 mobile app\(s\) | 3, 10, 29 |
| Claims checked | Customer \(OTP Bank Moldova\): confirmed; Investors vs registry \(SEVENTURE PARTNERS, SA à directoire, Tensor Co\-Investment Fund, Tensor Warehouse s\.r\.o\.\): confirmed | 7, 30, 31 |
| Timeline | Czech entity registered 2014\-12\-15; first press 2021\-12\-01 \(21 articles collected\) | 32, 33 |

# Detailed findings

## Ownership and capital

- Press‑reported funding: €3M round reported Jan 2025 naming Tensor Ventures, Elevator Ventures, J&amp;T Ventures\. *(Verified)* ^[4](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/)
  - Assumption: Press article accurately lists investors
- Series A reported \(\~€6\.8M\) led by Seventure Partners with Ariadnex founders and returning investors\. *(Verified)* ^[6](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html),[11](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/)
- Registry evidence of investors/shareholders: Tensor Co‑Investment Fund \(5\.44%\), Tensor Warehouse s\.r\.o\. \(6\.67%\), SEVENTURE PARTNERS entries \(2\.45% and 5\.71%\)\. *(Verified)* ^[14](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174),[34](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174),[15](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174),[16](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)

## Technology profile

- Product surfaces and docs: developer portal, downloadable Ignition Guide, deployment guides for Docker and REST APIs documented on developers\.wultra\.com\. *(Company claim)* ^[27](https://developers.wultra.com/),[35](https://www.wultra.com/downloads/ignition-guide-for-post-quantum-authentication),[29](https://developers.wultra.com/)
- Ship‑ready open components: multiple actively maintained public repos for PowerAuth, crypto, mobile SDKs and push/enrollment servers \(Apache/AGPL licenses\)\. *(Verified)* ^[1](https://github.com/wultra/powerauth-crypto),[2](https://github.com/wultra/powerauth-mobile-sdk),[36](https://github.com/wultra/powerauth-push-server),[37](https://github.com/wultra/digital-onboarding-apple)
- Engineering footprint: \~15 public repos with recent activity \(pushed 2026‑11‑16\), indicating active engineering outputs and reproducible SDKs\. *(Verified)* ^[25](https://github.com/wultra/mobile-utility-server),[26](https://github.com/wultra/react-native-powerauth-mobile-sdk),[38](https://github.com/wultra/powerauth-tests),[39](https://github.com/wultra/java-core),[24](https://github.com/wultra/mtoken-sdk-js)

## Rebuild check

- **Commodity:** SDKs, REST API and deployment guides — competent 2‑3 person team could reassemble an equivalent integration using public repos and Docker guidance\. *(Analyst view)* ^[2](https://github.com/wultra/powerauth-mobile-sdk),[1](https://github.com/wultra/powerauth-crypto),[27](https://developers.wultra.com/)
  - Assumption: Team uses existing Apache/AGPL codebases
- **Hard to copy:** Customer integrations, protocol maturity, a patent application for security tokens, and live bank/government deployments \(OTP Bank case study, Česká pošta contract\) are harder to reproduce quickly\. *(Analyst view)* ^[9](https://patents.google.com/patent/EM150508630001S),[7](https://cdn.prod.website-files.com/64fcce0d2e203c1c077a8c04/65c3aad8f10872792c8a7013_Wultra_CaseStudy_OTP_Bank.pdf),[8](https://smlouvy.gov.cz/smlouva/39855369)
  - Assumption: Integrations include non‑public operational glue
- **Verdict:** Quarter — a clone could be built in a quarter but would lack signed enterprise contracts, proven integrations and patent/legal protections\. *(Analyst view)* ^[1](https://github.com/wultra/powerauth-crypto),[7](https://cdn.prod.website-files.com/64fcce0d2e203c1c077a8c04/65c3aad8f10872792c8a7013_Wultra_CaseStudy_OTP_Bank.pdf),[9](https://patents.google.com/patent/EM150508630001S)
  - Assumption: Clone team has experienced security engineers

## Risks and caveats

- Unverified scale: press claims "70 clients across 25 countries" \(material to ARR and CAC\) lack registry or contract‑level corroboration in supplied facts\. *(Analyst view)* ^[10](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html),[6](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html)
  - Assumption: Press reflects company statements
- Open‑source exposure: core crypto and SDKs are public \(Apache/AGPL\), reducing technical exclusivity and making feature parity replicable from repos\. *(Analyst view)* ^[1](https://github.com/wultra/powerauth-crypto),[2](https://github.com/wultra/powerauth-mobile-sdk)
- Concentration risk: a small number of named large customers \(OTP Bank Moldova, Česká pošta contract\) imply potential customer concentration\. *(Analyst view)* ^[3](https://www.wultra.com/products/talisman-fido2-hardware-token),[8](https://smlouvy.gov.cz/smlouva/39855369)

## Questions for founders

- Provide top‑10 client list with contract start dates and ARR to validate the press claim of 70 clients and concentration risk\. *(Analyst view)* ^[10](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html)
- Share redacted enterprise contracts or reference letters for OTP Bank Moldova and Česká pošta to confirm deployment scope and SLAs\. *(Analyst view)* ^[7](https://cdn.prod.website-files.com/64fcce0d2e203c1c077a8c04/65c3aad8f10872792c8a7013_Wultra_CaseStudy_OTP_Bank.pdf),[8](https://smlouvy.gov.cz/smlouva/39855369)
- Clarify how the pending patent \(EM150508630001S\) maps to product claims and what is protected versus implemented in public repos\. *(Analyst view)* ^[9](https://patents.google.com/patent/EM150508630001S),[1](https://github.com/wultra/powerauth-crypto)
- Obtain ARR, gross margin and net retention metrics to validate per‑active‑user pricing assumptions and customer economics\. *(Analyst view)* ^[5](https://www.wultra.com/products/single-sign-on-sso),[40](https://www.wultra.com/products/mobile-first-authentication)

## Sources

1. [github\.com](https://github.com/wultra/powerauth-crypto) · Public technical artifact · GitHub repository · 2026\-11\-16 — “wultra/powerauth\-crypto · PowerAuth \- Open\-source solution for authentication, secure data storage and transport security in mobile banking\. · Java · last push 2026\-11\-16”
2. [github\.com](https://github.com/wultra/powerauth-mobile-sdk) · Public technical artifact · GitHub repository · 2026\-11\-16 — “wultra/powerauth\-mobile\-sdk · PowerAuth mobile SDK adds capability for authentication and transaction signing into the mobile apps \(iOS, tvOS, watchOS, Android\)\. · Java · last push 2026\-11\-16”
3. [wultra\.com](https://www.wultra.com/products/talisman-fido2-hardware-token) · Company's own website · Customer — “Case Study How OTP Bank Moldova Modernized Security &amp; UX for Corporate Customers OTP Bank SA \(Moldova\) undertook a strategic security upgrade to modernize transaction authentication for its corporate customers byreplacing its legacy hardware tokens with Talisman\.”
4. [tech\.eu](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/) · Independent press · Funding round — “Wultra has raised €3M from Tensor Ventures, Elevator Ventures, and J&amp;T Ventures to accelerate the development of post\-quantum authentication technology\.”
5. [wultra\.com](https://www.wultra.com/products/single-sign-on-sso) · Company's own website · Pricing — “Only pay for active users”
6. [finance\.yahoo\.com](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html) · Independent press · Funding round — “backed by lead investor Seventure Partners, followed by ARIADNEXT founders Marc Norlain and Guillaume Despagne and existing investors J&amp;T Ventures and Elevator Ventures \.”
7. [cdn\.prod\.website\-files\.com](https://cdn.prod.website-files.com/64fcce0d2e203c1c077a8c04/65c3aad8f10872792c8a7013_Wultra_CaseStudy_OTP_Bank.pdf) · Independent press · Independent check of a claim — “The following case study explores the successful outcomes of Wultra’s collaboration with OTP Bank\. Read on to learn why PSD2 compliance in the Moldovan market is more crucial than ever before, and additionally, how Wultra implemented a secure, compliant authentication solution into OTP Bank’s mobile”
8. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/39855369) · Official record · Public contract · 2026\-09\-24 — “Česká pošta, s\.p\. · 0 CZK · Smlouva o budoucí spolupráci”
9. [patents\.google\.com](https://patents.google.com/patent/EM150508630001S) · Official record · Patent publication — “EM150508630001S · Security tokens \[encryption devices\] · Wultra s\.r\.o\.”
10. [finance\.yahoo\.com](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html) · Independent press · Customer — “now support more than 70 clients across 25 countries worldwide,”
11. [lupa\.cz](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/) · Independent press · Funding round — “Prostředky v rámci investičního kola series A jako vedoucí investor poskytl fond Seventure Partners\.”
12. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Registry: shareholder · 2021\-11\-26 — “J&amp;T Ventures CG SICAV a\.s\. · 15\.0% · from 2021\-11\-26 · to 2022\-01\-01”
13. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Registry: shareholder · 2022\-01\-01 — “J&amp;T Ventures CG SICAV a\.s\. · 17\.68% · from 2022\-01\-01”
14. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Registry: shareholder · 2025\-12\-03 — “Tensor Co\-Investment Fund · 5\.44% · from 2025\-12\-03”
15. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Registry: shareholder · 2026\-06\-22 — “SEVENTURE PARTNERS, SA à directoire · 5\.71% · from 2026\-06\-22”
16. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Registry: shareholder · 2026\-06\-22 — “SEVENTURE PARTNERS, SA à directoire · 2\.45% · from 2026\-06\-22”
17. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/Covid-66F2A0C9D621A3DF40E30EB3EFC81EEB29372C85044499F21CD2EB2B0EE51FC4) · Official record · National grant · 2021 — “ANTIVIRUS · Úřad práce České republiky”
18. [wultra\.com](https://www.wultra.com/careers) · Company's own website · Job posting — “Chief Product Officer”
19. [wultra\.com](https://www.wultra.com/careers) · Company's own website · Job posting — “Chief People &amp; Culture Officer”
20. [wultra\.com](https://www.wultra.com/careers) · Company's own website · Job posting — “Security Tester”
21. [wultra\.com](https://www.wultra.com/careers) · Company's own website · Job posting — “Mobile Application Protection Product Manager”
22. [wultra\.com](https://www.wultra.com/careers) · Company's own website · Job posting — “Talent Acquisition Specialist / Recruiter”
23. [wultra\.com](https://www.wultra.com/careers) · Company's own website · Job posting — “People Operations Generalist”
24. [github\.com](https://github.com/wultra/mtoken-sdk-js) · Public technical artifact · GitHub repository · 2026\-11\-13 — “wultra/mtoken\-sdk\-js · PowerAuth based Mobile Token SDK for Javascript mobile platforms · TypeScript · last push 2026\-11\-13”
25. [github\.com](https://github.com/wultra/mobile-utility-server) · Public technical artifact · GitHub repository · 2026\-11\-16 — “wultra/mobile\-utility\-server · Utility server with various features suitable for mobile apps · Java · last push 2026\-11\-16”
26. [github\.com](https://github.com/wultra/react-native-powerauth-mobile-sdk) · Public technical artifact · GitHub repository · 2026\-11\-16 — “wultra/react\-native\-powerauth\-mobile\-sdk · JavaScript Mobile SDK for PowerAuth Protocol \(React Native, Cordova / iOS, Android\) · TypeScript · last push 2026\-11\-16”
27. [developers\.wultra\.com](https://developers.wultra.com/) · Company's own website · Website page — “Wultra Developer Portal”
28. [wultra\.com](https://www.wultra.com/brand-guidelines) · Company's own website · Website page — “Brand Guidelines │ Wultra”
29. [developers\.wultra\.com](https://developers.wultra.com/) · Company's own website · Pricing — “Follow our step\-by\-step guidebooks to deploy our Docker images, connect to our RESTful APIs, and integrate authentication SDK in your apps\.”
30. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Independent check of a claim · 2024\-12\-30 — “Press \(tech\.eu\) names Tensor Ventures as an investor; the commercial register lists Tensor Warehouse s\.r\.o\. as a shareholder from 2024\-12\-30 \(6\.67%\)\.”
31. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Independent check of a claim · 2025\-12\-03 — “Press \(tech\.eu\) names Tensor Ventures as an investor; the commercial register lists Tensor Co\-Investment Fund as a shareholder from 2025\-12\-03 \(5\.44%\)\.”
32. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/03643174) · Official record · Registry: incorporation · 2014\-12\-15 — “registered 2014\-12\-15”
33. [lupa\.cz](https://www.lupa.cz/aktuality/petr-dvorak-do-firmy-wultra-pustil-investory-j-t-za-desitky-milionu-ziskava-minoritu/) · Independent press · Press article · 2021\-12\-01 — “Petr Dvořák do firmy Wultra pustil investory, J&amp;T za desítky milionů získává minoritu \- Lupa\.cz”
34. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Registry: shareholder · 2024\-12\-30 — “Tensor Warehouse s\.r\.o\. · 6\.67% · from 2024\-12\-30 · to 2025\-12\-03”
35. [wultra\.com](https://www.wultra.com/downloads/ignition-guide-for-post-quantum-authentication) · Company's own website · Website page — “Ignition Guide – Ignition Guide: How to Switch to Post\-Quantum Authentication \| Wultra Downloads”
36. [github\.com](https://github.com/wultra/powerauth-push-server) · Public technical artifact · GitHub repository · 2026\-11\-16 — “wultra/powerauth\-push\-server · PowerAuth Push Server repository · Java · last push 2026\-11\-16”
37. [github\.com](https://github.com/wultra/digital-onboarding-apple) · Public technical artifact · GitHub repository · 2026\-11\-16 — “wultra/digital\-onboarding\-apple · Wultra Digital Onboarding for Apple platforms · Swift · last push 2026\-11\-16”
38. [github\.com](https://github.com/wultra/powerauth-tests) · Public technical artifact · GitHub repository · 2026\-11\-16 — “wultra/powerauth\-tests · Tests for PowerAuth backend services · Java · last push 2026\-11\-16”
39. [github\.com](https://github.com/wultra/java-core) · Public technical artifact · GitHub repository · 2026\-11\-16 — “wultra/java\-core · Core Java classes shared across our projects · Java · last push 2026\-11\-16”
40. [wultra\.com](https://www.wultra.com/products/mobile-first-authentication) · Company's own website · Pricing — “Only pay for active users”
41. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174) · Official record · Independent check of a claim · 2026\-06\-22 — “Press \(finance\.yahoo\.com, lupa\.cz\) names Seventure Partners as an investor; the commercial register lists SEVENTURE PARTNERS, SA à directoire as a shareholder from 2026\-06\-22 \(2\.45%\)\.”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 63 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 2 | starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 21 | press:globenewswire\.com, press:medium\.com, press:securityweek\.com |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 47 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 11 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 16 | — |
| Mobile apps | App Store \(seller must match the company\), Google Play if linked from the site | 1 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 4 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 5 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 83 | — |

Analysis: gpt\-5\-mini (cost $0.0111); AI extraction cost $0.0086. Full fact table: CSV export.

## Source appendix (all collected facts)

- F4471 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/03643174)
- F4472 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/03643174)
- F4473 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4474 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4475 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4476 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4477 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4478 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4479 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4480 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4481 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4482 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4483 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4484 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4485 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4486 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4487 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4488 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4489 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4490 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F4491 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4492 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4493 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4494 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4495 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4496 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4497 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4498 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4499 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4500 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4501 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4502 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4503 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4504 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4505 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4506 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4507 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4508 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4509 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4510 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4511 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4512 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4513 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4514 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4515 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4516 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4517 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4518 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4519 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4520 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4521 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4522 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4523 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4524 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4525 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4526 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4527 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4528 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4529 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4530 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4531 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4532 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=883583](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=883583)
- F4533 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=03643174&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=03643174&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F4534 · web\_page · Sourced · [https://www\.wultra\.com/](https://www.wultra.com/)
- F4535 · web\_page · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4536 · web\_page · Sourced · [https://www\.wultra\.com/privacy\-policy](https://www.wultra.com/privacy-policy)
- F4537 · web\_page · Sourced · [https://www\.wultra\.com/cookies\-policy](https://www.wultra.com/cookies-policy)
- F4538 · subprocessor · Medium confidence · [https://www\.wultra\.com/cookies\-policy](https://www.wultra.com/cookies-policy)
- F4539 · subprocessor · Medium confidence · [https://www\.wultra\.com/cookies\-policy](https://www.wultra.com/cookies-policy)
- F4540 · web\_page · Sourced · [https://www\.wultra\.com/recruitment\-privacy\-policy](https://www.wultra.com/recruitment-privacy-policy)
- F4541 · web\_page · Sourced · [https://www\.wultra\.com/career/devops\-engineer](https://www.wultra.com/career/devops-engineer)
- F4542 · web\_page · Sourced · [https://www\.wultra\.com/career/business\-development\-representative\-\-\-french\-arabic\-speaking](https://www.wultra.com/career/business-development-representative---french-arabic-speaking)
- F4543 · web\_page · Sourced · [https://www\.wultra\.com/career/business\-development\-representative\-\-\-german\-spanish\-speaking](https://www.wultra.com/career/business-development-representative---german-spanish-speaking)
- F4544 · web\_page · Sourced · [https://www\.wultra\.com/career/chief\-people\-culture\-officer](https://www.wultra.com/career/chief-people-culture-officer)
- F4545 · web\_page · Sourced · [https://www\.wultra\.com/career/chief\-product\-officer](https://www.wultra.com/career/chief-product-officer)
- F4546 · web\_page · Sourced · [https://www\.wultra\.com/career/it\-systems\-administrator](https://www.wultra.com/career/it-systems-administrator)
- F4547 · web\_page · Sourced · [https://www\.wultra\.com/career/java\-developer](https://www.wultra.com/career/java-developer)
- F4548 · web\_page · Sourced · [https://www\.wultra\.com/career/legal\-regulatory\-counsel](https://www.wultra.com/career/legal-regulatory-counsel)
- F4549 · web\_page · Sourced · [https://www\.wultra\.com/career/mobile\-reverse\-engineer\-\-\-android](https://www.wultra.com/career/mobile-reverse-engineer---android)
- F4550 · web\_page · Sourced · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F4551 · web\_page · Sourced · [https://www\.wultra\.com/compliance](https://www.wultra.com/compliance)
- F4552 · web\_page · Sourced · [https://www\.wultra\.com/brand\-guidelines](https://www.wultra.com/brand-guidelines)
- F4553 · web\_page · Sourced · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F4554 · web\_page · Sourced · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F4555 · web\_page · Sourced · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F4556 · web\_page · Sourced · [https://www\.wultra\.com/products/talisman\-fido2\-hardware\-token](https://www.wultra.com/products/talisman-fido2-hardware-token)
- F4557 · web\_page · Sourced · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F4558 · web\_page · Sourced · [https://www\.wultra\.com/products/digital\-identity\-wallet\-gateway](https://www.wultra.com/products/digital-identity-wallet-gateway)
- F4559 · web\_page · Sourced · [https://www\.wultra\.com/webinars/fraud\-compliance\-and\-the\-future\-of\-digital\-banking\-in\-asean\-how\-banks\-can\-stay\-ahead](https://www.wultra.com/webinars/fraud-compliance-and-the-future-of-digital-banking-in-asean-how-banks-can-stay-ahead)
- F4560 · web\_page · Sourced · [https://www\.wultra\.com/webinars/beyond\-otp\-how\-philippine\-banks\-can\-achieve\-quantum\-safe\-compliance\-today](https://www.wultra.com/webinars/beyond-otp-how-philippine-banks-can-achieve-quantum-safe-compliance-today)
- F4561 · web\_page · Sourced · [https://www\.wultra\.com/downloads/ignition\-guide\-for\-post\-quantum\-authentication](https://www.wultra.com/downloads/ignition-guide-for-post-quantum-authentication)
- F4562 · web\_page · Sourced · [https://www\.wultra\.com/case\-studies](https://www.wultra.com/case-studies)
- F4563 · web\_page · Sourced · [https://www\.wultra\.com/about\-us](https://www.wultra.com/about-us)
- F4564 · web\_page · Sourced · [https://www\.wultra\.com/product\-updates](https://www.wultra.com/product-updates)
- F4565 · web\_page · Sourced · [https://www\.wultra\.com/case\-studies/albanian\-post\-and\-helius\-systems\-make\-payments\-easier\-with\-their\-innovative\-fintech\-app\-protected\-by\-wultra\-authentication](https://www.wultra.com/case-studies/albanian-post-and-helius-systems-make-payments-easier-with-their-innovative-fintech-app-protected-by-wultra-authentication)
- F4566 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4567 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4568 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4569 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4570 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4571 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4572 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4573 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4574 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4575 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4576 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4577 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4578 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4579 · job\_post · Sourced · [https://www\.wultra\.com/careers](https://www.wultra.com/careers)
- F4580 · github\_org · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F4581 · tech\_stack · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F4582 · tech\_stack · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F4583 · tech\_stack · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F4584 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=wultra\.com&amp;type=MX](https://dns.google/resolve?name=wultra.com&type=MX)
- F4585 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=wultra\.com&amp;type=TXT](https://dns.google/resolve?name=wultra.com&type=TXT)
- F4586 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=wultra\.com&amp;type=TXT](https://dns.google/resolve?name=wultra.com&type=TXT)
- F4587 · subdomain · Sourced · [https://crt\.sh/?q=%25\.wultra\.com&amp;output=json](https://crt.sh/?q=%25.wultra.com&output=json)
- F4588 · subdomain · Sourced · [https://crt\.sh/?q=%25\.wultra\.com&amp;output=json](https://crt.sh/?q=%25.wultra.com&output=json)
- F4589 · subdomain · Sourced · [https://crt\.sh/?q=%25\.wultra\.com&amp;output=json](https://crt.sh/?q=%25.wultra.com&output=json)
- F4590 · subdomain · Sourced · [https://crt\.sh/?q=%25\.wultra\.com&amp;output=json](https://crt.sh/?q=%25.wultra.com&output=json)
- F4591 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.wultra\.com&amp;output=json](https://crt.sh/?q=%25.wultra.com&output=json)
- F4592 · github\_org · Sourced · [https://github\.com/wultra](https://github.com/wultra)
- F4593 · repo · Sourced · [https://github\.com/wultra/mobile\-utility\-server](https://github.com/wultra/mobile-utility-server)
- F4594 · repo · Sourced · [https://github\.com/wultra/react\-native\-powerauth\-mobile\-sdk](https://github.com/wultra/react-native-powerauth-mobile-sdk)
- F4595 · repo · Sourced · [https://github\.com/wultra/powerauth\-tests](https://github.com/wultra/powerauth-tests)
- F4596 · repo · Sourced · [https://github\.com/wultra/java\-core](https://github.com/wultra/java-core)
- F4597 · repo · Sourced · [https://github\.com/wultra/networking\-apple](https://github.com/wultra/networking-apple)
- F4598 · repo · Sourced · [https://github\.com/wultra/networking\-android](https://github.com/wultra/networking-android)
- F4599 · repo · Sourced · [https://github\.com/wultra/digital\-onboarding\-apple](https://github.com/wultra/digital-onboarding-apple)
- F4600 · repo · Sourced · [https://github\.com/wultra/mtoken\-sdk\-ios](https://github.com/wultra/mtoken-sdk-ios)
- F4601 · repo · Sourced · [https://github\.com/wultra/digital\-onboarding\-android](https://github.com/wultra/digital-onboarding-android)
- F4602 · repo · Sourced · [https://github\.com/wultra/mtoken\-sdk\-android](https://github.com/wultra/mtoken-sdk-android)
- F4603 · repo · Sourced · [https://github\.com/wultra/powerauth\-mobile\-sdk](https://github.com/wultra/powerauth-mobile-sdk)
- F4604 · repo · Sourced · [https://github\.com/wultra/powerauth\-crypto](https://github.com/wultra/powerauth-crypto)
- F4605 · repo · Sourced · [https://github\.com/wultra/enrollment\-server](https://github.com/wultra/enrollment-server)
- F4606 · repo · Sourced · [https://github\.com/wultra/powerauth\-push\-server](https://github.com/wultra/powerauth-push-server)
- F4607 · repo · Sourced · [https://github\.com/wultra/mtoken\-sdk\-js](https://github.com/wultra/mtoken-sdk-js)
- F4608 · app · Medium confidence · [https://www\.wultra\.com/case\-studies/albanian\-post\-and\-helius\-systems\-make\-payments\-easier\-with\-their\-innovative\-fintech\-app\-protected\-by\-wultra\-authentication](https://www.wultra.com/case-studies/albanian-post-and-helius-systems-make-payments-easier-with-their-innovative-fintech-app-protected-by-wultra-authentication)
- F4609 · wayback\_first · Sourced · [https://web\.archive\.org/web/20130530081513/http://wultra\.com](https://web.archive.org/web/20130530081513/http://wultra.com)
- F4610 · wayback\_first · Sourced · [https://web\.archive\.org/web/20210819122519/https://www\.wultra\.com/careers](https://web.archive.org/web/20210819122519/https://www.wultra.com/careers)
- F4611 · wayback\_first · Sourced · [https://web\.archive\.org/web/20200918225419/https://www\.wultra\.com/blog](https://web.archive.org/web/20200918225419/https://www.wultra.com/blog)
- F4612 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/wultra\.com](https://web.archive.org/web/%2A/wultra.com)
- F4618 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4619 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4620 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4621 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4622 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4623 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4624 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4625 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4626 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4627 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4628 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4629 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4630 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4631 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4632 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4633 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4634 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4635 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4636 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4637 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4638 · press\_mention · Sourced · [https://tech\.eu/2025/01/15/wultra\-secures\-eur3m\-to\-protect\-financial\-institutions\-from\-quantum\-threats/](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/)
- F4639 · press\_mention · Sourced · [https://finance\.yahoo\.com/technology/ai/articles/wultra\-raises\-6\-8\-million\-140000790\.html](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html)
- F4640 · press\_mention · Sourced · [https://finance\.yahoo\.com/news/wultra\-secures\-3m\-protect\-financial\-104000919\.html](https://finance.yahoo.com/news/wultra-secures-3m-protect-financial-104000919.html)
- F4641 · press\_mention · Sourced · [https://blog\.tensor\.ventures/p/wultra\-raises\-68m\-to\-make\-finance](https://blog.tensor.ventures/p/wultra-raises-68m-to-make-finance)
- F4642 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/ceska\-firma\-wultra\-vybrala\-dalsich\-160\-milionu\-na\-nasazeni\-postkvantoveho\-sifrovani/](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/)
- F4643 · press\_mention · Sourced · [https://www\.havelpartners\.cz/pravni\-poradenstvi\-pro\-investory\-pri\-vstupu\-do\-startupu\-wultra/](https://www.havelpartners.cz/pravni-poradenstvi-pro-investory-pri-vstupu-do-startupu-wultra/)
- F4644 · press\_mention · Sourced · [https://www\.jtbank\.cz/clanky/insight/j3i63nc9ev\-fond\-j\-t\-ventures\-investoval\-do\-startupu\-wultra](https://www.jtbank.cz/clanky/insight/j3i63nc9ev-fond-j-t-ventures-investoval-do-startupu-wultra)
- F4645 · press\_mention · Sourced · [https://quantumcomputingreport\.com/wultra\-secures\-e6\-8\-million\-7\-7\-million\-usd\-series\-a\-to\-expand\-post\-quantum\-digital\-identity\-infrastructure\-globally/](https://quantumcomputingreport.com/wultra-secures-e6-8-million-7-7-million-usd-series-a-to-expand-post-quantum-digital-identity-infrastructure-globally/)
- F4646 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/petr\-dvorak\-do\-firmy\-wultra\-pustil\-investory\-j\-t\-za\-desitky\-milionu\-ziskava\-minoritu/](https://www.lupa.cz/aktuality/petr-dvorak-do-firmy-wultra-pustil-investory-j-t-za-desitky-milionu-ziskava-minoritu/)
- F4647 · press\_mention · Sourced · [https://vestbee\.com/insights/articles/wultra\-raises\-6\-8\-m](https://vestbee.com/insights/articles/wultra-raises-6-8-m)
- F4648 · press\_mention · Sourced · [https://www\.prnewswire\.com/news\-releases/wultra\-raises\-6\-8\-million\-in\-series\-a\-funding\-to\-accelerate\-global\-expansion\-of\-post\-quantum\-digital\-identity\-solutions\-302813435\.html](https://www.prnewswire.com/news-releases/wultra-raises-6-8-million-in-series-a-funding-to-accelerate-global-expansion-of-post-quantum-digital-identity-solutions-302813435.html)
- F4649 · press\_mention · Sourced · [https://aipressroom\.com/wultra\-6m\-post\-quantum](https://aipressroom.com/wultra-6m-post-quantum)
- F4650 · press\_mention · Sourced · [https://www\.startup\.eu/investments/wultra\-6\-8\-m\-series\-a\-06\-2026](https://www.startup.eu/investments/wultra-6-8-m-series-a-06-2026)
- F4651 · press\_mention · Sourced · [https://fintech\.global/2026/06/29/post\-quantum\-auth\-firm\-wultra\-raises\-e6\-8m/](https://fintech.global/2026/06/29/post-quantum-auth-firm-wultra-raises-e6-8m/)
- F4652 · press\_mention · Sourced · [https://financialit\.net/news/fundraising\-news/wultra\-raises\-eu68\-million\-series\-funding](https://financialit.net/news/fundraising-news/wultra-raises-eu68-million-series-funding)
- F4653 · press\_mention · Sourced · [https://cfotech\.news/story/wultra\-raises\-eur\-6\-8m\-in\-series\-a\-led\-by\-seventure](https://cfotech.news/story/wultra-raises-eur-6-8m-in-series-a-led-by-seventure)
- F4654 · press\_mention · Sourced · [https://cfotech\.co\.uk/story/wultra\-raises\-eur\-6\-8m\-in\-series\-a\-led\-by\-seventure](https://cfotech.co.uk/story/wultra-raises-eur-6-8m-in-series-a-led-by-seventure)
- F4655 · source\_unavailable · Unavailable · [https://www\.securityweek\.com/wultra\-raises\-e3\-million\-for\-post\-quantum\-authentication](https://www.securityweek.com/wultra-raises-e3-million-for-post-quantum-authentication)
- F4656 · press\_mention · Sourced · [https://finance\.yahoo\.com/technology/ai/articles/wultra\-raises\-6\-8\-million\-130000062\.html](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-130000062.html)
- F4657 · press\_mention · Sourced · [https://fintech\.global/2025/01/15/czech\-cybersecurity\-startup\-wultra\-raises\-e3m\-to\-combat\-quantum\-threats/](https://fintech.global/2025/01/15/czech-cybersecurity-startup-wultra-raises-e3m-to-combat-quantum-threats/)
- F4658 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/dvorakova\-wultra\-nabrala\-kapital\-na\-nahradu\-mobilu\-pro\-prihlasovani\-k\-aplikacim\-a\-na\-postkvantove\-sifrovani/](https://www.lupa.cz/aktuality/dvorakova-wultra-nabrala-kapital-na-nahradu-mobilu-pro-prihlasovani-k-aplikacim-a-na-postkvantove-sifrovani/)
- F4659 · source\_unavailable · Unavailable · [https://medium\.com/wultra\-blog/wultra\-turned\-from\-a\-bootstrapped\-company\-to\-a\-venture\-backed\-company\-in\-2022\-b58f721ca0d6](https://medium.com/wultra-blog/wultra-turned-from-a-bootstrapped-company-to-a-venture-backed-company-in-2022-b58f721ca0d6)
- F4660 · source\_unavailable · Unavailable · [https://www\.globenewswire\.com/news\-release/2025/01/15/3009819/0/en/Wultra\-Secures\-3M\-to\-Protect\-Financial\-Institutions\-from\-Quantum\-Threats\.html](https://www.globenewswire.com/news-release/2025/01/15/3009819/0/en/Wultra-Secures-3M-to-Protect-Financial-Institutions-from-Quantum-Threats.html)
- F4661 · press\_mention · Sourced · [https://www\.therecursive\.com/czech\-wultra\-raises\-eur6\-8m\-series\-a\-to\-expand\-post\-quantum\-digital\-identity\-platform](https://www.therecursive.com/czech-wultra-raises-eur6-8m-series-a-to-expand-post-quantum-digital-identity-platform)
- F4662 · source\_unavailable · Unavailable · [https://medium\.com/wultra\-blog](https://medium.com/wultra-blog)
- F5546 · gov\_contract · Sourced · [https://smlouvy\.gov\.cz/smlouva/39855369](https://smlouvy.gov.cz/smlouva/39855369)
- F5547 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/Covid\-66F2A0C9D621A3DF40E30EB3EFC81EEB29372C85044499F21CD2EB2B0EE51FC4](https://www.hlidacstatu.cz/Dotace/Detail/Covid-66F2A0C9D621A3DF40E30EB3EFC81EEB29372C85044499F21CD2EB2B0EE51FC4)
- F5548 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Wultra%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Wultra%27)
- F5549 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F6260 · product\_capability · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6261 · product\_capability · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6262 · product\_capability · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6263 · product\_capability · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6264 · integration · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6265 · product\_capability · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6266 · product\_capability · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6267 · product\_capability · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6268 · tech\_claim · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6269 · tech\_claim · Medium confidence · [https://www\.wultra\.com/](https://www.wultra.com/)
- F6270 · product\_capability · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6271 · integration · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6272 · product\_capability · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6273 · product\_capability · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6274 · product\_capability · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6275 · product\_capability · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6276 · product\_capability · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6277 · tech\_claim · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6278 · pricing · Medium confidence · [https://developers\.wultra\.com/](https://developers.wultra.com/)
- F6279 · product\_capability · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6280 · product\_capability · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6281 · product\_capability · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6282 · product\_capability · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6283 · product\_capability · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6284 · product\_capability · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6285 · product\_capability · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6286 · product\_capability · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6287 · tech\_claim · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6288 · pricing · Medium confidence · [https://www\.wultra\.com/products](https://www.wultra.com/products)
- F6289 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6290 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6291 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6292 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6293 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6294 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6295 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6296 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6297 · tech\_claim · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6298 · pricing · Medium confidence · [https://www\.wultra\.com/products/single\-sign\-on\-sso](https://www.wultra.com/products/single-sign-on-sso)
- F6299 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6300 · tech\_claim · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6301 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6302 · integration · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6303 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6304 · pricing · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6305 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6306 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6307 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/mobile\-first\-authentication](https://www.wultra.com/products/mobile-first-authentication)
- F6308 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/talisman\-fido2\-hardware\-token](https://www.wultra.com/products/talisman-fido2-hardware-token)
- F6310 · tech\_claim · Medium confidence · [https://www\.wultra\.com/products/talisman\-fido2\-hardware\-token](https://www.wultra.com/products/talisman-fido2-hardware-token)
- F6311 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/talisman\-fido2\-hardware\-token](https://www.wultra.com/products/talisman-fido2-hardware-token)
- F6312 · pricing · Medium confidence · [https://www\.wultra\.com/products/talisman\-fido2\-hardware\-token](https://www.wultra.com/products/talisman-fido2-hardware-token)
- F6313 · customer · Medium confidence · [https://www\.wultra\.com/products/talisman\-fido2\-hardware\-token](https://www.wultra.com/products/talisman-fido2-hardware-token)
- F6314 · funding\_round · Medium confidence · [https://tech\.eu/2025/01/15/wultra\-secures\-eur3m\-to\-protect\-financial\-institutions\-from\-quantum\-threats/](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/)
- F6315 · product\_capability · Medium confidence · [https://tech\.eu/2025/01/15/wultra\-secures\-eur3m\-to\-protect\-financial\-institutions\-from\-quantum\-threats/](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/)
- F6316 · product\_capability · Medium confidence · [https://tech\.eu/2025/01/15/wultra\-secures\-eur3m\-to\-protect\-financial\-institutions\-from\-quantum\-threats/](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/)
- F6317 · tech\_claim · Medium confidence · [https://tech\.eu/2025/01/15/wultra\-secures\-eur3m\-to\-protect\-financial\-institutions\-from\-quantum\-threats/](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/)
- F6318 · customer · Medium confidence · [https://tech\.eu/2025/01/15/wultra\-secures\-eur3m\-to\-protect\-financial\-institutions\-from\-quantum\-threats/](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/)
- F6319 · tech\_claim · Medium confidence · [https://tech\.eu/2025/01/15/wultra\-secures\-eur3m\-to\-protect\-financial\-institutions\-from\-quantum\-threats/](https://tech.eu/2025/01/15/wultra-secures-eur3m-to-protect-financial-institutions-from-quantum-threats/)
- F6320 · funding\_round · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/wultra\-raises\-6\-8\-million\-140000790\.html](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html)
- F6322 · product\_capability · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/wultra\-raises\-6\-8\-million\-140000790\.html](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html)
- F6324 · team\_claim · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/wultra\-raises\-6\-8\-million\-140000790\.html](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html)
- F6325 · customer · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/wultra\-raises\-6\-8\-million\-140000790\.html](https://finance.yahoo.com/technology/ai/articles/wultra-raises-6-8-million-140000790.html)
- F6326 · product\_capability · Medium confidence · [https://finance\.yahoo\.com/news/wultra\-secures\-3m\-protect\-financial\-104000919\.html](https://finance.yahoo.com/news/wultra-secures-3m-protect-financial-104000919.html)
- F6327 · product\_capability · Medium confidence · [https://finance\.yahoo\.com/news/wultra\-secures\-3m\-protect\-financial\-104000919\.html](https://finance.yahoo.com/news/wultra-secures-3m-protect-financial-104000919.html)
- F6328 · tech\_claim · Medium confidence · [https://finance\.yahoo\.com/news/wultra\-secures\-3m\-protect\-financial\-104000919\.html](https://finance.yahoo.com/news/wultra-secures-3m-protect-financial-104000919.html)
- F6329 · tech\_claim · Medium confidence · [https://finance\.yahoo\.com/news/wultra\-secures\-3m\-protect\-financial\-104000919\.html](https://finance.yahoo.com/news/wultra-secures-3m-protect-financial-104000919.html)
- F6330 · tech\_claim · Medium confidence · [https://finance\.yahoo\.com/news/wultra\-secures\-3m\-protect\-financial\-104000919\.html](https://finance.yahoo.com/news/wultra-secures-3m-protect-financial-104000919.html)
- F6331 · tech\_claim · Medium confidence · [https://finance\.yahoo\.com/news/wultra\-secures\-3m\-protect\-financial\-104000919\.html](https://finance.yahoo.com/news/wultra-secures-3m-protect-financial-104000919.html)
- F6332 · tech\_claim · Medium confidence · [https://blog\.tensor\.ventures/p/wultra\-raises\-68m\-to\-make\-finance](https://blog.tensor.ventures/p/wultra-raises-68m-to-make-finance)
- F6333 · funding\_round · Medium confidence · [https://www\.lupa\.cz/aktuality/ceska\-firma\-wultra\-vybrala\-dalsich\-160\-milionu\-na\-nasazeni\-postkvantoveho\-sifrovani/](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/)
- F6334 · product\_capability · Medium confidence · [https://www\.lupa\.cz/aktuality/ceska\-firma\-wultra\-vybrala\-dalsich\-160\-milionu\-na\-nasazeni\-postkvantoveho\-sifrovani/](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/)
- F6335 · product\_capability · Medium confidence · [https://www\.lupa\.cz/aktuality/ceska\-firma\-wultra\-vybrala\-dalsich\-160\-milionu\-na\-nasazeni\-postkvantoveho\-sifrovani/](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/)
- F6336 · tech\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/ceska\-firma\-wultra\-vybrala\-dalsich\-160\-milionu\-na\-nasazeni\-postkvantoveho\-sifrovani/](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/)
- F6337 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6338 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6339 · integration · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6340 · tech\_claim · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6341 · pricing · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6342 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6343 · product\_capability · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6344 · tech\_claim · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6345 · tech\_claim · Medium confidence · [https://www\.wultra\.com/products/passkeys\-and\-fido2](https://www.wultra.com/products/passkeys-and-fido2)
- F6399 · patent · Sourced · [https://patents\.google\.com/patent/EM150508630001S](https://patents.google.com/patent/EM150508630001S)
- F6400 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F6401 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F6402 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/03643174](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03643174)
- F6404 · verification · Sourced · [https://cdn\.prod\.website\-files\.com/64fcce0d2e203c1c077a8c04/65c3aad8f10872792c8a7013\_Wultra\_CaseStudy\_OTP\_Bank\.pdf](https://cdn.prod.website-files.com/64fcce0d2e203c1c077a8c04/65c3aad8f10872792c8a7013_Wultra_CaseStudy_OTP_Bank.pdf)
