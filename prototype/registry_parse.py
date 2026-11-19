"""Parser for the open-data dumps of the Czech business register (dataor.justice.cz, *-full-*.xml.gz).

Extracts for every company:
  - legal-entity shareholders (společníci / akcionáři) with entry and exit dates;
  - the history of registered capital.
Natural persons are not stored (minimal personal data).

Run:
    python prototype/registry_parse.py <dump.xml.gz> <out.jsonl>
"""
import gzip
import json
import sys
import xml.etree.ElementTree as ET

SHAREHOLDER_TOP = ("SPOLECNIK", "AKCIONAR")  # codes of the top-level shareholder sections


def text(el, path):
    x = el.find(path)
    return x.text.strip() if x is not None and x.text else None


def walk_shareholders(udaj, top_kod, out):
    """Recursively finds legal-entity records (osoba/nazev) in a shareholder section."""
    for sub in udaj.iter("Udaj"):
        osoba = sub.find("osoba")
        if osoba is None:
            continue
        name = text(osoba, "nazev")
        if not name:
            continue  # natural person: skipped
        out.append({
            "name": name,
            "ico": text(osoba, "ico"),
            "country": text(osoba, "stat/kod") or text(sub, "adresa/statNazev"),
            "from": text(sub, "zapisDatum"),
            "to": text(sub, "vymazDatum"),
            "section": top_kod,
            "kod": text(sub, "udajTyp/kod"),
        })


def parse(path_in, path_out):
    n = kept = 0
    with gzip.open(path_in, "rb") as f, open(path_out, "w", encoding="utf-8") as out:
        for _, el in ET.iterparse(f, events=("end",)):
            if el.tag != "Subjekt":
                continue
            n += 1
            rec = {"name": text(el, "nazev"), "ico": text(el, "ico"), "registered": text(el, "zapisDatum"),
                   "holders": [], "capital": [], "top_kods": set()}
            udaje = el.find("udaje")
            for u in (udaje if udaje is not None else []):
                kod = text(u, "udajTyp/kod") or ""
                rec["top_kods"].add(kod)
                if kod.startswith(SHAREHOLDER_TOP):
                    walk_shareholders(u, kod, rec["holders"])
                elif kod == "ZAKLADNI_KAPITAL":
                    rec["capital"].append({"value": text(u, "hodnotaText") or text(u, "vklad/textValue"),
                                           "from": text(u, "zapisDatum"), "to": text(u, "vymazDatum")})
            rec["top_kods"] = sorted(rec["top_kods"])
            if rec["holders"] or rec["ico"] in WATCH:
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                kept += 1
            el.clear()
    print(f"subjects: {n}, with legal-entity holders: {kept}")


WATCH = set()

if __name__ == "__main__":
    parse(sys.argv[1], sys.argv[2])
