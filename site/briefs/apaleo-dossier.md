# Apaleo — due diligence brief

apaleo\.com · DE · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — part of it rests on an official or independent source, part on one outlet or the company's own words; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** API\-first, AI\-powered property management platform selling SaaS PMS and developer APIs to hotel and serviced\-apartment operators\. *(Company claim)* ^[1](https://apaleo.com/),[2](https://apaleo.com/about-us),[3](https://apaleo.com/api-terms-of-use)
- **Stage & traction.** Evidence of growth\-stage traction: reported Series A and a later €20M growth equity round led by PSG; press claims \~85k units, 1,700 properties\. *(Corroborated)* ^[4](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo),[5](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html),[6](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo)
- **Technology & moat.** Potential moat: open API ecosystem plus claimed MCP Server \(Model Context Protocol\) that exposes live property data to agents; public repos and API docs support platform openness\. *(Partly verified)* ^[2](https://apaleo.com/about-us),[7](https://apaleo.com/ai-powered-pms-solution),[8](https://github.com/apaleo/gsheet-addon),[9](https://apaleo.com/api-terms-of-use)
- **Key risk.** Key decision risk: AI/legal/compliance exposure — product relies on third‑party LLM vendors \(Anthropic, OpenAI\) while SOC2/compliance claims are not independently verifiable from public pages\. *(Analyst view)* ^[10](https://apaleo.com/dpa),[11](https://apaleo.com/dpa),[12](https://apaleo.com/)
- **Diligence focus.** First diligence to run: obtain SOC 2/PCI/PSD2 evidence and data\-flow mappings showing how MCP Server limits LLM access to PII and live hotel data\. *(Analyst view)* ^[12](https://apaleo.com/),[7](https://apaleo.com/ai-powered-pms-solution),[13](https://apaleo.com/pricing)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2023\-04\-26 · Series A · 9M EUR · Rockaway Ventures, Serpentine Ventures; 2024\-11\-20 · growth equity · 20M EUR · PSG, Redalpine, FOMCAP IV, Rockaway Ventures · 4 reports | 4, 14, 5, 15, 16 |
| Thesis fit \(Rockaway\) | sectors: AI\-led transformative tech \(6 facts\); deep tech \(5 facts\) · geography: DE \(core region\) · overlaps portfolio: JISR Institute, a\.s\. \(distrib, third\-p\) | 17, 18, 19 |
| Hiring | 11 open roles: sales gtm 4, other 3, engineering 3, forward deployed 1; Munich, Munich / Remote, Munich/ Berlin, Munich/ Berlin/ Germany remote, Paris, France | 20, 21, 22, 23, 24, 25 |
| AI dependency | relies on \(subprocessor / own claims\): Anthropic, OpenAI; own\-model evidence: 1 papers, 0 verified HF models, 1 ML roles, 0 own\-model claims | 10, 11, 26, 27 |
| Engineering footprint | 3 public repos \(8★, last push 2026\-11\-16\); product surfaces: portal\.apaleo\.com, status\.apaleo\.com; 1 docs pages; stack: Next\.js | 28, 29, 8, 30, 31, 9 |
| Customers | public pricing: yes | 32 |
| Claims checked | SOC 2 / ISO: not checkable | 12 |
| Timeline | first press 2018\-05\-02 \(21 articles collected\) | 33 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** API\-first, AI\-powered hospitality platform aligns with 'AI\-led transformative tech' and 'industrial / manufacturing AI' thesis elements via explicit AI product claims and architecture\. *(Analyst view)* ^[1](https://apaleo.com/),[7](https://apaleo.com/ai-powered-pms-solution),[34](https://apaleo.com/ai-powered-pms-solution),[35](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html)
  - Assumption: Fund's sector labels listed in DERIVED\.thesis apply
- **Portfolio overlap:** JISR Institute, a\.s\. appears in Rockaway's derived portfolio list; no direct product overlap shown in Apaleo facts, so likely not a conflict and could be neutral or synergistic\. *(Analyst view)* ^[6](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo),[4](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo)
  - Assumption: Derived portfolio\_overlap entry is accurate

## Business model

- Primary customers: hotel operators; Apaleo sells a SaaS property\-management platform to operators\. *(Partly verified)* ^[3](https://apaleo.com/api-terms-of-use),[36](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo)
- Pricing: published plans include €8 per room/month, and plans starting at €400/month; API usage is declared free\. *(Company claim)* ^[37](https://apaleo.com/pricing),[38](https://apaleo.com/pricing),[39](https://apaleo.com/api-terms-of-use)
- Other revenue lines stated: integrated payments \(Apaleo Pay\) and an app/store commerce layer \(Apaleo Store\)\. *(Company claim)* ^[40](https://apaleo.com/about-us),[41](https://apaleo.com/about-us),[2](https://apaleo.com/about-us)

## Competition

No sourced findings for this section.

## Case for and against

- **For:** Established product positioning—API\-first, MACH architecture and open\-PMS messaging give clear developer and integrator appeal\. *(Analyst view)* ^[42](https://apaleo.com/),[43](https://apaleo.com/about-us),[35](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html)
- **For:** Product roadmap includes AI agent layer \(Copilot\) and MCP Server to expose live property data to models—differentiator for AI\-enabled workflows\. *(Analyst view)* ^[7](https://apaleo.com/ai-powered-pms-solution),[34](https://apaleo.com/ai-powered-pms-solution),[44](https://apaleo.com/ai-powered-pms-solution)
- **Against:** Security/compliance claims \(SOC 2, PCI, PSD2\) are asserted but the SOC 2 attestation is not verifiable from available pages\. *(Analyst view)* ^[45](https://apaleo.com/),[12](https://apaleo.com/)
  - Assumption: SOC 2 report not published online
- **Against:** Dependence on third\-party AI and infra vendors \(Anthropic, OpenAI, AWS, PostHog\) creates operational and data\-governance dependencies\. *(Analyst view)* ^[10](https://apaleo.com/dpa),[11](https://apaleo.com/dpa),[46](https://apaleo.com/dpa),[47](https://apaleo.com/dpa)
- **Must be true:** Customer adoption / retention across &gt;1,700 properties or equivalent ARR must be validated versus the stated scale claims\. *(Analyst view)* ^[6](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo),[4](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo)
  - Assumption: Press/PR scale claim reflects paying customers
- **Must be true:** Confirmed, current SOC 2 / PCI evidence and contractual data\-handling terms for AI integrations \(OpenAI/Anthropic\) are in place and allowed by major enterprise buyers\. *(Analyst view)* ^[12](https://apaleo.com/),[10](https://apaleo.com/dpa),[11](https://apaleo.com/dpa)
  - Assumption: Enterprise procurement requires verifiable attestations

# Technical due diligence

## Ownership and capital

- Reported funding: extended Series A reported at EUR 9M \(Rockaway, Serpentine\) and a subsequent €20M growth equity round led by PSG with Redalpine, FOMCAP IV and Rockaway named\. *(Corroborated)* ^[4](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo),[5](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html),[14](https://www.privateequityinternational.com/psg-leads-growth-equity-funding-round-in-apaleo),[15](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo),[16](https://www.serpentine.vc/blog/apaleo-secures-20m-growth-equity-to-accelerate-global-expansion/)

## Technology profile

- What is built: API\-first open PMS, Apaleo Pay, Apaleo Store, and an AI 'Copilot' plus MCP Server for agent access to live property data \(company claims and product pages\)\. *(Company claim)* ^[41](https://apaleo.com/about-us),[40](https://apaleo.com/about-us),[34](https://apaleo.com/ai-powered-pms-solution),[7](https://apaleo.com/ai-powered-pms-solution)
- Engineering footprint: public GitHub org with active repos \(gsheet\-addon, n8n nodes\), a developer docs page, and public portal/status subdomains\. *(Partly verified)* ^[8](https://github.com/apaleo/gsheet-addon),[29](https://github.com/apaleo/n8n-nodes-apaleo),[28](https://github.com/apaleo/docker-resx2cs),[9](https://apaleo.com/api-terms-of-use),[31](https://crt.sh/?q=%25.apaleo.com&output=json)
- AI dependency and ops: company lists Anthropic and OpenAI as subprocessors \(LLM vendors used\); no public evidence of in\-house LLMs beyond a paper unrelated to product\. *(Partly verified)* ^[10](https://apaleo.com/dpa),[11](https://apaleo.com/dpa),[26](https://openalex.org/W7160130889)

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** API\-first PMS core and developer tools can be reproduced using public APIs, Next\.js frontend, AWS infra and documented API terms\. *(Analyst view)* ^[2](https://apaleo.com/about-us),[48](https://apaleo.com/),[46](https://apaleo.com/dpa),[9](https://apaleo.com/api-terms-of-use)
  - Assumption: No proprietary datasets or closed models required
- **Edge supported by public evidence:** Claimed MCP Server that implements a 'Model Context Protocol' to give agents secure live\-data access is public company claim and thus evidence of a unique integration approach\. *(Analyst view)* ^[7](https://apaleo.com/ai-powered-pms-solution),[44](https://apaleo.com/ai-powered-pms-solution)
  - Assumption: MCP Server is functionally implemented as described
- **Cannot be judged from outside:** Agentic efficacy, safety of autonomous Copilot actions, and real\-world impact on hotel operations cannot be judged without access to product logs, models, and field metrics\. *(Analyst view)* ^[34](https://apaleo.com/ai-powered-pms-solution),[12](https://apaleo.com/)
  - Assumption: Operational telemetry and model internals are not public

## Risks and caveats

- Dependency on third‑party LLM providers \(Anthropic, OpenAI\) for AI features creates vendor, cost, and data‑flow risk\. *(Analyst view)* ^[10](https://apaleo.com/dpa),[11](https://apaleo.com/dpa)
- Security/compliance evidence gap: SOC 2 / compliance claims are publicly stated but verification is not possible from collected pages\. *(Analyst view)* ^[45](https://apaleo.com/),[12](https://apaleo.com/)
- API sandbox/third‑party outages have been reported affecting distribution APIs, indicating exposure of developer experience and integrations to upstream vendors\. *(Analyst view)* ^[49](https://status.apaleo.com/),[50](https://status.apaleo.com/)

## Questions for founders

- Please produce SOC 2/PCI/PSD2 evidence and scope; verification fact shows claims are not publicly checkable\. *(Analyst view)* ^[12](https://apaleo.com/),[13](https://apaleo.com/pricing)
- Provide contract examples and revenue split for customers behind the claimed 85k units / 1,700 properties metric used in press coverage\. *(Analyst view)* ^[6](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo),[19](https://hoteltechnologynews.com/2024/11/apaleo-raises-21-million-to-expand-its-hotel-property-management-platform-built-on-api-first-architecture)
- Detail MCP Server data flow: which live fields are exposed to agents, and how PII is filtered before any LLM call\. *(Analyst view)* ^[7](https://apaleo.com/ai-powered-pms-solution),[10](https://apaleo.com/dpa)
- Supply SLA and incident history for API sandbox outages and quantify customer impact from status notices\. *(Analyst view)* ^[49](https://status.apaleo.com/),[50](https://status.apaleo.com/)

## Sources

1. [apaleo\.com](https://apaleo.com/) · Company's own website · Product capability — “An API\-first, AI\-powered Property Management Platform”
2. [apaleo\.com](https://apaleo.com/about-us) · Company's own website · Product capability — “Apaleo APIs”
3. [apaleo\.com](https://apaleo.com/api-terms-of-use) · Company's own website · Customer — “apaleo GmbH \(hereinafter referred to as "apaleo“ or "we“\) operates and provides a property management platform \(hereinafter referred to as "platform“\) over the internet to its customers, which are hotel operators, as a software as a service model\.”
4. [bakertilly\.de](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo) · Independent press · Funding round — “With the legal support of Baker Tilly, Rockaway Ventures and Serpentine Ventures invested in open hospitality platform Apaleo GmbH within an extended Series A financing round, bringing the growth funding to a total volume of EUR 9 million\.”
5. [finance\.yahoo\.com](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html) · Independent press · Funding round — “Open property management platform Apaleo has secured €20m \(€21\.1m\) in a funding growth equity investment\.”
6. [hengeler\-news\.com](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo) · Independent press · Technical claim — “Apaleo’s portfolio spans over 30 countries worldwide, managing more than 85,000 units across diverse markets and serving over 1,700 properties\.”
7. [apaleo\.com](https://apaleo.com/ai-powered-pms-solution) · Company's own website · Product capability — “The Apaleo MCP Server brings the Model Context Protocol to our open platform, giving AI agents a secure, direct way to access live property data and interact with Apaleo, without custom integrations\.”
8. [github\.com](https://github.com/apaleo/gsheet-addon) · Public technical artifact · GitHub repository · 2026\-11\-16 — “apaleo/gsheet\-addon · apaleo add\-on for Google Sheets · TypeScript · last push 2026\-11\-16”
9. [apaleo\.com](https://apaleo.com/api-terms-of-use) · Company's own website · Website page — “API Terms of Use \| Apaleo Hospitality Platform”
10. [apaleo\.com](https://apaleo.com/dpa) · Company's own website · Subprocessor \(privacy policy\) — “Apaleo uses large language models \(including Anthropic Claude models\) hosted by AWS \(Amazon Bedrock\) in all current and upcoming AI features\.”
11. [apaleo\.com](https://apaleo.com/dpa) · Company's own website · Subprocessor \(privacy policy\) — “OpenAI Ireland Ltd\. \(IE\) / OpenAI OpCo, LLC \(US\) – AI Subcontractor”
12. [apaleo\.com](https://apaleo.com/) · Company's own website · Independent check of a claim — “No trust portal, auditor or compliance\-platform reference found on the collected security pages or subdomains\. SOC 2 reports are private; the claim can only be verified by requesting the report\.”
13. [apaleo\.com](https://apaleo.com/pricing) · Company's own website · Technical claim — “PSD2 and PCI DSS certification”
14. [privateequityinternational\.com](https://www.privateequityinternational.com/psg-leads-growth-equity-funding-round-in-apaleo) · Independent press · Funding round — “PSG leads growth equity funding round in Apaleo”
15. [hengeler\-news\.com](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo) · Independent press · Funding round — “Apaleo, the API\-first open property management platform for the hospitality industry, has raised €20 million in a growth equity investment round led by PSG Equity\.”
16. [serpentine\.vc](https://www.serpentine.vc/blog/apaleo-secures-20m-growth-equity-to-accelerate-global-expansion/) · Independent press · Funding round — “Apaleo, a Serpentine Ventures portfolio company, raised €20M in growth equity led by PSG Equity\.”
17. [techround\.co\.uk](https://techround.co.uk/interviews/stephan-wiesener-founder-at-apaleo/) · Independent press · Press article · 2025\-09\-08 — “Stephan Wiesener, Founder at Apaleo: Building The Industry’s Most Flexible Property Management Platform \- TechRound”
18. [themodernhotelier\.com](https://themodernhotelier.com/episode/296) · Independent press · Press article · 2026\-06\-26 — “Giving Hoteliers Flexibility to Build Their Ideal Tech Stack \| with Philip von Ditfurth &amp; Florian Montag”
19. [hoteltechnologynews\.com](https://hoteltechnologynews.com/2024/11/apaleo-raises-21-million-to-expand-its-hotel-property-management-platform-built-on-api-first-architecture) · Independent press · Press article · 2024\-11\-21 — “Apaleo Raises $21 Million to Expand Its Hotel Property Management Platform Built on API\-First Architecture \|”
20. [boards\.greenhouse\.io](https://boards.greenhouse.io/apaleo) · Company's own website · Job posting — “Account Manager \(f/m/d\) · Munich/ Berlin/ Germany remote”
21. [boards\.greenhouse\.io](https://boards.greenhouse.io/apaleo) · Company's own website · Job posting — “GTM Engineer, marketing \(f/m/d\) · Munich”
22. [boards\.greenhouse\.io](https://boards.greenhouse.io/apaleo) · Company's own website · Job posting — “Sales Solutions Manager \(f/m/d\) · Munich/ Berlin”
23. [boards\.greenhouse\.io](https://boards.greenhouse.io/apaleo) · Company's own website · Job posting — “Technical Partnerships Manager \(f/m/d\) · Munich/ Berlin”
24. [boards\.greenhouse\.io](https://boards.greenhouse.io/apaleo) · Company's own website · Job posting — “Engineering Manager \(f/m/d\) · Munich”
25. [boards\.greenhouse\.io](https://boards.greenhouse.io/apaleo) · Company's own website · Job posting — “Senior Bilanzbuchhalter\*in \(m/w/d\) · Munich”
26. [openalex\.org](https://openalex.org/W7160130889) · Public technical artifact · Research paper · 2026\-02\-18 — “Body mass estimation for Neoglyptatelus uruguayensis Fernicola et al\., 2017 \(Mammalia, Cingulata, Pachyarmatheriidae\) · Revista Brasileira de Paleontologia”
27. [boards\.greenhouse\.io](https://boards.greenhouse.io/apaleo) · Company's own website · Job posting — “Senior Product Manager, AI Products &amp; Agentic Hospitality \(f/m/d\) · Munich”
28. [github\.com](https://github.com/apaleo/docker-resx2cs) · Public technical artifact · GitHub repository · 2022\-11\-25 — “apaleo/docker\-resx2cs · A small docker container to transfer resource files to c\# methods · JavaScript · last push 2022\-11\-25”
29. [github\.com](https://github.com/apaleo/n8n-nodes-apaleo) · Public technical artifact · GitHub repository · 2026\-10\-30 — “apaleo/n8n\-nodes\-apaleo · Apaleo nodes for N8N community · TypeScript · last push 2026\-10\-30”
30. [crt\.sh](https://crt.sh/?q=%25.apaleo.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2017\-07\-11 — “status\.apaleo\.com \(first certificate 2017\-07\-11\)”
31. [crt\.sh](https://crt.sh/?q=%25.apaleo.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-06\-29 — “portal\.apaleo\.com \(first certificate 2026\-06\-29\)”
32. [apaleo\.com](https://apaleo.com/) · Company's own website · Pricing — “With Apaleo, you never pay set\-up, license, maintenance, or integration fees, and you stay completely free from vendor lock\-in, enjoying full flexibility\.”
33. [redalpine\.com](https://www.redalpine.com/post/redalpine-invests-in-apaleo-disruptor-of-hotel-management-software) · Independent press · Press article · 2018\-05\-02 — “Redalpine invests in apaleo, disruptor of hotel management software”
34. [apaleo\.com](https://apaleo.com/ai-powered-pms-solution) · Company's own website · Product capability — “Meet the Apaleo Copilot\. A new agentic layer built into our platform that lets you handle complex tasks through a simple chat interface, whether checking arrivals, assigning rooms, resolving overbookings, or planning housekeeping\.”
35. [finance\.yahoo\.com](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html) · Independent press · Technical claim — “Supported by its microservices\-based, API\-first, cloud\-native, headless \(MACH\) architecture, the company offers scalability and flexibility for businesses to customise technology solutions to their unique business models\.”
36. [bakertilly\.de](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo) · Independent press · Product capability — “Founded in 2017 out of Munich, Apaleo is the open property management platform for hotel and serviced apartment groups\.”
37. [apaleo\.com](https://apaleo.com/pricing) · Company's own website · Pricing — “€8 per room per month”
38. [apaleo\.com](https://apaleo.com/pricing) · Company's own website · Pricing — “Starting at €400 per month”
39. [apaleo\.com](https://apaleo.com/api-terms-of-use) · Company's own website · Pricing — “The object of the agreement is your free\-of\-charge use of the API for the apaleo platform as per the documentation made available by us through the internet in its current form under your registration as a developer with us”
40. [apaleo\.com](https://apaleo.com/about-us) · Company's own website · Product capability — “Apaleo Pay”
41. [apaleo\.com](https://apaleo.com/about-us) · Company's own website · Product capability — “Apaleo Store”
42. [apaleo\.com](https://apaleo.com/) · Company's own website · Technical claim — “The only API\-first hospitality platform Discerning developers prefer Apaleo because our platform is built on MACH architecture\. Experience the speed, reliability, and flexibility of a platform built for microservices, APIs, cloud, and headless\.”
43. [apaleo\.com](https://apaleo.com/about-us) · Company's own website · Technical claim — “We take an API\-first approach to hotel tech”
44. [apaleo\.com](https://apaleo.com/ai-powered-pms-solution) · Company's own website · Product capability — “Open architecture enabling the autonomous hotel”
45. [apaleo\.com](https://apaleo.com/) · Company's own website · Technical claim — “Apaleo exceeds modern standards for data protection including GDPR, PCI, PSD2 and SOC 2 compliance\.”
46. [apaleo\.com](https://apaleo.com/dpa) · Company's own website · Subprocessor \(privacy policy\) — “Amazon Web Services EMEA SARL \(DE\) app\.Apaleo\.com uses Amazon Web Services \(AWS\) as infrastructure\. Thereby, personal data is stored and processed on AWS servers\.”
47. [apaleo\.com](https://apaleo.com/dpa) · Company's own website · Subprocessor \(privacy policy\) — “PostHog, Inc\. \(US\) – EU\-region hosting Apaleo uses PostHog for product analytics, to log prompt text and non\-personal usage data \(timing, outcome, feature interactions\) of the Fluid Dashboards feature in order to understand and improve it\.”
48. [apaleo\.com](https://apaleo.com/) · Public technical artifact · Technology detected
49. [status\.apaleo\.com](https://status.apaleo.com/) · Company's own website · Technical claim — “Some API request to distribution\.apaleo\.com are failing”
50. [status\.apaleo\.com](https://status.apaleo.com/) · Company's own website · Technical claim — “We are awaiting resolution from a third\-party service sandbox environment that is down\.”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 1 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | hlidac\_statu, starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 21 | press:hospitalityinvestor\.com, press:hospitalitynet\.org, press:hoteltechreport\.com, press:phocuswire\.com |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 62 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 34 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 4 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 1 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 5 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 1 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 45 | — |

Analysis: gpt\-5\-mini (cost $0.0151); AI extraction cost $0.0075. Full fact table: CSV export.

## Source appendix (all collected facts)

- F3878 · registry\_flag · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F3879 · web\_page · Sourced · [https://apaleo\.com/](https://apaleo.com/)
- F3880 · web\_page · Sourced · [https://apaleo\.com/careers](https://apaleo.com/careers)
- F3881 · web\_page · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3882 · web\_page · Sourced · [https://job\-boards\.greenhouse\.io/apaleo/jobs/8069357003](https://job-boards.greenhouse.io/apaleo/jobs/8069357003)
- F3883 · web\_page · Sourced · [https://job\-boards\.greenhouse\.io/apaleo](https://job-boards.greenhouse.io/apaleo)
- F3884 · web\_page · Sourced · [https://job\-boards\.greenhouse\.io/apaleo/jobs/8034366003](https://job-boards.greenhouse.io/apaleo/jobs/8034366003)
- F3885 · web\_page · Sourced · [https://job\-boards\.greenhouse\.io/apaleo/jobs/8016726003](https://job-boards.greenhouse.io/apaleo/jobs/8016726003)
- F3886 · web\_page · Sourced · [https://job\-boards\.greenhouse\.io/apaleo/jobs/8016738003](https://job-boards.greenhouse.io/apaleo/jobs/8016738003)
- F3887 · web\_page · Sourced · [https://job\-boards\.greenhouse\.io/apaleo/jobs/8026893003](https://job-boards.greenhouse.io/apaleo/jobs/8026893003)
- F3888 · web\_page · Sourced · [https://job\-boards\.greenhouse\.io/apaleo/jobs/8034435003](https://job-boards.greenhouse.io/apaleo/jobs/8034435003)
- F3889 · web\_page · Sourced · [https://job\-boards\.greenhouse\.io/apaleo/jobs/7730251003](https://job-boards.greenhouse.io/apaleo/jobs/7730251003)
- F3890 · web\_page · Sourced · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3891 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3892 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3893 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3894 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3895 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3896 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3897 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3898 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3899 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3900 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3901 · subprocessor · Medium confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3902 · web\_page · Sourced · [https://apaleo\.com/dpa\-archive](https://apaleo.com/dpa-archive)
- F3903 · web\_page · Sourced · [https://apaleo\.com/gdpr](https://apaleo.com/gdpr)
- F3904 · web\_page · Sourced · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3905 · subprocessor · Medium confidence · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3906 · subprocessor · Medium confidence · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3907 · subprocessor · Medium confidence · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3908 · subprocessor · Medium confidence · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3909 · subprocessor · Medium confidence · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3910 · subprocessor · Medium confidence · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3911 · subprocessor · Medium confidence · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3912 · subprocessor · Medium confidence · [https://apaleo\.com/privacy\-policy](https://apaleo.com/privacy-policy)
- F3913 · web\_page · Sourced · [https://apaleo\.com/pricing](https://apaleo.com/pricing)
- F3914 · web\_page · Sourced · [https://apaleo\.com/ai\-powered\-pms\-solution](https://apaleo.com/ai-powered-pms-solution)
- F3915 · web\_page · Sourced · [https://apaleo\.com/api\-terms\-of\-use](https://apaleo.com/api-terms-of-use)
- F3916 · web\_page · Sourced · [https://apaleo\.com/about\-us](https://apaleo.com/about-us)
- F3917 · web\_page · Sourced · [https://apaleo\.com/customer\-stories/home](https://apaleo.com/customer-stories/home)
- F3918 · web\_page · Sourced · [https://apaleo\.com/changelog](https://apaleo.com/changelog)
- F3919 · web\_page · Sourced · [https://apaleo\.com/sign\-up\-for\-community\-customer](https://apaleo.com/sign-up-for-community-customer)
- F3920 · web\_page · Sourced · [https://apaleo\.com/customer\-stories/hotel\-groups\-chains/apaleo\-and\-THE\-FLAG\-bring\-agentic\-AI\-into\-live\-hotel\-operations](https://apaleo.com/customer-stories/hotel-groups-chains/apaleo-and-THE-FLAG-bring-agentic-AI-into-live-hotel-operations)
- F3921 · web\_page · Sourced · [https://apaleo\.com/company\-culture/home](https://apaleo.com/company-culture/home)
- F3922 · web\_page · Sourced · [https://apaleo\.com/company\-culture/origin\-stories/maria\-ritzer](https://apaleo.com/company-culture/origin-stories/maria-ritzer)
- F3923 · web\_page · Sourced · [https://apaleo\.com/events](https://apaleo.com/events)
- F3924 · web\_page · Sourced · [https://apaleo\.com/blog/industry\-trends/autonomous\-hotel](https://apaleo.com/blog/industry-trends/autonomous-hotel)
- F3925 · web\_page · Sourced · [https://apaleo\.com/blog/apaleo\-news/mcp\-server\-adoption](https://apaleo.com/blog/apaleo-news/mcp-server-adoption)
- F3926 · web\_page · Sourced · [https://status\.apaleo\.com/](https://status.apaleo.com/)
- F3927 · web\_page · Sourced · [https://apaleo\.com/book\-a\-demo](https://apaleo.com/book-a-demo)
- F3928 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3929 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3930 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3931 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3932 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3933 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3934 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3935 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3936 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3937 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3938 · job\_post · Sourced · [https://boards\.greenhouse\.io/apaleo](https://boards.greenhouse.io/apaleo)
- F3939 · github\_org · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F3940 · github\_org · Low confidence · [https://apaleo\.com/dpa](https://apaleo.com/dpa)
- F3941 · tech\_stack · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F3942 · tech\_stack · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F3943 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=apaleo\.com&amp;type=MX](https://dns.google/resolve?name=apaleo.com&type=MX)
- F3944 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=apaleo\.com&amp;type=TXT](https://dns.google/resolve?name=apaleo.com&type=TXT)
- F3945 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=apaleo\.com&amp;type=TXT](https://dns.google/resolve?name=apaleo.com&type=TXT)
- F3946 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3947 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3948 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3949 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3950 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3951 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3952 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3953 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3954 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3955 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3956 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3957 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3958 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3959 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3960 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3961 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3962 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3963 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3964 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3965 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3966 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3967 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3968 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3969 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3970 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3971 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3972 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3973 · subdomain · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3974 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.apaleo\.com&amp;output=json](https://crt.sh/?q=%25.apaleo.com&output=json)
- F3975 · github\_org · Sourced · [https://github\.com/apaleo](https://github.com/apaleo)
- F3976 · repo · Sourced · [https://github\.com/apaleo/gsheet\-addon](https://github.com/apaleo/gsheet-addon)
- F3977 · repo · Sourced · [https://github\.com/apaleo/n8n\-nodes\-apaleo](https://github.com/apaleo/n8n-nodes-apaleo)
- F3978 · repo · Sourced · [https://github\.com/apaleo/docker\-resx2cs](https://github.com/apaleo/docker-resx2cs)
- F3979 · paper · Medium confidence · [https://openalex\.org/W7160130889](https://openalex.org/W7160130889)
- F3980 · wayback\_first · Sourced · [https://web\.archive\.org/web/20110210012312/http://apaleo\.com/](https://web.archive.org/web/20110210012312/http://apaleo.com/)
- F3981 · wayback\_first · Sourced · [https://web\.archive\.org/web/20190819144805/https://apaleo\.com/pricing\-2/](https://web.archive.org/web/20190819144805/https://apaleo.com/pricing-2/)
- F3982 · wayback\_first · Sourced · [https://web\.archive\.org/web/20210619091040/https://apaleo\.com/careers/](https://web.archive.org/web/20210619091040/https://apaleo.com/careers/)
- F3983 · wayback\_first · Sourced · [https://web\.archive\.org/web/20230328235253/https://apaleo\.com/blog/apaleo\-news/apaleo\-funding\-round\-series\-a](https://web.archive.org/web/20230328235253/https://apaleo.com/blog/apaleo-news/apaleo-funding-round-series-a)
- F3984 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/apaleo\.com](https://web.archive.org/web/%2A/apaleo.com)
- F3988 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3989 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3990 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3991 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3992 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3993 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3994 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3995 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3996 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3997 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3998 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3999 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4000 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4001 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4002 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4003 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4004 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4005 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4006 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4007 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4008 · source\_unavailable · Unavailable · [https://www\.hospitalitynet\.org/news/4083435\.html](https://www.hospitalitynet.org/news/4083435.html)
- F4009 · press\_mention · Sourced · [https://www\.bakertilly\.de/beitrag/baker\-tilly\-begleitet\-rockaway\-ventures\-und\-serpentine\-ventures\-bei\-investition\-in\-offene\-hospitality\-plattform\-apaleo](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo)
- F4010 · press\_mention · Sourced · [https://finance\.yahoo\.com/news/apaleo\-secures\-21m\-funding\-fuel\-145553468\.html](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html)
- F4011 · press\_mention · Sourced · [https://psgequity\.com/portfolio/apaleo](https://psgequity.com/portfolio/apaleo)
- F4012 · press\_mention · Sourced · [https://www\.privateequityinternational\.com/psg\-leads\-growth\-equity\-funding\-round\-in\-apaleo](https://www.privateequityinternational.com/psg-leads-growth-equity-funding-round-in-apaleo)
- F4013 · source\_unavailable · Unavailable · [https://www\.phocuswire\.com/apaleo\-secures\-20m\-growth\-equity\-investment\-round](https://www.phocuswire.com/apaleo-secures-20m-growth-equity-investment-round)
- F4014 · press\_mention · Sourced · [https://hengeler\-news\.com/en/articles/hengeler\-mueller\-advises\-psg\-equity\-on\-investment\-in\-apaleo](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo)
- F4015 · press\_mention · Sourced · [https://www\.serpentine\.vc/blog/apaleo\-secures\-20m\-growth\-equity\-to\-accelerate\-global\-expansion/](https://www.serpentine.vc/blog/apaleo-secures-20m-growth-equity-to-accelerate-global-expansion/)
- F4016 · press\_mention · Sourced · [https://www\.redalpine\.com/post/redalpine\-invests\-in\-apaleo\-disruptor\-of\-hotel\-management\-software](https://www.redalpine.com/post/redalpine-invests-in-apaleo-disruptor-of-hotel-management-software)
- F4017 · press\_mention · Sourced · [https://www\.serpentine\.vc/blog/why\-serpentine\-ventures\-invested\-in\-apaleo/](https://www.serpentine.vc/blog/why-serpentine-ventures-invested-in-apaleo/)
- F4018 · press\_mention · Sourced · [https://hoteltechnologynews\.com/2024/11/apaleo\-raises\-21\-million\-to\-expand\-its\-hotel\-property\-management\-platform\-built\-on\-api\-first\-architecture](https://hoteltechnologynews.com/2024/11/apaleo-raises-21-million-to-expand-its-hotel-property-management-platform-built-on-api-first-architecture)
- F4019 · press\_mention · Sourced · [https://leadiq\.com/c/apaleo/5a1dac392300005300a16b74](https://leadiq.com/c/apaleo/5a1dac392300005300a16b74)
- F4020 · press\_mention · Sourced · [https://servicedapartmentnews\.com/news/technology/apaleo\-series\-b\-funding\-round/](https://servicedapartmentnews.com/news/technology/apaleo-series-b-funding-round/)
- F4021 · press\_mention · Sourced · [https://realdeals\.eu\.com/article/apaleo\-checks\-in\-to\-20\-million\-psg\-investment](https://realdeals.eu.com/article/apaleo-checks-in-to-20-million-psg-investment)
- F4022 · press\_mention · Sourced · [https://leadiq\.com/c/apaleo/5a1dac392300005300a16b74/employee\-directory?page=4](https://leadiq.com/c/apaleo/5a1dac392300005300a16b74/employee-directory?page=4)
- F4023 · press\_mention · Sourced · [https://cerrano\.com\.br/bula/apaleo](https://cerrano.com.br/bula/apaleo)
- F4024 · press\_mention · Sourced · [https://www\.agrobulas\.com/bula/apaleo\-26023](https://www.agrobulas.com/bula/apaleo-26023)
- F4025 · source\_unavailable · Unavailable · [https://www\.phocuswire\.com/hotelhero\-founders\-exit\-join\-hospitality\-tech\-specialist\-apaleo](https://www.phocuswire.com/hotelhero-founders-exit-join-hospitality-tech-specialist-apaleo)
- F4026 · source\_unavailable · Unavailable · [https://hoteltechreport\.com/operations/property\-management\-systems/apaleo\-pms](https://hoteltechreport.com/operations/property-management-systems/apaleo-pms)
- F4027 · press\_mention · Sourced · [https://www\.munich\-startup\.de/en/startups\-and\-ecosystem/apaleo\-gmbh](https://www.munich-startup.de/en/startups-and-ecosystem/apaleo-gmbh)
- F4028 · press\_mention · Sourced · [https://techround\.co\.uk/interviews/stephan\-wiesener\-founder\-at\-apaleo/](https://techround.co.uk/interviews/stephan-wiesener-founder-at-apaleo/)
- F4029 · press\_mention · Sourced · [https://techround\.co\.uk/techround\-100/33\-apaleo/](https://techround.co.uk/techround-100/33-apaleo/)
- F4030 · press\_mention · Sourced · [https://themodernhotelier\.com/episode/296](https://themodernhotelier.com/episode/296)
- F4031 · source\_unavailable · Unavailable · [https://www\.hospitalityinvestor\.com/technology/hospitality\-startup\-apaleo\-extends\-series\-funding\-round\-eu9m](https://www.hospitalityinvestor.com/technology/hospitality-startup-apaleo-extends-series-funding-round-eu9m)
- F4032 · press\_mention · Sourced · [https://psgequity\.com/news/apaleo\-secures\-20\-million\-growth\-equity\-investment\-led\-by\-psg\-to\-accelerate\-global\-expansion](https://psgequity.com/news/apaleo-secures-20-million-growth-equity-investment-led-by-psg-to-accelerate-global-expansion)
- F4033 · press\_mention · Sourced · [https://cc\.cz/nemci\-modernizuji\-hotely\-startup\-zaujal\-i\-ceske\-rockaway\-podili\-se\-na\-investici\-pres\-200\-milionu/](https://cc.cz/nemci-modernizuji-hotely-startup-zaujal-i-ceske-rockaway-podili-se-na-investici-pres-200-milionu/)
- F6087 · product\_capability · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F6088 · product\_capability · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F6089 · pricing · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F6090 · tech\_claim · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F6091 · tech\_claim · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F6092 · tech\_claim · Medium confidence · [https://apaleo\.com/](https://apaleo.com/)
- F6093 · tech\_claim · Medium confidence · [https://status\.apaleo\.com/](https://status.apaleo.com/)
- F6094 · tech\_claim · Medium confidence · [https://status\.apaleo\.com/](https://status.apaleo.com/)
- F6095 · pricing · Medium confidence · [https://apaleo\.com/pricing](https://apaleo.com/pricing)
- F6096 · pricing · Medium confidence · [https://apaleo\.com/pricing](https://apaleo.com/pricing)
- F6097 · product\_capability · Medium confidence · [https://apaleo\.com/pricing](https://apaleo.com/pricing)
- F6098 · product\_capability · Medium confidence · [https://apaleo\.com/pricing](https://apaleo.com/pricing)
- F6099 · product\_capability · Medium confidence · [https://apaleo\.com/pricing](https://apaleo.com/pricing)
- F6100 · tech\_claim · Medium confidence · [https://apaleo\.com/pricing](https://apaleo.com/pricing)
- F6101 · product\_capability · Medium confidence · [https://apaleo\.com/ai\-powered\-pms\-solution](https://apaleo.com/ai-powered-pms-solution)
- F6102 · product\_capability · Medium confidence · [https://apaleo\.com/ai\-powered\-pms\-solution](https://apaleo.com/ai-powered-pms-solution)
- F6103 · product\_capability · Medium confidence · [https://apaleo\.com/ai\-powered\-pms\-solution](https://apaleo.com/ai-powered-pms-solution)
- F6104 · pricing · Medium confidence · [https://apaleo\.com/api\-terms\-of\-use](https://apaleo.com/api-terms-of-use)
- F6105 · customer · Medium confidence · [https://apaleo\.com/api\-terms\-of\-use](https://apaleo.com/api-terms-of-use)
- F6106 · tech\_claim · Medium confidence · [https://apaleo\.com/api\-terms\-of\-use](https://apaleo.com/api-terms-of-use)
- F6107 · pricing · Medium confidence · [https://apaleo\.com/api\-terms\-of\-use](https://apaleo.com/api-terms-of-use)
- F6108 · tech\_claim · Medium confidence · [https://apaleo\.com/api\-terms\-of\-use](https://apaleo.com/api-terms-of-use)
- F6109 · product\_capability · Medium confidence · [https://apaleo\.com/about\-us](https://apaleo.com/about-us)
- F6110 · product\_capability · Medium confidence · [https://apaleo\.com/about\-us](https://apaleo.com/about-us)
- F6111 · product\_capability · Medium confidence · [https://apaleo\.com/about\-us](https://apaleo.com/about-us)
- F6112 · product\_capability · Medium confidence · [https://apaleo\.com/about\-us](https://apaleo.com/about-us)
- F6113 · tech\_claim · Medium confidence · [https://apaleo\.com/about\-us](https://apaleo.com/about-us)
- F6114 · tech\_claim · Medium confidence · [https://apaleo\.com/about\-us](https://apaleo.com/about-us)
- F6115 · team\_claim · Medium confidence · [https://apaleo\.com/about\-us](https://apaleo.com/about-us)
- F6118 · funding\_round · Medium confidence · [https://www\.bakertilly\.de/beitrag/baker\-tilly\-begleitet\-rockaway\-ventures\-und\-serpentine\-ventures\-bei\-investition\-in\-offene\-hospitality\-plattform\-apaleo](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo)
- F6119 · product\_capability · Medium confidence · [https://www\.bakertilly\.de/beitrag/baker\-tilly\-begleitet\-rockaway\-ventures\-und\-serpentine\-ventures\-bei\-investition\-in\-offene\-hospitality\-plattform\-apaleo](https://www.bakertilly.de/beitrag/baker-tilly-begleitet-rockaway-ventures-und-serpentine-ventures-bei-investition-in-offene-hospitality-plattform-apaleo)
- F6120 · funding\_round · Medium confidence · [https://finance\.yahoo\.com/news/apaleo\-secures\-21m\-funding\-fuel\-145553468\.html](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html)
- F6121 · tech\_claim · Medium confidence · [https://finance\.yahoo\.com/news/apaleo\-secures\-21m\-funding\-fuel\-145553468\.html](https://finance.yahoo.com/news/apaleo-secures-21m-funding-fuel-145553468.html)
- F6122 · product\_capability · Medium confidence · [https://www\.privateequityinternational\.com/psg\-leads\-growth\-equity\-funding\-round\-in\-apaleo](https://www.privateequityinternational.com/psg-leads-growth-equity-funding-round-in-apaleo)
- F6123 · funding\_round · Medium confidence · [https://www\.privateequityinternational\.com/psg\-leads\-growth\-equity\-funding\-round\-in\-apaleo](https://www.privateequityinternational.com/psg-leads-growth-equity-funding-round-in-apaleo)
- F6124 · product\_capability · Medium confidence · [https://hengeler\-news\.com/en/articles/hengeler\-mueller\-advises\-psg\-equity\-on\-investment\-in\-apaleo](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo)
- F6125 · funding\_round · Medium confidence · [https://hengeler\-news\.com/en/articles/hengeler\-mueller\-advises\-psg\-equity\-on\-investment\-in\-apaleo](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo)
- F6126 · tech\_claim · Medium confidence · [https://hengeler\-news\.com/en/articles/hengeler\-mueller\-advises\-psg\-equity\-on\-investment\-in\-apaleo](https://hengeler-news.com/en/articles/hengeler-mueller-advises-psg-equity-on-investment-in-apaleo)
- F6127 · funding\_round · Medium confidence · [https://www\.serpentine\.vc/blog/apaleo\-secures\-20m\-growth\-equity\-to\-accelerate\-global\-expansion/](https://www.serpentine.vc/blog/apaleo-secures-20m-growth-equity-to-accelerate-global-expansion/)
- F6128 · team\_claim · Medium confidence · [https://apaleo\.com/company\-culture/home](https://apaleo.com/company-culture/home)
- F6129 · team\_claim · Medium confidence · [https://apaleo\.com/company\-culture/home](https://apaleo.com/company-culture/home)
- F6130 · team\_claim · Medium confidence · [https://apaleo\.com/company\-culture/home](https://apaleo.com/company-culture/home)
- F6131 · team\_claim · Medium confidence · [https://apaleo\.com/company\-culture/home](https://apaleo.com/company-culture/home)
- F6132 · team\_claim · Medium confidence · [https://apaleo\.com/company\-culture/home](https://apaleo.com/company-culture/home)
- F6133 · team\_claim · Medium confidence · [https://apaleo\.com/company\-culture/home](https://apaleo.com/company-culture/home)
- F6394 · verification · Sourced · [https://apaleo\.com/](https://apaleo.com/)
- F7686 · source\_unavailable · Unavailable · [https://www\.hlidacstatu\.cz/hledat](https://www.hlidacstatu.cz/hledat)
- F7687 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Apaleo%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Apaleo%27)
- F7688 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
