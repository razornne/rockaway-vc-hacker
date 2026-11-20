"""Semantic accuracy check: a sheet of brief statements for a person to label, and a score of the labels.

`dd eval` checks that quotes exist and that hand-checked registry facts are reproduced. It cannot tell whether a
statement is RIGHT: whether the quote supports it, whether its numbers and names are correct, whether a judgement
follows from the evidence. That needs a person. `dd label-sheet` writes one row per statement of the chosen briefs
with everything needed to judge it (the statement, the tool's evidence label, the cited quotes and links); the
reviewer fills the columns on the right; `dd label-score` counts the answers per question.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from dd import render
from dd.store import Store
from dd.writer import LABEL_TITLES, SECTION_TITLES

QUESTIONS = (
    ("supported", "Do the cited quotes support the statement?", ("yes", "partly", "no")),
    ("numbers", "Are amounts, currencies, dates and counts right?", ("yes", "no", "n/a")),
    ("entities", "Are the companies, investors, customers and buyers the right ones?", ("yes", "no", "n/a")),
    ("follows", "For a judgement: does it follow from the evidence?", ("yes", "partly", "no", "n/a")),
    ("from_absence", "Does it conclude something from missing data?", ("no", "yes")),
    ("severity", "If anything is wrong: would it mislead an investor?", ("material", "minor", "n/a")),
)
FIXED = ("row", "company", "section", "label", "statement", "tool_evidence_label", "cited_quotes", "cited_links")
HUMAN = tuple(q for q, _, _ in QUESTIONS) + ("comment",)


def sheet_rows(store: Store, company_ids: list[str]) -> list[dict]:
    rows = []
    for cid in company_ids:
        company = store.get_company(cid)
        analysis = store.latest_analysis(cid, "dossier")
        if not company or not analysis:
            continue
        facts = {f.id: f for f in store.facts(cid)}
        prepared = render.prepare(company, analysis, analysis["sections"], facts, [])
        items = [("summary", it) for it in prepared["tldr"]]
        items += [(s["kind"], it) for s in prepared["sections"] for it in s["items"]]
        for kind, it in items:
            ids = [i for i in it.get("fact_ids", []) if i in facts][:5]
            rows.append({
                "company": cid, "section": SECTION_TITLES.get(kind, kind),
                "label": LABEL_TITLES.get(it.get("label"), it.get("label") or ""),
                "statement": it["text"],
                "tool_evidence_label": render.STRENGTH[it["strength"]][0],
                # the same text the brief shows for a source: the quote, or for a register record its key fields
                "cited_quotes": "\n".join(f"[{n}] {render._snip(facts[i], 400)}" for n, i in enumerate(ids, 1)),
                "cited_links": "\n".join(f"[{n}] {facts[i].source_url}" for n, i in enumerate(ids, 1)),
            })
    for n, r in enumerate(rows, 1):
        r["row"] = n
    return rows


def write_sheet(store: Store, company_ids: list[str], path: Path) -> int:
    rows = sheet_rows(store, company_ids)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig: Excel opens Czech letters correctly
        w = csv.DictWriter(f, fieldnames=FIXED + HUMAN)
        w.writeheader()
        for r in rows:
            w.writerow({**r, **{k: "" for k in HUMAN}})
    return len(rows)


def summary(path: Path) -> dict | None:
    """The headline counts of a labelled sheet (for the showcase), or None when nothing is labelled yet."""
    if not path.exists():
        return None
    with path.open(encoding="utf-8-sig", newline="") as f:
        done = [r for r in csv.DictReader(f) if any((r.get(q) or "").strip() for q, _, _ in QUESTIONS)]
    if not done:
        return None
    c = {q: Counter((r.get(q) or "").strip().lower() for r in done) for q, _, _ in QUESTIONS}
    answered = lambda q: sum(v for k, v in c[q].items() if k not in ("", "n/a"))  # noqa: E731
    return {"n": len(done), "supported": c["supported"]["yes"], "partly": c["supported"]["partly"],
            "unsupported": c["supported"]["no"], "numbers_right": c["numbers"]["yes"], "numbers": answered("numbers"),
            "follows": c["follows"]["yes"], "judgements": answered("follows"), "from_absence": c["from_absence"]["yes"],
            "material": c["severity"]["material"], "minor": c["severity"]["minor"]}


def score(path: Path) -> str:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    done = [r for r in rows if any((r.get(q) or "").strip() for q, _, _ in QUESTIONS)]
    out = [f"# Semantic accuracy: {path.name}", "", f"Labelled rows: {len(done)} of {len(rows)}.", ""]
    for q, text, options in QUESTIONS:
        c = Counter((r.get(q) or "").strip().lower() or "(blank)" for r in done)
        if q == "severity":  # not a pass rate: how many problems, and how bad
            out.append(f"- **{text}** {c.get('material', 0)} material, {c.get('minor', 0)} minor, out of {len(done)} "
                       "statements")
            continue
        answered = sum(v for k, v in c.items() if k not in ("(blank)", "n/a"))
        parts = ", ".join(f"{k} {v}" for k, v in c.most_common())
        good = c.get(options[0], 0)
        share = f"{good / answered:.0%} {options[0]}" if answered else "no answers"
        out.append(f"- **{text}** {share} of {answered} answered ({parts})")
    out += ["", "## By section (statements with any problem / labelled)", ""]
    bad = lambda r: ((r.get("supported") or "").lower() in ("no", "partly") or (r.get("numbers") or "").lower() == "no"  # noqa: E731
                     or (r.get("entities") or "").lower() == "no" or (r.get("follows") or "").lower() in ("no", "partly")
                     or (r.get("from_absence") or "").lower() == "yes")
    by = Counter(r["section"] for r in done)
    probs = Counter(r["section"] for r in done if bad(r))
    out += [f"- {s}: {probs.get(s, 0)} / {n}" for s, n in by.most_common()]
    material = [r for r in done if (r.get("severity") or "").lower() == "material"]
    if material:
        out += ["", "## Material problems", ""] + [f"- row {r['row']} ({r['company']}, {r['section']}): "
                                                    f"{r['statement'][:120]} — {r.get('comment') or ''}" for r in material]
    return "\n".join(out) + "\n"
