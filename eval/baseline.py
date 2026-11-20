"""Baseline: what a capable model with web search writes about the same company, with no collectors, no quote checks
and no code-computed numbers. Its output is compared with the tool's brief on the facts that official records settle
(filed accounts, the funding round, public money, defence procurement, patents) in eval/baseline/README.md.

    uv run python eval/baseline.py fly4future dronetag

Uses the OpenAI Responses API with the web_search tool. The cost (tokens plus searches) is written to the same
ledger as every other model call and is refused when it would break LLM_BUDGET_USD.
"""
from __future__ import annotations

import sys
import time
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dd.config import ROOT, get_settings  # noqa: E402
from dd.store import Store, now  # noqa: E402

MODEL = "gpt-5-mini"
SEARCH_USD = 0.01  # per web search call (OpenAI price list); checked before running
TASK = (
    "You are preparing a first-look due diligence brief for a partner at a Seed to Series A venture fund (Rockaway "
    "Ventures, Prague). Company: {name} ({domain}), Czech company ID {ico}. Use web search. Write about 600 words with "
    "these sections: In short; Funding and ownership; Revenue, profit and cash; Public money (grants, public contracts); "
    "Defence relevance; Technology and what could be rebuilt; Risks; Questions for the founders. Give the source URL "
    "for every factual statement. Say clearly when something could not be found."
)


def run(cid: str) -> None:
    s = get_settings()
    store = Store(s.db_path)
    c = store.get_company(cid)
    spent = store.llm_spent()
    worst = 40_000 / 1e6 * 0.25 + 16_000 / 1e6 * 2.0 + 20 * SEARCH_USD
    if spent + worst > s.budget_usd:
        sys.exit(f"budget: spent ${spent:.3f}, a baseline run may cost up to ${worst:.3f}")
    from openai import OpenAI
    client = OpenAI(api_key=s.openai_api_key, timeout=300)
    t0 = time.monotonic()
    resp = client.responses.create(model=MODEL, tools=[{"type": "web_search"}], reasoning={"effort": "low"},
                                   input=TASK.format(name=c.name, domain=c.domain, ico=c.ico or "unknown"),
                                   max_output_tokens=16_000)
    secs = time.monotonic() - t0
    searches = sum(1 for o in resp.output if getattr(o, "type", "") == "web_search_call")
    u = resp.usage
    cost = u.input_tokens / 1e6 * 0.25 + u.output_tokens / 1e6 * 2.0 + searches * SEARCH_USD
    store.db.execute("INSERT INTO llm_call(cache_key,model,purpose,cost_usd,response,created_at,input_tokens,output_tokens) "
                     "VALUES(?,?,?,?,?,?,?,?)", (f"baseline:{uuid.uuid4().hex}", MODEL, f"baseline:{cid}", cost,
                                                 resp.output_text, now(), u.input_tokens, u.output_tokens))
    store.db.commit()
    out = ROOT / "eval" / "baseline" / f"{cid}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(f"# Baseline brief: {c.name}\n\n{MODEL} with web search, one call, {searches} searches, "
                   f"{secs:.0f} s, ${cost:.3f}, {now()[:10]}.\n\n---\n\n{resp.output_text}\n", encoding="utf-8")
    print(f"{cid}: {searches} searches, {secs:.0f}s, ${cost:.4f} -> {out}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for cid in sys.argv[1:]:
        run(cid)
