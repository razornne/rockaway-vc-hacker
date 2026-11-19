import json
from pathlib import Path

import pytest

from dd.collectors.apps import AppsCollector, seller_matches
from dd.collectors.base import Context
from dd.collectors.code import CodeCollector, domain_matches
from dd.collectors.history import HistoryCollector, parse_cdx
from dd.collectors.ml import MLCollector, name_in
from dd.config import Settings
from dd.http import Http, Resp
from dd.store import Company, Store


class FakeHttp:
    """Maps URL substring -> (status, payload)."""

    def __init__(self, routes):
        self.routes = routes
        self.calls = []

    def get(self, url, params=None, headers=None, **kw):
        self.calls.append((url, params))
        for frag, (status, payload) in self.routes.items():
            if frag in url:
                body = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
                return Resp(url, status, body, "application/json", False, "x", "")
        return Resp(url, 404, b"{}", "application/json", False, "x", "")


def make_ctx(tmp_path: Path, routes) -> Context:
    s = Settings(home=tmp_path)
    return Context(settings=s, store=Store(tmp_path / "t.sqlite"), http=FakeHttp(routes))


def test_domain_matches():
    assert domain_matches("https://www.navigara.com/x", "navigara.com")
    assert not domain_matches("https://evilnavigara.com", "navigara.com")
    assert not domain_matches(None, "navigara.com")


def test_code_with_hint(tmp_path):
    routes = {
        "/orgs/acme/repos": (200, [
            {"full_name": "acme/a", "fork": False, "stargazers_count": 5, "pushed_at": "2025-01-02T00:00:00Z"},
            {"full_name": "acme/f", "fork": True, "stargazers_count": 1, "pushed_at": "2025-03-02T00:00:00Z"}]),
        "/repos/acme/a/languages": (200, {"Python": 100}),
        "/repos/acme/a/contributors": (200, [{}, {}]),
        "/orgs/acme": (200, {"login": "acme", "public_repos": 2, "created_at": "2020-01-01T00:00:00Z"}),
    }
    ctx = make_ctx(tmp_path, routes)
    co = Company(id="acme", name="Acme", domain="acme.com", hints={"github_org": "acme"})
    facts = CodeCollector().collect(co, ctx)
    types = [f.type for f in facts]
    assert types.count("github_org") == 1 and types.count("repo") == 1  # fork skipped
    repo = next(f for f in facts if f.type == "repo")
    assert repo.value["contributors"] == 2 and repo.value["languages"] == {"Python": 100}


def test_code_rate_limited_is_unavailable(tmp_path):
    ctx = make_ctx(tmp_path, {"/orgs/acme": (403, {"message": "rate limit exceeded"})})
    co = Company(id="acme", name="Acme", domain="acme.com", hints={"github_org": "acme"})
    facts = CodeCollector().collect(co, ctx)
    assert [f.type for f in facts] == ["source_unavailable"]


def test_code_malformed_org_response_is_reported(tmp_path):
    ctx = make_ctx(tmp_path, {"/orgs/acme": (200, ["unexpected"])})
    co = Company(id="acme", name="Acme", domain="acme.com", hints={"github_org": "acme"})
    facts = CodeCollector().collect(co, ctx)
    assert facts and all(f.type == "source_unavailable" for f in facts)
    assert "unexpected account response" in facts[0].value["reason"]


def test_code_search_requires_domain_match(tmp_path):
    routes = {
        "/search/users": (200, {"items": [{"login": "noise"}]}),
        "/orgs/noise": (200, {"login": "noise", "blog": "https://other.io"}),
    }
    ctx = make_ctx(tmp_path, routes)
    co = Company(id="acme", name="Acme", domain="acme.com")
    assert CodeCollector().collect(co, ctx) == []


def test_ml_exact_author_and_affiliation(tmp_path):
    routes = {
        "/api/models": (200, [{"id": "acme/m1", "downloads": 3}, {"id": "acme-labs/m2"}]),
        "/api/datasets": (200, []),
        "openalex": (200, {"results": [
            {"id": "https://openalex.org/W1", "title": "P", "authorships": [
                {"raw_affiliation_strings": ["Acme AI, Prague"]}]},
            {"id": "https://openalex.org/W2", "title": "Q", "authorships": [
                {"raw_affiliation_strings": ["Acmetron University"]}]}]}),
    }
    ctx = make_ctx(tmp_path, routes)
    co = Company(id="acme", name="Acme", domain="acme.com")
    facts = MLCollector().collect(co, ctx)
    hf_fact = next(f for f in facts if f.type == "hf_model")
    assert hf_fact.key == "acme/m1"
    assert hf_fact.confidence == "medium" and hf_fact.value["identity_unverified"] is True
    assert [f.key for f in facts if f.type == "paper"] == ["W1"]


def test_ml_hf_explicit_hint_is_marked(tmp_path):
    ctx = make_ctx(tmp_path, {"/api/models": (200, [{"id": "acme-labs/m1"}]), "/api/datasets": (200, [])})
    company = Company(id="acme", name="Acme", domain="acme.com", hints={"hf_author": "acme-labs"})
    facts = [f for f in MLCollector().collect(company, ctx) if f.type == "hf_model"]
    assert len(facts) == 1
    assert facts[0].confidence == "high" and facts[0].value["identity_unverified"] is False


def test_ml_api_failure(tmp_path):
    ctx = make_ctx(tmp_path, {"/api/": (503, {}), "openalex": (500, {})})
    facts = MLCollector().collect(Company(id="a", name="A", domain="a.com"), ctx)
    assert facts and all(f.type == "source_unavailable" for f in facts)


def test_ml_malformed_openalex_reports_its_own_source(tmp_path):
    ctx = make_ctx(tmp_path, {"/api/": (200, []), "openalex": (200, ["unexpected"])})
    facts = MLCollector().collect(Company(id="a", name="Acme", domain="a.com"), ctx)
    errors = [f for f in facts if f.type == "source_unavailable"]
    assert any(f.key == "openalex" and "unexpected response shape" in f.value["reason"] for f in errors)


def test_name_in():
    assert name_in("Filuta AI s.r.o.", "Filuta AI")
    assert not name_in("Duvoir Institute", "Duvo")


def test_apps_seller_filter(tmp_path):
    routes = {"itunes.apple.com": (200, {"results": [
        {"trackId": 1, "trackName": "Real", "sellerName": "Acme s.r.o.", "sellerUrl": "https://acme.com"},
        {"trackId": 2, "trackName": "Noise", "sellerName": "Acme Corp Ltd"},
        {"trackId": 3, "trackName": "Dom", "sellerName": "X", "sellerUrl": "https://www.acme.com/app"}]})}
    ctx = make_ctx(tmp_path, routes)
    co = Company(id="acme", name="Acme", domain="acme.com")
    assert seller_matches({"sellerName": "Acme"}, co)
    assert not seller_matches({"sellerName": "Acme Corp Ltd"}, co)
    facts = [f for f in AppsCollector().collect(co, ctx) if f.type == "app"]
    keys = [f.key for f in facts]
    assert keys == ["ios:1", "ios:3"]  # verified company domain matches; unverified name prefix does not
    assert all(f.confidence == "high" for f in facts)  # both passed by verified seller URL


def test_apps_exact_company_name_is_medium_confidence(tmp_path):
    ctx = make_ctx(tmp_path, {"itunes.apple.com": (200, {"results": [
        {"trackId": 1, "trackName": "App", "sellerName": "Acme"}]})})
    facts = AppsCollector().collect(Company(id="acme", name="Acme", domain="acme.com"), ctx)
    app = next(f for f in facts if f.type == "app")
    assert app.key == "ios:1" and app.confidence == "medium"


def test_parse_cdx():
    rows = parse_cdx('[["timestamp","original"],["20200101000000","http://a.com/"]]')
    assert rows == [{"timestamp": "20200101000000", "original": "http://a.com/"}]
    assert parse_cdx("garbage") == []


def test_play_only_accepts_links_from_company_domain(tmp_path):
    ctx = make_ctx(tmp_path, {})
    raw = tmp_path / "press.html"
    raw.write_text('https://play.google.com/store/apps/details?id=unrelated.app', encoding="utf-8")
    ctx.store.add_source_doc(company_id="acme", url="https://news.example/article", kind="article",
                             status=200, content_type="text/html", sha256="x", raw_path=str(raw))
    co = Company(id="acme", name="Acme", domain="acme.com")
    assert AppsCollector()._play(co, ctx) == []
    assert ctx.http.calls == []


class _Client:
    timeout = 30


def test_history_first_capture(tmp_path):
    ctx = make_ctx(tmp_path, {"web.archive.org": (200, [["timestamp", "original", "statuscode"],
                                                          ["20210305101010", "http://acme.com/", "200"]])})
    ctx.http.client = _Client()
    facts = HistoryCollector().collect(Company(id="acme", name="Acme", domain="acme.com"), ctx)
    first = next(f for f in facts if f.key == "domain")
    assert first.event_date == "2021-03-05" and first.source_url.startswith("https://web.archive.org/web/2021")
    assert ctx.http.client.timeout == 30  # restored


def test_history_failure_never_raises(tmp_path):
    ctx = make_ctx(tmp_path, {"web.archive.org": (0, b"timeout")})
    ctx.http.client = _Client()
    facts = HistoryCollector().collect(Company(id="acme", name="Acme", domain="acme.com"), ctx)
    assert facts and all(f.type == "source_unavailable" for f in facts)


def test_history_malformed_response_is_reported(tmp_path):
    ctx = make_ctx(tmp_path, {"web.archive.org": (200, b"not json")})
    ctx.http.client = _Client()
    facts = HistoryCollector().collect(Company(id="acme", name="Acme", domain="acme.com"), ctx)
    assert facts and all(f.type == "source_unavailable" for f in facts)
    assert any("invalid JSON response" in f.value["reason"] for f in facts)


# ---- network ---------------------------------------------------------------

def real_ctx(tmp_path: Path) -> Context:
    s = Settings(home=tmp_path)
    s.ensure_dirs()
    store = Store(s.db_path)
    return Context(settings=s, store=store, http=Http(s.cache_dir, store))


@pytest.mark.network
@pytest.mark.parametrize("cid,name,domain,org", [("filuta", "Filuta AI", "filuta.ai", "FilutaAI"),
                                                  ("navigara", "Navigara", "navigara.com", "navigaracom")])
def test_network_orgs_found(tmp_path, cid, name, domain, org):
    ctx = real_ctx(tmp_path)
    co = Company(id=cid, name=name, domain=domain, hints={"github_org": org})
    ctx.store.upsert_company(co)
    facts = CodeCollector().collect(co, ctx)
    orgs = [f for f in facts if f.type == "github_org"]
    assert orgs and orgs[0].value["login"].lower() == org.lower(), [f.value for f in facts]


@pytest.mark.network
def test_network_navigara_wayback(tmp_path):
    ctx = real_ctx(tmp_path)
    co = Company(id="navigara", name="Navigara", domain="navigara.com")
    ctx.store.upsert_company(co)
    facts = HistoryCollector().collect(co, ctx)
    if all(f.type == "source_unavailable" for f in facts):
        pytest.skip("Wayback unavailable")
    assert any(f.type == "wayback_first" and f.key == "domain" for f in facts)
