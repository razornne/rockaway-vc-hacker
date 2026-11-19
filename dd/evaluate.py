"""`dd eval`: how good are the dossiers? Writes eval/report.md.

1. Golden facts — manually verified facts (eval/golden.json) must be reproduced by the collectors.
2. Quote integrity — every LLM-extracted fact's quote must be found in the saved source text.
3. Coverage — which dossier sections and 'at a glance' rows are filled, per company.
4. Evidence strength — distribution of labels over all findings (how much is verified vs company claim).
5. Cost — LLM spend per company (extraction + analysis).
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from dd.config import ROOT
from dd.extract import locate_quote
from dd.store import Store

GLANCE_ROWS = ("Funding (press)", "Investors in registry", "Public money", "Defence signals", "Thesis fit (Rockaway)",
               "Hiring", "AI dependency",
               "Engineering footprint", "Customers", "Claims checked", "Timeline")


def _golden(store: Store) -> list[tuple[str, str, bool, str]]:
    g = json.loads((ROOT / "eval" / "golden.json").read_text(encoding="utf-8"))
    out = []
    for cid, checks in g.items():
        if cid.startswith("_"):
            continue
        facts = store.facts(cid)
        holders = [f.value for f in facts if f.type == "registry_shareholder" and isinstance(f.value, dict)]
        for exp in checks.get("registry_shareholder", []):
            ok = any(exp["name_contains"].lower() in str(h.get("name", "")).lower() and h.get("from") == exp["from"]
                     for h in holders)
            out.append((cid, f"shareholder {exp['name_contains']} from {exp['from']}", ok, ""))
        for exp in checks.get("registry_capital", []):
            ok = any(isinstance(f.value, dict) and f.value.get("amount_czk") == exp["amount_czk"]
                     for f in facts if f.type == "registry_capital")
            out.append((cid, f"capital {exp['amount_czk']} CZK", ok, ""))
        for flag in checks.get("registry_flag", []):
            ok = any(f.type == "registry_flag" and f.key == flag for f in facts)
            out.append((cid, f"flag {flag}", ok, ""))
        for exp in checks.get("grant_national", []):
            grants = [f.value for f in facts if f.type == "grant_national" and isinstance(f.value, dict)]
            ok = any(exp["provider_contains"].lower() in str(v.get("provider", "")).lower()
                     and v.get("amount_czk") == exp["amount_czk"] for v in grants)
            agr = any(a.get("amount_czk") == exp.get("agreement_amount_czk")
                      for v in grants for a in (v.get("agreements") or []))
            out.append((cid, f"grant {exp['provider_contains']} {exp['amount_czk']} CZK", ok, ""))
            if "agreement_amount_czk" in exp:
                out.append((cid, "subsidy agreement attached to grant (not a customer contract)", agr, ""))
        if checks.get("no_gov_contract"):
            n = sum(f.type == "gov_contract" for f in facts)
            out.append((cid, "no subsidy counted as gov contract", n == 0, f"{n} gov_contract facts"))
        if "grant_count" in checks:
            n = sum(f.type == "grant_national" and f.extractor == "public_money" for f in facts)
            out.append((cid, f"{checks['grant_count']} distinct grants (no double counting)", n == checks["grant_count"], f"got {n}"))
        for sub in checks.get("subdomain_contains", []):
            ok = any(f.type == "subdomain" and f.key == sub for f in facts)
            out.append((cid, f"subdomain {sub}", ok, ""))
        if checks.get("github_org"):
            ok = any(f.type == "github_org" and str((f.value or {}).get("login", "")).lower() == checks["github_org"].lower()
                     for f in facts)
            out.append((cid, f"GitHub org {checks['github_org']}", ok, ""))
    return out


def _quote_integrity(store: Store, cid: str) -> tuple[int, int, list[str]]:
    docs = {d["id"]: d for d in store.source_docs(cid)}
    checked = bad = 0
    examples = []
    for f in store.facts(cid):
        if f.extractor != "llm_extract" or not f.snippet:
            continue
        d = docs.get(f.source_doc_id)
        if not d or not d["text_path"] or not Path(d["text_path"]).is_file():
            continue
        checked += 1
        text = Path(d["text_path"]).read_text(encoding="utf-8", errors="replace")
        if locate_quote(f.snippet, text) is None:
            bad += 1
            if len(examples) < 3:
                examples.append(f"F{f.id}: {f.snippet[:80]}")
    return checked, bad, examples


def metrics(store: Store) -> dict:
    """All evaluation numbers as data (used by the markdown report and the showcase site)."""
    from dd import render
    from dd.writer import SECTION_TITLES, _load_and_validate, glance_rows

    rows, strengths, total_cost = [], Counter(), 0.0
    by_section: dict[str, Counter] = {}
    integrity_rows = []
    for comp in store.companies():
        cid = comp.id
        try:
            analysis, sections, facts = _load_and_validate(store, comp)
        except ValueError as e:
            rows.append((cid, None, str(e)[:60]))
            continue
        glance = glance_rows(analysis.get("signals"))
        filled = {lab for lab, _, _ in glance}
        prep = render.prepare(comp, analysis, sections, facts, glance)
        items = prep["tldr"] + [it for s in prep["sections"] for it in s["items"]]
        strengths.update(it["strength"] for it in items)
        by_section.setdefault("summary (TL;DR)", Counter()).update(it["strength"] for it in prep["tldr"])
        for s in prep["sections"]:
            by_section.setdefault(s["kind"], Counter()).update(it["strength"] for it in s["items"])
        sec_filled = sum(not s["no_data"] for s in sections)
        extract_cost = store.db.execute("SELECT COALESCE(SUM(cost_usd),0) s FROM llm_call WHERE purpose=?",
                                        (f"extract:{cid}",)).fetchone()["s"]
        analysis_cost = float(analysis.get("cost_usd") or 0)
        total_cost += extract_cost + analysis_cost
        verified = sum(it["strength"] in ("verified", "corroborated") for it in items)
        rows.append((cid, {"sections": f"{sec_filled}/{len(SECTION_TITLES)}", "glance": filled, "facts": len(facts),
                           "sources": len(prep["sources"]), "verified": f"{verified}/{len(items)}",
                           "cost": extract_cost + analysis_cost,
                           "invest": any(s["kind"] == "investment_case" and not s["no_data"] for s in sections),
                           "generated_at": str(analysis.get("generated_at") or "")[:10]}, ""))
        integrity_rows.append((cid, *_quote_integrity(store, cid)))
    facts_only = Counter({k: v for k, v in strengths.items() if k != "view"})
    return {"golden": _golden(store), "integrity": integrity_rows, "rows": rows, "strengths": strengths,
            "by_section": by_section, "facts_only": facts_only, "total_cost": total_cost,
            "ledger": store.llm_spent()}


def evaluate(store: Store) -> str:
    from dd import render

    m = metrics(store)
    lines = ["# Evaluation report", ""]
    gold = m["golden"]
    passed = sum(ok for _, _, ok, _ in gold)
    lines += [f"## 1. Golden facts: {passed}/{len(gold)} reproduced", "", "| Company | Check | Result |", "|---|---|---|"]
    lines += [f"| {c} | {name} | {'✅' if ok else '❌ ' + note} |" for c, name, ok, note in gold]

    lines += ["", "## 2. Quote integrity (LLM-extracted facts vs saved source text)", "",
              "| Company | Checked | Not found | Examples |", "|---|---|---|---|"]
    for cid, checked, bad, ex in m["integrity"]:
        lines.append(f"| {cid} | {checked} | {bad} | {'; '.join(ex)} |")

    lines += ["", "## 3. Coverage per company", "",
              "| Company | Sections | Facts | Cited sources | Verified/corroborated findings | "
              + " | ".join(GLANCE_ROWS) + " | LLM cost |", "|---" * (6 + len(GLANCE_ROWS)) + "|"]
    for cid, r, err in m["rows"]:
        if r is None:
            lines.append(f"| {cid} | no dossier: {err} |")
            continue
        marks = " | ".join("●" if g in r["glance"] else "·" for g in GLANCE_ROWS)
        lines.append(f"| {cid} | {r['sections']} | {r['facts']} | {r['sources']} | {r['verified']} | {marks} | ${r['cost']:.4f} |")
    strengths = m["strengths"]
    n = sum(strengths.values()) or 1
    lines += ["", "## 4. Evidence strength over all findings", "", "| Label | Findings | Share |", "|---|---|---|"]
    for k, (label, _) in render.STRENGTH.items():
        lines.append(f"| {label} | {strengths.get(k, 0)} | {strengths.get(k, 0) / n:.0%} |")
    keys = list(render.STRENGTH)
    lines += ["", "### By section (views are expected in risks, rebuild verdict and questions)", "",
              "| Section | " + " | ".join(render.STRENGTH[k][0] for k in keys) + " |", "|---" * (len(keys) + 1) + "|"]
    for sec, cnt in m["by_section"].items():
        lines.append(f"| {sec} | " + " | ".join(str(cnt.get(k, 0)) for k in keys) + " |")
    facts_only = m["facts_only"]
    fm = sum(facts_only.values()) or 1
    lines += ["", f"Factual statements (everything except analyst views): {fm}. Verified or corroborated: "
              f"{(facts_only['verified'] + facts_only['corroborated']) / fm:.0%}; partly verified: {facts_only['mixed'] / fm:.0%}; "
              f"single outlet: {facts_only['single'] / fm:.0%}; company claim only: {facts_only['claim'] / fm:.0%}."]
    lines += ["", f"## 5. Cost", "", f"LLM total for current dossiers: ${m['total_cost']:.4f}; "
              f"ledger incl. all earlier runs: ${m['ledger']:.4f}."]
    return "\n".join(lines) + "\n"
