"""Fit with the Rockaway Ventures thesis, computed by code from the facts and our portfolio research.

The fund profile comes from public sources gathered in research/fund/fund_facts.md (each with a URL). The fit is a
checklist the partner can verify, not a score: sector (which thesis sectors the evidence points to, with fact ids),
geography, stage and ticket, and overlap with the existing portfolio (a possible conflict or synergy).
"""
from __future__ import annotations

import json
import re
from functools import lru_cache
from typing import Any

from dd.config import ROOT
from dd.store import Fact

FUND = {
    "name": "Rockaway Ventures",
    "stage": "late seed and Series A",
    "initial_ticket_eur": [500_000, 2_000_000],
    "geography": "CEE (about 60%), DACH, Western Europe and European founders in the US",
    "sectors": ["AI-led transformative tech", "deep tech", "defence / dual-use", "industrial / manufacturing AI", "energy"],
    "sources": ["https://www.rockawaycapital.com/en/fund/rockaway-ventures",
                "https://www.euro.cz/clanky/ceske-startupy-umeji-dokazat-hodne-s-malem-jen-si-nekdy-malo-veri-rika-petr-smid-z-rockaway-ventures/",
                "https://tech.eu/2025/05/16/rockaway-ventures-closes-55m-fund-to-back-transformative-tech-in-cee-and-beyond/"],
}
CEE = {"CZ", "SK", "PL", "HU", "RO", "BG", "SI", "HR", "RS", "EE", "LV", "LT", "UA", "AT", "DE", "CH"}
SECTOR_TERMS = {
    "defence / dual-use": r"defen[cs]e|military|armed forces|\barmy\b|\bNATO\b|dual[- ]use|counter[- ]?(uas|drone)|"
                          r"\bISR\b|battlefield|tactical|armád|obran|vojensk|bezpečnost",
    "AI-led transformative tech": r"artificial intelligence|\bAI\b|machine learning|neural|computer vision|"
                                  r"autonom|umělou inteligencí|umělá inteligence",
    "deep tech": r"robot|hardware|sensor|patent|research|universit|spin[- ]?off|lidar|radar|satellit|"
                 r"výzkum|vysoké učení|ČVUT|CTU",
    "industrial / manufacturing AI": r"manufactur|industrial|factory|inspection|predictive maintenance|"
                                     r"warehouse|logistics|výrob|průmysl",
    "energy": r"\benerg|battery|batteri|solar|photovolta|\bgrid\b|fotovolta",
}
EVIDENCE_TYPES = ("product_capability", "tech_claim", "business_model", "market_claim", "customer", "revenue_claim",
                  "press_mention", "grant_national", "grant_eu", "public_tender", "accelerator", "paper", "patent")
STRUCTURED_DEFENCE = ("public_tender", "grant_eu", "accelerator")
STOP = set("""with from that this their have will about into using based other more than also which while these
those they them company companies startup startups solution solutions platform system systems technology
technologies products product services service development developing management software
communication communications critical position positioning network networks real-time analytics operations
operational customer customers infrastructure protection security secure data teams team without online
operating revenue revenues business businesses market markets listed page pages built confirm confirmed
czech czechia link links fund funds deal deals source sources announced""".split())


def _text(f: Fact) -> str:
    v = f.value if isinstance(f.value, dict) else {}
    return " ".join(str(x) for x in (f.key, f.snippet, v.get("title"), v.get("summary"), v.get("area"),
                                     v.get("description"), v.get("buyer"), v.get("programme_name")) if x)


def _structured_defence(f: Fact) -> bool:
    v = f.value if isinstance(f.value, dict) else {}
    return (f.type == "public_tender" and v.get("defence_buyer") and v.get("role") in ("winner", "tenderer")) \
        or (f.type == "grant_eu" and v.get("defence")) \
        or (f.type == "accelerator" and "nato" in str(v.get("programme", "")).lower())


def sectors(facts: list[Fact]) -> list[dict]:
    out = []
    for sector, pat in SECTOR_TERMS.items():
        hits = [f for f in facts if f.type in EVIDENCE_TYPES and re.search(pat, _text(f), re.I)]
        strong = [f for f in facts if sector == "defence / dual-use" and _structured_defence(f)]
        ids = sorted({f.id for f in hits + strong if f.id is not None})
        if len(ids) >= 2 or strong:
            out.append({"sector": sector, "evidence": len(ids), "fact_ids": ids[:8],
                        "structured_evidence_fact_ids": sorted({f.id for f in strong if f.id is not None})})
    out.sort(key=lambda s: (-len(s["structured_evidence_fact_ids"]), -s["evidence"]))
    return out


@lru_cache(maxsize=1)
def _portfolio() -> list[dict]:
    out = []
    for path, name_key, desc_key in (("research/fund/portfolio_list.json", "name", "description"),
                                     ("research/defense/rockaway_defense_portfolio.json", "company", "description")):
        try:
            rows = json.loads((ROOT / path).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for r in rows:
            out.append({"name": r.get(name_key), "description": r.get(desc_key) or "",
                        "source_url": (r.get("source_url") or "").split(" ; ")[0] or None,
                        "vehicle": "Rockaway Defense" if "defense" in path else r.get("rockaway_entity")})
    return out


def _terms(text: str) -> set[str]:
    t = re.sub(r"\b(uavs?|uas|drones?)\b", " drone ", (text or "").lower())
    t = re.sub(r"\b(gnss|gps)[- ]?(denied|free)\b", " gpsdenied ", t)
    return {w[:7] for w in re.findall(r"[a-z][a-z-]{3,}", t) if w not in STOP}


def _base(name: str) -> str:
    return re.sub(r"\s*\(.*$", "", name or "").strip().lower()


def portfolio_overlap(facts: list[Fact], company_name: str | None) -> list[dict]:
    """Portfolio companies whose description shares two or more terms with the company's product evidence."""
    own = " ".join(_text(f) for f in facts if f.type in ("product_capability", "tech_claim", "business_model",
                                                           "market_claim", "competitor", "accelerator"))
    mine = _terms(own)
    out = []
    for p in _portfolio():
        if not p["name"] or (company_name and _base(p["name"]) == _base(company_name)):
            continue
        shared = sorted(_terms(p["description"]) & mine)
        if len(shared) >= 2:
            out.append({**p, "shared_terms": shared})
    out.sort(key=lambda p: -len(p["shared_terms"]))
    seen, uniq = set(), []
    for p in out:  # the same company can appear in both portfolio files
        key = _base(p["name"])
        if key not in seen:
            seen.add(key)
            uniq.append(p)
    return uniq[:4]


def fit(facts: list[Fact], company_name: str | None = None, country: str | None = None) -> dict[str, Any]:
    ident = next((f for f in facts if f.type == "identity" and isinstance(f.value, dict)), None)
    geo = country or ("CZ" if ident else None)
    return {
        "fund": FUND,
        "sectors": sectors(facts),
        "geography": {"country": geo, "in_core_region": bool(geo and geo.split("/")[0] in CEE),
                      "fact_ids": [ident.id] if ident and ident.id else []},
        "portfolio_overlap": portfolio_overlap(facts, company_name),
    }
