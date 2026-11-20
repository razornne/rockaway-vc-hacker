"""The semantic-accuracy sheet: a person labels statements, the score counts the answers."""
import csv

from dd.labels import FIXED, HUMAN, score


def test_score_counts_answers_and_lists_material_problems(tmp_path):
    p = tmp_path / "labels.csv"
    rows = [
        {"row": 1, "company": "x", "section": "TL;DR", "statement": "Raised €1m", "supported": "yes", "numbers": "yes",
         "entities": "yes", "follows": "n/a", "from_absence": "no", "severity": "n/a"},
        {"row": 2, "company": "x", "section": "Case for and against", "statement": "Round too large",
         "supported": "partly", "numbers": "no", "entities": "yes", "follows": "no", "from_absence": "no",
         "severity": "material", "comment": "CZK 15M is within the ticket"},
        {"row": 3, "company": "x", "section": "Risks and caveats", "statement": "not labelled yet"},
    ]
    with p.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=FIXED + HUMAN)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIXED + HUMAN})
    out = score(p)
    assert "Labelled rows: 2 of 3" in out
    assert "50% yes of 2 answered" in out          # supported: yes 1, partly 1
    assert "Numbers" not in out or "50% yes" in out
    assert "row 2 (x, Case for and against)" in out and "within the ticket" in out
