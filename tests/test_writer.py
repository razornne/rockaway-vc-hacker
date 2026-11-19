import csv
import json
from pathlib import Path

import pytest

from dd.analyze import fact_snapshot_sha256
from dd.store import Company, Fact, Store
from dd.writer import write_dossier


KINDS = ("ownership", "tech_profile", "rebuild_check", "risk_flags", "questions")


def make_store(tmp_path: Path):
    store = Store(tmp_path / "state.sqlite")
    company = Company(id="acme", name="Acme <script>alert(1)</script> & Co")
    store.upsert_company(company)
    fact = Fact(company_id=company.id, type="tech_claim", key="model",
                value={"claim": "<img src=x onerror=alert(1)>"},
                source_url="https://example.com/source?q=one&x=2", event_date="2025-01-02",
                snippet="<script>untrusted snippet</script>", extractor="llm_extract", confidence="medium")
    store.add_facts([fact])
    fact = store.facts(company.id)[0]
    return store, company, fact


def analysis(company_id: str, fact_ids: list[int] | None = None, **extra):
    sections = []
    for kind in KINDS:
        if kind == "tech_profile":
            sections.append({"kind": kind, "no_data": False, "items": [{
                "text": "<script>alert('analysis')</script> [click](javascript:alert(1))",
                "fact_ids": fact_ids if fact_ids is not None else [1],
                "assessment": True, "confidence": "medium", "assumptions": ["<b>assumption</b>"]} ]})
        else:
            sections.append({"kind": kind, "items": [], "no_data": True})
    return {"company_id": company_id, "generated_at": "2026-11-16T12:00:00Z", "sections": sections,
            "model": "gpt-test", "cost_usd": 0.0123, "cached": False, **extra}


def test_write_dossier_outputs_and_escapes_untrusted_content(tmp_path):
    store, company, fact = make_store(tmp_path)
    store.add_facts([Fact(company_id=company.id, type="source_check", key="empty",
                          value={"source": "test", "status": "empty", "result_count": 0},
                          source_url="https://example.com/check", extractor="fixture")])
    store.add_facts([Fact(company_id=company.id, type="hf_model", key="acme/m1",
                          value={"identity_unverified": True}, source_url="https://huggingface.co/acme/m1",
                          extractor="fixture", confidence="medium")])
    facts = store.facts(company.id)
    store.add_analysis(company.id, "dossier", analysis(company.id, [fact.id],
                                                        facts_hash=fact_snapshot_sha256(company.id, facts)))

    paths = write_dossier(store, company, tmp_path / "out")

    assert set(paths) == {"markdown", "html", "facts_csv"}
    assert all(Path(path).is_absolute() and Path(path).is_file() for path in paths.values())
    markdown = Path(paths["markdown"]).read_text(encoding="utf-8")
    page = Path(paths["html"]).read_text(encoding="utf-8")
    assert f"F{fact.id}" in markdown and "Source appendix" in markdown and "## Sources" in markdown
    assert "<script>" not in markdown
    assert "<script>alert(1)</script>" not in page
    assert "&lt;script&gt;alert(&#x27;analysis&#x27;)&lt;/script&gt;" in page
    assert 'href="javascript:' not in page
    assert 'href="#src-1"' in page and 'id="src-1"' in page and f'id="fact-{fact.id}"' in page
    assert "[1](https://example.com/source?q=one&x=2)" in markdown
    assert "Analyst view" in page and "How this dossier was built" in page
    assert 'href="https://example.com/source?q=one&amp;x=2"' in page
    assert "Identity unverified" in page and "Checked · no results" in page

    with Path(paths["facts_csv"]).open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    assert len(rows) == 3
    fact_row = next(row for row in rows if row["id"] == str(fact.id))
    assert json.loads(fact_row["value_json"]) == fact.value


def test_writer_refuses_items_without_fact_refs(tmp_path):
    store, company, fact = make_store(tmp_path)
    store.add_analysis(company.id, "dossier", analysis(company.id, []))
    with pytest.raises(ValueError, match="no fact references"):
        write_dossier(store, company, tmp_path / "out")
    assert not (tmp_path / "out").exists()


def test_writer_refuses_unknown_fact_ref(tmp_path):
    store, company, _ = make_store(tmp_path)
    store.add_analysis(company.id, "dossier", analysis(company.id, [999999]))
    with pytest.raises(ValueError, match="unknown fact references"):
        write_dossier(store, company, tmp_path / "out")


def test_writer_refuses_cross_company_fact_ref(tmp_path):
    store, company, _ = make_store(tmp_path)
    other = Company(id="other", name="Other")
    store.upsert_company(other)
    store.add_facts([Fact(company_id=other.id, type="tech_claim", value={"x": 1},
                          source_url="https://other.example", extractor="fixture")])
    other_fact = store.facts(other.id)[0]
    store.add_analysis(company.id, "dossier", analysis(company.id, [other_fact.id]))
    with pytest.raises(ValueError, match="cross-company fact references"):
        write_dossier(store, company, tmp_path / "out")


def test_writer_refuses_stale_fact_snapshot(tmp_path):
    store, company, fact = make_store(tmp_path)
    original_hash = fact_snapshot_sha256(company.id, store.facts(company.id))
    store.add_analysis(company.id, "dossier", analysis(company.id, [fact.id], facts_hash=original_hash))
    store.add_facts([Fact(company_id=company.id, type="funding_round", key="new",
                          value={"round": "seed"}, source_url="https://example.com/new", extractor="fixture")])
    with pytest.raises(ValueError, match="stale"):
        write_dossier(store, company, tmp_path / "out")


def test_writer_refuses_stale_v3_analysis(tmp_path):
    from dd.store import Company, Fact, Store
    from dd.writer import write_dossier
    store = Store(tmp_path / "w.sqlite")
    store.upsert_company(Company(id="st", name="St"))
    store.add_facts([Fact(company_id="st", type="customer", key="A", value={"name": "A"},
                          source_url="https://a.test", extractor="x")])
    fid = store.facts("st")[0].id
    from dd.analyze import fact_snapshot_sha256
    h = fact_snapshot_sha256("st", store.facts("st"))
    sections = [{"kind": k, "items": [], "no_data": True} for k in
                ("summary", "ownership", "tech_profile", "rebuild_check", "risk_flags")]
    sections.append({"kind": "questions", "no_data": False, "items": [
        {"text": "Q?", "fact_ids": [fid], "assessment": True, "confidence": "low", "assumptions": []}]})
    store.add_analysis("st", "dossier", {"company_id": "st", "fact_snapshot_sha256": h, "facts_hash": h,
                                         "sections": sections, "signals": {}})
    write_dossier(store, store.get_company("st"), tmp_path / "out")  # fresh: ok
    store.add_facts([Fact(company_id="st", type="customer", key="B", value={"name": "B"},
                          source_url="https://b.test", extractor="x")])
    import pytest
    with pytest.raises(ValueError, match="stale"):
        write_dossier(store, store.get_company("st"), tmp_path / "out")


def test_evidence_strength_is_computed_from_source_types():
    from dd.render import item_strength
    facts = {
        1: Fact(company_id="x", type="registry_shareholder", value={}, source_url="https://ares.gov.cz/x", extractor="registry", id=1),
        2: Fact(company_id="x", type="funding_round", value={}, source_url="https://cc.cz/a", extractor="llm_extract", id=2),
        3: Fact(company_id="x", type="funding_round", value={}, source_url="https://vestbee.com/b", extractor="llm_extract", id=3),
        4: Fact(company_id="x", type="tech_claim", value={}, source_url="https://acme.io/about", extractor="llm_extract", id=4),
    }
    assert item_strength([1], facts, "acme.io", False)[0] == "verified"
    assert item_strength([2, 3], facts, "acme.io", False)[0] == "corroborated"
    assert item_strength([2], facts, "acme.io", False)[0] == "single"
    assert item_strength([4], facts, "acme.io", False)[0] == "claim"
    key, basis = item_strength([1, 4], facts, "acme.io", True)
    assert key == "view" and "official record" in basis and "company's own website" in basis


def test_mixed_independent_and_company_evidence_is_partly_verified():
    from dd.render import item_strength
    facts = {
        1: Fact(company_id="x", type="repo", value={}, source_url="https://github.com/acme/x", extractor="code", id=1),
        2: Fact(company_id="x", type="tech_claim", value={}, source_url="https://acme.io/", extractor="llm_extract", id=2),
    }
    assert item_strength([1, 2], facts, "acme.io", False)[0] == "mixed"


def test_confirmed_verification_upgrades_company_claim():
    from dd.render import confirmed_claims, item_strength
    facts = {
        1: Fact(company_id="x", type="tech_claim", value={}, source_url="https://acme.io/", snippet="Patent pending core",
                extractor="llm_extract", id=1),
        2: Fact(company_id="x", type="verification", value={"check": "patents", "status": "confirmed",
                "claim_snippets": ["Patent pending core"]}, source_url="https://patents.google.com/?assignee=acme",
                extractor="verify", id=2),
    }
    assert item_strength([1], facts, "acme.io", False)[0] == "claim"
    assert item_strength([1], facts, "acme.io", False, confirmed_claims(facts))[0] == "verified"
