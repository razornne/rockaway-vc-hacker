"""Deterministic signals computed from the fact snapshot (no LLM).

These are the "at a glance" numbers a partner scans first. Every signal carries the fact IDs it was
computed from, so the dossier can link to evidence. The LLM analysis receives them as context, but they are
rendered from code, not from model output — they cannot be hallucinated.
"""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from typing import Any

from dd.store import Fact

LLM_VENDORS = {
    "OpenAI": r"\bopen\s?ai\b|\bgpt-?\d|\bchatgpt\b",
    "Anthropic": r"\banthropic\b|\bclaude\b",
    "Azure OpenAI": r"\bazure\s+open\s?ai\b",
    "Google Gemini / Vertex": r"\bgemini\b|\bvertex\s+ai\b",
    "Mistral": r"\bmistral\b",
    "Cohere": r"\bcohere\b",
    "Meta Llama": r"\bllama\b",
    "Hugging Face": r"\bhugging\s?face\b",
}
OWN_MODEL_PATTERNS = re.compile(
    r"\b(?:our|own|proprietary|in-house|custom)\s+(?:\w+\s+){0,2}(?:models?|llms?|neural|algorithms?|engine)\b|"
    r"\b(?:trained|train|fine-?tuned?|pre-?trained)\b|\bpatent", re.I)

ROLE_BUCKETS = [
    ("ml_research", r"\b(?:machine learning|ml|ai research|research scientist|scientist|data scientist|llm|nlp|computer vision|deep learning)\b"),
    ("sales_gtm", r"\b(?:account executive|sales|business development|bdr|sdr|partnerships?|customer success|account manager|growth|marketing)\b"),
    ("forward_deployed", r"\b(?:forward deployed|solutions? (?:engineer|architect)|implementation|customer engineer)\b"),
    ("engineering", r"\b(?:engineer|developer|devops|sre|architect|cto|tech lead|programmer|qa)\b"),
]
PRODUCT_SURFACES = ("api", "app", "docs", "developer", "developers", "status", "sandbox", "console", "dashboard",
                    "portal", "platform", "admin", "auth", "login", "sdk")
INVESTOR_HINT = re.compile(r"ventures?|capital|fund|scsp|sicav|invest|partners|holding|vc\b|rizikového", re.I)


def _ids(facts: list[Fact]) -> list[int]:
    return [f.id for f in facts if f.id is not None]


def _text(f: Fact) -> str:
    v = f.value if isinstance(f.value, dict) else {}
    return " ".join(str(x) for x in (f.key, f.snippet, v.get("summary"), v.get("title"), v.get("vendor"),
                                     v.get("evidence"), v.get("technology")) if x)


def _published_by_url(facts: list[Fact]) -> dict[str, str]:
    out = {}
    for f in facts:
        if f.type == "press_mention" and isinstance(f.value, dict) and f.value.get("published"):
            out[f.source_url] = str(f.value["published"])[:10]
    return out


def _inv_key(name: str) -> str:
    plain = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    plain = re.sub(r"\b(vc|\.vc|ventures?|capital|fund|partners|invest|s\.?r\.?o\.?|a\.?s\.?)\b", " ", plain)
    return re.sub(r"[^a-z0-9]", "", plain)


def _days(a: str | None, b: str | None) -> int | None:
    from datetime import date
    try:
        da, db = (date.fromisoformat((x + "-01-01")[:10] if len(x) == 4 else (x + "-01")[:10] if len(x) == 7 else x[:10])
                  for x in (a, b))
        return abs((da - db).days)
    except (TypeError, ValueError):
        return None


def _amount_numbers(amount: str | None) -> set[str]:
    return set(re.findall(r"\d+(?:[.,]\d+)?", (amount or "").replace(" ", "")))


def _shared_investor(a: set[str], b: set[str]) -> bool:
    """'psg' and 'psgequity' are the same investor (one report shortens the name)."""
    return any(x == y or (min(len(x), len(y)) >= 3 and (x in y or y in x)) for x in a for y in b)


def _round_key(label: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(label).lower().replace("series", "")) or "?"


def _parse_money(text):
    from dd.thesis import parse_money
    return parse_money(text)


def _cluster_rounds(rounds: list[dict]) -> list[dict]:
    """Several articles report the same round; merge reports within 60 days that share investors or amount."""
    clusters: list[dict] = []
    for r in rounds:
        keys = {_inv_key(i) for i in r["investors"] if _inv_key(i)}
        nums = _amount_numbers(r["amount"])
        target = None
        for c in clusters:
            gap = _days(c["date"], r["date"])
            if gap is not None and gap <= 60 and (_shared_investor(keys, c["_keys"]) or nums & c["_nums"]):
                target = c
                break
            same_label = bool(r.get("round") and c.get("round") and _round_key(r["round"]) == _round_key(c["round"]))
            if gap is None and nums & c["_nums"] and (_shared_investor(keys, c["_keys"]) or (same_label and not keys)):
                # undated report of the same round: same amount and (a shared investor, or same stage with no investors)
                target = c
                break
        if target is None:
            clusters.append({**r, "investors": list(r["investors"]), "reports": 1, "_keys": set(keys), "_nums": set(nums)})
            continue
        target["reports"] += 1
        target["fact_ids"] = list(dict.fromkeys(target["fact_ids"] + r["fact_ids"]))
        if (not target.get("round") or str(target["round"]).lower() == "unknown") and r.get("round"):
            target["round"] = r["round"]
        if r.get("amount") and (not target.get("amount") or (_parse_money(target["amount"]) is None
                                                             and _parse_money(r["amount"]) is not None)):
            target["amount"] = r["amount"]  # prefer the report that states the currency ("15 milionů korun")
        for inv in r["investors"]:
            k = _inv_key(inv)
            if k and not any(k in x or x in k for x in target["_keys"]):
                target["investors"].append(inv)
                target["_keys"].add(k)
        target["_nums"] |= nums
    for c in clusters:
        c.pop("_keys"), c.pop("_nums")
        if str(c.get("round") or "").lower() == "unknown":
            c["round"] = None
    return clusters


SUBSIDY_AGREEMENT = re.compile(r"poskytnutí\s+(?:podpory|dotace|příspěvku)|posk\.\s*podp|zvýhodněn\w*\s+služ|"
                               r"dotac|příspěvk", re.I)
RD_AGREEMENT = re.compile(r"účast\w* na řešení|spoluprác\w* (?:na|při) řešení|využití výsledk|řešení projekt|"
                          r"součinnost\w* a kooperac|vědeckotechnick|výzkum\w* spoluprác|konsorci|partnersk\w* smlouv|"
                          r"rámcov\w* smlouv\w* o (?:partnerství|spolupráci)|memorand|vypořádání závazků|"
                          r"\b(?:FW|TQ|CK|CL|TH|TN|FV|OZ|TM|SS)\d{6,}", re.I)
LOAN = re.compile(r"výpůjč", re.I)
PURCHASE = re.compile(r"kupní|objednávk|dodávk|nákup|služb|dílo|díla|licen|nájem|pronájem|servis|"
                      r"\bVZ\b|veřejn\w* zakáz|detekc|dron|UAS|zařízení|systém", re.I)


def _group(fs: list[Fact], key) -> dict[str, list[Fact]]:
    out: dict[str, list[Fact]] = {}
    for f in fs:
        out.setdefault(key(f), []).append(f)
    return out


def contract_kind(f: Fact) -> str:
    """What a registr-smluv contract is, from its subject: purchase (a public buyer pays for something), rd_project
    (research consortium / results agreement: the amount is a project budget, not the company's revenue),
    subsidy (support or subsidised services), loan (a device lent for testing), other."""
    subj = str((f.value or {}).get("subject") or "")
    for kind, rx in (("subsidy", SUBSIDY_AGREEMENT), ("rd_project", RD_AGREEMENT), ("loan", LOAN), ("purchase", PURCHASE)):
        if rx.search(subj):
            if kind == "purchase" and (f.value or {}).get("company_role") == "payer":
                return "other"  # the company bought something: not a sale to a public buyer
            return kind
    return "other"


SOUGHT = re.compile(r"žád\w*|shán\w*|hled\w*|plánuj\w*|chce\w* získat|chtěj\w*|potřebuj\w*|"
                    r"otevřel\w* (?:první )?(?:investiční )?kolo|finaliz\w*|uzavír\w*|seek\w*|looking for|"
                    r"aims? to raise|plans? to raise|is raising|currently raising|target\w*|příslib\w*", re.I)
CLOSED = re.compile(r"získal\w*|investoval\w*|investuje|investují|vložil\w*|uzavřel\w*|dokončil\w*|"
                    r"\braised\b|has raised|closed|secured|completed|announced .{0,40}(?:round|investment)|"
                    r"successfully closes", re.I)


def round_status(f: Fact) -> str:
    """'sought' when the quote describes money being sought (asks, targets, an open round), 'closed' when it
    reports money received; otherwise 'reported'. Sought wins over closed inside one quote ('raised X, now seeks Y'
    is rare; 'is finalising a round' is common)."""
    q = f.snippet or ""
    if SOUGHT.search(q):
        return "sought"
    if CLOSED.search(q):
        return "closed"
    return "reported"


def funding(facts: list[Fact]) -> dict[str, Any]:
    pub = _published_by_url(facts)
    rounds = []
    for f in facts:
        if f.type != "funding_round" or not isinstance(f.value, dict):
            continue
        v = f.value
        if not (v.get("amount") or v.get("round") or v.get("investors")):
            continue  # e.g. "project funded by the European Commission" — not an equity round
        if re.search(r"grant|dotac|subsid", str(v.get("round") or ""), re.I):
            continue  # a grant labelled as a round by the extractor
        rounds.append({"date": f.event_date or pub.get(f.source_url), "date_source": "quote" if f.event_date else
                       ("article published" if pub.get(f.source_url) else None),
                       "round": v.get("round"), "amount": v.get("amount"), "investors": v.get("investors") or [],
                       "fact_ids": _ids([f])})
    rounds = _cluster_rounds(sorted(rounds, key=lambda r: r["date"] or "9999"))
    by_id = {f.id: f for f in facts}
    for r in rounds:  # sought vs closed, from the quoted wording (code, not the LLM)
        st = {round_status(by_id[i]) for i in r["fact_ids"] if i in by_id}
        r["status"] = "closed" if "closed" in st else "sought" if "sought" in st else "reported"
    holders =[f for f in facts if f.type == "registry_shareholder" and isinstance(f.value, dict)]
    investor_holders = [f for f in holders if INVESTOR_HINT.search(str(f.value.get("name", "")))]
    contracts = [f for f in facts if f.type == "gov_contract"]
    grants, seen_eu = [], set()
    for f in sorted((f for f in facts if f.type in ("grant_national", "grant_eu")), key=lambda f: f.extractor != "public_money"):
        if f.type == "grant_eu" and f.extractor in ("public_money", "eu_funding"):
            if f.key in seen_eu:  # the same project from CORDIS and from the EU F&T portal
                continue
            seen_eu.add(f.key)
        grants.append(f)
    total = lambda fs: sum(float(f.value.get("amount_czk") or 0) for f in fs if isinstance(f.value, dict))
    acc = sorted((f for f in facts if f.type == "financial_statement" and isinstance(f.value, dict)
                  and f.value.get("readable")), key=lambda f: str(f.value.get("period")))
    a = acc[-1] if acc else None
    financials = None
    if a:
        v = a.value
        cur = lambda block, key: ((v.get(block) or {}).get(key) or {}).get("current")  # noqa: E731
        prev = lambda block, key: ((v.get(block) or {}).get(key) or {}).get("prior")  # noqa: E731
        financials = {
            "period": v.get("period"), "period_end": v.get("period_end"), "currency": "CZK",
            "income_statement_published": v.get("pnl_published"),
            "revenue": v.get("revenue"),
            "revenue_prior": (sum(x or 0 for x in (prev("pnl", "revenue_products_services"), prev("pnl", "revenue_goods")))
                              if v.get("pnl_published") else None),
            "other_operating_income": cur("pnl", "other_operating_income"),
            "personnel_costs": cur("pnl", "personnel_costs"), "operating_result": cur("pnl", "operating_result"),
            "net_result": cur("balance", "net_result"), "net_result_prior": prev("balance", "net_result"),
            "cash": cur("balance", "cash"), "cash_prior": prev("balance", "cash"),
            "equity": cur("balance", "equity"), "total_assets": cur("balance", "total_assets"),
            "liabilities": cur("balance", "liabilities"), "receivables": cur("balance", "receivables"),
            "checks": v.get("checks"), "fact_ids": _ids([a]),
        }
    return {
        "financials": financials,
        "rounds": rounds,
        "registry_investors": [{"name": f.value.get("name"), "from": f.value.get("from"), "to": f.value.get("to"),
                                "share_pct": f.value.get("share_pct"), "fact_ids": _ids([f])} for f in investor_holders],
        "public_money": {"contracts": len(contracts), "contracts_czk": total(contracts), "grants": len(grants),
                         # grants_czk = support AWARDED to the company (whole projects, multi-year); paid = only what
                         # the payments register (IsRed) records as paid out, by year
                         "grants_czk": total(grants), "fact_ids": _ids(contracts + grants),
                         "grants_paid_czk": sum(float((f.value or {}).get("paid_czk") or 0) for f in grants),
                         "grants_with_payment_data": sum(bool((f.value or {}).get("paid_czk")) for f in grants),
                         # registr smluv may publish a contract without a price: "not stated" is not "0 CZK"
                         "contracts_unpriced": sum(not (f.value or {}).get("amount_czk") for f in contracts),
                         "grants_unpriced": sum(not (f.value or {}).get("amount_czk") for f in grants),
                         "contract_kinds": {k: {"count": len(fs), "czk": total(fs), "fact_ids": _ids(fs)} for k, fs in
                                            _group(contracts, contract_kind).items()},
                         "counterparties": list(dict.fromkeys(
                             re.sub(r"\s*\(.*?\)\s*$", "", str((f.value or {}).get("counterparty") or "")).strip()
                             for f in contracts if (f.value or {}).get("counterparty")))[:4]},
    }


def team_gtm(facts: list[Fact]) -> dict[str, Any]:
    jobs = [f for f in facts if f.type == "job_post"]
    buckets: dict[str, list[Fact]] = {}
    for f in jobs:
        title = str((f.value or {}).get("title") or f.key or "").lower()
        bucket = next((b for b, pat in ROLE_BUCKETS if re.search(pat, title)), "other")
        if (f.value or {}).get("is_ml") and bucket == "engineering":
            bucket = "ml_research"
        buckets.setdefault(bucket, []).append(f)
    founding = [f for f in jobs if re.search(r"\bfounding\b|\bfirst\b", str((f.value or {}).get("title") or f.key), re.I)]
    locations = Counter(str((f.value or {}).get("location")) for f in jobs if (f.value or {}).get("location"))
    team_claims = [f for f in facts if f.type == "team_claim"]
    return {
        "open_roles": len(jobs),
        "by_function": {b: {"count": len(fs), "titles": [str((f.value or {}).get("title") or f.key) for f in fs][:6],
                            "fact_ids": _ids(fs)} for b, fs in buckets.items()},
        "founding_roles": {"titles": [str((f.value or {}).get("title") or f.key) for f in founding], "fact_ids": _ids(founding)},
        "locations": dict(locations.most_common(5)),
        "team_claims": {"count": len(team_claims), "fact_ids": _ids(team_claims)},
    }


USED_TYPES = ("subprocessor", "saas_tool", "tech_stack", "tech_claim")      # the company itself relies on it
INTEGRATED_TYPES = ("integration", "product_capability")                    # the product connects to it


def _vendor_hits(facts: list[Fact], types: tuple[str, ...]) -> dict[str, list[Fact]]:
    out: dict[str, list[Fact]] = {}
    for f in facts:
        if f.type not in types:
            continue
        t = _text(f)
        for vendor, pat in LLM_VENDORS.items():
            if re.search(pat, t, re.I):
                out.setdefault(vendor, []).append(f)
    return out


def ai_dependency(facts: list[Fact]) -> dict[str, Any]:
    """Separate 'the company relies on vendor X' (subprocessor, own tech claims) from 'the product connects
    to the customer's X account' (integrations). Only the first is a dependency risk."""
    vendors = _vendor_hits(facts, USED_TYPES)
    integrated = _vendor_hits(facts, INTEGRATED_TYPES)
    own = [f for f in facts if f.type in ("tech_claim", "product_capability") and OWN_MODEL_PATTERNS.search(_text(f))]
    hf = [f for f in facts if f.type == "hf_model" and not (isinstance(f.value, dict) and f.value.get("identity_unverified"))]
    papers = [f for f in facts if f.type == "paper"]
    ml_jobs = [f for f in facts if f.type == "job_post" and (f.value or {}).get("is_ml")]
    return {
        "_meaning": ("llm_vendors_used = named as subprocessor/tool/own tech claim (a dependency); "
                     "llm_vendors_integrated = the product connects to the customer's account (NOT a dependency)"),
        "llm_vendors_used": {v: _ids(fs) for v, fs in vendors.items()},
        "llm_vendors_integrated": {v: _ids(fs) for v, fs in integrated.items()},
        "own_model_evidence": {"claims": _ids(own), "hf_models": _ids(hf), "papers": _ids(papers),
                               "ml_roles": _ids(ml_jobs)},
    }


def engineering(facts: list[Fact]) -> dict[str, Any]:
    repos = [f for f in facts if f.type == "repo" and not (f.value or {}).get("fork")]
    pushed = sorted((str((f.value or {}).get("pushed_at") or "")[:10] for f in repos), reverse=True)
    subs = [f for f in facts if f.type == "subdomain" and not str(f.key or "").startswith("*.")]
    surfaces = [f for f in subs if str(f.key or "").split(".")[0].lower() in PRODUCT_SURFACES]
    docs = [f for f in facts if f.type == "web_page" and f.key == "docs"]
    stack = [f for f in facts if f.type == "tech_stack"]
    return {
        "public_repos": len(repos), "stars": sum(int((f.value or {}).get("stars") or 0) for f in repos),
        "last_push": pushed[0] if pushed else None, "repo_fact_ids": _ids(repos),
        "subdomains": len(subs), "product_surfaces": sorted({str(f.key) for f in surfaces}),
        "surface_fact_ids": _ids(surfaces), "docs_pages": len(docs), "docs_fact_ids": _ids(docs),
        "stack": sorted({str((f.value or {}).get("technology") or f.key).lower(): str((f.value or {}).get("technology") or f.key)
                         for f in stack}.values(), key=str.lower), "stack_fact_ids": _ids(stack),
    }


def _name_key(name: str) -> tuple[str, str]:
    """(accent-free alnum key, acronym) — 'Houston Independent School District', 'HISD', 'Houston ISD' share 'hisd'."""
    plain = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    key = re.sub(r"[^a-z0-9]", "", plain)
    base = re.sub(r"\([^)]*\)", " ", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode())
    words = re.findall(r"[A-Za-z0-9]+", base)
    acro = "".join(w.lower() if (w.isupper() and len(w) > 1) else w[0].lower() for w in words)
    return key, acro


def _customer_names(cust: list[Fact]) -> tuple[list[str], list[int]]:
    """Distinct short customer names. Descriptions ('a mid-size European game studio') are not names."""
    names: list[str] = []
    keys: list[tuple[str, str]] = []
    ids: list[int] = []
    for f in cust:
        raw = str((f.value or {}).get("name") or "")
        for part in re.split(r"\s*[;,]\s*", raw):
            part = part.strip().strip(".")
            words = part.split()
            if not part or len(words) > 6 or part[:1].islower() or re.match(r"(?i)(a|an|the|case study|public|several|many)\b", part):
                continue
            key, acro = _name_key(part)
            if any(key == k or (len(key) > 3 and (key in k or k in key)) or (len(acro) >= 3 and acro == a)
                   for k, a in keys):
                continue
            keys.append((key, acro))
            names.append(part)
            if f.id is not None and f.id not in ids:
                ids.append(f.id)
    return names, ids


def customers(facts: list[Fact], company_name: str | None = None) -> dict[str, Any]:
    cust = [f for f in facts if f.type == "customer"]
    pricing = [f for f in facts if f.type == "pricing"]
    apps = [f for f in facts if f.type == "app"]
    names, name_ids = _customer_names(cust)
    if company_name:  # a case study page names the company itself ("Wultra helped OTP Bank") — not a customer
        own = _name_key(company_name)[0]
        names = [n for n in names if _name_key(n)[0] != own]
    return {"named_customers": names[:10], "customer_fact_ids": name_ids,
            "pricing_public": bool(pricing), "pricing_fact_ids": _ids(pricing),
            "apps": len(apps), "app_fact_ids": _ids(apps)}


def timeline(facts: list[Fact]) -> dict[str, Any]:
    inc = [f for f in facts if f.type == "registry_incorporation" and f.event_date]
    press = sorted([f for f in facts if f.type == "press_mention" and f.event_date], key=lambda f: f.event_date)
    return {"incorporated": inc[0].event_date if inc else None, "incorporated_fact_ids": _ids(inc[:1]),
            "first_press": press[0].event_date if press else None, "first_press_fact_ids": _ids(press[:1]),
            "press_articles": len([f for f in facts if f.type == "press_mention"])}


def verification(facts: list[Fact]) -> list[dict[str, Any]]:
    """Outcome of independent checks of company claims (dd/verify.py)."""
    order = {"contradicted": 0, "confirmed": 1, "partly": 2, "not_found": 3, "not_checkable": 4}
    out = []
    for f in facts:
        if f.type != "verification" or not isinstance(f.value, dict):
            continue
        v = f.value
        out.append({"check": v.get("check"), "status": v.get("status"), "detail": v.get("detail"),
                    "subject": v.get("customer") or v.get("registry_holder"), "fact_ids": _ids([f])})
    patents = [f for f in facts if f.type == "patent"]
    out.sort(key=lambda x: (order.get(x["status"], 9), str(x["check"])))
    return out + ([{"check": "patents_found", "status": "info", "detail": f"{len(patents)} patent publications "
                    f"({sum(1 for p in patents if (p.value or {}).get('granted'))} granted)", "fact_ids": _ids(patents[:3])}]
                  if patents else [])


def defence(facts: list[Fact]) -> dict[str, Any]:
    """Defence / dual-use evidence from structured sources only (TED, EU F&T portal, NATO DIANA)."""
    tenders = [f for f in facts if f.type == "public_tender" and isinstance(f.value, dict)]
    won = [f for f in tenders if f.value.get("role") == "winner"]
    def_won = [f for f in won if f.value.get("defence_buyer")]
    edf = [f for f in facts if f.type == "grant_eu" and isinstance(f.value, dict) and f.value.get("defence")]
    acc = [f for f in facts if f.type == "accelerator"]
    peers = [f for f in facts if f.type == "peer_company" and isinstance(f.value, dict)]
    checks = {f.key: (f.value or {}).get("status") for f in facts if f.type == "source_check"
              and f.key in ("ted", "eu_ft_portal", "nato_diana")}
    return {
        "tenders_won": {"count": len(won), "defence_buyer": len(def_won),
                        "value_by_currency": {c: sum(float(f.value.get("value") or 0) for f in won if f.value.get("currency") == c)
                                              for c in {f.value.get("currency") for f in won if f.value.get("currency")}},
                        "buyers": list(dict.fromkeys(str(f.value.get("buyer")) for f in won if f.value.get("buyer")))[:4],
                        "fact_ids": _ids(won)},
        "tenders_mentioned": {"count": len(tenders) - len(won), "fact_ids": _ids([f for f in tenders if f not in won])},
        "eu_defence_projects": {"count": len(edf), "programmes": sorted({str(f.value.get("programme")) for f in edf}),
                                "fact_ids": _ids(edf)},
        "accelerators": [{"programme": (f.value or {}).get("programme"), "year": (f.value or {}).get("year"),
                          "area": (f.value or {}).get("area"), "fact_ids": _ids([f])} for f in acc],
        "peer_candidates": [{"name": f.value.get("name"), "country": f.value.get("country"),
                             "description": f.value.get("description"), "fact_ids": _ids([f])} for f in peers[:8]],
        "checks": checks,
    }


def compute(facts: list[Fact], company_name: str | None = None, country: str | None = None) -> dict[str, Any]:
    from dd import thesis
    fu = funding(facts)
    return {"funding": fu, "team_gtm": team_gtm(facts), "ai_dependency": ai_dependency(facts),
            "engineering": engineering(facts), "customers": customers(facts, company_name), "timeline": timeline(facts),
            "verification": verification(facts), "defence": defence(facts),
            "thesis": thesis.fit(facts, company_name, country, fu["rounds"])}


def all_fact_ids(signals: Any) -> set[int]:
    """Every fact id referenced anywhere inside a signals dict (for writer validation)."""
    out: set[int] = set()
    if isinstance(signals, dict):
        for k, v in signals.items():
            if (k == "fact_ids" or k.endswith("_fact_ids")) and isinstance(v, list):
                out.update(x for x in v if isinstance(x, int))
            else:
                out |= all_fact_ids(v)
    elif isinstance(signals, list):
        for v in signals:
            if isinstance(v, int) and not isinstance(v, bool):
                continue
            out |= all_fact_ids(v)
    return out
