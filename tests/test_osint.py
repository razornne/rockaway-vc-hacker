"""OSINT checks: parsing, matching, wording. No network: every source is a small synthetic sample."""
import gzip

from dd.osint import checks, claims, hiring, people, view
from dd.store import Company, Fact

CO = Company(id="x", name="Acme s.r.o.", domain="acme.cz", ico="12345678")

VR = {"zaznamy": [{"primarniZaznam": True, "statutarniOrgany": [{"nazevOrganu": "Statutární orgán", "clenoveOrganu": [
    {"datumZapisu": "2018-01-01", "nazevAngazma": "Jednatel", "clenstvi": {"funkce": {"nazev": "jednatel",
                                                                                     "vznikFunkce": "2018-01-01"}},
     "fyzickaOsoba": {"jmeno": "Jana", "prijmeni": "NOVÁKOVÁ", "datumNarozeni": "1980-05-01",
                      "adresa": {"textovaAdresa": "secret street 1"}}}]}],
    "spolecnici": [{"nazevOrganu": "Společníci", "spolecnik": [
        {"datumZapisu": "2018-01-01", "podil": [{"velikostPodilu": {"typObnos": "PROCENTA", "hodnota": "60"}}],
         "osoba": {"fyzickaOsoba": {"jmeno": "Petr", "prijmeni": "Svoboda", "datumNarozeni": "1975-02-03"}}}]}]}]}

DUMP = """<?xml version="1.0" encoding="UTF-8"?><xml><Subjekt><nazev>Other a.s.</nazev><ico>87654321</ico><udaje>
<Udaj><udajTyp><kod>STATUTARNI_ORGAN</kod></udajTyp><podudaje><Udaj><zapisDatum>2015-01-01</zapisDatum>
<funkce>předseda představenstva</funkce><funkceOd>2015-01-01</funkceOd><udajTyp><kod>STATUTARNI_ORGAN_CLEN</kod></udajTyp>
<osoba><jmeno>Jana</jmeno><prijmeni>Nováková</prijmeni><narozDatum>1980-05-01</narozDatum></osoba></Udaj>
<Udaj><zapisDatum>2015-01-01</zapisDatum><funkce>člen</funkce><udajTyp><kod>STATUTARNI_ORGAN_CLEN</kod></udajTyp>
<osoba><jmeno>Jana</jmeno><prijmeni>Nováková</prijmeni><narozDatum>1990-01-01</narozDatum></osoba></Udaj>
</podudaje></Udaj><Udaj><zapisDatum>2024-03-01</zapisDatum><udajTyp><kod>INSOLVENCE_SEKCE</kod></udajTyp></Udaj>
</udaje></Subjekt></xml>"""


def test_people_from_vr_keeps_names_and_roles_and_no_birth_date_in_facts(tmp_path):
    ps = people.people_from_vr(VR)
    assert [p.name for p in ps] == ["Jana Nováková", "Petr Svoboda"]
    assert ps[1].roles[0]["share_pct"] == 60
    f = tmp_path / "as-full-praha-2026.xml.gz"
    f.write_bytes(gzip.compress(DUMP.encode("utf-8")))
    roles = people.scan([f], {p.key for p in ps})
    jana = roles[ps[0].key]
    assert len(jana) == 1 and jana[0]["ico"] == "87654321"  # the namesake born in 1990 is not matched
    assert jana[0]["status"]["insolvency"] == "2024-03-01"
    facts = people.facts_for(CO, ps, roles, {}, [f])
    text = repr([x.value for x in facts]) + repr([x.key for x in facts])
    assert "1980" not in text and "1975" not in text and "secret street" not in text
    other = next(x for x in facts if x.type == "person_role_elsewhere")
    assert other.value["outcome"].startswith("insolvency register entries (2024)") and other.value["active"]


def test_merge_roles_joins_re_registered_entries():
    rows = [{"ico": "1", "kind": "STATUTARNI_ORGAN_CLEN", "role": "člen", "from": "2015-01-01", "to": "2016-01-01"},
            {"ico": "1", "kind": "STATUTARNI_ORGAN_CLEN", "role": "jednatel", "from": "2016-01-01", "to": None}]
    m = people.merge_roles(rows)
    assert len(m) == 1 and m[0]["from"] == "2015-01-01" and m[0]["to"] is None and m[0]["role"] == "jednatel"


def test_isir_answers():
    empty = ('<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:r xmlns:ns2="t">'
             "<stav><kodChyby>WS2</kodChyby></stav></ns2:r></soap:Body></soap:Envelope>")
    assert checks.parse_isir(empty) == {"count": 0, "proceedings": []}
    one = ('<e><data><druhVec>INS</druhVec><bcVec>12</bcVec><rocnik>2020</rocnik><druhStavKonkursu>KONKURS</druhStavKonkursu>'
           "<urlDetailRizeni>https://isir.justice.cz/x</urlDetailRizeni></data><stav><pocetVysledku>1</pocetVysledku></stav></e>")
    r = checks.parse_isir(one)
    assert r["count"] == 1 and r["proceedings"][0]["case"] == "INS 12/2020"
    assert checks.parse_isir("<html>error</html>") is None and checks.parse_isir("not xml") is None
    assert "<nazevOsoby>Nov&amp;ak</nazevOsoby>" in checks.isir_envelope(nazevOsoby="Nov&ak", jmeno=None)


def test_adis_answer_ignores_bank_accounts():
    xml = ('<x xmlns="http://adis.mfcr.cz/rozhraniCRPDPH/"><status statusCode="0"/><statusPlatceDPH dic="123" '
           'nespolehlivyPlatce="NE"><zverejneneUcty><ucet><standardniUcet cislo="1"/></ucet></zverejneneUcty>'
           "</statusPlatceDPH></x>")
    assert checks.parse_adis(xml) == {"123": {"unreliable": "NE", "since": None}}
    assert checks.parse_adis('<x><status statusCode="3"/></x>') is None


def test_sanctions_lists_parse_and_reject_error_pages():
    assert checks.load_eu("<!DOCTYPE html><title>Server temporarily unavailable</title>") is None
    cz = ('"Příjmení fyzické osoby/název","Jméno fyzické osoby ","Stav zápisu","Pozn","Datum narození"\n'
          '"GUNĎAJEV/GUNDYAYEV","Vladimir","platný",,20.11.1946\n')
    rows = checks.load_cz(cz)
    assert {"name": "vladimir gundajev", "birth": "1946-11-20", "type": "person", "active": True} in rows


def test_headcount_skips_plans_and_compares_with_personnel_costs():
    plan = Fact(company_id="x", type="team_claim", key="k", value={}, source_url="u",
                snippet="Cílem je vybudovat tým 60 až 100 lidí")
    now = Fact(id=7, company_id="x", type="team_claim", key="k", value={}, source_url="u",
               snippet="Dnes má kolem 40 zaměstnanců.")
    fin = {"period": "2025", "personnel_costs": 30_400_000, "fact_ids": [1], "source_url": "https://or.justice.cz"}
    assert claims.check_team_size(CO, [plan], fin) == []
    v = claims.check_team_size(CO, [plan, now], fin)[0].value
    assert v["claimed"] == 40 and v["status"] == "confirmed"
    big = Fact(id=8, company_id="x", type="team_claim", key="k", value={}, source_url="u", snippet="We have 200 engineers")
    assert claims.check_team_size(CO, [big], fin)[0].value["status"] == "contradicted"


def test_public_buyer_claim_without_records_is_a_question_not_a_denial():
    c = Fact(id=3, company_id="x", type="customer", key="k", value={"summary": "We supply the army"}, source_url="u")
    v = claims.check_public_buyers(CO, [c])[0].value
    assert v["status"] == "not_found" and "ask which public buyers" in v["detail"]


def test_view_flags_penalty_waivers_and_busy_founders():
    facts = [Fact(id=1, company_id="x", type="person", key="Jana", source_url="u",
                  value={"name": "Jana Nováková", "current": True, "roles_here": [{"role": "jednatel"}]}),
             *[Fact(id=10 + i, company_id="x", type="person_role_elsewhere", key=str(i), source_url="u",
                    value={"person": "Jana Nováková", "company": f"C{i}", "role": "jednatel", "active": True})
               for i in range(3)],
             Fact(id=20, company_id="x", type="grant_national", key="k", source_url="u",
                  value={"provider": "Česká správa sociálního zabezpečení",
                         "title": "Odstranění tvrdosti zákona prominutím penále"})]
    flags = view.summary(facts)["flags"]
    assert any("3 other active executive roles" in f for f in flags)
    assert any("waived a penalty" in f for f in flags)


def test_job_boards_found_from_company_links():
    f = Fact(company_id="x", type="web_page", key="careers", source_url="https://jobs.lever.co/acme/123", value={})
    assert hiring.boards([f]) == [("Lever", "https://api.lever.co/v0/postings/acme?mode=json")]
    jobs = hiring.parse_board("Greenhouse", '{"jobs":[{"title":"Account Executive","location":{"name":"Prague"}}]}')
    assert jobs[0]["title"] == "Account Executive" and hiring.bucket("Account Executive") == "sales_gtm"


def test_osint_facts_do_not_make_an_analysis_stale():
    from dd.analyze import fact_snapshot_sha256
    base = [Fact(id=1, company_id="x", type="identity", key="k", value={}, source_url="u", extractor="registry")]
    extra = Fact(id=2, company_id="x", type="person", key="p", value={}, source_url="u", extractor="osint_people")
    assert fact_snapshot_sha256("x", base) == fact_snapshot_sha256("x", base + [extra])


def test_isir_keeps_only_same_name_and_birth_date():
    rows = [{"_last": "Nováková", "_first": "Jana", "_birth": "1980-05-01", "case": "INS 1/2020"},
            {"_last": "NOVÁKOVÁ", "_first": "Jana", "_birth": "1985-01-01", "case": "INS 2/2020"},  # namesake
            {"_last": "Nováková", "_first": "Petra", "_birth": "1980-05-01", "case": "INS 3/2020"}]
    assert [r["case"] for r in checks.exact_matches(rows, "Jana", "Nováková", "1980-05-01")] == ["INS 1/2020"]


def test_dump_icos_get_their_leading_zeros_back(tmp_path):
    f = tmp_path / "sro-full-praha-2026.xml.gz"
    f.write_bytes(gzip.compress(DUMP.replace("<ico>87654321</ico>", "<ico>6632581</ico>").encode("utf-8")))
    key = people.person_key("Jana", "Nováková", "1980-05-01")
    assert people.scan([f], {key})[key][0]["ico"] == "06632581"


def test_trouble_counts_only_while_the_person_held_the_role():
    st = {"insolvency": "2012-05-01"}
    assert view.held_when_troubled({"from": "2010-01-01", "to": "2011-06-01", "status": st})  # left a year before
    assert not view.held_when_troubled({"from": "2014-01-01", "to": None, "status": st})  # joined after
    assert not view.held_when_troubled({"from": "2001-01-01", "to": "2005-01-01", "status": st})  # long before


def test_formation_agents_are_not_a_track_record():
    facts = [Fact(id=1, company_id="x", type="person", key="A", source_url="u",
                  value={"name": "Agent", "current": True, "roles_here": [{"role": "jednatel"}]})]
    facts += [Fact(id=100 + i, company_id="x", type="person_role_elsewhere", key=str(i), source_url="u",
                   value={"person": "Agent", "company": f"Shelf {i}", "role": "jednatel", "active": True,
                          "from": "2020-01-01", "to": None, "status": {"dissolution_proceedings": "2021-01-01"}})
              for i in range(45)]
    v = view.summary(facts)
    assert v["flags"] == [] and v["people"][0]["professional"]
