# Duvo — due diligence brief

duvo\.ai · duvo\.ai s\.r\.o\. · IČO 22646141 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** An Enterprise Execution OS selling prebuilt AI agents and process automation to retailers and enterprise operations teams\. *(Corroborated)* ^[1](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/),[2](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/),[3](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html),[4](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- **Stage & traction.** Completed $15M seed \(Dec 2025\) and a $32M Series A \(Oct 2026\), with named customers including Notino and Rohlik and US GTM hires\. *(Corroborated)* ^[5](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/),[6](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us),[7](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html),[4](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us),[8](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- **Technology & moat.** Claims center on process\-mapping at scale plus prebuilt agent skills and integrations; public repos show agent/tooling artifacts but no verified proprietary model IP\. *(Partly verified)* ^[9](https://www.duvo.ai/),[10](https://github.com/duvoai/skills),[11](https://github.com/duvoai/elevenlabs-agents),[2](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/)
- **Key risk.** Security and compliance certifications \(SOC 2/ISO\) and the 'no training on customer data' claim are documented on the site but are marked not\-checkable without private reports\. *(Analyst view)* ^[12](https://www.duvo.ai/pricing),[13](https://www.duvo.ai/)
- **Diligence focus.** First obtain SOC 2/ISO reports and sample audit logs showing agent writebacks to ERPs to confirm security, governance and claimed automation outcomes\. *(Analyst view)* ^[13](https://www.duvo.ai/),[14](https://www.duvo.ai/solutions/purchase-order-compliance),[15](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2025\-12\-02 · seed funding · $15 million · Index Ventures, Credo Ventures, Northzone, Puzzle Ventures, Roy Reznik \(angel\), David Sing; 2026\-10\-14 · Series A · €28\.55 million · Balderton Capital, Index Ventures, Northzone, Credo Ventures · 4 reports | 5, 6, 7, 16, 17 |
| Hiring | 9 open roles: other 2, sales gtm 2, ml research 2, forward deployed 2, engineering 1; European Union, London, United Kingdom, USA, United Kingdom | 18, 19, 20, 21, 22, 23 |
| AI dependency | relies on \(subprocessor / own claims\): Anthropic; own\-model evidence: 0 papers, 0 verified HF models, 2 ML roles, 2 own\-model claims | 24, 25, 12, 22 |
| Engineering footprint | 10 public repos \(14★, last push 2026\-11\-07\); product surfaces: api\.dev\.duvo\.ai, api\.duvo\.ai, api\.stg\.duvo\.ai, app\.dev\.duvo\.ai, app\.duvo\.ai, app\.stg\.duvo\.ai; 3 docs pages; stack: Next\.js | 11, 26, 27, 28, 29, 30 |
| Customers | 2 named: Notino, Rohlik; public pricing: yes | 4, 31, 32, 33 |
| Claims checked | Customer \(Notino, Rohlik\): confirmed; SOC 2 / ISO: not checkable | 34, 35, 13 |
| Timeline | Czech entity registered 2025\-02\-24; first press 2025\-12\-02 \(22 articles collected\) | 36, 37 |

# Detailed findings

## Ownership and capital

- Seed funding: $15M seed reported Dec 2, 2025 led by Index Ventures with Credo, Northzone, Puzzle and angels\. *(Single source)* ^[5](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/)
  - Assumption: Press reporting accurately reflects the round\.
- Series A: reported Oct 14, 2026 as €28\.55M / $32M led by Balderton with Index, Northzone and Credo participating\. *(Corroborated)* ^[6](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us),[7](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html),[17](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
  - Assumption: Media conversions between EUR and USD approximate reported totals\.
- Company registry: incorporated 2025\-02\-24 in Prague as duvo\.ai s\.r\.o\.; early shareholder Bizthusiasm then Taskcrew Inc\. holds 100% from 2025\-08\-01\. *(Verified)* ^[36](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22646141),[38](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141),[39](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141)
  - Assumption: Registry extracts reflect current filings\.

## Technology profile

- Product surfaces and docs: public developer docs and API reference exist \(developers, api\-reference, authentication pages\)\. *(Company claim)* ^[40](https://www.duvo.ai/developers),[41](https://www.duvo.ai/developers/api-reference),[42](https://www.duvo.ai/developers/authentication)
- Capabilities: process discovery \(Clarity\), exporting BPMN/Visio, prebuilt retail agent skills and multi\-system automation with writeback to source systems\. *(Partly verified)* ^[9](https://www.duvo.ai/),[43](https://www.duvo.ai/platform),[2](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/),[14](https://www.duvo.ai/solutions/purchase-order-compliance)
- Engineering footprint: 10\+ public repos \(including skills, agent integrations\) and many product subdomains and sandbox/staging surfaces\. *(Verified)* ^[44](https://github.com/duvoai),[10](https://github.com/duvoai/skills),[11](https://github.com/duvoai/elevenlabs-agents),[29](https://crt.sh/?q=%25.duvo.ai&output=json)

## Rebuild check

- **Commodity:** Process\-mapping interview flow and simple agent runs — rebuildable by a 2–3 person team in weeks using public APIs and the Free plan and SDK artifacts\. *(Analyst view)* ^[9](https://www.duvo.ai/),[45](https://www.duvo.ai/),[10](https://github.com/duvoai/skills)
  - Assumption: Team uses public SDKs and available OSS agent patterns\.
- **Hard to copy:** Enterprise\-grade ERP writeback, audited governance, and multi\-system authorized agents integrated at scale — evidence includes writeback claims, enterprise customers and audit/governance statements\. *(Analyst view)* ^[14](https://www.duvo.ai/solutions/purchase-order-compliance),[15](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/),[4](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
  - Assumption: Enterprise integrations require bespoke connectors and trust\.
- **Verdict:** Quarter — a competent startup could clone basic mapping and agents in a month, but a clone would lack verified SOC/ISO evidence, enterprise audit logs and installed customer integrations\. *(Analyst view)* ^[9](https://www.duvo.ai/),[13](https://www.duvo.ai/),[14](https://www.duvo.ai/solutions/purchase-order-compliance)
  - Assumption: Access to target customers and audits is time\-consuming\.

## Risks and caveats

- Unverified security claims: SOC 2 / ISO claims exist on the site but independent attestation not found; SOC 2 reports are private per verification\. *(Analyst view)* ^[12](https://www.duvo.ai/pricing),[13](https://www.duvo.ai/)
- Model\-provider dependency: trust portal lists Anthropic as a subprocessor, indicating reliance on an external LLM vendor for parts of the stack\. *(Analyst view)* ^[24](https://www.duvo.ai/trust-center),[46](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)

## Questions for founders

- Please produce SOC 2 Type II and ISO 27001/42001 audit reports and redacted SOC evidence referenced on site \(verification cites not\_checkable\)\. *(Analyst view)* ^[13](https://www.duvo.ai/),[12](https://www.duvo.ai/pricing)
- Provide sample audit logs and a recorded demo showing agent writeback to a live ERP and the governance workflow that approves writes \(site claims writeback\)\. *(Analyst view)* ^[14](https://www.duvo.ai/solutions/purchase-order-compliance),[15](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/)
- Substantiate the customer value claim \(&gt;$100M annual value\) with contract\-level outcomes or measurable ROI per customer referenced on Wired\. *(Analyst view)* ^[47](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi),[4](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- Clarify Anthropic dependency and fallback: which providers are used in production, and can customers host models on\-prem or in their own cloud \(site lists Anthropic and 'model\-agnostic'\)\. *(Analyst view)* ^[24](https://www.duvo.ai/trust-center),[46](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)

## Sources

1. [tech\.eu](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/) · Independent press · Product capability — “Duvo is an enterprise operating system that brings a company's processes together on one platform\.”
2. [tech\.eu](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/) · Independent press · Product capability — “The platform ships with ready\-made AI assistants for tasks such as weekly margin reviews, activating promotions and price changes, reconciling supplier invoices, assortment optimisation and vendor onboarding\.”
3. [finance\.yahoo\.com](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html) · Independent press · Product capability — “Duvo's agents then run the approved steps across ERPs, supplier portals, spreadsheets and inboxes, through APIs where they exist and through the same screens people use where they don't\.”
4. [therecursive\.com](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us) · Independent press · Customer — “Duvo's customers include Notino, Morrisons, Holland &amp; Barrett, Boden and Allegro, as well as Rohlik itself”
5. [tech\.eu](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/) · Independent press · Funding round — “Duvo , an AI\-native automation platform that gives retail teams an AI workforce for day\-to\-day operations, has raised $15 million in seed funding\.”
6. [therecursive\.com](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us) · Independent press · Funding round — “has raised a €28\.55 million \($32 million\) Series A led by Balderton Capital\.”
7. [finance\.yahoo\.com](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html) · Independent press · Funding round — “Duvo today announced a $32 million Series A led by Balderton Capital, with participation from existing investors Index Ventures, Northzone and Credo Ventures\.”
8. [therecursive\.com](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us) · Independent press · Team claim — “Duvo has also hired two US executives: Michael Green, who joins from Databricks to lead go\-to\-market after a similar role at Salesforce, and Spencer Insolia, former President of Kmart and Managing Director at Accenture, who becomes Managing Director for the US\.”
9. [duvo\.ai](https://www.duvo.ai/) · Company's own website · Product capability — “Duvo Clarity maps a process from 10\-minute AI interviews with the people who do the work, in 177\+ languages, while they share their screens\.”
10. [github\.com](https://github.com/duvoai/skills) · Public technical artifact · GitHub repository · 2026\-11\-07 — “duvoai/skills · Official agent skills for Duvo — automate operations with AI agents across your existing systems · last push 2026\-11\-07”
11. [github\.com](https://github.com/duvoai/elevenlabs-agents) · Public technical artifact · GitHub repository · 2025\-11\-25 — “duvoai/elevenlabs\-agents · Complete toolkit for integrating ElevenLabs Conversational AI agents with Claude Code \- includes skill definition and MCP server · TypeScript · last push 2025\-11\-25”
12. [duvo\.ai](https://www.duvo.ai/pricing) · Company's own website · Technical claim — “Duvo holds SOC 2 Type II, ISO 27001, and ISO 42001, supports GDPR requirements, and operates in line with NIS2\. Enterprise adds SSO and audit logs, and Duvo does not train its own or third\-party models on customer data\.”
13. [duvo\.ai](https://www.duvo.ai/) · Company's own website · Independent check of a claim — “No trust portal, auditor or compliance\-platform reference found on the collected security pages or subdomains\. SOC 2 reports are private; the claim can only be verified by requesting the report\.”
14. [duvo\.ai](https://www.duvo.ai/solutions/purchase-order-compliance) · Company's own website · Product capability — “The corrected fields and approval status are written back to the purchasing system before the PO proceeds\.”
15. [tech\.eu](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/) · Independent press · Technical claim — “Its agents act directly within retailers’ systems to carry out tasks autonomously, supported by governance features, audit trails, security controls and user management\.”
16. [wired\.cz](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi) · Independent press · Funding round — “čímž celkové financování firmy vzrostlo na 48 milionů dolarů\.”
17. [tech\.eu](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/) · Independent press · Funding round — “Duvo today announced a $32 million Series A led by Balderton Capital, with participation from existing investors Index Ventures, Northzone, and Credo Ventures\.”
18. [duvo\.ai](https://www.duvo.ai/careers/talent-partner-eu-uk-based-remote) · Company's own website · Job posting — “Talent Partner \(EU/UK Based \- Remote\)\. · London, United Kingdom”
19. [jobs\.ashbyhq\.com](https://jobs.ashbyhq.com/duvo/f3e6bcd3-6539-4677-b2ad-3eceb0582857/application) · Company's own website · Job posting — “Talent Partner \(EU/UK Based \- Remote\) · London, United Kingdom”
20. [duvo\.ai](https://www.duvo.ai/careers/sales-development-representative-us-remote) · Company's own website · Job posting — “Sales Development Representative \(US \- Remote\)\. · USA”
21. [jobs\.ashbyhq\.com](https://jobs.ashbyhq.com/duvo/3f2a755c-d6a2-4e33-a212-a1bb898bca00/application) · Company's own website · Job posting — “Sales Development Representative \(US \- Remote\) · USA”
22. [duvo\.ai](https://www.duvo.ai/careers/ai-platform-engineer-eu-uk-based-remote) · Company's own website · Job posting — “AI Platform Engineer \(EU/UK Based \- Remote\)\. · European Union”
23. [jobs\.ashbyhq\.com](https://jobs.ashbyhq.com/duvo/a1e5cdbc-6159-4895-8dae-cf71196550fa/application) · Company's own website · Job posting — “AI Platform Engineer \(EU/UK Based \- Remote\) · European Union”
24. [duvo\.ai](https://www.duvo.ai/trust-center) · Company's own website · Subprocessor \(privacy policy\) — “Duvo does not train its own or third\-party models on customer data\. The trust portal lists an Anthropic zero\-data\-retention certificate, available for review on request\. Retention depends on the selected provider, endpoint and configuration; agree those terms for your deployment\. Model\-provider retention is separate fr…”
25. [duvo\.ai](https://www.duvo.ai/) · Company's own website · Technical claim — “No\. Duvo does not train its own or third\-party models on customer data\. It holds SOC 2 Type II, ISO 27001 and ISO 42001 and supports GDPR requirements\.”
26. [github\.com](https://github.com/duvoai/cua-mcp-server) · Public technical artifact · GitHub repository · 2025\-12\-17 — “duvoai/cua\-mcp\-server · Agentic MCP server for CUA Cloud \- delegate desktop automation tasks to autonomous vision\-based agents · TypeScript · last push 2025\-12\-17”
27. [github\.com](https://github.com/duvoai/pii-guardrails-plugin) · Public technical artifact · GitHub repository · 2026\-02\-07 — “duvoai/pii\-guardrails\-plugin · Python · last push 2026\-02\-07”
28. [crt\.sh](https://crt.sh/?q=%25.duvo.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-08\-26 — “app\.duvo\.ai \(first certificate 2025\-08\-26\)”
29. [crt\.sh](https://crt.sh/?q=%25.duvo.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-09\-12 — “api\.duvo\.ai \(first certificate 2025\-09\-12\)”
30. [crt\.sh](https://crt.sh/?q=%25.duvo.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-11\-17 — “docs\.duvo\.ai \(first certificate 2025\-11\-17\)”
31. [finance\.yahoo\.com](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html) · Independent press · Customer — “At Notino, Europe's largest online beauty retailer, those results span finance, customer care and marketing\.”
32. [tech\.eu](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/) · Independent press · Customer — “Rohlik subsequently became a Duvo customer, and Čupr credits the technology with contributing to its operational transformation\.”
33. [duvo\.ai](https://www.duvo.ai/) · Company's own website · Pricing — “Process discovery · Free Map one business process, free\. Duvo interviews the people who do the work and maps what really happens, in two weeks\. Clarity Invoice reconciliation – Overpaid invoices Share Current process Transformation proposal Automation Completed Edit mode”
34. [therecursive\.com](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us) · Independent press · Independent check of a claim — “Duvo's customers include Notino, Morrisons, Holland &amp; Barrett, Boden and Allegro, as well as Rohlik itself\. At Czech online beauty retailer Notino, the company says, the quarterly reconciliation of around $45 million in annual supplier bonuses went from 70 days to 15, and the specialist time needed”
35. [therecursive\.com](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us) · Independent press · Independent check of a claim — “Duvo, the Prague\-based enterprise AI company founded by Rohlik Group founder and CEO Tomáš Čupr, has raised a €28\.55 million \($32 million\) Series A led by Balderton Capital\. Existing investors Index Ventures, Northzone and Credo Ventures also joined the round, bringing Duvo's total funding to €43 mi”
36. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22646141) · Official record · Registry: incorporation · 2025\-02\-24 — “registered 2025\-02\-24”
37. [tech\.eu](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/) · Independent press · Press article · 2025\-12\-02 — “Duvo raises $15M to give retailers AI staff that cuts manual work by 40% \- Tech\.eu”
38. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141) · Official record · Registry: shareholder · 2025\-02\-24 — “Bizthusiasm, a\.s\. · 33\.33% · from 2025\-02\-24 · to 2025\-08\-01”
39. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141) · Official record · Registry: shareholder · 2025\-08\-01 — “Taskcrew Inc\. · 100\.0% · from 2025\-08\-01”
40. [duvo\.ai](https://www.duvo.ai/developers) · Company's own website · Website page — “Developer platform: production runtime for agents \- Duvo”
41. [duvo\.ai](https://www.duvo.ai/developers/api-reference) · Company's own website · Website page — “Duvo API Reference \- Duvo Developer Platform”
42. [duvo\.ai](https://www.duvo.ai/developers/authentication) · Company's own website · Website page — “Duvo Authentication \- Duvo Developer Platform”
43. [duvo\.ai](https://www.duvo.ai/platform) · Company's own website · Product capability — “Process maps export as BPMN 2\.0 XML or native Visio drawings\.”
44. [github\.com](https://github.com/duvoai) · Public technical artifact · GitHub organisation · 2025\-03\-05 — “duvoai · 13 public repos”
45. [duvo\.ai](https://www.duvo.ai/) · Company's own website · Pricing — “Or start on your own: the Free plan at app\.duvo\.ai includes 2 Clarity interviews and 100 agent runs\. Start free”
46. [therecursive\.com](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us) · Independent press · Technical claim — “The platform is model\-agnostic and can run open\-weight models on dedicated GPUs or models hosted by the customer\.”
47. [wired\.cz](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi) · Independent press · Technical claim — “Platformu už využívají velké značky, kterým ročně generuje hodnotu přesahující 100 milionů dolarů\.”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 12 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 22 | press:citybiz\.co, press:finsmes\.com, press:techfundingnews\.com, press:theintelligent\.cz |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 44 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 53 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 11 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 1 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 5 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 3 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 60 | — |

Analysis: gpt\-5\-mini (cost $0.0095); AI extraction cost $0.0080. Full fact table: CSV export.

## Source appendix (all collected facts)

- F2697 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/22646141](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22646141)
- F2698 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/22646141](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22646141)
- F2699 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/22646141](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141)
- F2700 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/22646141](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141)
- F2701 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/22646141](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141)
- F2702 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/22646141](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141)
- F2703 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/22646141](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141)
- F2704 · registry\_flag · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/22646141](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22646141)
- F2705 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1267923](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1267923)
- F2706 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1267923](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1267923)
- F2707 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1267923](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1267923)
- F2708 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=22646141&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=22646141&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F2709 · web\_page · Sourced · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F2710 · web\_page · Sourced · [https://www\.duvo\.ai/careers](https://www.duvo.ai/careers)
- F2711 · web\_page · Sourced · [https://www\.duvo\.ai/privacy](https://www.duvo.ai/privacy)
- F2712 · subprocessor · Medium confidence · [https://www\.duvo\.ai/privacy](https://www.duvo.ai/privacy)
- F2713 · web\_page · Sourced · [https://www\.duvo\.ai/cookie\-policy](https://www.duvo.ai/cookie-policy)
- F2714 · subprocessor · Medium confidence · [https://www\.duvo\.ai/cookie\-policy](https://www.duvo.ai/cookie-policy)
- F2715 · subprocessor · Medium confidence · [https://www\.duvo\.ai/cookie\-policy](https://www.duvo.ai/cookie-policy)
- F2716 · web\_page · Sourced · [https://www\.duvo\.ai/careers/talent\-partner\-eu\-uk\-based\-remote](https://www.duvo.ai/careers/talent-partner-eu-uk-based-remote)
- F2717 · web\_page · Sourced · [https://jobs\.ashbyhq\.com/duvo/f3e6bcd3\-6539\-4677\-b2ad\-3eceb0582857/application](https://jobs.ashbyhq.com/duvo/f3e6bcd3-6539-4677-b2ad-3eceb0582857/application)
- F2718 · web\_page · Sourced · [https://www\.duvo\.ai/careers/sales\-development\-representative\-us\-remote](https://www.duvo.ai/careers/sales-development-representative-us-remote)
- F2719 · web\_page · Sourced · [https://jobs\.ashbyhq\.com/duvo/3f2a755c\-d6a2\-4e33\-a212\-a1bb898bca00/application](https://jobs.ashbyhq.com/duvo/3f2a755c-d6a2-4e33-a212-a1bb898bca00/application)
- F2720 · web\_page · Sourced · [https://www\.duvo\.ai/careers/ai\-platform\-engineer\-eu\-uk\-based\-remote](https://www.duvo.ai/careers/ai-platform-engineer-eu-uk-based-remote)
- F2721 · web\_page · Sourced · [https://jobs\.ashbyhq\.com/duvo/a1e5cdbc\-6159\-4895\-8dae\-cf71196550fa/application](https://jobs.ashbyhq.com/duvo/a1e5cdbc-6159-4895-8dae-cf71196550fa/application)
- F2722 · web\_page · Sourced · [https://www\.duvo\.ai/careers/forward\-deployed\-engineer\-uk\-based](https://www.duvo.ai/careers/forward-deployed-engineer-uk-based)
- F2723 · web\_page · Sourced · [https://jobs\.ashbyhq\.com/duvo/e2156092\-50f1\-4181\-87fb\-9e4bc299dde3/application](https://jobs.ashbyhq.com/duvo/e2156092-50f1-4181-87fb-9e4bc299dde3/application)
- F2724 · web\_page · Sourced · [https://www\.duvo\.ai/careers/site\-reliability\-engineer\-eu\-uk\-based\-remote](https://www.duvo.ai/careers/site-reliability-engineer-eu-uk-based-remote)
- F2725 · web\_page · Sourced · [https://www\.duvo\.ai/platform](https://www.duvo.ai/platform)
- F2726 · web\_page · Sourced · [https://www\.duvo\.ai/solutions](https://www.duvo.ai/solutions)
- F2727 · web\_page · Sourced · [https://www\.duvo\.ai/trust\-center](https://www.duvo.ai/trust-center)
- F2728 · subprocessor · Medium confidence · [https://www\.duvo\.ai/trust\-center](https://www.duvo.ai/trust-center)
- F2729 · web\_page · Sourced · [https://www\.duvo\.ai/automation](https://www.duvo.ai/automation)
- F2730 · web\_page · Sourced · [https://www\.duvo\.ai/industries](https://www.duvo.ai/industries)
- F2731 · web\_page · Sourced · [https://www\.duvo\.ai/pricing](https://www.duvo.ai/pricing)
- F2732 · web\_page · Sourced · [https://www\.duvo\.ai/developers](https://www.duvo.ai/developers)
- F2733 · web\_page · Sourced · [https://www\.duvo\.ai/offers/process\-discovery](https://www.duvo.ai/offers/process-discovery)
- F2734 · web\_page · Sourced · [https://www\.duvo\.ai/offers/freight\-audit](https://www.duvo.ai/offers/freight-audit)
- F2735 · web\_page · Sourced · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F2736 · web\_page · Sourced · [https://www\.duvo\.ai/solutions/store\-operations\-compliance](https://www.duvo.ai/solutions/store-operations-compliance)
- F2737 · web\_page · Sourced · [https://www\.duvo\.ai/developers/api\-reference](https://www.duvo.ai/developers/api-reference)
- F2738 · web\_page · Sourced · [https://www\.duvo\.ai/developers/authentication](https://www.duvo.ai/developers/authentication)
- F2739 · web\_page · Sourced · [https://www\.duvo\.ai/company](https://www.duvo.ai/company)
- F2740 · web\_page · Sourced · [https://www\.duvo\.ai/customer\-stories](https://www.duvo.ai/customer-stories)
- F2741 · web\_page · Sourced · [https://www\.duvo\.ai/culture](https://www.duvo.ai/culture)
- F2742 · web\_page · Sourced · [https://www\.duvo\.ai/solutions/customer\-complaint\-management](https://www.duvo.ai/solutions/customer-complaint-management)
- F2743 · job\_post · Sourced · [https://www\.duvo\.ai/careers/talent\-partner\-eu\-uk\-based\-remote](https://www.duvo.ai/careers/talent-partner-eu-uk-based-remote)
- F2744 · job\_post · Sourced · [https://jobs\.ashbyhq\.com/duvo/f3e6bcd3\-6539\-4677\-b2ad\-3eceb0582857/application](https://jobs.ashbyhq.com/duvo/f3e6bcd3-6539-4677-b2ad-3eceb0582857/application)
- F2745 · job\_post · Sourced · [https://www\.duvo\.ai/careers/sales\-development\-representative\-us\-remote](https://www.duvo.ai/careers/sales-development-representative-us-remote)
- F2746 · job\_post · Sourced · [https://jobs\.ashbyhq\.com/duvo/3f2a755c\-d6a2\-4e33\-a212\-a1bb898bca00/application](https://jobs.ashbyhq.com/duvo/3f2a755c-d6a2-4e33-a212-a1bb898bca00/application)
- F2747 · job\_post · Sourced · [https://www\.duvo\.ai/careers/ai\-platform\-engineer\-eu\-uk\-based\-remote](https://www.duvo.ai/careers/ai-platform-engineer-eu-uk-based-remote)
- F2748 · job\_post · Sourced · [https://jobs\.ashbyhq\.com/duvo/a1e5cdbc\-6159\-4895\-8dae\-cf71196550fa/application](https://jobs.ashbyhq.com/duvo/a1e5cdbc-6159-4895-8dae-cf71196550fa/application)
- F2749 · job\_post · Sourced · [https://www\.duvo\.ai/careers/forward\-deployed\-engineer\-uk\-based](https://www.duvo.ai/careers/forward-deployed-engineer-uk-based)
- F2750 · job\_post · Sourced · [https://jobs\.ashbyhq\.com/duvo/e2156092\-50f1\-4181\-87fb\-9e4bc299dde3/application](https://jobs.ashbyhq.com/duvo/e2156092-50f1-4181-87fb-9e4bc299dde3/application)
- F2751 · job\_post · Sourced · [https://www\.duvo\.ai/careers/site\-reliability\-engineer\-eu\-uk\-based\-remote](https://www.duvo.ai/careers/site-reliability-engineer-eu-uk-based-remote)
- F2752 · github\_org · Medium confidence · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F2753 · tech\_stack · Medium confidence · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F2754 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=duvo\.ai&amp;type=MX](https://dns.google/resolve?name=duvo.ai&type=MX)
- F2755 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=duvo\.ai&amp;type=TXT](https://dns.google/resolve?name=duvo.ai&type=TXT)
- F2756 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2757 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2758 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2759 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2760 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2761 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2762 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2763 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2764 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2765 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2766 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2767 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2768 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2769 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2770 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2771 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2772 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2773 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2774 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2775 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2776 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2777 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2778 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2779 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2780 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2781 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2782 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2783 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2784 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2785 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2786 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2787 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2788 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2789 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2790 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2791 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2792 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2793 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2794 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2795 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2796 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2797 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2798 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2799 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2800 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2801 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2802 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2803 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2804 · subdomain · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2805 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.duvo\.ai&amp;output=json](https://crt.sh/?q=%25.duvo.ai&output=json)
- F2806 · github\_org · Sourced · [https://github\.com/duvoai](https://github.com/duvoai)
- F2807 · repo · Sourced · [https://github\.com/duvoai/skills](https://github.com/duvoai/skills)
- F2808 · repo · Sourced · [https://github\.com/duvoai/\.github](https://github.com/duvoai/.github)
- F2809 · repo · Sourced · [https://github\.com/duvoai/autodesign](https://github.com/duvoai/autodesign)
- F2810 · repo · Sourced · [https://github\.com/duvoai/mintlify\-docs](https://github.com/duvoai/mintlify-docs)
- F2811 · repo · Sourced · [https://github\.com/duvoai/hubspot\-crm\-mcp](https://github.com/duvoai/hubspot-crm-mcp)
- F2812 · repo · Sourced · [https://github\.com/duvoai/agent\-badge](https://github.com/duvoai/agent-badge)
- F2813 · repo · Sourced · [https://github\.com/duvoai/skill\-factory](https://github.com/duvoai/skill-factory)
- F2814 · repo · Sourced · [https://github\.com/duvoai/pii\-guardrails\-plugin](https://github.com/duvoai/pii-guardrails-plugin)
- F2815 · repo · Sourced · [https://github\.com/duvoai/cua\-mcp\-server](https://github.com/duvoai/cua-mcp-server)
- F2816 · repo · Sourced · [https://github\.com/duvoai/elevenlabs\-agents](https://github.com/duvoai/elevenlabs-agents)
- F2817 · hf\_model · Identity unverified · [https://huggingface\.co/duvo/test](https://huggingface.co/duvo/test)
- F2818 · wayback\_first · Sourced · [https://web\.archive\.org/web/20250929195126/https://www\.duvo\.ai/](https://web.archive.org/web/20250929195126/https://www.duvo.ai/)
- F2819 · wayback\_first · Sourced · [https://web\.archive\.org/web/20260922060623/https://www\.duvo\.ai/pricing](https://web.archive.org/web/20260922060623/https://www.duvo.ai/pricing)
- F2820 · wayback\_first · Sourced · [https://web\.archive\.org/web/20251202100226/https://www\.duvo\.ai/careers](https://web.archive.org/web/20251202100226/https://www.duvo.ai/careers)
- F2821 · wayback\_first · Sourced · [https://web\.archive\.org/web/20250929214455/https://www\.duvo\.ai/blog](https://web.archive.org/web/20250929214455/https://www.duvo.ai/blog)
- F2822 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/duvo\.ai](https://web.archive.org/web/%2A/duvo.ai)
- F2827 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2828 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2829 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2830 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2831 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2832 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2833 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2834 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2835 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2836 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2837 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2838 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2839 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2840 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2841 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2842 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2843 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2844 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2845 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F2846 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F2847 · press\_mention · Sourced · [https://tech\.eu/2025/12/02/duvo\-raises\-15m\-to\-give\-retailers\-ai\-staff\-that\-cuts\-manual\-work\-by\-40/](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/)
- F2848 · press\_mention · Sourced · [https://www\.therecursive\.com/rohlik\-founder\-tomas\-cuprs\-duvo\-raises\-eur28\-7m\-series\-a\-to\-take\-enterprise\-ai\-agents\-to\-the\-us](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- F2849 · press\_mention · Sourced · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F2850 · press\_mention · Sourced · [https://www\.wired\.cz/news\-beat/cuprovo\-duvo\-ziskalo\-32\-milionu\-dolaru\-na\-expanzi](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi)
- F2851 · press\_mention · Sourced · [https://tech\.eu/2026/10/14/from\-rohlik\-to\-enterprise\-ai\-tomas\-cuprs\-duvo\-raises\-32m\-series\-a/](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
- F2852 · press\_mention · Sourced · [https://www\.tcfcap\.com/stories/duvo\-uz\-ma\-od\-investoru\-pres\-miliardu\-korun\-ai\-startup\-tomase\-cupra\-miri\-automatizovat\-podniky\-do\-usa](https://www.tcfcap.com/stories/duvo-uz-ma-od-investoru-pres-miliardu-korun-ai-startup-tomase-cupra-miri-automatizovat-podniky-do-usa)
- F2853 · press\_mention · Sourced · [https://media24\.cz/article/duvo\-ai\-nabira\-od\-investoru\-skoro\-tri\-ctvrte\-miliardy\-bezesporu\-muze\-byt\-vetsi\-nez\-rohlik\-rika\-cupr](https://media24.cz/article/duvo-ai-nabira-od-investoru-skoro-tri-ctvrte-miliardy-bezesporu-muze-byt-vetsi-nez-rohlik-rika-cupr)
- F2854 · press\_mention · Sourced · [https://cc\.cz/tomas\-cupr\-ma\-novy\-ai\-startup\-pres\-340\-milionu\-od\-investoru\-a\-hlasi\-vyresime\-to\-co\-firmy\-brzdi/](https://cc.cz/tomas-cupr-ma-novy-ai-startup-pres-340-milionu-od-investoru-a-hlasi-vyresime-to-co-firmy-brzdi/)
- F2855 · press\_mention · Sourced · [https://www\.aiforbusinessinstitute\.com/news/duvo\-secures\-32m\-to\-operationalise\-enterprise\-ai](https://www.aiforbusinessinstitute.com/news/duvo-secures-32m-to-operationalise-enterprise-ai)
- F2856 · source\_unavailable · Unavailable · [https://theintelligent\.cz/technologie/2026/cesky\-startup\-duvo\-ziskal\-misto\-v\-exkluzivnim\-programu\-microsoft\-pegasus](https://theintelligent.cz/technologie/2026/cesky-startup-duvo-ziskal-misto-v-exkluzivnim-programu-microsoft-pegasus)
- F2857 · press\_mention · Sourced · [https://pulse2\.com/duvo\-raises\-32\-million\-series\-a](https://pulse2.com/duvo-raises-32-million-series-a)
- F2858 · press\_mention · Sourced · [https://www\.remio\.ai/post/duvo\-series\-a\-raises\-32m\-but\-the\-hard\-problem\-is\-hidden\-work](https://www.remio.ai/post/duvo-series-a-raises-32m-but-the-hard-problem-is-hidden-work)
- F2859 · source\_unavailable · Unavailable · [https://www\.citybiz\.co/article/918388/duvo\-raises\-32m\-series\-a\-led\-by\-balderton\-capital\-appoints\-michael\-green\-and\-spencer\-insolia](https://www.citybiz.co/article/918388/duvo-raises-32m-series-a-led-by-balderton-capital-appoints-michael-green-and-spencer-insolia)
- F2860 · press\_mention · Sourced · [https://www\.fundedstartupsdaily\.com/company/duvo](https://www.fundedstartupsdaily.com/company/duvo)
- F2861 · press\_mention · Sourced · [https://www\.goodwinlaw\.com/en/news\-and\-events/news/2026/10/announcements\-technology\-goodwin\-advises\-duvo\-32\-million\-series\-a](https://www.goodwinlaw.com/en/news-and-events/news/2026/10/announcements-technology-goodwin-advises-duvo-32-million-series-a)
- F2862 · press\_mention · Sourced · [https://stros\.co\.uk/duvo\-series\-a](https://stros.co.uk/duvo-series-a)
- F2863 · press\_mention · Sourced · [https://theweightedaverage\.com/notes/2026\-10\-14\-duvo\-32m\-retail\-operations/](https://theweightedaverage.com/notes/2026-10-14-duvo-32m-retail-operations/)
- F2864 · source\_unavailable · Unavailable · [https://www\.finsmes\.com/2025/12/duvo\-raises\-15m\-in\-seed\-funding\.html](https://www.finsmes.com/2025/12/duvo-raises-15m-in-seed-funding.html)
- F2865 · source\_unavailable · Unavailable · [https://techfundingnews\.com/duvo\-ai\-retail\-automation\-seed\-funding](https://techfundingnews.com/duvo-ai-retail-automation-seed-funding)
- F2866 · press\_mention · Sourced · [https://tomascupr\.substack\.com/p/why\-i\-co\-founded\-duvoai](https://tomascupr.substack.com/p/why-i-co-founded-duvoai)
- F2867 · press\_mention · Sourced · [https://futurum\.media/duvo\-ai\-raises\-15\-million\-to\-automate\-retails\-manual\-chaos/](https://futurum.media/duvo-ai-raises-15-million-to-automate-retails-manual-chaos/)
- F2868 · press\_mention · Sourced · [https://www\.tcfcap\.com/en\-us/stories/duvo\-have\-raised\-15\-million\-seed\-round\-to\-give\-retail\-teams\-an\-ai\-workforce\-that\-goes\-live\-in\-weeks](https://www.tcfcap.com/en-us/stories/duvo-have-raised-15-million-seed-round-to-give-retail-teams-an-ai-workforce-that-goes-live-in-weeks)
- F2869 · press\_mention · Sourced · [https://retailtechinnovationhub\.com/home/2025/12/1/ai\-tech\-powered\-workforce\-duvo\-raises\-15\-million\-in\-index\-ventures\-led\-seed\-funding\-round](https://retailtechinnovationhub.com/home/2025/12/1/ai-tech-powered-workforce-duvo-raises-15-million-in-index-ventures-led-seed-funding-round)
- F2870 · press\_mention · Sourced · [https://www\.thesaasnews\.com/news/duvo\-raises\-15\-million\-seed\-round/](https://www.thesaasnews.com/news/duvo-raises-15-million-seed-round/)
- F2871 · press\_mention · Sourced · [https://consumerequitypartners\.com/news/2026/09/22/4/](https://consumerequitypartners.com/news/2026/09/22/4/)
- F2872 · press\_mention · Sourced · [https://www\.scalablepod\.it/en/startup/duvo](https://www.scalablepod.it/en/startup/duvo)
- F5474 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/hledat?Q=ico%3A22646141](https://www.hlidacstatu.cz/hledat?Q=ico%3A22646141)
- F5475 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/dotace/hledat?Q=ico%3A22646141](https://www.hlidacstatu.cz/dotace/hledat?Q=ico%3A22646141)
- F5476 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Duvo%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Duvo%27)
- F5477 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F5742 · tech\_claim · Medium confidence · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F5743 · team\_claim · Medium confidence · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F5744 · pricing · Medium confidence · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F5745 · pricing · Medium confidence · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F5746 · product\_capability · Medium confidence · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F5747 · pricing · Medium confidence · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F5748 · tech\_claim · Medium confidence · [https://www\.duvo\.ai/pricing](https://www.duvo.ai/pricing)
- F5749 · product\_capability · Medium confidence · [https://www\.duvo\.ai/platform](https://www.duvo.ai/platform)
- F5750 · product\_capability · Medium confidence · [https://www\.duvo\.ai/platform](https://www.duvo.ai/platform)
- F5751 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions](https://www.duvo.ai/solutions)
- F5752 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions](https://www.duvo.ai/solutions)
- F5753 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions](https://www.duvo.ai/solutions)
- F5754 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions](https://www.duvo.ai/solutions)
- F5755 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions](https://www.duvo.ai/solutions)
- F5756 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions](https://www.duvo.ai/solutions)
- F5757 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F5758 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F5759 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F5760 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F5761 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F5762 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F5763 · tech\_claim · Medium confidence · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F5764 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/purchase\-order\-compliance](https://www.duvo.ai/solutions/purchase-order-compliance)
- F5765 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/store\-operations\-compliance](https://www.duvo.ai/solutions/store-operations-compliance)
- F5766 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/store\-operations\-compliance](https://www.duvo.ai/solutions/store-operations-compliance)
- F5767 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/store\-operations\-compliance](https://www.duvo.ai/solutions/store-operations-compliance)
- F5768 · tech\_claim · Medium confidence · [https://www\.duvo\.ai/solutions/store\-operations\-compliance](https://www.duvo.ai/solutions/store-operations-compliance)
- F5769 · funding\_round · Medium confidence · [https://tech\.eu/2025/12/02/duvo\-raises\-15m\-to\-give\-retailers\-ai\-staff\-that\-cuts\-manual\-work\-by\-40/](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/)
- F5770 · product\_capability · Medium confidence · [https://tech\.eu/2025/12/02/duvo\-raises\-15m\-to\-give\-retailers\-ai\-staff\-that\-cuts\-manual\-work\-by\-40/](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/)
- F5771 · tech\_claim · Medium confidence · [https://tech\.eu/2025/12/02/duvo\-raises\-15m\-to\-give\-retailers\-ai\-staff\-that\-cuts\-manual\-work\-by\-40/](https://tech.eu/2025/12/02/duvo-raises-15m-to-give-retailers-ai-staff-that-cuts-manual-work-by-40/)
- F5772 · funding\_round · Medium confidence · [https://www\.therecursive\.com/rohlik\-founder\-tomas\-cuprs\-duvo\-raises\-eur28\-7m\-series\-a\-to\-take\-enterprise\-ai\-agents\-to\-the\-us](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- F5773 · product\_capability · Medium confidence · [https://www\.therecursive\.com/rohlik\-founder\-tomas\-cuprs\-duvo\-raises\-eur28\-7m\-series\-a\-to\-take\-enterprise\-ai\-agents\-to\-the\-us](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- F5775 · customer · Medium confidence · [https://www\.therecursive\.com/rohlik\-founder\-tomas\-cuprs\-duvo\-raises\-eur28\-7m\-series\-a\-to\-take\-enterprise\-ai\-agents\-to\-the\-us](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- F5776 · tech\_claim · Medium confidence · [https://www\.therecursive\.com/rohlik\-founder\-tomas\-cuprs\-duvo\-raises\-eur28\-7m\-series\-a\-to\-take\-enterprise\-ai\-agents\-to\-the\-us](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- F5777 · team\_claim · Medium confidence · [https://www\.therecursive\.com/rohlik\-founder\-tomas\-cuprs\-duvo\-raises\-eur28\-7m\-series\-a\-to\-take\-enterprise\-ai\-agents\-to\-the\-us](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- F5778 · funding\_round · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F5779 · product\_capability · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F5780 · product\_capability · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F5781 · customer · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F5782 · tech\_claim · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F5783 · tech\_claim · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F5784 · team\_claim · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F5785 · team\_claim · Medium confidence · [https://finance\.yahoo\.com/technology/ai/articles/duvo\-raises\-32\-million\-series\-130000587\.html](https://finance.yahoo.com/technology/ai/articles/duvo-raises-32-million-series-130000587.html)
- F5786 · funding\_round · Medium confidence · [https://www\.wired\.cz/news\-beat/cuprovo\-duvo\-ziskalo\-32\-milionu\-dolaru\-na\-expanzi](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi)
- F5788 · product\_capability · Medium confidence · [https://www\.wired\.cz/news\-beat/cuprovo\-duvo\-ziskalo\-32\-milionu\-dolaru\-na\-expanzi](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi)
- F5789 · customer · Medium confidence · [https://www\.wired\.cz/news\-beat/cuprovo\-duvo\-ziskalo\-32\-milionu\-dolaru\-na\-expanzi](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi)
- F5790 · team\_claim · Medium confidence · [https://www\.wired\.cz/news\-beat/cuprovo\-duvo\-ziskalo\-32\-milionu\-dolaru\-na\-expanzi](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi)
- F5791 · tech\_claim · Medium confidence · [https://www\.wired\.cz/news\-beat/cuprovo\-duvo\-ziskalo\-32\-milionu\-dolaru\-na\-expanzi](https://www.wired.cz/news-beat/cuprovo-duvo-ziskalo-32-milionu-dolaru-na-expanzi)
- F5792 · funding\_round · Medium confidence · [https://tech\.eu/2026/10/14/from\-rohlik\-to\-enterprise\-ai\-tomas\-cuprs\-duvo\-raises\-32m\-series\-a/](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
- F5793 · product\_capability · Medium confidence · [https://tech\.eu/2026/10/14/from\-rohlik\-to\-enterprise\-ai\-tomas\-cuprs\-duvo\-raises\-32m\-series\-a/](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
- F5794 · customer · Medium confidence · [https://tech\.eu/2026/10/14/from\-rohlik\-to\-enterprise\-ai\-tomas\-cuprs\-duvo\-raises\-32m\-series\-a/](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
- F5795 · customer · Medium confidence · [https://tech\.eu/2026/10/14/from\-rohlik\-to\-enterprise\-ai\-tomas\-cuprs\-duvo\-raises\-32m\-series\-a/](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
- F5796 · tech\_claim · Medium confidence · [https://tech\.eu/2026/10/14/from\-rohlik\-to\-enterprise\-ai\-tomas\-cuprs\-duvo\-raises\-32m\-series\-a/](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
- F5797 · tech\_claim · Medium confidence · [https://tech\.eu/2026/10/14/from\-rohlik\-to\-enterprise\-ai\-tomas\-cuprs\-duvo\-raises\-32m\-series\-a/](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
- F5798 · tech\_claim · Medium confidence · [https://tech\.eu/2026/10/14/from\-rohlik\-to\-enterprise\-ai\-tomas\-cuprs\-duvo\-raises\-32m\-series\-a/](https://tech.eu/2026/10/14/from-rohlik-to-enterprise-ai-tomas-cuprs-duvo-raises-32m-series-a/)
- F5799 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/customer\-complaint\-management](https://www.duvo.ai/solutions/customer-complaint-management)
- F5800 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/customer\-complaint\-management](https://www.duvo.ai/solutions/customer-complaint-management)
- F5801 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/customer\-complaint\-management](https://www.duvo.ai/solutions/customer-complaint-management)
- F5802 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/customer\-complaint\-management](https://www.duvo.ai/solutions/customer-complaint-management)
- F5803 · product\_capability · Medium confidence · [https://www\.duvo\.ai/solutions/customer\-complaint\-management](https://www.duvo.ai/solutions/customer-complaint-management)
- F6371 · verification · Sourced · [https://www\.duvo\.ai/](https://www.duvo.ai/)
- F6372 · verification · Sourced · [https://www\.therecursive\.com/rohlik\-founder\-tomas\-cuprs\-duvo\-raises\-eur28\-7m\-series\-a\-to\-take\-enterprise\-ai\-agents\-to\-the\-us](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
- F6373 · verification · Sourced · [https://www\.therecursive\.com/rohlik\-founder\-tomas\-cuprs\-duvo\-raises\-eur28\-7m\-series\-a\-to\-take\-enterprise\-ai\-agents\-to\-the\-us](https://www.therecursive.com/rohlik-founder-tomas-cuprs-duvo-raises-eur28-7m-series-a-to-take-enterprise-ai-agents-to-the-us)
