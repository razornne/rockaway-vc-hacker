from __future__ import annotations

import hashlib
from pathlib import Path
from urllib.parse import urlencode

import pytest

from dd.collectors.base import Context
from dd.collectors.press import PressCollector
from dd.collectors.public_money import PublicMoneyCollector, parse_contracts_api, parse_subsidies_api
from dd.config import Settings
from dd.http import Resp
from dd.search import search_detailed, usable_public_url
from dd.store import Company, Store


class StubHttp:
    """Small HTTP fixture that also records company-scoped source documents."""

    def __init__(self, root: Path, store: Store, routes=()):
        self.root = root
        self.store = store
        self.routes = list(routes)
        self.calls = []

    def _response(self, method, url, params=None, body=None, company_id=None, kind=None, title=None):
        full_url = url + ("?" + urlencode(params, doseq=True) if params else "")
        self.calls.append((method, full_url, company_id, kind, title))
        match = next((r for needle, r in self.routes if needle in full_url), None)
        if match is None:
            status, content, content_type = 404, b"not found", "text/plain"
        else:
            status, content, content_type = match
        if isinstance(content, str):
            content = content.encode("utf-8")
        key = hashlib.sha256((method + full_url).encode("utf-8")).hexdigest()
        raw = self.root / "responses" / f"{key}.bin"
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_bytes(content)
        resp = Resp(full_url, status, content, content_type, False, hashlib.sha256(content).hexdigest(), str(raw))
        if self.store is not None and company_id and kind:
            resp.doc_id = self.store.add_source_doc(company_id=company_id, url=url, kind=kind, status=status,
                                                    content_type=content_type, sha256=resp.sha256,
                                                    raw_path=str(raw), title=title)
        return resp

    def get(self, url, params=None, headers=None, company_id=None, kind=None, title=None, **kwargs):
        return self._response("GET", url, params, company_id=company_id, kind=kind, title=title)

    def post(self, url, json_body=None, headers=None, company_id=None, kind=None, title=None, **kwargs):
        return self._response("POST", url, body=json_body, company_id=company_id, kind=kind, title=title)


def make_context(tmp_path: Path, routes=(), **settings_kwargs):
    store = Store(tmp_path / "db.sqlite")
    settings = Settings(home=tmp_path, **settings_kwargs)
    return Context(settings=settings, store=store, http=StubHttp(tmp_path, store, routes))


def test_public_money_amount_parsers_and_recipient_shape():
    contracts = parse_contracts_api({"results": [{
        "id": "contract-1", "datumUzavreni": "2026-02-03", "platce": {"nazev": "Agency", "ico": "00000001"},
        "prijemce": {"nazev": "Filuta AI", "ico": "09745424"}, "hodnotaVcetneDph": "35 700 000 Kč",
        "predmet": "Research",
    }]})
    assert contracts[0]["supplier"] == "Filuta AI"
    assert contracts[0]["amount_czk"] == 35_700_000

    # shape of a live /api/v2/dotace/hledat result (api.hlidacstatu.cz, verified 2026-11-17), trimmed
    grants = parse_subsidies_api({"results": [
        {"id": "IsVavai-1", "recipient": {"ico": "09745424", "name": "Filuta AI CZ s.r.o."},
         "subsidyProvider": "Ministerstvo průmyslu a obchodu", "subsidyProviderIco": "47609109",
         "projectName": "Samoobslužní AI plánovací agenti", "approvedYear": 2025, "payedAmount": None,
         "subsidyAmount": 36790550.0, "assumedAmount": 36790550.0, "hints": {"isOriginal": True, "duplicates": []}},
        {"id": "Eufondy-dup", "recipient": {"name": "Filuta AI CZ s.r.o."}, "subsidyProvider": "MMR",
         "projectName": "Samoobslužní AI plánovací agenti", "approvedYear": 2025, "subsidyAmount": 36790550.0,
         "hints": {"isOriginal": False, "originalSubsidyId": "IsVavai-1"}},
    ]})
    assert len(grants) == 1  # Hlídač-marked duplicate dropped
    assert grants[0]["amount_czk"] == 36_790_550
    assert grants[0]["provider"] == "Ministerstvo průmyslu a obchodu" and grants[0]["year"] == "2025"
    assert grants[0]["title"] == "Samoobslužní AI plánovací agenti"


def test_hlidac_records_empty_and_error_per_dataset(monkeypatch, tmp_path):
    ctx = make_context(tmp_path, hlidac_token="test-token")
    company = Company(id="filuta", name="Filuta AI", ico="09745424")
    collector = PublicMoneyCollector()

    def api_pages(_ctx, _company, dataset, _parser):
        if dataset == "smlouvy":
            return []
        raise RuntimeError("API unavailable")

    def html_pages(_ctx, _company, base, _parser, _ico):
        assert "dotace" in base
        return [], "HTML HTTP 503"

    monkeypatch.setattr(collector, "_api_pages", api_pages)
    monkeypatch.setattr(collector, "_html_pages", html_pages)
    facts = collector._hlidac(company, ctx)
    checks = [f for f in facts if f.type == "source_check"]
    errors = [f for f in facts if f.type == "source_unavailable"]
    assert [f.key for f in checks] == ["hlidac_contracts_empty"]
    assert [f.key for f in errors] == ["hlidac_subsidies"]
    assert checks[0].value["status"] == "empty"


def test_public_money_preserves_partial_contract_result_and_marks_other_error(monkeypatch, tmp_path):
    ctx = make_context(tmp_path, hlidac_token="test-token")
    company = Company(id="filuta", name="Filuta AI", ico="09745424")
    collector = PublicMoneyCollector()

    def api_pages(_ctx, _company, dataset, _parser):
        if dataset == "smlouvy":
            return [{"id": "c1", "signed": "2025-01-02", "payer": "Agency", "payer_ico": "00000001",
                     "supplier": "Filuta AI", "supplier_ico": "09745424", "amount_czk": 1000,
                     "subject": "Research", "url": "https://www.hlidacstatu.cz/Detail/c1"}]
        raise RuntimeError("subsidies API unavailable")

    def html_pages(_ctx, _company, base, _parser, _ico):
        return [], "subsidies HTML unavailable"

    monkeypatch.setattr(collector, "_api_pages", api_pages)
    monkeypatch.setattr(collector, "_html_pages", html_pages)
    facts = collector._hlidac(company, ctx)
    assert any(f.type == "gov_contract" and f.key == "c1" for f in facts)
    assert any(f.type == "source_unavailable" and f.key == "hlidac_subsidies" for f in facts)


def test_search_detailed_keeps_partial_keyless_results_and_query_provenance(monkeypatch, tmp_path):
    import dd.search as search_module

    rss = """<?xml version="1.0"?><rss><channel><item><title>Acme seed funding</title>
    <link>https://press.example.com/acme</link><description>Acme raised a seed round.</description>
    <pubDate>Mon, 02 Feb 2026 10:00:00 GMT</pubDate></item></channel></rss>"""
    routes = [
        ("bing.com/news/search", (200, rss, "application/rss+xml")),
        ("cc.cz/", (503, "temporarily unavailable", "text/plain")),
        ("press.example.com/rss", (200, rss, "application/rss+xml")),
    ]
    ctx = make_context(tmp_path, routes)
    monkeypatch.setattr(search_module, "FEEDS", {"press.example.com": "https://press.example.com/rss"})
    batch = search_detailed("Acme seed", ctx, provider="keyless", n=5, company_id="acme")
    assert [s["status"] for s in batch["sources"]] == ["ok", "error", "ok"]
    assert batch["rows"]
    assert all(r["query"] == "Acme seed" for r in batch["rows"])
    assert {r["source"] for r in batch["rows"]} == {"bing_news", "press.example.com"}
    docs = ctx.store.source_docs("acme")
    assert len(docs) == 3
    assert all(call[2] == "acme" and call[3] for call in ctx.http.calls)


def test_press_persists_successful_empty_and_partial_failure_separately(monkeypatch, tmp_path):
    import dd.collectors.press as press_module

    ctx = make_context(tmp_path)
    company = Company(id="acme", name="Acme")
    runs = [
        {"query": "Acme raises", "provider": "keyless", "source": "bing_news", "url": "https://www.bing.com/news/search",
         "status": "empty", "result_count": 0},
        {"query": "Acme raises", "provider": "keyless", "source": "cc.cz", "url": "https://cc.cz/",
         "status": "error", "result_count": 0, "error": "HTTP 503"},
    ]
    monkeypatch.setattr(press_module, "research_seeds", lambda _c: [])
    monkeypatch.setattr(PressCollector, "_search", lambda self, c, ctx: ([], runs))
    facts = PressCollector().collect(company, ctx)
    assert len([f for f in facts if f.type == "search_check" and f.value["status"] == "empty"]) == 1
    assert len([f for f in facts if f.type == "source_unavailable"]) == 1
    assert not any(f.key == "press_none" for f in facts)


def test_press_mention_contains_search_provenance(monkeypatch, tmp_path):
    import dd.collectors.press as press_module

    article = "<html><head><title>Acme raises seed round</title></head><body><p>Acme announced a seed round. " + (
        "The company builds useful products for customers and continues to expand its engineering team. " * 8
    ) + "</p></body></html>"
    ctx = make_context(tmp_path, [("press.example.com/acme", (200, article, "text/html; charset=utf-8"))])
    company = Company(id="acme", name="Acme")
    rows = [{"url": "https://press.example.com/acme", "title": "Acme raises seed round", "published": "2026-02-02",
             "provider": "keyless", "source": "press.example.com", "query": "Acme seed"}]
    runs = [{"query": "Acme seed", "provider": "keyless", "source": "press.example.com",
             "url": "https://press.example.com/rss", "status": "ok", "result_count": 1}]
    monkeypatch.setattr(press_module, "research_seeds", lambda _c: [])
    monkeypatch.setattr(PressCollector, "_search", lambda self, c, ctx: (rows, runs))
    facts = PressCollector().collect(company, ctx)
    mention = next(f for f in facts if f.type == "press_mention")
    assert mention.value["search_provenance"] == [
        {"provider": "keyless", "source": "press.example.com", "query": "Acme seed"}]
    assert mention.snippet and "Acme" in mention.snippet


@pytest.mark.parametrize("status,content_type", [(503, "text/html"), (200, "application/pdf")])
def test_press_attempted_article_failures_are_not_silent(monkeypatch, tmp_path, status, content_type):
    import dd.collectors.press as press_module

    ctx = make_context(tmp_path, [("press.example.com/fail", (status, "bad response", content_type))])
    company = Company(id="acme", name="Acme")
    rows = [{"url": "https://press.example.com/fail", "title": "Acme news", "published": None,
             "provider": "keyless", "source": "press.example.com", "query": "Acme news"}]
    runs = [{"query": "Acme news", "provider": "keyless", "source": "press.example.com",
             "url": "https://press.example.com/rss", "status": "ok", "result_count": 1}]
    monkeypatch.setattr(press_module, "research_seeds", lambda _c: [])
    monkeypatch.setattr(PressCollector, "_search", lambda self, c, ctx: (rows, runs))
    facts = PressCollector().collect(company, ctx)
    failures = [f for f in facts if f.type == "source_unavailable" and f.key == "press:press.example.com"]
    assert len(failures) == 1
    assert failures[0].source_url == "https://press.example.com/fail"


@pytest.mark.parametrize("url", [
    "https://example.com/story", "http://news.example.cz/article",
])
def test_public_http_urls_allowed(url):
    assert usable_public_url(url)


@pytest.mark.parametrize("url", [
    "javascript:alert(1)", "file:///etc/passwd", "http://127.0.0.1/admin", "http://10.0.0.1/",
    "http://localhost/", "https://user:pass@example.com/", "https://news.crunchbase.com/story",
])
def test_nonpublic_or_blocked_urls_rejected(url):
    assert not usable_public_url(url)


def test_url_date_overrides_placeholder_metadata_date():
    from dd.collectors.press import _sane_date
    assert _sane_date("2014-01-01", "https://en.ain.ua/2025/06/25/filuta-ai-raises-42m/") == "2025-06-25"
    assert _sane_date("2025-06-26", "https://en.ain.ua/2025/06/25/x/") == "2025-06-26"
    assert _sane_date("2023-05-03", "https://cc.cz/clanek-bez-data/") == "2023-05-03"
