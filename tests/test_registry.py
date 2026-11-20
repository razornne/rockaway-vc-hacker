"""Registry collector + resolver: offline unit tests on inline fixtures, plus network golden checks."""
from __future__ import annotations

import logging
from pathlib import Path

import pytest

from dd.collectors.base import Context
from dd.collectors.registry import (RegistryCollector, parse_capital, parse_filings, parse_fraction,
                                    parse_isir_count, parse_officer_changes, parse_shareholders, parse_subjekt_id,
                                    structural_flags)
from dd.config import Settings
from dd.http import Http
from dd.resolver import ico_valid, looks_like_domain, normalize_ico, resolve
from dd.store import Company, Store

# --- inline fixtures mirroring the real ARES VR structure -----------------------------------
VR_SRO = {
    "zakladniKapital": [
        {"datumZapisu": "2026-08-24", "vklad": {"typObnos": "KORUNY", "hodnota": "14384"}},
        {"datumZapisu": "2022-01-10", "datumVymazu": "2026-08-24", "vklad": {"typObnos": "KORUNY", "hodnota": "10000"}},
    ],
    "statutarniOrgany": [{"nazevOrganu": "Statutární orgán", "clenoveOrganu": [
        {"datumZapisu": "2022-01-10", "clenstvi": {"funkce": {"vznikFunkce": "2022-01-10", "nazev": "jednatel"}},
         "fyzickaOsoba": {"jmeno": "SECRET", "prijmeni": "PERSON", "datumNarozeni": "1980-01-01",
                          "adresa": {"textovaAdresa": "Private street 1"}}},
        {"datumZapisu": "2022-01-10", "datumVymazu": "2024-02-23",
         "clenstvi": {"funkce": {"vznikFunkce": "2022-01-10", "zanikFunkce": "2024-01-31", "nazev": "jednatel"}},
         "fyzickaOsoba": {"jmeno": "X", "prijmeni": "Y"}},
    ]}],
    "spolecnici": [{"spolecnik": [
        {"osoba": {"datumZapisu": "2022-01-10", "fyzickaOsoba": {"jmeno": "NATURAL", "prijmeni": "HOLDER"}},
         "podil": [{"velikostPodilu": {"typObnos": "PROCENTA", "hodnota": "100"}}]},
        {"osoba": {"datumZapisu": "2026-08-24",
                   "pravnickaOsoba": {"obchodniJmeno": "Rockaway Ventures Fund SCSp",
                                      "adresa": {"kodStatu": "LU"}}},
         "podil": [{"datumZapisu": "2026-08-24", "velikostPodilu": {"typObnos": "ZLOMEK", "hodnota": "554;14384"}}]},
        {"osoba": {"datumZapisu": "2026-08-24",
                   "pravnickaOsoba": {"obchodniJmeno": "Presto Ventures II a.s.", "ico": "11678704",
                                      "adresa": {"kodStatu": "CZ"}}},
         "podil": [{"datumZapisu": "2026-08-24", "velikostPodilu": {"typObnos": "ZLOMEK", "hodnota": "1106;14384"}}]},
    ]}],
}

VR_SOLE_FOREIGN = {"spolecnici": [{"spolecnik": [
    {"osoba": {"datumZapisu": "2022-10-20", "pravnickaOsoba": {"obchodniJmeno": "Filuta AI Inc."}},
     "podil": [{"datumZapisu": "2022-10-20", "velikostPodilu": {"typObnos": "PROCENTA", "hodnota": "100"}}]},
    {"osoba": {"datumZapisu": "2020-12-11", "datumVymazu": "2022-10-20",
               "fyzickaOsoba": {"jmeno": "A", "prijmeni": "B"}},
     "podil": [{"datumZapisu": "2020-12-11", "datumVymazu": "2022-10-20",
                "velikostPodilu": {"typObnos": "PROCENTA", "hodnota": "100"}}]},
]}]}

FILINGS_HTML = """<table class="list"><tbody>
<tr><td><a href="./vypis-sl-detail?dokument=1&amp;subjektId=7&amp;spis=2"><span>C&nbsp;1/SL10/MSPH</span></a></td>
<td><span><span class="symbol">účetní závěrka [2025]</span></span> <span> - předána</span></td>
<td>12.4.2026</td><td>12.4.2026</td><td>16.4.2026</td><td class="center"></td><td></td></tr>
<tr><td><a href="./vypis-sl-detail?dokument=2&amp;subjektId=7&amp;spis=2"><span>C&nbsp;1/SL5/MSPH</span></a></td>
<td><span><span class="symbol">notářský zápis [NZ 315/2023, N 298/2023]</span></span></td>
<td>14.3.2023</td><td></td><td>14.3.2023</td><td class="center">5</td><td></td></tr>
</tbody></table>"""


def test_parse_fraction():
    assert parse_fraction({"typObnos": "PROCENTA", "hodnota": "12;30"}) == pytest.approx(12.30)
    assert parse_fraction({"typObnos": "ZLOMEK", "hodnota": "1;4"}) == pytest.approx(25.0)
    assert parse_fraction({"typObnos": "ZLOMEK", "hodnota": "1;0"}) is None


def test_shareholders_legal_entities_only():
    hs = parse_shareholders(VR_SRO)
    assert [h["name"] for h in hs] == ["Presto Ventures II a.s.", "Rockaway Ventures Fund SCSp"]
    assert all(h["from"] == "2026-08-24" and h["to"] is None for h in hs)
    rv = next(h for h in hs if h["name"].startswith("Rockaway"))
    assert rv["country"] == "LU" and rv["foreign"] is True and rv["share_pct"] == pytest.approx(3.85, abs=0.01)
    assert "NATURAL" not in repr(hs)


def test_capital_history():
    cap = parse_capital(VR_SRO)
    assert [(c["amount_czk"], c["from"], c["to"]) for c in cap] == [
        (10000, "2022-01-10", "2026-08-24"), (14384, "2026-08-24", None)]


def test_officer_changes_have_no_personal_data():
    ch = parse_officer_changes(VR_SRO)
    assert len(ch) == 2 and {c["role"] for c in ch} == {"jednatel"}
    assert ch[1]["to"] == "2024-01-31"
    blob = repr(ch)
    for secret in ("SECRET", "PERSON", "1980", "Private"):
        assert secret not in blob


def test_foreign_holding_flag_sole_holder():
    hs = parse_shareholders(VR_SOLE_FOREIGN)
    assert len(hs) == 1 and hs[0]["country"] is None and hs[0]["foreign"] is True  # inferred from "Inc."
    assert "foreign_holding" in structural_flags(hs, "112")


def test_no_foreign_flag_for_minority_fund_and_as_flag():
    flags = structural_flags(parse_shareholders(VR_SRO), "112")
    assert "foreign_holding" not in flags and "legal_form_as" not in flags
    assert "legal_form_as" in structural_flags([], "932")
    assert "legal_form_as" in structural_flags([], "121")


def test_unknown_share_does_not_imply_foreign_control():
    # Natural persons have been filtered out: one remaining legal entity proves no majority.
    holders = [{"name": "Foreign Inc.", "country": "US", "foreign": True,
                "share_pct": None, "from": "2020-01-01", "to": None}]
    assert "foreign_holding" not in structural_flags(holders, "112")


@pytest.mark.parametrize("route", ["ekonomicke-subjekty/", "ekonomicke-subjekty-vr/"])
def test_malformed_ares_response_preserves_other_sources(tmp_path, route):
    http = FakeHttp({route: FakeResp(content=b"[]")})
    facts = RegistryCollector().collect(Company(id="x", name="X", ico="09745424"), _ctx(tmp_path, http))
    assert any(f.type == "source_unavailable" and "invalid JSON" in f.value["reason"] for f in facts)


def test_filings_parser():
    docs = parse_filings(FILINGS_HTML, "https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=7")
    assert len(docs) == 2
    assert docs[0]["doc_type"] == "účetní závěrka" and docs[0]["period"] == "2025" and docs[0]["filed"] == "2026-04-16"
    assert docs[0]["url"].startswith("https://or.justice.cz/ias/ui/vypis-sl-detail?dokument=1")
    assert docs[1]["period"] is None and docs[1]["reference"].startswith("NZ 315/2023")


def test_small_parsers():
    assert parse_subjekt_id('<a href="./rejstrik-firma.vysledky?subjektId=1103788&amp;typ=UPLNY">') == "1103788"
    assert parse_isir_count("<td>POČET NALEZENÝCH DLUŽNÍKŮ</td> <b>0</b>") == 0
    assert parse_isir_count("nothing") is None


def test_resolver_helpers():
    assert ico_valid("09745424") and ico_valid("14134683") and not ico_valid("12345678")
    assert normalize_ico("097 45 424") == "09745424" and normalize_ico("9745424") == "09745424"
    assert looks_like_domain("filuta.ai") and looks_like_domain("https://www.valka.ai/") and not looks_like_domain("Filuta AI")


# --- offline collector run against a fake HTTP layer ---------------------------------------
class FakeResp:
    def __init__(self, status=200, content=b"{}", ctype="application/json"):
        self.status, self.content, self.content_type, self.doc_id = status, content, ctype, None

    @property
    def ok(self):
        return 200 <= self.status < 300

    @property
    def text(self):
        return self.content.decode("utf-8")

    def json(self):
        import json
        return json.loads(self.content)


class FakeHttp:
    def __init__(self, routes):
        self.routes = routes

    def get(self, url, **kw):
        for frag, resp in self.routes.items():
            if frag in url:
                return resp
        return FakeResp(404, b"")


def _ctx(tmp_path, http) -> Context:
    return Context(settings=Settings(), store=Store(tmp_path / "t.sqlite"), http=http, log=logging.getLogger("t"))


def test_collector_offline(tmp_path: Path):
    import json
    basic = {"ico": "14134683", "obchodniJmeno": "CRUXO group s.r.o.", "pravniForma": "112", "datumVzniku": "2022-01-10",
             "sidlo": {"nazevObce": "Praha", "kodStatu": "CZ"}, "czNace2008": ["620"]}
    http = FakeHttp({
        "ekonomicke-subjekty-vr/": FakeResp(content=json.dumps({"zaznamy": [{"rejstrik": "OR", "primarniZaznam": True, **VR_SRO}]}).encode()),
        "ekonomicke-subjekty/": FakeResp(content=json.dumps(basic).encode()),
        "rejstrik-$firma": FakeResp(content=b'<a href="./vypis-sl-firma?subjektId=7">', ctype="text/html"),
        "vypis-sl-firma": FakeResp(content=FILINGS_HTML.encode(), ctype="text/html"),
        "isir.justice.cz": FakeResp(content="POČET NALEZENÝCH DLUŽNÍKŮ 0".encode(), ctype="text/html"),
    })
    c = Company(id="cruxo", name="Cruxo", ico="14134683")
    facts = RegistryCollector().collect(c, _ctx(tmp_path, http))
    types = [f.type for f in facts]
    assert {"identity", "registry_incorporation", "registry_shareholder", "registry_capital",
            "registry_officer_change", "filing", "insolvency"} <= set(types)
    assert all(f.source_url and f.extractor == "registry" for f in facts)
    # the offline fixture has no accounts PDF to download: only that source may be reported unavailable
    assert {f.key for f in facts if f.type == "source_unavailable"} <= {"annual_accounts"}


def test_collector_network_failure_returns_unavailable(tmp_path: Path):
    http = FakeHttp({"": FakeResp(0, b"boom", "error")})
    facts = RegistryCollector().collect(Company(id="x", name="X", ico="09745424"), _ctx(tmp_path, http))
    assert facts and all(f.type == "source_unavailable" for f in facts)


def test_malformed_vr_section_keeps_identity(tmp_path):
    import json
    http = FakeHttp({
        "ekonomicke-subjekty-vr/": FakeResp(content=b'{"zaznamy": ["invalid"]}'),
        "ekonomicke-subjekty/": FakeResp(content=json.dumps({"ico": "09745424", "obchodniJmeno": "Filuta"}).encode()),
    })
    facts = RegistryCollector().collect(Company(id="filuta", name="Filuta", ico="09745424"), _ctx(tmp_path, http))
    assert any(f.type == "identity" for f in facts)
    assert any(f.type == "source_unavailable" and f.key == "ares_vr" for f in facts)


def test_no_ico_no_domain_gives_flag(tmp_path: Path):
    facts = RegistryCollector().collect(Company(id="x", name="X"), _ctx(tmp_path, FakeHttp({})))
    assert [(f.type, f.key) for f in facts] == [("registry_flag", "no_cz_entity")]


# --- network golden checks (eval/golden.json) ---------------------------------------------
@pytest.fixture(scope="module")
def live_ctx(tmp_path_factory):
    d = tmp_path_factory.mktemp("live")
    store = Store(d / "t.sqlite")
    return Context(settings=Settings(), store=store, http=Http(d / "cache", store=store), log=logging.getLogger("t"))


def _collect(live_ctx, cid, name, ico, domain=None):
    c = Company(id=cid, name=name, ico=ico, domain=domain)
    live_ctx.store.upsert_company(c)
    return RegistryCollector().collect(c, live_ctx)


def _holder(facts, contains):
    return [f for f in facts if f.type == "registry_shareholder" and contains in f.value["name"]]


@pytest.mark.network
def test_golden_campiri(live_ctx):
    facts = _collect(live_ctx, "campiri", "Campiri", "09283447")
    assert any(h.value["from"] == "2022-05-04" for h in _holder(facts, "Rockaway Ventures Fund"))
    assert any(h.value["from"] == "2022-05-04" for h in _holder(facts, "MITON Happy Campers"))


@pytest.mark.network
def test_golden_cruxo(live_ctx):
    facts = _collect(live_ctx, "cruxo", "Cruxo", "14134683")
    for n in ("Rockaway Ventures Fund", "Czech Founders Ventures", "Presto Ventures II"):
        assert any(h.value["from"] == "2026-08-24" for h in _holder(facts, n)), n
    assert any(f.type == "registry_capital" and f.value["amount_czk"] == 14384 and f.value["from"] == "2026-08-24"
               for f in facts)
    assert any(f.type == "filing" for f in facts)


@pytest.mark.network
def test_golden_filuta(live_ctx):
    facts = _collect(live_ctx, "filuta", "Filuta AI", "09745424")
    assert any(h.value["from"] == "2022-10-20" for h in _holder(facts, "Filuta AI Inc"))
    assert any(f.type == "registry_flag" and f.key == "foreign_holding" for f in facts)


@pytest.mark.network
def test_golden_valkaai(live_ctx):
    facts = _collect(live_ctx, "valkaai", "ValkaAI", "23132221")
    assert any(h.value["from"] == "2025-04-01" for h in _holder(facts, "Valka.AI B.V"))
    assert any(f.type == "registry_flag" and f.key == "foreign_holding" for f in facts)


@pytest.mark.network
def test_resolver_live(live_ctx):
    c = resolve("09745424", live_ctx)
    assert len(c) == 1 and "Filuta" in c[0].name and c[0].legal_form == "s.r.o."
    names = resolve("Campiri", live_ctx)
    assert any(x.ico == "09283447" for x in names)
