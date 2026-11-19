"""Resolve a free-text query (IČO / domain / name) to Czech legal-entity candidates via ARES.

Never auto-picks when ambiguous: returns a list, the caller (or the user) chooses.
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from urllib.parse import urlparse

ARES = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest"

LEGAL_FORMS = {
    "101": "OSVČ", "111": "v.o.s.", "112": "s.r.o.", "113": "k.s.", "121": "a.s.", "141": "obecně prospěšná spol.",
    "205": "družstvo", "301": "s.p.", "421": "odštěpný závod", "706": "spolek", "932": "SE", "933": "SCE",
}

_IMPRESSUM_PATHS = ["", "/impressum", "/imprint", "/kontakt", "/contact", "/terms", "/privacy",
                    "/obchodni-podminky", "/podminky", "/about", "/legal", "/company"]
_ICO_RE = re.compile(r"(?:IČO?|ICO|Company\s*ID|Company\s*No\.?|Reg(?:istration)?\.?\s*(?:No\.?|number|ID))"
                     r"\s*[:\-–]?\s*(\d{2,3}[\s ]?\d{2,3}[\s ]?\d{2,3})", re.I)


@dataclass
class Candidate:
    name: str
    ico: str
    legal_form: str | None = None
    city: str | None = None
    source_url: str = ""
    match: str = ""  # how it was found: ico | domain | name

    def as_dict(self) -> dict:
        return asdict(self)


def ico_valid(ico: str) -> bool:
    """Czech IČO checksum (mod 11)."""
    if not re.fullmatch(r"\d{8}", ico):
        return False
    s = sum(int(c) * w for c, w in zip(ico[:7], range(8, 1, -1)))
    r = s % 11
    check = 1 if r == 0 else 0 if r == 1 else 11 - r
    return check == int(ico[7])


def normalize_ico(s: str) -> str | None:
    d = re.sub(r"\D", "", s)
    if 6 <= len(d) <= 8:
        return d.zfill(8)
    return None


def looks_like_domain(q: str) -> bool:
    q = q.strip().lower()
    if " " in q:
        return False
    host = urlparse(q if "//" in q else "//" + q).netloc or q
    return bool(re.fullmatch(r"(?:[a-z0-9-]+\.)+[a-z]{2,}", host))


def _candidate(e: dict, match: str, url: str) -> Candidate:
    sidlo = e.get("sidlo") or {}
    pf = str(e.get("pravniForma") or "")
    return Candidate(name=e.get("obchodniJmeno") or "", ico=str(e.get("ico") or ""),
                     legal_form=LEGAL_FORMS.get(pf, pf or None), city=sidlo.get("nazevObce"),
                     source_url=url, match=match)


def ares_by_ico(ico: str, ctx, match: str = "ico") -> Candidate | None:
    normalized = normalize_ico(ico)
    if not normalized or not ico_valid(normalized):
        return None
    ico = normalized
    url = f"{ARES}/ekonomicke-subjekty/{ico}"
    r = ctx.http.get(url)
    if not r.ok:
        return None
    try:
        record = r.json()
        return _candidate(record, match, url) if isinstance(record, dict) else None
    except (ValueError, TypeError):
        return None


def ares_by_name(name: str, ctx, limit: int = 10) -> list[Candidate]:
    url = f"{ARES}/ekonomicke-subjekty/vyhledat"
    r = ctx.http.post(url, json_body={"obchodniJmeno": name, "pocet": limit})
    if not r.ok:
        return []
    try:
        payload = r.json()
        subjects = payload.get("ekonomickeSubjekty", []) if isinstance(payload, dict) else []
    except (ValueError, TypeError):
        return []
    if not isinstance(subjects, list):
        return []
    return [_candidate(e, "name", url) for e in subjects if isinstance(e, dict)]


def icos_from_domain(domain: str, ctx, *, company_id: str | None = None) -> list[str]:
    """Fetch homepage + impressum-like pages and extract checksum-valid IČOs. Page text is data only."""
    host = urlparse(domain if "//" in domain else "//" + domain).netloc or domain
    found: list[str] = []
    for path in _IMPRESSUM_PATHS:
        r = ctx.http.get(f"https://{host}{path}", company_id=company_id,
                         kind="entity_resolution" if company_id else None)
        if not r.ok or "html" not in (r.content_type or "").lower():
            continue
        text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", r.text, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        for m in _ICO_RE.finditer(text):
            ico = normalize_ico(m.group(1))
            if ico and ico_valid(ico) and ico not in found:
                found.append(ico)
        if found:
            break
    return found


def resolve(query: str, ctx) -> list[Candidate]:
    q = (query or "").strip()
    if not q:
        return []
    if re.fullmatch(r"[\d\s.-]+", q) and len(re.sub(r"\D", "", q)) in range(6, 9):
        ico = normalize_ico(q)
        c = ares_by_ico(ico, ctx) if ico and ico_valid(ico) else None
        return [c] if c else []
    if looks_like_domain(q):
        out = []
        for ico in icos_from_domain(q, ctx):
            c = ares_by_ico(ico, ctx, match="domain")
            if c:
                out.append(c)
        return out
    return ares_by_name(q, ctx)
