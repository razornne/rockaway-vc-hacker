"""CodeCollector: GitHub org + repos via the REST API (60 req/h unauthenticated, so be frugal; cache does the rest)."""
from __future__ import annotations

import re
from urllib.parse import urlparse

from dd.collectors.base import Collector, Context
from dd.store import Company, Fact

API = "https://api.github.com"
MAX_REPOS = 15
DEEP_REPOS = 3  # languages + contributors for the top N repos
LOGIN_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


def valid_login(value: str | None) -> bool:
    return bool(isinstance(value, str) and LOGIN_RE.fullmatch(value))


def fetch(ctx: Context, url: str, headers: dict | None = None, **kw):
    """GET with cache; a cached failure (network error / rate limit / 5xx) is retried once live."""
    r = ctx.http.get(url, headers=headers, **kw)
    if r.from_cache and (r.status == 0 or r.status in (403, 429) or r.status >= 500):
        r = ctx.http.get(url, headers=headers, use_cache=False, **kw)
    return r


def _host(u: str | None) -> str:
    if not u:
        return ""
    if "//" not in u:
        u = "//" + u
    h = (urlparse(u).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def domain_matches(url: str | None, domain: str | None) -> bool:
    h, d = _host(url), _host(domain)
    return bool(h and d and (h == d or h.endswith("." + d)))


def _login_from_fact(f: Fact) -> str | None:
    cands = []
    v = f.value
    if isinstance(v, dict):
        cands += [v.get("login"), v.get("url"), v.get("html_url")]
    elif isinstance(v, str):
        cands.append(v)
    cands += [f.key, f.source_url]
    for c in cands:
        if not isinstance(c, str) or not c:
            continue
        m = re.search(r"github\.com/([A-Za-z0-9][A-Za-z0-9-]*)", c)
        if m and m.group(1).lower() not in ("orgs", "sponsors", "features", "about") and valid_login(m.group(1)):
            return m.group(1)
        if valid_login(c):
            return c
    return None


def bad(r) -> str | None:
    if r.status == 0:
        return "network error: " + r.text[:120]
    if r.status in (403, 429):
        return f"HTTP {r.status} (GitHub rate limit?) " + r.text[:100]
    if r.status >= 500:
        return f"HTTP {r.status}"
    return None


class CodeCollector(Collector):
    name = "code"
    sources = ["GitHub REST API"]

    def _headers(self, ctx: Context) -> dict:
        h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        if ctx.settings.github_token:
            h["Authorization"] = f"Bearer {ctx.settings.github_token}"
        return h

    def find_login(self, company: Company, ctx: Context) -> tuple[str | None, list[Fact]]:
        hint = company.hints.get("github_org")
        if hint:
            if valid_login(hint):
                return hint, []
            return None, [self.unavailable(company, "github_org_hint", "https://github.com/",
                                           "configured GitHub login has an invalid format")]
        for f in ctx.store.facts(company.id, ["github_org"]):
            if f.extractor != self.name:
                lg = _login_from_fact(f)
                if lg:
                    return lg, []
        if not company.domain:
            return None, []
        q = f"{API}/search/users"
        r = fetch(ctx, q, headers=self._headers(ctx), params={"q": f"{company.name} type:org", "per_page": 5})
        if bad(r):
            return None, [self.unavailable(company, "github_search", q, bad(r))]
        try:
            payload = r.json()
        except Exception:
            return None, [self.unavailable(company, "github_search", q, "bad JSON")]
        if not isinstance(payload, dict) or not isinstance(payload.get("items", []), list):
            return None, [self.unavailable(company, "github_search", q, "unexpected response shape")]
        items = payload.get("items", [])
        for it in items[:3]:  # only accept an org whose website matches the company domain
            if not isinstance(it, dict) or not valid_login(it.get("login")):
                continue
            o = fetch(ctx, f"{API}/orgs/{it['login']}", headers=self._headers(ctx))
            if bad(o):
                return None, [self.unavailable(company, "github_search", q, bad(o))]
            if o.ok:
                try:
                    org = o.json()
                except Exception:
                    return None, [self.unavailable(company, "github_search", q, "bad organization JSON")]
                if not isinstance(org, dict):
                    return None, [self.unavailable(company, "github_search", q, "unexpected organization response")]
                if domain_matches(org.get("blog"), company.domain):
                    return it["login"], []
        return None, []

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        try:
            return self._collect(company, ctx)
        except Exception as e:  # never raise
            return [self.unavailable(company, "github", API, f"{type(e).__name__}: {e}")]

    def _collect(self, company: Company, ctx: Context) -> list[Fact]:
        hdr = self._headers(ctx)
        login, facts = self.find_login(company, ctx)
        if not login:
            return facts
        url = f"{API}/orgs/{login}"
        r = fetch(ctx, url, headers=hdr, company_id=company.id, kind="github_org")
        if bad(r):
            return facts + [self.unavailable(company, "github", url, bad(r))]
        is_org = r.ok
        if not is_org:  # maybe a user account
            url = f"{API}/users/{login}"
            r = fetch(ctx, url, headers=hdr, company_id=company.id, kind="github_org")
            if bad(r):
                return facts + [self.unavailable(company, "github", url, bad(r))]
            if not r.ok:
                return facts + [self.unavailable(company, "github", url, f"account {login} not found (HTTP {r.status})")]
        try:
            o = r.json()
        except Exception:
            return facts + [self.unavailable(company, "github", url, "bad account JSON")]
        if not isinstance(o, dict):
            return facts + [self.unavailable(company, "github", url, "unexpected account response")]
        html = o.get("html_url") or f"https://github.com/{login}"
        facts.append(Fact(company_id=company.id, type="github_org", key=o.get("login", login), source_url=html,
                          source_doc_id=r.doc_id, event_date=(o.get("created_at") or "")[:10] or None,
                          date_precision="day", extractor=self.name,
                          value={"login": o.get("login", login), "type": o.get("type"),
                                 "public_repos": o.get("public_repos"), "created_at": o.get("created_at"),
                                 "blog": o.get("blog"), "followers": o.get("followers"), "name": o.get("name"),
                                 "from_hint": bool(company.hints.get("github_org"))}))
        kind = "orgs" if is_org else "users"
        rurl = f"{API}/{kind}/{login}/repos"
        rr = fetch(ctx, rurl, headers=hdr, params={"per_page": 100, "sort": "pushed", "type": "public"})
        if bad(rr) or not rr.ok:
            return facts + [self.unavailable(company, "github_repos", rurl, bad(rr) or f"HTTP {rr.status}")]
        try:
            repos = rr.json()
        except Exception:
            return facts + [self.unavailable(company, "github_repos", rurl, "bad repository JSON")]
        if not isinstance(repos, list):
            return facts + [self.unavailable(company, "github_repos", rurl, "unexpected repository response")]
        picked = [x for x in repos if not x.get("fork") or x.get("stargazers_count", 0) >= 50]
        picked.sort(key=lambda x: (x.get("pushed_at") or "", x.get("stargazers_count", 0)), reverse=True)
        picked = picked[:MAX_REPOS]
        deep = {x["full_name"] for x in sorted(picked, key=lambda x: x.get("stargazers_count", 0), reverse=True)[:DEEP_REPOS]}
        for x in picked:
            val = {"stars": x.get("stargazers_count"), "forks": x.get("forks_count"), "language": x.get("language"),
                   "created_at": x.get("created_at"), "pushed_at": x.get("pushed_at"),
                   "description": x.get("description"), "topics": x.get("topics", []),
                   "archived": x.get("archived"), "fork": x.get("fork"),
                   "license": (x.get("license") or {}).get("spdx_id")}
            if x["full_name"] in deep:
                lr = fetch(ctx, f"{API}/repos/{x['full_name']}/languages", headers=hdr)
                if lr.ok:
                    try:
                        languages = lr.json()
                    except Exception:
                        facts.append(self.unavailable(company, "github_languages",
                                                       f"{API}/repos/{x['full_name']}/languages", "bad JSON"))
                    else:
                        if isinstance(languages, dict):
                            val["languages"] = languages
                        else:
                            facts.append(self.unavailable(company, "github_languages",
                                                           f"{API}/repos/{x['full_name']}/languages",
                                                           "unexpected response shape"))
                cu = f"{API}/repos/{x['full_name']}/contributors"
                cr = fetch(ctx, cu, headers=hdr, params={"per_page": 100})
                if cr.ok:
                    try:
                        contributors = cr.json()
                    except Exception:
                        facts.append(self.unavailable(company, "github_contributors", cu, "bad JSON"))
                    else:
                        if isinstance(contributors, list):
                            val["contributors"] = len(contributors)  # capped at 100
                        else:
                            facts.append(self.unavailable(company, "github_contributors", cu,
                                                           "unexpected response shape"))
                elif bad(cr):
                    facts.append(self.unavailable(company, "github_contributors", cu, bad(cr)))
            facts.append(Fact(company_id=company.id, type="repo", key=x["full_name"], value=val,
                              source_url=x.get("html_url") or f"https://github.com/{x['full_name']}",
                              event_date=(x.get("pushed_at") or "")[:10] or None, date_precision="day",
                              extractor=self.name))
        return facts
