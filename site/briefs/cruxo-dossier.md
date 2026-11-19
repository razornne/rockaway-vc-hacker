# Cruxo — due diligence brief

cruxo\.io · CRUXO group s\.r\.o\. · IČO 14134683 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A retail‑media SaaS for retailers and brands to plan, serve and analyze on‑site and off‑site e‑commerce ads\. *(Company claim)* ^[1](https://cruxo.io/),[2](https://cruxo.io/),[3](https://cruxo.io/),[4](https://cruxo.io/advertisers/),[5](https://cruxo.io/advertisers/)
- **Stage & traction.** Multiple press‑reported funding rounds \(20M \+ 15M CZK total\), confirmed VC shareholders, national grants and named customers \(Dr\.Max, Lékárna\.cz\)\. *(Verified)* ^[6](https://www.mediaguru.cz/clanky/2023/05/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc/),[7](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/),[8](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/),[9](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683),[10](https://cruxo.io/)
- **Technology & moat.** Company claims a proprietary data‑insights framework; evidence is currently company statements rather than independently verified IP or published models\. *(Partly verified)* ^[11](https://cruxo.io/about/),[12](https://cruxo.io/about/),[13](https://github.com/cruxoio/status)
- **Key risk.** Several technical and compliance claims \(IAB TCF listing, enterprise ad‑serving scale\) are unverified or not found in verification checks\. *(Analyst view)* ^[14](https://vendor-list.consensu.org/v3/vendor-list.json),[15](https://cruxo.io/retailers/)
- **Diligence focus.** First verify ad‑server scale &amp; latency SLAs and IAB TCF vendor status, then corroborate monthly revenue and multi‑country customer depth\. *(Analyst view)* ^[15](https://cruxo.io/retailers/),[14](https://vendor-list.consensu.org/v3/vendor-list.json),[16](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2023\-05\-03 · not specified · 20 milionů Kč · Czech Founders, Presto Ventures, Zaka · 4 reports; 2024\-11\-11 · 20 million CZK \(first round\) \+ 15 million CZK \(second round\) · Presto Ventures, Zaka VC, Czech Founders VC, Rockaway Ventures, angel investors; 2025\-01\-31 · CZK 15 Million · Czech Founders VC, Rockaway Ventures, angel investors | 6, 17, 18, 19, 7, 8 |
| Investors in registry | Czech Founders Ventures s\.r\.o\., osoba rizikového kapitálu \(from 2026\-08\-24, 10\.77%\); Presto Ventures II a\.s\., osoba rizikového kapitálu \(from 2026\-08\-24, 7\.69%\); Rockaway Ventures Fund SCSp \(from 2026\-08\-24, 3\.85%\) | 9, 20, 21 |
| Public money | 3 grant\(s\), 5\.8M CZK | 22, 23, 24 |
| Engineering footprint | 1 public repos \(0★, last push 2025\-01\-16\); product surfaces: admin\.dev\.cruxo\.io, app\.dev\.cruxo\.io, app\.stage\.cruxo\.io, docs\.tool\.cruxo\.io | 13, 25, 26, 27 |
| Customers | 2 named: Dr\.Max, Lekarna\.cz; public pricing: yes | 10, 28, 29 |
| Claims checked | Customer \(Dr\.Max, Lekarna\.cz\): confirmed; Investors vs registry \(Czech Founders Ventures s\.r\.o\., osoba rizikového kapitálu, Presto Ventures II a\.s\., osoba rizikového kapitálu, Rockaway Ventures Fund SCSp, ZAKA Startup 18 j\. s\. a\.\): confirmed; IAB TCF: not found | 30, 31, 32, 33, 14 |
| Timeline | Czech entity registered 2022\-01\-10; first press 2023\-04\-18 \(18 articles collected\) | 34, 35 |

# Detailed findings

## Ownership and capital

- Press reports: \~20M CZK disclosed funding \(May 2023\) and subsequent \~15M CZK round reported; investors named include Czech Founders, Presto, Zaka, Rockaway and angels\. *(Verified)* ^[6](https://www.mediaguru.cz/clanky/2023/05/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc/),[7](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/),[8](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/)
  - Assumption: Press sums represent announced amounts, not legal close documents\.
- Registry shareholders \(commercial register filings\) confirm Czech Founders Ventures, Presto Ventures II, Rockaway Ventures Fund SCSp and ZAKA Startup 18 as shareholders \(from 2026‑08‑24 entries\)\. *(Verified)* ^[9](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683),[20](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683),[21](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683),[36](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- Public grants: three national grants totalling \~5\.78M CZK \(CzechInvest and ministries\) supporting product development/internationalization\. *(Verified)* ^[22](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-E0C57E408EB523AB5DEC3D175F5C14B60687EF2281EE7E88E0D96A7EEF14E43A),[23](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-ECFB6E6BF304AB059D9781E53253A46317597279C47B6458E4E9B547CEC19336),[24](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-7F57C816735C39D7FE4922DFE0CA74F10EBB49C74734EB86301501AD2B63C3BC)

## Technology profile

- Product surfaces: public subdomains and staging/admin hosts indicate a SaaS product with docs/admin/app endpoints \(docs\.tool, app\.stage, admin\.dev, app\.dev\)\. *(Verified)* ^[25](https://crt.sh/?q=%25.cruxo.io&output=json),[37](https://crt.sh/?q=%25.cruxo.io&output=json),[26](https://crt.sh/?q=%25.cruxo.io&output=json),[27](https://crt.sh/?q=%25.cruxo.io&output=json)
- Core capabilities \(company statements\): unified ad management, real‑time analytics, dashboards, campaign automation, multi‑country/currency support and thousands‑campaign scale claims\. *(Company claim)* ^[1](https://cruxo.io/),[38](https://cruxo.io/),[39](https://cruxo.io/),[40](https://cruxo.io/),[41](https://cruxo.io/retailers/)
  - Assumption: These are site/product claims, not independently validated\.
- Engineering footprint: a small public GitHub org with one archived repo; limited public open‑source artifacts visible\. *(Verified)* ^[42](https://github.com/cruxoio),[13](https://github.com/cruxoio/status)
  - Assumption: Private repos and CI artifacts not visible in facts\.

## Rebuild check

- **Commodity:** Campaign management, dashboards and multi‑format ad inventory UI — rebuildable by a 2–3 person team in weeks using standard ad APIs and BI tools\. *(Analyst view)* ^[1](https://cruxo.io/),[39](https://cruxo.io/),[43](https://cruxo.io/),[44](https://cruxo.io/retailers/)
  - Assumption: Uses standard ad formats and analytics endpoints\.
- **Hard to copy:** Claimed proprietary data‑insights framework, enterprise ad‑serving at 'billions of daily impressions', national grants and named enterprise customers across six countries indicate harder elements to clone\. *(Analyst view)* ^[11](https://cruxo.io/about/),[15](https://cruxo.io/retailers/),[45](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/),[22](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-E0C57E408EB523AB5DEC3D175F5C14B60687EF2281EE7E88E0D96A7EEF14E43A)
  - Assumption: Proprietary data access and scale depend on customer integrations\.
- **Verdict:** Quarter — a competent team could replicate UI/flows in weeks, but a clone would likely lack customer data integrations, grant‑backed product maturation and verified high‑scale ad serving\. *(Analyst view)* ^[1](https://cruxo.io/),[11](https://cruxo.io/about/),[15](https://cruxo.io/retailers/)
  - Assumption: Customer integrations and real traffic volumes are primary moat\.

## Risks and caveats

- IAB TCF claim not found on GVL; may indicate compliance surface claim versus registered vendor status \(verification not\_found\)\. *(Analyst view)* ^[46](https://cruxo.io/retailers/),[14](https://vendor-list.consensu.org/v3/vendor-list.json)
  - Assumption: Company site claim may refer to using a TCF tool, not vendor registration\.
- Ad‑serving scale claim \('billions of daily impressions'\) is unverified and material to scalability and infra spend assumptions\. *(Analyst view)* ^[15](https://cruxo.io/retailers/)
  - Assumption: Press/site language may be marketing hyperbole\.
- Revenue/traction concentration: named customers are large retailers but depth \(ARPU, churn, contract terms\) is unverified; press cites 'unit‑millions CZK per month' without corroborating financial filings\. *(Analyst view)* ^[10](https://cruxo.io/),[28](https://cruxo.io/),[16](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/)
  - Assumption: Public filings \(accounting\) not parsed for revenue line items in facts\.

## Questions for founders

- Please provide evidence \(metrics/SLOs or customer references\) that substantiate the 'billions of daily impressions' ad‑serving claim\. *(Analyst view)* ^[15](https://cruxo.io/retailers/)
  - Assumption: Claim drives infra and gross margin assumptions\.
- Can management produce a GVL vendor ID or legal documentation proving IAB TCF vendor registration/TCF compliance? *(Analyst view)* ^[46](https://cruxo.io/retailers/),[14](https://vendor-list.consensu.org/v3/vendor-list.json)
  - Assumption: GVL listing materially affects publisher consent responsibilities\.
- Request customer contracts or anonymized unit economics from Dr\.Max / Lékárna\.cz to confirm reported 'unit‑millions CZK per month' turnover and revenue concentration\. *(Analyst view)* ^[10](https://cruxo.io/),[28](https://cruxo.io/),[16](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/)
  - Assumption: Press turnover claims require contract validation\.
- Ask for technical architecture overview and logs/access controls showing proprietary data sources used by the 'data insights framework'\. *(Analyst view)* ^[11](https://cruxo.io/about/),[13](https://github.com/cruxoio/status)
  - Assumption: Proprietary data access underpins the asserted moat\.

## Sources

1. [cruxo\.io](https://cruxo.io/) · Company's own website · Product capability — “With CRUXO, you manage your ads in one seamless platform\.”
2. [cruxo\.io](https://cruxo.io/) · Company's own website · Product capability — “Easily manage and launch retail marketing campaigns\. Choose from on\-site banners, sponsored products and brand pages\.”
3. [cruxo\.io](https://cruxo.io/) · Company's own website · Product capability — “Blend onsite, offsite and instore &amp; create seamless customer journey\.”
4. [cruxo\.io](https://cruxo.io/advertisers/) · Company's own website · Product capability — “We plan and manage your retail media campaigns\.”
5. [cruxo\.io](https://cruxo.io/advertisers/) · Company's own website · Product capability — “We evaluate and benchmark your online performance across key retailers\.”
6. [mediaguru\.cz](https://www.mediaguru.cz/clanky/2023/05/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc/) · Independent press · Funding round — “Czech Founders, Presto Ventures a Zaka vkládají do české platformy Cruxo investici ve výši 20 milionů korun na rozvoj retailových médií v Česku i v zahraničí\.”
7. [cc\.cz](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/) · Independent press · Funding round — “Už loni startup získal dvacetimilionovou investici od Presto Ventures, Zaka VC a Czech Founders VC\. A teď do něj přiteklo dalších 15 milionů korun – tentokrát od Rockaway Ventures, Czech Founders VC a několika andělských investorů\.”
8. [rockawayventures\.com](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/) · Independent press · Funding round — “secured investment from Czech Founders VC, Rockaway Ventures, and angel investors for further growth\.”
9. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683) · Official record · Registry: shareholder · 2026\-08\-24 — “Czech Founders Ventures s\.r\.o\., osoba rizikového kapitálu · 10\.77% · from 2026\-08\-24”
10. [cruxo\.io](https://cruxo.io/) · Company's own website · Customer — “As a client of CRUXO, I highly value their deep understanding of retail media and the dynamics between retailers and vendors\. They provide clear guidance on structuring internal processes and workflows\. I value their business\-driven approach and effort to deliver incremental revenue and profitability\.”
11. [cruxo\.io](https://cruxo.io/about/) · Company's own website · Technical claim — “In combination with proprietary data insights framework, we help both retailers and vendors to unlock the full potential of e\-commerce ecosystem\.”
12. [cruxo\.io](https://cruxo.io/about/) · Company's own website · Team claim — “Backed by 90 years of combined experience in retail, vendor marketing, and digital media, CRUXO founders built the platform for retailers and brands that makes launching and scaling retail media fast, simple, and effective\.”
13. [github\.com](https://github.com/cruxoio/status) · Public technical artifact · GitHub repository · 2025\-01\-16 — “cruxoio/status · Markdown · last push 2025\-01\-16”
14. [vendor\-list\.consensu\.org](https://vendor-list.consensu.org/v3/vendor-list.json) · Official record · Independent check of a claim — “'cruxo' is not in the IAB Global Vendor List v185 \(1237 vendors\)\. The claim may mean the platform integrates a TCF\-compliant consent tool rather than being a registered vendor — ask\.”
15. [cruxo\.io](https://cruxo.io/retailers/) · Company's own website · Technical claim — “Ad serving tested by large enterprises with billions of daily impressions\.”
16. [cc\.cz](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/) · Independent press · Customer — “Cruxo navíc hlásí, že už má zákazníky v šesti zemích a jeho měsíční obrat se pohybuje v jednotkách milionů\.”
17. [mediaguru\.cz](https://www.mediaguru.cz/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc) · Independent press · Funding round — “Czech Founders, Presto Ventures a Zaka vkládají do české platformy Cruxo investici ve výši 20 milionů korun na rozvoj retailových médií v Česku i v zahraničí\.”
18. [borovan\.cz](https://www.borovan.cz/hraci_dne/do-marketingove-agentury-cruxo-nalily-miliony-korun-venture-capital-fondy) · Independent press · Funding round — “CRUXO group získala peníze od tří investorů\. Celkem téměř 20 milionů korun do ní vkládají Czech Founders VC , Presto Ventures a Zaka VC \.”
19. [mediar\.cz](https://www.mediar.cz/cruxo-ziskalo-dvacetimilionovou-investici-zakladatele-doplnil-martin-svarc/) · Independent press · Funding round — “Cruxo získalo dvacetimilionovou investici, zakladatele doplnil Martin Švarc — Médiář”
20. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683) · Official record · Registry: shareholder · 2026\-08\-24 — “Presto Ventures II a\.s\., osoba rizikového kapitálu · 7\.69% · from 2026\-08\-24”
21. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683) · Official record · Registry: shareholder · 2026\-08\-24 — “Rockaway Ventures Fund SCSp · 3\.85% · from 2026\-08\-24”
22. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-E0C57E408EB523AB5DEC3D175F5C14B60687EF2281EE7E88E0D96A7EEF14E43A) · Official record · National grant · 2024 — “Podpora z projektu Technologické inkubace\. · Agentura pro podporu podnikání a investic CzechInvest · 1 336 273 CZK”
23. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-ECFB6E6BF304AB059D9781E53253A46317597279C47B6458E4E9B547CEC19336) · Official record · National grant · 2025 — “Účast v programu Internacionalizace v rámci NPO, číslo projektu 2425000002, KA Expanze · Agentura pro podporu podnikání a investic CzechInvest · 2 000 000 CZK”
24. [hlidacstatu\.cz](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-7F57C816735C39D7FE4922DFE0CA74F10EBB49C74734EB86301501AD2B63C3BC) · Official record · National grant · 2026 — “CRUXO rozvoj retail media platformy · Ministerstvo pro místní rozvoj · 2 449 765 CZK”
25. [crt\.sh](https://crt.sh/?q=%25.cruxo.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-10\-04 — “docs\.tool\.cruxo\.io \(first certificate 2023\-10\-04\)”
26. [crt\.sh](https://crt.sh/?q=%25.cruxo.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-10\-10 — “admin\.dev\.cruxo\.io \(first certificate 2023\-10\-10\)”
27. [crt\.sh](https://crt.sh/?q=%25.cruxo.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-10\-10 — “app\.dev\.cruxo\.io \(first certificate 2023\-10\-10\)”
28. [cruxo\.io](https://cruxo.io/) · Company's own website · Customer — “The platform is user\-friendly and intuitive, making it easy to work with while ensuring seamless execution\.”
29. [cruxo\.io](https://cruxo.io/retailers/) · Company's own website · Pricing — “Various pricing models \(from flat rate to CPC, CPM, CPA or CPV\)”
30. [launchbox\.cz](https://launchbox.cz/p/cruxo) · Independent press · Independent check of a claim — “Cruxo – E\-shop jako reklamní plocha pro značky · Launchbox \# Cruxo E\-shop jako reklamní plocha pro značky \#\# Co dělá Cruxo umožňuje obchodníkům vytvářet a schvalovat retail\-media kampaně dodavatelů\. Nastavuje reklamní formáty a cílení podle dat obchodníka a poskytuje dashboardy a přehled rozpočt”
31. [mediaguru\.cz](https://www.mediaguru.cz/lekarna-cz-prevadi-online-inzerci-pod-cruxo) · Independent press · Independent check of a claim — “Cruxo bude nově spravovat digitální inzertní plochy společnosti Lékárna\.cz\. Kromě správy online inzercí bude mít na starost také optimalizaci”
32. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683) · Official record · Independent check of a claim · 2026\-08\-24 — “Press \(borovan\.cz, cc\.cz, mediaguru\.cz, mediar\.cz, rockawayventures\.com\) names Czech Founders as an investor; the commercial register lists Czech Founders Ventures s\.r\.o\., osoba rizikového kapitálu as a shareholder from 2026\-08\-24 \(10\.77%\)\.”
33. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683) · Official record · Independent check of a claim · 2026\-08\-24 — “Press \(borovan\.cz, cc\.cz, mediaguru\.cz, mediar\.cz\) names Presto Ventures as an investor; the commercial register lists Presto Ventures II a\.s\., osoba rizikového kapitálu as a shareholder from 2026\-08\-24 \(7\.69%\)\.”
34. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14134683) · Official record · Registry: incorporation · 2022\-01\-10 — “registered 2022\-01\-10”
35. [www2\.mediaguru\.cz](https://www2.mediaguru.cz/martin-svarc-vstoupil-do-cruxo-je-dalsim-partnerem) · Independent press · Press article · 2023\-04\-18 — “Martin Švarc vstoupil do Cruxo, je dalším partnerem \| MediaGuru”
36. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683) · Official record · Registry: shareholder · 2026\-08\-24 — “ZAKA Startup 18 j\. s\. a\. · 3\.55% · from 2026\-08\-24”
37. [crt\.sh](https://crt.sh/?q=%25.cruxo.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2024\-01\-04 — “app\.stage\.cruxo\.io \(first certificate 2024\-01\-04\)”
38. [cruxo\.io](https://cruxo.io/) · Company's own website · Product capability — “Get real\-time data &amp; insights to improve campaign results\.”
39. [cruxo\.io](https://cruxo.io/) · Company's own website · Product capability — “Discover new ways to monetize your ad space &amp; stay ahead with budget dashboards, smart calendar and digital shelf performance analyzer\.”
40. [cruxo\.io](https://cruxo.io/) · Company's own website · Product capability — “Manage thousands of ad campaigns in a few clicks”
41. [cruxo\.io](https://cruxo.io/retailers/) · Company's own website · Technical claim — “Multi country scalability Manage multiple countries and currencies in one platform —”
42. [github\.com](https://github.com/cruxoio) · Public technical artifact · GitHub organisation · 2023\-09\-05 — “cruxoio · 1 public repos”
43. [cruxo\.io](https://cruxo.io/) · Company's own website · Product capability — “Choose from customisable reports and different data views\.”
44. [cruxo\.io](https://cruxo.io/retailers/) · Company's own website · Product capability — “Save time with self\-served &amp; automated platform”
45. [rockawayventures\.com](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/) · Independent press · Customer — “The platform has customers in 6 countries, supports multiple languages”
46. [cruxo\.io](https://cruxo.io/retailers/) · Company's own website · Technical claim — “Full GDPR compliance, ad serving system implemented the IAB’s TCF standard\.”
47. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683) · Official record · Independent check of a claim · 2026\-08\-24 — “Press \(cc\.cz, rockawayventures\.com\) names Rockaway Ventures as an investor; the commercial register lists Rockaway Ventures Fund SCSp as a shareholder from 2026\-08\-24 \(3\.85%\)\.”
48. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683) · Official record · Independent check of a claim · 2026\-08\-24 — “Press \(borovan\.cz, cc\.cz, mediaguru\.cz, mediar\.cz\) names Zaka as an investor; the commercial register lists ZAKA Startup 18 j\. s\. a\. as a shareholder from 2026\-08\-24 \(3\.55%\)\.”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 24 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 3 | starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 18 | press:finsmes\.com, press:seedtable\.com |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 5 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 76 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 2 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 3 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 7 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 42 | — |

Analysis: gpt\-5\-mini (cost $0.0104); AI extraction cost $0.0105. Full fact table: CSV export.

## Source appendix (all collected facts)

- F2495 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14134683)
- F2496 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/14134683)
- F2497 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2498 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2499 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2500 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2501 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2502 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2503 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2504 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2505 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F2506 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2507 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2508 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2509 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2510 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2511 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2512 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2513 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2514 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2515 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2516 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2517 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1145924](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1145924)
- F2518 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=14134683&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=14134683&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F2519 · web\_page · Sourced · [https://cruxo\.io/](https://cruxo.io/)
- F2520 · web\_page · Sourced · [https://cruxo\.io/privacy\-policy/](https://cruxo.io/privacy-policy/)
- F2521 · web\_page · Sourced · [https://cruxo\.io/about/](https://cruxo.io/about/)
- F2522 · web\_page · Sourced · [https://cruxo\.io/retailers/](https://cruxo.io/retailers/)
- F2523 · web\_page · Sourced · [https://cruxo\.io/advertisers/](https://cruxo.io/advertisers/)
- F2524 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=cruxo\.io&amp;type=MX](https://dns.google/resolve?name=cruxo.io&type=MX)
- F2525 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=cruxo\.io&amp;type=TXT](https://dns.google/resolve?name=cruxo.io&type=TXT)
- F2526 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2527 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2528 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2529 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2530 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2531 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2532 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2533 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2534 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2535 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2536 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2537 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2538 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2539 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2540 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2541 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2542 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2543 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2544 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2545 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2546 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2547 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2548 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2549 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2550 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2551 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2552 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2553 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2554 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2555 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2556 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2557 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2558 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2559 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2560 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2561 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2562 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2563 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2564 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2565 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2566 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2567 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2568 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2569 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2570 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2571 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2572 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2573 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2574 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2575 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2576 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2577 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2578 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2579 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2580 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2581 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2582 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2583 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2584 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2585 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2586 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2587 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2588 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2589 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2590 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2591 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2592 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2593 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2594 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2595 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2596 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2597 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2598 · subdomain · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2599 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.cruxo\.io&amp;output=json](https://crt.sh/?q=%25.cruxo.io&output=json)
- F2600 · github\_org · Sourced · [https://github\.com/cruxoio](https://github.com/cruxoio)
- F2601 · repo · Sourced · [https://github\.com/cruxoio/status](https://github.com/cruxoio/status)
- F2602 · wayback\_first · Sourced · [https://web\.archive\.org/web/20220408211018/https://cruxo\.io/](https://web.archive.org/web/20220408211018/https://cruxo.io/)
- F2603 · wayback\_first · Sourced · [https://web\.archive\.org/web/20230926151606/https://cruxo\.io/blog\-post/the\-future\-is\-here\-understanding\-the\-impact\-of\-retail\-media\-marketing/](https://web.archive.org/web/20230926151606/https://cruxo.io/blog-post/the-future-is-here-understanding-the-impact-of-retail-media-marketing/)
- F2604 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/cruxo\.io](https://web.archive.org/web/%2A/cruxo.io)
- F2611 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2612 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2613 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2614 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2615 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2616 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2617 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2618 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2619 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2620 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2621 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2622 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2623 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2624 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2625 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2626 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2627 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2628 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2629 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2630 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2631 · press\_mention · Sourced · [https://www\.mediaguru\.cz/clanky/2023/05/cruxo\-ziskalo\-na\-svou\-expanzi\-investici\-20\-milionu\-kc/](https://www.mediaguru.cz/clanky/2023/05/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc/)
- F2632 · press\_mention · Sourced · [https://cc\.cz/v\-e\-commerce\-bezi\-tuhy\-boj\-o\-marzi\-i\-zakaznika\-cruxo\-chce\-pomoct\-s\-lepsi\-reklamou\-a\-hlasi\-investici/](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/)
- F2633 · press\_mention · Sourced · [https://itkey\.media/?p=21034](https://itkey.media/?p=21034)
- F2634 · press\_mention · Sourced · [https://www\.mediaguru\.cz/cruxo\-ziskalo\-na\-svou\-expanzi\-investici\-20\-milionu\-kc](https://www.mediaguru.cz/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc)
- F2635 · press\_mention · Sourced · [https://cc\.cz/startup\-exsefa\-rohliku\-i\-manazeru\-procter\-gamble\-pomaha\-navysit\-prijmy\-e\-shopu\-ziskal\-20\-milionu/](https://cc.cz/startup-exsefa-rohliku-i-manazeru-procter-gamble-pomaha-navysit-prijmy-e-shopu-ziskal-20-milionu/)
- F2636 · press\_mention · Sourced · [https://www\.borovan\.cz/hraci\_dne/do\-marketingove\-agentury\-cruxo\-nalily\-miliony\-korun\-venture\-capital\-fondy](https://www.borovan.cz/hraci_dne/do-marketingove-agentury-cruxo-nalily-miliony-korun-venture-capital-fondy)
- F2637 · press\_mention · Sourced · [https://www\.mediar\.cz/cruxo\-ziskalo\-dvacetimilionovou\-investici\-zakladatele\-doplnil\-martin\-svarc/](https://www.mediar.cz/cruxo-ziskalo-dvacetimilionovou-investici-zakladatele-doplnil-martin-svarc/)
- F2638 · press\_mention · Sourced · [https://rockawayventures\.com/cruxo\-revolutionizes\-supplier\-advertising\-on\-e\-commerce\-platforms\-boosts\-e\-shop\-profits\-across\-6\-countries\-and\-secures\-a\-new\-czk\-15\-million\-investment/](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/)
- F2639 · press\_mention · Sourced · [https://zaka\.vc/our\-new\-investment\-retail\-media\-platform\-cruxo\-from\-czech\-republic/](https://zaka.vc/our-new-investment-retail-media-platform-cruxo-from-czech-republic/)
- F2640 · press\_mention · Sourced · [https://czechfounders\.vc/our\-portfolio/cruxo](https://czechfounders.vc/our-portfolio/cruxo)
- F2641 · press\_mention · Sourced · [https://itkey\.media/eur\-800k\-for\-czech\-adtech\-cruxos\-retail\-media\-ambition/](https://itkey.media/eur-800k-for-czech-adtech-cruxos-retail-media-ambition/)
- F2642 · source\_unavailable · Unavailable · [https://www\.finsmes\.com/2023/05/cruxo\-raises\-eur800k\-in\-funding\.html](https://www.finsmes.com/2023/05/cruxo-raises-eur800k-in-funding.html)
- F2643 · press\_mention · Sourced · [https://www\.trysignalbase\.com/news/funding/cruxo\-raises\-602k\-seed](https://www.trysignalbase.com/news/funding/cruxo-raises-602k-seed)
- F2644 · source\_unavailable · Unavailable · [https://seedtable\.com/companies/cruxo](https://seedtable.com/companies/cruxo)
- F2645 · press\_mention · Sourced · [https://technologickainkubace\.org/en/startupy/cruxo](https://technologickainkubace.org/en/startupy/cruxo)
- F2646 · press\_mention · Sourced · [https://www\.cnaip\.cz/en/entity/cruxo](https://www.cnaip.cz/en/entity/cruxo)
- F2647 · press\_mention · Sourced · [https://upnext\.world/retail\-media\-smaller\-retailers\-cruxo\-europe/](https://upnext.world/retail-media-smaller-retailers-cruxo-europe/)
- F2648 · press\_mention · Sourced · [https://www\.gaebler\.com/VC\-Funding\-BAE4ADF4\-A318\-464B\-BB92\-C04A7D76362F\-Cruxo\-05\-08\-2023](https://www.gaebler.com/VC-Funding-BAE4ADF4-A318-464B-BB92-C04A7D76362F-Cruxo-05-08-2023)
- F2649 · press\_mention · Sourced · [https://millionrounds\.com/company/cruxo](https://millionrounds.com/company/cruxo)
- F2650 · press\_mention · Sourced · [https://www2\.mediaguru\.cz/martin\-svarc\-vstoupil\-do\-cruxo\-je\-dalsim\-partnerem](https://www2.mediaguru.cz/martin-svarc-vstoupil-do-cruxo-je-dalsim-partnerem)
- F5457 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/hledat?Q=ico%3A14134683](https://www.hlidacstatu.cz/hledat?Q=ico%3A14134683)
- F5458 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-E0C57E408EB523AB5DEC3D175F5C14B60687EF2281EE7E88E0D96A7EEF14E43A](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-E0C57E408EB523AB5DEC3D175F5C14B60687EF2281EE7E88E0D96A7EEF14E43A)
- F5459 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/DeMinimis\-ECFB6E6BF304AB059D9781E53253A46317597279C47B6458E4E9B547CEC19336](https://www.hlidacstatu.cz/Dotace/Detail/DeMinimis-ECFB6E6BF304AB059D9781E53253A46317597279C47B6458E4E9B547CEC19336)
- F5460 · grant\_national · Sourced · [https://www\.hlidacstatu\.cz/Dotace/Detail/Eufondy\-7F57C816735C39D7FE4922DFE0CA74F10EBB49C74734EB86301501AD2B63C3BC](https://www.hlidacstatu.cz/Dotace/Detail/Eufondy-7F57C816735C39D7FE4922DFE0CA74F10EBB49C74734EB86301501AD2B63C3BC)
- F5461 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Cruxo%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Cruxo%27)
- F5462 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F5691 · product\_capability · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5692 · product\_capability · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5693 · product\_capability · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5694 · product\_capability · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5695 · product\_capability · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5696 · product\_capability · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5697 · product\_capability · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5698 · customer · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5699 · customer · Medium confidence · [https://cruxo\.io/](https://cruxo.io/)
- F5700 · tech\_claim · Medium confidence · [https://cruxo\.io/about/](https://cruxo.io/about/)
- F5701 · team\_claim · Medium confidence · [https://cruxo\.io/about/](https://cruxo.io/about/)
- F5702 · product\_capability · Medium confidence · [https://cruxo\.io/retailers/](https://cruxo.io/retailers/)
- F5703 · product\_capability · Medium confidence · [https://cruxo\.io/retailers/](https://cruxo.io/retailers/)
- F5704 · product\_capability · Medium confidence · [https://cruxo\.io/retailers/](https://cruxo.io/retailers/)
- F5705 · tech\_claim · Medium confidence · [https://cruxo\.io/retailers/](https://cruxo.io/retailers/)
- F5706 · tech\_claim · Medium confidence · [https://cruxo\.io/retailers/](https://cruxo.io/retailers/)
- F5707 · pricing · Medium confidence · [https://cruxo\.io/retailers/](https://cruxo.io/retailers/)
- F5708 · tech\_claim · Medium confidence · [https://cruxo\.io/retailers/](https://cruxo.io/retailers/)
- F5709 · product\_capability · Medium confidence · [https://cruxo\.io/advertisers/](https://cruxo.io/advertisers/)
- F5710 · product\_capability · Medium confidence · [https://cruxo\.io/advertisers/](https://cruxo.io/advertisers/)
- F5711 · product\_capability · Medium confidence · [https://cruxo\.io/advertisers/](https://cruxo.io/advertisers/)
- F5712 · product\_capability · Medium confidence · [https://cruxo\.io/advertisers/](https://cruxo.io/advertisers/)
- F5713 · product\_capability · Medium confidence · [https://cruxo\.io/advertisers/](https://cruxo.io/advertisers/)
- F5714 · pricing · Medium confidence · [https://cruxo\.io/advertisers/](https://cruxo.io/advertisers/)
- F5715 · funding\_round · Medium confidence · [https://www\.mediaguru\.cz/clanky/2023/05/cruxo\-ziskalo\-na\-svou\-expanzi\-investici\-20\-milionu\-kc/](https://www.mediaguru.cz/clanky/2023/05/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc/)
- F5716 · product\_capability · Medium confidence · [https://www\.mediaguru\.cz/clanky/2023/05/cruxo\-ziskalo\-na\-svou\-expanzi\-investici\-20\-milionu\-kc/](https://www.mediaguru.cz/clanky/2023/05/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc/)
- F5717 · team\_claim · Medium confidence · [https://www\.mediaguru\.cz/clanky/2023/05/cruxo\-ziskalo\-na\-svou\-expanzi\-investici\-20\-milionu\-kc/](https://www.mediaguru.cz/clanky/2023/05/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc/)
- F5718 · funding\_round · Medium confidence · [https://cc\.cz/v\-e\-commerce\-bezi\-tuhy\-boj\-o\-marzi\-i\-zakaznika\-cruxo\-chce\-pomoct\-s\-lepsi\-reklamou\-a\-hlasi\-investici/](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/)
- F5719 · customer · Medium confidence · [https://cc\.cz/v\-e\-commerce\-bezi\-tuhy\-boj\-o\-marzi\-i\-zakaznika\-cruxo\-chce\-pomoct\-s\-lepsi\-reklamou\-a\-hlasi\-investici/](https://cc.cz/v-e-commerce-bezi-tuhy-boj-o-marzi-i-zakaznika-cruxo-chce-pomoct-s-lepsi-reklamou-a-hlasi-investici/)
- F5720 · funding\_round · Medium confidence · [https://www\.mediaguru\.cz/cruxo\-ziskalo\-na\-svou\-expanzi\-investici\-20\-milionu\-kc](https://www.mediaguru.cz/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc)
- F5721 · product\_capability · Medium confidence · [https://www\.mediaguru\.cz/cruxo\-ziskalo\-na\-svou\-expanzi\-investici\-20\-milionu\-kc](https://www.mediaguru.cz/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc)
- F5722 · team\_claim · Medium confidence · [https://www\.mediaguru\.cz/cruxo\-ziskalo\-na\-svou\-expanzi\-investici\-20\-milionu\-kc](https://www.mediaguru.cz/cruxo-ziskalo-na-svou-expanzi-investici-20-milionu-kc)
- F5725 · funding\_round · Medium confidence · [https://www\.borovan\.cz/hraci\_dne/do\-marketingove\-agentury\-cruxo\-nalily\-miliony\-korun\-venture\-capital\-fondy](https://www.borovan.cz/hraci_dne/do-marketingove-agentury-cruxo-nalily-miliony-korun-venture-capital-fondy)
- F5726 · product\_capability · Medium confidence · [https://www\.borovan\.cz/hraci\_dne/do\-marketingove\-agentury\-cruxo\-nalily\-miliony\-korun\-venture\-capital\-fondy](https://www.borovan.cz/hraci_dne/do-marketingove-agentury-cruxo-nalily-miliony-korun-venture-capital-fondy)
- F5727 · team\_claim · Medium confidence · [https://www\.borovan\.cz/hraci\_dne/do\-marketingove\-agentury\-cruxo\-nalily\-miliony\-korun\-venture\-capital\-fondy](https://www.borovan.cz/hraci_dne/do-marketingove-agentury-cruxo-nalily-miliony-korun-venture-capital-fondy)
- F5728 · funding\_round · Medium confidence · [https://www\.mediar\.cz/cruxo\-ziskalo\-dvacetimilionovou\-investici\-zakladatele\-doplnil\-martin\-svarc/](https://www.mediar.cz/cruxo-ziskalo-dvacetimilionovou-investici-zakladatele-doplnil-martin-svarc/)
- F5729 · product\_capability · Medium confidence · [https://www\.mediar\.cz/cruxo\-ziskalo\-dvacetimilionovou\-investici\-zakladatele\-doplnil\-martin\-svarc/](https://www.mediar.cz/cruxo-ziskalo-dvacetimilionovou-investici-zakladatele-doplnil-martin-svarc/)
- F5730 · funding\_round · Medium confidence · [https://rockawayventures\.com/cruxo\-revolutionizes\-supplier\-advertising\-on\-e\-commerce\-platforms\-boosts\-e\-shop\-profits\-across\-6\-countries\-and\-secures\-a\-new\-czk\-15\-million\-investment/](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/)
- F5731 · product\_capability · Medium confidence · [https://rockawayventures\.com/cruxo\-revolutionizes\-supplier\-advertising\-on\-e\-commerce\-platforms\-boosts\-e\-shop\-profits\-across\-6\-countries\-and\-secures\-a\-new\-czk\-15\-million\-investment/](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/)
- F5732 · product\_capability · Medium confidence · [https://rockawayventures\.com/cruxo\-revolutionizes\-supplier\-advertising\-on\-e\-commerce\-platforms\-boosts\-e\-shop\-profits\-across\-6\-countries\-and\-secures\-a\-new\-czk\-15\-million\-investment/](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/)
- F5733 · customer · Medium confidence · [https://rockawayventures\.com/cruxo\-revolutionizes\-supplier\-advertising\-on\-e\-commerce\-platforms\-boosts\-e\-shop\-profits\-across\-6\-countries\-and\-secures\-a\-new\-czk\-15\-million\-investment/](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/)
- F5734 · team\_claim · Medium confidence · [https://rockawayventures\.com/cruxo\-revolutionizes\-supplier\-advertising\-on\-e\-commerce\-platforms\-boosts\-e\-shop\-profits\-across\-6\-countries\-and\-secures\-a\-new\-czk\-15\-million\-investment/](https://rockawayventures.com/cruxo-revolutionizes-supplier-advertising-on-e-commerce-platforms-boosts-e-shop-profits-across-6-countries-and-secures-a-new-czk-15-million-investment/)
- F6364 · verification · Sourced · [https://vendor\-list\.consensu\.org/v3/vendor\-list\.json](https://vendor-list.consensu.org/v3/vendor-list.json)
- F6365 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F6366 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F6367 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F6368 · verification · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/14134683](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14134683)
- F6369 · verification · Sourced · [https://launchbox\.cz/p/cruxo](https://launchbox.cz/p/cruxo)
- F6370 · verification · Sourced · [https://www\.mediaguru\.cz/lekarna\-cz\-prevadi\-online\-inzerci\-pod\-cruxo](https://www.mediaguru.cz/lekarna-cz-prevadi-online-inzerci-pod-cruxo)
