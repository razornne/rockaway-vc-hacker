"""Dossier rendering (Markdown + standalone HTML).

Two ideas make the dossier readable for a partner:

1. **Sequential source numbers.** Facts keep their database IDs internally, but the dossier numbers the cited
   sources 1..N in reading order, like footnotes. Hovering a number shows the outlet and the quote.
2. **Evidence strength, computed by code.** Instead of the model's self-reported "confidence", every finding gets a
   label derived from WHERE its cited facts come from: an official record, a public technical artifact, two or
   more independent outlets, a single outlet, or only the company's own website. Analyst judgements (assessments)
   are labelled as such, with the evidence they rest on.
"""
from __future__ import annotations

import html
import re
from collections import Counter
from typing import Any
from urllib.parse import quote, urlparse

from dd.store import Company, Fact

OFFICIAL_HOSTS = ("ares.gov.cz", "justice.cz", "hlidacstatu.cz", "smlouvy.gov.cz", "cordis.europa.eu",
                  "ec.europa.eu", "starfos.tacr.cz", "prh.fi", "ytj.fi", "handelsregister.de", "orsr.sk",
                  "patents.google.com", "vendor-list.consensu.org", "uspto.gov", "epo.org")
TECH_HOSTS = ("github.com", "crt.sh", "web.archive.org", "openalex.org", "huggingface.co", "itunes.apple.com",
              "apps.apple.com", "play.google.com", "dns.google", "arxiv.org", "doi.org")
ATS_HOSTS = ("lever.co", "greenhouse.io", "recruitee.com", "teamtailor.com", "ashbyhq.com", "workable.com",
             "personio.de", "breezy.hr", "startupjobs.cz")
TECH_EXTRACTORS = ("techfp", "code", "ml", "apps", "history")
CHECK_TYPES = ("source_unavailable", "source_check", "search_check")

CLASS_LABELS = {
    "official": "Official record", "technical": "Public technical artifact", "press": "Independent press",
    "company": "Company's own website", "check": "Source check",
}

STRENGTH = {  # key: (short label, explanation)
    "verified": ("Verified", "backed by an official record or a public technical artifact"),
    "corroborated": ("Corroborated", "reported by two or more independent outlets"),
    "single": ("Single source", "one independent outlet; not yet corroborated"),
    "mixed": ("Partly verified", "combines independent evidence with the company's own statements"),
    "claim": ("Company claim", "only the company's own website says so — verify in diligence"),
    "view": ("Analyst view", "a judgement drawn from the cited evidence, not a fact"),
}

TYPE_LABELS = {
    "identity": "Registry: identity", "registry_incorporation": "Registry: incorporation",
    "registry_shareholder": "Registry: shareholder", "registry_capital": "Registry: registered capital",
    "registry_officer_change": "Registry: statutory body", "registry_flag": "Registry: structure",
    "filing": "Registry: filed document", "insolvency": "Insolvency register check",
    "gov_contract": "Public contract", "grant_national": "National grant", "grant_eu": "EU grant",
    "press_mention": "Press article", "funding_round": "Funding round", "web_page": "Website page",
    "product_capability": "Product capability", "pricing": "Pricing", "customer": "Customer",
    "job_post": "Job posting", "subprocessor": "Subprocessor (privacy policy)", "integration": "Integration",
    "tech_claim": "Technical claim", "team_claim": "Team claim", "tech_stack": "Technology detected",
    "saas_tool": "SaaS tool (DNS)", "subdomain": "Subdomain (certificates)", "cert_first": "First certificate",
    "github_org": "GitHub organisation", "repo": "GitHub repository", "hf_model": "Hugging Face model",
    "paper": "Research paper", "app": "Mobile app", "wayback_first": "Web archive capture",
    "patent": "Patent publication", "verification": "Independent check of a claim",
    "public_tender": "EU procurement notice (TED)", "eu_registration": "EU funding portal: participant",
    "accelerator": "Accelerator selection", "peer_company": "NATO DIANA cohort company",
    "business_model": "Business model", "revenue_claim": "Revenue / traction figure", "market_claim": "Market statement",
    "competitor": "Competitor named",
}

METHOD = [  # extractor, human name, what it reads
    ("registry", "Czech business registry", "ARES and ARES VR (identity, shareholders, capital), or.justice.cz "
                                            "Sbírka listin (filed documents), ISIR (insolvency)"),
    ("public_money", "Public money", "Hlídač státu (public contracts from registr smluv, subsidies), CORDIS"),
    ("procurement", "EU public procurement", "TED (Tenders Electronic Daily) API: notices naming the company; winner "
                                               "or tenderer by IČO, defence buyers flagged"),
    ("eu_funding", "EU funding portal", "EU Funding & Tenders portal: participant record matched by IČO, its projects "
                                        "incl. European Defence Fund"),
    ("diana", "NATO DIANA", "archived cohort pages (Wayback Machine; the live site blocks scripts): selection and "
                            "competitor candidates from the cohort list"),
    ("press", "Press", "CzechCrunch, Lupa, E15, Vestbee, tech.eu… found via search / RSS and earlier research; "
                       "an article is kept only if it mentions the company"),
    ("web", "Company website", "up to 30 pages: product, pricing, docs, customers, careers, privacy (robots.txt "
                               "respected); job boards linked from the site"),
    ("techfp", "Technical fingerprint", "HTTP headers and HTML markers, DNS records, certificate transparency "
                                        "(crt.sh) for subdomains"),
    ("code", "Public code", "GitHub organisation and repositories (only if linked from the company or matching "
                            "its domain)"),
    ("ml", "Research & models", "OpenAlex (papers by affiliation), Hugging Face (models)"),
    ("apps", "Mobile apps", "App Store (seller must match the company), Google Play if linked from the site"),
    ("history", "Web history", "Wayback Machine: first captures of the domain and key pages"),
    ("verify", "Claim verification", "company claims checked against independent sources: Google Patents (patents), "
                                     "IAB Global Vendor List (TCF), commercial register (investors named in press), "
                                     "security pages (SOC 2 / ISO attestations), news search (customers)"),
    ("llm_extract", "AI extraction","an LLM reads saved pages and articles and proposes facts; a fact is kept only "
                                     "if its quote is found in the source text and its category passes rule checks"),
]


# ----------------------------------------------------------------------------------------------------------------
def host_of(url: str | None) -> str:
    try:
        return (urlparse(url or "").netloc or "").lower().removeprefix("www.")
    except ValueError:
        return ""


def _ends(host: str, suffixes: tuple[str, ...]) -> bool:
    return any(host == s or host.endswith("." + s) for s in suffixes)


def source_class(fact: Fact, company_domain: str | None) -> str:
    if fact.type in CHECK_TYPES:
        return "check"
    host = host_of(fact.source_url)
    if _ends(host, OFFICIAL_HOSTS) or re.search(r"(?:^|\.)(?:gov|mil)(?:\.[a-z]{2})?$|(?:^|\.)europa\.eu$", host):
        return "official"
    if fact.extractor == "diana":  # NATO's own page, read from the Internet Archive
        return "official"
    if _ends(host, TECH_HOSTS) or fact.extractor in TECH_EXTRACTORS:
        return "technical"
    cd = (company_domain or "").lower().removeprefix("www.")
    if (cd and _ends(host, (cd,))) or fact.extractor == "web" or _ends(host, ATS_HOSTS):
        return "company"
    return "press"


def confirmed_claims(facts: dict[int, Fact]) -> set[str]:
    """Snippets of company claims that an independent check (dd/verify.py) confirmed."""
    out: set[str] = set()
    for f in facts.values():
        v = f.value if isinstance(f.value, dict) else {}
        if f.type == "verification" and v.get("status") == "confirmed":
            out.update(s for s in [v.get("claim_snippet"), *(v.get("claim_snippets") or [])] if s)
    return out


def item_strength(fact_ids: list[int], facts: dict[int, Fact], company_domain: str | None,
                  assessment: bool, confirmed: set[str] | frozenset = frozenset()) -> tuple[str, str]:
    """(strength key, human explanation of what the item rests on)."""
    classes = Counter()
    outlets = set()
    for fid in fact_ids:
        f = facts.get(fid)
        if not f:
            continue
        c = source_class(f, company_domain)
        if c in ("company", "press") and f.snippet and f.snippet in confirmed:
            c = "official"  # the claim itself was confirmed by an independent check
        classes[c] += 1
        if c == "press":
            outlets.add(host_of(f.source_url))
    basis = ", ".join(f"{n}× {CLASS_LABELS[c].lower()}" for c, n in classes.most_common() if c != "check")
    if len(outlets) > 1:
        basis += f" ({len(outlets)} outlets)"
    if assessment:
        return "view", basis
    independent = classes["official"] + classes["technical"] + classes["press"]
    if classes["company"] and independent:
        return "mixed", basis
    if classes["official"] or classes["technical"]:
        return "verified", basis
    if len(outlets) >= 2:
        return "corroborated", basis
    if outlets:
        return "single", basis
    return "claim", basis


class Refs:
    """Assigns 1..N to cited facts in reading order."""

    def __init__(self, facts: dict[int, Fact]):
        self.facts = facts
        self.order: list[int] = []
        self.num: dict[int, int] = {}

    def add(self, ids: list[int]) -> list[int]:
        out = []
        for fid in ids:
            if fid not in self.facts:
                continue
            if fid not in self.num:
                self.order.append(fid)
                self.num[fid] = len(self.order)
            if self.num[fid] not in out:
                out.append(self.num[fid])
        return out


def _identity(facts: dict[int, Fact]) -> dict[str, Any]:
    for f in facts.values():
        if f.type == "identity" and isinstance(f.value, dict):
            return f.value
    return {}


def _describe(f: Fact) -> str | None:
    """Readable one-liner for structured facts, where the raw snippet is not informative."""
    v = f.value if isinstance(f.value, dict) else {}
    czk = lambda x: f"{float(x):,.0f} CZK".replace(",", " ") if x not in (None, "") else ""
    if f.type == "paper":
        return " · ".join(str(x) for x in (v.get("title"), v.get("venue"), v.get("cited_by") and f"cited {v['cited_by']}×") if x)
    if f.type == "gov_contract":
        return " · ".join(x for x in (v.get("counterparty"), czk(v.get("amount_czk")), v.get("subject")) if x)
    if f.type in ("grant_national", "grant_eu"):
        return " · ".join(x for x in (v.get("title"), v.get("provider"), czk(v.get("amount_czk"))) if x)
    if f.type == "registry_shareholder":
        share = f"{v['share_pct']}%" if v.get("share_pct") else ""
        return " · ".join(x for x in (v.get("name"), share, v.get("from") and f"from {v['from']}",
                                      v.get("to") and f"to {v['to']}") if x)
    if f.type == "repo":
        return " · ".join(str(x) for x in (f.key, v.get("description"), v.get("language"),
                                           v.get("pushed_at") and f"last push {str(v['pushed_at'])[:10]}") if x)
    if f.type == "github_org":
        return f"{v.get('login')} · {v.get('public_repos')} public repos"
    if f.type == "press_mention":
        return v.get("title")
    if f.type == "job_post":
        return " · ".join(x for x in (v.get("title"), v.get("location")) if x)
    if f.type in ("identity", "registry_incorporation", "registry_capital"):
        return " · ".join(str(x) for x in (v.get("name"), v.get("legal_form"), v.get("registered") and f"registered {v['registered']}",
                                           v.get("amount_czk") and czk(v["amount_czk"])) if x)
    if f.type == "subdomain":
        return f"{f.key} (first certificate {v.get('first_seen')})"
    return None


def _snip(f: Fact, n: int = 220) -> str:
    s = _describe(f) or " ".join((f.snippet or "").split())
    if not s and isinstance(f.value, dict):
        s = str(f.value.get("summary") or f.value.get("title") or f.value.get("name") or "")
    return s[:n] + ("…" if len(s) > n else "")


def _method_rows(all_facts: dict[int, Fact]) -> list[tuple[str, str, int, list[str]]]:
    by_ex = Counter(f.extractor for f in all_facts.values() if f.type not in CHECK_TYPES)
    unavailable: dict[str, list[str]] = {}
    for f in all_facts.values():
        if f.type == "source_unavailable":
            unavailable.setdefault(f.extractor, []).append(f.key or host_of(f.source_url))
    rows = []
    for ex, name, what in METHOD:
        if by_ex.get(ex) or unavailable.get(ex):
            rows.append((name, what, by_ex.get(ex, 0), sorted(set(unavailable.get(ex, [])))))
    return rows


# ------------------------------------------------------------------- shared prep
FACTUAL_SECTIONS = ("ownership", "tech_profile")
_PAREN = re.compile(r"\s*\(([^()]*)\)")
_IDWORD = re.compile(r"\b(facts?|fact ids?|contracts?|patents?|grants?|repos?|claims?|F)\s*#?(\d{3,7})"
                     r"(?:\s*(?:,|/|and|&)\s*\d{3,7})*", re.I)


def strip_fact_ids(text: str, known: set[int]) -> str:
    """The model sometimes writes internal fact ids into prose ('(fact 7084)', 'contracts 7221, 7236'); readers
    cannot use them (the bracketed source numbers are the references), so they are removed."""
    def paren(m):
        nums = [int(n) for n in re.findall(r"\d{3,7}", m.group(1))]
        return "" if nums and all(n in known for n in nums) else m.group(0)

    def word(m):
        if int(m.group(2)) not in known:
            return m.group(0)
        return "" if m.group(1).lower() in ("f", "fact", "facts", "fact id", "fact ids") else m.group(1)
    text = _PAREN.sub(paren, text)
    text = _IDWORD.sub(word, text)
    # internal field names the model sometimes repeats from the derived signals ('rd_project', grants_czk)
    for raw, plain in INTERNAL_WORDS:
        text = re.sub(raw, plain, text, flags=re.I)
    return re.sub(r"\s+([.,;:?])", r"\1", re.sub(r"\s{2,}", " ", text)).strip()


INTERNAL_WORDS = (
    (r"['‘’\"]?\brd_project\b['‘’\"]?(?:\s+(?:contracts?\s+)?(?:kinds?|categories|category))?", "R&D project agreements"),
    (r"['‘’\"]purchase['‘’\"](?:\s+(?:contracts?\s+)?(?:kinds?|categories|category))?", "purchase contracts"),
    (r"['‘’\"]subsidy['‘’\"](?:\s+(?:contracts?\s+)?(?:kinds?|categories|category))?", "subsidy agreements"),
    (r"\bgrants_paid_czk\b", "grants paid"), (r"\bgrants_czk\b", "grants awarded"),
    (r"\bcontract_kinds\b", "contract types"),
)


INVEST_KINDS = ("thesis_fit", "business_model", "market", "competition", "investment_case")
LABELLED_SECTIONS = ("rebuild_check", "thesis_fit", "investment_case")
INVEST_NOTE = ("Inputs for the partner's memo, not a recommendation: what the evidence says about the business, the "
               "market, competitors and fit with the fund, and the case for and against.")


def _groups(sections: list[dict]) -> list[tuple[str, str | None, list[dict]]]:
    inv = [s for s in sections if s["kind"] in INVEST_KINDS]
    tech = [s for s in sections if s["kind"] not in INVEST_KINDS]
    out = []
    if any(not s["no_data"] for s in inv):
        out.append(("Investment view", INVEST_NOTE, inv))
    out.append(("Technical due diligence" if out else "Detailed findings", None, tech))
    return out

def prepare(company: Company, analysis: dict, sections: list[dict], facts: dict[int, Fact], glance) -> dict:
    refs = Refs(facts)
    confirmed = confirmed_claims(facts)
    summary = next((s for s in sections if s["kind"] == "summary"), None)
    out_sections = []
    tldr = []
    if summary and not summary["no_data"]:
        for it in summary["items"]:
            # product / stage / technology are evidence statements: label them by their sources;
            # key_risk and diligence_focus are judgements
            judgement = it.get("label") in ("key_risk", "diligence_focus")
            key, basis = item_strength(it["fact_ids"], facts, company.domain, judgement, confirmed)
            tldr.append({**it, "text": strip_fact_ids(it["text"], set(facts)), "nums": refs.add(it["fact_ids"]),
                         "strength": key, "basis": basis})
    glance_rows = [(lab, text, refs.add(ids[:6])) for lab, text, ids in glance]
    for s in sections:
        if s["kind"] == "summary":
            continue
        items = []
        for it in s["items"]:
            if s["kind"] == "thesis_fit" and it.get("label") == "stage_ticket":
                continue  # older analyses let the model compare round size with the ticket; code does it now
            # ownership and technology items state facts: label them by their sources, not by the model's own flag
            judgement = it["assessment"] and s["kind"] not in FACTUAL_SECTIONS
            key, basis = item_strength(it["fact_ids"], facts, company.domain, judgement, confirmed)
            items.append({**it, "text": strip_fact_ids(it["text"], set(facts)), "nums": refs.add(it["fact_ids"]),
                          "strength": key, "basis": basis})
        out_sections.append({**s, "items": items})
    from dd import page  # key numbers, tables and charts: registered here so their sources are numbered too
    extras = page.extras(analysis.get("signals") or {}, facts, refs, company)
    sources = []
    for fid in refs.order:
        f = facts[fid]
        sources.append({"n": refs.num[fid], "fid": fid, "cls": source_class(f, company.domain),
                        "host": host_of(f.source_url) or "source", "type": TYPE_LABELS.get(f.type, f.type.replace("_", " ")),
                        "date": f.event_date, "quote": _snip(f, 320), "url": f.source_url, "fact": f})
    return {"tldr": tldr, "glance": glance_rows, "sections": out_sections, "sources": sources, "refs": refs,
            "extras": extras,
            "identity": _identity(facts), "method": _method_rows(facts)}


# ------------------------------------------------------------------- markdown
def _md(value: str) -> str:
    escaped = html.escape(" ".join(str(value).split()), quote=False)
    return re.sub(r"([\\`*_{}\[\]()#+.!|>~-])", r"\\\1", escaped)


def _md_url(url: str | None, safe_href) -> str | None:
    u = safe_href(url)
    return quote(u, safe=":/?&=#%+-._~") if u else None


def render_markdown(company: Company, analysis: dict, p: dict, titles: dict, label_titles: dict, safe_href,
                    extraction_cost: float, value_json, fact_status, all_facts: dict[int, Fact]) -> str:
    def refs(nums):
        if not nums:
            return ""
        parts = []
        for n in nums:
            src = p["sources"][n - 1]
            u = _md_url(src["url"], safe_href)
            parts.append(f"[{n}]({u})" if u else str(n))
        return " ^" + ",".join(parts)

    ident = p["identity"]
    lines = [f"# {_md(company.name)} — due diligence brief", ""]
    meta = [x for x in (company.domain, ident.get("name"), ident.get("ico") and f"IČO {ident['ico']}",
                        company.country, analysis.get("generated_at", "")[:10]) if x]
    lines += [" · ".join(_md(m) for m in meta), ""]
    lines += ["**How to read:** numbers ^1,2 are sources listed at the end. Labels show how strong the evidence is: "
              + "; ".join(f"*{v[0]}* — {v[1]}" for v in STRENGTH.values()) + ".", ""]
    lines += ["## TL;DR", ""]
    for it in p["tldr"]:
        lines.append(f"- **{label_titles.get(it.get('label'), '')}.** {_md(it['text'])} "
                     f"*({STRENGTH[it['strength']][0]})*{refs(it['nums'])}")
    lines.append("")
    if p["glance"]:
        lines += ["## At a glance (computed by code, no LLM)", "", "| Signal | Value | Sources |", "|---|---|---|"]
        for lab, text, nums in p["glance"]:
            lines.append(f"| {_md(lab)} | {_md(text)} | {', '.join(str(n) for n in nums)} |")
        lines.append("")
    for group, note, secs in _groups(p["sections"]):
        lines += [f"# {group}", ""] + ([f"*{_md(note)}*", ""] if note else [])
        for s in secs:
            lines += [f"## {titles[s['kind']]}", ""]
            if s["no_data"]:
                lines += ["No sourced findings for this section.", ""]
                continue
            for it in s["items"]:
                tag = f"**{label_titles.get(it.get('label'))}:** " if it.get("label") else ""
                lines.append(f"- {tag}{_md(it['text'])} *({STRENGTH[it['strength']][0]})*{refs(it['nums'])}")
                for a in it["assumptions"]:
                    lines.append(f"  - Assumption: {_md(a)}")
            lines.append("")
    lines += ["## Sources", ""]
    for src in p["sources"]:
        u = _md_url(src["url"], safe_href)
        link = f"[{_md(src['host'])}]({u})" if u else _md(src["host"])
        date = f" · {_md(src['date'])}" if src["date"] else ""
        quote_txt = f" — “{_md(src['quote'])}”" if src["quote"] else ""
        lines.append(f"{src['n']}. {link} · {CLASS_LABELS[src['cls']]} · {_md(src['type'])}{date}{quote_txt}")
    lines += ["", "## How this dossier was built", "", "| Step | What it reads | Facts | Unavailable |", "|---|---|---|---|"]
    for name, what, n, unav in p["method"]:
        lines.append(f"| {_md(name)} | {_md(what)} | {n} | {_md(', '.join(unav)) if unav else '—'} |")
    lines += ["", f"Analysis: {_md(str(analysis.get('model') or 'unknown'))} (cost ${float(analysis.get('cost_usd') or 0):.4f}); "
              f"AI extraction cost ${extraction_cost:.4f}. Full fact table: CSV export.", "",
              "## Source appendix (all collected facts)", ""]
    for fid in sorted(all_facts):
        f = all_facts[fid]
        u = _md_url(f.source_url, safe_href)
        src = f"[{_md(f.source_url)}]({u})" if u else _md(f.source_url or "(no URL)")
        lines.append(f"- F{fid} · {_md(f.type)} · {fact_status(f)} · {src}")
    return "\n".join(lines).rstrip() + "\n"


# ------------------------------------------------------------------- html
CSS = """
:root{--ink:#1d2433;--muted:#667085;--line:#e4e8ee;--soft:#f6f8fb;--accent:#2f5bd3;--paper:#fff;
--v:#1f7a4d;--vb:#e6f4ec;--c:#0f6f78;--cb:#e3f3f4;--s:#8a5a00;--sb:#fdf1dc;--k:#9a3b17;--kb:#fbe9e1;--w:#5b45b0;--wb:#efebfb}
*{box-sizing:border-box}html{background:#eef1f5}body{margin:0;color:var(--ink);font:14px/1.5 Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
.page{max-width:1080px;margin:28px auto;background:var(--paper);border-radius:14px;box-shadow:0 10px 40px #1d243314;overflow:hidden}
header{padding:28px 40px 22px;background:linear-gradient(135deg,#1d2b53,#2f5bd3);color:#fff}
.eyebrow{font-size:11px;letter-spacing:.14em;text-transform:uppercase;opacity:.75;margin:0 0 6px}
h1{font-size:30px;line-height:1.15;margin:0 0 12px;font-weight:700}
.chips{display:flex;flex-wrap:wrap;gap:6px}.chip{font-size:12px;padding:3px 10px;border-radius:99px;background:#ffffff1f;border:1px solid #ffffff33}
main{padding:24px 40px 36px}
h2{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:30px 0 12px;font-weight:700}
.legend{display:flex;flex-wrap:wrap;gap:8px 14px;font-size:12px;color:var(--muted);padding:10px 14px;background:var(--soft);border-radius:10px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.badge{display:inline-block;font-size:11px;font-weight:600;padding:2px 8px;border-radius:99px;white-space:nowrap;vertical-align:1px}
.b-verified{color:var(--v);background:var(--vb)}.b-corroborated{color:var(--c);background:var(--cb)}
.b-single{color:var(--s);background:var(--sb)}.b-mixed{color:#4a5a12;background:#eef4d8}.b-claim{color:var(--k);background:var(--kb)}.b-view{color:var(--w);background:var(--wb)}
.tldr{display:grid;grid-template-columns:170px 1fr;border:1px solid var(--line);border-radius:12px;overflow:hidden}
.tldr dt{padding:12px 16px;background:var(--soft);font-weight:700;font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:#33415c;border-top:1px solid var(--line)}
.tldr dd{margin:0;padding:12px 16px;border-top:1px solid var(--line);font-size:15px}
.tldr dt:first-of-type,.tldr dd:first-of-type{border-top:0}
sup.refs{font-size:10px;margin-left:2px;white-space:nowrap}sup.refs a{color:var(--accent);text-decoration:none;font-weight:600;padding:0 1px}
sup.refs a:hover{text-decoration:underline}
table{width:100%;border-collapse:collapse}
.glance td,.glance th{padding:9px 12px;border-top:1px solid var(--line);vertical-align:top;text-align:left;font-size:13px}
.glance tr:first-child td,.glance tr:first-child th{border-top:0}.glance th{width:180px;color:#33415c;font-weight:600}
.glance .src{width:90px;color:var(--muted);font-size:12px}.glance{border:1px solid var(--line);border-radius:12px;overflow:hidden;border-collapse:separate;border-spacing:0}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}.card{border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.card h3{margin:0 0 10px;font-size:16px}.wide{grid-column:1/-1}
.item{margin:0 0 12px}.item:last-child{margin-bottom:0}.item p{margin:4px 0 0}.basis{font-size:11.5px;color:var(--muted)}
.lab{font-weight:700;color:#33415c}.assume{font-size:12px;color:var(--muted);margin:3px 0 0;padding-left:12px;border-left:2px solid var(--line)}
.rebuild{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.rebuild .item{background:var(--soft);border-radius:10px;padding:12px;margin:0}
.empty{color:var(--muted);font-size:13px}.note{color:var(--muted);font-size:13px;margin:-6px 0 14px}
ol.sources{padding-left:0;list-style:none;margin:0}ol.sources li{display:grid;grid-template-columns:34px 1fr;gap:8px;padding:9px 0;border-top:1px solid var(--line);font-size:13px}
ol.sources .n{font-weight:700;color:var(--accent)}ol.sources q{color:#3d4757}ol.sources .meta{color:var(--muted);font-size:12px}
.cls{font-size:11px;font-weight:600;padding:1px 7px;border-radius:99px;background:var(--soft);color:#33415c}
.cls-official,.cls-technical{background:var(--vb);color:var(--v)}.cls-press{background:var(--cb);color:var(--c)}.cls-company{background:var(--kb);color:var(--k)}
.method td,.method th{padding:8px 10px;border-top:1px solid var(--line);font-size:12.5px;text-align:left;vertical-align:top}.method th{color:var(--muted);font-weight:600}
details{margin-top:18px}summary{cursor:pointer;color:var(--accent);font-size:13px}
.fact{padding:6px 0;border-top:1px solid var(--line);font-size:12px;overflow-wrap:anywhere}.fact code{font-size:11px}
a{color:var(--accent)}.foot{font-size:12px;color:var(--muted);margin-top:22px}
@media(max-width:760px){header,main{padding-left:16px;padding-right:16px}.grid,.rebuild{grid-template-columns:1fr}.tldr{grid-template-columns:1fr}.tldr dd{border-top:0;padding-top:0}.page{margin:0;border-radius:0}}
@media print{html{background:#fff}.page{box-shadow:none;margin:0;max-width:none}header{-webkit-print-color-adjust:exact;print-color-adjust:exact}details{display:none}.card,.tldr{break-inside:avoid}}
"""


def render_html(company: Company, analysis: dict, p: dict, titles: dict, label_titles: dict, safe_href,
                extraction_cost: float, value_json, fact_status, all_facts: dict[int, Fact]) -> str:
    from dd import page
    return page.render(company, analysis, p, titles, label_titles, safe_href, extraction_cost, value_json,
                       fact_status, all_facts)


def render_html_v1(company: Company, analysis: dict, p: dict, titles: dict, label_titles: dict, safe_href,
                   extraction_cost: float, value_json, fact_status, all_facts: dict[int, Fact]) -> str:
    h = html.escape
    srcs = p["sources"]

    def refs(nums):
        if not nums:
            return ""
        links = []
        for n in nums:
            s = srcs[n - 1]
            tip = f"{s['host']} · {CLASS_LABELS[s['cls']]}" + (f" — {s['quote']}" if s["quote"] else "")
            links.append(f'<a href="#src-{n}" title="{h(tip, quote=True)}">{n}</a>')
        return f'<sup class="refs">[{", ".join(links)}]</sup>'

    def badge(key, basis):
        lab, expl = STRENGTH[key]
        title = expl + (f" · based on: {basis}" if basis else "")
        return f'<span class="badge b-{key}" title="{h(title, quote=True)}">{h(lab)}</span>'

    def item_html(it, show_label=True, question=False):
        lab = f'<span class="lab">{h(label_titles.get(it.get("label"), ""))}.</span> ' if show_label and it.get("label") else ""
        head = "" if question else badge(it["strength"], it["basis"]) + " "
        out = [f'<div class="item">{head}{lab}{h(it["text"])}{refs(it["nums"])}']
        if it["strength"] == "view" and it["basis"]:
            out.append(f'<div class="basis">{"Prompted by" if question else "Based on"}: {h(it["basis"])}</div>')
        for a in it["assumptions"]:
            out.append(f'<div class="assume">Assumption: {h(a)}</div>')
        out.append("</div>")
        return "".join(out)

    ident = p["identity"]
    chips = [company.domain, ident.get("name"), ident.get("ico") and f"IČO {ident['ico']}", company.country,
             f"Generated {str(analysis.get('generated_at', ''))[:10]}", f"{len(srcs)} sources cited"]
    parts = ["<!doctype html>", '<html lang="en"><head><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             f"<title>{h(company.name)} — due diligence brief</title><style>{CSS}</style></head><body>",
             '<div class="page"><header><p class="eyebrow">Due diligence brief · investment view and technical DD</p>',
             f"<h1>{h(company.name)}</h1><div class=chips>"
             + "".join(f'<span class="chip">{h(str(c))}</span>' for c in chips if c) + "</div></header><main>"]
    parts.append('<div class="legend"><b style="color:#33415c">Evidence labels:</b>'
                 + "".join(f'<span><span class="badge b-{k}">{h(v[0])}</span>{h(v[1])}</span>' for k, v in STRENGTH.items())
                 + '<span>Numbers in brackets are sources — hover to preview, click to jump.</span></div>')
    if p["tldr"]:
        parts.append('<h2>TL;DR</h2><dl class="tldr">')
        for it in p["tldr"]:
            parts.append(f'<dt>{h(label_titles.get(it.get("label"), ""))}</dt><dd>{badge(it["strength"], it["basis"])} '
                         f'{h(it["text"])}{refs(it["nums"])}</dd>')
        parts.append("</dl>")
    if p["glance"]:
        parts.append('<h2>At a glance · computed by code from sources, no LLM</h2><table class="glance">')
        for lab, text, nums in p["glance"]:
            parts.append(f"<tr><th>{h(lab)}</th><td>{h(text)}</td><td class=src>{refs(nums)}</td></tr>")
        parts.append("</table>")
    for group, note, secs in _groups(p["sections"]):
        parts.append(f'<h2>{h(group)}</h2>' + (f'<p class="note">{h(note)}</p>' if note else "") + '<div class="grid">')
        for s in secs:
            wide = " wide" if s["kind"] in ("rebuild_check", "investment_case", "competition") else ""
            parts.append(f'<section class="card{wide}"><h3>{h(titles[s["kind"]])}</h3>')
            if s["no_data"]:
                parts.append('<p class="empty">No sourced findings for this section.</p></section>')
                continue
            if s["kind"] == "rebuild_check":
                parts.append('<div class="rebuild">' + "".join(item_html(it) for it in s["items"]) + "</div>")
            else:
                parts.append("".join(item_html(it, show_label=s["kind"] in LABELLED_SECTIONS,
                                               question=s["kind"] == "questions") for it in s["items"]))
            parts.append("</section>")
        parts.append("</div>")
    parts.append('<h2>Sources</h2><ol class="sources">')
    for s in srcs:
        url = safe_href(s["url"])
        link = f'<a href="{h(url, quote=True)}" rel="noopener noreferrer" target="_blank">{h(s["host"])} ↗</a>' if url else h(s["host"])
        date = f" · {h(s['date'])}" if s["date"] else ""
        q = f"<br><q>{h(s['quote'])}</q>" if s["quote"] else ""
        parts.append(f'<li id="src-{s["n"]}"><span class="n">{s["n"]}</span><div>{link} '
                     f'<span class="cls cls-{s["cls"]}">{h(CLASS_LABELS[s["cls"]])}</span> '
                     f'<span class="meta">{h(s["type"])}{date}</span>{q}</div></li>')
    parts.append("</ol>")
    parts.append('<h2>How this dossier was built</h2><table class="method"><tr><th>Step</th><th>What it reads</th>'
                 "<th>Facts</th><th>Unavailable this run</th></tr>")
    for name, what, n, unav in p["method"]:
        parts.append(f"<tr><td><b>{h(name)}</b></td><td>{h(what)}</td><td>{n}</td><td>{h(', '.join(unav)) if unav else '—'}</td></tr>")
    parts.append("</table>")
    parts.append(f'<p class="foot">Analysis model {h(str(analysis.get("model") or "unknown"))} · analysis cost '
                 f'${float(analysis.get("cost_usd") or 0):.4f} · AI extraction cost ${extraction_cost:.4f}. Structured sources '
                 "(registries, DNS, GitHub…) are parsed by code; the LLM only extracts quoted facts from text and writes "
                 "the findings above, each tied to cited sources. This is an outside-in assessment from public data and "
                 "does not replace access to code, data and contracts.</p>")
    parts.append(f"<details><summary>Source appendix — all {len(all_facts)} collected facts, incl. checks and "
                 "unavailable sources</summary>")
    for fid in sorted(all_facts):
        f = all_facts[fid]
        url = safe_href(f.source_url)
        src = f'<a href="{h(url, quote=True)}" rel="noopener noreferrer">{h(f.source_url)}</a>' if url else h(f.source_url or "(no URL)")
        parts.append(f'<div class="fact" id="fact-{fid}"><b>F{fid}</b> · {h(f.type)} · {h(fact_status(f))} · {src}'
                     f'<br><code>{h(value_json(f.value))}</code></div>')
    parts.append("</details></main></div></body></html>")
    return "\n".join(parts)
