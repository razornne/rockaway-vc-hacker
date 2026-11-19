# Vermeer — due diligence brief

getvermeer\.com · US · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** Vermeer sells a Visual Positioning System \(VPS\) enabling drones and aerial platforms to determine absolute location in GPS‑denied or contested environments using multi‑camera vision and pre‑generated maps\. *(Partly verified)* ^[1](https://www.getvermeer.com/),[2](https://vestbee.com/insights/articles/vermeer-raises-funds),[3](https://www.rockawaycapital.com/en/news/from-hollywood-studios-to-the-frontlines-rockaway-ventures-invests-in-vermeer-the-startup-enabling-drones-to-fly-without-gps)
- **Stage & traction.** Company closed a $10M Series A led by Draper Associates with participation from Rockaway and others and reports &gt;30 customers and defense partnerships\. *(Partly verified)* ^[4](https://scroll.media/en/2025/10/23/vermeer-raises-10m),[5](https://www.getvermeer.com/news),[6](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/)
- **Technology & moat.** Claims include cameras \+ Nvidia‑powered AI and listed US patent numbers, but independent patent search found no publications under 'Vermeer', leaving IP moat unclear\. *(Partly verified)* ^[7](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation),[8](https://www.getvermeer.com/patents),[9](https://patents.google.com/?assignee=vermeer)
- **Key risk.** Core IP and defensive claims \(granted patents, proprietary training footage\) are unverified or contradicted by patent search, risking easy competitive replication or procurement risk for defense customers\. *(Analyst view)* ^[9](https://patents.google.com/?assignee=vermeer),[7](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- **Diligence focus.** First verify patent grant status and assignees, then confirm contractual customer references \(the &gt;30 customers and named defense partners\) to validate revenue durability\. *(Analyst view)* ^[8](https://www.getvermeer.com/patents),[6](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/),[10](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2025\-10\-23 · Series A · $10 million · Rockaway Ventures, Draper Associates, AeroX Ventures, Boscolo Intervest, High Point Ventur · 5 reports | 11, 4, 12, 5, 13 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; own\-model evidence: 10 papers, 0 verified HF models, 0 ML roles, 4 own\-model claims | 14, 8, 15 |
| Engineering footprint | stack: Cloudflare, Webflow |  |
| Claims checked | Patents: not found | 9 |
| Timeline | first press 2025\-10\-23 \(9 articles collected\) | 16 |

# Detailed findings

## Ownership and capital

- Series A $10M reported \(Oct 2025\) with Draper Associates lead and participation from Rockaway Ventures, AeroX, Boscolo Intervest, High Point, and a U\.S\. Air Force Techstars connection\. *(Partly verified)* ^[4](https://scroll.media/en/2025/10/23/vermeer-raises-10m),[5](https://www.getvermeer.com/news),[13](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation),[17](https://www.draper.vc/portfolio/vermeer),[16](https://www.rockawaycapital.com/en/news/from-hollywood-studios-to-the-frontlines-rockaway-ventures-invests-in-vermeer-the-startup-enabling-drones-to-fly-without-gps)

## Technology profile

- Product capabilities: VPS claims GPS‑free absolute localization for aerial platforms, passive operation, mixed‑reality previsualization, and named SKUs \(AVA, VPS‑212, VPS‑160\)\. *(Company claim)* ^[1](https://www.getvermeer.com/),[18](https://www.getvermeer.com/news),[14](https://www.getvermeer.com/patents)
- Engineering footprint: Public site and patents page exist; site hosted on Webflow/Cloudflare; a GitHub org named AeroboDrones/Vermeer exists but no linked public product repos shown\. *(Partly verified)* ^[19](https://www.getvermeer.com/),[20](https://www.getvermeer.com/),[21](https://www.getvermeer.com/),[22](https://github.com/AeroboDrones)
- AI dependency and assets: Company states use of Nvidia‑powered AI and thousands of hours of aerial footage for training; no verified LLM vendor dependency documented\. *(Single source)* ^[7](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation),[10](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)

## Rebuild check

- **Commodity:** Passive camera‑based absolute localization \(single‑platform VPS\) — a competent 2–3 person team can prototype visual localization using open CV and public mapping APIs in weeks\. *(Analyst view)* ^[1](https://www.getvermeer.com/),[23](https://vestbee.com/insights/articles/vermeer-raises-funds)
  - Assumption: Use of public datasets and off‑the‑shelf ML APIs
- **Hard to copy:** Claimed advantage — thousands of hours of aerial footage, Nvidia‑powered models, named defense partnerships and CMMC Level 2 assertion suggest nontrivial data, integration and compliance barriers to copy\. *(Analyst view)* ^[7](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation),[10](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation),[24](https://www.getvermeer.com/news)
  - Assumption: Partnerships imply access to realistic operational data
- **Verdict:** Month — a functional visual localisation prototype can be built in \~1 month; a clone would lack Vermeer's claimed dataset, verified patents, and defense integrations\. *(Analyst view)* ^[1](https://www.getvermeer.com/),[7](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation),[9](https://patents.google.com/?assignee=vermeer)
  - Assumption: No access to Vermeer’s claimed proprietary footage or partner contracts

## Risks and caveats

- Patent claims vs independent search contradiction: company lists US patent numbers on its site but independent Google Patents search returned no publications for 'Vermeer' assignee\. *(Analyst view)* ^[8](https://www.getvermeer.com/patents),[15](https://www.getvermeer.com/patents),[25](https://www.getvermeer.com/patents),[9](https://patents.google.com/?assignee=vermeer)
- Customer/partner concentration risk: many defense partnerships named \(US Army/USAF/Lockheed/Northrop\) which can create procurement, export control, and dependency risk\. *(Analyst view)* ^[10](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation),[6](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/)
- Thin public engineering trace: site on Webflow/Cloudflare and a GitHub org exist but no identified public product repos or docs to validate engineering depth\. *(Analyst view)* ^[20](https://www.getvermeer.com/),[21](https://www.getvermeer.com/),[22](https://github.com/AeroboDrones)

## Questions for founders

- Please produce chain‑of‑title and grant documents for the cited U\.S\. patents \(12,705,791; 12,366,459; 11,355,019\) given the patent search returned no matching assignee\. *(Analyst view)* ^[8](https://www.getvermeer.com/patents),[15](https://www.getvermeer.com/patents),[25](https://www.getvermeer.com/patents),[9](https://patents.google.com/?assignee=vermeer)
- Provide three signed customer references \(including contactable POC and contract terms\) from the &gt;30 customers, and clarify paid vs PoC status\. *(Analyst view)* ^[6](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/),[26](https://vestbee.com/insights/articles/vermeer-raises-funds)
- Document the proprietary dataset: size, provenance, labeling process, and exclusivity of the 'thousands of hours' of aerial footage used to train the Nvidia models\. *(Analyst view)* ^[7](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- Confirm CMMC Level 2 final assessment evidence and scope \(systems covered\), since the claim supports defense contracting trust assumptions\. *(Analyst view)* ^[24](https://www.getvermeer.com/news)

## Sources

1. [getvermeer\.com](https://www.getvermeer.com/) · Company's own website · Product capability — “Determine your absolute location in GPS denied environments for your aerial platform\.”
2. [vestbee\.com](https://vestbee.com/insights/articles/vermeer-raises-funds) · Independent press · Technical claim — “Vermeer develops Visual Positioning Systems \(VPS\), technology that enables drones and other autonomous vehicles to navigate without GPS\.”
3. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/from-hollywood-studios-to-the-frontlines-rockaway-ventures-invests-in-vermeer-the-startup-enabling-drones-to-fly-without-gps) · Independent press · Product capability — “VPS uses up to four electro\-optical or infrared cameras combined with pre\-generated 2D or 3D maps\.”
4. [scroll\.media](https://scroll.media/en/2025/10/23/vermeer-raises-10m) · Independent press · Funding round — “The company closed its Series A $10 million round, with participation from AeroX Ventures, Boscolo Intervest, High Point Ventures, Rockaway Ventures, and U\.S\. Air Force Techstars\.”
5. [getvermeer\.com](https://www.getvermeer.com/news) · Company's own website · Funding round — “Vermeer Raises 10M in Series A”
6. [cc\.cz](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/) · Independent press · Customer — “Vermeer už má více než 30 zákazníků a spolupracuje například s kanadským výrobcem dronů Draganfly, který integruje VPS do modelu Commander 3XL\.”
7. [optics\.org](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation) · Independent press · Technical claim — “Instead of GPS and radiofrequency signals, Vermeer's approach relies on up to four infrared cameras, combined with thousands of hours of aerial video footage and Nvidia\-powered AI technology\.”
8. [getvermeer\.com](https://www.getvermeer.com/patents) · Company's own website · Technical claim — “Localization Processing Service”
9. [patents\.google\.com](https://patents.google.com/?assignee=vermeer) · Official record · Independent check of a claim — “No publication with assignee 'Vermeer' \(or a listed legal name\) on Google Patents; other assignees sharing the name were excluded\.”
10. [optics\.org](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation) · Independent press · Integration — “Vermeer says it has since partnered with the US Army, the US Air Force, Lockheed Martin, Northrop Grumman, and other defense organizations, as well as the AFU\.”
11. [cc\.cz](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/) · Independent press · Funding round — “Čeští investoři z Rockaway Ventures se podíleli na investici do amerického startupu Vermeer”
12. [vestbee\.com](https://vestbee.com/insights/articles/vermeer-raises-funds) · Independent press · Funding round — “Vermeer will use the $10 million Series A funding to advance its Visual Positioning System \(VPS\), increase production capacity, and scale global operations\.”
13. [optics\.org](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation) · Independent press · Funding round — “Vermeer , a New York\-based startup with significant operations in Ukraine, says it has raised $10 million in series A venture funding to scale its optical navigational technology platform for drones\.”
14. [getvermeer\.com](https://www.getvermeer.com/patents) · Company's own website · Product capability — “Applicable Products: AVA, VPS\-212, VPS\-160”
15. [getvermeer\.com](https://www.getvermeer.com/patents) · Company's own website · Technical claim — “Localization Processing Service and Observed Scene Reconstruction Service”
16. [rockawaycapital\.com](https://www.rockawaycapital.com/en/news/from-hollywood-studios-to-the-frontlines-rockaway-ventures-invests-in-vermeer-the-startup-enabling-drones-to-fly-without-gps) · Independent press · Press article · 2025\-10\-23 — “From Hollywood Studios to the Frontlines: Rockaway Ventures Invests in Vermeer, the Startup Enabling Drones to Fly Without GPS – Rockaway Capital”
17. [draper\.vc](https://www.draper.vc/portfolio/vermeer) · Independent press · Press article — “Vermeer \| Portfolio Company \| DRAPER ASSOCIATES”
18. [getvermeer\.com](https://www.getvermeer.com/news) · Company's own website · Technical claim — “Vermeer: Mixed Reality to Previsualize Drone Missions”
19. [getvermeer\.com](https://www.getvermeer.com/) · Company's own website · Website page — “See the world \- Vermeer”
20. [getvermeer\.com](https://www.getvermeer.com/) · Public technical artifact · Technology detected
21. [getvermeer\.com](https://www.getvermeer.com/) · Public technical artifact · Technology detected
22. [github\.com](https://github.com/AeroboDrones) · Public technical artifact · GitHub organisation · 2017\-10\-02 — “AeroboDrones · 3 public repos”
23. [vestbee\.com](https://vestbee.com/insights/articles/vermeer-raises-funds) · Independent press · Technical claim — “The system uses electro\-optical or infrared cameras to analyze the environment and match it to 2D or 3D visual maps, determining precise location even when satellite signals are jammed or unavailable\.”
24. [getvermeer\.com](https://www.getvermeer.com/news) · Company's own website · Technical claim — “PR Newswire: Vermeer Achieves Final Assessment Status for CMMC Level 2, Strengthening Its Position as a Trusted Defense Technology Partner”
25. [getvermeer\.com](https://www.getvermeer.com/patents) · Company's own website · Technical claim — “Motion Tracking Interface for Planning Travel Path”
26. [vestbee\.com](https://vestbee.com/insights/articles/vermeer-raises-funds) · Independent press · Customer — ““Our goal isn’t just to give drones mass, it’s to give them precision, intelligence, and purpose\. We’re proud to have earned the trust of over 30 customers, and with the support of Draper, and our other venture partners, we’re ready to scale that mission," claims Brian Streem, CEO of Vermeer\.”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 1 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | hlidac\_statu, starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 9 | press:axios\.com, press:dronelife\.com, press:en\.wikipedia\.org, press:finsmes\.com, press:founderlodge\.com, press:indeed\.com, press:nsin\.mil |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 7 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 4 | crt\_sh |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 1 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 10 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 4 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 1 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 39 | — |

Analysis: gpt\-5\-mini (cost $0.0085); AI extraction cost $0.0108. Full fact table: CSV export.

## Source appendix (all collected facts)

- F5111 · registry\_flag · Medium confidence · [https://getvermeer\.com/](https://getvermeer.com/)
- F5112 · web\_page · Sourced · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5113 · web\_page · Sourced · [https://vermeer\.homerun\.co/](https://vermeer.homerun.co/)
- F5114 · web\_page · Sourced · [https://vermeer\.homerun\.co/?lang=en](https://vermeer.homerun.co/?lang=en)
- F5115 · web\_page · Sourced · [https://www\.getvermeer\.com/team](https://www.getvermeer.com/team)
- F5116 · web\_page · Sourced · [https://www\.getvermeer\.com/news](https://www.getvermeer.com/news)
- F5117 · web\_page · Sourced · [https://www\.getvermeer\.com/contact](https://www.getvermeer.com/contact)
- F5118 · web\_page · Sourced · [https://www\.getvermeer\.com/patents](https://www.getvermeer.com/patents)
- F5119 · tech\_stack · Medium confidence · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5120 · tech\_stack · Medium confidence · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5121 · tech\_stack · Medium confidence · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5122 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=getvermeer\.com&amp;type=MX](https://dns.google/resolve?name=getvermeer.com&type=MX)
- F5123 · source\_unavailable · Unavailable · [https://crt\.sh/?q=%25\.getvermeer\.com&amp;output=json](https://crt.sh/?q=%25.getvermeer.com&output=json)
- F5124 · github\_org · Sourced · [https://github\.com/AeroboDrones](https://github.com/AeroboDrones)
- F5125 · paper · Medium confidence · [https://openalex\.org/W2431840051](https://openalex.org/W2431840051)
- F5126 · paper · Medium confidence · [https://openalex\.org/W1975506997](https://openalex.org/W1975506997)
- F5127 · paper · Medium confidence · [https://openalex\.org/W2061353398](https://openalex.org/W2061353398)
- F5128 · paper · Medium confidence · [https://openalex\.org/W1989086261](https://openalex.org/W1989086261)
- F5129 · paper · Medium confidence · [https://openalex\.org/W2602751835](https://openalex.org/W2602751835)
- F5130 · paper · Medium confidence · [https://openalex\.org/W3204018698](https://openalex.org/W3204018698)
- F5131 · paper · Medium confidence · [https://openalex\.org/W2078560087](https://openalex.org/W2078560087)
- F5132 · paper · Medium confidence · [https://openalex\.org/W2049738540](https://openalex.org/W2049738540)
- F5133 · paper · Medium confidence · [https://openalex\.org/W2324857942](https://openalex.org/W2324857942)
- F5134 · paper · Medium confidence · [https://openalex\.org/W2323462836](https://openalex.org/W2323462836)
- F5135 · wayback\_first · Sourced · [https://web\.archive\.org/web/20180707152654/http://www\.getvermeer\.com:80/](https://web.archive.org/web/20180707152654/http://www.getvermeer.com:80/)
- F5136 · wayback\_first · Sourced · [https://web\.archive\.org/web/20230325223325/https://www\.getvermeer\.com/careers/job\-posting\-cto\-2](https://web.archive.org/web/20230325223325/https://www.getvermeer.com/careers/job-posting-cto-2)
- F5137 · wayback\_first · Sourced · [https://web\.archive\.org/web/20190716211722/https://www\.getvermeer\.com/blog/page/2/](https://web.archive.org/web/20190716211722/https://www.getvermeer.com/blog/page/2/)
- F5138 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/getvermeer\.com](https://web.archive.org/web/%2A/getvermeer.com)
- F5142 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5143 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5144 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5145 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5146 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5147 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5148 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5149 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5150 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5151 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5152 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5153 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5154 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5155 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5156 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5157 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5158 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5159 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5160 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F5161 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F5162 · source\_unavailable · Unavailable · [https://nsin\.mil/news/2024\-05\-03\-vermeer](https://nsin.mil/news/2024-05-03-vermeer)
- F5163 · press\_mention · Sourced · [https://www\.rockawaycapital\.com/en/news/from\-hollywood\-studios\-to\-the\-frontlines\-rockaway\-ventures\-invests\-in\-vermeer\-the\-startup\-enabling\-drones\-to\-fly\-without\-gps](https://www.rockawaycapital.com/en/news/from-hollywood-studios-to-the-frontlines-rockaway-ventures-invests-in-vermeer-the-startup-enabling-drones-to-fly-without-gps)
- F5164 · source\_unavailable · Unavailable · [https://dronelife\.com/2025/10/23/vermeer\-secures\-10\-million\-series\-a\-to\-advance\-gps\-free\-drone\-navigation\-for\-defense\-and\-dual\-use\-applications/](https://dronelife.com/2025/10/23/vermeer-secures-10-million-series-a-to-advance-gps-free-drone-navigation-for-defense-and-dual-use-applications/)
- F5165 · press\_mention · Sourced · [https://www\.draper\.vc/portfolio/vermeer](https://www.draper.vc/portfolio/vermeer)
- F5166 · press\_mention · Sourced · [https://cc\.cz/z\-hollywoodskych\-studii\-na\-ukrajinskou\-frontu\-pomahaji\-dronum\-a\-nabiraji\-pres\-200\-milionu/](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/)
- F5167 · press\_mention · Sourced · [https://scroll\.media/en/2025/10/23/vermeer\-raises\-10m](https://scroll.media/en/2025/10/23/vermeer-raises-10m)
- F5168 · press\_mention · Sourced · [https://vestbee\.com/insights/articles/vermeer\-raises\-funds](https://vestbee.com/insights/articles/vermeer-raises-funds)
- F5169 · press\_mention · Sourced · [https://optics\.org/news/vermeer\-raises\-10m\-for\-optical\-drone\-navigation](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- F5170 · press\_mention · Sourced · [https://pulse2\.com/vermeer\-10\-million\-series\-a\-raised\-to\-advance\-gps\-free\-drone\-navigation\-technology](https://pulse2.com/vermeer-10-million-series-a-raised-to-advance-gps-free-drone-navigation-technology)
- F5171 · source\_unavailable · Unavailable · [https://www\.axios\.com/2025/10/22/vermeer\-ukraine\-drones\-draper\-vc](https://www.axios.com/2025/10/22/vermeer-ukraine-drones-draper-vc)
- F5172 · press\_mention · Sourced · [https://www\.draper\.vc/newsroom/draper\-associates\-leads\-vermeer\-series\-a](https://www.draper.vc/newsroom/draper-associates-leads-vermeer-series-a)
- F5173 · source\_unavailable · Unavailable · [https://www\.indeed\.com/cmp/Vermeer/reviews?ftext=company](https://www.indeed.com/cmp/Vermeer/reviews?ftext=company)
- F5174 · source\_unavailable · Unavailable · [https://www\.finsmes\.com/2025/10/vermeer\-reaches\-10m\-in\-total\-series\-a\-funding\.html](https://www.finsmes.com/2025/10/vermeer-reaches-10m-in-total-series-a-funding.html)
- F5175 · press\_mention · Sourced · [https://www\.hardwarefyi\.com/startup\-news/vermeer\-raises\-10m\-series\-a/](https://www.hardwarefyi.com/startup-news/vermeer-raises-10m-series-a/)
- F5176 · source\_unavailable · Unavailable · [https://founderlodge\.com/round/Vermeer\-raises\-10000000\-Series\-A\-2025\-10\-24\-Brian\-Streem\-MjQ1NzY](https://founderlodge.com/round/Vermeer-raises-10000000-Series-A-2025-10-24-Brian-Streem-MjQ1NzY)
- F5177 · source\_unavailable · Unavailable · [https://en\.wikipedia\.org/wiki/Vermeer\_Corporation](https://en.wikipedia.org/wiki/Vermeer_Corporation)
- F5518 · source\_unavailable · Unavailable · [https://www\.hlidacstatu\.cz/hledat](https://www.hlidacstatu.cz/hledat)
- F5519 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Vermeer%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27Vermeer%27)
- F5520 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F5986 · product\_capability · Medium confidence · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5987 · product\_capability · Medium confidence · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5988 · product\_capability · Medium confidence · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5989 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5990 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/](https://www.getvermeer.com/)
- F5991 · tech\_claim · Medium confidence · [https://vermeer\.homerun\.co/](https://vermeer.homerun.co/)
- F5992 · tech\_claim · Medium confidence · [https://vermeer\.homerun\.co/](https://vermeer.homerun.co/)
- F5993 · tech\_claim · Medium confidence · [https://vermeer\.homerun\.co/?lang=en](https://vermeer.homerun.co/?lang=en)
- F5994 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/team](https://www.getvermeer.com/team)
- F5995 · funding\_round · Medium confidence · [https://www\.getvermeer\.com/news](https://www.getvermeer.com/news)
- F5996 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/news](https://www.getvermeer.com/news)
- F5997 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/news](https://www.getvermeer.com/news)
- F5998 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/news](https://www.getvermeer.com/news)
- F5999 · product\_capability · Medium confidence · [https://www\.getvermeer\.com/contact](https://www.getvermeer.com/contact)
- F6000 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/contact](https://www.getvermeer.com/contact)
- F6001 · product\_capability · Medium confidence · [https://www\.rockawaycapital\.com/en/news/from\-hollywood\-studios\-to\-the\-frontlines\-rockaway\-ventures\-invests\-in\-vermeer\-the\-startup\-enabling\-drones\-to\-fly\-without\-gps](https://www.rockawaycapital.com/en/news/from-hollywood-studios-to-the-frontlines-rockaway-ventures-invests-in-vermeer-the-startup-enabling-drones-to-fly-without-gps)
- F6003 · tech\_claim · Medium confidence · [https://cc\.cz/z\-hollywoodskych\-studii\-na\-ukrajinskou\-frontu\-pomahaji\-dronum\-a\-nabiraji\-pres\-200\-milionu/](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/)
- F6004 · tech\_claim · Medium confidence · [https://cc\.cz/z\-hollywoodskych\-studii\-na\-ukrajinskou\-frontu\-pomahaji\-dronum\-a\-nabiraji\-pres\-200\-milionu/](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/)
- F6005 · funding\_round · Medium confidence · [https://cc\.cz/z\-hollywoodskych\-studii\-na\-ukrajinskou\-frontu\-pomahaji\-dronum\-a\-nabiraji\-pres\-200\-milionu/](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/)
- F6006 · customer · Medium confidence · [https://cc\.cz/z\-hollywoodskych\-studii\-na\-ukrajinskou\-frontu\-pomahaji\-dronum\-a\-nabiraji\-pres\-200\-milionu/](https://cc.cz/z-hollywoodskych-studii-na-ukrajinskou-frontu-pomahaji-dronum-a-nabiraji-pres-200-milionu/)
- F6007 · funding\_round · Medium confidence · [https://scroll\.media/en/2025/10/23/vermeer\-raises\-10m](https://scroll.media/en/2025/10/23/vermeer-raises-10m)
- F6008 · product\_capability · Medium confidence · [https://scroll\.media/en/2025/10/23/vermeer\-raises\-10m](https://scroll.media/en/2025/10/23/vermeer-raises-10m)
- F6009 · tech\_claim · Medium confidence · [https://scroll\.media/en/2025/10/23/vermeer\-raises\-10m](https://scroll.media/en/2025/10/23/vermeer-raises-10m)
- F6010 · team\_claim · Medium confidence · [https://scroll\.media/en/2025/10/23/vermeer\-raises\-10m](https://scroll.media/en/2025/10/23/vermeer-raises-10m)
- F6011 · funding\_round · Medium confidence · [https://vestbee\.com/insights/articles/vermeer\-raises\-funds](https://vestbee.com/insights/articles/vermeer-raises-funds)
- F6012 · tech\_claim · Medium confidence · [https://vestbee\.com/insights/articles/vermeer\-raises\-funds](https://vestbee.com/insights/articles/vermeer-raises-funds)
- F6013 · tech\_claim · Medium confidence · [https://vestbee\.com/insights/articles/vermeer\-raises\-funds](https://vestbee.com/insights/articles/vermeer-raises-funds)
- F6014 · tech\_claim · Medium confidence · [https://vestbee\.com/insights/articles/vermeer\-raises\-funds](https://vestbee.com/insights/articles/vermeer-raises-funds)
- F6015 · customer · Medium confidence · [https://vestbee\.com/insights/articles/vermeer\-raises\-funds](https://vestbee.com/insights/articles/vermeer-raises-funds)
- F6016 · funding\_round · Medium confidence · [https://optics\.org/news/vermeer\-raises\-10m\-for\-optical\-drone\-navigation](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- F6017 · product\_capability · Medium confidence · [https://optics\.org/news/vermeer\-raises\-10m\-for\-optical\-drone\-navigation](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- F6018 · tech\_claim · Medium confidence · [https://optics\.org/news/vermeer\-raises\-10m\-for\-optical\-drone\-navigation](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- F6019 · integration · Medium confidence · [https://optics\.org/news/vermeer\-raises\-10m\-for\-optical\-drone\-navigation](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- F6020 · team\_claim · Medium confidence · [https://optics\.org/news/vermeer\-raises\-10m\-for\-optical\-drone\-navigation](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- F6021 · tech\_claim · Medium confidence · [https://optics\.org/news/vermeer\-raises\-10m\-for\-optical\-drone\-navigation](https://optics.org/news/vermeer-raises-10m-for-optical-drone-navigation)
- F6022 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/patents](https://www.getvermeer.com/patents)
- F6023 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/patents](https://www.getvermeer.com/patents)
- F6024 · tech\_claim · Medium confidence · [https://www\.getvermeer\.com/patents](https://www.getvermeer.com/patents)
- F6025 · product\_capability · Medium confidence · [https://www\.getvermeer\.com/patents](https://www.getvermeer.com/patents)
- F6387 · verification · Sourced · [https://patents\.google\.com/?assignee=vermeer](https://patents.google.com/?assignee=vermeer)
