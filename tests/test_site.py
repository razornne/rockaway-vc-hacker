"""Key-number tiles must not claim 'None found' for a source that was never read, and the showcase site builds."""
from dd import page
from dd.render import Refs
from dd.store import Company, Fact

CO = Company(id="x", name="X", domain="x.com")


def _facts(*fs: Fact) -> dict[int, Fact]:
    for i, f in enumerate(fs, start=1):
        f.id = i
    return {f.id: f for f in fs}


def _tiles(sig, facts):
    return {t["label"]: t for t in page.extras(sig, facts, Refs(facts), CO)["tiles"]}


def test_public_money_not_checked_without_ico():
    facts = _facts(Fact(company_id="x", type="source_unavailable", key="hlidac_statu", source_url="https://hlidacstatu.cz",
                        value={"reason": "no Czech IČO known for this company"}, extractor="public_money"))
    t = _tiles({}, facts)
    assert t["Sales to public buyers"]["value"] == "Not checked"
    assert "no Czech IČO" in t["Sales to public buyers"]["sub"]
    assert t["Grants & subsidies awarded (not revenue)"]["value"] == "Not checked"
    assert t["Defence evidence (official sources)"]["value"] == "Not checked"


def test_public_money_checked_and_empty_is_not_visible_never_none():
    # an empty register is "not visible", with what the register cannot show: never "None found"
    facts = _facts(Fact(company_id="x", type="source_check", key="hlidac_contracts_empty", source_url="https://hlidacstatu.cz",
                        value={"status": "empty"}, extractor="public_money"))
    t = _tiles({}, facts)
    assert t["Sales to public buyers"]["value"] == page.NOT_VISIBLE
    assert "EU tenders not checked" in t["Sales to public buyers"]["sub"]
    assert "not published" in t["Sales to public buyers"]["sub"]
    assert t["Grants & subsidies awarded (not revenue)"]["value"] == page.NOT_VISIBLE
    assert t["Funding rounds"]["value"] == "None reported"
    assert all(x["value"] != "None found" for x in t.values())


def test_defence_tile_empty_says_where_read_and_what_it_cannot_show():
    facts = _facts(Fact(company_id="x", type="source_check", key="ted", source_url="https://ted.europa.eu",
                        value={"status": "empty"}, extractor="procurement"))
    d = _tiles({}, facts)["Defence evidence (official sources)"]
    assert d["value"] == page.NOT_VISIBLE
    assert "TED" in d["sub"] and "ask the company" in d["sub"]


def test_portfolio_overlap_shows_what_the_portfolio_company_does():
    sig = {"thesis": {"fund": {"sectors": ["defence"], "geography": "CEE", "stage": "seed",
                               "initial_ticket_eur": [500_000, 2_000_000]},
                      "portfolio_overlap": [{"name": "Vermeer (VENTURES deal, not Defense fund)",
                                             "description": "GPS-free navigation for drones",
                                             "shared_terms": ["drone", "navigat"]}]}}
    row = next(r for r in page.extras(sig, _facts(), Refs(_facts()), CO)["thesis"] if r["criterion"] == "Portfolio overlap")
    assert row["company"].startswith("Vermeer: GPS-free navigation for drones")
    assert "not a confirmed conflict" in row["company"] and "navigat," not in row["company"]


def test_grant_without_amount_is_not_none_found():
    sig = {"funding": {"public_money": {"grants": 1, "grants_czk": 0}}}
    t = _tiles(sig, _facts())
    assert t["Grants & subsidies awarded (not revenue)"]["value"] == "amount not published"


def test_latest_reported_round_by_stage_not_article_date():
    # an English article dated 2025 restates the 2023 pre-seed (with a wrong currency); the latest round is the seed
    sig = {"funding": {"rounds": [
        {"date": "2023-01-23", "round": "pre-seed", "amount": "56 milionů korun", "fact_ids": []},
        {"date": "2025-06-24", "round": "seed", "amount": "4.2 million USD", "fact_ids": []},
        {"date": "2025-06-24", "round": "pre-seed", "amount": "nearly $56 million", "fact_ids": []}]}}
    t = _tiles(sig, _facts())
    assert t["Latest reported round"]["value"] == "4.2M USD"
    assert [page._stage(x) for x in ("pre-seed", "Pre-Seed", "seed", "Series A", "growth equity", "loan")] == [1, 1, 2, 3, 6, 0]


def test_site_pages_are_noindex(tmp_path, monkeypatch):
    from dd import site
    m = {"golden": [("a", "check", True, "")], "integrity": [("a", 10, 0, [])],
         "rows": [("a", {"cost": 0.02, "facts": 5, "sources": 3, "verified": "1/2", "sections": "6/6",
                         "invest": False, "glance": set(), "generated_at": "2026-11-17"}, "")],
         "strengths": {"verified": 1, "view": 1}, "by_section": {}, "facts_only": __import__("collections").Counter(
             {"verified": 1}), "total_cost": 0.02, "ledger": 0.5}
    html = site._index(m, "", {}, 12)
    assert site.NOINDEX in html and "1/1" in html and "10/10" in html
    assert site.NOINDEX in site._method(m)
