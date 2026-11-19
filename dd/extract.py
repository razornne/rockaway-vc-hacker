"""LLM extraction of facts from saved page/article text, with snippet verification.

A fact is stored only if its `quote` is an exact, meaningful substring in the source text and its category
passes conservative lexical checks. Rejected items are counted and reported.

Limitation: quote matching and category keywords do not prove that every detail in `summary`, `amount`,
`investors`, or `name` is entailed by the quote. These checks prevent obvious category mismatches; synthesized
claims still require review against the cited source.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from dd.llm import LLM
from dd.store import Fact, Store
PROMPT_VERSION = "extract-v3"
MAX_CHARS = 12000          # per document sent to the model
MAX_DOCS = 12              # per company (cost control)
PAGE_SLOTS = 6             # pages taken before press articles get their quota
ARTICLE_SLOTS = 5          # press articles carry funding history, which sites rarely state
ARTICLE_FUNDING_HINT = re.compile(
    r"invest|fund|raise|seed|series|round|kolo|získal|milion|million|€|\$|financ", re.I)
MIN_QUOTE_ALNUM = 8        # short fragments such as "AI" are not evidence

PAGE_PRIORITY = [  # url substrings, earlier = more important
    "pricing", "price", "product", "platform", "features", "solution", "customers", "case", "docs", "api",
    "about", "company", "security", "trust", "careers", "jobs",
]

FUNDING_EVIDENCE = re.compile(
    r"\b(?:fund(?:ing|ed|s)?|investment|investments|investor|investors|invested|investing|invests?|"
    r"seed|raised|raise|financ(?:e|ed|ing)|round|series\s+(?:pre[- ]?seed|seed|[a-f])|venture\s+capital|"
    r"invest(?:ic\w*|ičn\w*|or\w*|oval\w*|ovat|uje|ují)|financ\w*|"
    r"kolo\s+(?:financování|investiční))\b", re.I)
INTEGRATION_RELATIONSHIPS = tuple(re.compile(pattern, re.I) for pattern in (
    r"\bintegrat(?:e|es|ed|ing|ion|ions)\b.{0,100}\b(?:with|into|to|for)\b",
    r"\bworks?\s+with\b",
    r"\bconnect(?:s|ed|ing)?\s+(?:to|with|into)\b",
    r"\bconnectors?\s+(?:for|to|with)\b",
    r"\b(?:supports?|supporting|supported)\s+(?:the\s+)?(?:integration|integrations|connector|connectors|api|sdk)\b",
    r"\bpartners?\s+with\b|\bpartnered\s+with\b|\bpartnership\s+with\b",
    r"\b(?:api|sdk)\s+(?:integration|integrates?|connects?|for|to|supports?)\b",
    r"\b(?:provides?|offers?|exposes?)\s+(?:an?\s+)?(?:api|sdk)\s+(?:for|to|that)\b",
    r"\bintegrace\s+s\b|\bintegruje\s+se\s+s\b|\bintegrují\s+se\s+s\b",
    r"\bpodporuj\w*\s+(?:integraci|integrace|konektor\w*|api|sdk)\b|"
    r"\bumožňuj\w*\s+(?:integraci|konektor\w*|api|sdk)\b",
    r"\bpropojen\w*\s+s\b|\bpartnerství\s+s\b|\bkonektor\w*\s+(?:pro|k|s)\b",
    r"\bapi\s+(?:pro|k|slouží\s+pro)\b|\bsdk\s+(?:pro|k)\b|"
    r"\bnabíz\w*\s+(?:api|sdk)\s+(?:pro|k)\b",
))

CUSTOMER_EVIDENCE = re.compile(
    r"\b(?:customers?|clients?|trusted\s+by|used\s+by|loved\s+by|chosen\s+by|chose|case\s+stud\w*|deployed\s+(?:at|by|with|for)|"
    r"works?\s+with|working\s+with|partnered\s+with|helped|helps|pilot\w*|rolled\s+out|signed|contract\w*|"
    r"zákazník\w*|klient\w*|používají|používá|spolupracuje|spolupráce|nasadil\w*|nasazen\w*|reference)\b", re.I)
CUSTOMER_PAGE = re.compile(r"/(?:case|customer|client|stories|references|reference|success)", re.I)
# A team claim must be about THIS company's people, not a demo dashboard ("350 engineers") or a benchmarked org.
TEAM_EVIDENCE = re.compile(
    r"\b(?:we|we're|we are|our|us|náš|naše|našeho|našem|tým\w*|founded|co-?founded|founders?|co-?founders?|ceo|cto|coo|"
    r"zakladatel\w*|spoluzakladatel\w*|employees|zaměstnan\w*|headcount|hiring|lidí|people|staff)\b|"
    r"\bthe team (?:is|has|includes)\b|\bteam of\b|\bteam headquartered\b", re.I)
LEGAL_PAGE = re.compile(r"/(?:privacy|terms|cookie|cookies|gdpr|legal|dpa|imprint|impressum|ochrana-osobnich)", re.I)
BLOG_PAGE = re.compile(r"/(?:blog|news|insights|articles?)/", re.I)
GRANT_WORDS = re.compile(r"\b(?:project|programme|program|grant|h2020|horizon|european commission|eu funds?|"
                         r"projekt\w*|dotac\w*|podpor\w*)\b", re.I)
EU_WORDS = re.compile(r"\b(?:european commission|h2020|horizon|eu\b|eic\b|evropsk)", re.I)

Kind = Literal["product_capability", "pricing", "customer", "integration", "funding_round", "tech_claim", "team_claim",
               "business_model", "revenue_claim", "market_claim", "competitor"]


class Item(BaseModel):
    kind: Kind
    summary: str = Field(description="one short factual sentence in English")
    quote: str = Field(description="EXACT verbatim text copied from the document (max ~250 chars) that supports it")
    date: str | None = Field(default=None, description="YYYY-MM-DD / YYYY-MM / YYYY if the text dates it")
    amount: str | None = Field(default=None, description="funding_round / revenue_claim / market_claim: figure with unit or currency as written")
    round: str | None = Field(default=None, description="for funding_round: pre-seed/seed/Series A…")
    investors: list[str] = Field(default_factory=list, description="for funding_round: investors named")
    name: str | None = Field(default=None, description="customer / integration / partner / competitor name")
    stated_by: str | None = Field(default=None, description="market_claim: who makes the statement (the company, the journalist, a named analyst or report)")


class Extraction(BaseModel):
    items: list[Item]


INSTR = """Extract facts about the company "{company}" ({domain}) from the document below.
Return only items clearly supported by the text. Kinds:
- product_capability: a concrete thing the product does (not marketing adjectives)
- pricing: a plan, price or pricing model
- customer: a named customer, logo or case study
- integration: a named integration / platform / partner it works with
- funding_round: an investment round (amount, round, investors, date)
- tech_claim: a technical claim (own models, architecture, patents, accuracy numbers, infrastructure)
- team_claim: team size, notable background, hiring scale (no personal data beyond names and roles)
- business_model: how the company makes money: hardware sales, subscriptions/licences, custom development, R&D contracts, services; who pays (governments, armed forces, industry, consumers)
- revenue_claim: a stated revenue, sales, order book, units sold/produced, number of customers or countries, growth figure (put the figure in `amount`, its period in `date`)
- market_claim: a statement about the market: size, growth, demand drivers, regulation or procurement trends, supply dependence (e.g. on Chinese drones). Fill `stated_by`; put any number in `amount`
- competitor: a named competitor or alternative the company is compared with (put it in `name`); not partners or customers
For every item `quote` MUST be copied exactly, character-for-character, from the document. Quote a meaningful sentence or clause, not one or two generic words. Max 10 items. Prefer specific over generic.

Document URL: {url}
<document>
{text}
</document>"""


@dataclass
class ExtractStats:
    docs: int = 0
    accepted: int = 0
    rejected: int = 0
    cost: float = 0.0
    cached: int = 0
    rejected_examples: list[str] = field(default_factory=list)
    rejected_reasons: dict[str, int] = field(default_factory=dict)
    skipped_docs: int = 0
    skipped_reasons: dict[str, int] = field(default_factory=dict)
    skipped_examples: list[str] = field(default_factory=list)


def _rank(url: str) -> int:
    u = url.lower()
    for i, k in enumerate(PAGE_PRIORITY):
        if k in u:
            return i
    path = re.sub(r"^https?://[^/]+", "", u).strip("/")
    return -1 if path == "" else len(PAGE_PRIORITY)  # homepage first


def _doc_eligibility(doc) -> str | None:
    status = doc["status"]
    if status is None or not 200 <= status < 300:
        return "http_failed"
    text_path = doc["text_path"]
    if not text_path:
        return "missing_text_path"
    try:
        if not Path(text_path).is_file():
            return "missing_text_file"
    except (OSError, ValueError, TypeError):
        return "invalid_text_path"
    return None


def _pick_docs(store: Store, company_id: str, max_docs: int | None = None) -> tuple[list, list[tuple[str, str]]]:
    limit = MAX_DOCS if max_docs is None else max(0, int(max_docs))
    eligible = []
    skipped = []
    # only documents the collectors still stand behind: a page dropped by a later guard (ATS vendor site,
    # same-name company) stays in source_doc but must not feed extraction again
    current = {(f.source_doc_id, f.source_url) for f in store.facts(company_id) if f.extractor in ("web", "press")}
    cur_ids = {i for i, _ in current if i}
    cur_urls = {u for _, u in current if u}
    for doc in store.source_docs(company_id, ["page", "article"]):
        reason = _doc_eligibility(doc)
        if not reason and current and doc["id"] not in cur_ids and doc["url"] not in cur_urls:
            reason = "not_in_current_collection"
        if reason:
            skipped.append((doc["url"], reason))
        else:
            eligible.append(doc)
    pages = sorted([d for d in eligible if d["kind"] == "page"], key=lambda d: _rank(d["url"]))
    # careers pages are parsed deterministically by the web collector; they go last
    pages = [d for d in pages if not _is_careers(d["url"])] + [d for d in pages if _is_careers(d["url"])]
    arts = sorted([d for d in eligible if d["kind"] == "article"],
                  key=lambda d: (not ARTICLE_FUNDING_HINT.search(f"{d['title'] or ''} {d['url']}"), d["id"]))
    return (pages[:PAGE_SLOTS] + arts[:ARTICLE_SLOTS] + pages[PAGE_SLOTS:] + arts[ARTICLE_SLOTS:])[:limit], skipped


def _is_careers(url: str) -> bool:
    return bool(re.search(r"/(careers?|jobs?|join|kariera|prace)(/|$)", url.lower()))


def pick_docs(store: Store, company_id: str, max_docs: int | None = None) -> list:
    """Select usable documents; failures and missing extracted-text files are excluded."""
    docs, _ = _pick_docs(store, company_id, max_docs)
    return docs


def locate_quote(quote: str | None, source: str) -> str | None:
    """Find `quote` in `source` ignoring whitespace only (case and every other character must match).

    Page text is extracted with a newline per HTML element, so inline tags split sentences
    ("Cruxo\\ninvestici", "Ventures\\n (\\nknown"). The model quotes the readable sentence; we accept it only if
    the same characters appear in the same order with whitespace being the only difference, and return the
    source span (whitespace collapsed) as the stored evidence.
    """
    if not quote:
        return None
    if quote in source:
        return quote
    q = re.sub(r"\s+", "", quote)
    if not q:
        return None
    idx = [i for i, ch in enumerate(source) if not ch.isspace()]
    compact = "".join(source[i] for i in idx)
    pos = compact.find(q)
    if pos < 0:
        return None
    span = source[idx[pos]: idx[pos + len(q) - 1] + 1]
    return re.sub(r"\s+", " ", span)


def _quote_rejection_reason(quote: str | None, source: str, kind: str | None = None, url: str = "",
                            company_name: str = "", name: str | None = None) -> str | None:
    if not quote or not quote.strip():
        return "empty_or_trivial_quote"
    terms = re.findall(r"[^\W_]+", quote, flags=re.UNICODE)
    if len(terms) < 2 or sum(len(t) for t in terms) < MIN_QUOTE_ALNUM:
        return "empty_or_trivial_quote"
    if locate_quote(quote, source) is None:
        return "quote_not_exact_substring"
    if kind == "funding_round" and not FUNDING_EVIDENCE.search(quote):
        return "funding_category_unsupported"
    if kind == "integration" and not any(pattern.search(quote) for pattern in INTEGRATION_RELATIONSHIPS):
        return "integration_relationship_unsupported"
    # a list of logos/org names ("Graded live, in public: Microsoft OpenAI Meta…") is not a customer relationship
    if kind == "customer" and not CUSTOMER_EVIDENCE.search(quote) and not CUSTOMER_PAGE.search(url or ""):
        return "customer_relationship_unsupported"
    if kind in ("product_capability", "tech_claim", "team_claim", "pricing", "customer") and LEGAL_PAGE.search(url or ""):
        return "legal_page_boilerplate"
    if kind in ("revenue_claim",) and not re.search(r"\d", quote):
        return "figure_missing"
    if kind == "competitor" and not (name and name.lower() in quote.lower()):
        return "competitor_not_named_in_quote"
    if kind == "competitor" and company_name and name and company_name.lower() in name.lower():
        return "competitor_is_the_company"
    if kind in ("business_model", "revenue_claim", "market_claim") and LEGAL_PAGE.search(url or ""):
        return "legal_page_boilerplate"
    if kind == "pricing" and BLOG_PAGE.search(url or ""):
        return "pricing_from_blog_commentary"
    if kind == "team_claim" and not TEAM_EVIDENCE.search(quote) and not (company_name and company_name.lower() in quote.lower()):
        return "team_claim_not_about_company"
    return None


def _verified_date(value: str | None, quote: str) -> str | None:
    """Keep only the precision explicitly present in the cited quotation."""
    if not value or value not in quote:
        return None
    return value


def _date_precision(value: str | None) -> str | None:
    if not value:
        return None
    return {4: "year", 7: "month", 10: "day"}.get(len(value))


def _record_rejection(st: ExtractStats, kind: str, quote: str, reason: str) -> None:
    st.rejected += 1
    st.rejected_reasons[reason] = st.rejected_reasons.get(reason, 0) + 1
    if len(st.rejected_examples) < 5:
        st.rejected_examples.append(f"{reason} / {kind}: {quote[:80]}")


def _record_skips(st: ExtractStats, skipped: list[tuple[str, str]]) -> None:
    for url, reason in skipped:
        st.skipped_docs += 1
        st.skipped_reasons[reason] = st.skipped_reasons.get(reason, 0) + 1
        if len(st.skipped_examples) < 5:
            st.skipped_examples.append(f"{reason}: {url[:180]}")


def extract_company(store: Store, llm: LLM, company, model: str | None = None,
                    max_docs: int | None = None) -> ExtractStats:
    st = ExtractStats()
    model = model or llm.s.model_extract
    out: list[Fact] = []
    docs, skipped = _pick_docs(store, company.id, max_docs)
    _record_skips(st, skipped)
    for d in docs:
        try:
            text = Path(d["text_path"]).read_text(encoding="utf-8", errors="replace")
        except (OSError, ValueError, TypeError) as e:
            st.skipped_docs += 1
            reason = "text_read_failed"
            st.skipped_reasons[reason] = st.skipped_reasons.get(reason, 0) + 1
            if len(st.skipped_examples) < 5:
                st.skipped_examples.append(f"{reason}: {d['url'][:180]} ({type(e).__name__})")
            continue
        if len(text) < 200:
            st.skipped_docs += 1
            st.skipped_reasons["text_too_short"] = st.skipped_reasons.get("text_too_short", 0) + 1
            if len(st.skipped_examples) < 5:
                st.skipped_examples.append(f"text_too_short: {d['url'][:180]}")
            continue
        chunk = text[:MAX_CHARS]
        prompt = INSTR.format(company=company.name, domain=company.domain or "", url=d["url"], text=chunk)
        r = llm.call(purpose=f"extract:{company.id}", model=model, prompt=prompt, schema=Extraction,
                     max_output_tokens=6000)
        st.docs += 1
        st.cost += r.cost_usd
        st.cached += r.cached
        for it in r.parsed.items:
            rejection_reason = _quote_rejection_reason(it.quote, chunk, it.kind, d["url"], company.name, it.name)
            if rejection_reason:
                _record_rejection(st, it.kind, it.quote, rejection_reason)
                continue
            st.accepted += 1
            evidence = locate_quote(it.quote, chunk) or it.quote
            ftype = it.kind
            if it.kind == "funding_round" and not (it.amount or it.round or it.investors) and GRANT_WORDS.search(evidence):
                # "project funded by the European Commission" is a grant, not an equity round
                ftype = "grant_eu" if EU_WORDS.search(evidence) else "grant_national"
            item_values = it.model_dump()
            item_values["date"] = _verified_date(it.date, evidence)
            value = {k: v for k, v in item_values.items()
                     if k not in ("kind", "quote") and v not in (None, [], "")}
            out.append(Fact(company_id=company.id, type=ftype, key=(it.name or it.summary)[:80], value=value,
                            source_url=d["url"], source_doc_id=d["id"], snippet=evidence,
                            event_date=item_values["date"], date_precision=_date_precision(item_values["date"]),
                            extractor="llm_extract", confidence="medium"))
    store.replace_facts(company.id, "llm_extract", out)
    return st
