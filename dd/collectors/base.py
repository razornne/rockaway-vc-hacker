"""Collector interface. Each collector lives in its own module and is independent of the others.

Contract:
  - `name`: short id, used as Fact.extractor (e.g. "registry", "web", "techfp").
  - `collect(company, ctx)` returns facts; it must NOT raise on network/source errors —
    instead return a `source_unavailable` fact (with the URL it tried) and continue.
  - Every Fact needs `source_url`. Use ctx.http so responses are cached and recorded.
  - Structured sources are parsed with code; do not call the LLM from collectors.
  - Personal data: never store birth dates / addresses of natural persons.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field

from dd.config import Settings
from dd.http import Http
from dd.store import Company, Fact, Store


@dataclass
class Context:
    settings: Settings
    store: Store
    http: Http
    log: logging.Logger = field(default_factory=lambda: logging.getLogger("dd"))


class Collector:
    name: str = "base"
    #: human-readable list of sources this collector reads
    sources: list[str] = []

    def collect(self, company: Company, ctx: Context) -> list[Fact]:  # pragma: no cover - interface
        raise NotImplementedError

    # helper
    def unavailable(self, company: Company, source: str, url: str, reason: str) -> Fact:
        return Fact(company_id=company.id, type="source_unavailable", key=source, value={"reason": reason[:300]},
                    source_url=url, extractor=self.name, confidence="high")
