from types import SimpleNamespace

import pytest

from dd.config import Settings
from dd.extract import Extraction
from dd.llm import LLM, BudgetExceeded
from dd.store import Store


def make(tmp_path, response):
    settings = Settings(openai_api_key='test', home=tmp_path)
    class Responses:
        calls = 0
        def create(self, **kw):
            self.calls += 1
            if isinstance(response, Exception):
                raise response
            return response
    responses = Responses()
    store = Store(tmp_path / 'db.sqlite')
    return LLM(settings, store, client=SimpleNamespace(responses=responses)), store, responses


@pytest.mark.parametrize('status,text', [('incomplete',''), ('completed','invalid json')])
def test_bad_output_still_records_usage(tmp_path, status, text):
    llm, store, _ = make(tmp_path, SimpleNamespace(status=status, output_text=text,
        usage=SimpleNamespace(input_tokens=1000, output_tokens=200)))
    with pytest.raises((ValueError, RuntimeError)):
        llm.call(purpose='test',model='gpt-5-nano',prompt='input',schema=Extraction)
    assert store.llm_spent() == pytest.approx(.00013)
    assert store.db.execute('SELECT response FROM llm_call').fetchone()[0] is None


def test_timeout_keeps_reservation(tmp_path):
    llm, store, responses = make(tmp_path, TimeoutError('lost response'))
    with pytest.raises(TimeoutError):
        llm.call(purpose='test',model='gpt-5-nano',prompt='input',schema=Extraction)
    assert store.llm_spent() > 0
    assert responses.calls == 1


def test_strict_json_success_is_cached(tmp_path):
    llm, store, responses = make(tmp_path, SimpleNamespace(status='completed', output_text='{"items":[]}',
        usage=SimpleNamespace(input_tokens=100, output_tokens=10)))
    kwargs = dict(purpose='test',model='gpt-5-nano',prompt='input',schema=Extraction)
    llm.call(**kwargs)
    spent = store.llm_spent()
    assert llm.call(**kwargs).cached
    assert store.llm_spent() == spent and responses.calls == 1


def test_price_prefix_does_not_accept_other_models(tmp_path):
    llm, _, _ = make(tmp_path, None)
    with pytest.raises(BudgetExceeded):
        llm.price('gpt-5-mini-expensive')
    assert llm.price('gpt-5-mini-2025-08-07') == (.25, 2.)
