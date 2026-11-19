from pathlib import Path
from types import SimpleNamespace
import sqlite3

import pytest

from dd.config import Settings
from dd.extract import Extraction, Item, extract_company, pick_docs
from dd.llm import LLM, BudgetExceeded
from dd.store import Company, Fact, Store


class FakeResponses:
    def __init__(self, items):
        self.items = items
        self.calls = 0

    def parse(self, **kw):
        self.calls += 1
        return SimpleNamespace(output_parsed=Extraction(items=self.items), status="completed",
                               usage=SimpleNamespace(input_tokens=1000, output_tokens=200))


def make(tmp_path: Path, items, budget=1.0):
    s = Settings(openai_api_key="x", budget_usd=budget, prices={"gpt-5-nano": (0.05, 0.40)},
                 model_extract="gpt-5-nano", home=tmp_path)
    store = Store(tmp_path / "db.sqlite")
    fake = SimpleNamespace(responses=FakeResponses(items))
    return s, store, LLM(s, store, client=fake), fake


def add_page(store, tmp_path, cid, url, text):
    raw = tmp_path / f"{abs(hash(url))}.bin"
    raw.write_text(text, encoding="utf-8")
    txt = raw.with_suffix(".txt")
    txt.write_text(text, encoding="utf-8")
    store.add_source_doc(company_id=cid, url=url, kind="page", status=200, content_type="text/html",
                         sha256="x", raw_path=str(raw), text_path=str(txt))


def add_doc(store, cid, url, kind, status, text_path=None):
    store.add_source_doc(company_id=cid, url=url, kind=kind, status=status, content_type="text/html",
                         sha256="x", raw_path=None, text_path=str(text_path) if text_path else None)


def test_snippet_verification_and_cache(tmp_path):
    text = "Acme analyses pull requests and measures AI impact on engineering teams. " * 10
    items = [Item(kind="product_capability", summary="Analyses PRs", quote="analyses pull requests and measures AI impact"),
             Item(kind="customer", summary="Has customer Foo", quote="Trusted by Foo Corp")]  # not in text
    s, store, llm, fake = make(tmp_path, items)
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    add_page(store, tmp_path, "acme", "https://acme.io/", text)
    st = extract_company(store, llm, store.get_company("acme"))
    assert st.accepted == 1 and st.rejected == 1
    assert [f.type for f in store.facts("acme")] == ["product_capability"]
    # second run is served from cache: no new API call, zero cost
    st2 = extract_company(store, llm, store.get_company("acme"))
    assert fake.responses.calls == 1 and st2.cost == 0 and st2.cached == 1


def test_budget_refuses(tmp_path):
    s, store, llm, _ = make(tmp_path, [], budget=0.0)
    with pytest.raises(BudgetExceeded):
        llm.call(purpose="t", model="gpt-5-nano", prompt="hi", schema=Extraction)


def test_unknown_price_refused(tmp_path):
    s, store, llm, _ = make(tmp_path, [])
    with pytest.raises(BudgetExceeded):
        llm.call(purpose="t", model="some-unpriced-model", prompt="hi", schema=Extraction)


def test_failed_and_missing_text_docs_are_skipped_and_reported(tmp_path):
    _, store, llm, fake = make(tmp_path, [Item(kind="tech_claim", summary="Claim", quote="" * 1)])
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    valid_txt = tmp_path / "failed.txt"
    valid_txt.write_text("A failed response should never be sent to the LLM. " * 8, encoding="utf-8")
    add_doc(store, "acme", "https://acme.io/failed", "page", 503, valid_txt)
    add_doc(store, "acme", "https://acme.io/missing", "article", 200, tmp_path / "not-there.txt")
    add_doc(store, "acme", "https://acme.io/no-text-path", "article", 200)

    assert pick_docs(store, "acme") == []
    st = extract_company(store, llm, store.get_company("acme"))
    assert fake.responses.calls == 0 and st.docs == 0
    assert st.skipped_docs == 3
    assert st.skipped_reasons == {"http_failed": 1, "missing_text_file": 1, "missing_text_path": 1}


def test_empty_and_trivial_quotes_are_rejected_with_reasons(tmp_path):
    text = "Acme describes a detailed product capability with multiple supporting words. " * 8
    items = [
        Item(kind="tech_claim", summary="Empty", quote=""),
        Item(kind="tech_claim", summary="Whitespace", quote="   "),
        Item(kind="tech_claim", summary="Trivial", quote="AI is"),
    ]
    _, store, llm, _ = make(tmp_path, items)
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    add_page(store, tmp_path, "acme", "https://acme.io/", text)
    st = extract_company(store, llm, store.get_company("acme"))
    assert st.accepted == 0 and st.rejected == 3
    assert st.rejected_reasons == {"empty_or_trivial_quote": 3}
    assert not store.facts("acme")


def test_quote_must_be_exact_case_sensitive_substring(tmp_path):
    text = "Acme Product delivers a measurable engineering workflow benefit. " * 8
    item = Item(kind="product_capability", summary="Acme product", quote="acme Product delivers")
    _, store, llm, _ = make(tmp_path, [item])
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    add_page(store, tmp_path, "acme", "https://acme.io/", text)
    st = extract_company(store, llm, store.get_company("acme"))
    assert st.accepted == 0 and st.rejected_reasons == {"quote_not_exact_substring": 1}


def test_long_exact_quote_is_stored_without_silent_truncation(tmp_path):
    quote = "The platform helps teams coordinate work across systems with a repeatable technical review process. " * 6
    text = quote + " Additional supporting text makes this a useful document for extraction. " * 4
    item = Item(kind="product_capability", summary="Coordinates technical review", quote=quote.strip())
    _, store, llm, _ = make(tmp_path, [item])
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    add_page(store, tmp_path, "acme", "https://acme.io/", text)
    st = extract_company(store, llm, store.get_company("acme"))
    fact = store.facts("acme")[0]
    assert st.accepted == 1
    assert fact.snippet == quote.strip()
    assert len(fact.snippet) > 400


def test_extract_company_default_cap_and_override(tmp_path):
    text = "Acme provides a specific product capability for engineering teams. " * 8
    _, store, llm, fake = make(tmp_path, [])
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    for i in range(16):
        add_page(store, tmp_path, "acme", f"https://acme.io/page/{i}", text)

    default = extract_company(store, llm, store.get_company("acme"))
    assert default.docs == 12 and fake.responses.calls == 12
    extended = extract_company(store, llm, store.get_company("acme"), max_docs=16)
    assert extended.docs == 16 and fake.responses.calls == 16


def test_funding_and_integration_require_category_evidence(tmp_path):
    funding_quote = "© 2026 Navigara, Inc."
    integration_quote = "Cloudflare · Vercel · OpenAI · Google · Meta · Microsoft"
    text = (funding_quote + " " + integration_quote + " ") * 8
    items = [
        Item(kind="funding_round", summary="company behind index", quote=funding_quote, date="2026-01-01"),
        Item(kind="integration", summary="platforms integrated", quote=integration_quote),
    ]
    _, store, llm, _ = make(tmp_path, items)
    store.upsert_company(Company(id="navigara", name="Navigara", domain="navigara.com"))
    add_page(store, tmp_path, "navigara", "https://navigara.com/", text)

    st = extract_company(store, llm, store.get_company("navigara"))
    assert st.accepted == 0 and st.rejected == 2
    assert st.rejected_reasons == {
        "funding_category_unsupported": 1,
        "integration_relationship_unsupported": 1,
    }
    assert not store.facts("navigara")


def test_supported_categories_and_dates_keep_only_quoted_precision(tmp_path):
    funding_quote = "The company raised €2m in a seed round in 2025."
    integration_quote = "The product integrates with Salesforce through an API connector."
    text = f"{funding_quote} {integration_quote} " * 8
    items = [
        Item(kind="funding_round", summary="Raised a seed round", quote=funding_quote, date="2025-01-01",
             amount="€2m", round="seed"),
        Item(kind="integration", summary="Integrates with Salesforce", quote=integration_quote, name="Salesforce"),
    ]
    _, store, llm, _ = make(tmp_path, items)
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    add_page(store, tmp_path, "acme", "https://acme.io/", text)

    st = extract_company(store, llm, store.get_company("acme"))
    facts = store.facts("acme")
    assert st.accepted == 2 and st.rejected == 0
    funding = next(f for f in facts if f.type == "funding_round")
    integration = next(f for f in facts if f.type == "integration")
    # The quote contains only a year; do not fabricate a day/month such as 2025-01-01.
    assert funding.event_date is None and funding.value.get("date") is None
    assert integration.value["name"] == "Salesforce"


def test_czech_funding_and_integration_evidence_is_recognized(tmp_path):
    funding_quote = "Společnost získala seed investici v roce 2025."
    integration_quote = "Produkt podporuje integraci s Salesforce přes API."
    text = f"{funding_quote} {integration_quote} " * 8
    items = [
        Item(kind="funding_round", summary="Získala seed investici", quote=funding_quote, date="2025"),
        Item(kind="integration", summary="Podporuje integraci", quote=integration_quote),
    ]
    _, store, llm, _ = make(tmp_path, items)
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    add_page(store, tmp_path, "acme", "https://acme.io/", text)
    st = extract_company(store, llm, store.get_company("acme"))
    funding = next(f for f in store.facts("acme") if f.type == "funding_round")
    assert st.accepted == 2 and st.rejected == 0
    assert funding.event_date == "2025" and funding.date_precision == "year"


def test_atomic_fact_replacement_preserves_previous_snapshot_on_write_failure(tmp_path):
    store = Store(tmp_path / "db.sqlite")
    old = Fact(company_id="acme", type="product_capability", key="old", value={"summary": "old"},
               source_url="https://acme.io/old", extractor="llm_extract")
    store.add_facts([old])
    store.db.execute(
        """CREATE TRIGGER reject_bad_fact BEFORE INSERT ON fact WHEN NEW.key='explode'
           BEGIN SELECT RAISE(ABORT, 'forced write failure'); END""")
    store.db.commit()
    replacement = [
        Fact(company_id="acme", type="product_capability", key="new", value={"summary": "new"},
             source_url="https://acme.io/new", extractor="llm_extract"),
        Fact(company_id="acme", type="product_capability", key="explode", value={"summary": "bad"},
             source_url="https://acme.io/bad", extractor="llm_extract"),
    ]

    with pytest.raises(sqlite3.IntegrityError):
        store.replace_facts("acme", "llm_extract", replacement)

    facts = store.facts("acme")
    assert [(f.key, f.value["summary"]) for f in facts] == [("old", "old")]


def test_quote_matching_tolerates_only_whitespace_differences():
    from dd.extract import locate_quote
    src = "Czech Founders vkládají do platformy Cruxo\ninvestici ve výši 20 milionů\nPresto Ventures\n (\nknown\n for investing"
    assert locate_quote("platformy Cruxo investici ve výši 20 milionů", src) == "platformy Cruxo investici ve výši 20 milionů"
    assert locate_quote("Presto Ventures (known for investing", src) == "Presto Ventures ( known for investing"
    assert locate_quote("presto ventures (known for investing", src) is None   # case still matters
    assert locate_quote("platformy Cruxo investici ve výši 30 milionů", src) is None  # characters still matter


def test_semantic_guards_from_audit():
    from dd.extract import _quote_rejection_reason
    src = ("Last 30 days · 350 engineers Engineering capacity. How the team uses AI · 350 developers. "
           "Founded in 2025 by Jirka Bachel and Peter Malina, Navigara builds tools. "
           "If your AI bill exploded when you moved off per-seat pricing. There is no decision-making based on automated processing.")
    r = lambda q, kind, url="https://navigara.com/": _quote_rejection_reason(q, src, kind, url, "Navigara")
    assert r("Last 30 days · 350 engineers Engineering capacity", "team_claim") == "team_claim_not_about_company"
    assert r("How the team uses AI · 350 developers", "team_claim") == "team_claim_not_about_company"
    assert r("Founded in 2025 by Jirka Bachel and Peter Malina", "team_claim") is None
    assert r("If your AI bill exploded when you moved off per-seat pricing", "pricing",
             "https://navigara.com/blog/ai-bill") == "pricing_from_blog_commentary"
    assert r("There is no decision-making based on automated processing", "tech_claim",
             "https://filuta.ai/privacy-policy") == "legal_page_boilerplate"


def test_subsidy_agreement_is_not_a_customer_contract_and_duplicates_merge():
    from dd.collectors.public_money import SUBSIDY_SUBJECT, _matching_subsidy, dedupe_subsidies
    assert SUBSIDY_SUBJECT.search("Poskytnutí účelové podpory")
    subs = dedupe_subsidies([
        {"id": 1, "provider": "MPO", "title": "CZ.01.02.01/04/25_057/0008388 - CRUXO rozvoj retail media platformy",
         "year": "2025", "amount_czk": 2449765, "url": "u1"},
        {"id": 2, "provider": "MMR", "title": "CRUXO rozvoj retail media platformy", "year": "2026",
         "amount_czk": 2449765, "url": "u2"}])
    assert len(subs) == 1 and subs[0]["also_listed_as"][0]["provider"] == "MMR"
    grant = [{"id": 3, "provider": "MPO", "title": "AI agenti", "year": "2025", "amount_czk": 36790550, "url": "u3"}]
    assert _matching_subsidy({"signed": "2025-10-06", "amount_czk": 35675527}, grant) is grant[0]


def test_dropped_pages_do_not_feed_extraction(tmp_path):
    """A page a later guard dropped (ATS vendor site, same-name company) stays in source_doc but is not extracted."""
    from dd.store import Fact
    _, store, _, _ = make(tmp_path, [])
    store.upsert_company(Company(id="acme", name="Acme", domain="acme.io"))
    add_page(store, tmp_path, "acme", "https://acme.io/", "Acme product page " * 30)
    add_page(store, tmp_path, "acme", "https://www.homerun.co/", "Homerun ATS customers " * 30)
    assert len(pick_docs(store, "acme")) == 2   # no collector facts yet: nothing to filter by
    store.replace_facts("acme", "web", [Fact(company_id="acme", type="web_page", key="home", value={},
                                             source_url="https://acme.io/", extractor="web", confidence="high")])
    assert [d["url"] for d in pick_docs(store, "acme")] == ["https://acme.io/"]
