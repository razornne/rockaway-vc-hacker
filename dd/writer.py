"""Render the latest fact-linked dossier analysis as Markdown, standalone HTML and CSV."""
from __future__ import annotations

import csv
import html
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

from dd.store import Company, Fact, Store

SECTION_TITLES = {
    "summary": "TL;DR",
    "thesis_fit": "Fit with the Rockaway thesis",
    "business_model": "Business model",
    "market": "Market",
    "competition": "Competition",
    "investment_case": "Case for and against",
    "ownership": "Ownership and capital",
    "tech_profile": "Technology profile",
    "rebuild_check": "What could be rebuilt, and what cannot be judged from outside",
    "risk_flags": "Risks and caveats",
    "questions": "Questions for founders",
}
SECTION_ORDER = tuple(SECTION_TITLES)
INVEST_SECTIONS = ("thesis_fit", "business_model", "market", "competition", "investment_case")
CONFIDENCE_LEVELS = {"high", "medium", "low"}
LABEL_TITLES = {
    "product": "Product", "stage_traction": "Stage & traction", "technology_moat": "Technology & moat",
    "key_risk": "Key risk", "diligence_focus": "Diligence focus",
    "commodity": "Commodity", "hard": "Hard to copy", "verdict": "Verdict",
    "replicable": "Replicable with off-the-shelf parts", "evidenced_edge": "Edge supported by public evidence",
    "not_assessable": "Cannot be judged from outside",
    "sector": "Sector", "stage_ticket": "Stage & ticket", "portfolio_overlap": "Portfolio overlap",
    "for": "For", "against": "Against", "must_be_true": "Must be true",
}


def _czk(x: float) -> str:
    return f"{x / 1e6:.1f}M CZK" if x >= 1e6 else f"{x:,.0f} CZK"


def glance_rows(signals: dict | None) -> list[tuple[str, str, list[int]]]:
    """Plain-language rows of the code-computed signals: (label, text, fact_ids)."""
    if not isinstance(signals, dict):
        return []
    rows: list[tuple[str, str, list[int]]] = []
    fu = signals.get("funding") or {}
    rounds = fu.get("rounds") or []
    if rounds:
        parts, ids = [], []
        for r in rounds[:5]:
            bits = [r.get("date") or "date n/a", r.get("round"), r.get("amount"),
                    ", ".join(r.get("investors") or [])[:90] or None,
                    f"{r['reports']} reports" if r.get("reports", 1) > 1 else None]
            parts.append(" · ".join(str(b) for b in bits if b))
            ids += r.get("fact_ids") or []
        rows.append(("Funding (press)", "; ".join(parts), ids))
    inv = fu.get("registry_investors") or []
    if inv:
        rows.append(("Investors in registry", "; ".join(
            f"{i.get('name')} (from {i.get('from')}{', ' + str(i['share_pct']) + '%' if i.get('share_pct') else ''})"
            for i in inv[:6]), [x for i in inv for x in i.get("fact_ids", [])]))
    pm = fu.get("public_money") or {}
    if pm.get("contracts") or pm.get("grants"):
        def money(n: int, word: str, czk: float, unpriced: int) -> str:
            if not n:
                return ""
            amount = _czk(czk) if czk else "amount not published"
            if czk and unpriced:
                amount += f" + {unpriced} without published amount"
            return f"{n} {word}(s), {amount}"
        kinds = pm.get("contract_kinds") or {}
        # a total over all contracts would add research-project budgets to purchases: show the split instead
        contracts = (f"{pm['contracts']} contract(s) in the contract register" if kinds and pm.get("contracts") else
                     money(pm.get("contracts", 0), "contract", pm.get("contracts_czk") or 0, pm.get("contracts_unpriced", 0)))
        grants = money(pm.get("grants", 0), "grant project", pm.get("grants_czk") or 0, pm.get("grants_unpriced", 0))
        if grants and pm.get("grants_czk"):
            grants = grants.replace(", ", " awarded ", 1) + (
                f", {_czk(pm['grants_paid_czk'])} paid so far" if pm.get("grants_paid_czk") else "")
        parts = [contracts, grants]
        text = "; ".join(x for x in parts if x)
        if kinds:
            names = (("purchase", "purchase(s) by public buyers"), ("rd_project", "R&D project agreement(s), amounts are "
                     "project budgets, not revenue"), ("subsidy", "subsidy agreement(s)"), ("loan", "device loan(s)"),
                     ("other", "other"))
            text += " · by kind: " + "; ".join(
                f"{kinds[k]['count']} {label}" + (f" ({_czk(kinds[k]['czk'])})" if kinds[k].get("czk") and k != "rd_project" else "")
                for k, label in names if k in kinds)
        if pm.get("counterparties"):
            text += " · counterparties: " + ", ".join(pm["counterparties"])
        rows.append(("Public money", text, pm.get("fact_ids") or []))
    de = signals.get("defence") or {}
    tw, edf, acc = de.get("tenders_won") or {}, de.get("eu_defence_projects") or {}, de.get("accelerators") or []
    if tw.get("count") or edf.get("count") or acc:
        bits, ids = [], []
        if tw.get("count"):
            val = ", ".join(_czk(v) if c == "CZK" else f"{v:,.0f} {c}" for c, v in (tw.get("value_by_currency") or {}).items() if v)
            bits.append(f"{tw['count']} EU-procurement award(s)" + (f", {tw['defence_buyer']} from defence buyers" if tw.get("defence_buyer") else "")
                        + (f" ({val})" if val else "") + (f": {', '.join(tw.get('buyers') or [])}" if tw.get("buyers") else ""))
            ids += tw.get("fact_ids") or []
        if edf.get("count"):
            bits.append(f"{edf['count']} EU defence project(s) ({', '.join(edf.get('programmes') or [])})")
            ids += edf.get("fact_ids") or []
        for a in acc:
            bits.append(f"{a.get('programme')} {a.get('year')}" + (f" ({a['area']})" if a.get("area") else ""))
            ids += a.get("fact_ids") or []
        rows.append(("Defence signals", "; ".join(bits), ids))
    th = signals.get("thesis") or {}
    if th.get("sectors") or th.get("portfolio_overlap"):
        secs = [f"{x['sector']} ({x['evidence']} facts" + (", incl. structured defence evidence" if x.get("structured_evidence_fact_ids") else "") + ")"
                for x in th.get("sectors") or []]
        text = "sectors: " + ("; ".join(secs) if secs else "none evidenced")
        geo = th.get("geography") or {}
        if geo.get("country"):
            text += f" · geography: {geo['country']}" + (" (core region)" if geo.get("in_core_region") else "")
        ov = th.get("portfolio_overlap") or []
        if ov:
            text += " · overlaps portfolio: " + ", ".join(f"{p['name']} ({', '.join(p['shared_terms'][:3])})" for p in ov[:3])
        rows.append(("Thesis fit (Rockaway)", text, [i for x in th.get("sectors") or [] for i in x.get("fact_ids", [])[:2]]))
    tg = signals.get("team_gtm") or {}
    if tg.get("open_roles"):
        by = tg.get("by_function") or {}
        mix = ", ".join(f"{k.replace('_', ' ')} {v['count']}" for k, v in sorted(by.items(), key=lambda kv: -kv[1]["count"]))
        founding = (tg.get("founding_roles") or {}).get("titles") or []
        text = f"{tg['open_roles']} open roles: {mix}" + (f"; founding roles: {', '.join(founding)}" if founding else "")
        if tg.get("locations"):
            text += "; " + ", ".join(tg["locations"])
        rows.append(("Hiring", text, [x for v in by.values() for x in v.get("fact_ids", [])][:8]))
    ai = signals.get("ai_dependency") or {}
    used = ai.get("llm_vendors_used") or ai.get("third_party_llm_vendors") or {}
    integrated = ai.get("llm_vendors_integrated") or {}
    own = ai.get("own_model_evidence") or {}
    own_bits = [f"{len(own.get(k) or [])} {n}" for k, n in
                (("papers", "papers"), ("hf_models", "verified HF models"), ("ml_roles", "ML roles"), ("claims", "own-model claims"))]
    if used or integrated or any(own.get(k) for k in own):
        bits = [f"relies on (subprocessor / own claims): {', '.join(used)}" if used else
                "no LLM vendor named as subprocessor or in own tech claims"]
        if integrated:
            bits.append(f"integrates with customers' {', '.join(integrated)} (not a dependency)")
        bits.append("own-model evidence: " + ", ".join(own_bits))
        rows.append(("AI dependency", "; ".join(bits),
                     [x for v in used.values() for x in v][:3] + [x for v in integrated.values() for x in v][:2]
                     + [x for k in own for x in own[k]][:3]))
    en = signals.get("engineering") or {}
    if en.get("public_repos") or en.get("subdomains") or en.get("docs_pages") or en.get("stack"):
        bits = []
        if en.get("public_repos"):
            bits.append(f"{en['public_repos']} public repos ({en.get('stars', 0)}★, last push {en.get('last_push') or 'n/a'})")
        if en.get("product_surfaces"):
            bits.append("product surfaces: " + ", ".join(en["product_surfaces"][:6]))
        elif en.get("subdomains"):
            bits.append(f"{en['subdomains']} subdomains")
        if en.get("docs_pages"):
            bits.append(f"{en['docs_pages']} docs pages")
        if en.get("stack"):
            bits.append("stack: " + ", ".join(en["stack"][:5]))
        rows.append(("Engineering footprint", "; ".join(bits),
                     (en.get("repo_fact_ids") or [])[:3] + (en.get("surface_fact_ids") or [])[:3] + (en.get("docs_fact_ids") or [])[:2]))
    cu = signals.get("customers") or {}
    if cu.get("named_customers") or cu.get("pricing_public") or cu.get("apps"):
        bits = []
        if cu.get("named_customers"):
            bits.append(f"{len(cu['named_customers'])} named: " + ", ".join(cu["named_customers"][:5]))
        bits.append("public pricing: " + ("yes" if cu.get("pricing_public") else "not found"))
        if cu.get("apps"):
            bits.append(f"{cu['apps']} mobile app(s)")
        rows.append(("Customers", "; ".join(bits), (cu.get("customer_fact_ids") or [])[:4] + (cu.get("pricing_fact_ids") or [])[:1]))
    checks = [c for c in (signals.get("verification") or []) if c.get("status") != "info"]
    if checks:
        names = {"patents": "Patents", "iab_tcf": "IAB TCF", "funding_vs_registry": "Investors vs registry",
                 "security_attestation": "SOC 2 / ISO", "customer_corroboration": "Customer",
                 "public_sector_vendor": "Government listing"}
        grouped: dict[tuple, list] = {}
        for c in checks:
            grouped.setdefault((c["check"], c["status"]), []).append(c)
        bits, ids = [], []
        for (check, status), cs in grouped.items():
            label = names.get(check, check)
            subj = ", ".join(sorted({c["subject"] for c in cs if c.get("subject")}))
            bits.append(f"{label}{' (' + subj + ')' if subj else ''}: {status.replace('_', ' ')}")
            ids += [x for c in cs for x in c.get("fact_ids", [])][:2]
        rows.append(("Claims checked", "; ".join(bits), ids[:6]))
    tl = signals.get("timeline") or {}
    if tl.get("incorporated") or tl.get("first_press"):
        bits = []
        if tl.get("incorporated"):
            bits.append(f"Czech entity registered {tl['incorporated']}")
        if tl.get("first_press"):
            bits.append(f"first press {tl['first_press']} ({tl.get('press_articles', 0)} articles collected)")
        rows.append(("Timeline", "; ".join(bits), (tl.get("incorporated_fact_ids") or []) + (tl.get("first_press_fact_ids") or [])))
    return rows
FACT_CSV_FIELDS = ("id", "company_id", "type", "key", "value_json", "event_date", "date_precision",
                   "source_url", "snippet", "extractor", "confidence")


def _safe_href(value: str | None) -> str | None:
    """Allow only absolute HTTP(S) links; all other URLs render as plain escaped text."""
    if not isinstance(value, str):
        return None
    try:
        parsed = urlparse(value.strip())
    except ValueError:
        return None
    if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
        return None
    return value.strip()


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "-", value).strip("-_")[:80]
    return slug or "company"


def _markdown_text(value: str) -> str:
    """Escape raw HTML and Markdown syntax so generated analysis stays inert in .md viewers."""
    escaped = html.escape(" ".join(value.split()), quote=False)
    return re.sub(r"([\\`*_{}\[\]()#+.!|>~-])", r"\\\1", escaped)


def _value_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)


def _fact_status(fact: Fact) -> str:
    if fact.type == "source_unavailable":
        return "Unavailable"
    if fact.type in {"source_check", "search_check"}:
        value = fact.value if isinstance(fact.value, dict) else {}
        status = str(value.get("status") or value.get("outcome") or "").lower()
        count = value.get("result_count", value.get("count"))
        if status in {"empty", "no_results", "checked_empty", "zero_results"} or count == 0:
            return "Checked · no results"
        return "Checked"
    if isinstance(fact.value, dict) and fact.value.get("identity_unverified"):
        return "Identity unverified"
    if fact.confidence in CONFIDENCE_LEVELS and fact.confidence != "high":
        return f"{fact.confidence.title()} confidence"
    return "Sourced"


def _analysis_error(message: str) -> ValueError:
    return ValueError(f"cannot render dossier: {message}")


def _load_and_validate(store: Store, company: Company) -> tuple[dict, list[Fact], dict[int, Fact]]:
    analysis = store.latest_analysis(company.id, "dossier")
    if not isinstance(analysis, dict):
        raise _analysis_error("no latest dossier analysis exists")
    if analysis.get("company_id") != company.id:
        raise _analysis_error("analysis company_id does not match the requested company")
    sections = analysis.get("sections")
    if not isinstance(sections, list):
        raise _analysis_error("analysis sections must be a list")

    if not any(isinstance(s, dict) and s.get("kind") == "summary" for s in sections):
        sections = [{"kind": "summary", "items": [], "no_data": True}] + sections  # pre-v3 analyses
    by_kind = {}
    for section in sections:
        if not isinstance(section, dict):
            raise _analysis_error("section must be an object")
        kind = section.get("kind")
        if kind not in SECTION_TITLES or kind in by_kind:
            raise _analysis_error(f"unknown or duplicate section kind: {kind!r}")
        if not isinstance(section.get("no_data"), bool):
            raise _analysis_error(f"section {kind} must declare no_data")
        items = section.get("items")
        if not isinstance(items, list):
            raise _analysis_error(f"section {kind} items must be a list")
        if section["no_data"] and items:
            raise _analysis_error(f"section {kind} has items but is marked no_data")
        if not section["no_data"] and not items:
            raise _analysis_error(f"section {kind} is empty but is not marked no_data")
        by_kind[kind] = section
    if not any(k in by_kind for k in INVEST_SECTIONS):  # analyses made before the investment view existed
        by_kind.update({k: {"kind": k, "items": [], "no_data": True} for k in INVEST_SECTIONS})
    missing = [kind for kind in SECTION_ORDER if kind not in by_kind]
    if missing:
        raise _analysis_error("missing sections: " + ", ".join(missing))

    facts = store.facts(company.id)
    fact_by_id = {f.id: f for f in facts if f.id is not None}
    refs: set[int] = set()
    for kind in SECTION_ORDER:
        section = by_kind[kind]
        for item in section["items"]:
            if not isinstance(item, dict):
                raise _analysis_error(f"item in {kind} must be an object")
            if not isinstance(item.get("text"), str) or not item["text"].strip():
                raise _analysis_error(f"item in {kind} needs non-empty text")
            if not isinstance(item.get("assessment"), bool):
                raise _analysis_error(f"item in {kind} must declare assessment")
            if item.get("confidence") not in CONFIDENCE_LEVELS:
                raise _analysis_error(f"item in {kind} has invalid confidence")
            assumptions = item.get("assumptions")
            if not isinstance(assumptions, list) or not all(isinstance(x, str) for x in assumptions):
                raise _analysis_error(f"item in {kind} assumptions must be a list of strings")
            fact_ids = item.get("fact_ids")
            if not isinstance(fact_ids, list) or not fact_ids:
                raise _analysis_error(f"item in {kind} has no fact references")
            if any(not isinstance(fid, int) or isinstance(fid, bool) or fid <= 0 for fid in fact_ids):
                raise _analysis_error(f"item in {kind} has invalid fact references")
            refs.update(fact_ids)

    missing_refs = sorted(refs - fact_by_id.keys())
    if missing_refs:
        rows = []
        for start in range(0, len(missing_refs), 500):
            batch = missing_refs[start:start + 500]
            placeholders = ",".join("?" for _ in batch)
            rows.extend(store.db.execute(f"SELECT id, company_id FROM fact WHERE id IN ({placeholders})", batch).fetchall())
        owners = {int(row["id"]): row["company_id"] for row in rows}
        cross = [fid for fid in missing_refs if fid in owners and owners[fid] != company.id]
        unknown = [fid for fid in missing_refs if fid not in owners]
        if cross:
            raise _analysis_error("cross-company fact references: " + ", ".join(map(str, cross)))
        if unknown:
            raise _analysis_error("unknown fact references: " + ", ".join(map(str, unknown)))
        raise _analysis_error("fact references are not available in the company snapshot")

    expected_hash = analysis.get("facts_hash")
    if expected_hash is not None:
        if not isinstance(expected_hash, str) or not expected_hash:
            raise _analysis_error("facts_hash must be a non-empty string")
        try:
            from dd.analyze import fact_snapshot_sha256
        except ImportError as exc:
            raise _analysis_error("fact snapshot hash helper is unavailable") from exc
        actual_hash = fact_snapshot_sha256(company.id, facts)
        if actual_hash != expected_hash:
            raise _analysis_error("analysis is stale because company facts changed")

    return analysis, [by_kind[k] for k in SECTION_ORDER], fact_by_id


def _write_facts_csv(path: Path, facts: list[Fact]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FACT_CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for fact in facts:
            row = {
                "id": fact.id,
                "company_id": fact.company_id,
                "type": fact.type,
                "key": fact.key,
                "value_json": _value_json(fact.value),
                "event_date": fact.event_date,
                "date_precision": fact.date_precision,
                "source_url": fact.source_url,
                "snippet": fact.snippet,
                "extractor": fact.extractor,
                "confidence": fact.confidence,
            }
            writer.writerow({key: _csv_safe(value) for key, value in row.items()})


def _csv_safe(value: Any) -> Any:
    """Prevent spreadsheet applications from interpreting untrusted text as a formula."""
    if isinstance(value, str) and value.lstrip().startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


def write_dossier(store: Store, company: Company, output_dir: Path) -> dict[str, str]:
    """Render the latest dossier analysis after validating all fact references and snapshot age."""
    analysis, sections, fact_by_id = _load_and_validate(store, company)
    output_dir = Path(output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = _slug(company.id)
    markdown_path = (output_dir / f"{stem}-dossier.md").resolve()
    html_path = (output_dir / f"{stem}-dossier.html").resolve()
    csv_path = (output_dir / f"{stem}-facts.csv").resolve()
    from dd import render
    row = store.db.execute("SELECT COALESCE(SUM(cost_usd),0) s FROM llm_call WHERE purpose=?",
                           (f"extract:{company.id}",)).fetchone()
    extraction_cost = float(row["s"] if row else 0)
    prepared = render.prepare(company, analysis, sections, fact_by_id, glance_rows(analysis.get("signals")))
    args = (company, analysis, prepared, SECTION_TITLES, LABEL_TITLES, _safe_href, extraction_cost,
            _value_json, _fact_status, fact_by_id)
    markdown_path.write_text(render.render_markdown(*args), encoding="utf-8")
    html_path.write_text(render.render_html(*args), encoding="utf-8")
    _write_facts_csv(csv_path, list(fact_by_id.values()))
    return {"markdown": str(markdown_path), "html": str(html_path), "facts_csv": str(csv_path)}
