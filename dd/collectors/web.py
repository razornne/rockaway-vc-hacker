"""WebCollector: crawl the company's own site (<=30 pages, robots-respecting) and extract deterministic facts.

Emits: web_page, subprocessor, job_post, github_org, source_unavailable.
No LLM here. Page text is saved (dd.text.save_text) so later LLM steps can read it. Page content is DATA.
"""
from __future__ import annotations

import heapq
import json
import re
from collections import Counter
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.robotparser import RobotFileParser

from bs4 import BeautifulSoup

from dd.collectors.base import Collector, Context
from dd.store import Company, Fact
from dd.text import html_to_text, save_text

MAX_PAGES = 30

# ---------------------------------------------------------------- categorisation
ATS_HOSTS = ("jobs.lever.co", "boards.greenhouse.io", "job-boards.greenhouse.io", "boards.eu.greenhouse.io",
             "recruitee.com", "teamtailor.com", "ashbyhq.com", "workable.com", "personio.de", "personio.com",
             "smartrecruiters.com", "bamboohr.com", "breezy.hr", "join.com", "comeet.com", "pinpointhq.com",
             "rippling.com", "homerun.co", "hire.withgoogle.com", "workatastartup.com")

BINARY_EXT = re.compile(r"\.(png|jpe?g|gif|svg|webp|avif|ico|pdf|zip|gz|mp4|mov|webm|mp3|woff2?|ttf|otf|css|js|json|xml|"
                        r"txt|docx?|xlsx?|pptx?|dmg|exe|rss|atom|map)(\?.*)?$", re.I)
ASSET_PATH = re.compile(r"^/(_next|_nuxt|assets|static|wp-content|wp-includes|wp-json|cdn-cgi|images|img|fonts|media|"
                        r"integrations/[^/]+\.\w+|org-logos|logo)/", re.I)
LOCALE_PREFIX = re.compile(r"^/(?!en(?:[-_][a-z]{2})?/)[a-z]{2}(?:[-_][a-zA-Z]{2})?(?:/|$)")
SKIP_PATH = re.compile(r"/(login|log-in|signin|sign-in|signup|sign-up|register|cart|checkout|account|unsubscribe|"
                       r"feed|tag|tags|author|category|page/\d+)(/|$)", re.I)

# order matters: first match wins
CATEGORY_RULES: list[tuple[str, re.Pattern]] = [
    ("privacy", re.compile(r"privacy|subprocessor|sub-processor|data-processing|\bdpa\b|gdpr|cookie|datenschutz|"
                           r"ochrana-osobnich|zasady-ochrany", re.I)),
    ("security", re.compile(r"security|trust|compliance|soc-?2|iso-?27001|certification", re.I)),
    ("careers", re.compile(r"career|\bjobs?\b|join-us|join-our|work-with-us|work-at|hiring|vacanc|openings?|"
                           r"positions?|kariera|pozice|recruit", re.I)),
    ("pricing", re.compile(r"pricing|\bplans?\b|\bprices?\b|cenik|ceník", re.I)),
    ("docs", re.compile(r"\bdocs?\b|documentation|developers?|\bapi\b|reference|guides?|help|knowledge|"
                        r"get-started|quickstart", re.I)),
    ("changelog", re.compile(r"changelog|release-notes|releases|whats-new|what-s-new|product-updates", re.I)),
    ("customers", re.compile(r"customers?|case-stud|success-stor|testimonial|references", re.I)),
    ("product", re.compile(r"product|features?|platform|solutions?|use-cases?|how-it-works|technology|"
                           r"capabilit|industries|automation|offers?", re.I)),
    ("about", re.compile(r"\babout|\bteam\b|company|people|mission|our-story|culture|who-we-are|o-nas", re.I)),
    ("blog", re.compile(r"blog|news|press|insights|articles|resources|stories|events", re.I)),
]
PRIORITY = {"careers": 0, "privacy": 0, "security": 1, "product": 1, "pricing": 1, "docs": 1, "about": 2,
            "customers": 2, "changelog": 2, "blog": 3, "other": 5}
CAP = {"careers": 10, "privacy": 4, "security": 3, "product": 6, "pricing": 2, "docs": 5, "about": 3,
       "customers": 3, "changelog": 2, "blog": 3, "other": 2, "home": 1}
HOST_HINT = {"docs": "docs", "developers": "docs", "developer": "docs", "api": "docs", "help": "docs",
             "support": "docs", "trust": "security", "security": "security", "blog": "blog",
             "careers": "careers", "jobs": "careers", "status": "other"}


def is_ats(host: str) -> bool:
    return any(host == h or host.endswith("." + h) for h in ATS_HOSTS)


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def ats_tenant(url: str, company: Company) -> bool:
    """Is this ATS URL the company's own board (vermeer.homerun.co, jobs.lever.co/valka), not the ATS vendor's site?

    Without this guard a careers link to homerun.co pulled the vendor's marketing pages (and its customers) into the
    company's dossier."""
    p = urlparse(url)
    host = p.netloc.lower()
    base = next((h for h in ATS_HOSTS if host == h or host.endswith("." + h)), "")
    sub = host[: -len(base)].rstrip(".") if base and host != base else ""
    parts = [x for x in p.path.split("/") if x]
    cands = [x for x in sub.split(".") if x not in ("www", "jobs", "careers", "app", "apply", "boards", "job-boards")]
    cands += parts[:2]
    keys = {_slug(company.name), _slug((company.domain or "").split(".")[0]), _slug(company.id)}
    keys |= {_slug(w) for w in re.findall(r"[A-Za-z0-9]+", company.name or "") if len(w) >= 4}
    keys.discard("")
    for c in map(_slug, cands):
        if len(c) >= 3 and any(c == k or (len(c) >= 4 and (c in k or k in c)) for k in keys):
            return True
    return False


def categorize(url: str, anchor: str = "", site_domain: str = "") -> str:
    p = urlparse(url)
    host = p.netloc.lower()
    if is_ats(host):
        return "careers"
    label = host.split(".")[0]
    path = p.path.lower()
    if host != site_domain and label in HOST_HINT and path.strip("/") == "":
        return HOST_HINT[label]
    if re.match(r"^/(blog|news|press|stories|insights|articles|resources|events)/.+", path):
        return "blog"
    if path.strip("/") == "":
        return HOST_HINT.get(label, "home") if host != site_domain else "home"
    for cat, rx in CATEGORY_RULES:
        if rx.search(path):
            return cat
    if host != site_domain and label in HOST_HINT:
        return HOST_HINT[label]
    a = (anchor or "").strip().lower()
    if a and len(a) < 40:
        for cat, rx in CATEGORY_RULES:
            if cat != "blog" and rx.search(a):
                return cat
    return "other"


# ---------------------------------------------------------------- subprocessors
# canonical name -> regex (word-bounded, case-insensitive). Order is irrelevant; each vendor matched independently.
VENDORS: dict[str, str] = {
    "OpenAI": r"open\s?ai(?!\s*(?:for|compatible))", "Azure OpenAI": r"azure\s+open\s?ai",
    "Anthropic": r"anthropic|claude\b", "Cohere": r"cohere", "Mistral": r"mistral(?:\s?ai)?",
    "Hugging Face": r"hugging\s?face", "Google Cloud": r"google\s+cloud|gcp\b|vertex\s?ai|gemini",
    "Google Analytics": r"google\s+analytics", "AWS": r"\baws\b|amazon\s+web\s+services|amazon\s+bedrock",
    "Microsoft Azure": r"microsoft\s+azure|\bazure\b", "Pinecone": r"pinecone", "Weaviate": r"weaviate",
    "Qdrant": r"qdrant", "Supabase": r"supabase", "Vercel": r"vercel", "Netlify": r"netlify",
    "Cloudflare": r"cloudflare", "Stripe": r"stripe", "Intercom": r"intercom", "HubSpot": r"hubspot",
    "Segment": r"\bsegment(?:\.io|\s+(?:io|inc))\b|twilio\s+segment", "Mixpanel": r"mixpanel",
    "Amplitude": r"amplitude", "PostHog": r"posthog", "Sentry": r"sentry", "Datadog": r"datadog",
    "Twilio": r"twilio", "SendGrid": r"sendgrid", "Mailgun": r"mailgun", "Postmark": r"postmark",
    "Zendesk": r"zendesk", "Salesforce": r"salesforce", "Snowflake": r"snowflake", "MongoDB": r"mongodb",
    "Databricks": r"databricks", "Slack": r"\bslack\b", "Atlassian": r"atlassian|jira\b",
    "Notion": r"\bnotion\b", "Linear": r"\blinear\.app\b", "GitHub": r"\bgithub\b", "Heroku": r"heroku",
    "DigitalOcean": r"digitalocean|digital\s+ocean", "Hetzner": r"hetzner", "OVHcloud": r"ovh(?:cloud)?",
    "Elastic": r"elastic(?:search|\s+cloud)", "Auth0": r"auth0|\bokta\b", "Clerk": r"\bclerk\b",
    "Fireworks AI": r"fireworks\s?ai", "Together AI": r"together\s?ai", "Replicate": r"replicate\.com",
    "Groq": r"\bgroq\b", "Deepgram": r"deepgram", "ElevenLabs": r"elevenlabs", "Whisper": r"\bwhisper\b",
    "Langfuse": r"langfuse", "LangChain": r"langchain|langsmith", "Weights & Biases": r"weights\s*(?:&|and)\s*biases",
    "Mailchimp": r"mailchimp", "Brevo": r"brevo|sendinblue", "Typeform": r"typeform", "Calendly": r"calendly",
    "Hotjar": r"hotjar", "LinkedIn": r"linkedin\s+(?:insight|ads|pixel)", "Meta": r"meta\s+pixel|facebook\s+pixel",
    "Vimeo": r"vimeo", "Zapier": r"zapier", "Airtable": r"airtable", "Webflow": r"webflow", "Framer": r"\bframer\b",
    "Fly.io": r"fly\.io", "Render": r"render\.com", "Railway": r"railway\.app", "Redis": r"redis",
    "Confluent": r"confluent", "Fivetran": r"fivetran", "dbt": r"\bdbt\b", "Vanta": r"\bvanta\b",
    "Drata": r"\bdrata\b", "Paddle": r"\bpaddle\b", "Chargebee": r"chargebee", "Pipedrive": r"pipedrive",
    "Crisp": r"\bcrisp\b", "Freshdesk": r"freshdesk|freshworks", "Loom": r"\bloom\b", "Zoom": r"\bzoom\b",
}
VENDOR_RX = {v: re.compile(r"(?<![\w-])(?:" + rx + r")(?![\w-])", re.I) for v, rx in VENDORS.items()}
# vendors too ambiguous in prose to trust from non-subprocessor sentences
AMBIGUOUS = {"Sentry", "Segment", "Render", "Linear", "Clerk", "Crisp", "Loom", "Zoom", "Paddle", "Notion",
             "Slack", "Elastic", "Redis", "dbt", "Meta", "Whisper", "Amplitude", "Stripe"}
SUBPROC_CATS = {"privacy", "security"}


def main_text(html: str) -> str:
    """Body text without navigation / mega-menus / footers (their link lists look like vendor lists)."""
    soup = BeautifulSoup(html, "lxml")
    for t in soup(["script", "style", "noscript", "svg", "iframe", "template", "nav", "header", "footer", "aside"]):
        t.decompose()
    for t in soup.select('[role=navigation], [role=banner], [role=contentinfo]'):
        t.decompose()
    root = soup.find("main") or soup.find("article") or soup.body or soup
    text = root.get_text("\n")
    text = re.sub(r"[ \t\xa0]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n", text).strip()


def split_sentences(text: str) -> list[str]:
    out = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if len(line) > 400:
            out.extend(s.strip() for s in re.split(r"(?<=[.;!?])\s+", line) if s.strip())
        else:
            out.append(line)
    return out


def extract_subprocessors(text: str) -> dict[str, str]:
    """vendor -> first exact sentence/line mentioning it. Only trusts lists/sentences about processors/hosting/AI."""
    context_rx = re.compile(r"process|provider|vendor|host|infrastructure|third[- ]part|service|storage|analytics|"
                            r"model|ai\b|cloud|payment|email|support|partner|sub-?contract|data", re.I)
    found: dict[str, str] = {}
    sents = split_sentences(text)
    for i, s in enumerate(sents):
        for vendor, rx in VENDOR_RX.items():
            if vendor in found or not rx.search(s):
                continue
            if vendor in AMBIGUOUS:
                # require processor-ish wording in this line or its neighbours
                ctx = " ".join(sents[max(0, i - 1): i + 2])
                if not re.search(r"sub-?processor|processor|third[- ]part|service provider|vendor", ctx, re.I):
                    continue
            elif not context_rx.search(s) and len(s) > 80:
                continue
            snip = s
            j = i + 1
            while len(snip) < 60 and j < len(sents) and j <= i + 3 and len(snip) + len(sents[j]) < 300:
                snip += " " + sents[j]  # short list item: add the description lines that follow
                j += 1
            found[vendor] = snip[:400]
    return found


# ---------------------------------------------------------------- jobs
ML_RX = re.compile(r"\b(ml|machine[- ]learning|ai|a\.i\.|artificial intelligence|llm|nlp|deep[- ]learning|"
                   r"computer vision|data scien\w+|research(?:er)?|applied scien\w+|mlops|genai|generative)\b", re.I)
JOB_WORD = re.compile(r"engineers?\b|developers?\b|designers?\b|manager|scientist|analyst|architect|lead\b|head of|director|"
                      r"intern\b|internship|specialist|researcher|consultant|officer|sales|account|marketing|"
                      r"recruiter|coordinator|associate|executive|representative|writer|devops|sre\b|qa\b|tester|"
                      r"product|support|success|operations|founder|cto|cfo|ceo|vp\b|president|administrator|"
                      r"programmer|inženýr|vývojář|specialista|manažer|praktikant", re.I)
NON_ML = re.compile(r"front[- ]?end|back[- ]?end|full[- ]?stack|sales|account|marketing|designer|support|recruit|"
                    r"finance|legal|people|operations", re.I)
NOT_JOB = re.compile(r"^(careers?|jobs?|open (?:positions?|roles?)|view all|see all|all (?:jobs|positions|roles)|"
                     r"apply|apply now|learn more|read more|back|home|join us|join the team|work with us|"
                     r"powered by|privacy|terms|cookie|login|sign in|filter|search|show more|load more|"
                     r"no open positions.*|\d+ open positions?)$", re.I)
JOB_HREF = re.compile(r"/(jobs?|careers?|positions?|openings?|o|vacanc\w+|apply|postings?|roles?|kariera|pozice)/[^/?#]+",
                      re.I)


def _clean(s: str | None) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip()


def _job(title: str, team: str | None = None, location: str | None = None, url: str | None = None) -> dict | None:
    title = _clean(title)
    if not (3 <= len(title) <= 120) or NOT_JOB.match(title):
        return None
    team = re.sub(r"^\d{2}-\d{4}(?:\.\d+)?\s*", "", _clean(team))  # drop O*NET codes
    if " " not in title and not re.search(r"engineer|developer|designer|scientist|manager|intern", title, re.I):
        return None  # single words are department headings ("Sales", "Engineering")
    return {"title": title, "team": team or None, "location": _clean(location) or None,
            "is_ml": bool(ML_RX.search(title)) and not NON_ML.search(title), "url": url}


def jobs_from_jsonld(soup: BeautifulSoup) -> list[dict]:
    out = []
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(tag.string or "")
        except (ValueError, TypeError):
            continue
        stack = data if isinstance(data, list) else [data]
        while stack:
            d = stack.pop()
            if isinstance(d, list):
                stack.extend(d)
            elif isinstance(d, dict):
                if "@graph" in d:
                    stack.extend(d["@graph"])
                if str(d.get("@type")) == "JobPosting":
                    loc = d.get("jobLocation")
                    if isinstance(loc, list):
                        loc = loc[0] if loc else None
                    addr = (loc or {}).get("address", {}) if isinstance(loc, dict) else {}
                    place = ", ".join(x for x in (addr.get("addressLocality"), addr.get("addressCountry")) if isinstance(x, str))
                    j = _job(d.get("title") or d.get("name") or "", d.get("occupationalCategory") or None, place,
                             d.get("url"))
                    if j:
                        out.append(j)
    return out


def extract_jobs_html(html: str, page_url: str) -> list[dict]:
    """Generic + ATS-specific job-title extraction from a careers/ATS listing page."""
    soup = BeautifulSoup(html, "lxml")
    jobs = jobs_from_jsonld(soup)
    if len(jobs) == 1:  # a single-posting detail page: do not mine its sidebar links
        return jobs
    host = urlparse(page_url).netloc.lower()
    # Lever
    for div in soup.select("div.posting"):
        a = div.select_one("a.posting-title") or div
        t = a.select_one("[data-qa=posting-name]") or a.select_one("h5")
        j = _job(t.get_text() if t else "", (div.select_one(".sort-by-team") or div).get_text() if div.select_one(".sort-by-team") else None,
                 div.select_one(".sort-by-location").get_text() if div.select_one(".sort-by-location") else None,
                 a.get("href") if a.name == "a" else None)
        if j:
            jobs.append(j)
    # Greenhouse (classic + new boards)
    for div in soup.select("div.opening, tr.job-post"):
        a = div.find("a")
        loc = div.select_one(".location, p.body__secondary")
        dep = None
        sec = div.find_previous(["h3", "h4"], class_=re.compile("department|section|job-posts--department", re.I))
        if sec:
            dep = sec.get_text()
        if a:
            j = _job((a.select_one("p.body--medium") or a).get_text(), dep, loc.get_text() if loc else None, a.get("href"))
            if j:
                jobs.append(j)
    # Recruitee
    for a in soup.select('a[href*="/o/"]'):
        if "recruitee" in host or "/o/" in a.get("href", ""):
            j = _job(a.get_text(" "), None, None, a.get("href"))
            if j and (is_ats(host) or JOB_WORD.search(j["title"])):
                jobs.append(j)
    # Teamtailor / Personio / generic: <a href=".../jobs/<slug>">
    if not jobs:
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if not JOB_HREF.search(urlparse(href).path):
                continue
            title = a.get("title") or a.get_text(" ")
            h = a.find(["h2", "h3", "h4", "h5", "span"])
            if h and 3 < len(_clean(h.get_text())) < 120:
                title = h.get_text(" ")
            if len(_clean(title)) > 90:
                continue
            j = _job(title, None, None, href)
            if j and JOB_WORD.search(j["title"]):
                jobs.append(j)
    # de-dup by title
    seen, out = set(), []
    for j in jobs:
        k = j["title"].lower()
        if k not in seen:
            seen.add(k)
            out.append(j)
    return out


def jobs_from_ats_api(ctx: Context, company: Company, url: str) -> list[tuple[str, dict]]:
    """Public JSON endpoints of common ATSs (structured → code). Returns [(source_url, job)]."""
    p = urlparse(url)
    host, parts = p.netloc.lower(), [x for x in p.path.split("/") if x]
    out: list[tuple[str, dict]] = []
    try:
        if host == "jobs.lever.co" and parts:
            api = f"https://api.lever.co/v0/postings/{parts[0]}?mode=json"
            r = ctx.http.get(api)
            for d in (r.json() if r.ok else []):
                cat = d.get("categories", {})
                j = _job(d.get("text", ""), cat.get("team"), cat.get("location"), d.get("hostedUrl"))
                if j:
                    out.append((url, j))
        elif host.endswith("greenhouse.io") and parts:
            slug = parts[0]
            api = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
            r = ctx.http.get(api)
            for d in (r.json().get("jobs", []) if r.ok else []):
                j = _job(d.get("title", ""), None, (d.get("location") or {}).get("name"), d.get("absolute_url"))
                if j:
                    out.append((url, j))
        elif host.endswith(".recruitee.com"):
            r = ctx.http.get(f"https://{host}/api/offers/")
            for d in (r.json().get("offers", []) if r.ok else []):
                j = _job(d.get("title", ""), d.get("department"), d.get("location"), d.get("careers_url"))
                if j:
                    out.append((url, j))
        elif host == "apply.workable.com" and parts:
            r = ctx.http.post(f"https://apply.workable.com/api/v3/accounts/{parts[0]}/jobs",
                              json_body={"query": "", "location": [], "department": [], "worktype": [], "remote": []})
            for d in (r.json().get("results", []) if r.ok else []):
                loc = d.get("location") or {}
                j = _job(d.get("title", ""), (d.get("department") or [None])[0] if isinstance(d.get("department"), list) else None,
                         ", ".join(x for x in (loc.get("city"), loc.get("country")) if x),
                         f"https://apply.workable.com/{parts[0]}/j/{d.get('shortcode')}/")
                if j:
                    out.append((url, j))
    except Exception:  # noqa: BLE001 - APIs are best-effort; HTML parsing is the fallback
        return []
    return out


# ---------------------------------------------------------------- github orgs
GH_RESERVED = {"features", "about", "pricing", "enterprise", "sponsors", "orgs", "marketplace", "topics", "login",
               "join", "settings", "collections", "readme", "security", "contact", "site", "explore", "apps",
               "notifications", "pulls", "issues", "search", "customer-stories", "team", "solutions", "resources",
               "premium-support", "why-github", "trending", "new", "organizations", "users", "events", "github",
               "docs", "login", "signup", "partners", "copilot", "actions", "codespaces", "mobile"}
GH_RX = re.compile(r"https?://(?:www\.)?github\.com/([A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))(?:/[^\s\"'<>)]*)?", re.I)


def github_orgs(html: str) -> list[str]:
    out = []
    for m in GH_RX.finditer(html):
        login = m.group(1)
        if login.lower() in GH_RESERVED or login in out:
            continue
        out.append(login)
    return out


# ---------------------------------------------------------------- sitemap
def parse_sitemap(xml: str) -> tuple[list[str], list[str]]:
    """Return (page urls, nested sitemap urls)."""
    soup = BeautifulSoup(xml, "lxml-xml")
    subs = [l.get_text(strip=True) for sm in soup.find_all("sitemap") for l in sm.find_all("loc")]
    urls = [l.get_text(strip=True) for u in soup.find_all("url") for l in u.find_all("loc")]
    return urls, subs


def extract_links(html: str, base: str) -> list[tuple[str, str]]:
    soup = BeautifulSoup(html, "lxml")
    out = []
    for a in soup.find_all("a", href=True):
        h = a["href"].strip()
        if not h or h.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        u = urljoin(base, h)
        p = urlparse(u)
        if p.scheme not in ("http", "https"):
            continue
        u = urlunparse((p.scheme, p.netloc.lower(), p.path or "/", "", p.query if is_ats(p.netloc.lower()) else "", ""))
        out.append((u, _clean(a.get_text(" "))[:80]))
    return out


# ---------------------------------------------------------------- collector
class WebCollector(Collector):
    name = "web"
    sources = ["company website (robots.txt, sitemap.xml, <=30 pages)", "ATS job boards (public JSON/HTML)"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        if not company.domain:
            return [self.unavailable(company, "web", company.id, "no domain known")]
        domain = company.domain.lower().removeprefix("www.")
        facts: list[Fact] = []
        home = None
        for start in (f"https://{domain}/", f"https://www.{domain}/", f"http://{domain}/"):
            r = ctx.http.get(start, company_id=company.id, kind="page")
            if r.ok and "html" in r.content_type.lower():
                home, home_url = r, start
                break
        if home is None:
            return [self.unavailable(company, "web", f"https://{domain}/", "homepage not reachable")]
        site_host = urlparse(home.url).netloc.lower()
        base = f"{urlparse(home.url).scheme}://{site_host}"

        robots = RobotFileParser()
        robots_txt = ""
        rr = ctx.http.get(f"{base}/robots.txt")
        if rr.ok and "html" not in rr.content_type.lower():
            robots_txt = rr.text
            robots.parse(robots_txt.splitlines())
        else:
            robots.parse([])
        robots_by_host = {site_host: robots}

        def allowed(u: str) -> bool:
            p = urlparse(u)
            host = p.netloc.lower()
            host_rules = robots_by_host.get(host)
            if host_rules is None:
                host_rules = RobotFileParser()
                rules_url = f"{p.scheme}://{host}/robots.txt"
                rules_resp = ctx.http.get(rules_url)
                if rules_resp.ok and "html" not in rules_resp.content_type.lower():
                    host_rules.parse(rules_resp.text.splitlines())
                else:
                    # Preserve the existing fail-open behavior when robots.txt is absent or unavailable.
                    host_rules.parse([])
                robots_by_host[host] = host_rules
            return host_rules.can_fetch("*", u)

        def same_site(host: str) -> bool:
            return host == domain or host.endswith("." + domain) or host == site_host

        # ---- candidate queue
        heap: list[tuple[int, int, str, str]] = []
        queued: set[str] = {home.url, home_url}
        counter = 0
        cat_count: Counter = Counter()

        def push(url: str, anchor: str = "", boost: int = 0) -> None:
            nonlocal counter
            p = urlparse(url)
            host = p.netloc.lower()
            if url in queued or p.scheme not in ("http", "https"):
                return
            ats = is_ats(host)
            if ats and not ats_tenant(url, company):
                return  # the ATS vendor's own site, not the company's job board
            if not (same_site(host) or ats):
                return
            if BINARY_EXT.search(p.path) or ASSET_PATH.match(p.path) or SKIP_PATH.search(p.path):
                return
            if not ats and LOCALE_PREFIX.match(p.path):
                return
            if host.split(".")[0] in ("app", "console", "dashboard", "admin", "portal") and host != site_host:
                return
            cat = categorize(url, anchor, site_host if host == site_host else domain)
            if cat == "home" and url != base + "/":
                cat = "other"
            queued.add(url)
            depth = len([x for x in p.path.split("/") if x])
            counter += 1
            heapq.heappush(heap, (PRIORITY.get(cat, 5) * 10 + min(depth, 5) + boost, counter, url, cat))

        home_html = home.text
        for u, a in extract_links(home_html, home.url):
            push(u, a)

        # sitemap(s)
        sm_urls = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", robots_txt) or [f"{base}/sitemap.xml"]
        seen_sm, sm_queue, sm_pages = set(), list(sm_urls[:3]), 0
        while sm_queue and sm_pages < 400:
            sm = sm_queue.pop(0)
            if sm in seen_sm or len(seen_sm) >= 5:
                continue
            seen_sm.add(sm)
            r = ctx.http.get(sm)
            if not r.ok or "<" not in r.text[:200]:
                continue
            try:
                urls, subs = parse_sitemap(r.text)
            except Exception:  # noqa: BLE001
                continue
            sm_queue.extend(subs[:5])
            for u in urls[:300]:
                sm_pages += 1
                # sitemap pages are lower-confidence than homepage links: slight depth penalty
                push(u, "", boost=1)

        # ---- crawl
        fetched: list[tuple[str, str, str]] = []  # url, cat, text
        orgs_seen: dict[str, str] = {}
        jobs: dict[str, tuple[str, int | None, dict]] = {}  # title -> (source_url, doc_id, job)

        def process(url: str, cat: str, resp, html: str) -> None:
            title, text = html_to_text(html)
            doc_title = title
            save_text(ctx.store, resp, text, title)
            facts.append(Fact(company_id=company.id, type="web_page", key=cat,
                              value={"url": url, "title": doc_title, "chars": len(text)}, source_url=url,
                              source_doc_id=resp.doc_id, extractor=self.name))
            for login in github_orgs(html):
                orgs_seen.setdefault(login, url)
            if cat in SUBPROC_CATS or re.search(r"subprocessor|sub-processor|dpa", url, re.I):
                for vendor, sent in extract_subprocessors(main_text(html)).items():
                    facts.append(Fact(company_id=company.id, type="subprocessor", key=vendor,
                                      value={"vendor": vendor, "page": url}, source_url=url,
                                      source_doc_id=resp.doc_id, snippet=sent, extractor=self.name,
                                      confidence="medium"))
            if cat == "careers":
                found = [(url, j) for j in extract_jobs_html(html, url)]
                if is_ats(urlparse(url).netloc.lower()):
                    api = jobs_from_ats_api(ctx, company, url)
                    if api:
                        found = api
                for src, j in found:
                    if j.get("url"):
                        j["url"] = urljoin(src, j["url"])
                    old = jobs.get(j["title"].lower())
                    if old:  # same role seen on listing and detail page: fill the gaps
                        for f in ("team", "location", "url"):
                            old[2][f] = old[2].get(f) or j.get(f)
                    else:
                        jobs[j["title"].lower()] = (src, resp.doc_id, j)
                # discover ATS boards / job detail links from careers pages
                for u, a in extract_links(html, url):
                    h = urlparse(u).netloc.lower()
                    if is_ats(h):
                        push(u, a, boost=-3)
                    elif same_site(h) and JOB_HREF.search(urlparse(u).path) and cat_count["careers"] < 4:
                        push(u, a)

        def fetch(url: str, cat: str, first: bool = False):
            r = ctx.http.get(url, company_id=company.id, kind="page", title=cat)
            if not r.ok:
                return
            ct = r.content_type.lower()
            if "html" not in ct and "xml" not in ct:
                return
            html = r.text
            process(r.url if first else url, cat, r, html)
            fetched.append((url, cat, html))

        # homepage
        fetch(home.url, "home", first=True)
        cat_count["home"] += 1
        while heap and len(fetched) < MAX_PAGES:
            _, _, url, cat = heapq.heappop(heap)
            if cat_count[cat] >= CAP.get(cat, 2):
                continue
            if not allowed(url):
                ctx.log.info("robots.txt disallows %s", url)
                continue
            cat_count[cat] += 1
            try:
                fetch(url, cat)
            except Exception as e:  # noqa: BLE001 - one bad page must not kill the crawl
                ctx.log.warning("web: %s failed: %s", url, e)
                facts.append(self.unavailable(company, "web_page", url, f"parse error: {e}"))

        for src, doc_id, j in jobs.values():
            facts.append(Fact(company_id=company.id, type="job_post", key=j["title"][:100],
                              value={x: j[x] for x in ("title", "team", "location", "is_ml", "url")},
                              source_url=src, source_doc_id=doc_id, extractor=self.name))
        slug = re.sub(r"[^a-z0-9]", "", company.name.lower())
        label = re.sub(r"[^a-z0-9]", "", domain.split(".")[0])
        for login, found_on in orgs_seen.items():
            norm = re.sub(r"[^a-z0-9]", "", login.lower())
            likely = any(x and (x in norm or norm in x) for x in (slug, label))
            facts.append(Fact(company_id=company.id, type="github_org", key=login,
                              value={"login": login, "found_on": found_on, "name_match": likely},
                              source_url=found_on, extractor=self.name, confidence="medium" if likely else "low"))
        return facts
