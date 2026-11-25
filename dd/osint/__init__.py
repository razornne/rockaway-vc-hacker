"""OSINT checks: what public records say about a company's claims and about the people behind it.

Runs after a brief has been analysed and adds facts that only code reads and shows: the language model never sees
them, and they do not make an analysis stale (dd.analyze.fact_snapshot_sha256 skips these extractors). Plan, sources
and decisions: docs/OSINT_PLAN.md.

  claims   - company claims against records (AI, team size, revenue, public customers); no network
  people   - officers and shareholders, their other companies and how those ended (register open data)
  checks   - insolvency of people (ISIR web service), unreliable VAT payer (ADIS), sanctions lists (EU, CZ)
  hiring   - public job-board APIs and earlier versions of the careers page (Wayback)
"""
from __future__ import annotations

EXTRACTORS = ("osint_claims", "osint_people", "osint_checks", "osint_hiring")


def is_osint(extractor: str | None) -> bool:
    return extractor in EXTRACTORS
