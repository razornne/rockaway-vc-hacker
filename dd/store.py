"""SQLite fact store. One file, no ORM.

Core objects:
  Company     — what we analyse (id = slug)
  SourceDoc   — every fetched document (raw bytes on disk, extracted text on disk)
  Fact        — one atomic, sourced statement about a company
  Analysis    — LLM / code analysis output with cost
"""
from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SCHEMA = """
CREATE TABLE IF NOT EXISTS company (
  id TEXT PRIMARY KEY, name TEXT NOT NULL, domain TEXT, ico TEXT, country TEXT,
  legal_form TEXT, hints TEXT DEFAULT '{}', created_at TEXT
);
CREATE TABLE IF NOT EXISTS source_doc (
  id INTEGER PRIMARY KEY AUTOINCREMENT, company_id TEXT, url TEXT NOT NULL, kind TEXT,
  status INTEGER, content_type TEXT, sha256 TEXT, raw_path TEXT, text_path TEXT,
  title TEXT, fetched_at TEXT, UNIQUE(company_id, url, kind)
);
CREATE TABLE IF NOT EXISTS fact (
  id INTEGER PRIMARY KEY AUTOINCREMENT, company_id TEXT NOT NULL, type TEXT NOT NULL,
  key TEXT, value TEXT, event_date TEXT, date_precision TEXT, source_url TEXT,
  source_doc_id INTEGER, snippet TEXT, extractor TEXT, confidence TEXT, created_at TEXT,
  UNIQUE(company_id, type, key, source_url, extractor)
);
CREATE TABLE IF NOT EXISTS analysis (
  id INTEGER PRIMARY KEY AUTOINCREMENT, company_id TEXT, kind TEXT, output TEXT,
  model TEXT, prompt_version TEXT, fact_ids TEXT, cost_usd REAL DEFAULT 0, created_at TEXT
);
CREATE TABLE IF NOT EXISTS llm_call (
  id INTEGER PRIMARY KEY AUTOINCREMENT, cache_key TEXT UNIQUE, model TEXT, purpose TEXT,
  input_tokens INTEGER, output_tokens INTEGER, cost_usd REAL, response TEXT, created_at TEXT
);
CREATE INDEX IF NOT EXISTS fact_company ON fact(company_id, type);
"""


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass
class Company:
    id: str
    name: str
    domain: str | None = None
    ico: str | None = None
    country: str | None = None
    legal_form: str | None = None
    hints: dict[str, Any] = field(default_factory=dict)  # e.g. github_org, app_seller, aliases


@dataclass
class Fact:
    """One atomic statement. `source_url` is mandatory for anything shown in a dossier.

    type        — vocabulary in dd/facts.py (FACT_TYPES)
    key         — distinguishes several facts of one type (subdomain name, repo name, holder name…)
    value       — JSON-serialisable payload
    event_date  — 'YYYY-MM-DD' | 'YYYY-MM' | 'YYYY' | None
    snippet     — exact text from the source that supports the fact (required for LLM-extracted facts)
    confidence  — 'high' (structured source / parser) | 'medium' | 'low'
    """
    company_id: str
    type: str
    value: Any
    source_url: str
    key: str | None = None
    event_date: str | None = None
    date_precision: str | None = None
    snippet: str | None = None
    source_doc_id: int | None = None
    extractor: str = ""
    confidence: str = "high"
    id: int | None = None


class Store:
    def __init__(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path, timeout=60)  # several collectors may write concurrently
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)

    # --- company ---------------------------------------------------------
    def upsert_company(self, c: Company) -> Company:
        self.db.execute(
            """INSERT INTO company(id,name,domain,ico,country,legal_form,hints,created_at)
               VALUES(?,?,?,?,?,?,?,?)
               ON CONFLICT(id) DO UPDATE SET name=excluded.name,
                 domain=COALESCE(excluded.domain, company.domain), ico=COALESCE(excluded.ico, company.ico),
                 country=COALESCE(excluded.country, company.country),
                 legal_form=COALESCE(excluded.legal_form, company.legal_form), hints=excluded.hints""",
            (c.id, c.name, c.domain, c.ico, c.country, c.legal_form, json.dumps(c.hints, ensure_ascii=False), now()),
        )
        self.db.commit()
        return c

    def get_company(self, cid: str) -> Company | None:
        r = self.db.execute("SELECT * FROM company WHERE id=?", (cid,)).fetchone()
        if not r:
            return None
        return Company(id=r["id"], name=r["name"], domain=r["domain"], ico=r["ico"], country=r["country"],
                       legal_form=r["legal_form"], hints=json.loads(r["hints"] or "{}"))

    def companies(self) -> list[Company]:
        return [self.get_company(r["id"]) for r in self.db.execute("SELECT id FROM company ORDER BY id")]

    # --- source docs -----------------------------------------------------
    def add_source_doc(self, *, company_id: str | None, url: str, kind: str, status: int | None,
                       content_type: str | None, sha256: str | None, raw_path: str | None,
                       text_path: str | None = None, title: str | None = None) -> int:
        self.db.execute(
            """INSERT INTO source_doc(company_id,url,kind,status,content_type,sha256,raw_path,text_path,title,fetched_at)
               VALUES(?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(company_id,url,kind) DO UPDATE SET status=excluded.status, sha256=excluded.sha256,
                 raw_path=excluded.raw_path, text_path=COALESCE(excluded.text_path, source_doc.text_path),
                 title=COALESCE(excluded.title, source_doc.title), fetched_at=excluded.fetched_at""",
            (company_id, url, kind, status, content_type, sha256, raw_path, text_path, title, now()),
        )
        self.db.commit()
        return self.db.execute("SELECT id FROM source_doc WHERE company_id IS ? AND url=? AND kind=?",
                               (company_id, url, kind)).fetchone()["id"]

    def set_doc_text(self, doc_id: int, text_path: str, title: str | None = None) -> None:
        self.db.execute("UPDATE source_doc SET text_path=?, title=COALESCE(?, title) WHERE id=?",
                        (text_path, title, doc_id))
        self.db.commit()

    def source_docs(self, company_id: str, kinds: Iterable[str] | None = None) -> list[sqlite3.Row]:
        q, args = "SELECT * FROM source_doc WHERE company_id=?", [company_id]
        if kinds:
            kinds = list(kinds)
            q += f" AND kind IN ({','.join('?' * len(kinds))})"
            args += kinds
        return list(self.db.execute(q + " ORDER BY id", args))

    # --- facts -----------------------------------------------------------
    def add_facts(self, facts: Iterable[Fact]) -> int:
        n = 0
        for f in facts:
            if not f.source_url:
                raise ValueError(f"fact without source_url: {f.type} {f.key}")
            cur = self.db.execute(
                """INSERT INTO fact(company_id,type,key,value,event_date,date_precision,source_url,source_doc_id,
                                    snippet,extractor,confidence,created_at)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                   ON CONFLICT(company_id,type,key,source_url,extractor) DO UPDATE SET value=excluded.value,
                     event_date=excluded.event_date, date_precision=excluded.date_precision,
                     snippet=excluded.snippet, confidence=excluded.confidence, source_doc_id=excluded.source_doc_id""",
                (f.company_id, f.type, f.key, json.dumps(f.value, ensure_ascii=False, default=str), f.event_date,
                 f.date_precision, f.source_url, f.source_doc_id, f.snippet, f.extractor, f.confidence, now()),
            )
            n += cur.rowcount
        self.db.commit()
        return n

    def facts(self, company_id: str, types: Iterable[str] | None = None) -> list[Fact]:
        q, args = "SELECT * FROM fact WHERE company_id=?", [company_id]
        if types:
            types = list(types)
            q += f" AND type IN ({','.join('?' * len(types))})"
            args += types
        out = []
        for r in self.db.execute(q + " ORDER BY type, event_date, id", args):
            out.append(Fact(id=r["id"], company_id=r["company_id"], type=r["type"], key=r["key"],
                            value=json.loads(r["value"]) if r["value"] else None, event_date=r["event_date"],
                            date_precision=r["date_precision"], source_url=r["source_url"],
                            source_doc_id=r["source_doc_id"], snippet=r["snippet"], extractor=r["extractor"],
                            confidence=r["confidence"]))
        return out

    def clear_facts(self, company_id: str, extractor: str) -> None:
        self.db.execute("DELETE FROM fact WHERE company_id=? AND extractor=?", (company_id, extractor))
        self.db.commit()

    def replace_facts(self, company_id: str, extractor: str, facts: Iterable[Fact]) -> int:
        """Replace one collector snapshot atomically, preserving the previous snapshot on failure."""
        facts = list(facts)
        for fact in facts:
            if fact.company_id != company_id or fact.extractor != extractor or not fact.source_url:
                raise ValueError("invalid collector fact ownership or missing source URL")
            json.dumps(fact.value, ensure_ascii=False, default=str)
        self.db.execute("SAVEPOINT collector_snapshot")
        try:
            self.db.execute("DELETE FROM fact WHERE company_id=? AND extractor=?", (company_id, extractor))
            for fact in facts:
                self.db.execute(
                    """INSERT INTO fact(company_id,type,key,value,event_date,date_precision,source_url,source_doc_id,
                                        snippet,extractor,confidence,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
                       ON CONFLICT(company_id,type,key,source_url,extractor) DO UPDATE SET
                         value=excluded.value, event_date=excluded.event_date,
                         date_precision=excluded.date_precision, source_doc_id=excluded.source_doc_id,
                         snippet=excluded.snippet, confidence=excluded.confidence""",
                    (fact.company_id, fact.type, fact.key, json.dumps(fact.value, ensure_ascii=False, default=str),
                     fact.event_date, fact.date_precision, fact.source_url, fact.source_doc_id, fact.snippet,
                     fact.extractor, fact.confidence, now()))
            self.db.execute("RELEASE SAVEPOINT collector_snapshot")
        except Exception:
            self.db.execute("ROLLBACK TO SAVEPOINT collector_snapshot")
            self.db.execute("RELEASE SAVEPOINT collector_snapshot")
            raise
        return len(facts)

    # --- analyses / llm --------------------------------------------------
    def add_analysis(self, company_id: str, kind: str, output: Any, model: str = "", prompt_version: str = "",
                     fact_ids: list[int] | None = None, cost_usd: float = 0.0) -> int:
        cur = self.db.execute(
            "INSERT INTO analysis(company_id,kind,output,model,prompt_version,fact_ids,cost_usd,created_at) VALUES(?,?,?,?,?,?,?,?)",
            (company_id, kind, json.dumps(output, ensure_ascii=False, default=str), model, prompt_version,
             json.dumps(fact_ids or []), cost_usd, now()))
        self.db.commit()
        return cur.lastrowid

    def latest_analysis(self, company_id: str, kind: str) -> Any:
        r = self.db.execute("SELECT output FROM analysis WHERE company_id=? AND kind=? ORDER BY id DESC LIMIT 1",
                            (company_id, kind)).fetchone()
        return json.loads(r["output"]) if r else None

    def llm_spent(self) -> float:
        return self.db.execute("SELECT COALESCE(SUM(cost_usd),0) s FROM llm_call").fetchone()["s"]
