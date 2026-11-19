# Valpas — due diligence brief

valpashotels\.com · FI · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** IoT smart bed legs plus mobile/web AI that provides room\-level 'bed bug\-safe' certification and an LLM Visibility audit product for hotels and travel platforms\. *(Partly verified)* ^[1](https://siliconcanals.com/helsinki-based-valpas-raises-4m/),[2](https://siliconcanals.com/helsinki-based-valpas-raises-4m/),[3](https://valpashotels.com/about),[4](https://optimiser.valpashotels.com/)
- **Stage & traction.** Seed round \~€4M with Zenith, Icebreaker, Tesi, Canon/Global Brain et al\.; prior seed activity with Icebreaker/Reaktor; customer roster claims &gt;300 hotels including Accor\-family and case studies\. *(Corroborated)* ^[5](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/),[6](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709),[7](https://siliconcanals.com/helsinki-based-valpas-raises-4m/),[8](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/)
- **Technology & moat.** Granted patent\(s\) for a 'bed bug monitoring furniture leg' plus deployed IoT hardware and image\-recognition claims—patent \+ hardware integrations are the primary defensibility signals\. *(Verified)* ^[9](https://patents.google.com/?assignee=valpas),[1](https://siliconcanals.com/helsinki-based-valpas-raises-4m/),[10](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/)
- **Key risk.** Material customer\-validation gaps—some named case studies lack independent corroboration while commercial claims reference large hotel groups; customer concentration and unverifed enterprise references matter\. *(Analyst view)* ^[11](https://valpashotels.com/case-studies),[12](https://valpashotels.com/case-studies),[7](https://siliconcanals.com/helsinki-based-valpas-raises-4m/)
- **Diligence focus.** First verify patent family scope and enforceability, and independently confirm paid deployments with Accor/other major brands \(contracts, rollout counts, revenue per room\)\. *(Analyst view)* ^[9](https://patents.google.com/?assignee=valpas),[7](https://siliconcanals.com/helsinki-based-valpas-raises-4m/),[13](https://bedbugsjapan.com/bed-bug-protection-hotels-japan-valpas)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2024\-06\-26 · Seed · €4 million · Zenith VC, Icebreaker VC, Finnish Industry Investment, Canon Marketing Japan MIRAI Fund, A · 4 reports; date n/a · Icebreaker, Reaktor | 5, 14, 8, 15, 6 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; integrates with customers' OpenAI \(not a dependency\); own\-model evidence: 1 papers, 0 verified HF models, 0 ML roles, 3 own\-model claims | 16, 17, 3, 18 |
| Engineering footprint | product surfaces: api\.valpashotels\.com, app\.valpashotels\.com, dashboard\.valpashotels\.com, docs\.valpashotels\.com; stack: Next\.js, Vercel | 19, 20, 21 |
| Customers | 10 named: RUNO Hotel, Kamisuwa Onsen Shinyu, Kabin Hotel Group, Hotel Prince de Galles, Sokos Hotels Kupittaa; public pricing: yes; 2 mobile app\(s\) | 22, 23, 24, 25, 26 |
| Claims checked | Customer \(Kabin Hotel Group\): confirmed; Patents: confirmed; Customer \(Kamisuwa Onsen Shinyu, RUNO Hotel\): not found | 13, 9, 11, 12 |
| Timeline | first press 2023\-10\-06 \(16 articles collected\) | 27 |

# Detailed findings

## Ownership and capital

- Seed round: €4M reported \(June 2024 press\) with investors including Zenith VC \(lead\), Icebreaker VC, Finnish Industry Investment/Tesi, Canon Marketing Japan MIRAI Fund, Activum SG Ventures, Houghton Street, Rockaway, Morrow, Reaktor, Global Brain\. *(Corroborated)* ^[5](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/),[8](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/),[14](https://techfundingnews.com/finnish-startup-valpas-raises-e4m-for-chemical-free-bedbug-safety-tech/),[15](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/)
- Prior financing: earlier seed/angel activity reported in 2017 involving Icebreaker and Reaktor \(single\-source press report\)\. *(Single source)* ^[6](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709)

## Technology profile

- Product surfaces: public subdomains and apps—api\., app\., dashboard\., docs\.; mobile apps listed on iOS and Google Play\. *(Verified)* ^[21](https://crt.sh/?q=%25.valpashotels.com&output=json),[19](https://crt.sh/?q=%25.valpashotels.com&output=json),[20](https://crt.sh/?q=%25.valpashotels.com&output=json),[28](https://crt.sh/?q=%25.valpashotels.com&output=json),[29](https://apps.apple.com/us/app/valpas-for-travelers/id6753011582?uo=4)
- Built capabilities: smart anti\-bedbug bed legs \(IoT\), real\-time room monitoring/alerts, and in‑app image recognition for pest ID; claims pesticide\-free operation\. *(Corroborated)* ^[1](https://siliconcanals.com/helsinki-based-valpas-raises-4m/),[30](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709),[10](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/)
- AI products: 'LLM Visibility Report' and optimiser that queries multiple LLMs; site states integration with ChatGPT \(OpenAI\)\. *(Company claim)* ^[4](https://optimiser.valpashotels.com/),[31](https://optimiser.valpashotels.com/),[16](https://valpashotels.com/)

## Rebuild check

- **Commodity:** LLM Visibility audit \(Visibility Score, Data Gaps, Quick Wins\) — could be rebuilt by 2–3 engineers using OpenAI \+ web scraping/APIs\. *(Analyst view)* ^[4](https://optimiser.valpashotels.com/),[32](https://optimiser.valpashotels.com/),[16](https://valpashotels.com/),[31](https://optimiser.valpashotels.com/)
  - Assumption: access to OpenAI or equivalent LLM API
- **Hard to copy:** Patented smart bed legs combined with deployed IoT hardware, sensors and image‑recognition workflow—granted patent\(s\) found \(EP3468360B1\) and hardware deployment claims\. *(Analyst view)* ^[9](https://patents.google.com/?assignee=valpas),[1](https://siliconcanals.com/helsinki-based-valpas-raises-4m/),[30](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709)
  - Assumption: patent covers key functional claims
- **Verdict:** Quarter — software\-only clone possible in weeks, full hardware\+patent‑safe clone takes a quarter or more and still lacks granted patent coverage, installed hotel rollouts, and verified large\-brand contracts\. *(Analyst view)* ^[4](https://optimiser.valpashotels.com/),[9](https://patents.google.com/?assignee=valpas),[7](https://siliconcanals.com/helsinki-based-valpas-raises-4m/)
  - Assumption: hardware manufacturing and certification required

## Risks and caveats

- Integration/dependency risk: company states integration with ChatGPT/OpenAI for AI features — product reliance on a third‑party LLM increases operational and cost exposure\. *(Analyst view)* ^[16](https://valpashotels.com/)
- Customer\-reference risk: independent corroboration exists for Kabin Hotel Group but some other named case studies \(e\.g\., RUNO, Kamisuwa Onsen\) are unverified in independent checks\. *(Analyst view)* ^[13](https://bedbugsjapan.com/bed-bug-protection-hotels-japan-valpas),[11](https://valpashotels.com/case-studies),[12](https://valpashotels.com/case-studies)
- Performance/impact claims: environmental \(1\.4t CO2e per room\) and financial \(NOI/GOP uplift, capitalised fee accounting\) are asserted on site but lack independent validation in provided facts\. *(Analyst view)* ^[33](https://valpashotels.com/),[26](https://valpashotels.com/),[34](https://valpashotels.com/)

## Questions for founders

- Please produce the patent family claim chart: which specific claims of EP3468360B1 cover the active lure, trap, sensor and data certification functions? \(ref: EP3468360B1 / 6390\)\. *(Analyst view)* ^[9](https://patents.google.com/?assignee=valpas),[35](https://patents.google.com/patent/EP3468360B1)
- For major enterprise references \(Accor, The Luxury Collection\): provide signed contracts, deployment counts, ARR per room and churn; press claims currently cite 300\+ hotels but need revenue verification\. *(Analyst view)* ^[7](https://siliconcanals.com/helsinki-based-valpas-raises-4m/),[8](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/)
- Share independent test reports or confusion matrices for the image\-recognition and sensor detection pipeline \(accuracy, false positive/negative rates\) referenced in press and product copy\. *(Analyst view)* ^[10](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/),[30](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709)
- Provide customer\-level billing/contract treatment showing the 'all\-inclusive annual fee' is capitalised and examples of asset accounting entries with auditor confirmation\. *(Analyst view)* ^[26](https://valpashotels.com/)

## Sources

1. [siliconcanals\.com](https://siliconcanals.com/helsinki-based-valpas-raises-4m/) · Independent press · Product capability — “Valpas has developed a solution that centres on smart anti\-bedbug bed legs\.”
2. [siliconcanals\.com](https://siliconcanals.com/helsinki-based-valpas-raises-4m/) · Independent press · Product capability — “IoT and AI\-enabled mobile web app then provide in\-app image recognition to identify and dispose of the pests\.”
3. [valpashotels\.com](https://valpashotels.com/about) · Company's own website · Product capability — “Valpas makes pest control obsolete\. With Valpas' patented smart bed legs installed, hotels are able to enjoy permanent protection from bed bug infestations and offer every guest rock\-solid digital certification that their room is bed bug\-safe\.”
4. [optimiser\.valpashotels\.com](https://optimiser.valpashotels.com/) · Company's own website · Product capability — “LLM Visibility Report Grand Hotel Example V 74 Score 8 Gaps 12 Wins Enter your email to unlock What We Analyze Three dimensions of AI visibility 01 Visibility Score See how well AI assistants can understand and recommend your hotel to potential guests\.”
5. [tech\.eu](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/) · Independent press · Funding round — “Valpas has secured €4 million in Seed funding\.”
6. [nordic9\.com](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709) · Independent press · Funding round — “Prior to this deal, Valpas raised money from Icebreaker and Reaktor in 2017\.”
7. [siliconcanals\.com](https://siliconcanals.com/helsinki-based-valpas-raises-4m/) · Independent press · Customer — “The company is already working with over 300 hotels flagged under premium brands including Accor Hotels, The Luxury Collection, Design Hotels, ARP\-Hansen, and Bob W in over 40 destinations – amongst others across Europe, Mexico, and Japan\.”
8. [arctictoday\.com](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/) · Independent press · Funding round — “Valpas raised €4m in seed funding led by Zenith Venture Capital”
9. [patents\.google\.com](https://patents.google.com/?assignee=valpas) · Official record · Independent check of a claim — “1 granted patent\(s\) found, e\.g\. EP3468360B1\.”
10. [tech\.eu](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/) · Independent press · Technical claim — “Valpas’ IoT and AI\-enabled mobile web app then provides in\-app image recognition to identify and dispose of the pests\.”
11. [valpashotels\.com](https://valpashotels.com/case-studies) · Company's own website · Independent check of a claim
12. [valpashotels\.com](https://valpashotels.com/case-studies) · Company's own website · Independent check of a claim
13. [bedbugsjapan\.com](https://bedbugsjapan.com/bed-bug-protection-hotels-japan-valpas) · Independent press · Independent check of a claim — “The three Nagano hotels installed Valpas in all rooms as prevention and say no bed bugs had been found there \(DX Magazine, in Japanese\)\. The WAYFARER and KABIN groups say Valpas runs in every room of their hotels\. To see every hotel with a stated measure, open the map and keep “Hotel safety measures”
14. [techfundingnews\.com](https://techfundingnews.com/finnish-startup-valpas-raises-e4m-for-chemical-free-bedbug-safety-tech/) · Independent press · Funding round — “The round was led by Zenith VC \(which invested in Treyd and Freshsound \) alongside Icebreaker VC, Finnish Industry Investment, Canon Marketing Japan MIRAI Fund, Activum SG Ventures, Houghton Street Ventures, Rockaway Ventures and Morrow Ventures\.”
15. [arctictoday\.com](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/) · Independent press · Funding round — “Canon as an investor in Valpas’ vision of safe, seamless and sustainable travel via Canon Marketing Japan and Global Brain Corporation \.”
16. [valpashotels\.com](https://valpashotels.com/) · Company's own website · Integration — “Integrated with ChatGPT\.”
17. [valpashotels\.com](https://valpashotels.com/about) · Company's own website · Product capability — “Valpas makes pest control obsolete\. With Valpas' patented smart bed legs installed, hotels are able to enjoy permanent protection from bed bug infestations and offer every guest rock\-solid digital certification that their room is bed bug\-safe\.”
18. [valpashotels\.com](https://valpashotels.com/about) · Company's own website · Technical claim — “Valpas' patented smart bed legs installed”
19. [crt\.sh](https://crt.sh/?q=%25.valpashotels.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2022\-08\-03 — “app\.valpashotels\.com \(first certificate 2022\-08\-03\)”
20. [crt\.sh](https://crt.sh/?q=%25.valpashotels.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2023\-01\-09 — “dashboard\.valpashotels\.com \(first certificate 2023\-01\-09\)”
21. [crt\.sh](https://crt.sh/?q=%25.valpashotels.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2024\-12\-10 — “api\.valpashotels\.com \(first certificate 2024\-12\-10\)”
22. [valpashotels\.com](https://valpashotels.com/case-studies) · Company's own website · Customer — ““We want guests staying with us to feel that everything has been thought through down to the smallest detail\.””
23. [valpashotels\.com](https://valpashotels.com/case-studies) · Company's own website · Customer — ““Attracting more customers with visible travel assurance””
24. [valpashotels\.com](https://valpashotels.com/case-studies) · Company's own website · Customer — ““With Valpas, we safeguard long\-term property value by preventing costly incidents that lead to downtime\.””
25. [valpashotels\.com](https://valpashotels.com/case-studies) · Company's own website · Customer — ““Cost savings and guaranteed guest promise of safety and comfort””
26. [valpashotels\.com](https://valpashotels.com/) · Company's own website · Pricing — “Accounting\-wise, the all\-inclusive annual Valpas fee sits outside the P&amp;L – capitalised as an asset improvement, not an operational cost\.”
27. [tech\.eu](https://tech.eu/2023/10/06/this-startup-has-the-solution-to-the-paris-bed-bug-bedlam/) · Independent press · Press article · 2023\-10\-06 — “This startup has the solution to the Paris bed bug bedlam \- Tech\.eu”
28. [crt\.sh](https://crt.sh/?q=%25.valpashotels.com&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-03\-12 — “docs\.valpashotels\.com \(first certificate 2026\-03\-12\)”
29. [apps\.apple\.com](https://apps.apple.com/us/app/valpas-for-travelers/id6753011582?uo=4) · Public technical artifact · Mobile app · 2025\-10\-15 — “Valpas for Travelers”
30. [nordic9\.com](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709) · Independent press · Product capability — “Hotels just replace their existing bed legs with Valpas’ smart bed legs, and can instantly start monitoring rooms in real\-time and receive notifications of eliminated bed bug incidents caught inside the legs\.”
31. [optimiser\.valpashotels\.com](https://optimiser.valpashotels.com/) · Company's own website · Technical claim — “Our AI queries multiple LLMs and cross\-references your online presence\.”
32. [optimiser\.valpashotels\.com](https://optimiser.valpashotels.com/) · Company's own website · Product capability — “Three dimensions of AI visibility”
33. [valpashotels\.com](https://valpashotels.com/) · Company's own website · Technical claim — “1\.4t CO₂e saved per room, per year\.”
34. [valpashotels\.com](https://valpashotels.com/) · Company's own website · Technical claim — “Valpas turns unpredictable opex into capitalised, permanent infrastructure that improves GOP, NOI and asset value\.”
35. [patents\.google\.com](https://patents.google.com/patent/EP3468360B1) · Official record · Patent publication — “EP3468360B1 · Bed bug monitoring furniture leg · Valpas Enterprises Oy”
36. [patents\.google\.com](https://patents.google.com/patent/EM37625250001S) · Official record · Patent publication — “EM37625250001S · Destruction of pests \(Traps and articles for \-\); Furniture feet · Valpas Enterprises Oy”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 1 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | hlidac\_statu, starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 16 | press:arcticstartup\.com, press:avoindata\.prh\.fi, press:businesswire\.com, press:eu\-startups\.com, press:finsmes\.com, press:founderstoday\.news, press:medium\.com, press:traveldailymedia\.com |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 17 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 36 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 1 | — |
| Mobile apps | App Store \(seller must match the company\), Google Play if linked from the site | 2 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 5 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 6 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 53 | — |

Analysis: gpt\-5\-mini (cost $0.0094); AI extraction cost $0.0075. Full fact table: CSV export.

## Source appendix (all collected facts)

- F3705 · registry\_flag · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F3706 · web\_page · Sourced · [https://valpashotels\.com/](https://valpashotels.com/)
- F3707 · web\_page · Sourced · [https://valpashotels\.com/careers](https://valpashotels.com/careers)
- F3708 · web\_page · Sourced · [https://valpashotels\.com/privacy\-policy](https://valpashotels.com/privacy-policy)
- F3709 · web\_page · Sourced · [https://valpashotels\.com/en/privacy\-policy](https://valpashotels.com/en/privacy-policy)
- F3710 · web\_page · Sourced · [https://valpashotels\.com/impact\-and\-scope](https://valpashotels.com/impact-and-scope)
- F3711 · web\_page · Sourced · [https://valpashotels\.com/technology](https://valpashotels.com/technology)
- F3712 · web\_page · Sourced · [https://valpashotels\.com/guest\-need\-of\-the\-decade](https://valpashotels.com/guest-need-of-the-decade)
- F3713 · web\_page · Sourced · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F3714 · web\_page · Sourced · [https://valpashotels\.com/about](https://valpashotels.com/about)
- F3715 · web\_page · Sourced · [https://valpashotels\.com/changelog](https://valpashotels.com/changelog)
- F3716 · web\_page · Sourced · [https://valpashotels\.com/case\-studies/prince\-de\-galles](https://valpashotels.com/case-studies/prince-de-galles)
- F3717 · web\_page · Sourced · [https://valpashotels\.com/case\-studies/sokos\-hotel\-kupittaa](https://valpashotels.com/case-studies/sokos-hotel-kupittaa)
- F3718 · web\_page · Sourced · [https://valpashotels\.com/blog](https://valpashotels.com/blog)
- F3719 · web\_page · Sourced · [https://valpashotels\.com/news](https://valpashotels.com/news)
- F3720 · web\_page · Sourced · [https://valpashotels\.com/blog/how\-guestapart\-turned\-bed\-bug\-safety\-into\-eur24\-more\-in\-direct\-booking\-revenue\-per\-room\-per\-month\-with\-a\-3x\-return](https://valpashotels.com/blog/how-guestapart-turned-bed-bug-safety-into-eur24-more-in-direct-booking-revenue-per-room-per-month-with-a-3x-return)
- F3721 · web\_page · Sourced · [https://travel\-managers\.valpashotels\.com/](https://travel-managers.valpashotels.com/)
- F3722 · web\_page · Sourced · [https://optimiser\.valpashotels\.com/](https://optimiser.valpashotels.com/)
- F3723 · tech\_stack · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F3724 · tech\_stack · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F3725 · tech\_stack · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F3726 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=valpashotels\.com&amp;type=MX](https://dns.google/resolve?name=valpashotels.com&type=MX)
- F3727 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3728 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3729 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3730 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3731 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3732 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3733 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3734 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3735 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3736 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3737 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3738 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3739 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3740 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3741 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3742 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3743 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3744 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3745 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3746 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3747 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3748 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3749 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3750 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3751 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3752 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3753 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3754 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3755 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3756 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3757 · subdomain · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3758 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.valpashotels\.com&amp;output=json](https://crt.sh/?q=%25.valpashotels.com&output=json)
- F3759 · paper · Medium confidence · [https://openalex\.org/W2324058551](https://openalex.org/W2324058551)
- F3760 · app · Sourced · [https://apps\.apple\.com/us/app/valpas\-for\-travelers/id6753011582?uo=4](https://apps.apple.com/us/app/valpas-for-travelers/id6753011582?uo=4)
- F3761 · app · Medium confidence · [https://valpashotels\.com](https://valpashotels.com)
- F3762 · wayback\_first · Sourced · [https://web\.archive\.org/web/20190419123450/http://www\.valpashotels\.com:80/](https://web.archive.org/web/20190419123450/http://www.valpashotels.com:80/)
- F3763 · wayback\_first · Sourced · [https://web\.archive\.org/web/20210922165038/https://www\.valpashotels\.com/careers](https://web.archive.org/web/20210922165038/https://www.valpashotels.com/careers)
- F3764 · wayback\_first · Sourced · [https://web\.archive\.org/web/20190421054811/http://www\.valpashotels\.com:80/jobs](https://web.archive.org/web/20190421054811/http://www.valpashotels.com:80/jobs)
- F3765 · wayback\_first · Sourced · [https://web\.archive\.org/web/20190421054800/http://www\.valpashotels\.com:80/blog](https://web.archive.org/web/20190421054800/http://www.valpashotels.com:80/blog)
- F3766 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/valpashotels\.com](https://web.archive.org/web/%2A/valpashotels.com)
- F3770 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3771 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3772 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3773 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3774 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3775 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3776 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3777 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3778 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3779 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3780 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3781 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3782 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3783 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3784 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3785 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3786 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3787 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3788 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F3789 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F3790 · source\_unavailable · Unavailable · [https://avoindata\.prh\.fi/opendata\-ytj\-api/v3/companies?businessId=2575159\-9](https://avoindata.prh.fi/opendata-ytj-api/v3/companies?businessId=2575159-9)
- F3791 · source\_unavailable · Unavailable · [https://www\.finsmes\.com/?p=136222](https://www.finsmes.com/?p=136222)
- F3792 · press\_mention · Sourced · [https://tech\.eu/2024/06/26/pest\-control\-startup\-valpas\-raised\-4m\-seed\-for\-pesticide\-free\-bed\-bug\-solution/](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/)
- F3793 · press\_mention · Sourced · [https://thehub\.io/startups/valpas](https://thehub.io/startups/valpas)
- F3794 · press\_mention · Sourced · [https://play\.google\.com/store/apps/details?id=com\.quody\.valpasapp&amp;hl=en\_US](https://play.google.com/store/apps/details?id=com.quody.valpasapp&hl=en_US)
- F3795 · source\_unavailable · Unavailable · [https://medium\.com/zenith\-venture\-capital/solving\-an\-itchy\-problem\-our\-investment\-in\-valpas\-f7948e8fdfa1](https://medium.com/zenith-venture-capital/solving-an-itchy-problem-our-investment-in-valpas-f7948e8fdfa1)
- F3796 · source\_unavailable · Unavailable · [https://www\.finsmes\.com/2024/06/valpas\-raises\-e4m\-in\-seed\-funding\.html](https://www.finsmes.com/2024/06/valpas-raises-e4m-in-seed-funding.html)
- F3797 · press\_mention · Sourced · [https://hsvc\.substack\.com/p/houghton\-street\-community\-newsletter\-3e2](https://hsvc.substack.com/p/houghton-street-community-newsletter-3e2)
- F3798 · press\_mention · Sourced · [https://www\.arctictoday\.com/%F0%9F%87%AB%F0%9F%87%AE\-valpas\-raised\-e4m\-in\-seed\-funding\-led\-by\-zenith\-venture\-capital/](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/)
- F3799 · source\_unavailable · Unavailable · [https://arcticstartup\.com/valpas\-raises\-e4m\-seed/](https://arcticstartup.com/valpas-raises-e4m-seed/)
- F3800 · press\_mention · Sourced · [https://techfundingnews\.com/finnish\-startup\-valpas\-raises\-e4m\-for\-chemical\-free\-bedbug\-safety\-tech/](https://techfundingnews.com/finnish-startup-valpas-raises-e4m-for-chemical-free-bedbug-safety-tech/)
- F3801 · press\_mention · Sourced · [https://siliconcanals\.com/helsinki\-based\-valpas\-raises\-4m/](https://siliconcanals.com/helsinki-based-valpas-raises-4m/)
- F3802 · press\_mention · Sourced · [https://nordic9\.com/news/valpas\-raises\-500k\-in\-a\-seed\-funding\-round\-supported\-by\-maki\-vc\-icebreaker\-vc\-and\-reaktor\-ventures\-news9430502709](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709)
- F3803 · press\_mention · Sourced · [https://theventurecodex\.com/companies/valpas](https://theventurecodex.com/companies/valpas)
- F3804 · source\_unavailable · Unavailable · [https://www\.businesswire\.com/news/home/20240626337541/en/Bedbug\-Safety\-Tech\-Scale\-up\-Valpas\-Attracts\-%E2%82%AC4M\-to\-Accelerate\-Innovative\-Prevention\-Technology](https://www.businesswire.com/news/home/20240626337541/en/Bedbug-Safety-Tech-Scale-up-Valpas-Attracts-%E2%82%AC4M-to-Accelerate-Innovative-Prevention-Technology)
- F3805 · press\_mention · Sourced · [https://thenextweb\.com/news/helsinki\-startup\-valpas\-smart\-bed\-legs\-bed\-bugs](https://thenextweb.com/news/helsinki-startup-valpas-smart-bed-legs-bed-bugs)
- F3806 · press\_mention · Sourced · [https://nordic9\.com/news/valpas\-raised\-4m\-in\-seed\-funding\-led\-by\-zenith\-vc\-joined\-by\-icebreaker\-tesi\-activum\-sg\-houghton\-street\-ventures\-rockaway\-capital\-reaktor\-ventures](https://nordic9.com/news/valpas-raised-4m-in-seed-funding-led-by-zenith-vc-joined-by-icebreaker-tesi-activum-sg-houghton-street-ventures-rockaway-capital-reaktor-ventures)
- F3807 · press\_mention · Sourced · [https://en\.ain\.ua/2024/06/27/valpas\-raises\-4m\-seed\-funding\-for\-bedbug\-prevention/](https://en.ain.ua/2024/06/27/valpas-raises-4m-seed-funding-for-bedbug-prevention/)
- F3808 · press\_mention · Sourced · [https://shorttermrentalz\.com/news/valpas\-seed\-funding\-bedbug\-solution/](https://shorttermrentalz.com/news/valpas-seed-funding-bedbug-solution/)
- F3809 · press\_mention · Sourced · [https://maki\.vc/case/valpas/](https://maki.vc/case/valpas/)
- F3810 · source\_unavailable · Unavailable · [https://www\.traveldailymedia\.com/valpas\-bolsters\-global\-expansion\-as\-it\-hires\-four\-new\-executives/](https://www.traveldailymedia.com/valpas-bolsters-global-expansion-as-it-hires-four-new-executives/)
- F3811 · source\_unavailable · Unavailable · [https://www\.eu\-startups\.com/directory/valpas/](https://www.eu-startups.com/directory/valpas/)
- F3812 · press\_mention · Sourced · [https://tech\.eu/2023/10/06/this\-startup\-has\-the\-solution\-to\-the\-paris\-bed\-bug\-bedlam/](https://tech.eu/2023/10/06/this-startup-has-the-solution-to-the-paris-bed-bug-bedlam/)
- F3813 · source\_unavailable · Unavailable · [https://www\.founderstoday\.news/valpas\-secures\-4\-millions\-in\-funding/](https://www.founderstoday.news/valpas-secures-4-millions-in-funding/)
- F3814 · press\_mention · Sourced · [https://play\.google\.com/store/apps/details?id=com\.whaith\.valpasmobilefortravelers&amp;hl=en\_US](https://play.google.com/store/apps/details?id=com.whaith.valpasmobilefortravelers&hl=en_US)
- F5522 · source\_unavailable · Unavailable · [https://www\.hlidacstatu\.cz/hledat](https://www.hlidacstatu.cz/hledat)
- F5523 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Valpas%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Valpas%27)
- F5524 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F6027 · product\_capability · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F6028 · tech\_claim · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F6029 · tech\_claim · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F6030 · tech\_claim · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F6031 · integration · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F6032 · pricing · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F6033 · tech\_claim · Medium confidence · [https://valpashotels\.com/](https://valpashotels.com/)
- F6034 · product\_capability · Medium confidence · [https://optimiser\.valpashotels\.com/](https://optimiser.valpashotels.com/)
- F6035 · product\_capability · Medium confidence · [https://optimiser\.valpashotels\.com/](https://optimiser.valpashotels.com/)
- F6036 · product\_capability · Medium confidence · [https://optimiser\.valpashotels\.com/](https://optimiser.valpashotels.com/)
- F6037 · pricing · Medium confidence · [https://optimiser\.valpashotels\.com/](https://optimiser.valpashotels.com/)
- F6038 · tech\_claim · Medium confidence · [https://optimiser\.valpashotels\.com/](https://optimiser.valpashotels.com/)
- F6039 · product\_capability · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6040 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6041 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6042 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6043 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6044 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6045 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6046 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6047 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6048 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6049 · customer · Medium confidence · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6050 · product\_capability · Medium confidence · [https://valpashotels\.com/case\-studies/prince\-de\-galles](https://valpashotels.com/case-studies/prince-de-galles)
- F6051 · customer · Medium confidence · [https://valpashotels\.com/case\-studies/prince\-de\-galles](https://valpashotels.com/case-studies/prince-de-galles)
- F6052 · customer · Medium confidence · [https://valpashotels\.com/case\-studies/prince\-de\-galles](https://valpashotels.com/case-studies/prince-de-galles)
- F6053 · product\_capability · Medium confidence · [https://valpashotels\.com/case\-studies/sokos\-hotel\-kupittaa](https://valpashotels.com/case-studies/sokos-hotel-kupittaa)
- F6054 · customer · Medium confidence · [https://valpashotels\.com/case\-studies/sokos\-hotel\-kupittaa](https://valpashotels.com/case-studies/sokos-hotel-kupittaa)
- F6055 · tech\_claim · Medium confidence · [https://valpashotels\.com/case\-studies/sokos\-hotel\-kupittaa](https://valpashotels.com/case-studies/sokos-hotel-kupittaa)
- F6056 · tech\_claim · Medium confidence · [https://tech\.eu/2024/06/26/pest\-control\-startup\-valpas\-raised\-4m\-seed\-for\-pesticide\-free\-bed\-bug\-solution/](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/)
- F6057 · customer · Medium confidence · [https://tech\.eu/2024/06/26/pest\-control\-startup\-valpas\-raised\-4m\-seed\-for\-pesticide\-free\-bed\-bug\-solution/](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/)
- F6058 · funding\_round · Medium confidence · [https://tech\.eu/2024/06/26/pest\-control\-startup\-valpas\-raised\-4m\-seed\-for\-pesticide\-free\-bed\-bug\-solution/](https://tech.eu/2024/06/26/pest-control-startup-valpas-raised-4m-seed-for-pesticide-free-bed-bug-solution/)
- F6059 · funding\_round · Medium confidence · [https://www\.arctictoday\.com/%F0%9F%87%AB%F0%9F%87%AE\-valpas\-raised\-e4m\-in\-seed\-funding\-led\-by\-zenith\-venture\-capital/](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/)
- F6060 · integration · Medium confidence · [https://www\.arctictoday\.com/%F0%9F%87%AB%F0%9F%87%AE\-valpas\-raised\-e4m\-in\-seed\-funding\-led\-by\-zenith\-venture\-capital/](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/)
- F6061 · team\_claim · Medium confidence · [https://www\.arctictoday\.com/%F0%9F%87%AB%F0%9F%87%AE\-valpas\-raised\-e4m\-in\-seed\-funding\-led\-by\-zenith\-venture\-capital/](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/)
- F6062 · funding\_round · Medium confidence · [https://www\.arctictoday\.com/%F0%9F%87%AB%F0%9F%87%AE\-valpas\-raised\-e4m\-in\-seed\-funding\-led\-by\-zenith\-venture\-capital/](https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-valpas-raised-e4m-in-seed-funding-led-by-zenith-venture-capital/)
- F6063 · funding\_round · Medium confidence · [https://techfundingnews\.com/finnish\-startup\-valpas\-raises\-e4m\-for\-chemical\-free\-bedbug\-safety\-tech/](https://techfundingnews.com/finnish-startup-valpas-raises-e4m-for-chemical-free-bedbug-safety-tech/)
- F6064 · product\_capability · Medium confidence · [https://techfundingnews\.com/finnish\-startup\-valpas\-raises\-e4m\-for\-chemical\-free\-bedbug\-safety\-tech/](https://techfundingnews.com/finnish-startup-valpas-raises-e4m-for-chemical-free-bedbug-safety-tech/)
- F6065 · integration · Medium confidence · [https://techfundingnews\.com/finnish\-startup\-valpas\-raises\-e4m\-for\-chemical\-free\-bedbug\-safety\-tech/](https://techfundingnews.com/finnish-startup-valpas-raises-e4m-for-chemical-free-bedbug-safety-tech/)
- F6066 · team\_claim · Medium confidence · [https://techfundingnews\.com/finnish\-startup\-valpas\-raises\-e4m\-for\-chemical\-free\-bedbug\-safety\-tech/](https://techfundingnews.com/finnish-startup-valpas-raises-e4m-for-chemical-free-bedbug-safety-tech/)
- F6067 · tech\_claim · Medium confidence · [https://techfundingnews\.com/finnish\-startup\-valpas\-raises\-e4m\-for\-chemical\-free\-bedbug\-safety\-tech/](https://techfundingnews.com/finnish-startup-valpas-raises-e4m-for-chemical-free-bedbug-safety-tech/)
- F6069 · product\_capability · Medium confidence · [https://siliconcanals\.com/helsinki\-based\-valpas\-raises\-4m/](https://siliconcanals.com/helsinki-based-valpas-raises-4m/)
- F6070 · product\_capability · Medium confidence · [https://siliconcanals\.com/helsinki\-based\-valpas\-raises\-4m/](https://siliconcanals.com/helsinki-based-valpas-raises-4m/)
- F6071 · product\_capability · Medium confidence · [https://siliconcanals\.com/helsinki\-based\-valpas\-raises\-4m/](https://siliconcanals.com/helsinki-based-valpas-raises-4m/)
- F6072 · customer · Medium confidence · [https://siliconcanals\.com/helsinki\-based\-valpas\-raises\-4m/](https://siliconcanals.com/helsinki-based-valpas-raises-4m/)
- F6073 · tech\_claim · Medium confidence · [https://siliconcanals\.com/helsinki\-based\-valpas\-raises\-4m/](https://siliconcanals.com/helsinki-based-valpas-raises-4m/)
- F6074 · tech\_claim · Medium confidence · [https://nordic9\.com/news/valpas\-raises\-500k\-in\-a\-seed\-funding\-round\-supported\-by\-maki\-vc\-icebreaker\-vc\-and\-reaktor\-ventures\-news9430502709](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709)
- F6075 · product\_capability · Medium confidence · [https://nordic9\.com/news/valpas\-raises\-500k\-in\-a\-seed\-funding\-round\-supported\-by\-maki\-vc\-icebreaker\-vc\-and\-reaktor\-ventures\-news9430502709](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709)
- F6076 · team\_claim · Medium confidence · [https://nordic9\.com/news/valpas\-raises\-500k\-in\-a\-seed\-funding\-round\-supported\-by\-maki\-vc\-icebreaker\-vc\-and\-reaktor\-ventures\-news9430502709](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709)
- F6077 · funding\_round · Medium confidence · [https://nordic9\.com/news/valpas\-raises\-500k\-in\-a\-seed\-funding\-round\-supported\-by\-maki\-vc\-icebreaker\-vc\-and\-reaktor\-ventures\-news9430502709](https://nordic9.com/news/valpas-raises-500k-in-a-seed-funding-round-supported-by-maki-vc-icebreaker-vc-and-reaktor-ventures-news9430502709)
- F6078 · product\_capability · Medium confidence · [https://valpashotels\.com/about](https://valpashotels.com/about)
- F6079 · product\_capability · Medium confidence · [https://valpashotels\.com/about](https://valpashotels.com/about)
- F6080 · tech\_claim · Medium confidence · [https://valpashotels\.com/about](https://valpashotels.com/about)
- F6388 · patent · Sourced · [https://patents\.google\.com/patent/EP3468360B1](https://patents.google.com/patent/EP3468360B1)
- F6389 · patent · Sourced · [https://patents\.google\.com/patent/EM37625250001S](https://patents.google.com/patent/EM37625250001S)
- F6390 · verification · Sourced · [https://patents\.google\.com/?assignee=valpas](https://patents.google.com/?assignee=valpas)
- F6391 · verification · Sourced · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6392 · verification · Sourced · [https://valpashotels\.com/case\-studies](https://valpashotels.com/case-studies)
- F6393 · verification · Sourced · [https://bedbugsjapan\.com/bed\-bug\-protection\-hotels\-japan\-valpas](https://bedbugsjapan.com/bed-bug-protection-hotels-japan-valpas)
