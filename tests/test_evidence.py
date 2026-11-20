"""Evidence labels must not make a whole statement look verified when only part of it rests on an official record."""
from dd.render import item_strength
from dd.store import Fact


def _f(i, url, extractor="public_money", ftype="grant_national"):
    return Fact(id=i, company_id="x", type=ftype, key=str(i), value={}, source_url=url, extractor=extractor,
                snippet=f"s{i}")


FACTS = {1: _f(1, "https://www.hlidacstatu.cz/Dotace/Detail/1"),
         2: _f(2, "https://cc.cz/article", "llm_extract", "press_mention"),
         3: _f(3, "https://forbes.cz/article", "llm_extract", "press_mention"),
         4: _f(4, "https://x.com/about", "web", "product_capability")}


def test_official_only_is_verified():
    assert item_strength([1], FACTS, "x.com", False)[0] == "verified"


def test_official_plus_one_outlet_is_only_partly_verified():
    assert item_strength([1, 2], FACTS, "x.com", False)[0] == "mixed"


def test_official_plus_two_outlets_is_corroborated():
    assert item_strength([1, 2, 3], FACTS, "x.com", False)[0] == "corroborated"


def test_company_words_make_it_partly_verified_and_judgements_stay_views():
    assert item_strength([1, 4], FACTS, "x.com", False)[0] == "mixed"
    assert item_strength([1], FACTS, "x.com", True)[0] == "view"
