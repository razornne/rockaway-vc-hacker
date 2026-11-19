"""Defects found in the 14-company run (2026-11-17): name collisions, ATS vendor pages, cached outages."""
from __future__ import annotations

import json

from dd.collectors.press import about_company
from dd.collectors.web import ats_tenant
from dd.http import Http
from dd.store import Company
from dd.verify import assignee_matches

VERMEER = Company(id="vermeer", name="Vermeer", domain="getvermeer.com",
                  hints={"context_terms": ["drone", "gps denied", "visual navigation", "draper"]})
VALPAS = Company(id="valpas", name="Valpas", domain="valpashotels.com")
FILUTA = Company(id="filuta", name="Filuta AI", domain="filuta.ai")


def test_ats_vendor_site_is_not_the_company_board():
    assert ats_tenant("https://vermeer.homerun.co/", VERMEER)
    assert ats_tenant("https://vermeer.homerun.co/?lang=en", VERMEER)
    assert not ats_tenant("https://www.homerun.co/", VERMEER)
    assert not ats_tenant("https://jobs.homerun.co/?lang=en", VERMEER)
    assert not ats_tenant("https://www.homerun.co/pricing", VERMEER)
    valka = Company(id="valkaai", name="ValkaAI", domain="valka.ai")
    assert ats_tenant("https://jobs.lever.co/valka/123", valka)
    assert not ats_tenant("https://jobs.lever.co/", valka)


def test_ambiguous_name_needs_context():
    assert not about_company("Vermeer Corporation announces a new compact articulated loader.", VERMEER)
    assert not about_company("Vermeer is a London wealth manager with £2bn AUM.", VERMEER)
    assert about_company("Vermeer raises $10M for GPS denied drone navigation.", VERMEER)
    assert about_company("See getvermeer.com for details.", VERMEER)
    # names without the hint keep the plain rule
    assert about_company("Valpas raises funding for bed-bug-free hotel rooms.", VALPAS)


def test_patent_assignee_collision_guard():
    assert assignee_matches("Valpas Enterprises Oy", VALPAS, "valpas")
    assert not assignee_matches("Juha Valpas Viitanen", VALPAS, "valpas")
    assert not assignee_matches("V. P. VALPAS VALVOLE S.r.l.", VALPAS, "valpas")
    assert assignee_matches("Filuta AI Inc.", FILUTA, "filuta")
    assert not assignee_matches("Vermeer Manufacturing Company", VERMEER, "vermeer")
    legal = Company(id="vermeer", name="Vermeer", hints={**VERMEER.hints, "legal_names": ["Vermeer Inc."]})
    assert assignee_matches("Vermeer Inc", legal, "vermeer")


def test_cached_outage_is_fetched_again(tmp_path, monkeypatch):
    http = Http(tmp_path, min_delay=0)
    calls = []

    class R:
        def __init__(self, code):
            self.status_code, self.content, self.headers, self.url = code, b"x", {"content-type": "text/plain"}, "https://e.x/"

    codes = iter([503, 200, 999])
    monkeypatch.setattr(http.client, "request", lambda *a, **k: calls.append(1) or R(next(codes)))
    assert http.get("https://e.x/").status == 503
    assert http.get("https://e.x/").status == 200   # the 503 was not served from cache
    assert http.get("https://e.x/").status == 200   # a success is
    assert len(calls) == 2
    meta = next(tmp_path.rglob("*.json"))
    assert json.loads(meta.read_text())["status"] == 200


def test_round_reports_merge_when_investor_name_is_shortened():
    from dd.signals import _cluster_rounds
    rounds = [
        {"date": "2024-11-20", "round": "growth equity", "amount": None, "investors": ["PSG"], "fact_ids": [1]},
        {"date": "2024-11-21", "round": None, "amount": "€20m", "investors": ["PSG Equity", "Redalpine"], "fact_ids": [2]},
        {"date": "2023-04-26", "round": "Series A", "amount": "EUR 9 million", "investors": ["Serpentine"], "fact_ids": [3]},
    ]
    out = _cluster_rounds(rounds)
    assert len(out) == 2
    psg = next(c for c in out if c["date"] == "2024-11-20")
    assert psg["amount"] == "€20m" and psg["reports"] == 2 and "Redalpine" in psg["investors"]


def test_factual_sections_are_labelled_by_sources_not_model_flag():
    from dd import render
    from dd.store import Fact
    f = Fact(id=7, company_id="x", type="registry_shareholder", key="k", value={}, source_url="https://or.justice.cz/x",
             extractor="registry", confidence="high")
    comp = Company(id="x", name="X", domain="x.com")
    item = {"text": "Rockaway holds 3.85 %.", "fact_ids": [7], "assessment": True, "assumptions": [], "label": None}
    sections = [{"kind": "ownership", "no_data": False, "items": [item]},
                {"kind": "risk_flags", "no_data": False, "items": [dict(item)]}]
    prep = render.prepare(comp, {}, sections, {7: f}, [])
    own, risk = prep["sections"]
    assert own["items"][0]["strength"] == "verified"
    assert risk["items"][0]["strength"] == "view"


def test_company_is_not_its_own_customer():
    from dd.signals import customers
    from dd.store import Fact
    fs = [Fact(id=i, company_id="wultra", type="customer", key=n, value={"name": n}, source_url="https://wultra.com/x",
               extractor="llm_extract", confidence="medium") for i, n in ((1, "OTP Bank Moldova"), (2, "Wultra"))]
    assert customers(fs, "Wultra")["named_customers"] == ["OTP Bank Moldova"]


def test_unpriced_public_money_is_not_zero():
    from dd.writer import glance_rows
    sig = {"funding": {"public_money": {"contracts": 1, "contracts_czk": 0, "contracts_unpriced": 1, "grants": 0,
                                        "grants_czk": 0, "counterparties": ["Česká pošta, s.p."], "fact_ids": [1]}}}
    row = next(r for r in glance_rows(sig) if r[0] == "Public money")
    assert "0 CZK" not in row[1] and "amount not published" in row[1] and "Česká pošta" in row[1]


def test_antivirus_agreement_is_a_subsidy_not_a_contract():
    from dd.collectors.public_money import SUBSIDY_SUBJECT, _matching_subsidy
    subj = "DOHODA o poskytnutí příspěvku z cíleného programu Antivirus č. ABC-CO-9006482/2020"
    assert SUBSIDY_SUBJECT.search(subj)
    sub = {"title": "ANTIVIRUS", "year": "2021", "amount_czk": None}
    assert _matching_subsidy({"subject": subj, "signed": "2020-04-19", "amount_czk": 0}, [sub]) is sub
    assert not SUBSIDY_SUBJECT.search("Smlouva o budoucí spolupráci")


def test_undated_report_without_investors_merges_on_stage_and_amount():
    from dd.signals import _cluster_rounds
    rounds = [{"date": "2025-10-23", "round": "Series A", "amount": "$10 million", "investors": ["Draper Associates"], "fact_ids": [1]},
              {"date": None, "round": "Series A", "amount": "10M", "investors": [], "fact_ids": [2]}]
    out = _cluster_rounds(rounds)
    assert len(out) == 1 and out[0]["reports"] == 2
