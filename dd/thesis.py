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


# ------------------------------------------------------------------ stage and ticket (code, never the model)
# Round size is the total raised from all investors; the fund's initial ticket is its own cheque. Comparing them is
# arithmetic, so it is done here and the model is told not to restate it (a model once wrote that CZK 15M "exceeds"
# a EUR 0.5-2m ticket).
EUR_PER = {"EUR": 1.0, "CZK": 1 / 25.0, "USD": 1 / 1.10}  # approximate fixed rates, stated next to every result
FX_NOTE = "converted at approximate fixed rates (25 CZK/EUR, 1.10 USD/EUR)"
STAGES = ((r"pre-?seed", 1), (r"\bseed", 2), (r"series\s*a\b", 3), (r"series\s*b\b", 4), (r"series\s*c\b", 5),
          (r"growth|series\s*[d-z]\b", 6))
_NUM = r"\d{1,3}(?:[  ]\d{3})+(?![\d.,])|\d{1,3}(?:[.,]\d{3})+(?![\d.,])|\d+(?:[.,]\d+)?"
_AMOUNT = re.compile(rf"({_NUM})\s*(?:[-–—]|to|až)\s*[€$]?\s*({_NUM})|({_NUM})", re.I)
_MULT = ((re.compile(r"\b(?:mld|miliard\w*|billions?|bn)\b", re.I), 1e9),
         (re.compile(r"\b(?:mil\w*|millions?|mio|mn)\b|(?<=\d)\s?m\b", re.I), 1e6),
         (re.compile(r"\b(?:tis\w*|thousands?)\b|(?<=\d)\s?k\b", re.I), 1e3))
_CURRENCY = (("EUR", re.compile(r"€|\beur\w*\b", re.I)), ("USD", re.compile(r"\$|\busd\b|\bdolar\w*|\bdollar\w*", re.I)),
             ("CZK", re.compile(r"\bkč\b|kč|\bczk\b|\bkorun\w*", re.I)))


class _Never:
    def start(self):
        return 10 ** 6


_NOPE = _Never()


def stage_rank(name: Any) -> int:
    n = str(name or "").lower()
    return next((rank for pat, rank in STAGES if re.search(pat, n)), 0)  # first match: "pre-seed" before "seed"


def _num(s: str, scaled: bool = False) -> float:
    """'85 291', '28,000,000' and '28.000.000' are grouped thousands; '1,5' and '4.2' are decimals. A single group
    after a comma ('28,000') is thousands unless a word like 'million' follows ('1,500 milionu' is 1.5 million)."""
    s = s.replace("\u00a0", " ")
    if re.fullmatch(r"\d{1,3}(?: \d{3})+", s):
        return float(s.replace(" ", ""))
    if re.fullmatch(r"\d{1,3}([.,])\d{3}(?:\1\d{3})+", s) or (re.fullmatch(r"\d{1,3},\d{3}", s) and not scaled):
        return float(re.sub(r"[.,]", "", s))
    return float(s.replace(",", "."))


def parse_money(text: Any) -> dict | None:
    """'15 milionů korun' -> {'low': 15e6, 'high': 15e6, 'currency': 'CZK'} in the original currency. None when the
    amount or its currency cannot be read: an unreadable amount is unknown, never zero."""
    t = str(text or "")
    m = _AMOUNT.search(t)
    if not m or "+" in t:  # "100 milionů korun + 4-5 milionů eur" is several amounts: not one number
        return None
    # the currency that belongs to this number: a symbol just before it, or a word just after it
    before, after = t[max(0, m.start() - 3):m.start()], t[m.end():m.end() + 30]
    cur = (next((c for c, rx in _CURRENCY if rx.search(before)), None)
           or next((c for c, rx in sorted(_CURRENCY, key=lambda cr: (cr[1].search(after) or _NOPE).start())
                    if rx.search(after)), None))
    if not cur:
        found = {c for c, rx in _CURRENCY if rx.search(t)}
        cur = found.pop() if len(found) == 1 else None
    if not cur:
        return None
    lo, hi = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(3))
    mult = next((k for rx, k in _MULT if rx.search(t[m.start():m.end() + 30])), 1.0)
    return {"low": _num(lo, mult > 1) * mult, "high": _num(hi, mult > 1) * mult, "currency": cur}


def parse_amount(text: Any) -> dict | None:
    """Like parse_money, converted to EUR at the stated approximate rates."""
    a = parse_money(text)
    if not a:
        return None
    rate = EUR_PER[a["currency"]]
    return {"low": a["low"] * rate, "high": a["high"] * rate, "currency": a["currency"]}


def _m(x: float) -> str:
    if x >= 1e9:
        return f"{x / 1e9:.2f}".rstrip("0").rstrip(".") + "B"
    if x >= 1e6:
        return f"{x / 1e6:.2f}".rstrip("0").rstrip(".") + "M"
    return f"{x / 1e3:.0f}k"


def format_money(text: Any) -> str | None:
    """One way to write amounts everywhere: '15 milionů korun' -> '15M CZK', '10 až 16 milionů eur' -> '10–16M EUR'.
    None when the amount or currency cannot be read (the caller then shows the source's own wording)."""
    a = parse_money(text)
    if not a:
        return None
    if a["low"] == a["high"]:
        return f"{_m(a['low'])} {a['currency']}"
    lo, hi = _m(a["low"]), _m(a["high"])
    if lo[-1] == hi[-1]:
        lo = lo[:-1]
    return f"{lo}–{hi} {a['currency']}"


def pick_round(rounds: list[dict]) -> dict | None:
    """The round a partner would discuss: the latest one being raised, else the latest closed one by stage then date
    (a later article can restate an earlier round, sometimes with a wrong currency), else the latest by stage."""
    sought = [r for r in rounds if r.get("status") == "sought"]
    if sought:
        return sorted(sought, key=lambda r: r.get("date") or "")[-1]
    return last_round(rounds)


def last_round(rounds: list[dict]) -> dict | None:
    """The latest round that is not just being sought: highest stage first (a seed round reported without the word
    'raised' still comes after a closed pre-seed), then closed over merely reported, then date."""
    done = [r for r in rounds if r.get("status") != "sought"]
    return sorted(done, key=lambda r: (stage_rank(r.get("round")), r.get("status") == "closed",
                                       r.get("date") or ""))[-1] if done else None


def _eur(x: float) -> str:
    return f"€{x / 1e6:.1f}m".replace(".0m", "m") if x >= 1e5 else f"€{x / 1e3:.0f}k"


STATUS_WORD = {"sought": "Round being raised", "closed": "Closed round", "reported": "Reported round"}


def stage_ticket(rounds: list[dict]) -> dict:
    lo_t, hi_t = FUND["initial_ticket_eur"]
    ticket = f"{_eur(lo_t)}–{_eur(hi_t)}"
    r = pick_round(rounds or [])
    if not r:
        return {"relation": "no_round", "text": "No round reported in collected sources.", "fact_ids": []}
    shown = format_money(r.get("amount")) or r.get("amount") or "amount not stated"
    head = f"{STATUS_WORD.get(r.get('status'), 'Reported round')}: {shown}" \
           + (f" ({r['round']})" if r.get("round") else "")
    a = parse_amount(r.get("amount"))
    if not a:
        return {"relation": "unknown_amount", "round": r, "fact_ids": r.get("fact_ids") or [],
                "text": f"{head}. The amount or its currency is not stated clearly, so it is not compared with the "
                        f"fund's initial ticket ({ticket})."}
    size = _eur(a["low"]) if a["low"] == a["high"] else f"{_eur(a['low'])}–{_eur(a['high'])}"
    approx = "" if a["currency"] == "EUR" else f" ≈ {size}, {FX_NOTE}"
    if a["high"] < lo_t:
        rel, says = "below_ticket", f"smaller than the fund's minimum initial ticket ({_eur(lo_t)})"
    elif a["low"] > hi_t:
        rel, says = "above_ticket", (f"larger than the fund's initial ticket ({ticket}). A round is the total from all "
                                     "investors, so the fund would be one investor in a syndicate, as lead or participant")
    elif a["low"] >= lo_t and a["high"] <= hi_t:
        rel, says = "within_ticket", f"within the fund's initial ticket ({ticket}): one cheque could cover the whole round"
    else:
        rel, says = "overlaps_ticket", f"partly within the fund's initial ticket ({ticket})"
    return {"relation": rel, "round": r, "round_eur": [a["low"], a["high"]], "fact_ids": r.get("fact_ids") or [],
            "text": f"{head}{approx}. The round is {says}."}


def fit(facts: list[Fact], company_name: str | None = None, country: str | None = None,
        rounds: list[dict] | None = None) -> dict[str, Any]:
    ident = next((f for f in facts if f.type == "identity" and isinstance(f.value, dict)), None)
    geo = country or ("CZ" if ident else None)
    return {
        "fund": FUND,
        "sectors": sectors(facts),
        "geography": {"country": geo, "in_core_region": bool(geo and geo.split("/")[0] in CEE),
                      "fact_ids": [ident.id] if ident and ident.id else []},
        "stage_ticket": stage_ticket(rounds or []),
        "portfolio_overlap": portfolio_overlap(facts, company_name),
    }
