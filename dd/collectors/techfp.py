"""Deterministic website, DNS and certificate-transparency fingerprints."""
from __future__ import annotations

import json
import re
from datetime import date
from urllib.parse import quote, urlparse

from bs4 import BeautifulSoup

from dd.collectors.base import Collector, Context
from dd.store import Company, Fact

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$", re.I)
MAX_SUBDOMAINS = 200

# Fingerprints are deliberately tied to concrete markers in the returned HTML or headers.
HTML_MARKERS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("framework", "Next.js", ("__next_data__", "/_next/static/")),
    ("framework", "Nuxt", ("__nuxt__", "/_nuxt/")),
    ("framework", "Gatsby", ("___gatsby",)),
    ("framework", "WordPress", ("/wp-content/", "/wp-includes/")),
    ("platform", "Shopify", ("cdn.shopify.com", "shopify.theme")),
    ("platform", "Webflow", ("webflow.js", "data-wf-domain")),
    ("platform", "Wix", ("wixstatic.com",)),
    ("platform", "Framer", ("framerusercontent.com",)),
    ("platform", "Squarespace", ("static1.squarespace.com",)),
)
HEADER_MARKERS: tuple[tuple[str, str], ...] = (
    ("x-powered-by", "runtime"), ("x-generator", "generator"), ("server", "server"),
)

DNS_VENDOR_MARKERS: dict[str, tuple[str, ...]] = {
    "Google Workspace": ("google.com", "googlemail.com", "googlehosted.com"),
    "Microsoft 365": ("outlook.com", "protection.outlook.com", "microsoft.com"),
    "Zoho Mail": ("zoho.com", "zohomail.com"),
    "Proton Mail": ("protonmail.ch", "protonmail.com", "proton.me"),
    "Fastmail": ("fastmail.com", "messagingengine.com"),
    "SendGrid": ("sendgrid.net",),
    "Mailgun": ("mailgun.org", "mailgun.com"),
    "Amazon SES": ("amazonses.com",),
    "Postmark": ("spf.mtasv.net", "postmarkapp.com"),
    "Brevo": ("sendinblue.com", "brevo.com"),
}


def normalize_domain(value: str | None) -> str | None:
    """Return an ASCII hostname, excluding URLs, paths, ports and wildcard labels."""
    if not value:
        return None
    value = value.strip().lower()
    if "://" in value:
        value = urlparse(value).hostname or ""
    value = value.strip(". ")
    if value.startswith("www."):
        value = value[4:]
    try:
        value = value.encode("idna").decode("ascii")
    except UnicodeError:
        return None
    return value if DOMAIN_RE.fullmatch(value) else None


def _date(value: str) -> str | None:
    try:
        return date.fromisoformat(value[:10]).isoformat()
    except (TypeError, ValueError):
        return None


def parse_certificates(payload: str, domain: str) -> tuple[list[dict], str | None]:
    """Parse crt.sh JSON into unique, in-scope names and their earliest seen dates."""
    try:
        rows = json.loads(payload)
    except (json.JSONDecodeError, TypeError):
        return [], None
    if not isinstance(rows, list):
        return [], None

    seen: dict[str, str | None] = {}
    all_dates: list[str] = []
    suffix = "." + domain
    for row in rows:
        if not isinstance(row, dict):
            continue
        cert_date = _date(row.get("not_before", ""))
        raw_names = "\n".join(str(row.get(key) or "") for key in ("name_value", "common_name"))
        row_in_scope = False
        for raw_name in raw_names.splitlines():
            name = raw_name.strip().lower().rstrip(".")
            wildcard = name.startswith("*.")
            hostname = name[2:] if wildcard else name
            if hostname != domain and not hostname.endswith(suffix):
                continue
            try:
                hostname = hostname.encode("idna").decode("ascii")
            except UnicodeError:
                continue
            name = f"*.{hostname}" if wildcard else hostname
            row_in_scope = True
            prev = seen.get(name)
            if name not in seen or (cert_date and (prev is None or cert_date < prev)):
                seen[name] = cert_date
        if row_in_scope and cert_date:
            all_dates.append(cert_date)
    subdomains = [{"fqdn": name, "first_seen": first_seen}
                  for name, first_seen in sorted(seen.items()) if name != domain][:MAX_SUBDOMAINS]
    return subdomains, min(all_dates) if all_dates else None


def _txt_answers(payload: dict) -> list[str]:
    out = []
    answers = payload.get("Answer", []) if isinstance(payload, dict) else []
    if not isinstance(answers, list):
        return out
    for answer in answers:
        if not isinstance(answer, dict):
            continue
        data = str(answer.get("data", "")).strip().strip('"')
        if data:
            out.append(data)
    return out


def _contains_dns_vendor(answer: str, marker: str) -> bool:
    """Match a DNS provider hostname as a label sequence, not inside a lookalike domain."""
    return re.search(rf"(?<![a-z0-9-]){re.escape(marker)}(?![a-z0-9-]|\.[a-z0-9-])", answer.lower()) is not None


class TechFingerprintCollector(Collector):
    name = "techfp"
    sources = ["company website HTML and selected response headers", "Google Public DNS", "crt.sh"]

    def collect(self, company: Company, ctx: Context) -> list[Fact]:
        domain = normalize_domain(company.domain)
        if not domain:
            url = "https://crt.sh/"
            return [self.unavailable(company, "techfp", url, "company domain is missing or invalid")]

        out: list[Fact] = []
        self._website(company, ctx, domain, out)
        self._dns(company, ctx, domain, out)
        self._certificates(company, ctx, domain, out)
        return out

    def _unavailable_response(self, company: Company, source: str, resp, reason: str) -> Fact:
        fact = self.unavailable(company, source, resp.url, reason)
        fact.source_doc_id = resp.doc_id
        return fact

    def _request(self, ctx: Context, company: Company, *, url: str, kind: str, title: str):
        try:
            return ctx.http.get(url, company_id=company.id, kind=kind, title=title)
        except Exception as exc:  # source errors must not abort other techfp lookups
            ctx.log.warning("techfp request failed for %s: %s", url, exc)
            return None

    def _website(self, company: Company, ctx: Context, domain: str, out: list[Fact]) -> None:
        url = f"https://{domain}/"
        resp = self._request(ctx, company, url=url, kind="techfp_site", title="Technology fingerprint website")
        if resp is None:
            out.append(self.unavailable(company, "techfp_website", url, "request failed"))
            return
        if not resp.ok:
            out.append(self._unavailable_response(company, "techfp_website", resp, f"HTTP {resp.status}"))
            return
        if "html" not in resp.content_type.lower():
            out.append(self._unavailable_response(company, "techfp_website", resp,
                                                  f"unexpected content type: {resp.content_type[:100]}"))
            return

        html = resp.text
        soup = BeautifulSoup(html, "html.parser")
        generator = soup.find("meta", attrs={"name": re.compile(r"^generator$", re.I)})
        if generator and generator.get("content"):
            value = str(generator["content"])[:200]
            self._stack_fact(company, out, resp.url, "generator", value, f"meta name=generator: {value}",
                             resp.doc_id)

        lowered = html.lower()
        for category, tech, markers in HTML_MARKERS:
            marker = next((m for m in markers if m in lowered), None)
            if marker is None and tech == "Next.js" and soup.find(id="__next"):
                marker = "id=__next"
            if marker:
                self._stack_fact(company, out, resp.url, category, tech, f"HTML marker: {marker}", resp.doc_id)

        for header, category in HEADER_MARKERS:
            value = resp.headers.get(header)
            if value:
                self._stack_fact(company, out, resp.url, category, value[:100], f"{header}: {value[:200]}",
                                 resp.doc_id)

        # Hosting providers are only emitted when a provider-specific response header exists.
        hosting_headers = (("x-vercel-id", "Vercel"), ("x-nf-request-id", "Netlify"),
                          ("cf-ray", "Cloudflare"), ("x-wix-request-id", "Wix"))
        for header, vendor in hosting_headers:
            if resp.headers.get(header):
                self._stack_fact(company, out, resp.url, "hosting", vendor,
                                 f"{header}: {resp.headers[header][:160]}", resp.doc_id)

    def _stack_fact(self, company: Company, out: list[Fact], url: str, category: str, tech: str, evidence: str,
                    source_doc_id: int | None = None) -> None:
        slug = re.sub(r"[^a-z0-9]+", "_", tech.lower()).strip("_")[:80] or "unknown"
        out.append(Fact(company_id=company.id, type="tech_stack", key=f"{category}:{slug}",
                        value={"category": category, "technology": tech, "evidence": evidence},
                        source_url=url, source_doc_id=source_doc_id, extractor=self.name, confidence="medium"))

    def _dns(self, company: Company, ctx: Context, domain: str, out: list[Fact]) -> None:
        for record_type in ("MX", "TXT"):
            url = f"https://dns.google/resolve?name={quote(domain)}&type={record_type}"
            source = f"dns_{record_type.lower()}"
            resp = self._request(ctx, company, url=url, kind=f"techfp_{source}", title=f"DNS {record_type} records")
            if resp is None:
                out.append(self.unavailable(company, source, url, "request failed"))
                continue
            if not resp.ok:
                out.append(self._unavailable_response(company, source, resp, f"HTTP {resp.status}"))
                continue
            try:
                payload = resp.json()
            except (json.JSONDecodeError, ValueError):
                out.append(self._unavailable_response(company, source, resp, "invalid DNS JSON"))
                continue
            if not isinstance(payload, dict):
                out.append(self._unavailable_response(company, source, resp, "unexpected DNS response"))
                continue
            rcode = payload.get("Status")
            if not isinstance(rcode, int) or isinstance(rcode, bool):
                out.append(self._unavailable_response(company, source, resp, "DNS response is missing a valid Status"))
                continue
            if rcode not in (0, 3):  # NOERROR and NXDOMAIN are valid DNS results.
                out.append(self._unavailable_response(company, source, resp, f"DNS response status {rcode}"))
                continue
            raw_answers = payload.get("Answer", [])
            if raw_answers is not None and not isinstance(raw_answers, list):
                out.append(self._unavailable_response(company, source, resp, "DNS Answer is not a list"))
                continue
            answers = _txt_answers(payload) if record_type == "TXT" else [
                str(a.get("data", "")).rstrip(".") for a in (raw_answers or []) if isinstance(a, dict)]
            for vendor, markers in DNS_VENDOR_MARKERS.items():
                evidence = next((answer for answer in answers
                                 if any(_contains_dns_vendor(answer, marker) for marker in markers)), None)
                if evidence:
                    out.append(Fact(company_id=company.id, type="saas_tool", key=vendor,
                                    value={"vendor": vendor, "record_type": record_type, "evidence": evidence[:240]},
                                    source_url=resp.url, source_doc_id=resp.doc_id, extractor=self.name,
                                    confidence="medium"))

    def _certificates(self, company: Company, ctx: Context, domain: str, out: list[Fact]) -> None:
        url = f"https://crt.sh/?q=%25.{quote(domain)}&output=json"
        resp = self._request(ctx, company, url=url, kind="techfp_certificates", title="Certificate transparency")
        if resp is None:
            out.append(self.unavailable(company, "crt_sh", url, "request failed"))
            return
        if not resp.ok:
            out.append(self._unavailable_response(company, "crt_sh", resp, f"HTTP {resp.status}"))
            return
        try:
            payload = json.loads(resp.text)
        except json.JSONDecodeError:
            out.append(self._unavailable_response(company, "crt_sh", resp, "invalid certificate JSON"))
            return
        if not isinstance(payload, list):
            out.append(self._unavailable_response(company, "crt_sh", resp, "unexpected certificate response"))
            return
        subdomains, first_date = parse_certificates(resp.text, domain)
        for item in subdomains:
            out.append(Fact(company_id=company.id, type="subdomain", key=item["fqdn"], value=item,
                            event_date=item["first_seen"], date_precision="day" if item["first_seen"] else None,
                            source_url=resp.url, source_doc_id=resp.doc_id, extractor=self.name, confidence="high"))
        if first_date:
            out.append(Fact(company_id=company.id, type="cert_first", key="domain", value={"domain": domain},
                            event_date=first_date, date_precision="day", source_url=resp.url,
                            source_doc_id=resp.doc_id,
                            extractor=self.name, confidence="high"))
