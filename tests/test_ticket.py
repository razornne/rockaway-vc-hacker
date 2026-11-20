"""Round size vs the fund's initial ticket is arithmetic done by code, never by the model."""
import pytest

from dd import thesis


@pytest.mark.parametrize("text,low,high,cur", [
    ("~15M CZK", 600_000, 600_000, "CZK"),
    ("15 milionů korun", 600_000, 600_000, "CZK"),
    ("€8–16m", 8_000_000, 16_000_000, "EUR"),
    ("4.2 million USD", 4.2e6 / 1.10, 4.2e6 / 1.10, "USD"),
    ("nearly $56 million", 56e6 / 1.10, 56e6 / 1.10, "USD"),
    ("2,5 mil. Kč", 100_000, 100_000, "CZK"),
    ("12 milionů eur", 12e6, 12e6, "EUR"),
    ("500 000 EUR", 500_000, 500_000, "EUR"),
])
def test_parse_amount(text, low, high, cur):
    a = thesis.parse_amount(text)
    assert a["currency"] == cur and a["low"] == pytest.approx(low) and a["high"] == pytest.approx(high)


@pytest.mark.parametrize("text", [None, "", "undisclosed", "tens of millions", "15 million"])
def test_unreadable_amount_is_unknown(text):
    assert thesis.parse_amount(text) is None


def test_dronetag_round_is_within_ticket_not_above():
    # regression: the model wrote that a CZK 15M round "exceeds" the EUR 0.5-2m initial ticket
    st = thesis.stage_ticket([{"date": "2023-05-01", "round": "convertible loan", "amount": "~15M CZK",
                               "status": "closed", "fact_ids": [6]}])
    assert st["relation"] == "within_ticket"
    assert "€0.6m" in st["text"] and "exceed" not in st["text"]


def test_large_round_is_a_syndicate_not_a_misfit():
    st = thesis.stage_ticket([{"date": "2026-06-15", "round": "Series A", "amount": "€8–16m", "status": "sought",
                               "fact_ids": [8]}])
    assert st["relation"] == "above_ticket" and "syndicate" in st["text"]


def test_no_round_and_unknown_amount():
    assert thesis.stage_ticket([])["relation"] == "no_round"
    st = thesis.stage_ticket([{"round": "seed", "amount": "undisclosed", "status": "closed", "fact_ids": [1]}])
    assert st["relation"] == "unknown_amount" and "not compared" in st["text"]


def test_sought_round_wins_over_older_closed_round():
    rounds = [{"date": "2023-01-01", "round": "seed", "amount": "€1m", "status": "closed", "fact_ids": [1]},
              {"date": "2026-01-01", "round": "Series A", "amount": "€5m", "status": "sought", "fact_ids": [2]}]
    assert thesis.pick_round(rounds)["round"] == "Series A"


def test_restated_earlier_round_does_not_become_the_latest_closed_round():
    # Filuta: a 2025 English article restates the 2023 pre-seed as "nearly $56 million" (it was CZK 56M)
    rounds = [{"date": "2023-01-23", "round": "pre-seed", "amount": "56 milionů korun", "status": "closed", "fact_ids": [1]},
              {"date": "2025-06-24", "round": "seed", "amount": "4.2 million USD", "status": "closed", "fact_ids": [2]},
              {"date": "2025-06-25", "round": "pre-seed", "amount": "nearly $56 million", "status": "closed", "fact_ids": [3]}]
    assert thesis.pick_round(rounds)["amount"] == "4.2 million USD"


def test_reported_later_stage_beats_closed_earlier_stage():
    # Filuta as stored: the seed with Rockaway is 'reported' (no 'raised' in the quote), the restated pre-seed 'closed'
    rounds = [{"date": "2023-01-23", "round": "pre-seed", "amount": "56 milionů korun", "status": "closed", "fact_ids": [1]},
              {"date": "2025-06-24", "round": "seed", "amount": "4.2 million USD", "status": "reported", "fact_ids": [2]},
              {"date": "2025-06-24", "round": "pre-seed", "amount": "nearly $56 million", "status": "closed", "fact_ids": [3]}]
    assert thesis.last_round(rounds)["amount"] == "4.2 million USD"
    assert thesis.stage_ticket(rounds)["relation"] == "above_ticket"
