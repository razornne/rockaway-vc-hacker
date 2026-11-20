"""Settings from environment / .env."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


DEFAULT_PRICES = "gpt-5-nano=0.05,0.40;gpt-5-mini=0.25,2.00"


def _prices() -> dict[str, tuple[float, float]]:
    """LLM_PRICES='model=in,out;model2=in,out' (USD per 1M tokens)."""
    out = {}
    for part in os.getenv("LLM_PRICES", DEFAULT_PRICES).split(";"):
        if "=" not in part:
            continue
        model, nums = part.split("=", 1)
        try:
            i, o = (float(x) for x in nums.split(","))
            out[model.strip()] = (i, o)
        except ValueError:
            pass
    return out


@dataclass
class Settings:
    openai_api_key: str = field(default_factory=lambda: os.getenv("OPENAI_API_KEY", ""))
    # Claude models (claude-*) run through the Anthropic API, for model comparisons. Its own hard limit, because it is
    # a separate account with its own balance; spend still counts towards LLM_BUDGET_USD as well.
    anthropic_api_key: str = field(default_factory=lambda: os.getenv("ANTHROPIC_API_KEY", ""))
    anthropic_budget_usd: float = field(default_factory=lambda: float(os.getenv("ANTHROPIC_BUDGET_USD", "0.40")))
    model_extract: str = field(default_factory=lambda: os.getenv("LLM_MODEL_EXTRACT", "gpt-5-nano"))
    model_analyze: str = field(default_factory=lambda: os.getenv("LLM_MODEL_ANALYZE", "gpt-5-mini"))
    budget_usd: float = field(default_factory=lambda: float(os.getenv("LLM_BUDGET_USD", "2.50")))
    prices: dict[str, tuple[float, float]] = field(default_factory=_prices)
    github_token: str = field(default_factory=lambda: os.getenv("GITHUB_TOKEN", ""))
    hlidac_token: str = field(default_factory=lambda: os.getenv("HLIDAC_TOKEN", ""))
    tavily_api_key: str = field(default_factory=lambda: os.getenv("TAVILY_API_KEY", ""))
    brave_api_key: str = field(default_factory=lambda: os.getenv("BRAVE_API_KEY", ""))
    exa_api_key: str = field(default_factory=lambda: os.getenv("EXA_API_KEY", ""))
    home: Path = field(default_factory=lambda: ROOT / os.getenv("DD_HOME", ".dd"))

    @property
    def db_path(self) -> Path:
        return self.home / "dd.sqlite"

    @property
    def cache_dir(self) -> Path:
        return self.home / "cache"

    def ensure_dirs(self) -> None:
        self.cache_dir.mkdir(parents=True, exist_ok=True)


def get_settings() -> Settings:
    s = Settings()
    s.ensure_dirs()
    return s
