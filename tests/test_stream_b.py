import json
from pathlib import Path

from dd.collectors.base import Context
from dd.collectors.techfp import TechFingerprintCollector, normalize_domain, parse_certificates
from dd.config import Settings
from dd.http import Resp
from dd.store import Company, Store


class FakeHttp:
    def __init__(self, routes):
        self.routes = routes
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        for needle, response in self.routes.items():
            if needle in url:
                if isinstance(response, Exception):
                    raise response
                status, content, content_type, headers, doc_id = response
                if not isinstance(content, bytes):
                    content = json.dumps(content).encode("utf-8")
                return Resp(url, status, content, content_type, False, "fake-sha", "fake-cache",
                            doc_id=doc_id, headers=headers)
        return Resp(url, 404, b"", "text/plain", False, "fake-sha", "fake-cache", doc_id=999)


def make_context(tmp_path: Path, routes) -> Context:
    store = Store(tmp_path / "isolated.sqlite")
    return Context(settings=Settings(home=tmp_path), store=store, http=FakeHttp(routes))


def response(status=200, body="", content_type="application/json", headers=None, doc_id=1):
    return status, body, content_type, headers or {}, doc_id


def test_normalize_domain_accepts_url_and_rejects_invalid_values():
    assert normalize_domain("https://www.navigara.com/path") == "navigara.com"
    assert normalize_domain("tést.example") == "xn--tst-bma.example"
    assert normalize_domain("https://not a domain/") is None
    assert normalize_domain("example.com.evil") == "example.com.evil"


def test_parse_certificates_keeps_wildcard_and_ignores_out_of_scope_dates():
    payload = json.dumps([
        {"not_before": "2018-01-01T00:00:00", "name_value": "navigara.com.attacker.test"},
        {"not_before": "2019-02-03T00:00:00", "name_value": "evilnavigara.com"},
        {"not_before": "2021-05-06T00:00:00", "name_value": "*.navigara.com\napp.navigara.com"},
        {"not_before": "2020-04-05T00:00:00", "name_value": "api.navigara.com"},
        {"not_before": "2017-01-01T00:00:00", "name_value": "*.elsewhere.test"},
    ])

    subdomains, first_date = parse_certificates(payload, "navigara.com")

    assert {x["fqdn"] for x in subdomains} == {"*.navigara.com", "api.navigara.com", "app.navigara.com"}
    assert first_date == "2020-04-05"
    wildcard = next(x for x in subdomains if x["fqdn"] == "*.navigara.com")
    assert wildcard["first_seen"] == "2021-05-06"


def test_parse_certificates_keeps_earliest_date_per_name_and_validates_json():
    payload = json.dumps([
        {"not_before": "2022-01-02", "name_value": "docs.navigara.com"},
        {"not_before": "2020-03-04", "name_value": "docs.navigara.com"},
        {"not_before": "not-a-date", "name_value": "api.navigara.com"},
    ])
    subdomains, first_date = parse_certificates(payload, "navigara.com")
    assert {x["fqdn"]: x["first_seen"] for x in subdomains} == {
        "api.navigara.com": None, "docs.navigara.com": "2020-03-04"}
    assert first_date == "2020-03-04"
    assert parse_certificates("not-json", "navigara.com") == ([], None)
    assert parse_certificates("{}", "navigara.com") == ([], None)


def test_dns_provider_matching_uses_hostname_boundaries():
    from dd.collectors.techfp import _contains_dns_vendor

    assert _contains_dns_vendor("10 aspmx.l.google.com.", "google.com")
    assert _contains_dns_vendor('v=spf1 include:_spf.google.com ~all', "google.com")
    assert not _contains_dns_vendor("mx.badgoogle.com", "google.com")
    assert not _contains_dns_vendor("mx.not-google.com", "google.com")
    assert not _contains_dns_vendor("v=spf1 include:google.com.attacker.test ~all", "google.com")


def test_collect_emits_facts_with_direct_source_urls_and_document_ids(tmp_path):
    site_url = "https://navigara.com/"
    mx_url = "https://dns.google/resolve?name=navigara.com&type=MX"
    txt_url = "https://dns.google/resolve?name=navigara.com&type=TXT"
    ct_url = "https://crt.sh/?q=%25.navigara.com&output=json"
    routes = {
        site_url: response(body=("<html><head><meta name='generator' content='Example CMS'></head>"
                                 "<body><div id='__next'></div></body></html>"), content_type="text/html; charset=utf-8",
                           headers={"server": "nginx", "cf-ray": "abc123"}, doc_id=101),
        "type=MX": response(body={"Status": 0, "Answer": [{"data": "10 aspmx.l.google.com."}]}, doc_id=102),
        "type=TXT": response(body={"Status": 0, "Answer": [
            {"data": '"v=spf1 include:badgoogle.com include:_spf.google.com ~all"'}]}, doc_id=103),
        "crt.sh": response(body=[
            {"not_before": "2021-01-01T00:00:00", "name_value": "*.navigara.com\napp.navigara.com"},
            {"not_before": "2010-01-01T00:00:00", "name_value": "navigara.com.bad.test"},
        ], doc_id=104),
    }
    ctx = make_context(tmp_path, routes)
    company = Company(id="navigara", name="Navigara", domain="navigara.com")

    facts = TechFingerprintCollector().collect(company, ctx)

    stack = [f for f in facts if f.type == "tech_stack"]
    assert any(f.value["technology"] == "Next.js" and f.source_url == site_url for f in stack)
    assert any(f.value["technology"] == "Example CMS" for f in stack)
    assert any(f.value["technology"] == "nginx" for f in stack)
    assert any(f.value["technology"] == "Cloudflare" for f in stack)
    tools = [f for f in facts if f.type == "saas_tool"]
    assert {f.key for f in tools} == {"Google Workspace"}
    assert {f.source_url for f in tools} == {mx_url, txt_url}
    assert all(f.source_doc_id in {101, 102, 103, 104} and f.source_url for f in facts)
    assert any(f.type == "subdomain" and f.key == "*.navigara.com" and f.source_url == ct_url for f in facts)
    assert any(f.type == "cert_first" and f.event_date == "2021-01-01" and f.source_doc_id == 104 for f in facts)


def test_dns_rcode_and_unexpected_json_are_reported_without_stopping(tmp_path):
    routes = {
        "type=MX": response(body={"Status": 2, "Answer": []}, doc_id=11),
        "type=TXT": response(body={"Status": 0, "Answer": "not-an-array"}, doc_id=12),
        "crt.sh": response(body=[], doc_id=13),
        "navigara.com/": response(body="<html></html>", content_type="text/html", doc_id=10),
    }
    ctx = make_context(tmp_path, routes)
    facts = TechFingerprintCollector().collect(Company(id="n", name="N", domain="navigara.com"), ctx)

    unavailable = {f.key: f for f in facts if f.type == "source_unavailable"}
    assert "DNS response status 2" in unavailable["dns_mx"].value["reason"]
    assert unavailable["dns_txt"].value["reason"] == "DNS Answer is not a list"
    assert all(f.source_url and f.source_doc_id for f in unavailable.values())
    # A valid empty certificate result is not mislabeled as a source failure.
    assert "crt_sh" not in unavailable


def test_request_exceptions_are_isolated_per_source(tmp_path):
    routes = {
        "navigara.com/": response(body="<html></html>", content_type="text/html", doc_id=21),
        "type=MX": RuntimeError("dns resolver offline"),
        "type=TXT": response(body={"Status": 3}, doc_id=23),
        "crt.sh": response(body=[], doc_id=24),
    }
    ctx = make_context(tmp_path, routes)
    facts = TechFingerprintCollector().collect(Company(id="n", name="N", domain="navigara.com"), ctx)

    failed = next(f for f in facts if f.type == "source_unavailable" and f.key == "dns_mx")
    assert "request failed" in failed.value["reason"]
    assert failed.source_url == "https://dns.google/resolve?name=navigara.com&type=MX"
    assert all(f.source_url for f in facts)


def test_http_and_json_failures_produce_source_unavailable_facts(tmp_path):
    routes = {
        "navigara.com/": response(status=503, doc_id=31),
        "type=MX": response(body="not-json", doc_id=32),
        "type=TXT": response(body={"Status": 0}, doc_id=33),
        "crt.sh": response(body="<html>error</html>", content_type="text/html", doc_id=34),
    }
    ctx = make_context(tmp_path, routes)
    facts = TechFingerprintCollector().collect(Company(id="n", name="N", domain="navigara.com"), ctx)

    unavailable = {f.key: f for f in facts if f.type == "source_unavailable"}
    assert {"techfp_website", "dns_mx", "crt_sh"} <= unavailable.keys()
    assert all(f.source_url and f.source_doc_id for f in unavailable.values())
