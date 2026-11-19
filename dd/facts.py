"""Fact type vocabulary. Collectors must use these types (add new ones here, with a description)."""

FACT_TYPES: dict[str, str] = {
    # identity / registry (Czech)
    "identity": "basic identity: legal name, IČO, legal form, seat, CZ-NACE (value: dict)",
    "registry_incorporation": "company registered (event_date)",
    "registry_shareholder": "a legal-entity shareholder with from/to dates (key: holder name; value: {name, ico, country, from, to})",
    "registry_capital": "registered capital value with from/to (value: {amount_czk, from, to})",
    "registry_officer_change": "statutory body change (no personal data beyond role; value: {role, from, to})",
    "registry_flag": "structural flag: foreign_holding | legal_form_as | no_cz_entity | convertible_suspected (key: flag)",
    "filing": "document in Sbírka listin (value: {doc_type, period, filed, url})",
    "insolvency": "ISIR insolvency record",
    # public money
    "gov_contract": "contract in registr smluv (value: {counterparty, amount_czk, subject})",
    "grant_national": "national grant / subsidy (TA ČR, MPO, CEDR…)",
    "grant_eu": "EU project (CORDIS / EU F&T portal; key = project number; value.defence for EDF/EDIDP/PADR)",
    "eu_registration": "participant record in the EU Funding & Tenders portal (key: PIC; value: {legal_name, validated, projects})",
    "public_tender": "EU procurement notice naming the company (TED; value: {role: winner|tenderer|mentioned, buyer, value, defence_buyer})",
    # accelerators / peers
    "accelerator": "selection into an accelerator, e.g. NATO DIANA (key: programme:year; value: {programme, year, area})",
    "peer_company": "company from a vetted list (NATO DIANA cohorts) whose description overlaps the company's — competitor candidate",
    # press / funding
    "press_mention": "article mentioning the company (value: {title, outlet})",
    "funding_round": "round from press (value: {round, amount, currency, lead, investors})",
    "source_check": "a source was checked successfully but returned no matching records (value includes source and status)",
    "search_check": "press search provenance for one query/provider/source, including status and result count",
    # web / product (from site crawl; LLM-extracted ones carry snippet)
    "web_page": "crawled page of the company site (key: category: product|docs|pricing|careers|privacy|security|blog|about|other)",
    "product_capability": "what the product does (LLM-extracted, snippet required)",
    "pricing": "pricing plan / model (snippet required)",
    "customer": "named customer / logo / case study (snippet required)",
    "job_post": "open role (value: {title, team, location, stack, is_ml})",
    "subprocessor": "third-party processor named in privacy/trust page (key: vendor) — e.g. OpenAI, Anthropic, AWS",
    "integration": "integration / partner named by the company",
    "tech_claim": "technical claim by the company: own models, architecture, patents, benchmarks (snippet required)",
    "team_claim": "team size / background / hiring scale claim (snippet required)",
    "business_model": "how the company makes money and who pays (LLM-extracted, snippet required)",
    "revenue_claim": "stated revenue / sales / units / customer count / growth (snippet required; value.amount)",
    "market_claim": "statement about the market: size, growth, demand drivers, regulation (snippet; value.stated_by)",
    "competitor": "named competitor or alternative the company is compared with (snippet required; key: name)",
    # technical fingerprint
    "tech_stack": "technology detected from headers/HTML/JS (key: tech; value: {category, evidence})",
    "saas_tool": "SaaS detected via DNS MX/TXT (key: vendor)",
    "subdomain": "subdomain seen in certificate transparency (key: fqdn; value: {first_seen})",
    "cert_first": "earliest certificate for the domain (event_date)",
    # code / ML / apps / history
    "github_org": "GitHub organisation (value: {login, public_repos, created_at, followers})",
    "repo": "public repository (key: full_name; value: {stars, language, pushed_at, created_at, fork})",
    "hf_model": "Hugging Face model or dataset (key: id)",
    "paper": "paper by the company/team (value: {title, venue, year})",
    "app": "mobile app (key: store:id; value: {name, seller, released, rating, ratings_count})",
    "wayback_first": "first Wayback capture (key: url pattern, e.g. domain, /pricing, /careers)",
    "patent": "patent publication with the company as assignee (Google Patents; value: {number, title, assignee, granted})",
    "verification": "a company claim checked against an independent source (value: {check, status: confirmed|partly|"
                    "contradicted|not_found|not_checkable, claim_snippet, detail})",
    "source_unavailable":"a source could not be checked (key: source; value: {reason}) — shown as 'no data', not as absence",
}
