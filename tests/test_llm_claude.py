"""Claude models go through the Anthropic API with the same cache, cost ledger and hard budgets."""
from types import SimpleNamespace

import pytest
from pydantic import BaseModel

from dd.config import Settings
from dd.llm import LLM, BudgetExceeded
from dd.store import Store


class Out(BaseModel):
    answer: str


class FakeMessages:
    def __init__(self, text='{"answer": "ok"}', stop="end_turn"):
        self.calls, self.text, self.stop = [], text, stop

    def create(self, **kw):
        self.calls.append(kw)
        return SimpleNamespace(usage=SimpleNamespace(input_tokens=20_000, output_tokens=3_000), stop_reason=self.stop,
                               content=[SimpleNamespace(type="thinking", thinking=""), SimpleNamespace(type="text", text=self.text)])


def make(tmp_path, budget=0.40, **fake):
    s = Settings(openai_api_key="", anthropic_api_key="fake", budget_usd=2.5, anthropic_budget_usd=budget,
                 prices={"claude-sonnet-5-5": (2.0, 10.0)}, home=tmp_path)
    store = Store(tmp_path / "db.sqlite")
    llm = LLM(s, store)
    llm._anthropic = SimpleNamespace(messages=FakeMessages(**fake))
    return store, llm


def test_claude_call_is_structured_costed_and_cached(tmp_path):
    store, llm = make(tmp_path)
    r = llm.call(purpose="t", model="claude-sonnet-5-5", prompt="p", schema=Out, max_output_tokens=4000)
    assert r.parsed.answer == "ok" and r.cost_usd == pytest.approx(0.07)
    kw = llm._anthropic.messages.calls[0]
    assert kw["output_config"]["format"]["type"] == "json_schema" and kw["output_config"]["effort"] == llm.effort
    again = llm.call(purpose="t", model="claude-sonnet-5-5", prompt="p", schema=Out, max_output_tokens=4000)
    assert again.cached and len(llm._anthropic.messages.calls) == 1


def test_anthropic_budget_is_enforced_separately(tmp_path):
    store, llm = make(tmp_path, budget=0.01)
    with pytest.raises(BudgetExceeded, match="Anthropic budget"):
        llm.call(purpose="t", model="claude-sonnet-5-5", prompt="p", schema=Out, max_output_tokens=4000)
    assert llm._anthropic.messages.calls == []


def test_truncated_claude_answer_records_usage_and_fails(tmp_path):
    store, llm = make(tmp_path, stop="max_tokens")
    with pytest.raises(RuntimeError, match="max_tokens"):
        llm.call(purpose="t", model="claude-sonnet-5-5", prompt="p", schema=Out, max_output_tokens=4000)
    assert store.llm_spent() == pytest.approx(0.07)
