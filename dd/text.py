"""HTML → clean text, and saving text next to the raw cached document."""
from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup


def html_to_text(html: str) -> tuple[str | None, str]:
    """Return (title, visible text). Scripts, styles, nav/footer noise removed; paragraphs kept on lines."""
    soup = BeautifulSoup(html, "lxml")
    title = soup.title.get_text(strip=True) if soup.title else None
    for t in soup(["script", "style", "noscript", "svg", "iframe", "template"]):
        t.decompose()
    text = soup.get_text("\n")
    text = re.sub(r"[ \t\xa0]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text).strip()
    return title, text


def save_text(store, resp, text: str, title: str | None = None) -> str:
    """Write extracted text as <raw>.txt and link it to the SourceDoc (resp.doc_id must be set)."""
    p = Path(resp.raw_path).with_suffix(".txt")
    p.write_text(text, encoding="utf-8")
    if store is not None and resp.doc_id:
        store.set_doc_text(resp.doc_id, str(p), title)
    return str(p)


def normalize(s: str) -> str:
    """For snippet verification: lowercase, collapse whitespace."""
    return re.sub(r"\s+", " ", s or "").strip().lower()


def snippet_in(snippet: str, text: str) -> bool:
    return bool(snippet) and normalize(snippet) in normalize(text)
