"""One subsidised project = one grant: Czech registers list the same project several times with different meanings."""
from dd.collectors.public_money import _matching_subsidy, merge_projects, parse_subsidies_api, reconcile_award


def _api(*records):
    return parse_subsidies_api({"results": [{"hints": {"isOriginal": True}, "recipient": {"name": "X"}, **r}
                                            for r in records]})


def test_award_and_payments_of_one_project_are_not_added_up():
    # Fly4Future, FW10010379: IS VaVaI states the award, IsRed the payments by year (live shapes, trimmed)
    rows = _api({"id": "IsVavai-1", "primaryDataSource": "IsVavai", "projectCode": "FW10010379", "approvedYear": 2024,
                 "projectName": "Letecká platforma pro autonomní inspekce v členitém indoor prostředí",
                 "subsidyAmount": 14507600.0, "payedAmount": None},
                {"id": "IsRed-1", "primaryDataSource": "IsRed", "projectCode": "Z771201000576", "approvedYear": 2025,
                 "projectName": "Letecká platforma pro autonomní inspekce v členitém indoor prostředí",
                 "subsidyAmount": 7725400.0, "payedAmount": 15542600.0,
                 "cerpani": [{"year": 2024, "amount": 7817200.0}, {"year": 2025, "amount": 7725400.0}]})
    out = merge_projects(rows)
    assert len(out) == 1
    p = out[0]
    assert p["awarded_czk"] == 14_507_600 and p["paid_czk"] == 15_542_600
    assert [y["year"] for y in p["paid_by_year"]] == [2024, 2025]
    assert p["also_listed_as"][0]["dataset"] == "IsRed"


def test_eu_fund_year_is_not_a_payment_year():
    rows = _api({"id": "Eufondy-1", "primaryDataSource": "Eufondy", "approvedYear": 2028,
                 "projectCode": "CZ.01.01.01/01/24_063/0006766", "projectName": "Létající robot",
                 "subsidyAmount": 35982614.29, "payedAmount": 35982614.29})
    p = merge_projects(rows)[0]
    assert p["awarded_czk"] == 35_982_614 and p["paid_czk"] is None and p["paid_by_year"] == []


def test_repeated_aid_in_one_register_stays_separate():
    rows = _api({"id": "DeMinimis-1", "primaryDataSource": "DeMinimis", "approvedYear": 2021,
                 "projectName": "Podpora v rámci projektu PSC II – inkubátor Startup centra", "payedAmount": 56714.0},
                {"id": "DeMinimis-2", "primaryDataSource": "DeMinimis", "approvedYear": 2022,
                 "projectName": "Podpora v rámci projektu PSC II – inkubátor Startup centra", "payedAmount": 144684.0})
    assert len(merge_projects(rows)) == 2


def test_short_generic_title_needs_same_amount():
    rows = _api({"id": "Eufondy-2", "primaryDataSource": "Eufondy", "approvedYear": 2024,
                 "projectCode": "CZ.01.01.01/05/24_042/0004834", "projectName": "Registrace ochranné známky",
                 "subsidyAmount": 187500.0},
                {"id": "IsRed-2", "primaryDataSource": "IsRed", "approvedYear": 2025, "projectCode": "Z220402001983",
                 "projectName": "Registrace ochranné známky", "subsidyAmount": 50550.0, "payedAmount": 50550.0})
    assert len(merge_projects(rows)) == 2


def test_de_minimis_record_joins_eu_project_by_code_in_title():
    rows = _api({"id": "Eufondy-3", "primaryDataSource": "Eufondy", "projectCode": "CZ.01.02.01/04/24_044/0005114",
                 "projectName": "Posílení mezinárodní pozice", "subsidyAmount": 984927.62, "approvedYear": 2027},
                {"id": "DeMinimis-3", "primaryDataSource": "DeMinimis",
                 "projectName": "CZ.01.02.01/04/24_044/0005114 - Posílení mezinárodní pozice a globální expanze",
                 "payedAmount": 279824.72, "approvedYear": 2025})
    out = merge_projects(rows)
    assert len(out) == 1 and out[0]["awarded_czk"] == 984_928


def test_support_agreement_matches_its_programme_and_sets_the_award():
    projects = merge_projects(_api(
        {"id": "IsVavai-4", "primaryDataSource": "IsVavai", "projectCode": "TQ03000786", "approvedYear": 2024,
         "projectName": "Rozhraní pro intuitivní a spolehlivou obsluhu heterogenní skupiny robotů",
         "subsidyAmount": 3350000.0},
        {"id": "IsRed-5", "primaryDataSource": "IsRed", "projectCode": "Z771301000301", "approvedYear": 2025,
         "projectName": "Udržitelné zemědělství: Energeticky výkonné bezpilotní technologie",
         "subsidyAmount": 4907700.0, "payedAmount": 4907700.0}))
    agreement = {"signed": "2024-02-05", "amount_czk": 4879000, "subject": "Smlouva o poskytnutí podpory Sigma DC2 (TQ03)"}
    match = _matching_subsidy(agreement, projects)
    assert match["project_code"] == "TQ03000786"  # by programme code, not by the nearest amount
    match.setdefault("agreements", []).append(agreement)
    reconcile_award(match)
    assert match["amount_czk"] == 4_879_000 and match["register_award_czk"] == 3_350_000
    assert match["awarded_from"].startswith("support agreement")
