"""Defence / dual-use sources: TED procurement, EU Funding & Tenders portal, NATO DIANA cohorts."""
from __future__ import annotations

import json

from dd.collectors.diana import DianaCollector, parse_cohort, peers
from dd.collectors.eu_funding import matches, parse_org
from dd.collectors.procurement import parse_notices
from dd.store import Company

DRONETAG = Company(id="dronetag", name="Dronetag", domain="dronetag.com", ico="08198519")
F4F = Company(id="fly4future", name="Fly4Future", domain="fly4future.com", ico="06632581")


# --- TED -------------------------------------------------------------------------------------------------------
def test_ted_winner_by_ico_and_defence_buyer():
    data = {"notices": [
        {"publication-number": "436033-2026", "notice-type": "can-standard", "publication-date": "2026-06-25+02:00",
         "contract-conclusion-date": ["2026-06-23+02:00"], "buyer-name": {"ces": ["Ministerstvo obrany"]},
         "buyer-country": ["CZE"], "winner-identifier": ["08198519"], "winner-name": {"ces": ["Dronetag s.r.o."]},
         "total-value": 27440000, "total-value-cur": ["CZK"], "classification-cpv": ["64216000"],
         "notice-title": {"eng": "Czechia – Electronic message and information services – Detekce UAS"}},
        {"publication-number": "271589-2023", "notice-type": "can-standard", "publication-date": "2023-05-08+02:00",
         "buyer-name": {"ces": ["Vysoké učení technické v Brně"]}, "total-value": 544487,
         "notice-title": {"eng": "Czechia-Brno: Industrial machinery"}},
    ]}
    won, mentioned = parse_notices(data, DRONETAG)
    assert won.value["role"] == "winner" and won.value["defence_buyer"] and won.value["value"] == 27440000
    assert won.event_date == "2026-06-23" and won.confidence == "high"
    assert mentioned.value["role"] == "mentioned" and mentioned.confidence == "medium"
    assert mentioned.value["value"] is None  # a notice that only mentions us is not our revenue
    assert not mentioned.value["defence_buyer"]


def test_ted_winner_by_name_and_cpv_35_is_defence():
    data = {"notices": [{"publication-number": "1-2025", "winner-name": ["FLY4FUTURE S.R.O."],
                         "buyer-name": ["Some agency"], "classification-cpv": ["35613000"]}]}
    (f,) = parse_notices(data, F4F)
    assert f.value["role"] == "winner" and f.value["defence_buyer"]


# --- EU Funding & Tenders portal ------------------------------------------------------------------------------
ORG = {"esIN_name": ["FLY4FUTURE S.R.O."], "esIN_pic": ["887136005"], "esIN_registrationNum": ["06632581"],
       "esST_vat": ["CZ06632581"], "esNU_noOfProjects": ["2"], "esST_validationStatus": ["31042522"],
       "esDA_FirstIngestDate": ["2024-12-06T07:20:02.087+0100"],
       "esBI_publicProjects": [json.dumps([
           {"program": {"abbreviation": "HORIZON", "description": "Horizon Europe (HORIZON)"}, "number": "101071270",
            "acronym": "AeroSTREAM", "title": "Autonomous Aerial Systems", "call": {"abbreviation": "WIDERA"},
            "status": "Signed"},
           {"program": {"abbreviation": "EDF", "description": "European Defence Fund (EDF)"}, "number": "101121418",
            "acronym": "SWARM-X", "title": "Swarms", "status": "Signed"}])]}


def test_eu_org_matched_by_ico_not_name():
    assert matches(ORG, F4F)
    other = Company(id="x", name="Fly4Future", ico="12345678")
    assert not matches(ORG, other)  # same name, different IČO
    assert matches(ORG, Company(id="y", name="Fly4Future s.r.o."))  # no IČO known: exact core name


def test_eu_projects_flag_defence_fund():
    facts = parse_org(ORG, F4F)
    reg = facts[0]
    assert reg.type == "eu_registration" and reg.value["validated"] and reg.value["projects"] == 2
    grants = {f.key: f.value for f in facts if f.type == "grant_eu"}
    assert not grants["101071270"]["defence"] and grants["101121418"]["defence"]
    assert all("org-details/887136005" in f.source_url for f in facts)


# --- NATO DIANA ------------------------------------------------------------------------------------------------
HTML_2024 = """<div id="isw"><div class="display center"><h1>SECURE INFORMATION SHARING</h1></div>
<div class="mdl-grid"><div class="center mdl-cell mdl-cell--3-col"><div class="display">
<a href="https://dronetag.cz/">DRONETAG</a></div></div></div></div>"""
HTML_2025 = """<div id="isw"><div class="mdl-grid"><div class="mdl-cell mdl-cell--12-col"><h1>2025 Cohort of Companies</h1></div>
<div class="mdl-cell mdl-cell--12-col center"><img src="../uploads/cohort-energy-9aneq1.png"></div>
<div class="mdl-cell mdl-cell--3-col center"><a href="https://www.iplventures.com/">Atomiver S.R.O</a></div></div></div>"""
HTML_2026 = """<div id="isw"><div class="category-box-1 mdl-grid">
<div class="mdl-cell mdl-cell--12-col category-header"><div class="logo-text">Autonomy &amp; Unmanned Systems</div></div>
<div class="mdl-cell mdl-cell--4-col cohort-card"><h4><a href="https://www.alpha-autonomy.com">Alpha Autonomy</a></h4>
<p>AI-powered autonomous UAV swarms for resilient, low-altitude ISR in denied environments</p><p>Greece</p></div>
<div class="mdl-cell mdl-cell--4-col cohort-card"><h4><a href="http://www.delian.ai">Delian Alliance Industries</a></h4>
<p>Low-cost, highly accurate GPS-denied navigation for any UAV</p><p>United Kingdom</p></div>
<div class="mdl-cell mdl-cell--4-col cohort-card"><h4><a href="https://e-peas.com">e-peas</a></h4>
<p>Providing ICs for energy autonomous sensors and infrastructure monitoring</p><p>Belgium</p></div>
</div></div>"""


def test_three_cohort_layouts():
    (d,) = parse_cohort(HTML_2024, 2024)
    assert d["name"] == "DRONETAG" and d["area"] == "Secure Information Sharing" and d["url"] == "https://dronetag.cz/"
    (a,) = parse_cohort(HTML_2025, 2025)
    assert a["name"] == "Atomiver S.R.O" and a["area"] == "Energy"
    c = parse_cohort(HTML_2026, 2026)
    assert [x["name"] for x in c] == ["Alpha Autonomy", "Delian Alliance Industries", "e-peas"]
    assert c[0]["area"] == "Autonomy & Unmanned Systems" and c[0]["country"] == "Greece"


def test_peers_use_distinctive_terms_and_synonyms():
    entries = parse_cohort(HTML_2026, 2026)
    site = ("Our autonomous drones fly in swarms. Drone swarm research. UAV swarms for inspection. " * 5
            + "We also monitor energy use. ")
    names = [p["name"] for p in peers(entries, site, "fly4future")]
    assert names[0] == "Alpha Autonomy"  # 'UAV swarms' == 'drones … swarms' after synonyms
    assert names[-1] == "e-peas"  # shares one generic term only: ranked last


class _Resp:
    def __init__(self, status, text="", url="https://web.archive.org/x"):
        self.status, self.text, self.url = status, text, url

    @property
    def ok(self):
        return 200 <= self.status < 300


class _Http:
    def __init__(self, pages):
        self.pages = pages

    def get(self, url, **kw):
        for year, html in self.pages.items():
            if f"{year}-cohort" in url:
                return html if isinstance(html, _Resp) else _Resp(200, html, url)
        return _Resp(404)


class _Store:
    def source_docs(self, cid):
        return []


class _Ctx:
    def __init__(self, pages):
        self.http, self.store = _Http(pages), _Store()


def test_membership_found_by_domain(monkeypatch):
    monkeypatch.setattr("dd.collectors.diana.RETRY_WAIT", 0)
    facts = DianaCollector().collect(DRONETAG, _Ctx({2024: HTML_2024, 2026: HTML_2026}))
    acc = [f for f in facts if f.type == "accelerator"]
    assert len(acc) == 1 and acc[0].value["year"] == 2024 and acc[0].value["programme"] == "NATO DIANA"


def test_unreadable_year_is_not_absence(monkeypatch):
    monkeypatch.setattr("dd.collectors.diana.RETRY_WAIT", 0)
    facts = DianaCollector().collect(F4F, _Ctx({2024: HTML_2024, 2025: _Resp(429), 2026: HTML_2026}))
    assert not any(f.type == "accelerator" for f in facts)
    check = next(f for f in facts if f.type == "source_check")
    assert check.value == {"source": "NATO DIANA cohorts", "status": "not_listed_in_checked_years", "years_checked": [2024, 2026]}
    gap = next(f for f in facts if f.type == "source_unavailable")
    assert "2025: HTTP 429" in gap.value["reason"]


def test_after_rate_limit_later_years_are_tried_once(monkeypatch):
    monkeypatch.setattr("dd.collectors.diana.RETRY_WAIT", 0)
    calls = []
    ctx = _Ctx({2024: _Resp(429), 2026: HTML_2026})
    orig = ctx.http.get
    ctx.http.get = lambda url, **kw: calls.append(url) or orig(url, **kw)
    facts = DianaCollector().collect(DRONETAG, ctx)
    assert sum("2024-cohort" in c for c in calls) == 3 and sum("2026-cohort" in c for c in calls) == 1
    assert any(f.type == "peer_company" or f.type == "source_check" for f in facts)


def test_all_years_unreadable_gives_no_data(monkeypatch):
    monkeypatch.setattr("dd.collectors.diana.RETRY_WAIT", 0)
    facts = DianaCollector().collect(F4F, _Ctx({2023: _Resp(429), 2024: _Resp(429), 2025: _Resp(429), 2026: _Resp(429)}))
    assert [f.type for f in facts] == ["source_unavailable"]


# --- public money: amounts and contract kinds ------------------------------------------------------------------
def test_api_amount_with_vat_decimals_is_not_inflated():
    from dd.collectors.public_money import _czk
    assert _czk(1351788.1146) == 1351788       # number from the API
    assert _czk("1351788.1146") == 1351788     # same value as text: was parsed as 13.5 bn
    assert _czk("1 117 180,26 Kč") == 1117180
    assert _czk("1.234.567") == 1234567 and _czk("36 790 550") == 36790550


def test_contract_kinds_separate_sales_from_research_budgets():
    from dd.signals import contract_kind
    from dd.store import Fact
    k = lambda subj: contract_kind(Fact(company_id="x", type="gov_contract", value={"subject": subj}, source_url="u"))
    assert k("Kupní smlouva - detekční zařízení") == "purchase"
    assert k("objednávka: nákup 1 ks zařízení pro dálkovou identifikaci dronů") == "purchase"
    assert k("Smlouva o účasti na řešení projektu CK03000054 a využití výsledků") == "rd_project"
    assert k("Projekt FW12010288: Multi-robotický letecký systém") == "rd_project"
    assert k("Smlouva o poskytnutí zvýhodněných služeb CzechStarter - mentoring") == "subsidy"
    assert k("Smlouva o výpůjčce - 1 x Dronetag Scout") == "loan"
