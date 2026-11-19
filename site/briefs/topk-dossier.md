# TopK — due diligence brief

topk\.io · CZ/US · 2026\-11\-17

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** An AI\-native hybrid search engine \(semantic, dense/sparse, multi\-vector, keyword\) sold to developers and AI/recSys teams via SDKs and APIs\. *(Partly verified)* ^[1](https://docs.topk.io/),[2](https://www.topk.io/),[3](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/),[4](https://siliconcanals.com/?p=65960),[5](https://www.topk.io/use-cases/recsys)
- **Stage & traction.** Seed round $5\.5M led by Earlybird/KAYA/Irregular Expressions; at least one named customer \(SalesEQ\) and public press coverage\. *(Partly verified)* ^[6](https://siliconcanals.com/?p=65960),[7](https://vestbee.com/insights/articles/top-k-secures-5-5-m),[8](https://www.topk.io/customers/saleseq),[9](https://siliconcanals.com/?p=65960)
- **Technology & moat.** Evidence of research outputs \(three 2026 papers\) and active open\-source repos for core engine and connectors, suggesting reproducible engineering plus some research IP\. *(Verified)* ^[10](https://openalex.org/W7128615148),[11](https://openalex.org/W7214324948),[12](https://openalex.org/W7214339189),[13](https://github.com/topk-io/topk),[14](https://github.com/topk-io/dars)
- **Key risk.** Several central performance and security claims \(p99 latency, SOC 2\) are company\-sourced and only partly verified, raising operational/compliance risk for enterprise deals\. *(Analyst view)* ^[15](https://www.topk.io/use-cases/recsys),[16](https://vestbee.com/insights/articles/top-k-secures-5-5-m),[17](https://www.topk.io/security)
- **Diligence focus.** First obtain the Vanta/SOC2 report and reproduce the semantic\_index benchmark \(10M\-scale p99/throughput\) because these underpin enterprise sales and pricing\. *(Analyst view)* ^[17](https://www.topk.io/security),[15](https://www.topk.io/use-cases/recsys),[18](https://www.topk.io/)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2025\-07\-01 · seed · $5\.5M \(nearly €4\.66M\) · Earlybird, KAYA, Irregular Expressions, angel investors, niekoľkých anjelských investorov · 5 reports | 6, 7, 19, 20, 21 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; integrates with customers' OpenAI \(not a dependency\); own\-model evidence: 4 papers, 0 verified HF models, 0 ML roles, 1 own\-model claims | 22, 23, 24, 10 |
| Engineering footprint | 8 public repos \(106★, last push 2026\-11\-17\); product surfaces: api\.topk\.io, console\.topk\.io, docs\.topk\.io, login\.topk\.io, status\.topk\.io; 5 docs pages; stack: Next\.js, Vercel | 14, 25, 26, 27, 28, 29 |
| Customers | 1 named: SalesEQ; public pricing: yes | 8, 18 |
| Claims checked | SOC 2 / ISO: partly; Customer \(SalesEQ\): not found | 17, 30 |
| Timeline | first press 2025\-07\-01 \(19 articles collected\) | 9 |

# Detailed findings

## Ownership and capital

- Seed funding: $5\.5M \(≈€4\.66M / 120M CZK\) raised in a seed round with Earlybird, KAYA, Irregular Expressions and angel investors reported across outlets\. *(Corroborated)* ^[6](https://siliconcanals.com/?p=65960),[7](https://vestbee.com/insights/articles/top-k-secures-5-5-m),[20](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/),[21](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/)
  - Assumption: Press reports reflect the same round
- No CZ business registry ID found on the site \(impressum/contacts\), suggesting cross‑jurisdictional footprint or non‑CZ entity presence\. *(Company claim)* ^[31](https://topk.io/)
  - Assumption: No IČO shown on public site equals not listed

## Technology profile

- Core product: unified retrieval engine combining semantic, dense, sparse, keyword and multi\-vector search exposed via API/console and Python/Node SDKs\. *(Partly verified)* ^[1](https://docs.topk.io/),[32](https://www.topk.io/),[33](https://docs.topk.io/),[3](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/),[34](https://docs.topk.io/start)
  - Assumption: Docs reflect actual production surfaces
- Engineering footprint: active GitHub org with multiple repos \(core Rust engine, benchmarks, SDKs and connectors\) and public docs/site subdomains \(api, docs, console, status\)\. *(Verified)* ^[35](https://github.com/topk-io),[13](https://github.com/topk-io/topk),[14](https://github.com/topk-io/dars),[25](https://github.com/topk-io/topk-haystack),[36](https://crt.sh/?q=%25.topk.io&output=json)
  - Assumption: Public repos map to product codebase
- AI dependency: product advertises built\-in multi\-vector embedding model and lists OpenAI as an integrated LLM vendor \(integration to customer accounts\)\. *(Partly verified)* ^[37](https://www.topk.io/),[22](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/),[38](https://www.topk.io/pricing)
  - Assumption: Integration implies product can call customer OpenAI accounts

## Rebuild check

- **Commodity:** Python SDK and basic semantic API can be rebuilt by a 2–3 person team in weeks using docs and public connectors \(SDK evidence: Python SDK and docs\)\. *(Analyst view)* ^[39](https://docs.topk.io/),[40](https://docs.topk.io/start),[3](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)
  - Assumption: OSS connectors and docs are complete enough to replicate
- **Hard to copy:** Reproducing claimed low\-cost, large\-scale hybrid engine with MaxSim multi\-vector late interaction, published benchmarks, and academic papers is nontrivial due to research and system engineering evidence\. *(Analyst view)* ^[41](https://www.topk.io/use-cases/recsys),[15](https://www.topk.io/use-cases/recsys),[10](https://openalex.org/W7128615148),[13](https://github.com/topk-io/topk),[42](https://patents.google.com/patent/US20240254752A1)
  - Assumption: Papers and repos contain nontrivial algorithms
- **Verdict:** Month — a functional clone of APIs and SDKs could be built in a month, but a production\-grade engine matching latency/scale and research IP would be missing\. *(Analyst view)* ^[39](https://docs.topk.io/),[13](https://github.com/topk-io/topk),[15](https://www.topk.io/use-cases/recsys)
  - Assumption: Benchmark reproducibility requires internal ops data

## Risks and caveats

- Dependency risk: product lists OpenAI integration \(customer\-account connection\) which may create single\-vendor operational exposure for inference paths\. *(Analyst view)* ^[22](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/)
  - Assumption: Integration used in production inference paths
- Unverified enterprise claims: SOC 2 / uptime pointer exists but report shared under NDA only \(security attestation partly verified\)\. *(Analyst view)* ^[17](https://www.topk.io/security)
  - Assumption: Pointer without report insufficient for enterprise sales
- Customer validation gap: SalesEQ testimonial present on vendor site but independent corroboration was not found in checks\. *(Analyst view)* ^[8](https://www.topk.io/customers/saleseq),[30](https://www.topk.io/customers/saleseq)
  - Assumption: No independent reference page equals uncorroborated

## Questions for founders

- Can TopK provide the full Vanta/SOC 2 Type I report and current uptime/incident logs to validate enterprise claims \(evidence: security pointer partly verified\)? *(Analyst view)* ^[17](https://www.topk.io/security)
  - Assumption: Full report exists and can be shared under NDA
- Please supply raw data and configuration for the 10M\-scale semantic\_index benchmark \(p99 124\.8ms, 176\.5 QPS\) so we can reproduce latency/throughput claims\. *(Analyst view)* ^[15](https://www.topk.io/use-cases/recsys)
  - Assumption: Benchmarks are reproducible with provided artifacts
- Provide three independent customer references \(contacts\) beyond on‑site testimonials, and evidence of revenue or ARR from named customers\. *(Analyst view)* ^[8](https://www.topk.io/customers/saleseq),[30](https://www.topk.io/customers/saleseq),[6](https://siliconcanals.com/?p=65960)
  - Assumption: SalesEQ alone insufficient for enterprise proof
- Clarify the role of OpenAI in production: is TopK reliant on OpenAI for core embeddings/inference or merely integrates customers' accounts? *(Analyst view)* ^[22](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/),[37](https://www.topk.io/),[38](https://www.topk.io/pricing)
  - Assumption: Answer will affect vendor concentration risk

## Sources

1. [docs\.topk\.io](https://docs.topk.io/) · Company's own website · Product capability — “Semantic, keyword, dense, sparse, and multi\-vector search with filtering and custom ranking, in one API\.”
2. [topk\.io](https://www.topk.io/) · Company's own website · Product capability — “Enterprise search Retrieve the right context from complex documents\.”
3. [lupa\.cz](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/) · Independent press · Product capability — “Firma nabízí SDK v Pythonu a Node\.js, respektive JavaScript\.”
4. [siliconcanals\.com](https://siliconcanals.com/?p=65960) · Independent press · Product capability — “The company is developing a unified search engine that enables developers and AI agents to manage both structured and unstructured data through a single system\.”
5. [topk\.io](https://www.topk.io/use-cases/recsys) · Company's own website · Product capability — “TopK gives RecSys teams one serving layer for fresh writes, product\-aware filters, and dense, sparse, keyword, and multi\-vector retrieval across every surface\.”
6. [siliconcanals\.com](https://siliconcanals.com/?p=65960) · Independent press · Funding round — “TopK has raised $5\.5M \(nearly €4\.66M\) in seed funding to advance its AI\-native search platform\.”
7. [vestbee\.com](https://vestbee.com/insights/articles/top-k-secures-5-5-m) · Independent press · Funding round — “Prague\-based firm TopK, which builds an AI\-powered search engine for better data retrieval, has secured $5\.5 million in a seed funding round from Earlybird, KAYA, Irregular Expressions, and several angel investors, as Vestbee was told\.”
8. [topk\.io](https://www.topk.io/customers/saleseq) · Company's own website · Customer — ““TopK has been one of our most important third\-party vendors\. We absolutely love the platform, and we’ve told so many people about it\.””
9. [siliconcanals\.com](https://siliconcanals.com/?p=65960) · Independent press · Press article · 2025\-07\-01 — “Prague’s TopK raises €4\.6M to build a search engine for the AI era”
10. [openalex\.org](https://openalex.org/W7128615148) · Public technical artifact · Research paper · 2026\-04\-09 — “Efficient Learning of Sparse Representations from Interactions · International World Wide Web Conference \(WWW\) · cited 5×”
11. [openalex\.org](https://openalex.org/W7214324948) · Public technical artifact · Research paper · 2026\-09\-25 — “Sparse Autoencoders as Semantic Domain Adapters for Recommender Systems · ACM Conference on Recommender Systems \(RecSys\)”
12. [openalex\.org](https://openalex.org/W7214339189) · Public technical artifact · Research paper · 2026\-09\-25 — “COMPRESSO: Espresso\-Style Sparse Representation Learning for Interpretable Recommender Systems · ACM Conference on Recommender Systems \(RecSys\)”
13. [github\.com](https://github.com/topk-io/topk) · Public technical artifact · GitHub repository · 2026\-11\-17 — “topk\-io/topk · High\-quality search for AI\-native applications\. · Rust · last push 2026\-11\-17”
14. [github\.com](https://github.com/topk-io/dars) · Public technical artifact · GitHub repository · 2026\-02\-09 — “topk\-io/dars · Declarative Agents in Rust · Rust · last push 2026\-02\-09”
15. [topk\.io](https://www.topk.io/use-cases/recsys) · Company's own website · Technical claim — “In the production semantic\_index benchmark, TopK measured the whole path end\-to\-end: ingest, embedding inference, indexing, concurrent queries, and retrieval quality\. On a sustained 10M\-scale run, the system served multi\-vector retrieval at 124\.8 ms p99 latency while sustaining 176\.5 QPS per replica set, with 1\.2s inde…”
16. [vestbee\.com](https://vestbee.com/insights/articles/top-k-secures-5-5-m) · Independent press · Technical claim — “security and reliability features such as SOC 2 Type I compliance and a 99\.9% uptime guarantee\.”
17. [topk\.io](https://www.topk.io/security) · Company's own website · Independent check of a claim — “Public attestation pointer found: vanta on https://www\.topk\.io/security, subdomain trust\.topk\.io\. The report itself is shared under NDA — request it\.”
18. [topk\.io](https://www.topk.io/) · Company's own website · Pricing — “with a production model offered inside TopK for $0\.05/1M tokens\.”
19. [cc\.cz](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/) · Independent press · Funding round — “Loni rozjeli vlastní startup TopK – a teď nabírají investici ve výši necelých 120 milionů korun\.”
20. [lupa\.cz](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/) · Independent press · Funding round — “TopK získal investici 120 milionů korun \(5,5 milionu dolarů\) od fondů Earlybird, Kaya, Irregular Expressions a několika andělských investorů\. Jde o prvotní kolo seed, na jehož poměry jde o vysokou sumu\.”
21. [startitup\.sk](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/) · Independent press · Funding round — “Startup TopK, založený slovenskou dvojicou Marek Galovič a Jerguš Lejko, získal 5,5 milióna dolárov v rámci seed investičného kola\.”
22. [startitup\.sk](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/) · Independent press · Product capability — “V čase, keď prudko rastie záujem o jazykové modely ako ChatGPT, TopK reaguje technológiou, ktorá prepája rôzne prístupy do jedného flexibilného systému\.”
23. [cc\.cz](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/) · Independent press · Product capability — “To vývojářům umožňuje doladit výsledky pro jejich konkrétní doménu a použití, například v e\-commerce, financích, zdravotnictví či právu\.”
24. [openalex\.org](https://openalex.org/W2921738510) · Public technical artifact · Research paper · 2019\-03\-01 — “PBK/TOPK overexpression and survival in solid tumors: A PRISMA\-compliant meta\-analysis · Medicine · cited 21×”
25. [github\.com](https://github.com/topk-io/topk-haystack) · Public technical artifact · GitHub repository · 2026\-06\-08 — “topk\-io/topk\-haystack · Python · last push 2026\-06\-08”
26. [github\.com](https://github.com/topk-io/bench) · Public technical artifact · GitHub repository · 2026\-08\-07 — “topk\-io/bench · Reproducible benchmarking tool for evaluating vector databases under realistic workloads\. · Rust · last push 2026\-08\-07”
27. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-01\-26 — “docs\.topk\.io \(first certificate 2025\-01\-26\)”
28. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-02\-06 — “console\.topk\.io \(first certificate 2025\-02\-06\)”
29. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-05\-19 — “status\.topk\.io \(first certificate 2025\-05\-19\)”
30. [topk\.io](https://www.topk.io/customers/saleseq) · Company's own website · Independent check of a claim
31. [topk\.io](https://topk.io/) · Company's own website · Registry: structure
32. [topk\.io](https://www.topk.io/) · Company's own website · Product capability — “Retrieval engine, models, and inference built together\.”
33. [docs\.topk\.io](https://docs.topk.io/) · Company's own website · Technical claim — “Search by meaning\. No embedding pipeline, vector store, or reranker to run\.”
34. [docs\.topk\.io](https://docs.topk.io/start) · Company's own website · Product capability — “Create a movies collection with a semantic index on the plot, so it can be searched by meaning:”
35. [github\.com](https://github.com/topk-io) · Public technical artifact · GitHub organisation · 2024\-11\-02 — “topk\-io · 19 public repos”
36. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-04\-15 — “api\.topk\.io \(first certificate 2026\-04\-15\)”
37. [topk\.io](https://www.topk.io/) · Company's own website · Technical claim — “Open\-source multimodal multi\-vector embedding models, with a production model offered inside TopK for $0\.05/1M tokens\.”
38. [topk\.io](https://www.topk.io/pricing) · Company's own website · Pricing — “Text &amp; Image embedding Built\-in multi\-vector embeddings per 1M tokens $ 0\.05”
39. [docs\.topk\.io](https://docs.topk.io/) · Company's own website · Product capability — “Search from Python\. TopK embeds your text for you\.”
40. [docs\.topk\.io](https://docs.topk.io/start) · Company's own website · Website page — “Agent quickstart \- TopK”
41. [topk\.io](https://www.topk.io/use-cases/recsys) · Company's own website · Product capability — “Late interaction is expressive because it does more work: MaxSim compares query vectors against item vectors and aggregates the best matches\. TopK does not brute\-force that across the corpus\. Managed semantic\_index and bring\-your\-own representations in multi\_vector\_index both use sparse multi\-vector encoding as a fast …”
42. [patents\.google\.com](https://patents.google.com/patent/US20240254752A1) · Official record · Patent publication — “US20240254752A1 · Modular assembly including multiple modules · Topk USA LLC”

## How this dossier was built

| Step | What it reads | Facts | Unavailable |
|---|---|---|---|
| Czech business registry | ARES and ARES VR \(identity, shareholders, capital\), or\.justice\.cz Sbírka listin \(filed documents\), ISIR \(insolvency\) | 1 | — |
| Public money | Hlídač státu \(public contracts from registr smluv, subsidies\), CORDIS | 0 | hlidac\_statu, starfos |
| Press | CzechCrunch, Lupa, E15, Vestbee, tech\.eu… found via search / RSS and earlier research; an article is kept only if it mentions the company | 19 | press:ca\.investing\.com, press:eu\-startups\.com, press:forbes\.sk, press:investing\.com |
| Company website | up to 30 pages: product, pricing, docs, customers, careers, privacy \(robots\.txt respected\); job boards linked from the site | 26 | — |
| Technical fingerprint | HTTP headers and HTML markers, DNS records, certificate transparency \(crt\.sh\) for subdomains | 37 | — |
| Public code | GitHub organisation and repositories \(only if linked from the company or matching its domain\) | 9 | — |
| Research &amp; models | OpenAlex \(papers by affiliation\), Hugging Face \(models\) | 4 | — |
| Web history | Wayback Machine: first captures of the domain and key pages | 4 | — |
| Claim verification | company claims checked against independent sources: Google Patents \(patents\), IAB Global Vendor List \(TCF\), commercial register \(investors named in press\), security pages \(SOC 2 / ISO attestations\), news search \(customers\) | 3 | — |
| AI extraction | an LLM reads saved pages and articles and proposes facts; a fact is kept only if its quote is found in the source text and its category passes rule checks | 57 | — |

Analysis: gpt\-5\-mini (cost $0.0090); AI extraction cost $0.0082. Full fact table: CSV export.

## Source appendix (all collected facts)

- F4083 · registry\_flag · Medium confidence · [https://topk\.io/](https://topk.io/)
- F4084 · web\_page · Sourced · [https://www\.topk\.io/](https://www.topk.io/)
- F4085 · web\_page · Sourced · [https://www\.topk\.io/careers](https://www.topk.io/careers)
- F4086 · web\_page · Sourced · [https://docs\.topk\.io/](https://docs.topk.io/)
- F4087 · web\_page · Sourced · [https://trust\.topk\.io/](https://trust.topk.io/)
- F4088 · web\_page · Sourced · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F4089 · web\_page · Sourced · [https://docs\.topk\.io/start](https://docs.topk.io/start)
- F4090 · web\_page · Sourced · [https://www\.topk\.io/security](https://www.topk.io/security)
- F4091 · web\_page · Sourced · [https://www\.topk\.io/use\-cases/recsys](https://www.topk.io/use-cases/recsys)
- F4092 · web\_page · Sourced · [https://www\.topk\.io/learn/elasticsearch\-api\-compatibility](https://www.topk.io/learn/elasticsearch-api-compatibility)
- F4093 · web\_page · Sourced · [https://www\.topk\.io/learn/hybrid\-search\-elasticsearch\-api](https://www.topk.io/learn/hybrid-search-elasticsearch-api)
- F4094 · web\_page · Sourced · [https://www\.topk\.io/learn/knn\-search\-elasticsearch\-api](https://www.topk.io/learn/knn-search-elasticsearch-api)
- F4095 · web\_page · Sourced · [https://www\.topk\.io/team](https://www.topk.io/team)
- F4096 · web\_page · Sourced · [https://www\.topk\.io/customers/saleseq](https://www.topk.io/customers/saleseq)
- F4097 · web\_page · Sourced · [https://www\.topk\.io/blog](https://www.topk.io/blog)
- F4098 · web\_page · Sourced · [https://www\.topk\.io/blog/topk\-embed\-v1](https://www.topk.io/blog/topk-embed-v1)
- F4099 · web\_page · Sourced · [https://www\.topk\.io/blog/20260814\-fast\-regex\-search\-sparse\-grams](https://www.topk.io/blog/20260814-fast-regex-search-sparse-grams)
- F4100 · web\_page · Sourced · [https://status\.topk\.io/](https://status.topk.io/)
- F4101 · web\_page · Sourced · [https://www\.topk\.io/benchmarks](https://www.topk.io/benchmarks)
- F4102 · github\_org · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F4103 · github\_org · Low confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F4104 · github\_org · Low confidence · [https://www\.topk\.io/learn/elasticsearch\-api\-compatibility](https://www.topk.io/learn/elasticsearch-api-compatibility)
- F4105 · github\_org · Low confidence · [https://www\.topk\.io/team](https://www.topk.io/team)
- F4106 · github\_org · Low confidence · [https://www\.topk\.io/team](https://www.topk.io/team)
- F4107 · github\_org · Low confidence · [https://www\.topk\.io/team](https://www.topk.io/team)
- F4108 · github\_org · Low confidence · [https://www\.topk\.io/team](https://www.topk.io/team)
- F4109 · github\_org · Low confidence · [https://www\.topk\.io/team](https://www.topk.io/team)
- F4110 · tech\_stack · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F4111 · tech\_stack · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F4112 · tech\_stack · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F4113 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=topk\.io&amp;type=MX](https://dns.google/resolve?name=topk.io&type=MX)
- F4114 · saas\_tool · Medium confidence · [https://dns\.google/resolve?name=topk\.io&amp;type=TXT](https://dns.google/resolve?name=topk.io&type=TXT)
- F4115 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4116 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4117 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4118 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4119 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4120 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4121 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4122 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4123 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4124 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4125 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4126 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4127 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4128 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4129 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4130 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4131 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4132 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4133 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4134 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4135 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4136 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4137 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4138 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4139 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4140 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4141 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4142 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4143 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4144 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4145 · subdomain · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4146 · cert\_first · Sourced · [https://crt\.sh/?q=%25\.topk\.io&amp;output=json](https://crt.sh/?q=%25.topk.io&output=json)
- F4147 · github\_org · Sourced · [https://github\.com/topk\-io](https://github.com/topk-io)
- F4148 · repo · Sourced · [https://github\.com/topk\-io/topk](https://github.com/topk-io/topk)
- F4149 · repo · Sourced · [https://github\.com/topk\-io/llama\-index\-vector\-stores\-topk](https://github.com/topk-io/llama-index-vector-stores-topk)
- F4150 · repo · Sourced · [https://github\.com/topk\-io/langchain\-topk](https://github.com/topk-io/langchain-topk)
- F4151 · repo · Sourced · [https://github\.com/topk\-io/homebrew\-topk](https://github.com/topk-io/homebrew-topk)
- F4152 · repo · Sourced · [https://github\.com/topk\-io/adk\-topk](https://github.com/topk-io/adk-topk)
- F4153 · repo · Sourced · [https://github\.com/topk\-io/bench](https://github.com/topk-io/bench)
- F4154 · repo · Sourced · [https://github\.com/topk\-io/topk\-haystack](https://github.com/topk-io/topk-haystack)
- F4155 · repo · Sourced · [https://github\.com/topk\-io/dars](https://github.com/topk-io/dars)
- F4156 · paper · Medium confidence · [https://openalex\.org/W7128615148](https://openalex.org/W7128615148)
- F4157 · paper · Medium confidence · [https://openalex\.org/W7214324948](https://openalex.org/W7214324948)
- F4158 · paper · Medium confidence · [https://openalex\.org/W7214339189](https://openalex.org/W7214339189)
- F4159 · paper · Medium confidence · [https://openalex\.org/W2921738510](https://openalex.org/W2921738510)
- F4160 · wayback\_first · Sourced · [https://web\.archive\.org/web/20241122134629/https://topk\.io/](https://web.archive.org/web/20241122134629/https://topk.io/)
- F4161 · wayback\_first · Sourced · [https://web\.archive\.org/web/20250807095704/https://www\.topk\.io/pricing](https://web.archive.org/web/20250807095704/https://www.topk.io/pricing)
- F4162 · wayback\_first · Sourced · [https://web\.archive\.org/web/20250702110512/https://www\.topk\.io/blog](https://web.archive.org/web/20250702110512/https://www.topk.io/blog)
- F4163 · wayback\_first · Sourced · [https://web\.archive\.org/web/\*/topk\.io](https://web.archive.org/web/%2A/topk.io)
- F4167 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4168 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4169 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4170 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4171 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4172 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4173 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4174 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4175 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4176 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4177 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4178 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4179 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4180 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4181 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4182 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4183 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4184 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4185 · search\_check · Checked · [https://api\.tavily\.com/search](https://api.tavily.com/search)
- F4186 · search\_check · Checked · [https://api\.exa\.ai/search](https://api.exa.ai/search)
- F4187 · press\_mention · Sourced · [https://siliconcanals\.com/?p=65960](https://siliconcanals.com/?p=65960)
- F4188 · source\_unavailable · Unavailable · [https://ca\.investing\.com/equities/top\-kinisis\-travel\-public\-ltd](https://ca.investing.com/equities/top-kinisis-travel-public-ltd)
- F4189 · press\_mention · Sourced · [https://vestbee\.com/insights/articles/top\-k\-secures\-5\-5\-m](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- F4190 · source\_unavailable · Unavailable · [https://www\.investing\.com/equities/top\-kinisis\-travel\-public\-ltd](https://www.investing.com/equities/top-kinisis-travel-public-ltd)
- F4191 · press\_mention · Sourced · [https://redis\.io/docs/latest/develop/data\-types/probabilistic/top\-k](https://redis.io/docs/latest/develop/data-types/probabilistic/top-k)
- F4192 · press\_mention · Sourced · [https://cc\.cz/chodili\-spolu\-na\-stredni\-ted\-nabiraji\-120\-milionu\-a\-chteji\-pohanet\-vyhledavani\-pro\-top\-aplikace/](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/)
- F4193 · press\_mention · Sourced · [https://www\.lupa\.cz/aktuality/databaze\-s\-prichodem\-ai\-prochazi\-zasadni\-transformaci\-cesko\-slovensky\-startup\-na\-to\-ziskal\-120\-milionu/](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)
- F4194 · press\_mention · Sourced · [https://www\.startitup\.sk/web\-stories/slovaci\-chcu\-prepisat\-buducnost\-vyhladavania\-startup\-topk\-ziskal\-miliony\-na\-ai\-revoluciu/](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/)
- F4195 · press\_mention · Sourced · [https://www\.euro\.cz/clanky/cesko\-slovensky\-startup\-topk\-chce\-zmenit\-zpusob\-vyhledavani\-v\-ere\-ai\-od\-investoru\-ziskal\-120\-milionu\-a\-miri\-na\-firmy\-typu\-openai/](https://www.euro.cz/clanky/cesko-slovensky-startup-topk-chce-zmenit-zpusob-vyhledavani-v-ere-ai-od-investoru-ziskal-120-milionu-a-miri-na-firmy-typu-openai/)
- F4196 · press\_mention · Sourced · [https://earlybird\.com/companies/topk](https://earlybird.com/companies/topk)
- F4197 · source\_unavailable · Unavailable · [https://www\.forbes\.sk/slovaci\-maju\-kluc\-k\-umelej\-inteligencii\-ich\-startup\-ma\-zabezpecit\-pristup\-ai\-ku\-kvalitnejsim\-datam/](https://www.forbes.sk/slovaci-maju-kluc-k-umelej-inteligencii-ich-startup-ma-zabezpecit-pristup-ai-ku-kvalitnejsim-datam/)
- F4198 · press\_mention · Sourced · [https://itkey\.media/topk\-raises\-usd\-5\-5m\-to\-tackle\-chatgpt\-era\-challenges\-with\-ai\-native\-hybrid\-search\-engine\-for\-enterprises/](https://itkey.media/topk-raises-usd-5-5m-to-tackle-chatgpt-era-challenges-with-ai-native-hybrid-search-engine-for-enterprises/)
- F4199 · press\_mention · Sourced · [https://tech\.eu/2025/07/01/topk\-raises\-55m\-to\-develop\-ai\-native\-search\-engine\-for\-enterprises](https://tech.eu/2025/07/01/topk-raises-55m-to-develop-ai-native-search-engine-for-enterprises)
- F4200 · source\_unavailable · Unavailable · [https://www\.eu\-startups\.com/2025/07/czech\-startup\-topk\-raises\-e4\-6\-million\-to\-build\-an\-ai\-native\-search\-engine\-for\-enterprises/](https://www.eu-startups.com/2025/07/czech-startup-topk-raises-e4-6-million-to-build-an-ai-native-search-engine-for-enterprises/)
- F4201 · press\_mention · Sourced · [https://siliconcanals\.com/topk\-raises\-e4\-6m/](https://siliconcanals.com/topk-raises-e4-6m/)
- F4202 · press\_mention · Sourced · [https://techfundingnews\.com/topk\-perplexity\-for\-corporates\-raises\-5\-5m\-ai\-search/](https://techfundingnews.com/topk-perplexity-for-corporates-raises-5-5m-ai-search/)
- F4203 · press\_mention · Sourced · [https://www\.therecursive\.com/topk\-raises\-5\-68m\-for\-ai\-native\-hybrid\-search/](https://www.therecursive.com/topk-raises-5-68m-for-ai-native-hybrid-search/)
- F4204 · press\_mention · Sourced · [https://www\.thesaasnews\.com/news/topk\-raises\-4\-6\-million\-in\-seed\-round/](https://www.thesaasnews.com/news/topk-raises-4-6-million-in-seed-round/)
- F4205 · press\_mention · Sourced · [https://huggingface\.co/ByteDance\-Seed/Cross\-Layer\-TopK\-CLT](https://huggingface.co/ByteDance-Seed/Cross-Layer-TopK-CLT)
- F4206 · press\_mention · Sourced · [https://www\.techguru\.sk/30195/topk\-slovaci\-cesi\-ai\-databaza](https://www.techguru.sk/30195/topk-slovaci-cesi-ai-databaza)
- F4207 · press\_mention · Sourced · [https://www\.gaebler\.com/VC\-Funding\-BA995EA6\-EA64\-4C15\-B880\-8C9EB23E59A0\-TopK\-07\-01\-2025](https://www.gaebler.com/VC-Funding-BA995EA6-EA64-4C15-B880-8C9EB23E59A0-TopK-07-01-2025)
- F4208 · press\_mention · Sourced · [https://dbdb\.io/db/topk](https://dbdb.io/db/topk)
- F4209 · press\_mention · Sourced · [https://github\.com/topk\-io/topk](https://github.com/topk-io/topk)
- F5535 · source\_unavailable · Unavailable · [https://www\.hlidacstatu\.cz/hledat](https://www.hlidacstatu.cz/hledat)
- F5536 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27TopK%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27TopK%27)
- F5537 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
- F6136 · product\_capability · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F6137 · tech\_claim · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F6138 · product\_capability · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F6139 · product\_capability · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F6140 · product\_capability · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F6141 · product\_capability · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F6142 · pricing · Medium confidence · [https://www\.topk\.io/](https://www.topk.io/)
- F6143 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6144 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6145 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6146 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6147 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6148 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6149 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6150 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6151 · pricing · Medium confidence · [https://www\.topk\.io/pricing](https://www.topk.io/pricing)
- F6152 · customer · Medium confidence · [https://www\.topk\.io/customers/saleseq](https://www.topk.io/customers/saleseq)
- F6153 · product\_capability · Medium confidence · [https://www\.topk\.io/use\-cases/recsys](https://www.topk.io/use-cases/recsys)
- F6154 · product\_capability · Medium confidence · [https://www\.topk\.io/use\-cases/recsys](https://www.topk.io/use-cases/recsys)
- F6155 · product\_capability · Medium confidence · [https://www\.topk\.io/use\-cases/recsys](https://www.topk.io/use-cases/recsys)
- F6156 · product\_capability · Medium confidence · [https://www\.topk\.io/use\-cases/recsys](https://www.topk.io/use-cases/recsys)
- F6157 · tech\_claim · Medium confidence · [https://www\.topk\.io/use\-cases/recsys](https://www.topk.io/use-cases/recsys)
- F6158 · pricing · Medium confidence · [https://www\.topk\.io/use\-cases/recsys](https://www.topk.io/use-cases/recsys)
- F6159 · tech\_claim · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6160 · product\_capability · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6161 · tech\_claim · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6162 · tech\_claim · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6163 · tech\_claim · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6164 · tech\_claim · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6165 · tech\_claim · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6166 · tech\_claim · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6167 · product\_capability · Medium confidence · [https://docs\.topk\.io/](https://docs.topk.io/)
- F6168 · funding\_round · Medium confidence · [https://siliconcanals\.com/?p=65960](https://siliconcanals.com/?p=65960)
- F6169 · product\_capability · Medium confidence · [https://siliconcanals\.com/?p=65960](https://siliconcanals.com/?p=65960)
- F6170 · tech\_claim · Medium confidence · [https://siliconcanals\.com/?p=65960](https://siliconcanals.com/?p=65960)
- F6171 · funding\_round · Medium confidence · [https://vestbee\.com/insights/articles/top\-k\-secures\-5\-5\-m](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- F6172 · product\_capability · Medium confidence · [https://vestbee\.com/insights/articles/top\-k\-secures\-5\-5\-m](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- F6173 · product\_capability · Medium confidence · [https://vestbee\.com/insights/articles/top\-k\-secures\-5\-5\-m](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- F6174 · product\_capability · Medium confidence · [https://vestbee\.com/insights/articles/top\-k\-secures\-5\-5\-m](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- F6175 · integration · Medium confidence · [https://vestbee\.com/insights/articles/top\-k\-secures\-5\-5\-m](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- F6176 · tech\_claim · Medium confidence · [https://vestbee\.com/insights/articles/top\-k\-secures\-5\-5\-m](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- F6177 · product\_capability · Medium confidence · [https://cc\.cz/chodili\-spolu\-na\-stredni\-ted\-nabiraji\-120\-milionu\-a\-chteji\-pohanet\-vyhledavani\-pro\-top\-aplikace/](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/)
- F6178 · product\_capability · Medium confidence · [https://cc\.cz/chodili\-spolu\-na\-stredni\-ted\-nabiraji\-120\-milionu\-a\-chteji\-pohanet\-vyhledavani\-pro\-top\-aplikace/](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/)
- F6179 · funding\_round · Medium confidence · [https://cc\.cz/chodili\-spolu\-na\-stredni\-ted\-nabiraji\-120\-milionu\-a\-chteji\-pohanet\-vyhledavani\-pro\-top\-aplikace/](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/)
- F6180 · tech\_claim · Medium confidence · [https://cc\.cz/chodili\-spolu\-na\-stredni\-ted\-nabiraji\-120\-milionu\-a\-chteji\-pohanet\-vyhledavani\-pro\-top\-aplikace/](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/)
- F6181 · team\_claim · Medium confidence · [https://cc\.cz/chodili\-spolu\-na\-stredni\-ted\-nabiraji\-120\-milionu\-a\-chteji\-pohanet\-vyhledavani\-pro\-top\-aplikace/](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/)
- F6182 · funding\_round · Medium confidence · [https://www\.lupa\.cz/aktuality/databaze\-s\-prichodem\-ai\-prochazi\-zasadni\-transformaci\-cesko\-slovensky\-startup\-na\-to\-ziskal\-120\-milionu/](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)
- F6183 · product\_capability · Medium confidence · [https://www\.lupa\.cz/aktuality/databaze\-s\-prichodem\-ai\-prochazi\-zasadni\-transformaci\-cesko\-slovensky\-startup\-na\-to\-ziskal\-120\-milionu/](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)
- F6185 · team\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/databaze\-s\-prichodem\-ai\-prochazi\-zasadni\-transformaci\-cesko\-slovensky\-startup\-na\-to\-ziskal\-120\-milionu/](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)
- F6186 · tech\_claim · Medium confidence · [https://www\.lupa\.cz/aktuality/databaze\-s\-prichodem\-ai\-prochazi\-zasadni\-transformaci\-cesko\-slovensky\-startup\-na\-to\-ziskal\-120\-milionu/](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)
- F6187 · funding\_round · Medium confidence · [https://www\.startitup\.sk/web\-stories/slovaci\-chcu\-prepisat\-buducnost\-vyhladavania\-startup\-topk\-ziskal\-miliony\-na\-ai\-revoluciu/](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/)
- F6188 · team\_claim · Medium confidence · [https://www\.startitup\.sk/web\-stories/slovaci\-chcu\-prepisat\-buducnost\-vyhladavania\-startup\-topk\-ziskal\-miliony\-na\-ai\-revoluciu/](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/)
- F6189 · product\_capability · Medium confidence · [https://www\.startitup\.sk/web\-stories/slovaci\-chcu\-prepisat\-buducnost\-vyhladavania\-startup\-topk\-ziskal\-miliony\-na\-ai\-revoluciu/](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/)
- F6190 · product\_capability · Medium confidence · [https://docs\.topk\.io/start](https://docs.topk.io/start)
- F6191 · product\_capability · Medium confidence · [https://docs\.topk\.io/start](https://docs.topk.io/start)
- F6192 · tech\_claim · Medium confidence · [https://docs\.topk\.io/start](https://docs.topk.io/start)
- F6193 · tech\_claim · Medium confidence · [https://docs\.topk\.io/start](https://docs.topk.io/start)
- F6395 · patent · Sourced · [https://patents\.google\.com/patent/US20240254752A1](https://patents.google.com/patent/US20240254752A1)
- F6396 · verification · Sourced · [https://www\.topk\.io/security](https://www.topk.io/security)
- F6397 · verification · Sourced · [https://www\.topk\.io/customers/saleseq](https://www.topk.io/customers/saleseq)
