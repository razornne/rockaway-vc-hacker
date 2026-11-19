from pathlib import Path

import pytest

from dd.store import Company, Fact, Store
from dd.text import html_to_text, snippet_in


def test_store_roundtrip(tmp_path: Path):
    s = Store(tmp_path / "t.sqlite")
    s.upsert_company(Company(id="x", name="X", domain="x.com", hints={"a": 1}))
    assert s.get_company("x").hints == {"a": 1}
    s.add_facts([Fact(company_id="x", type="subdomain", key="app.x.com", value={"first_seen": "2024-01-01"},
                      source_url="https://crt.sh/?q=x.com", extractor="techfp")])
    # upsert by (company,type,key,url,extractor) must not duplicate
    s.add_facts([Fact(company_id="x", type="subdomain", key="app.x.com", value={"first_seen": "2023-01-01"},
                      source_url="https://crt.sh/?q=x.com", extractor="techfp")])
    fs = s.facts("x")
    assert len(fs) == 1 and fs[0].value["first_seen"] == "2023-01-01"


def test_fact_requires_source(tmp_path: Path):
    s = Store(tmp_path / "t.sqlite")
    with pytest.raises(ValueError):
        s.add_facts([Fact(company_id="x", type="identity", value={}, source_url="")])


def test_text_and_snippet():
    title, text = html_to_text("<html><title>T</title><script>x()</script><p>Hello   <b>world</b></p></html>")
    assert title == "T" and "x()" not in text
    assert snippet_in("hello world", text.replace("\n", " "))


def test_snapshot_failure_keeps_previous_facts(tmp_path):
    s = Store(tmp_path / "t.sqlite")
    previous = Fact(company_id="x", type="identity", value={"old": True}, source_url="https://example.com", extractor="registry")
    s.add_facts([previous])
    # Simulate a storage error after DELETE, to exercise transaction rollback.
    s.db.execute("CREATE TRIGGER reject_new BEFORE INSERT ON fact BEGIN SELECT RAISE(ABORT, 'reject'); END")
    with pytest.raises(Exception, match="reject"):
        s.replace_facts("x", "registry", [previous])
    assert s.facts("x")[0].value == {"old": True}


def test_http_keeps_distinct_queries_and_safe_headers(tmp_path):
    import httpx
    from dd.http import Http
    s = Store(tmp_path / "t.sqlite")
    h = Http(tmp_path / "cache", store=s, min_delay=0)
    h.client.close()
    h.client = httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(
        200, json={"ok": True}, headers={"x-powered-by": "Next.js", "set-cookie": "secret=123"})))
    try:
        first = h.get("https://example.com/search", params={"page": 1}, company_id="x", kind="api")
        second = h.get("https://example.com/search", params={"page": 2}, company_id="x", kind="api")
        cached = h.get("https://example.com/search", params={"page": 1}, company_id="x", kind="api")
        assert first.doc_id != second.doc_id
        assert cached.from_cache and cached.doc_id == first.doc_id
        assert cached.headers == {"x-powered-by": "Next.js"}
        assert "secret" not in "".join(p.read_text() for p in (tmp_path / "cache").rglob("*.json"))
    finally:
        h.client.close()
