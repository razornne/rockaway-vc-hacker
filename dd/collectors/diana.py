"""DianaCollector: NATO DIANA accelerator cohorts (via Wayback Machine snapshots).

diana.nato.int sits behind Cloudflare bot management and answers 403 to any script, although robots.txt allows
crawling. We do not try to get around the bot check. The Internet Archive keeps snapshots of the public cohort
pages, and we read those (cached, one request per year).

Two uses:
  accelerator  — the company itself was selected (name or website domain match), with year and challenge area;
  peer_company — companies from the same cohorts whose one-line description overlaps the company's own site text.
                 These are competitor *candidates* from a NATO-vetted list, each with a source; the analysis
                 decides which are real competitors. Only 2026+ pages carry descriptions and countries.
Facts: accelerator, peer_company, source_check, source_unavailable. Never raises.
"""
from __future__ import annotations

import math
import re
import time
from collections import Counter
from datetime import date
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from dd.collectors.base import Collector, Context
from dd.store import Company, Fact
from dd.text import html_to_text
from dd.verify import _core

PAGE = "https://www.diana.nato.int/about-diana/{year}-cohort-of-companies.html"
ARCHIVE = "https://web.archive.org/web/{stamp}id_/{url}"
FIRST_YEAR = 2023
MAX_PEERS = 12
RETRY_WAIT = 20  # seconds; the Internet Archive rate-limits bursts with 429
STOP = set("""about across after against also among based been being between both built by cannot cost could data
defence defense during each enable enabling first from future have high highly into just level like make more most
much next only other over platform provide provides providing real secure security solution solutions system systems
than that their them then there these they this through time using very well what when where which while will with
within without world your company companies develop development developed research design designed technology
technologies innovation innovative engineering industry industrial information team contact products product
service services project projects support customer customers partner partners solution application applications
news read learn home page more cookies privacy""".split())
SYNONYMS = [(re.compile(r"\b(c-?uas|counter[- ](uas|drones?|uavs?))\b"), " counterdrone "),  # before 'drone'
            (re.compile(r"\b(uavs?|uas|suas|drones?|unmanned aerial|multicopters?|quadcopters?|multirotors?)\b"), " drone "),
            (re.compile(r"\b(swarms?|swarming)\b"), " swarm "),
            (re.compile(r"\b(gnss|gps)[- ]?(denied|free|independent)\b"), " gpsdenied ")]
PROFILE = 40      # distinctive terms of the company's own site
CORE = 8          # a peer must share at least one of the company's top terms


def _host(url: str | None) -> str | None:
    if not url or not url.startswith("http"):
        return None
    h = urlparse(url).netloc.lower()
    return h[4:] if h.startswith("www.") else h


def parse_cohort(html: str, year: int) -> list[dict]:
    """Three layouts so far: 2024 (h1 area headers, logo grid), 2025 (area as an image, name grid),
    2026 (cards with name, description and country)."""
    soup = BeautifulSoup(html, "html.parser")
    root = soup.find(id="isw") or soup
    out, area = [], None
    for el in root.find_all(["div", "h1", "img", "a"]):
        cls = " ".join(el.get("class") or [])
        if el.name == "div" and "category-header" in cls:
            area = el.get_text(" ", strip=True) or area
        elif el.name == "h1" and "cohort" not in el.get_text().lower() and el.find_parent(class_="display"):
            area = el.get_text(" ", strip=True).title()
        elif el.name == "img" and "cohort-" in (el.get("src") or ""):
            m = re.search(r"cohort-([a-z-]+?)(?:-[a-z0-9]{6})?\.\w+$", el.get("src"))
            if m:
                area = m.group(1).replace("-", " ").title()
        elif el.name == "div" and "cohort-card" in cls:
            a = el.find("h4")
            ps = [p.get_text(" ", strip=True) for p in el.find_all("p")]
            link = a.find("a") if a else None
            if a:
                out.append({"name": a.get_text(" ", strip=True), "url": link.get("href") if link else None,
                            "description": ps[0] if ps else None, "country": ps[1].title() if len(ps) > 1 else None,
                            "area": area, "year": year})
        elif el.name == "a" and not el.find_parent(class_="cohort-card") and el.find_parent(class_="mdl-cell--3-col"):
            name = el.get_text(" ", strip=True)
            href = el.get("href") or ""
            if name:
                out.append({"name": name, "url": href if href.startswith("http") else None, "description": None,
                            "country": None, "area": area, "year": year})
    return out


def _stems(text: str) -> list[str]:
    t = (text or "").lower()
    for rx, rep in SYNONYMS:
        t = rx.sub(rep, t)
    return [w[:6] for w in re.findall(r"[a-z][a-z-]{3,}", t) if w not in STOP]


def peers(entries: list[dict], site_text: str, exclude: str) -> list[dict]:
    """Competitor candidates: cohort companies whose one-line description uses the words that distinguish the
    company's own site (TF-IDF: frequent on the site, rare across cohort descriptions). Code finds candidates;
    whether they really compete is left to the analysis, which must say so as a judgement."""
    descs = [e for e in entries if e.get("description") and _core(e["name"]) != exclude]
    if not descs:
        return []
    df = Counter(t for e in descs for t in set(_stems(e["description"])))
    n = len(descs)
    site = Counter(_stems(site_text))
    total = sum(site.values()) or 1
    weight = {t: c / total * 1000 * (math.log((n + 1) / (df[t] + 1)) + 1) for t, c in site.items() if t in df and c >= 3}
    profile = dict(sorted(weight.items(), key=lambda kv: -kv[1])[:PROFILE])
    core = set(list(profile)[:CORE])
    scored = []
    for e in descs:
        shared = set(_stems(e["description"])) & set(profile)
        if not shared & core:
            continue
        scored.append({**e, "overlap": round(sum(profile[t] for t in shared), 1), "shared_terms": sorted(shared)})
    scored.sort(key=lambda e: (-e["overlap"], e["name"]))
    return scored[:MAX_PEERS]


class DianaCollector(Collector):
    name = "diana"
    sources = ["NATO DIANA cohort pages via Wayback Machine snapshots (the live site blocks scripts)"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        entries, sources, failed, limited = [], {}, [], False
        for year in range(FIRST_YEAR, date.today().year + 2):
            page = PAGE.format(year=year)
            url = ARCHIVE.format(stamp=f"{date.today().year + 1}", url=page)  # latest snapshot before that
            try:
                r = self._get(ctx, company, url, year, retries=0 if limited else 2)
            except Exception as e:
                failed.append(f"{year}: {type(e).__name__}")
                continue
            if r.status == 404:
                continue  # no such cohort page
            if not r.ok:
                failed.append(f"{year}: HTTP {r.status}")
                limited = limited or r.status in (429, 503)  # later years: one attempt each (cached pages still load)
                continue
            got = parse_cohort(r.text, year)
            if got:
                entries += got
                sources[year] = r.url
        if not entries:
            reason = "; ".join(failed) or "no cohort pages archived"
            return [self.unavailable(company, "nato_diana", PAGE.format(year=date.today().year), reason)]

        core, host = _core(company.name), _host(f"https://{company.domain}" if company.domain else None)
        out = []
        for e in entries:
            if _core(e["name"]) == core or (host and _host(e["url"]) == host):
                out.append(Fact(company_id=company.id, type="accelerator", key=f"nato_diana:{e['year']}",
                                value={"programme": "NATO DIANA", "year": e["year"], "area": e["area"],
                                       "listed_as": e["name"], "description": e["description"]},
                                event_date=str(e["year"]), date_precision="year", source_url=sources[e["year"]],
                                snippet=f"{e['name']} — {e['description'] or e['area'] or ''}"[:300],
                                extractor=self.name))
        site = self._site_text(company, ctx) + " " + " ".join(company.hints.get("sector_terms") or [])
        for p in peers(entries, site, core):
            out.append(Fact(company_id=company.id, type="peer_company", key=f"nato_diana:{p['year']}:{p['name']}",
                            value={"name": p["name"], "website": p["url"], "country": p["country"],
                                   "description": p["description"], "area": p["area"], "year": p["year"],
                                   "list": "NATO DIANA cohort", "overlap": p["overlap"],
                                   "shared_terms": p["shared_terms"]},
                            source_url=sources[p["year"]], snippet=f"{p['name']}: {p['description']}"[:300],
                            extractor=self.name, confidence="medium"))
        if failed:  # a year we could not read is "no data", never "not selected"
            out.append(self.unavailable(company, "nato_diana", PAGE.format(year=date.today().year), "; ".join(failed)))
        if not any(f.type == "accelerator" for f in out):
            out.append(Fact(company_id=company.id, type="source_check", key="nato_diana",
                            value={"source": "NATO DIANA cohorts",
                                   "status": "not_listed_in_checked_years" if failed else "not_listed",
                                   "years_checked": sorted(sources)}, source_url=PAGE.format(year=max(sources)),
                            extractor=self.name))
        return out

    def _get(self, ctx: Context, company: Company, url: str, year: int, retries: int = 2):
        for attempt in range(retries + 1):
            r = ctx.http.get(url, company_id=company.id, kind="page", title=f"NATO DIANA {year} cohort (archived)")
            if r.status not in (429, 503) or attempt == retries:
                return r
            time.sleep(RETRY_WAIT * (attempt + 1))  # a cached 429 is never reused (dd.http.TRANSIENT)
        return r

    def _site_text(self, company: Company, ctx: Context) -> str:
        """Text of the company's own pages saved by the web collector; the home page if none were saved."""
        if not company.domain:
            return ""
        texts = []
        for d in ctx.store.source_docs(company.id):
            if d["text_path"] and _host(d["url"]) and _host(d["url"]).endswith(company.domain.lower()):
                try:
                    texts.append(open(d["text_path"], encoding="utf-8", errors="replace").read()[:20000])
                except OSError:
                    pass
        if texts:
            return " ".join(texts)
        try:
            r = ctx.http.get(f"https://{company.domain}/")
            return html_to_text(r.text)[1] if r.ok else ""
        except Exception:
            return ""
