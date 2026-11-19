from types import SimpleNamespace

import pytest

from dd import cli
from dd.collectors.base import Context
from dd.config import Settings
from dd.store import Company, Fact, Store


def test_collect_rejects_unknown_name_before_running(tmp_path):
    store = Store(tmp_path / "store.sqlite")
    store.upsert_company(Company(id="x", name="X"))
    ctx = Context(Settings(home=tmp_path), store, None)
    with pytest.raises(SystemExit, match="unknown collectors"):
        cli.cmd_collect(SimpleNamespace(id="x", only="typo"), ctx)


def test_collect_preserves_snapshot_on_crash_and_runs_remaining(tmp_path, monkeypatch):
    store = Store(tmp_path / "store.sqlite")
    store.upsert_company(Company(id="x", name="X"))
    old = Fact(company_id="x", type="identity", value="old", source_url="https://example.com", extractor="registry")
    store.add_facts([old])

    class Broken:
        name = "registry"
        def collect(self, *args):
            raise ValueError("broken source")

    class Good:
        name = "code"
        def collect(self, *args):
            return [Fact(company_id="x", type="github_org", value="ok", source_url="https://github.com/x", extractor="code")]

    monkeypatch.setattr(cli, "load", lambda names: {"registry": Broken(), "code": Good()})
    ctx = Context(Settings(home=tmp_path), store, None)
    with pytest.raises(SystemExit):
        cli.cmd_collect(SimpleNamespace(id="x", only="registry,code"), ctx)
    assert store.facts("x", ["identity"])[0].value == "old"
    assert store.facts("x", ["github_org"])[0].value == "ok"
