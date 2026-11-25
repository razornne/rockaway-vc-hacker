"""Hiring: open roles from public job-board APIs, and earlier versions of the careers page from the Wayback Machine.

Job boards (no key needed for reading public postings, docs checked 25 November 2026): Greenhouse, Lever, Ashby,
Personio. They are queried only when the company's own careers links point to them. LinkedIn is never read.
"""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date
from urllib.parse import urlencode, urlparse

from dd.store import Company, Fact

NAME = "osint_hiring"
CDX = "https://web.archive.org/cdx/search/cdx"
YEARS_BACK = 3


def bucket(title: str) -> str:
    from dd.signals import ROLE_BUCKETS
    t = (title or "").lower()
    return next((b for b, pat in ROLE_BUCKETS if re.search(pat, t)), "other")


def boards(facts: list[Fact]) -> list[tuple[str, str]]:
    """(vendor, API URL) for each job board the company's own pages link to."""
    out = []
    for f in facts:
        for url in (f.source_url, (f.value or {}).get("url") if isinstance(f.value, dict) else None):
            if not url:
                continue
            u = urlparse(url)
            host, parts = (u.hostname or "").lower(), [p for p in u.path.split("/") if p]
            if not parts:
                if host.endswith((".jobs.personio.de", ".jobs.personio.com")):
                    out.append(("Personio", f"https://{host}/xml"))
                continue
            if host in ("boards.greenhouse.io", "job-boards.greenhouse.io"):
                out.append(("Greenhouse", f"https://boards-api.greenhouse.io/v1/boards/{parts[0]}/jobs"))
            elif host in ("boards.eu.greenhouse.io", "job-boards.eu.greenhouse.io"):
                out.append(("Greenhouse", f"https://boards-api.eu.greenhouse.io/v1/boards/{parts[0]}/jobs"))
            elif host == "jobs.lever.co":
                out.append(("Lever", f"https://api.lever.co/v0/postings/{parts[0]}?mode=json"))
            elif host == "jobs.eu.lever.co":
                out.append(("Lever", f"https://api.eu.lever.co/v0/postings/{parts[0]}?mode=json"))
            elif host == "jobs.ashbyhq.com":
                out.append(("Ashby", f"https://api.ashbyhq.com/posting-api/job-board/{parts[0]}"))
            elif host.endswith((".jobs.personio.de", ".jobs.personio.com")):
                out.append(("Personio", f"https://{host}/xml"))
    return list(dict.fromkeys(out))


def parse_board(vendor: str, text: str) -> list[dict] | None:
    try:
        if vendor == "Personio":
            root = ET.fromstring(text)
            return [{"title": (p.findtext("name") or "").strip(), "team": p.findtext("department"),
                     "location": p.findtext("office"), "url": None} for p in root.iter("position")]
        data = json.loads(text)
    except (ValueError, ET.ParseError):
        return None
    if vendor == "Greenhouse":
        return [{"title": j.get("title"), "team": ", ".join(d.get("name", "") for d in j.get("departments") or []) or None,
                 "location": (j.get("location") or {}).get("name"), "url": j.get("absolute_url")}
                for j in data.get("jobs") or []]
    if vendor == "Lever":
        return [{"title": j.get("text"), "team": (j.get("categories") or {}).get("team"),
                 "location": (j.get("categories") or {}).get("location"), "url": j.get("hostedUrl")}
                for j in data if isinstance(j, dict)] if isinstance(data, list) else None
    if vendor == "Ashby":
        return [{"title": j.get("title"), "team": j.get("department") or j.get("team"),
                 "location": j.get("location"), "url": j.get("jobUrl")} for j in data.get("jobs") or []]
    return None


def board_jobs(company: Company, facts: list[Fact], ctx) -> list[Fact]:
    out = []
    for vendor, url in boards(facts)[:2]:
        r = ctx.http.get(url, company_id=company.id, kind="job_board")
        jobs = parse_board(vendor, r.text) if r.ok else None
        if jobs is None:
            out.append(Fact(company_id=company.id, type="source_unavailable", key=f"job_board:{vendor}",
                            value={"reason": f"HTTP {r.status} or unreadable"}, source_url=url, extractor=NAME))
            continue
        by = Counter(bucket(j["title"] or "") for j in jobs if j.get("title"))
        out.append(Fact(company_id=company.id, type="hiring_snapshot", key=f"{vendor} {date.today().isoformat()}",
                        source_url=url, extractor=NAME, event_date=date.today().isoformat(), date_precision="day",
                        value={"source": f"{vendor} job board", "year": date.today().year, "count": len(jobs),
                               "by_function": dict(by), "titles": [j["title"] for j in jobs if j.get("title")][:10]}))
    return out


def careers_url(facts: list[Fact]) -> str | None:
    pages = [f.source_url for f in facts if f.type == "web_page" and f.key == "careers" and f.source_url]
    return sorted(pages, key=len)[0] if pages else None


def careers_history(company: Company, facts: list[Fact], ctx) -> list[Fact]:
    """One archived copy of the careers page per year, for the last YEARS_BACK years, parsed for job titles."""
    from dd.collectors.history import parse_cdx, timeout
    from dd.collectors.web import extract_jobs_html
    url = careers_url(facts)
    if not url:
        return []
    this_year = date.today().year
    q = f"{CDX}?{urlencode({'url': url, 'output': 'json', 'fl': 'timestamp,original', 'filter': 'statuscode:200', 'collapse': 'timestamp:4'})}"
    out = []
    with timeout(ctx, 60):
        r = ctx.http.get(q, company_id=company.id, kind="wayback_cdx")
        rows = parse_cdx(r.text) if r.ok else None
        if rows is None:
            return [Fact(company_id=company.id, type="source_unavailable", key="wayback:careers", source_url=q,
                         value={"reason": f"HTTP {r.status}"}, extractor=NAME)]
        rows = [x for x in rows if x.get("timestamp", "")[:4].isdigit()
                and this_year - YEARS_BACK <= int(x["timestamp"][:4]) < this_year]
        for row in rows[-YEARS_BACK:]:
            ts = row["timestamp"]
            snap = f"https://web.archive.org/web/{ts}id_/{row['original']}"
            s = ctx.http.get(snap, company_id=company.id, kind="wayback_snapshot")
            if not s.ok:
                continue
            titles = [j["title"] for j in extract_jobs_html(s.text, row["original"]) if j.get("title")]
            out.append(Fact(company_id=company.id, type="hiring_snapshot", key=f"wayback {ts[:8]}",
                            source_url=f"https://web.archive.org/web/{ts}/{row['original']}", extractor=NAME,
                            event_date=f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}", date_precision="day",
                            value={"source": "archived careers page", "year": int(ts[:4]), "count": len(titles),
                                   "by_function": dict(Counter(bucket(t) for t in titles)), "titles": titles[:10]}))
    return out
