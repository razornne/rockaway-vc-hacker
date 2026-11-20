# ValkaAI — due diligence brief

valka\.ai · Valka\.AI s\.r\.o\. · IČO 23132221 · CZ · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A real\-time interactive AI\-video platform selling lifelike AI personas and live commentators to sports, esports and media/entertainment customers\. *(Partly verified)* ^[1](https://valka.ai/),[2](https://valka.ai/),[3](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
- **Stage & traction.** Pre\-seed with large external rounds \(reported €12M closed; later reported expansion to €13M\) and media coverage; no named paying customers found in the facts\. *(Corroborated)* ^[4](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[5](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[6](https://cc.cz/jeho-startup-rychle-roste-ted-zavetril-dalsi-prilezitost-vyviji-lidskeho-avatara-pro-hry-a-igaming/)
- **Technology & moat.** Claimed proprietary 'language of motion' and control model for real\-time synthesis — technical description exists, but public patents not found\. *(Verified)* ^[7](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[8](https://patents.google.com/?assignee=valkaai)
- **Key risk.** Central technical claims \(real\-time synthesis, 'proprietary control model'\) are unverified externally and lack independent patent evidence\. *(Analyst view)* ^[7](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[8](https://patents.google.com/?assignee=valkaai)
- **Diligence focus.** Verify live\-system demos under customer\-like latency and quality constraints, and obtain independent performance metrics and cost\-per\-minute estimates\. *(Analyst view)* ^[9](https://vestbee.com/insights/articles/valka-ai-raises-12-m),[10](https://vestbee.com/insights/articles/valka-ai-raises-12-m),[11](https://valka.ai/blog/valkaai-raises-12-million)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2026\-02\-24 · pre\-seed · €12 million · Rockaway Ventures, J&amp;T Ventures, Tensor Ventures, BD Partners, Fond Naše Česko, Petr Zámeč · 7 reports; 2026\-11\-12 · pre\-seed · €13 million · Look AI Ventures, ff Venture Capital, Rockaway Ventures, J&amp;T Ventures, Tensor Ventures, BD · 2 reports | 4, 12, 13, 14, 15, 16 |
| Public money | 1 grant project\(s\) awarded 20\.6M CZK | 17 |
| Thesis fit \(Rockaway\) | sectors: AI\-led transformative tech \(34 facts\); deep tech \(8 facts\); industrial / manufacturing AI \(2 facts\) · geography: CZ \(core region\) · overlaps portfolio: CulturePulse \(VENTURES deal, not Defense fund\) \(digital, frames\) | 6, 18, 19, 2, 17 |
| Hiring | 5 open roles: other 2, ml research 2, engineering 1 | 20, 21, 22, 23, 24 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; own\-model evidence: 0 papers, 0 verified HF models, 3 ML roles, 2 own\-model claims | 25, 7, 20 |
| Engineering footprint | product surfaces: api\.bots\.dev\.valka\.ai, api\.bots\.prd\.valka\.ai, api\.bots\.valka\.ai, api\.matchvision\.dev\.valka\.ai, api\.matchvision\.valka\.ai, auth\.bots\.dev\.valka\.ai; stack: Next\.js | 26, 27, 28 |
| Claims checked | Patents: not found | 8 |
| Timeline | Czech entity registered 2025\-04\-01; first press 2025\-05\-12 \(25 articles collected\) | 29, 6 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the market, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** AI\-led transformative tech — company claims real\-time generative video, audio and event\-understanding research across three areas, positioning as AI\-native entertainment infrastructure\. *(Analyst view)* ^[30](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[7](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[31](https://valka.ai/company)
  - Assumption: Claims reflect core product focus rather than marketing only
- **Portfolio overlap:** CulturePulse — overlap possible as both are framed by the fund as dual\-use / behaviour/intelligence platforms; ValkaAI’s lifelike personas and real\-time commentary could be complementary or competitive depending on buyer \(media vs risk/defence\)\. *(Analyst view)* ^[3](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[1](https://valka.ai/),[32](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
  - Assumption: CulturePulse overlap inferred from Rockaway framing, not direct product comparison

## Business model

- Primary commercial product pitch: a platform for entertainment players to create interactive digital environments and AI avatars \(buyers implied: broadcasters, sports/esports platforms\)\. *(Corroborated)* ^[3](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[33](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment)
- Specific product revenue channel: ValkaAI Commentator sells live sports/esports commentary generated from event data \(implied B2B SaaS or licensing to rights\-holders/broadcasters\)\. *(Analyst view)* ^[34](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[35](https://valka.ai/blog/valkaai-raises-12-million)
  - Assumption: Pricing and contract form \(SaaS/license\) unreported
- Public support: awarded a Czech governmental targeted support agreement worth 20,563,542 Kč \(grant record exists; payment status unspecified\)\. *(Verified)* ^[17](https://smlouvy.gov.cz/smlouva/39346345)

## Market

- Target market: global streaming and live entertainment \(sports and esports\) — stated by company and trade coverage as primary go\-to market\. *(Corroborated)* ^[19](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment),[33](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment),[36](https://lookai.vc/portfolio/valkaai)
- Demand driver cited: need for scalable, personalised live commentary and interactive digital personas to increase engagement for viewers and platforms \(company and press claim\)\. *(Single source)* ^[9](https://vestbee.com/insights/articles/valka-ai-raises-12-m),[10](https://vestbee.com/insights/articles/valka-ai-raises-12-m),[37](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- No sourced numerical market size or TAM estimate found in the supplied facts\. *(Single source)* ^[38](https://vestbee.com/insights/articles/valka-ai-raises-12-m)

## Competition

No sourced findings for this section.

## Case for and against

- **For:** Differentiated real\-time stack — company claims proprietary 'language of motion' and efficient real\-time synthesis across voice, motion and cognition, supporting interactive avatars at scale\. *(Analyst view)* ^[7](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[11](https://valka.ai/blog/valkaai-raises-12-million)
  - Assumption: Proprietary claims translate into technical differentiation
- **For:** Experienced founding / research team and international presence \(founder with Oddin\.gg exit history; \~45 employees including researchers from Meta/DeepMind claimed\)\. *(Analyst view)* ^[39](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment),[40](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
  - Assumption: Team claims map to execution capability
- **For:** Strong capital signal — a large pre\-seed raise led by Rockaway \(reported €12M–€13M\) provides runway and investor validation for rapid product development\. *(Analyst view)* ^[4](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[5](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/)
  - Assumption: Reported round amounts reflect actual closed funding
- **Against:** No verified IP assigned to the company found in patent databases \(search returned no publications under 'valkaai'\)\. *(Analyst view)* ^[8](https://patents.google.com/?assignee=valkaai)
  - Assumption: Patent search covered company assignee names
- **Against:** Customer traction and revenue not documented in supplied facts — no named customers or contract wins are present in the data\. *(Analyst view)* ^[34](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[3](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
  - Assumption: Public reporting would mention early commercial pilot customers
- **Must be true:** The technology delivers low\-latency, visually convincing avatars in live contexts as claimed \(real\-time synthesis and synchronization across voice/motion\)\. *(Analyst view)* ^[7](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[11](https://valka.ai/blog/valkaai-raises-12-million)
  - Assumption: Real\-time claims are demonstrable in production settings

# Technical due diligence

## Ownership and capital

- Incorporated in Czech Republic 2025\-04\-01 as Valka\.AI s\.r\.o\.; 100% foreign holding recorded \(Valka\.AI B\.V\., NL\)\. *(Verified)* ^[41](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221),[42](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23132221)
- Reported pre\-seed funding: €12M \(Rockaway lead, J&amp;T, Tensor, BD Partners, Fond Naše Česko, individual investor\), later reported €13M extension including Look AI and ffVC\. *(Partly verified)* ^[4](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[5](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[43](https://valka.ai/blog/valkaai-raises-12-million)
- Company received national targeted support recorded as CZK 20,563,542 \(Ministerstvo průmyslu a obchodu agreement in 2026\)\. *(Verified)* ^[17](https://smlouvy.gov.cz/smlouva/39346345)

## Technology profile

- Built product claims: real\-time AI avatars, live commentators, and a platform for interactive synthetic video and audio\. *(Partly verified)* ^[9](https://vestbee.com/insights/articles/valka-ai-raises-12-m),[2](https://valka.ai/),[34](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/)
- Engineering footprint: public subdomains exposing API surfaces \(api\.bots\.\*, api\.matchvision\.\*, auth\.bots\.dev\) and Next\.js\-driven website\. *(Verified)* ^[26](https://crt.sh/?q=%25.valka.ai&output=json),[27](https://crt.sh/?q=%25.valka.ai&output=json),[28](https://crt.sh/?q=%25.valka.ai&output=json),[44](https://crt.sh/?q=%25.valka.ai&output=json),[45](https://crt.sh/?q=%25.valka.ai&output=json),[46](https://valka.ai/)
- AI dependency / models: company claims developing own models across video, audio and event understanding; no verified external\-model dependencies listed\. *(Partly verified)* ^[30](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[47](https://valka.ai/blog/valkaai-raises-12-million),[25](https://www.valka.ai/company)

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** Live\-commentary from event data can be reproduced using an event\-to\-text pipeline plus an open TTS and speech pipeline \(company shows 'ValkaAI Commentator' capability\)\. *(Analyst view)* ^[34](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[35](https://valka.ai/blog/valkaai-raises-12-million)
  - Assumption: Rebuilder uses standard open\-source TTS and NLG models
- **Edge supported by public evidence:** Company cites a proprietary 'language of motion' and control model for frame\-consistent real\-time synthesis; this claim is documented in press and investor materials\. *(Analyst view)* ^[7](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[32](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
  - Assumption: Press/investor materials accurately reflect internal R&amp;D
- **Cannot be judged from outside:** Real\-time visual fidelity, temporal consistency and production latency under load cannot be judged without source code, models, datasets, or live\-system logs\. *(Analyst view)* ^[10](https://vestbee.com/insights/articles/valka-ai-raises-12-m),[11](https://valka.ai/blog/valkaai-raises-12-million)
  - Assumption: No third\-party verification or benchmarks provided in facts

## Risks and caveats

- Unverified IP: company leadership claims patents/research but patent search returned no ValkaAI assignee publications\. *(Analyst view)* ^[25](https://www.valka.ai/company),[8](https://patents.google.com/?assignee=valkaai)
- Revenue concentration unknown: sizable pre\-seed funding and press launches exist, but no named paying customers or published pricing found\. *(Analyst view)* ^[4](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[38](https://vestbee.com/insights/articles/valka-ai-raises-12-m),[26](https://crt.sh/?q=%25.valka.ai&output=json)
- Execution scaling risk: ambitious real\-time multi\-modal synchronization claims require substantial ML and infra hiring; current public jobs show early\-stage ML hiring\. *(Analyst view)* ^[11](https://valka.ai/blog/valkaai-raises-12-million),[23](https://valka.ai/careers),[24](https://valka.ai/careers)

## Questions for founders

- Provide technical benchmark reports \(latency, frame consistency, cost\) for the ValkaAI Commentator in a production\-like stream; press claims exist but no metrics shown\. *(Analyst view)* ^[34](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[9](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- Share IP evidence: list patent applications, assignees, and any third\-party lab verifications to reconcile leadership patent claims with the 'not\_found' patent check\. *(Analyst view)* ^[25](https://www.valka.ai/company),[8](https://patents.google.com/?assignee=valkaai)
- Customer reference request: provide signed pilot agreements or purchase orders and unit economics for AI\-commentary deployments versus claimed platform ambitions\. *(Analyst view)* ^[4](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[5](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[9](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- Clarify model provenance and dependencies: which components are in\-house versus using external LLM/TTS providers, and related subprocessors or integrations\. *(Analyst view)* ^[30](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[23](https://valka.ai/careers),[24](https://valka.ai/careers)

## Sources

1. [valka\.ai](https://valka.ai/) · Company's own website · Product capability — “We create synthetic video for sports and media using lifelike characters with real agency\.”
2. [valka\.ai](https://valka.ai/) · Company's own website · Product capability — “Live commentary, generated for the audience actually listening\.”
3. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures) · Independent press · Product capability — “The company’s core product will be a platform that enables entertainment industry players to create digital environments and AI avatars with which users can actively interact\.”
4. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures) · Independent press · Funding round — “The company has raised €12 million in a pre\-seed funding round led by Rockaway Ventures, with participation from J&amp;T Ventures, Tensor Ventures, BD Partners, and Fond Naše Česko\.”
5. [lookai\.vc](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/) · Independent press · Funding round — “Look AI Ventures has joined ValkaAI‘s pre\-seed round alongside ff Venture Capital, bringing the round to €13 million\.”
6. [cc\.cz](https://cc.cz/jeho-startup-rychle-roste-ted-zavetril-dalsi-prilezitost-vyviji-lidskeho-avatara-pro-hry-a-igaming/) · Independent press · Press article · 2025\-05\-12 — “Jeho startup rychle roste, teď zavětřil další příležitost \- CzechCrunch”
7. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures) · Independent press · Technical claim — “The ValkaAI team is currently focused on developing fully controlled, real\-time AI synthesis of motion and visuals\. Instead of generating entire video segments at once, which is slow and computationally demanding, the system works with an efficient representation, a ‘language of motion,’ and a proprietary control model…”
8. [patents\.google\.com](https://patents.google.com/?assignee=valkaai) · Official record · Independent check of a claim — “No publication with assignee starting with 'valkaai' on Google Patents\.”
9. [vestbee\.com](https://vestbee.com/insights/articles/valka-ai-raises-12-m) · Independent press · Product capability — “ValkaAI develops real\-time interactive video technology using AI\-driven digital avatars\. The company’s platform generates synthetic video content on demand, including AI commentators and digital characters that react to live events and user interactions\.”
10. [vestbee\.com](https://vestbee.com/insights/articles/valka-ai-raises-12-m) · Independent press · Technical claim — “The technology works by creating fully controllable avatars capable of performing in real time, with personalized responses tailored to individual viewers\.”
11. [valka\.ai](https://valka.ai/blog/valkaai-raises-12-million) · Company's own website · Technical claim — “This type of work involves synchronization across voice, motion, cognition, and infrastructure\.”
12. [valka\.ai](https://valka.ai/company) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
13. [valka\.ai](https://www.valka.ai/company) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
14. [valka\.ai](https://valka.ai/privacy-policy) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
15. [valka\.ai](https://www.valka.ai/privacy-policy) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
16. [valka\.ai](https://valka.ai/blog) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
17. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/39346345) · Official record · National grant · 2026 — “Poskytnutí účelové podpory · Ministerstvo průmyslu a obchodu · 20 563 542 CZK”
18. [e15\.cz](https://www.e15.cz/rozhovory/vybudoval-nejrychleji-rostouci-startup-ted-chce-venclik-postavit-nejlepsi-ai-video-firmu-1425083) · Independent press · Press article · 2025\-06\-08 — “Vybudoval nejrychleji rostoucí startup\. Teď chce postavit nejlepší AI video firmu, plánuje Venclík \| e15\.cz”
19. [czechtradeoffices\.com](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment) · Independent press · Press article — “CzechTrade Offices \- Czech AI Startup ValkaAI Targets Global Streaming Market with €12 Million Investment”
20. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “Applied Science Intern \- World Models”
21. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “Senior Product Manager”
22. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “Kotlin Developer”
23. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “LLM Researcher”
24. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “Research Scientist \(Text\-To\-Speech\)”
25. [valka\.ai](https://www.valka.ai/company) · Company's own website · Technical claim — “With a PhD in computer graphics, he has co\-authored leading SIGGRAPH and CVPR papers, co\-invented several patents, and developed AI models for stylized and photorealistic digital humans – bridging academic research with production\-grade results\.”
26. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-10\-08 — “api\.bots\.dev\.valka\.ai \(first certificate 2025\-10\-08\)”
27. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-01\-28 — “api\.bots\.prd\.valka\.ai \(first certificate 2026\-01\-28\)”
28. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-01\-29 — “api\.bots\.valka\.ai \(first certificate 2026\-01\-29\)”
29. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221) · Official record · Registry: incorporation · 2025\-04\-01 — “registered 2025\-04\-01”
30. [lookai\.vc](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/) · Independent press · Technical claim — “Its own technology\. Instead of building on top of existing generative AI models, ValkaAI develops its own across three research areas: video generation, audio generation, and event understanding\.”
31. [valka\.ai](https://valka.ai/company) · Company's own website · Product capability — “Lifelike AI personas – built to make digital experiences more engaging, expressive, and scalable\.”
32. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures) · Independent press · Press article · 2026\-02\-24 — “€12M Investment in ValkaAI Led by Rockaway Ventures – Rockaway Capital”
33. [czechtradeoffices\.com](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment) · Independent press · Product capability — “The startup’s technology aims to enable digital avatars to react to content in real time, including sports matches and other entertainment formats\.”
34. [lookai\.vc](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/) · Independent press · Product capability — “ValkaAI Commentator , launched this year, generates live sports and esports commentary directly from event data\.”
35. [valka\.ai](https://valka.ai/blog/valkaai-raises-12-million) · Company's own website · Product capability — “In e\-sports, this technology could take the form of an AI commentator that reacts to in\-game action in real time, speaks the viewer’s language, and adapts to their viewing style\.”
36. [lookai\.vc](https://lookai.vc/portfolio/valkaai) · Independent press · Press article · 2026\-10\-21 — “ValkaAI — Real\-Time AI Sports Commentary \| Look AI Ventures”
37. [vestbee\.com](https://vestbee.com/insights/articles/valka-ai-raises-12-m) · Independent press · Funding round — “With the fresh €12 million investment, ValkaAI aims to accelerate the development of its core technologies, including fully controllable digital avatars and AI commentators that react in real time\.”
38. [vestbee\.com](https://vestbee.com/insights/articles/valka-ai-raises-12-m) · Independent press · Press article · 2026\-02\-24 — “Czech firm ValkaAI raises €12M to build real\-time interactive AI video platform \| Vestbee”
39. [czechtradeoffices\.com](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment) · Independent press · Team claim — “ValkaAI was founded by entrepreneurs with experience from the Czech technology scale\-up Oddin\.gg, which focuses on esports betting and data solutions\.”
40. [vestbee\.com](https://vestbee.com/insights/articles/valka-ai-raises-12-m) · Independent press · Team claim — “ValkaAI operates teams in San Francisco, Prague, and Dubai and employs around 45 people, including researchers from Meta and DeepMind\.”
41. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221) · Official record · Registry: identity · 2025\-04\-01 — “Valka\.AI s\.r\.o\. · s\.r\.o\. · registered 2025\-04\-01”
42. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23132221) · Official record · Registry: shareholder · 2025\-04\-01 — “Valka\.AI B\.V\. · 100\.0% · from 2025\-04\-01”
43. [valka\.ai](https://valka.ai/blog/valkaai-raises-12-million) · Company's own website · Funding round — “we’re thrilled about our first external capital—€12M pre\-seed funding, led by Rockaway Ventures, with participation from J&amp;T Ventures, Tensor Ventures, BD Partners, Fond Naše Česko and Petr Zámečník\.”
44. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-09\-25 — “api\.matchvision\.dev\.valka\.ai \(first certificate 2026\-09\-25\)”
45. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-09\-25 — “api\.matchvision\.valka\.ai \(first certificate 2026\-09\-25\)”
46. [valka\.ai](https://valka.ai/) · Public technical artifact · Technology detected
47. [valka\.ai](https://valka.ai/blog/valkaai-raises-12-million) · Company's own website · Technical claim — “Our unique three\-tiered genAI process will be able to create the technology for on\-demand content at scale and without the technical limitations we currently see with AI\-generated video”
48. [cc\.cz](https://cc.cz/rekordni-investici-cesky-startup-jeste-navysil-tvurci-ai-komentatora-ziskali-uz-stovky-milionu/) · Independent press · Funding round — “úvodní, tzv\. pre\-seedovou investici ve výši téměř 300 milionů korun”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 9 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 1 | starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 25 | press:eu\-startups\.com, press:globalstartupsinsights\.com, press:theintelligent\.cz |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 17 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 100 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 4 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 1 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 37 | — |

Analysis: gpt\-5\-mini (cost $0.0174); AI extraction cost $0.0101. Full fact table: CSV export.

## Source appendix (all collected facts)

- F5196 · identity · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/23132221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221)
- F5197 · registry\_incorporation · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty/23132221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221)
- F5198 · registry\_shareholder · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23132221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23132221)
- F5199 · registry\_capital · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23132221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23132221)
- F5200 · registry\_officer\_change · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23132221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23132221)
- F5201 · registry\_flag · Sourced · [https://ares\.gov\.cz/ekonomicke\-subjekty\-v\-be/rest/ekonomicke\-subjekty\-vr/23132221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23132221)
- F5202 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1272272](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1272272)
- F5203 · filing · Sourced · [https://or\.justice\.cz/ias/ui/vypis\-sl\-firma?subjektId=1272272](https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=1272272)
- F5204 · insolvency · Sourced · [https://isir\.justice\.cz/isir/ueu/vysledek\_lustrace\.do?ic=23132221&amp;aktualnost=AKTUALNI\_I\_UKONCENA&amp;rowsAtOnce=50](https://isir.justice.cz/isir/ueu/vysledek_lustrace.do?ic=23132221&aktualnost=AKTUALNI_I_UKONCENA&rowsAtOnce=50)
- F5205 · web\_page · Sourced · [https://valka\.ai/](https://valka.ai/)
- F5206 · web\_page · Sourced · [https://valka\.ai/careers](https://valka.ai/careers)
- F5207 · web\_page · Sourced · [https://valka\.ai/privacy\-policy](https://valka.ai/privacy-policy)
- F5208 · web\_page · Sourced · [https://www\.valka\.ai/careers](https://www.valka.ai/careers)
- F5209 · web\_page · Sourced · [https://www\.valka\.ai/privacy\-policy](https://www.valka.ai/privacy-policy)
- F5210 · web\_page · Sourced · [https://valka\.ai/company](https://valka.ai/company)
- F5211 · web\_page · Sourced · [https://www\.valka\.ai/company](https://www.valka.ai/company)
- F5212 · web\_page · Sourced · [https://valka\.ai/blog](https://valka.ai/blog)
- F5213 · web\_page · Sourced · [https://valka\.ai/blog/valkaai\-raises\-12\-million](https://valka.ai/blog/valkaai-raises-12-million)
- F5214 · web\_page · Sourced · [https://valka\.ai/blog/from\-live\-data\-to\-live\-commentary](https://valka.ai/blog/from-live-data-to-live-commentary)
- F5215 · web\_page · Sourced · [https://valka\.ai/commentator](https://valka.ai/commentator)
- F5216 · web\_page · Sourced · [https://valka\.ai/research](https://valka.ai/research)
- F5217 · job\_post · Sourced · [https://valka\.ai/careers](https://valka.ai/careers)
- F5218 · job\_post · Sourced · [https://valka\.ai/careers](https://valka.ai/careers)
- F5219 · job\_post · Sourced · [https://valka\.ai/careers](https://valka.ai/careers)
- F5220 · job\_post · Sourced · [https://valka\.ai/careers](https://valka.ai/careers)
- F5221 · job\_post · Sourced · [https://valka\.ai/careers](https://valka.ai/careers)
- F5222 · tech\_stack · Medium confidence · [https://valka\.ai/](https://valka.ai/)
- F5223 · tech\_stack · Medium confidence · [https://valka\.ai/](https://valka.ai/)
- F5224 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=valka\.ai&amp;type=MX](https://dns.google/resolve?name=valka.ai&type=MX)
- F5225 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=valka\.ai&amp;type=TXT](https://dns.google/resolve?name=valka.ai&type=TXT)
- F5226 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=valka\.ai&amp;type=TXT](https://dns.google/resolve?name=valka.ai&type=TXT)
- F5227 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5228 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5229 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5230 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5231 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5232 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5233 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5234 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5235 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5236 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5237 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5238 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5239 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5240 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5241 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5242 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5243 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5244 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5245 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5246 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5247 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5248 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5249 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5250 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5251 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5252 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5253 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5254 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5255 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5256 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5257 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5258 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5259 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5260 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5261 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5262 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5263 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5264 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5265 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5266 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5267 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5268 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5269 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5270 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5271 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5272 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5273 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5274 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5275 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5276 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5277 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5278 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5279 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5280 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5281 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5282 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5283 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5284 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5285 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5286 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5287 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5288 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5289 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5290 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5291 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5292 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5293 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5294 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5295 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5296 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5297 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5298 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5299 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5300 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5301 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5302 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5303 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5304 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5305 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5306 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5307 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5308 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5309 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5310 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5311 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5312 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5313 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5314 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5315 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5316 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5317 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5318 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5319 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5320 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5321 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.valka\.ai&amp;output=json](https://crt.sh/?q=%25.valka.ai&output=json)
- F5322 · wayback\_first · Sourced · [https://web\.archive\.org/web/20250709002724/https://valka\.ai/](https://web.archive.org/web/20250709002724/https://valka.ai/)
- F5323 · wayback\_first · Sourced · [https://web\.archive\.org/web/20250912195949/https://valka\.ai/careers](https://web.archive.org/web/20250912195949/https://valka.ai/careers)
- F5324 · wayback\_first · Sourced · [https://web\.archive\.org/web/20260418204320/https://valka\.ai/blog/how\-ai\-avatars\-drive\-long\-term\-engagement](https://web.archive.org/web/20260418204320/https://valka.ai/blog/how-ai-avatars-drive-long-term-engagement)
- F5325 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/valka\.ai](https://web.archive.org/web/%2A/valka.ai)
- F5330 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5331 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5332 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5333 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5334 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5335 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5336 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5337 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5338 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5339 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5340 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5341 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5342 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5343 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5344 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5345 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5346 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5347 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5348 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5349 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5350 · press\_mention · Sourced · [https://cc\.cz/jeho\-startup\-rychle\-roste\-ted\-zavetril\-dalsi\-prilezitost\-vyviji\-lidskeho\-avatara\-pro\-hry\-a\-igaming/](https://cc.cz/jeho-startup-rychle-roste-ted-zavetril-dalsi-prilezitost-vyviji-lidskeho-avatara-pro-hry-a-igaming/)
- F5351 · press\_mention · Sourced · [https://www\.e15\.cz/rozhovory/vybudoval\-nejrychleji\-rostouci\-startup\-ted\-chce\-venclik\-postavit\-nejlepsi\-ai\-video\-firmu\-1425083](https://www.e15.cz/rozhovory/vybudoval-nejrychleji-rostouci-startup-ted-chce-venclik-postavit-nejlepsi-ai-video-firmu-1425083)
- F5352 · press\_mention · Sourced · [https://www\.rockawaycapital\.com/en/news/e12m\-investment\-in\-valkaai\-led\-by\-rockaway\-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
- F5353 · press\_mention · Sourced · [https://www\.lupa\.cz/clanky/dokonaly\-avatar\-cesi\-se\-zkusenostmi\-z\-americkych\-laboratori\-skladaji\-v\-prazskem\-startupu\-video\-hlas\-a\-pohyb\-v\-realnem\-case/](https://www.lupa.cz/clanky/dokonaly-avatar-cesi-se-zkusenostmi-z-americkych-laboratori-skladaji-v-prazskem-startupu-video-hlas-a-pohyb-v-realnem-case/)
- F5354 · press\_mention · Sourced · [https://www\.czechtradeoffices\.com/nl/news/czech\-ai\-startup\-valkaai\-targets\-global\-streaming\-market\-with\-%E2%82%AC12\-million\-investment](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment)
- F5355 · press\_mention · Sourced · [https://vestbee\.com/insights/articles/valka\-ai\-raises\-12\-m](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- F5356 · press\_mention · Sourced · [https://lookai\.vc/portfolio/valkaai](https://lookai.vc/portfolio/valkaai)
- F5357 · press\_mention · Sourced · [https://lookai\.vc/look\-ai\-ventures\-joins\-valkaai\-13m\-pre\-seed\-round/](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/)
- F5358 · press\_mention · Sourced · [https://cc\.cz/rekordni\-investici\-cesky\-startup\-jeste\-navysil\-tvurci\-ai\-komentatora\-ziskali\-uz\-stovky\-milionu/](https://cc.cz/rekordni-investici-cesky-startup-jeste-navysil-tvurci-ai-komentatora-ziskali-uz-stovky-milionu/)
- F5359 · source\_unavailable · Unavailable · [https://www\.eu\-startups\.com/2026/11/czech\-startup\-valkaai\-extends\-pre\-seed\-round\-to\-e13\-million\-to\-bring\-ai\-personas\-to\-live\-events\-at\-scale/](https://www.eu-startups.com/2026/11/czech-startup-valkaai-extends-pre-seed-round-to-e13-million-to-bring-ai-personas-to-live-events-at-scale/)
- F5360 · press\_mention · Sourced · [https://lookai\.vc/cs/spolecnost\-look\-ai\-ventures\-se\-pripojila\-k\-predseedovemu\-kolu\-financovani\-spolecnosti\-valkaai\-ve\-vysi\-13\-milionu/](https://lookai.vc/cs/spolecnost-look-ai-ventures-se-pripojila-k-predseedovemu-kolu-financovani-spolecnosti-valkaai-ve-vysi-13-milionu/)
- F5361 · source\_unavailable · Unavailable · [https://theintelligent\.cz/technologie/2026/cesky\-startup\-valkaai\-navysil\-pre\-seed\-kolo\-na\-13\-milionu\-eur](https://theintelligent.cz/technologie/2026/cesky-startup-valkaai-navysil-pre-seed-kolo-na-13-milionu-eur)
- F5362 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/rekordne\-zainvestovana\-ceska\-valkaai\-ziskala\-dalsi\-penize\-a\-predstavila\-ai\-komentatora/](https://www.lupa.cz/aktuality/rekordne-zainvestovana-ceska-valkaai-ziskala-dalsi-penize-a-predstavila-ai-komentatora/)
- F5363 · press\_mention · Sourced · [https://www\.rockawaycapital\.com/cs/aktuality/valkaai\-ziskava\-investici\-12\-milionu\-eur\-pod\-vedenim\-rockaway\-ventures](https://www.rockawaycapital.com/cs/aktuality/valkaai-ziskava-investici-12-milionu-eur-pod-vedenim-rockaway-ventures)
- F5364 · press\_mention · Sourced · [https://www\.thesaasnews\.com/news/valkaai\-raises\-13m\-pre\-seed\-extension/](https://www.thesaasnews.com/news/valkaai-raises-13m-pre-seed-extension/)
- F5365 · press\_mention · Sourced · [https://aipressroom\.com/valkaai\-13m\-ai\-personas](https://aipressroom.com/valkaai-13m-ai-personas)
- F5366 · press\_mention · Sourced · [https://startupkitchen\.community/czech\-valkaai\-raises\-e13m\-pre\-seed\-extension\-from\-ai\-focused\-vc\-funds/](https://startupkitchen.community/czech-valkaai-raises-e13m-pre-seed-extension-from-ai-focused-vc-funds/)
- F5367 · press\_mention · Sourced · [https://nordic9\.com/news/valkaai\-in\-a\-1\-million\-seed\-extension\-with\-lo/](https://nordic9.com/news/valkaai-in-a-1-million-seed-extension-with-lo/)
- F5368 · source\_unavailable · Unavailable · [https://www\.globalstartupsinsights\.com/funding/czech/valkaai\-extends\-pre\-seed\-funding\-to\-e13\-million\-for\-real\-time\-ai/](https://www.globalstartupsinsights.com/funding/czech/valkaai-extends-pre-seed-funding-to-e13-million-for-real-time-ai/)
- F5369 · press\_mention · Sourced · [https://techfundingnews\.com/valkaai\-12m\-pre\-seed\-cee\-largest\-real\-time\-ai\-avatars/](https://techfundingnews.com/valkaai-12m-pre-seed-cee-largest-real-time-ai-avatars/)
- F5370 · press\_mention · Sourced · [https://www\.therecursive\.com/valkaai\-12m\-pre\-seed\-rockaway\-ventures\-interactive\-video\-ai](https://www.therecursive.com/valkaai-12m-pre-seed-rockaway-ventures-interactive-video-ai)
- F5371 · press\_mention · Sourced · [https://realms\.group/news/valkaai\-raises\-12m\-to\-build\-the\-next\-generation\-of\-live\-ai\-avatars](https://realms.group/news/valkaai-raises-12m-to-build-the-next-generation-of-live-ai-avatars)
- F5372 · press\_mention · Sourced · [https://www\.startbase\.com/news/e12\-millionen\-pre\-seed\-fuer\-valkaai/](https://www.startbase.com/news/e12-millionen-pre-seed-fuer-valkaai/)
- F5373 · press\_mention · Sourced · [https://blog\.tensor\.ventures/p/new\-investment\-valkaai\-building\-the](https://blog.tensor.ventures/p/new-investment-valkaai-building-the)
- F5374 · press\_mention · Sourced · [https://www\.l\-ab\.eu/work/valkaai](https://www.l-ab.eu/work/valkaai)
- F5375 · press\_mention · Sourced · [https://eqvista\.com/interview\-with\-vlastimil\-venclik\-valkaai/](https://eqvista.com/interview-with-vlastimil-venclik-valkaai/)
- F5376 · press\_mention · Sourced · [https://vikend\.hn\.cz/c1\-67888510\-ai\-brzy\-nebude\-jen\-chatovaci\-okno\-bude\-mit\-tvar\-a\-komentovat\-fotbal\-sef\-ceskeho\-start\-upu\-uz\-to\-resi\-s\-top\-ligami](https://vikend.hn.cz/c1-67888510-ai-brzy-nebude-jen-chatovaci-okno-bude-mit-tvar-a-komentovat-fotbal-sef-ceskeho-start-upu-uz-to-resi-s-top-ligami)
- F5377 · press\_mention · Sourced · [https://www\.seznamzpravy\.cz/clanek/ekonomika\-firmy\-byznys\-startupy\-technologie\-cesky\-startup\-ziskal\-stovky\-milionu\-slibuje\-prepsat\-budoucnost\-zabavy\-299599](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-startup-ziskal-stovky-milionu-slibuje-prepsat-budoucnost-zabavy-299599)
- F5807 · product\_capability · Medium confidence · [https://valka\.ai/](https://valka.ai/)
- F5808 · product\_capability · Medium confidence · [https://valka\.ai/](https://valka.ai/)
- F5809 · tech\_claim · Medium confidence · [https://valka\.ai/](https://valka.ai/)
- F5810 · funding\_round · Medium confidence · [https://valka\.ai/company](https://valka.ai/company)
- F5811 · product\_capability · Medium confidence · [https://valka\.ai/company](https://valka.ai/company)
- F5812 · product\_capability · Medium confidence · [https://valka\.ai/company](https://valka.ai/company)
- F5813 · product\_capability · Medium confidence · [https://valka\.ai/company](https://valka.ai/company)
- F5814 · team\_claim · Medium confidence · [https://valka\.ai/company](https://valka.ai/company)
- F5815 · funding\_round · Medium confidence · [https://www\.valka\.ai/company](https://www.valka.ai/company)
- F5816 · product\_capability · Medium confidence · [https://www\.valka\.ai/company](https://www.valka.ai/company)
- F5818 · team\_claim · Medium confidence · [https://www\.valka\.ai/company](https://www.valka.ai/company)
- F5822 · tech\_claim · Medium confidence · [https://www\.valka\.ai/company](https://www.valka.ai/company)
- F5823 · funding\_round · Medium confidence · [https://valka\.ai/privacy\-policy](https://valka.ai/privacy-policy)
- F5824 · funding\_round · Medium confidence · [https://www\.valka\.ai/privacy\-policy](https://www.valka.ai/privacy-policy)
- F5825 · funding\_round · Medium confidence · [https://valka\.ai/blog](https://valka.ai/blog)
- F5826 · product\_capability · Medium confidence · [https://valka\.ai/blog](https://valka.ai/blog)
- F5827 · funding\_round · Medium confidence · [https://www\.rockawaycapital\.com/en/news/e12m\-investment\-in\-valkaai\-led\-by\-rockaway\-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
- F5828 · product\_capability · Medium confidence · [https://www\.rockawaycapital\.com/en/news/e12m\-investment\-in\-valkaai\-led\-by\-rockaway\-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
- F5829 · tech\_claim · Medium confidence · [https://www\.rockawaycapital\.com/en/news/e12m\-investment\-in\-valkaai\-led\-by\-rockaway\-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
- F5830 · team\_claim · Medium confidence · [https://www\.rockawaycapital\.com/en/news/e12m\-investment\-in\-valkaai\-led\-by\-rockaway\-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
- F5832 · product\_capability · Medium confidence · [https://www\.czechtradeoffices\.com/nl/news/czech\-ai\-startup\-valkaai\-targets\-global\-streaming\-market\-with\-%E2%82%AC12\-million\-investment](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment)
- F5833 · team\_claim · Medium confidence · [https://www\.czechtradeoffices\.com/nl/news/czech\-ai\-startup\-valkaai\-targets\-global\-streaming\-market\-with\-%E2%82%AC12\-million\-investment](https://www.czechtradeoffices.com/nl/news/czech-ai-startup-valkaai-targets-global-streaming-market-with-%E2%82%AC12-million-investment)
- F5834 · funding\_round · Medium confidence · [https://vestbee\.com/insights/articles/valka\-ai\-raises\-12\-m](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- F5835 · product\_capability · Medium confidence · [https://vestbee\.com/insights/articles/valka\-ai\-raises\-12\-m](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- F5836 · tech\_claim · Medium confidence · [https://vestbee\.com/insights/articles/valka\-ai\-raises\-12\-m](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- F5837 · team\_claim · Medium confidence · [https://vestbee\.com/insights/articles/valka\-ai\-raises\-12\-m](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- F5839 · funding\_round · Medium confidence · [https://lookai\.vc/look\-ai\-ventures\-joins\-valkaai\-13m\-pre\-seed\-round/](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/)
- F5840 · product\_capability · Medium confidence · [https://lookai\.vc/look\-ai\-ventures\-joins\-valkaai\-13m\-pre\-seed\-round/](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/)
- F5842 · tech\_claim · Medium confidence · [https://lookai\.vc/look\-ai\-ventures\-joins\-valkaai\-13m\-pre\-seed\-round/](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/)
- F5843 · team\_claim · Medium confidence · [https://lookai\.vc/look\-ai\-ventures\-joins\-valkaai\-13m\-pre\-seed\-round/](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/)
- F5845 · funding\_round · Medium confidence · [https://cc\.cz/rekordni\-investici\-cesky\-startup\-jeste\-navysil\-tvurci\-ai\-komentatora\-ziskali\-uz\-stovky\-milionu/](https://cc.cz/rekordni-investici-cesky-startup-jeste-navysil-tvurci-ai-komentatora-ziskali-uz-stovky-milionu/)
- F5846 · funding\_round · Medium confidence · [https://valka\.ai/blog/valkaai\-raises\-12\-million](https://valka.ai/blog/valkaai-raises-12-million)
- F5847 · product\_capability · Medium confidence · [https://valka\.ai/blog/valkaai\-raises\-12\-million](https://valka.ai/blog/valkaai-raises-12-million)
- F5848 · tech\_claim · Medium confidence · [https://valka\.ai/blog/valkaai\-raises\-12\-million](https://valka.ai/blog/valkaai-raises-12-million)
- F5849 · product\_capability · Medium confidence · [https://valka\.ai/blog/valkaai\-raises\-12\-million](https://valka.ai/blog/valkaai-raises-12-million)
- F5850 · team\_claim · Medium confidence · [https://valka\.ai/blog/valkaai\-raises\-12\-million](https://valka.ai/blog/valkaai-raises-12-million)
- F5851 · tech\_claim · Medium confidence · [https://valka\.ai/blog/valkaai\-raises\-12\-million](https://valka.ai/blog/valkaai-raises-12-million)
- F6374 · verification · Sourced · [https://patents\.google\.com/?assignee=valkaai](https://patents.google.com/?assignee=valkaai)
- F7814 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/dotace/hledat?Q=ico%3A23132221](https://www.hlidacstatu.cz/dotace/hledat?Q=ico%3A23132221)
- F7815 · grant\_national · Sourced · [https://smlouvy\.gov\.cz/smlouva/39346345](https://smlouvy.gov.cz/smlouva/39346345)
- F7816 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27ValkaAI%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27ValkaAI%27)
- F7817 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
