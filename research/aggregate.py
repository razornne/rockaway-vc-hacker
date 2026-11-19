"""Aggregates research/<group>/*.json into a table: source -> how early it showed the company.

Run (from research/ or the project root):
    python research/aggregate.py
Writes research/signals.md and research/signals.csv.

Segments:
  fund    - Rockaway Ventures fund deals (without group legacy deals and without Apptronik)
  legacy  - Rockaway Capital investments made before the fund
  control - control group: CEE rounds led by other funds
"""
import csv
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).parent
LEGACY = {"productboard", "bezrealitky", "creditas", "gjirafa"}
EXCLUDE = {"apptronik"}  # large US round, not a CEE sourcing case
SKIP_TYPES = {"rockaway_announced", "rockaway_deal"}

CATEGORY = {
    "website_first": "existence", "registry_incorporation": "existence", "registry_other": "existence",
    "registry_capital_increase": "money", "registry_new_shareholder": "money", "prior_round": "money",
    "investor_portfolio": "money", "press_round": "money",
    "gov_contract": "customers/growth", "website_customers": "customers/growth", "website_pricing": "customers/growth",
    "hiring": "customers/growth", "product_launch": "customers/growth", "financial_statements": "customers/growth",
    "grant_national": "team/technology", "grant_eu": "team/technology",
    "accelerator": "team/technology", "award_competition": "team/technology",
    "press_first": "press", "other": "other",
}


def load(folder, keep):
    out = []
    for p in sorted((ROOT / folder).glob("*.json")):
        if p.stem == "control_list" or not keep(p.stem):
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        d["_slug"] = p.stem
        out.append(d)
    return out


def pre_t0(c):
    return [e for e in c.get("events", [])
            if e.get("url") and isinstance(e.get("months_before_t0"), (int, float))
            and e["months_before_t0"] > 0 and e.get("source_type") not in SKIP_TYPES]


def segment(name, companies, md, rows):
    n = len(companies)
    by_type = {}
    per_company = []
    for c in companies:
        pre = pre_t0(c)
        first = {}
        for e in pre:
            t = e["source_type"]
            if t not in first or e["months_before_t0"] > first[t]["months_before_t0"]:
                first[t] = e
        for t, e in first.items():
            by_type.setdefault(t, []).append((c.get("company") or c["_slug"], e["months_before_t0"]))
        any_ = max(pre, key=lambda e: e["months_before_t0"], default=None)
        subst = [e for e in pre if CATEGORY.get(e["source_type"]) not in ("existence", "other")]
        sub = max(subst, key=lambda e: e["months_before_t0"], default=None)
        per_company.append((c.get("company") or c["_slug"], (c.get("rockaway") or c.get("control_round") or {}).get("t0") or "", any_, sub))

    md += [f"## {name} (n={n})", "",
           "For each company, the earliest event of each type before T0 (events with a URL only).", "",
           "| source_type | category | companies | share | median months before T0 | min | max |",
           "|---|---|---|---|---|---|---|"]
    for t, vals in sorted(by_type.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        m = [v for _, v in vals]
        row = [name, t, CATEGORY.get(t, "?"), len(vals), f"{len(vals)/n:.0%}", round(statistics.median(m), 1),
               round(min(m), 1), round(max(m), 1), "; ".join(f"{c} ({v:.1f})" for c, v in vals)]
        rows.append(row)
        md.append("| " + " | ".join(str(x) for x in row[1:8]) + " |")
    md += ["", "| company | T0 | earliest signal (months) | earliest substantive signal (months) |",
           "|---|---|---|---|"]
    fmt = lambda e: "—" if e is None else f"{e['source_type']} ({e['months_before_t0']:.1f})"
    for comp, t0, a, s in per_company:
        md.append(f"| {comp} | {t0} | {fmt(a)} | {fmt(s)} |")
    md.append("")


def main():
    segs = [
        ("fund", load("companies", lambda s: s not in LEGACY | EXCLUDE)),
        ("legacy", load("companies", lambda s: s in LEGACY)),
        ("control", load("control", lambda s: True)),
    ]
    md = ["# Signals before T0", "",
          "Categories: existence = website and incorporation (they show the company's age, not that it is interesting);",
          "money = prior rounds, capital and shareholders in the register; customers/growth = public contracts, product, hiring;",
          "team/technology = grants, accelerators. A substantive signal is any signal except existence and other.", ""]
    rows = []
    for name, comps in segs:
        segment(name, comps, md, rows)
    (ROOT / "signals.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    with (ROOT / "signals.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["segment", "source_type", "category", "companies_covered", "share",
                    "median_months_before_t0", "min", "max", "companies"])
        w.writerows(rows)
    print("\n".join(md))


if __name__ == "__main__":
    main()
