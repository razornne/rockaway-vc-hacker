"""Compare search providers on the same queries (result in eval/search_comparison.md).

    uv run python eval/compare_search.py

For each query and provider: results, results that mention the company, results off the company's own domain,
URLs only this provider found, latency. Writes eval/search_comparison.md.
"""
from __future__ import annotations

import sys
import time
import unicodedata
from pathlib import Path

from dd import search
from dd.cli import ctx_from_settings

QUERIES = [  # (company token, company domain, query)
    ("filuta", "filuta.ai", '"Filuta" Houston ISD'),
    ("filuta", "filuta.ai", "Filuta AI funding round"),
    ("filuta", "filuta.ai", "Filuta AI composite AI autonomous testing customers"),
    ("cruxo", "cruxo.io", '"Cruxo" "Dr. Max"'),
    ("cruxo", "cruxo.io", "Cruxo retail media investment"),
    ("navigara", "navigara.com", "Navigara seed round investors"),
    ("navigara", "navigara.com", "Navigara engineering performance customers"),
    ("navigara", "navigara.com", "Navigara SOC 2"),
    ("valka", "valka.ai", "ValkaAI pre-seed Rockaway"),
]
PROVIDERS = ["tavily", "exa", "keyless"]


def fold(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s or "") if not unicodedata.combining(c)).lower()


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ctx = ctx_from_settings()
    avail = search.available(ctx)
    rows, per_query = [], []
    totals = {p: {"results": 0, "relevant": 0, "independent": 0, "unique": 0, "seconds": 0.0} for p in PROVIDERS}
    for token, domain, q in QUERIES:
        found = {}
        for p in PROVIDERS:
            if p not in avail:
                continue
            t = time.monotonic()
            res = search.search_detailed(q, ctx, provider=p, n=10)
            dt = time.monotonic() - t
            rs = res.get("rows", [])
            rel = [r for r in rs if token in fold(f"{r.get('title')} {r.get('snippet')} {r.get('url')}")]
            ind = [r for r in rel if domain not in (r.get("url") or "")]
            found[p] = {r["url"] for r in ind}
            totals[p]["results"] += len(rs)
            totals[p]["relevant"] += len(rel)
            totals[p]["independent"] += len(ind)
            totals[p]["seconds"] += dt
            rows.append((q, p, len(rs), len(rel), len(ind), dt, [r["url"] for r in ind][:4]))
        for p in found:
            others = set().union(*[found[o] for o in found if o != p]) if len(found) > 1 else set()
            uniq = found[p] - others
            totals[p]["unique"] += len(uniq)
        per_query.append((q, found))
    lines = ["# Search provider comparison", "", f"Queries: {len(QUERIES)}. 'Relevant' = mentions the company; "
             "'independent' = relevant and not on the company's own domain; 'unique' = independent URLs no other "
             "provider returned.", "", "| Provider | Results | Relevant | Independent | Unique | Avg latency |",
             "|---|---|---|---|---|---|"]
    for p, t in totals.items():
        if p in avail:
            lines.append(f"| {p} | {t['results']} | {t['relevant']} | {t['independent']} | {t['unique']} | "
                         f"{t['seconds'] / len(QUERIES):.1f}s |")
    lines += ["", "## Per query", "", "| Query | Provider | Results | Relevant | Independent | Examples |", "|---|---|---|---|---|---|"]
    for q, p, n, rel, ind, dt, ex in rows:
        lines.append(f"| {q} | {p} | {n} | {rel} | {ind} | {'<br>'.join(ex)} |")
    out = Path(__file__).with_name("search_comparison.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:12]))
    print(f"\nwritten {out}")


if __name__ == "__main__":
    main()
