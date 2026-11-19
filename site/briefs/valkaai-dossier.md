# ValkaAI — due diligence brief

valka\.ai · Valka\.AI s\.r\.o\. · IČO 23132221 · CZ · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A platform selling real\-time synthetic video and AI personas \(AI commentators, interactive avatars\) to entertainment and streaming customers\. *(Partly verified)* ^[1](https://valka.ai/),[2](https://valka.ai/),[3](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- **Stage & traction.** Pre\-seed with large institutional rounds \(€12M announced, later reported €13M extension\) and a national grant; public press coverage claims \~45–50 headcount\. *(Verified)* ^[4](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[5](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[6](https://smlouvy.gov.cz/smlouva/39346345),[7](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- **Technology & moat.** Company claims a 'language of motion', proprietary control model and three\-tiered real‑time synthesis across video, audio and event understanding—asserted research/IP rather than independently verified patents\. *(Partly verified)* ^[8](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[9](https://valka.ai/blog/valkaai-raises-12-million),[10](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[11](https://patents.google.com/?assignee=valkaai)
- **Key risk.** Core IP and production\-readiness are primarily company claims with no assignee patents found; this undermines defensibility if claims cannot be proven or reproduced\. *(Analyst view)* ^[11](https://patents.google.com/?assignee=valkaai),[8](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[9](https://valka.ai/blog/valkaai-raises-12-million)
- **Diligence focus.** First verify live deployments/customers and latency/compute metrics for the 'real\-time' commentator/avatar products because business scalability hinges on operating cost and clear customer integrations\. *(Analyst view)* ^[12](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[2](https://valka.ai/),[13](https://crt.sh/?q=%25.valka.ai&output=json)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2026\-02\-24 · pre\-seed · €12 million · Rockaway Ventures, J&amp;T Ventures, Tensor Ventures, BD Partners, Fond Naše Česko, Petr Zámeč · 7 reports; 2026\-11\-12 · pre\-seed · €13 million · Look AI Ventures, ff Venture Capital, Rockaway Ventures, J&amp;T Ventures, Tensor Ventures, BD · 2 reports | 4, 14, 15, 16, 17, 18 |
| Public money | 1 grant\(s\), 20\.6M CZK | 6 |
| Hiring | 5 open roles: other 2, ml research 2, engineering 1 | 19, 20, 21, 22, 23 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; own\-model evidence: 0 papers, 0 verified HF models, 3 ML roles, 2 own\-model claims | 24, 8, 19 |
| Engineering footprint | product surfaces: api\.bots\.dev\.valka\.ai, api\.bots\.prd\.valka\.ai, api\.bots\.valka\.ai, api\.matchvision\.dev\.valka\.ai, api\.matchvision\.valka\.ai, auth\.bots\.dev\.valka\.ai; stack: Next\.js | 13, 25, 26 |
| Claims checked | Patents: not found | 11 |
| Timeline | Czech entity registered 2025\-04\-01; first press 2025\-05\-12 \(25 articles collected\) | 27, 28 |

# Detailed findings

## Ownership and capital

- Registry: Valka\.AI s\.r\.o\. incorporated 2025\-04\-01; 100% owned by Valka\.AI B\.V\. \(Netherlands\) per registry\. *(Verified)* ^[27](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221),[29](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221),[30](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23132221)
- Funding: announced €12M pre\-seed \(Rockaway\-led\) and later reporting of a €13M pre\-seed extension with additional investors \(Look AI, ff VC\)\. *(Partly verified)* ^[4](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[5](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[31](https://valka.ai/blog/valkaai-raises-12-million)
- Public money: a Czech ministry grant of 20,563,542 Kč was recorded \(signed 2026\-09\-01\)\. *(Verified)* ^[6](https://smlouvy.gov.cz/smlouva/39346345)

## Technology profile

- Core product capabilities: live AI commentators and real\-time interactive AI avatars for sports/streaming, per company product pages and press announcements\. *(Partly verified)* ^[2](https://valka.ai/),[12](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[3](https://vestbee.com/insights/articles/valka-ai-raises-12-m)
- Engineering footprint: public API subdomains exist \(api\.bots\*\.valka\.ai, api\.matchvision\*\.valka\.ai, auth\.bots\.dev\.\.\.\), indicating API surfaces for bots and match/event processing\. *(Verified)* ^[13](https://crt.sh/?q=%25.valka.ai&output=json),[25](https://crt.sh/?q=%25.valka.ai&output=json),[26](https://crt.sh/?q=%25.valka.ai&output=json),[32](https://crt.sh/?q=%25.valka.ai&output=json),[33](https://crt.sh/?q=%25.valka.ai&output=json),[34](https://crt.sh/?q=%25.valka.ai&output=json)
- ML / hiring: open roles include LLM Researcher, TTS Research Scientist and Applied Science intern—signals active ML research hiring\. *(Company claim)* ^[22](https://valka.ai/careers),[23](https://valka.ai/careers),[19](https://valka.ai/careers)

## Rebuild check

- **Commodity:** Live commentary generation from event data — a minimal MVP \(event\-&gt;speech\) could be rebuilt quickly using event feeds plus TTS/APIs; ValkaAI markets this capability\. *(Analyst view)* ^[12](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[2](https://valka.ai/)
  - Assumption: Use of off\-the\-shelf TTS and event parsers
- **Hard to copy:** Claimed proprietary 'language of motion' and control model enabling real‑time synchronized voice, motion and visuals across frames; company ties this to production\-grade visual consistency\. *(Analyst view)* ^[8](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[35](https://valka.ai/blog/valkaai-raises-12-million),[9](https://valka.ai/blog/valkaai-raises-12-million)
  - Assumption: Proprietary model and training data exist as claimed
- **Verdict:** Quarter — a competent small team can rebuild a basic commentator in a month, but reproducing claimed real‑time, frame‑consistent avatars with proprietary control and synchronization would likely take a quarter\-plus and lack the company's claimed control\-model and training data\. *(Analyst view)* ^[12](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[8](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[9](https://valka.ai/blog/valkaai-raises-12-million),[13](https://crt.sh/?q=%25.valka.ai&output=json)
  - Assumption: No access to ValkaAI's proprietary datasets or control\-model weights

## Risks and caveats

- Unverified IP: company asserts patents/research but patent search shows no publications assigned to 'valkaai'\. *(Analyst view)* ^[11](https://patents.google.com/?assignee=valkaai),[24](https://www.valka.ai/company)
- Concentration of early capital and public grant exposure could create milestone pressure; large pre\-seed sums reported and a significant national grant recorded\. *(Analyst view)* ^[4](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[5](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[6](https://smlouvy.gov.cz/smlouva/39346345)
- Scale risk: product claims real\-time, low\-latency synthesis but no independent performance or named customer deployments are verifiable in facts provided\. *(Analyst view)* ^[35](https://valka.ai/blog/valkaai-raises-12-million),[12](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[2](https://valka.ai/)

## Questions for founders

- Provide customer references, signed contracts, and live deployment metrics for the ValkaAI Commentator \(latency, concurrency, pricing\), citing the product launch claims\. *(Analyst view)* ^[12](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[2](https://valka.ai/)
- Produce IP evidence: patent applications/assignments, dataset provenance or model checkpoints to substantiate the claimed proprietary control model and 'language of motion'\. *(Analyst view)* ^[8](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[9](https://valka.ai/blog/valkaai-raises-12-million),[11](https://patents.google.com/?assignee=valkaai)
- Share architecture and cost estimates \(GPU/RT compute\) for real‑time avatar synthesis to validate unit economics and scalability assumptions behind 'real\-time' claims\. *(Analyst view)* ^[35](https://valka.ai/blog/valkaai-raises-12-million),[8](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
- Clarify whether the stack relies on third‑party LLM/TT S providers or fully on in‑house models, given statements of own\-model development\. *(Analyst view)* ^[10](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/),[8](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures),[22](https://valka.ai/careers)

## Sources

1. [valka\.ai](https://valka.ai/) · Company's own website · Product capability — “We create synthetic video for sports and media using lifelike characters with real agency\.”
2. [valka\.ai](https://valka.ai/) · Company's own website · Product capability — “Live commentary, generated for the audience actually listening\.”
3. [vestbee\.com](https://vestbee.com/insights/articles/valka-ai-raises-12-m) · Independent press · Product capability — “ValkaAI develops real\-time interactive video technology using AI\-driven digital avatars\. The company’s platform generates synthetic video content on demand, including AI commentators and digital characters that react to live events and user interactions\.”
4. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures) · Independent press · Funding round — “The company has raised €12 million in a pre\-seed funding round led by Rockaway Ventures, with participation from J&amp;T Ventures, Tensor Ventures, BD Partners, and Fond Naše Česko\.”
5. [lookai\.vc](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/) · Independent press · Funding round — “Look AI Ventures has joined ValkaAI‘s pre\-seed round alongside ff Venture Capital, bringing the round to €13 million\.”
6. [smlouvy\.gov\.cz](https://smlouvy.gov.cz/smlouva/39346345) · Official record · National grant · 2026 — “Poskytnutí účelové podpory · Ministerstvo průmyslu a obchodu · 20 563 542 CZK”
7. [vestbee\.com](https://vestbee.com/insights/articles/valka-ai-raises-12-m) · Independent press · Team claim — “ValkaAI operates teams in San Francisco, Prague, and Dubai and employs around 45 people, including researchers from Meta and DeepMind\.”
8. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures) · Independent press · Technical claim — “The ValkaAI team is currently focused on developing fully controlled, real\-time AI synthesis of motion and visuals\. Instead of generating entire video segments at once, which is slow and computationally demanding, the system works with an efficient representation, a ‘language of motion,’ and a proprietary control model…”
9. [valka\.ai](https://valka.ai/blog/valkaai-raises-12-million) · Company's own website · Technical claim — “Our unique three\-tiered genAI process will be able to create the technology for on\-demand content at scale and without the technical limitations we currently see with AI\-generated video”
10. [lookai\.vc](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/) · Independent press · Technical claim — “Its own technology\. Instead of building on top of existing generative AI models, ValkaAI develops its own across three research areas: video generation, audio generation, and event understanding\.”
11. [patents\.google\.com](https://patents.google.com/?assignee=valkaai) · Official record · Independent check of a claim — “No publication with assignee starting with 'valkaai' on Google Patents\.”
12. [lookai\.vc](https://lookai.vc/look-ai-ventures-joins-valkaai-13m-pre-seed-round/) · Independent press · Product capability — “ValkaAI Commentator , launched this year, generates live sports and esports commentary directly from event data\.”
13. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-10\-08 — “api\.bots\.dev\.valka\.ai \(first certificate 2025\-10\-08\)”
14. [valka\.ai](https://valka.ai/company) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
15. [valka\.ai](https://www.valka.ai/company) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
16. [valka\.ai](https://valka.ai/privacy-policy) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
17. [valka\.ai](https://www.valka.ai/privacy-policy) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
18. [valka\.ai](https://valka.ai/blog) · Company's own website · Funding round — “We're thrilled to announce ValkaAl has received €12M pre\-seed funding”
19. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “Applied Science Intern \- World Models”
20. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “Senior Product Manager”
21. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “Kotlin Developer”
22. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “LLM Researcher”
23. [valka\.ai](https://valka.ai/careers) · Company's own website · Job posting — “Research Scientist \(Text\-To\-Speech\)”
24. [valka\.ai](https://www.valka.ai/company) · Company's own website · Technical claim — “With a PhD in computer graphics, he has co\-authored leading SIGGRAPH and CVPR papers, co\-invented several patents, and developed AI models for stylized and photorealistic digital humans – bridging academic research with production\-grade results\.”
25. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-01\-28 — “api\.bots\.prd\.valka\.ai \(first certificate 2026\-01\-28\)”
26. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-01\-29 — “api\.bots\.valka\.ai \(first certificate 2026\-01\-29\)”
27. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221) · Official record · Registry: incorporation · 2025\-04\-01 — “registered 2025\-04\-01”
28. [cc\.cz](https://cc.cz/jeho-startup-rychle-roste-ted-zavetril-dalsi-prilezitost-vyviji-lidskeho-avatara-pro-hry-a-igaming/) · Independent press · Press article · 2025\-05\-12 — “Jeho startup rychle roste, teď zavětřil další příležitost \- CzechCrunch”
29. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/23132221) · Official record · Registry: identity · 2025\-04\-01 — “Valka\.AI s\.r\.o\. · s\.r\.o\. · registered 2025\-04\-01”
30. [ares\.gov\.cz](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/23132221) · Official record · Registry: shareholder · 2025\-04\-01 — “Valka\.AI B\.V\. · 100\.0% · from 2025\-04\-01”
31. [valka\.ai](https://valka.ai/blog/valkaai-raises-12-million) · Company's own website · Funding round — “we’re thrilled about our first external capital—€12M pre\-seed funding, led by Rockaway Ventures, with participation from J&amp;T Ventures, Tensor Ventures, BD Partners, Fond Naše Česko and Petr Zámečník\.”
32. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-09\-25 — “api\.matchvision\.dev\.valka\.ai \(first certificate 2026\-09\-25\)”
33. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-09\-25 — “api\.matchvision\.valka\.ai \(first certificate 2026\-09\-25\)”
34. [crt\.sh](https://crt.sh/?q=%25.valka.ai&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-04\-09 — “auth\.bots\.dev\.valka\.ai \(first certificate 2026\-04\-09\)”
35. [valka\.ai](https://valka.ai/blog/valkaai-raises-12-million) · Company's own website · Technical claim — “This type of work involves synchronization across voice, motion, cognition, and infrastructure\.”
36. [cc\.cz](https://cc.cz/rekordni-investici-cesky-startup-jeste-navysil-tvurci-ai-komentatora-ziskali-uz-stovky-milionu/) · Independent press · Funding round — “úvodní, tzv\. pre\-seedovou investici ve výši téměř 300 milionů korun”

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

Analysis: gpt\-5\-mini (cost $0.0100); AI extraction cost $0.0101. Full fact table: CSV export.

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
- F5482 · source\_check · Checked · no results · [https://www\.hlidacstatu\.cz/dotace/hledat?Q=ico%3A23132221](https://www.hlidacstatu.cz/dotace/hledat?Q=ico%3A23132221)
- F5483 · grant\_national · Sourced · [https://smlouvy\.gov\.cz/smlouva/39346345](https://smlouvy.gov.cz/smlouva/39346345)
- F5484 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27ValkaAI%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27ValkaAI%27)
- F5485 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
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
