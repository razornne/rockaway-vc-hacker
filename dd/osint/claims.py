"""Company claims against records, by code over facts already collected. No network, no model.

Each check returns `verification` facts (extractor osint_claims) with the usual statuses (dd/verify.py):
confirmed, partly, contradicted, not_found. "not_found" means not visible in the records read, never "false".
"""
from __future__ import annotations

import re

from dd.store import Company, Fact

NAME = "osint_claims"

AI_CLAIM = re.compile(r"\b(?:AI|A\.I\.|artificial intelligence|machine learning|deep learning|neural|LLM|"
                      r"computer vision|umělá inteligence|umělou inteligencí|strojové učení)\b", re.I)
HEADCOUNT = re.compile(r"(?<![\d.,])(\d{1,3}(?:[ ,.]\d{3})?|\d{2,4})\s*\+?\s*(?:full[- ]time\s+)?"
                       r"(?:people|employees|engineers|team members|staff|specialists|experts|developers|"
                       r"zaměstnanc\w*|lidí|odborník\w*|inženýr\w*)\b", re.I)
REVENUE = re.compile(r"(?:revenue|turnover|sales|tržb\w*|obrat\w*)", re.I)
PUBLIC_BUYER = re.compile(r"\b(?:army|armed forces|military|ministry of defen[cs]e|ministry|police|fire (?:and )?rescue|"
                          r"government|municipalit\w*|city of|armád\w*|ministerstv\w*|policie|policií|hasič\w*|"
                          r"vojensk\w*|státní správ\w*)\b", re.I)
# Full employer cost of one full-time person a year in Czechia, as a deliberately wide range: from about the national
# average wage with contributions (CZK 0.75M) to a senior engineer (CZK 1.6M). Stated beside every result.
COST_PER_FTE_CZK = (750_000, 1_600_000)


def _text(f: Fact) -> str:
    v = f.value if isinstance(f.value, dict) else {}
    return f"{f.snippet or ''} {v.get('summary') or ''}"


def _fact(company: Company, key: str, value: dict, url: str, snippet: str | None = None) -> Fact:
    return Fact(company_id=company.id, type="verification", key=key, value=value, source_url=url, snippet=snippet,
                extractor=NAME, confidence="high")


def check_ai(company: Company, facts: list[Fact]) -> list[Fact]:
    """'We build AI': is there evidence of the company's own ML work, or does it only use vendors' models?"""
    from dd.signals import ai_dependency
    claims = [f for f in facts if f.type in ("tech_claim", "product_capability", "business_model")
              and AI_CLAIM.search(_text(f))]
    if not claims:
        return []
    dep = ai_dependency(facts)
    own = dep["own_model_evidence"]
    by_id = {f.id: f for f in facts}
    evidence = {"papers": own["papers"], "published models": own["hf_models"], "ML job posts": own["ml_roles"]}
    ml_repos = [f.id for f in facts if f.type == "repo" and re.search(
        r"\b(?:ml|model|neural|torch|tensorflow|training|dataset|vision|llm|ai)\b",
        f"{(f.value or {}).get('description', '')} {(f.value or {}).get('language', '')} {f.key}", re.I)]
    if ml_repos:
        evidence["ML repositories"] = ml_repos
    found = {k: v for k, v in evidence.items() if v}
    vendors = sorted(dep["llm_vendors_used"])
    c = claims[0]
    if found:
        status = "confirmed"
        detail = "Own ML work visible: " + "; ".join(f"{len(v)} {k}" for k, v in found.items()) + "."
        ref = by_id.get(next(iter(found.values()))[0])
    elif vendors:
        status = "partly"
        detail = (f"The AI it describes uses third-party models ({', '.join(vendors[:3])}); no own models, papers, "
                  "ML repositories or ML job posts are visible.")
        ref = by_id.get(dep["llm_vendors_used"][vendors[0]][0])
    else:
        status = "not_found"
        detail = ("No own models, papers, ML repositories, ML job posts or named model vendors are visible in the "
                  "sources read; ask who builds the AI and on which models.")
        ref = c
    return [_fact(company, "ai", {"check": "ai_claim", "status": status, "detail": detail,
                                  "claim_snippet": (c.snippet or "")[:300], "claim_url": c.source_url,
                                  "claim_fact_ids": [f.id for f in claims[:3] if f.id]},
                  (ref or c).source_url, snippet=detail)]


# A headcount that is a plan ("the goal is a team of 60 to 100", "we should reach 43") is not the team today.
PLAN = re.compile(r"\b(?:goal|target|plan\w*|aim\w*|ambition|will|should|would|want\w*|expect\w*|grow to|reach|"
                  r"cíl\w*|vybudovat|bude\w*|budou|bychom|chce\w*|měli|dostat na|ambic\w*|by 20\d\d|do roku)\b", re.I)
NOW = re.compile(r"\b(?:today|now|currently|employs|has|have|dnes\w*|dnešní\w*|nyní|aktuálně|současn\w*|zaměstnává|má)\b\W*"
                 r"(?:\w+\W+){0,2}$", re.I)


def _headcount(facts: list[Fact]) -> tuple[int, Fact] | None:
    """The largest headcount stated as the team today; plans and ranges are skipped."""
    best = None
    for f in facts:
        if f.type not in ("team_claim", "tech_claim", "business_model", "product_capability"):
            continue
        t = _text(f)
        for m in HEADCOUNT.finditer(t):
            before = t[max(0, m.start() - 60):m.start()]
            planned = PLAN.search(before) and (re.search(r"\b(?:to|na|až)\s*$", before) or not NOW.search(before[-25:]))
            if re.search(r"\d\s*[-–]\s*$", before) or planned:  # "from 33 today to 43" (planned): 43 is skipped
                continue
            n = int(re.sub(r"[ ,.]", "", m.group(1)))
            if 5 <= n <= 5000 and (best is None or n > best[0]):
                best = (n, f)
    return best


def check_team_size(company: Company, facts: list[Fact], financials: dict | None) -> list[Fact]:
    """A stated headcount against what filed personnel costs can pay for."""
    hc = _headcount(facts)
    if not hc or not financials or not financials.get("personnel_costs"):
        return []
    n, claim = hc
    cost = float(financials["personnel_costs"])
    lo, hi = cost / COST_PER_FTE_CZK[1], cost / COST_PER_FTE_CZK[0]
    period = financials.get("period")
    basis = (f"personnel costs {period} of CZK {cost / 1e6:.1f}M pay for about {lo:.0f}–{hi:.0f} full-time people at "
             f"CZK {COST_PER_FTE_CZK[0] / 1e6:.2f}–{COST_PER_FTE_CZK[1] / 1e6:.1f}M a year each")
    if n <= hi * 1.25:
        status, detail = "confirmed", f"A team of {n} fits: {basis}."
    elif n <= hi * 2:
        status, detail = "partly", (f"The company mentions {n} people; {basis}. Part-timers, contractors or "
                                    "university staff could explain the gap: ask how the team is employed.")
    else:
        status, detail = "contradicted", (f"The company mentions {n} people; {basis}. Ask how many are employed "
                                          "and how many are contractors or shared with other organisations.")
    src = (financials.get("source_url") or claim.source_url)
    return [_fact(company, "team_size", {"check": "team_size", "status": status, "detail": detail,
                                         "claimed": n, "fte_range": [round(lo), round(hi)],
                                         "claim_snippet": (claim.snippet or "")[:300], "claim_url": claim.source_url,
                                         "claim_fact_ids": [claim.id] if claim.id else [],
                                         "record_fact_ids": financials.get("fact_ids") or []},
                  src, snippet=detail)]


def check_revenue(company: Company, facts: list[Fact], financials: dict | None) -> list[Fact]:
    """A revenue figure for a year (press, website) against filed revenue for the same year."""
    from dd.thesis import parse_money
    if not financials or not financials.get("income_statement_published") or not financials.get("revenue"):
        return []
    year = str(financials.get("period") or "")
    filed = float(financials["revenue"])
    out = []
    for f in facts:
        if f.type not in ("revenue_claim", "press_mention", "business_model", "tech_claim", "team_claim"):
            continue
        t = _text(f)
        if not REVENUE.search(t) or year not in t:
            continue
        m = parse_money(t)
        if not m or m["currency"] != "CZK" or m["high"] < 1e6:
            continue
        mid = (m["low"] + m["high"]) / 2
        gap = mid / filed - 1
        status = "confirmed" if abs(gap) <= 0.15 else "contradicted" if abs(gap) > 0.30 else "partly"
        detail = (f"Stated {year} revenue about CZK {mid / 1e6:.1f}M; filed accounts show CZK {filed / 1e6:.1f}M "
                  f"({gap:+.0%}).")
        out.append(_fact(company, f"revenue:{f.id}", {"check": "revenue_claim", "status": status, "detail": detail,
                                                      "claim_snippet": (f.snippet or "")[:300],
                                                      "claim_url": f.source_url, "claim_fact_ids": [f.id],
                                                      "record_fact_ids": financials.get("fact_ids") or []},
                         f.source_url, snippet=detail))
        if len(out) >= 2:
            break
    return out


def check_public_buyers(company: Company, facts: list[Fact]) -> list[Fact]:
    """'We supply the army / ministries / cities' against contracts and tenders in public records."""
    claims = [f for f in facts if f.type in ("customer", "tech_claim", "product_capability", "business_model")
              and PUBLIC_BUYER.search(_text(f))]
    if not claims:
        return []
    records = [f for f in facts if (f.type == "gov_contract" and (f.value or {}).get("company_role") == "supplier")
               or (f.type == "public_tender" and (f.value or {}).get("role") == "winner")]
    c = claims[0]
    if records:
        buyers = list(dict.fromkeys(str((f.value or {}).get("counterparty") or (f.value or {}).get("buyer") or "")
                                    for f in records if f.value))[:3]
        detail = f"{len(records)} public contract(s) or won tender(s) visible, e.g. with {', '.join(b for b in buyers if b)}."
        return [_fact(company, "public_buyers", {"check": "public_buyers", "status": "confirmed", "detail": detail,
                                                 "claim_snippet": (c.snippet or "")[:300], "claim_url": c.source_url,
                                                 "claim_fact_ids": [f.id for f in claims[:3] if f.id],
                                                 "record_fact_ids": [f.id for f in records[:3] if f.id]},
                      records[0].source_url, snippet=detail)]
    detail = ("No contract or won tender with a public buyer is visible in the Czech contracts register or TED; "
              "defence and security purchases are often not published, so ask which public buyers they supply.")
    return [_fact(company, "public_buyers", {"check": "public_buyers", "status": "not_found", "detail": detail,
                                             "claim_snippet": (c.snippet or "")[:300], "claim_url": c.source_url,
                                             "claim_fact_ids": [f.id for f in claims[:3] if f.id]},
                  c.source_url, snippet=detail)]


def run(company: Company, facts: list[Fact], financials: dict | None) -> list[Fact]:
    """financials: the dict dd.signals.funding()['financials'] builds from the filed accounts (or None)."""
    facts = [f for f in facts if f.extractor not in ("osint_claims",)]
    out: list[Fact] = []
    for check in (lambda: check_ai(company, facts), lambda: check_team_size(company, facts, financials),
                  lambda: check_revenue(company, facts, financials), lambda: check_public_buyers(company, facts)):
        out += check()
    return out


def financials_source(facts: list[Fact], fin: dict | None) -> dict | None:
    """The financials dict with the URL of the filing it was read from (for citing)."""
    if not fin:
        return None
    ids = set(fin.get("fact_ids") or [])
    src = next((f.source_url for f in facts if f.id in ids), None)
    return {**fin, "source_url": src}


