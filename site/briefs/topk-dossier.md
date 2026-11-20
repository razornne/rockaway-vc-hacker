# TopK — due diligence brief

topk\.io · CZ/US · 2026\-11\-20

**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: *Verified* — backed by an official record or a public technical artifact; *Corroborated* — reported by two or more independent outlets; *Single source* — one independent outlet; not yet corroborated; *Partly verified* — combines independent evidence with the company's own statements; *Company claim* — only the company's own website says so — verify in diligence; *Analyst view* — a judgement drawn from the cited evidence, not a fact.

## TL;DR

- **Product.** A cloud SaaS AI\-native hybrid search engine \(multi\-vector, dense/sparse, keyword\) sold to developer and enterprise customers via API/SDKs and console\. *(Partly verified)* ^[1](https://docs.topk.io/),[2](https://www.topk.io/),[3](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/),[4](https://crt.sh/?q=%25.topk.io&output=json),[5](https://crt.sh/?q=%25.topk.io&output=json)
- **Stage & traction.** Closed $5\.5M seed led by Earlybird/KAYA/Irregular Expressions; one named reference customer \(SalesEQ\); public press coverage since 2025\. *(Partly verified)* ^[6](https://siliconcanals.com/?p=65960),[7](https://vestbee.com/insights/articles/top-k-secures-5-5-m),[8](https://earlybird.com/companies/topk),[9](https://www.topk.io/customers/saleseq),[10](https://siliconcanals.com/?p=65960)
- **Technology & moat.** Evidence of engineering output \(8\+ public repos, active pushes, Rust core repo\) and published ML papers claiming novel sparse representations\. *(Verified)* ^[11](https://github.com/topk-io/topk),[12](https://github.com/topk-io/llama-index-vector-stores-topk),[13](https://openalex.org/W7128615148),[14](https://openalex.org/W7214324948)
- **Key risk.** Several product performance and security claims \(benchmarks, SOC2\) are company\-published and only partly independently verified\. *(Analyst view)* ^[15](https://www.topk.io/use-cases/recsys),[16](https://vestbee.com/insights/articles/top-k-secures-5-5-m),[17](https://www.topk.io/security),[18](https://www.topk.io/customers/saleseq)
- **Diligence focus.** Verify benchmark reproducibility, SOC2 report access, and SalesEQ reference to confirm latency, reliability, and real\-world recall\. *(Analyst view)* ^[15](https://www.topk.io/use-cases/recsys),[17](https://www.topk.io/security),[18](https://www.topk.io/customers/saleseq)

## At a glance (computed by code, no LLM)

| Signal | Value | Sources |
|---|---|---|
| Funding \(press\) | 2025\-07\-01 · seed · $5\.5M \(nearly €4\.66M\) · Earlybird, KAYA, Irregular Expressions, angel investors, niekoľkých anjelských investorov · 5 reports | 6, 7, 19, 20, 21 |
| Thesis fit \(Rockaway\) | sectors: AI\-led transformative tech \(20 facts\); deep tech \(7 facts\); energy \(2 facts\) · geography: CZ/US \(core region\) · overlaps portfolio: Gjirafa \(e\-comme, search\) | 10, 22, 13, 14, 23, 24 |
| AI dependency | no LLM vendor named as subprocessor or in own tech claims; integrates with customers' OpenAI \(not a dependency\); own\-model evidence: 4 papers, 0 verified HF models, 0 ML roles, 1 own\-model claims | 25, 26, 27, 13 |
| Engineering footprint | 8 public repos \(106★, last push 2026\-11\-17\); product surfaces: api\.topk\.io, console\.topk\.io, docs\.topk\.io, login\.topk\.io, status\.topk\.io; 5 docs pages; stack: Next\.js, Vercel | 28, 29, 30, 31, 5, 32 |
| Customers | 1 named: SalesEQ; public pricing: yes | 9, 33 |
| Claims checked | SOC 2 / ISO: partly; Customer \(SalesEQ\): not found | 17, 18 |
| Timeline | first press 2025\-07\-01 \(19 articles collected\) | 10 |

# Investment view

*Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the market, competitors and fit with the fund, and the case for and against\.*

## Fit with the Rockaway thesis

- **Sector:** AI\-led transformative tech — TopK positions itself as an AI\-native, hybrid retrieval engine combining vectors, keywords and multi\-vector models for enterprise search\. *(Analyst view)* ^[34](https://www.topk.io/),[2](https://www.topk.io/),[1](https://docs.topk.io/)
  - Assumption: Company product pages reflect core sector positioning\.
- **Portfolio overlap:** Gjirafa listed in fund overlap; potential thematic overlap on 'search' \(TopK builds an enterprise search engine\), which could be a strategic synergy or buyer overlap risk to check\. *(Analyst view)* ^[35](https://siliconcanals.com/?p=65960),[36](https://vestbee.com/insights/articles/top-k-secures-5-5-m),[37](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)
  - Assumption: TopK's search capability overlaps meaningfully with general\-purpose search products\.

## Business model

- Revenue model: usage\-based SaaS pricing \(monthly billing\) with per\-operation and per‑token charges and free credits for trials\. *(Company claim)* ^[38](https://www.topk.io/pricing),[39](https://www.topk.io/pricing),[40](https://www.topk.io/pricing),[41](https://www.topk.io/pricing)
- Buyers/payors: sells to enterprises — at least one named customer \(SalesEQ\) who uses TopK for agentic search over meetings\. *(Company claim)* ^[9](https://www.topk.io/customers/saleseq)

## Market

- Demand driver \(company/press\): enterprise need for AI\-native search and retrieval in the 'ChatGPT era' is cited as TopK's market rationale by multiple press outlets\. *(Corroborated)* ^[10](https://siliconcanals.com/?p=65960),[42](https://tech.eu/2025/07/01/topk-raises-55m-to-develop-ai-native-search-engine-for-enterprises),[43](https://itkey.media/topk-raises-usd-5-5m-to-tackle-chatgpt-era-challenges-with-ai-native-hybrid-search-engine-for-enterprises/)
- Target buyers \(company claim\): TopK targets use cases across e\-commerce, finance, healthcare, and law by enabling domain\-specific tuning\. *(Single source)* ^[26](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/)

## Competition

- OpenAI \(mentioned in press as a target/comparator\): cited by Euro\.cz as a firm TopK 'aims at' — indicates positioning against large AI incumbents or their developer offerings\. *(Analyst view)* ^[23](https://www.euro.cz/clanky/cesko-slovensky-startup-topk-chce-zmenit-zpusob-vyhledavani-v-ere-ai-od-investoru-ziskal-120-milionu-a-miri-na-firmy-typu-openai/)
  - Assumption: Mention in press implies perceived market/positioning overlap\.
- Elasticsearch / Elastic compatibility: TopK documents describe Elasticsearch API compatibility and migration messaging — positions TopK as an alternative to Elastic's stack for hybrid search\. *(Analyst view)* ^[44](https://www.topk.io/learn/hybrid-search-elasticsearch-api),[45](https://www.topk.io/learn/elasticsearch-api-compatibility)
  - Assumption: API\-compatibility docs indicate deliberate product positioning vs Elastic\.
- Redis Top\-K / probabilistic top\-k: Redis docs appear in the fact set \(top\-k data type\); this represents a technical incumbent/approach TopK must differentiate from for specific workloads\. *(Analyst view)* ^[46](https://redis.io/docs/latest/develop/data-types/probabilistic/top-k)
  - Assumption: Redis top\-k is a comparable technical approach for some retrieval tasks\.

## Case for and against

- **For:** Differentiated tech — unified hybrid retrieval \(semantic, sparse, dense, multi\-vector\) with production embedding pricing and SDKs, enabling one API for complex retrieval\. *(Analyst view)* ^[1](https://docs.topk.io/),[2](https://www.topk.io/),[3](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)
  - Assumption: Product claims translate to practical engineering differentiation\.
- **For:** Early traction and validation — $5\.5M seed from recognized VCs \(Earlybird, KAYA\) and at least one named enterprise customer \(SalesEQ\)\. *(Analyst view)* ^[6](https://siliconcanals.com/?p=65960),[7](https://vestbee.com/insights/articles/top-k-secures-5-5-m),[9](https://www.topk.io/customers/saleseq)
  - Assumption: Seed participation by tiered VCs signals third‑party validation\.
- **Against:** Customer corroboration gap — SalesEQ is named on TopK site but third‑party corroboration was not found in verification facts\. *(Analyst view)* ^[9](https://www.topk.io/customers/saleseq),[18](https://www.topk.io/customers/saleseq)
  - Assumption: Independent customer references are required for commercial validation\.
- **Against:** Partial security attestation — TopK points to a Vanta SOC2 pointer but report access appears gated \(shared under NDA\), leaving a verification gap for enterprise security posture\. *(Analyst view)* ^[17](https://www.topk.io/security),[16](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
  - Assumption: Enterprises will require full SOC2 evidence during diligence\.
- **Must be true:** Confirmed enterprise references and usage metrics beyond one named customer \(volume, ARR, contract terms\)\. *(Analyst view)* ^[9](https://www.topk.io/customers/saleseq),[6](https://siliconcanals.com/?p=65960)
  - Assumption: Commercial scale is necessary to justify enterprise go\-to\-market claims\.
- **Must be true:** Obtain verifiable security artefacts \(SOC2 report or equivalent\) and penetration\-test results to support claims of enterprise readiness\. *(Analyst view)* ^[17](https://www.topk.io/security),[16](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
  - Assumption: Security evidence materially affects enterprise sales prospects\.

# Technical due diligence

## Ownership and capital

- Seed round: $5\.5M \(≈120M CZK\) reported closed with investors Earlybird, KAYA, Irregular Expressions and angels\. *(Corroborated)* ^[6](https://siliconcanals.com/?p=65960),[7](https://vestbee.com/insights/articles/top-k-secures-5-5-m),[19](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/),[20](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/),[21](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/)
  - Assumption: Press round reporting equals closed funding
- Founders and leadership named in press: Marek Galovič, Jerguš Lejko and additional founders listed in coverage\. *(Corroborated)* ^[47](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/),[48](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/)

## Technology profile

- Product surfaces: public API, console, docs, login and status subdomains exist for SaaS product access and docs\. *(Verified)* ^[4](https://crt.sh/?q=%25.topk.io&output=json),[5](https://crt.sh/?q=%25.topk.io&output=json),[31](https://crt.sh/?q=%25.topk.io&output=json),[49](https://crt.sh/?q=%25.topk.io&output=json),[32](https://crt.sh/?q=%25.topk.io&output=json)
- Engineering footprint: at least eight public GitHub repos \(Rust core with \~98 stars\), active pushes as recent as 2026\-11\-17\. *(Verified)* ^[11](https://github.com/topk-io/topk),[12](https://github.com/topk-io/llama-index-vector-stores-topk),[50](https://github.com/topk-io/langchain-topk),[28](https://github.com/topk-io/dars),[51](https://github.com/topk-io)
- Product capabilities claimed: unified hybrid retrieval \(semantic, dense, sparse, keyword\), multi\-vector/late\-interaction, high\-throughput online writes\. *(Company claim)* ^[1](https://docs.topk.io/),[52](https://www.topk.io/use-cases/recsys),[53](https://www.topk.io/use-cases/recsys),[54](https://www.topk.io/use-cases/recsys)

## What could be rebuilt, and what cannot be judged from outside

- **Replicable with off-the-shelf parts:** API/SDK surfaces and hybrid\-search behavior can be reassembled using open libraries \(OpenSearch/Elasticsearch API compatibility, open embeddings, MaxSim concepts\)\. *(Analyst view)* ^[55](https://www.topk.io/learn/elasticsearch-api-compatibility),[1](https://docs.topk.io/),[54](https://www.topk.io/use-cases/recsys)
  - Assumption: Public docs and standards allow reimplementation
- **Edge supported by public evidence:** Published end\-to\-end benchmark \(124\.8 ms p99, 176\.5 QPS\) is company\-published and is verifiable by reproduction of that run\. *(Analyst view)* ^[15](https://www.topk.io/use-cases/recsys)
  - Assumption: Benchmark dataset and config would be shared for reproduction
- **Cannot be judged from outside:** Real\-world recall/precision on customer data and production robustness cannot be judged externally without logs, test harnesses, or SalesEQ corroboration\. *(Analyst view)* ^[18](https://www.topk.io/customers/saleseq),[9](https://www.topk.io/customers/saleseq),[15](https://www.topk.io/use-cases/recsys)
  - Assumption: Requires internal metrics or customer audits

## Risks and caveats

- Unverified customer claim: SalesEQ testimonial exists on vendor site but independent corroboration not found\. *(Analyst view)* ^[9](https://www.topk.io/customers/saleseq),[18](https://www.topk.io/customers/saleseq)
- Security attestation behind NDA: public pointer to Vanta exists, but the SOC2 evidence requires requester access\. *(Analyst view)* ^[17](https://www.topk.io/security),[16](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- Benchmark and performance claims are self\-reported; reproduction and dataset/context are necessary to trust latency/recall numbers\. *(Analyst view)* ^[15](https://www.topk.io/use-cases/recsys),[54](https://www.topk.io/use-cases/recsys)

## Questions for founders

- Can TopK provide the raw benchmark config, dataset, and replica topology used for the 124\.8 ms p99 / 176\.5 QPS result? *(Analyst view)* ^[15](https://www.topk.io/use-cases/recsys)
- Please provide the SOC 2 Type I report or attestation artifact currently behind NDA and confirm date/coverage\. *(Analyst view)* ^[17](https://www.topk.io/security),[16](https://vestbee.com/insights/articles/top-k-secures-5-5-m)
- Request an independent SalesEQ reference call or telemetry demonstrating production recall and index lag under their workload\. *(Analyst view)* ^[9](https://www.topk.io/customers/saleseq),[18](https://www.topk.io/customers/saleseq),[53](https://www.topk.io/use-cases/recsys)
- Which embedding models are offered in\-product vs\. those requiring customer OpenAI accounts, and what data leaves customer boundaries? *(Analyst view)* ^[2](https://www.topk.io/),[25](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/),[41](https://www.topk.io/pricing)

## Sources

1. [docs\.topk\.io](https://docs.topk.io/) · Company's own website · Product capability — “Semantic, keyword, dense, sparse, and multi\-vector search with filtering and custom ranking, in one API\.”
2. [topk\.io](https://www.topk.io/) · Company's own website · Technical claim — “Open\-source multimodal multi\-vector embedding models, with a production model offered inside TopK for $0\.05/1M tokens\.”
3. [lupa\.cz](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/) · Independent press · Product capability — “Firma nabízí SDK v Pythonu a Node\.js, respektive JavaScript\.”
4. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-04\-15 — “api\.topk\.io \(first certificate 2026\-04\-15\)”
5. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-02\-06 — “console\.topk\.io \(first certificate 2025\-02\-06\)”
6. [siliconcanals\.com](https://siliconcanals.com/?p=65960) · Independent press · Funding round — “TopK has raised $5\.5M \(nearly €4\.66M\) in seed funding to advance its AI\-native search platform\.”
7. [vestbee\.com](https://vestbee.com/insights/articles/top-k-secures-5-5-m) · Independent press · Funding round — “Prague\-based firm TopK, which builds an AI\-powered search engine for better data retrieval, has secured $5\.5 million in a seed funding round from Earlybird, KAYA, Irregular Expressions, and several angel investors, as Vestbee was told\.”
8. [earlybird\.com](https://earlybird.com/companies/topk) · Independent press · Press article — “Earlybird”
9. [topk\.io](https://www.topk.io/customers/saleseq) · Company's own website · Customer — ““TopK has been one of our most important third\-party vendors\. We absolutely love the platform, and we’ve told so many people about it\.””
10. [siliconcanals\.com](https://siliconcanals.com/?p=65960) · Independent press · Press article · 2025\-07\-01 — “Prague’s TopK raises €4\.6M to build a search engine for the AI era”
11. [github\.com](https://github.com/topk-io/topk) · Public technical artifact · GitHub repository · 2026\-11\-17 — “topk\-io/topk · High\-quality search for AI\-native applications\. · Rust · last push 2026\-11\-17”
12. [github\.com](https://github.com/topk-io/llama-index-vector-stores-topk) · Public technical artifact · GitHub repository · 2026\-11\-17 — “topk\-io/llama\-index\-vector\-stores\-topk · Python · last push 2026\-11\-17”
13. [openalex\.org](https://openalex.org/W7128615148) · Public technical artifact · Research paper · 2026\-04\-09 — “Efficient Learning of Sparse Representations from Interactions · International World Wide Web Conference \(WWW\) · cited 5×”
14. [openalex\.org](https://openalex.org/W7214324948) · Public technical artifact · Research paper · 2026\-09\-25 — “Sparse Autoencoders as Semantic Domain Adapters for Recommender Systems · ACM Conference on Recommender Systems \(RecSys\)”
15. [topk\.io](https://www.topk.io/use-cases/recsys) · Company's own website · Technical claim — “In the production semantic\_index benchmark, TopK measured the whole path end\-to\-end: ingest, embedding inference, indexing, concurrent queries, and retrieval quality\. On a sustained 10M\-scale run, the system served multi\-vector retrieval at 124\.8 ms p99 latency while sustaining 176\.5 QPS per replica set, with 1\.2s inde…”
16. [vestbee\.com](https://vestbee.com/insights/articles/top-k-secures-5-5-m) · Independent press · Technical claim — “security and reliability features such as SOC 2 Type I compliance and a 99\.9% uptime guarantee\.”
17. [topk\.io](https://www.topk.io/security) · Company's own website · Independent check of a claim — “Public attestation pointer found: vanta on https://www\.topk\.io/security, subdomain trust\.topk\.io\. The report itself is shared under NDA — request it\.”
18. [topk\.io](https://www.topk.io/customers/saleseq) · Company's own website · Independent check of a claim
19. [cc\.cz](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/) · Independent press · Funding round — “Loni rozjeli vlastní startup TopK – a teď nabírají investici ve výši necelých 120 milionů korun\.”
20. [lupa\.cz](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/) · Independent press · Funding round — “TopK získal investici 120 milionů korun \(5,5 milionu dolarů\) od fondů Earlybird, Kaya, Irregular Expressions a několika andělských investorů\. Jde o prvotní kolo seed, na jehož poměry jde o vysokou sumu\.”
21. [startitup\.sk](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/) · Independent press · Funding round — “Startup TopK, založený slovenskou dvojicou Marek Galovič a Jerguš Lejko, získal 5,5 milióna dolárov v rámci seed investičného kola\.”
22. [vestbee\.com](https://vestbee.com/insights/articles/top-k-secures-5-5-m) · Independent press · Press article · 2025\-07\-01 — “Prague\-based startup TopK secures $5\.5M to revolutionize AI\-native search engines \| Vestbee”
23. [euro\.cz](https://www.euro.cz/clanky/cesko-slovensky-startup-topk-chce-zmenit-zpusob-vyhledavani-v-ere-ai-od-investoru-ziskal-120-milionu-a-miri-na-firmy-typu-openai/) · Independent press · Press article · 2025\-07\-01 — “Česko\-slovenský startup TopK chce změnit způsob vyhledávání v éře umělé inteligence\. Nabírá 120 milionů korun a míří i na firmy typu OpenAI \- Euro\.cz”
24. [topk\.io](https://www.topk.io/use-cases/recsys) · Company's own website · Product capability — “Bring your own late\-interaction representations with multi\_vector\_index and SMVE , or use managed semantic\_index for batteries\-included retrieval over text data with managed multi\-vector inference\.”
25. [startitup\.sk](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/) · Independent press · Product capability — “V čase, keď prudko rastie záujem o jazykové modely ako ChatGPT, TopK reaguje technológiou, ktorá prepája rôzne prístupy do jedného flexibilného systému\.”
26. [cc\.cz](https://cc.cz/chodili-spolu-na-stredni-ted-nabiraji-120-milionu-a-chteji-pohanet-vyhledavani-pro-top-aplikace/) · Independent press · Product capability — “To vývojářům umožňuje doladit výsledky pro jejich konkrétní doménu a použití, například v e\-commerce, financích, zdravotnictví či právu\.”
27. [openalex\.org](https://openalex.org/W2921738510) · Public technical artifact · Research paper · 2019\-03\-01 — “PBK/TOPK overexpression and survival in solid tumors: A PRISMA\-compliant meta\-analysis · Medicine · cited 21×”
28. [github\.com](https://github.com/topk-io/dars) · Public technical artifact · GitHub repository · 2026\-02\-09 — “topk\-io/dars · Declarative Agents in Rust · Rust · last push 2026\-02\-09”
29. [github\.com](https://github.com/topk-io/topk-haystack) · Public technical artifact · GitHub repository · 2026\-06\-08 — “topk\-io/topk\-haystack · Python · last push 2026\-06\-08”
30. [github\.com](https://github.com/topk-io/bench) · Public technical artifact · GitHub repository · 2026\-08\-07 — “topk\-io/bench · Reproducible benchmarking tool for evaluating vector databases under realistic workloads\. · Rust · last push 2026\-08\-07”
31. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-01\-26 — “docs\.topk\.io \(first certificate 2025\-01\-26\)”
32. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2025\-05\-19 — “status\.topk\.io \(first certificate 2025\-05\-19\)”
33. [topk\.io](https://www.topk.io/) · Company's own website · Pricing — “with a production model offered inside TopK for $0\.05/1M tokens\.”
34. [topk\.io](https://www.topk.io/) · Company's own website · Product capability — “Retrieval engine, models, and inference built together\.”
35. [siliconcanals\.com](https://siliconcanals.com/?p=65960) · Independent press · Product capability — “The company is developing a unified search engine that enables developers and AI agents to manage both structured and unstructured data through a single system\.”
36. [vestbee\.com](https://vestbee.com/insights/articles/top-k-secures-5-5-m) · Independent press · Product capability — “TopK develops a search engine that combines vector search, keyword matching, and filtering in a single query system\.”
37. [lupa\.cz](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/) · Independent press · Press article · 2025\-07\-01 — “Databáze s příchodem AI prochází zásadní transformací\. Česko\-slovenský startup na to získal 120 milionů \- Lupa\.cz”
38. [topk\.io](https://www.topk.io/pricing) · Company's own website · Pricing — “Pay only for what you use\. Transparent, usage\-based pricing, billed monthly\.”
39. [topk\.io](https://www.topk.io/pricing) · Company's own website · Pricing — “Start with $10 free credits”
40. [topk\.io](https://www.topk.io/pricing) · Company's own website · Pricing — “Write requests Batched upsert operations per 1K requests $ 0\.01”
41. [topk\.io](https://www.topk.io/pricing) · Company's own website · Pricing — “Text &amp; Image embedding Built\-in multi\-vector embeddings per 1M tokens $ 0\.05”
42. [tech\.eu](https://tech.eu/2025/07/01/topk-raises-55m-to-develop-ai-native-search-engine-for-enterprises) · Independent press · Press article · 2025\-07\-01 — “TopK raises $5\.5M to develop AI\-native search engine for enterprises \- Tech\.eu”
43. [itkey\.media](https://itkey.media/topk-raises-usd-5-5m-to-tackle-chatgpt-era-challenges-with-ai-native-hybrid-search-engine-for-enterprises/) · Independent press · Press article · 2025\-08\-11 — “TopK Raises USD 5\.5M to Tackle ChatGPT\-Era Challenges with AI\-Native Hybrid Search Engine for Enterprises \- ITKeyMedia”
44. [topk\.io](https://www.topk.io/learn/hybrid-search-elasticsearch-api) · Company's own website · Website page — “Can You Do Hybrid Search Through the Elasticsearch API? \| TopK”
45. [topk\.io](https://www.topk.io/learn/elasticsearch-api-compatibility) · Company's own website · GitHub organisation — “elastic · None public repos”
46. [redis\.io](https://redis.io/docs/latest/develop/data-types/probabilistic/top-k) · Independent press · Press article — “Top\-K \| Docs”
47. [startitup\.sk](https://www.startitup.sk/web-stories/slovaci-chcu-prepisat-buducnost-vyhladavania-startup-topk-ziskal-miliony-na-ai-revoluciu/) · Independent press · Team claim — “Startup TopK, založený slovenskou dvojicou Marek Galovič a Jerguš Lejko, získal 5,5 milióna dolárov v rámci seed investičného kola\.”
48. [lupa\.cz](https://www.lupa.cz/aktuality/databaze-s-prichodem-ai-prochazi-zasadni-transformaci-cesko-slovensky-startup-na-to-ziskal-120-milionu/) · Independent press · Team claim — “Zakladateli TopK jsou Marek Galovič, Jerguš Lejko, Peter Toth a Barbora Grillusová\.”
49. [crt\.sh](https://crt.sh/?q=%25.topk.io&output=json) · Public technical artifact · Subdomain \(certificates\) · 2026\-06\-22 — “login\.topk\.io \(first certificate 2026\-06\-22\)”
50. [github\.com](https://github.com/topk-io/langchain-topk) · Public technical artifact · GitHub repository · 2026\-11\-17 — “topk\-io/langchain\-topk · Python · last push 2026\-11\-17”
51. [github\.com](https://github.com/topk-io) · Public technical artifact · GitHub organisation · 2024\-11\-02 — “topk\-io · 19 public repos”
52. [topk\.io](https://www.topk.io/use-cases/recsys) · Company's own website · Product capability — “TopK gives RecSys teams one serving layer for fresh writes, product\-aware filters, and dense, sparse, keyword, and multi\-vector retrieval across every surface\.”
53. [topk\.io](https://www.topk.io/use-cases/recsys) · Company's own website · Product capability — “Online writes without rebuilds TopK can ingest 70 MB/s per partition with writes becoming queryable without index rebuild lag\.”
54. [topk\.io](https://www.topk.io/use-cases/recsys) · Company's own website · Product capability — “Late interaction is expressive because it does more work: MaxSim compares query vectors against item vectors and aggregates the best matches\. TopK does not brute\-force that across the corpus\. Managed semantic\_index and bring\-your\-own representations in multi\_vector\_index both use sparse multi\-vector encoding as a fast …”
55. [topk\.io](https://www.topk.io/learn/elasticsearch-api-compatibility) · Company's own website · Website page — “Can You Replace Elasticsearch Without Rewriting Queries? \| TopK”
56. [patents\.google\.com](https://patents.google.com/patent/US20240254752A1) · Official record · Patent publication — “US20240254752A1 · Modular assembly including multiple modules · Topk USA LLC”

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

Analysis: gpt\-5\-mini (cost $0.0175); AI extraction cost $0.0082. Full fact table: CSV export.

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
- F7778 · source\_unavailable · Unavailable · [https://www\.hlidacstatu\.cz/hledat](https://www.hlidacstatu.cz/hledat)
- F7779 · source\_check · Checked · no results · [https://cordis\.europa\.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27TopK%27](https://cordis.europa.eu/search/en?q=contenttype%3D%27project%27%20AND%20%27TopK%27)
- F7780 · source\_unavailable · Unavailable · [https://starfos\.tacr\.cz](https://starfos.tacr.cz)
