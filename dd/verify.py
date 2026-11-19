"""Verification: check what the company claims against independent sources.

Runs after collection and extraction (it needs the company's claims). Produces:
  - `patent` facts (Google Patents, by assignee);
  - `verification` facts: one per check, value = {check, status, claim_snippet, detail, ...}.

Statuses:
  confirmed      — an independent source supports the claim
  partly         — supports part of it (e.g. patent APPLICATIONS exist, no granted patent)
  contradicted   — an independent source disagrees (e.g. "owns patents" but only applications are published)
  not_found      — the independent source was checked and has no record (absence in one source ≠ claim is false)
  not_checkable  — no public source to check against was found

Everything is deterministic code; no LLM. Network failures produce `source_unavailable`, never exceptions.
"""
from __future__ import annotations

import html as htmllib
import json
import re
import time
import unicodedata
from pathlib import Path
from urllib.parse import quote

from dd.collectors.base import Context
from dd.store import Company, Fact

NAME = "verify"
GVL_URL = "https://vendor-list.consensu.org/v3/vendor-list.json"
PATENTS_XHR = "https://patents.google.com/xhr/query?url={q}&exp="
TRUST_VENDORS = ("vanta", "drata", "safebase", "secureframe", "sprinto", "trustcloud", "whistic", "conveyor",
                 "oneleet", "thoropass", "a-lign", "prescient", "schellman", "johanson", "insight assurance")
LEGAL_SUFFIX = re.compile(r"\b(s\.?\s?r\.?\s?o\.?|a\.?\s?s\.?|se|inc\.?|ltd\.?|llc|gmbh|b\.?v\.?|cz|ai|labs?|group)\b", re.I)


def fold(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s or "") if not unicodedata.combining(c)).lower()


def name_token(company: Company, facts: list[Fact]) -> str:
    """Distinctive lowercase name token, e.g. 'filuta' from 'Filuta AI' / 'Filuta AI CZ s.r.o.'."""
    base = LEGAL_SUFFIX.sub(" ", company.name or "")
    words = [w for w in re.findall(r"[A-Za-z0-9]+", fold(base)) if len(w) > 2]
    return words[0] if words else fold(company.id)


def _ambiguous(company: Company) -> bool:
    return bool(company.hints.get("context_terms"))


def _core(name: str) -> str:
    """'Filuta AI Inc.' -> 'filuta', 'Vermeer Manufacturing Company' -> 'vermeer manufacturing company'."""
    return " ".join(re.findall(r"[a-z0-9]+", fold(LEGAL_SUFFIX.sub(" ", name or ""))))


def assignee_matches(assignee: str, company: Company, token: str) -> bool:
    """Name-collision guard. The assignee must START with the company token ('Valpas Enterprises Oy' yes;
    'Juha Valpas Viitanen', 'V. P. VALPAS VALVOLE S.r.l.' no). For ambiguous names (Vermeer the drone company vs
    Vermeer Manufacturing) only the exact name or a known legal name counts."""
    a = fold(assignee)
    if not re.match(re.escape(token) + r"(?![a-z0-9])", a):
        return False
    if not _ambiguous(company):
        return True
    allowed = {_core(company.name), *(_core(n) for n in company.hints.get("legal_names") or [])}
    return _core(assignee) in allowed


def _about(company: Company, text: str) -> bool:
    from dd.collectors.press import about_company
    return about_company(text, company)


def _fact(company: Company, ftype: str, key: str, value: dict, url: str, snippet: str | None = None,
          date: str | None = None) -> Fact:
    return Fact(company_id=company.id, type=ftype, key=key, value=value, source_url=url, snippet=snippet,
                event_date=date, date_precision="day" if date and len(date) == 10 else None,
                extractor=NAME, confidence="high")


def _unavailable(company: Company, source: str, url: str, reason: str) -> Fact:
    return Fact(company_id=company.id, type="source_unavailable", key=source, value={"reason": reason[:300]},
                source_url=url, extractor=NAME, confidence="high")


def _claims(facts: list[Fact], pattern: str) -> list[Fact]:
    rx = re.compile(pattern, re.I)
    return [f for f in facts if f.type in ("tech_claim", "product_capability", "team_claim", "customer", "pricing")
            and rx.search(f"{f.snippet or ''} {(f.value or {}).get('summary', '') if isinstance(f.value, dict) else ''}")]


# ----------------------------------------------------------------------------------------------- patents
def _clean(s: str) -> str:
    return htmllib.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def check_patents(company: Company, facts: list[Fact], ctx: Context) -> list[Fact]:
    token = name_token(company, facts)
    q = quote(f"assignee={token}&oq=assignee:{token}", safe="")
    url = PATENTS_XHR.format(q=q)
    human_url = f"https://patents.google.com/?assignee={quote(token)}"
    r = ctx.http.get(url, company_id=company.id, kind="verify_patents")
    if r.status in (429, 503):  # Google Patents rate-limits bursts: one polite retry
        time.sleep(8)
        r = ctx.http.get(url, company_id=company.id, kind="verify_patents", use_cache=False)
    out: list[Fact] = []
    pubs = []
    if not r.ok:
        # no answer is not "no patents": report the outage and make no claim about the claims
        return [_unavailable(company, "google_patents", human_url, f"HTTP {r.status}")]
    else:
        try:
            data = r.json()
            for cl in data.get("results", {}).get("cluster", []):
                for res in cl.get("result", []):
                    p = res.get("patent", {})
                    assignee = _clean(p.get("assignee", ""))
                    if not assignee_matches(assignee, company, token):
                        continue  # name collision guard
                    num = p.get("publication_number", "")
                    pubs.append({"number": num, "title": _clean(p.get("title", "")), "assignee": assignee,
                                 "priority_date": p.get("priority_date"), "publication_date": p.get("publication_date"),
                                 "granted": bool(re.search(r"B\d?$", num)) or bool(p.get("grant_date"))})
        except (ValueError, AttributeError) as e:
            out.append(_unavailable(company, "google_patents", human_url, f"unparseable response: {e}"))
    seen = set()
    for p in pubs:
        if p["number"] in seen:
            continue
        seen.add(p["number"])
        out.append(_fact(company, "patent", p["number"], p, f"https://patents.google.com/patent/{p['number']}",
                         snippet=f"{p['number']} · {p['title']} · {p['assignee']}", date=p["publication_date"] and
                         f"{p['publication_date'][:4]}-{p['publication_date'][4:6]}-{p['publication_date'][6:8]}"
                         if p.get("publication_date") and len(p["publication_date"]) == 8 else None))
    claims = _claims(facts, r"patent")
    granted = [p for p in pubs if p["granted"]]
    us_apps = sorted({p["number"] for p in pubs if p["number"].startswith("US") and not p["granted"]})
    grouped: dict[str, dict] = {}
    for c in claims:
        text = fold(c.snippet or "")
        owns = re.search(r"\b(own|owns|vlastni|granted|patented|udelen|patentovan)", text) and not re.search(r"pending|applic|prihlask", text)
        if not pubs:
            status, detail = "not_found", (
                f"No publication with assignee '{company.name}' (or a listed legal name) on Google Patents; "
                f"other assignees sharing the name were excluded." if _ambiguous(company)
                else f"No publication with assignee starting with '{token}' on Google Patents.")
        elif owns and not granted:
            status = "contradicted"
            detail = (f"Claim implies owned/granted patents, but only published applications were found "
                      f"({len(pubs)} publications, 0 granted): {', '.join(us_apps[:3]) or pubs[0]['number']}.")
        elif granted:
            status, detail = "confirmed", f"{len(granted)} granted patent(s) found, e.g. {granted[0]['number']}."
        else:
            status = "partly" if not re.search(r"pending|applic|prihlask", text) else "confirmed"
            detail = f"{len(pubs)} published patent applications (none granted yet), e.g. {', '.join(us_apps[:2]) or pubs[0]['number']}."
        g = grouped.setdefault(status, {"check": "patents", "status": status, "claim_snippet": c.snippet,
                                        "claim_url": c.source_url, "claim_snippets": [], "detail": detail,
                                        "publications": [p["number"] for p in pubs][:10]})
        if c.snippet and c.snippet not in g["claim_snippets"]:
            g["claim_snippets"].append(c.snippet)
    for status, g in grouped.items():
        out.append(_fact(company, "verification", f"patents:{status}", g, human_url, snippet=g["detail"]))
    return out


# ----------------------------------------------------------------------------------------------- IAB TCF
def check_tcf(company: Company, facts: list[Fact], ctx: Context) -> list[Fact]:
    claims = _claims(facts, r"\bTCF\b|transparency\s*(?:&|and)\s*consent\s+framework|\bIAB\b")
    if not claims:
        return []
    r = ctx.http.get(GVL_URL)  # global file, cached; not company-scoped
    if not r.ok:
        return [_unavailable(company, "iab_gvl", GVL_URL, f"HTTP {r.status}")]
    try:
        gvl = r.json()
    except ValueError as e:
        return [_unavailable(company, "iab_gvl", GVL_URL, f"unparseable: {e}")]
    token = name_token(company, facts)
    hits = [(k, v.get("name")) for k, v in gvl.get("vendors", {}).items() if token in fold(v.get("name", ""))]
    version = gvl.get("vendorListVersion")
    out = []
    for c in claims:
        if hits:
            status, detail = "confirmed", f"Registered TCF vendor: {hits[0][1]} (vendor id {hits[0][0]}, list v{version})."
        else:
            status = "not_found"
            detail = (f"'{token}' is not in the IAB Global Vendor List v{version} ({len(gvl.get('vendors', {}))} vendors). "
                      "The claim may mean the platform integrates a TCF-compliant consent tool rather than being a "
                      "registered vendor — ask.")
        out.append(_fact(company, "verification", f"iab_tcf:{c.id}", {
            "check": "iab_tcf", "status": status, "claim_snippet": c.snippet, "claim_url": c.source_url,
            "detail": detail, "gvl_version": version}, GVL_URL, snippet=detail))
    return out


# ----------------------------------------------------------------------------------------------- funding vs registry
def _inv_key(s: str) -> str:
    s = re.sub(r"\b(vc|ventures?|capital|fund|scsp|sicav|raif|s\.?r\.?o\.?|a\.?s\.?|se|osoba rizikoveho kapitalu)\b", " ", fold(s))
    return re.sub(r"[^a-z0-9]", "", s)


def check_funding_registry(company: Company, facts: list[Fact], ctx: Context) -> list[Fact]:
    rounds = [f for f in facts if f.type == "funding_round" and isinstance(f.value, dict) and f.value.get("investors")]
    holders = [f for f in facts if f.type == "registry_shareholder" and isinstance(f.value, dict)]
    if not rounds or not holders:
        return []
    out = []
    for h in holders:
        hk = _inv_key(h.value.get("name", ""))
        if len(hk) < 4:
            continue
        matched = [(rf, inv) for rf in rounds for inv in rf.value.get("investors", [])
                   if len(_inv_key(inv)) >= 4 and (_inv_key(inv) in hk or hk in _inv_key(inv))]
        if not matched:
            continue
        rf, inv = matched[0]
        outlets = sorted({re.sub(r"^https?://(www\.)?", "", m[0].source_url).split("/")[0] for m in matched})
        detail = (f"Press ({', '.join(outlets)}) names {inv} as an investor; the commercial register lists "
                  f"{h.value.get('name')} as a shareholder from {h.value.get('from')}"
                  + (f" ({h.value['share_pct']}%)" if h.value.get("share_pct") else "") + ".")
        out.append(_fact(company, "verification", f"funding_registry:{hk}", {
            "check": "funding_vs_registry", "status": "confirmed", "claim_snippet": rf.snippet,
            "claim_snippets": sorted({m[0].snippet for m in matched if m[0].snippet}),
            "claim_url": rf.source_url, "detail": detail, "investor": inv,
            "registry_holder": h.value.get("name"), "registry_from": h.value.get("from")},
            h.source_url, snippet=detail, date=h.value.get("from")))
    return out


# ----------------------------------------------------------------------------------------------- security attestations
def check_security(company: Company, facts: list[Fact], ctx: Context) -> list[Fact]:
    claims = _claims(facts, r"SOC\s?2|ISO\s?27001|ISO/IEC\s?27001")
    if not claims:
        return []
    found = []
    for d in ctx.store.source_docs(company.id, ["page"]):
        if not d["text_path"] or not re.search(r"security|trust|compliance|soc|privacy", d["url"], re.I):
            continue
        try:
            text = fold(Path(d["text_path"]).read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        for v in TRUST_VENDORS:
            if re.search(rf"\b{re.escape(v)}\b", text):
                found.append((v, d["url"]))
    trust_subs = [f.key for f in facts if f.type == "subdomain" and str(f.key or "").split(".")[0] in ("trust", "security", "compliance")]
    c = claims[0]
    if found or trust_subs:
        status = "partly"
        detail = ("Public attestation pointer found: "
                  + ", ".join([f"{v} on {u}" for v, u in found[:2]] + [f"subdomain {s}" for s in trust_subs[:2]])
                  + ". The report itself is shared under NDA — request it.")
        url = found[0][1] if found else f"https://{trust_subs[0]}"
    else:
        status = "not_checkable"
        detail = ("No trust portal, auditor or compliance-platform reference found on the collected security pages "
                  "or subdomains. SOC 2 reports are private; the claim can only be verified by requesting the report.")
        url = c.source_url
    return [_fact(company, "verification", "security", {
        "check": "security_attestation", "status": status, "claim_snippet": c.snippet,
        "claim_snippets": sorted({x.snippet for x in claims if x.snippet}), "claim_url": c.source_url,
        "detail": detail}, url, snippet=detail)]


# ----------------------------------------------------------------------------------------------- customers
def check_customers(company: Company, facts: list[Fact], ctx: Context) -> list[Fact]:
    from dd import search
    from dd.signals import customers
    names = customers(facts, company.name)["named_customers"]
    if not names:
        return []
    token = name_token(company, facts)
    domain = (company.domain or "").lower()
    out = []
    keyed = [p for p in search.available(ctx) if p != "keyless"]
    for cust in names[:3]:
        q = f'"{cust}" "{company.name}"'
        rows = []
        for p in (keyed or [None]):
            try:
                res = search.search_detailed(q, ctx, provider=p, n=8, company_id=company.id)
                rows += res.get("rows", []) if isinstance(res, dict) else res
            except Exception as e:  # search must never break verification
                out.append(_unavailable(company, f"customer_search:{p}:{cust}", "search", str(e)))
        ctok = [w for w in re.findall(r"[a-z0-9]+", fold(cust)) if len(w) > 2][:2]
        from dd.collectors.press import AGGREGATOR_HOSTS
        hits = [x for x in rows if domain not in (x.get("url") or "").lower()
                and re.sub(r"^https?://(www\.)?", "", (x.get("url") or "").lower()).split("/")[0] not in AGGREGATOR_HOSTS
                and token in fold(f"{x.get('title')} {x.get('snippet')}")
                and _about(company, f"{x.get('title')} {x.get('snippet')} {x.get('url')}")
                and all(w in fold(f"{x.get('title')} {x.get('snippet')}") for w in ctok)]
        claim = next((f for f in facts if f.type == "customer" and cust.lower()[:6] in str((f.value or {}).get("name", "")).lower()), None)
        if hits:
            h = hits[0]
            out.append(_fact(company, "verification", f"customer:{cust}", {
                "check": "customer_corroboration", "status": "confirmed", "customer": cust,
                "claim_snippet": claim.snippet if claim else None, "detail": f"Independent page mentions both: {h.get('title')}",
                "providers": keyed or ["keyless"]}, h["url"], snippet=(h.get("snippet") or h.get("title") or "")[:300]))
        else:
            out.append(_fact(company, "verification", f"customer:{cust}", {
                "check": "customer_corroboration", "status": "not_found", "customer": cust,
                "claim_snippet": claim.snippet if claim else None,
                "detail": ("No independent page mentioning both found"
                           + ("" if keyed else " (news search only — add a web search API key for broader coverage)")),
                "providers": keyed or ["keyless"]}, claim.source_url if claim else f"https://{domain}",
                snippet=None))
    return out


GOV_HOST = re.compile(r"(?:^|\.)(?:gov|mil)(?:\.[a-z]{2})?$|(?:^|\.)gov\.cz$|(?:^|\.)europa\.eu$|(?:^|\.)justice\.cz$|"
                      r"(?:^|\.)smlouvy\.gov\.cz$|(?:^|\.)nen\.nipez\.cz$|(?:^|\.)ted\.europa\.eu$|(?:^|\.)k12\.[a-z]{2}\.us$")


def check_public_sector(company: Company, facts: list[Fact], ctx: Context) -> list[Fact]:
    """Is the company listed on a government site (vendor registry, contract, procurement)? Independent and official."""
    from dd import search
    keyed = [p for p in search.available(ctx) if p != "keyless"]
    if not keyed:
        return []
    token = name_token(company, facts)
    domain = (company.domain or "").lower()
    q = f'"{company.name}" vendor contract government procurement'
    hits = {}
    for p in keyed:
        try:
            res = search.search_detailed(q, ctx, provider=p, n=10, company_id=company.id)
        except Exception as e:
            return [_unavailable(company, f"public_sector_search:{p}", "search", str(e))]
        for r in res.get("rows", []):
            url = r.get("url") or ""
            host = re.sub(r"^https?://(www\.)?", "", url).split("/")[0].lower()
            text = fold(f"{r.get('title')} {r.get('snippet')} {url}")
            if (GOV_HOST.search(host) and token in text and domain not in url
                    and _about(company, f"{r.get('title')} {r.get('snippet')} {url}")):
                hits.setdefault(url, r)
    out = []
    for url, r in list(hits.items())[:3]:
        detail = f"Listed on a government site: {r.get('title') or url}"
        out.append(_fact(company, "verification", f"public_sector:{url[:80]}", {
            "check": "public_sector_vendor", "status": "confirmed", "detail": detail,
            "claim_snippet": None}, url, snippet=(r.get("snippet") or detail)[:300]))
    return out


CHECKS = (check_patents, check_tcf, check_funding_registry, check_security, check_customers, check_public_sector)


def verify_company(company: Company, ctx: Context) -> list[Fact]:
    facts = ctx.store.facts(company.id)
    out: list[Fact] = []
    for check in CHECKS:
        try:
            out += check(company, facts, ctx)
        except Exception as e:  # one failing check must not lose the others
            out.append(_unavailable(company, check.__name__, company.domain or company.id, f"crash: {e}"))
    ctx.store.replace_facts(company.id, NAME, out)
    return out
