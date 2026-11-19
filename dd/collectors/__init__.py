"""Collector registry. Modules are imported lazily so a missing / broken collector doesn't break the CLI."""
from __future__ import annotations

import importlib
import logging

# module name -> class name. Each parallel workstream owns its own module(s).
KNOWN = {
    "registry": "RegistryCollector",        # stream A
    "web": "WebCollector",                  # stream B
    "techfp": "TechFingerprintCollector",   # stream B
    "code": "CodeCollector",                # stream C
    "ml": "MLCollector",                    # stream C
    "apps": "AppsCollector",                # stream C
    "history": "HistoryCollector",          # stream C
    "public_money": "PublicMoneyCollector", # stream D
    "press": "PressCollector",              # stream D
    "procurement": "ProcurementCollector",  # defence/dual-use: TED
    "eu_funding": "EUFundingCollector",     # defence/dual-use: EU F&T portal (EDF)
    "diana": "DianaCollector",              # defence/dual-use: NATO DIANA cohorts
}


def load(names: list[str] | None = None) -> dict:
    out = {}
    for mod, cls in KNOWN.items():
        if names and mod not in names:
            continue
        try:
            m = importlib.import_module(f"dd.collectors.{mod}")
            out[mod] = getattr(m, cls)()
        except (ImportError, AttributeError) as e:
            logging.getLogger("dd").debug("collector %s not available: %s", mod, e)
    return out
