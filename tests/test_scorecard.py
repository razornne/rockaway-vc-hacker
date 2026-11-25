"""The screening scorecard: missing data widens the range, it never counts against the company."""
from datetime import date

from dd.scorecard import BAR, scorecard
from dd.store import Fact

AS_OF = date(2026, 11, 25)


def _sig(**over):
    sig = {"thesis": {"sectors": [{"sector": "deep tech", "evidence": 12, "fact_ids": [1],
                                   "structured_evidence_fact_ids": []}],
                      "geography": {"country": "CZ", "fact_ids": [2]}},
           "funding": {"rounds": [{"date": "2026-06-01", "round": "seed", "amount": "1.5 million EUR",
                                   "status": "closed", "fact_ids": [3]}],
                       "financials": {"period": "2025", "income_statement_published": True, "revenue": 30e6,
                                      "revenue_prior": 20e6, "net_result": 1e6, "cash": 10e6, "fact_ids": [4]},
                       "public_money": {"grants": 2}},
           "engineering": {"public_repos": 8, "repo_fact_ids": [5]},
           "verification": [{"check": "customer_corroboration", "status": "confirmed", "fact_ids": [6]}]}
    for k, v in over.items():
        sig[k] = v
    return sig


def _rows(s):
    return {r["key"]: r for r in s["rows"]}


GRANT = {9: Fact(company_id="x", type="grant_national", key="IsVavai-abc", source_url="https://hlidacstatu.cz",
                 value={"title": "R&D project"})}
TRADEMARK = {9: Fact(company_id="x", type="grant_national", key="DeMinimis-abc", source_url="https://hlidacstatu.cz",
                     value={"title": "Registrace ochranné známky"})}


def test_strong_company_passes_with_a_closed_score():
    s = scorecard(_sig(), GRANT, AS_OF)
    assert (s["min"], s["max"], s["total"]) == (14, 14, 14) and s["tone"] == "pass"


def test_missing_accounts_are_open_not_zero():
    sig = _sig()
    sig["funding"] = {**sig["funding"], "financials": None}
    r = _rows(scorecard(sig, {}, AS_OF))
    assert (r["traction"]["min"], r["traction"]["max"]) == (0, 2) and r["traction"]["ask"]
    assert (r["finances"]["min"], r["finances"]["max"]) == (0, 2)


def test_public_sales_raise_the_floor_when_revenue_is_not_published():
    sig = _sig()
    sig["funding"] = {**sig["funding"], "financials": None,
                      "public_money": {"contract_kinds": {"purchase": {"count": 2, "fact_ids": [7]}}}}
    assert (_rows(scorecard(sig, {}, AS_OF))["traction"]["min"], _rows(scorecard(sig, {}, AS_OF))["traction"]["max"]) == (1, 2)


def test_contradicted_claim_scores_zero():
    s = scorecard(_sig(verification=[{"status": "confirmed"}, {"status": "contradicted"}]), {}, AS_OF)
    assert _rows(s)["claims"]["max"] == 0


def test_stale_round_is_open():
    sig = _sig()
    sig["funding"] = {**sig["funding"], "rounds": [{"date": "2022-06-01", "round": "convertible loan",
                                                    "amount": "15 milionů korun", "status": "closed", "fact_ids": [3]}]}
    r = _rows(scorecard(sig, {}, AS_OF))["round"]
    assert r["open"] and r["finding"] == "Last reported round: 15M CZK convertible loan (2022-06). No current round is reported."


def test_verdict_is_open_when_unknowns_decide_it_and_never_below_on_missing_data():
    sig = {"thesis": {"geography": {"country": "CZ"}}}  # almost nothing known
    s = scorecard(sig, {}, AS_OF)
    assert s["min"] < BAR <= s["max"] and s["tone"] == "open" and "needs" in s["verdict"]


def test_below_only_when_even_the_best_case_misses_the_bar():
    sig = _sig(verification=[{"status": "contradicted"}], engineering={})
    sig["thesis"] = {"sectors": [], "geography": {"country": "BR"}}
    sig["funding"] = {"rounds": [], "financials": {"period": "2025", "income_statement_published": True,
                                                   "revenue": 0, "net_result": -10e6, "cash": 1e6}}
    s = scorecard(sig, {}, AS_OF)
    assert s["max"] < BAR and s["tone"] == "below"


def test_insolvency_records_and_portfolio_overlap_are_flags():
    facts = {1: Fact(company_id="x", type="insolvency", key="isir", source_url="https://isir.justice.cz",
                     value={"records_found": 2})}
    sig = _sig()
    sig["thesis"] = {**sig["thesis"], "portfolio_overlap": [{"name": "Vermeer (VENTURES deal)"}]}
    flags = scorecard(sig, facts, AS_OF)["flags"]
    assert any("Vermeer" in f and "(" not in f for f in flags) and any("Insolvency" in f for f in flags)


def test_only_research_grants_count_as_technology_evidence():
    assert _rows(scorecard(_sig(), GRANT, AS_OF))["technology"]["min"] == 2
    assert _rows(scorecard(_sig(), TRADEMARK, AS_OF))["technology"]["min"] == 1  # repositories only
