"""dd — command line.

  dd seed                       load eval/companies.json into the store
  dd add ID --name N [--domain D] [--ico I]
  dd collectors                 list available collectors
  dd collect ID [--only a,b] [--no-cache]
  dd facts ID [--type T]
  dd models                     list OpenAI models available to the key
  dd spent                      LLM spend so far
  dd osint [IDS ...] [--all] [--offline]   OSINT checks after analysis (docs/OSINT_PLAN.md)
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from pathlib import Path

from dd.collectors import KNOWN, load
from dd.collectors.base import Context
from dd.config import ROOT, get_settings
from dd.http import Http
from dd.store import Company, Store


def ctx_from_settings(no_cache: bool = False) -> Context:
    s = get_settings()
    store = Store(s.db_path)
    http = Http(s.cache_dir, store=store)
    if no_cache:
        orig = http.request
        http.request = lambda *a, **kw: orig(*a, **{**kw, "use_cache": False})  # type: ignore[method-assign]
    return Context(settings=s, store=store, http=http)


def cmd_seed(args, ctx):
    data = json.loads((ROOT / "eval" / "companies.json").read_text(encoding="utf-8"))
    for c in data:
        ctx.store.upsert_company(Company(id=c["id"], name=c["name"], domain=c.get("domain"), ico=c.get("ico"),
                                         country=c.get("country"), hints={**c.get("hints", {}), "tier": c.get("tier")}))
    print(f"seeded {len(data)} companies")


def cmd_add(args, ctx):
    ctx.store.upsert_company(Company(id=args.id, name=args.name, domain=args.domain, ico=args.ico))
    print("ok")


def cmd_collectors(args, ctx):
    avail = load()
    for mod in KNOWN:
        c = avail.get(mod)
        print(f"{'✓' if c else '·'} {mod:14s} {', '.join(getattr(c, 'sources', [])) if c else '(not implemented yet)'}")


def cmd_resolve(args, ctx):
    from dd.resolver import resolve
    candidates = resolve(args.query, ctx)
    if not candidates:
        print("no candidates")
        return
    for i, candidate in enumerate(candidates, 1):
        legal_form = f" · {candidate.legal_form}" if candidate.legal_form else ""
        city = f" · {candidate.city}" if candidate.city else ""
        print(f"{i}. {candidate.name} · IČO {candidate.ico}{legal_form}{city} · match={candidate.match}")
        if candidate.source_url:
            print(f"   {candidate.source_url}")


def cmd_collect(args, ctx):
    comp = ctx.store.get_company(args.id)
    if not comp:
        sys.exit(f"unknown company {args.id}; run `dd seed` or `dd add`")
    names = [n.strip() for n in args.only.split(",")] if args.only else None
    unknown = set(names or []) - set(KNOWN)
    if unknown:
        sys.exit(f"unknown collectors: {', '.join(sorted(unknown))}")
    available = load(names)
    missing = set(names or KNOWN) - set(available)
    if missing:
        sys.exit(f"collectors could not be loaded: {', '.join(sorted(missing))}; run with -v for details")
    failed = False
    for name, col in available.items():
        t = time.monotonic()
        try:
            facts = col.collect(comp, ctx)
        except Exception as e:  # collectors should not raise; this is a safety net
            logging.getLogger("dd").exception("collector %s failed", name)
            print(f"{name:14s} failed; previous facts preserved", file=sys.stderr)
            failed = True
            continue
        try:
            n = ctx.store.replace_facts(comp.id, col.name, facts)
        except Exception:
            logging.getLogger("dd").exception("cannot store collector %s output", name)
            failed = True
            continue
        print(f"{name:14s} {n:4d} facts  {time.monotonic() - t:5.1f}s")
    if failed:
        sys.exit(1)


def cmd_facts(args, ctx):
    for f in ctx.store.facts(args.id, [args.type] if args.type else None):
        v = json.dumps(f.value, ensure_ascii=False)[:110]
        print(f"[{f.id}] {f.type:22s} {f.key or '':28.28s} {f.event_date or '':10s} {v}  <{f.source_url[:70]}>")


def cmd_extract(args, ctx):
    from dd.extract import extract_company
    from dd.llm import LLM, BudgetExceeded
    comp = ctx.store.get_company(args.id)
    if not comp:
        sys.exit(f"unknown company {args.id}")
    try:
        st = extract_company(ctx.store, LLM(ctx.settings, ctx.store), comp, model=args.model,
                             max_docs=args.max_docs)
    except BudgetExceeded as e:
        sys.exit(f"stopped: {e}")
    print(f"docs {st.docs} (cached {st.cached}) | accepted {st.accepted} | rejected (quote not in source) {st.rejected}"
          f" | skipped docs {st.skipped_docs} | cost ${st.cost:.4f} | budget ledger ${ctx.store.llm_spent():.4f}")
    for ex in st.rejected_examples:
        print("  rejected:", ex)


def cmd_models(args, ctx):
    from openai import OpenAI
    if not ctx.settings.openai_api_key:
        sys.exit("OPENAI_API_KEY is not set (.env)")
    ids = sorted(m.id for m in OpenAI(api_key=ctx.settings.openai_api_key).models.list())
    for i in ids:
        if i.startswith(("gpt", "o")):
            print(i, "(configured)" if i in (ctx.settings.model_extract, ctx.settings.model_analyze) else "")


def cmd_spent(args, ctx):
    pending = ctx.store.db.execute('SELECT COUNT(*) FROM llm_call WHERE response IS NULL').fetchone()[0]
    print(f"LLM usage + unresolved reservations: ${ctx.store.llm_spent():.4f} of ${ctx.settings.budget_usd:.2f}"
          f" | {pending} uncached/failed calls")


def cmd_eval(args, ctx):
    from dd.evaluate import evaluate
    report = evaluate(ctx.store)
    out = ROOT / "eval" / "report.md"
    out.write_text(report, encoding="utf-8")
    print(report.split("## 3.")[0])
    print(f"full report: {out}")


def cmd_verify(args, ctx):
    from dd.verify import verify_company
    company = ctx.store.get_company(args.id)
    if not company:
        sys.exit(f"unknown company {args.id}")
    facts = verify_company(company, ctx)
    for f in facts:
        v = f.value if isinstance(f.value, dict) else {}
        if f.type == "verification":
            print(f"{v.get('check', ''):22s} {v.get('status', ''):13s} {str(v.get('detail', ''))[:150]}")
        elif f.type == "source_unavailable":
            print(f"{'unavailable':22s} {f.key}: {v.get('reason', '')[:120]}")
    print(f"patents: {sum(f.type == 'patent' for f in facts)} | checks: {sum(f.type == 'verification' for f in facts)}")


def cmd_analyze(args, ctx):
    from dd.analyze import analyze_company
    from dd.llm import LLM
    company = ctx.store.get_company(args.id)
    if not company:
        sys.exit(f"unknown company {args.id}")
    # --compare stores the run apart (kind "dossier@<model>") so the published brief is not replaced
    kind = f"dossier@{args.model}" if args.compare and args.model else "dossier"
    result = analyze_company(ctx.store, LLM(ctx.settings, ctx.store), company, model=args.model, kind=kind)
    print(f"{company.id}: {len(result['sections'])} sections | cost ${result['cost_usd']:.4f}"
          f" | cached={result['cached']}")


def cmd_dossier(args, ctx):
    from dd.writer import write_dossier
    company = ctx.store.get_company(args.id)
    if not company:
        sys.exit(f"unknown company {args.id}")
    kind, suffix = (f"dossier@{args.model}", f"-{args.model}") if args.model else ("dossier", "")
    paths = write_dossier(ctx.store, company, Path(args.output) if args.output else ctx.settings.home / 'dossiers',
                          kind=kind, suffix=suffix)
    for kind, path in paths.items():
        print(f"{kind}: {path}")


def cmd_site(args, ctx):
    from dd.site import build_site
    from dd.config import ROOT
    paths = build_site(ctx.store, Path(args.output) if args.output else ROOT / "site")
    print(f"{len(paths)} files written to {paths[-1].parent}")


def cmd_compare(args, ctx):
    from dd.compare import write_compare
    path = write_compare(ctx.store, args.id, [m.strip() for m in args.models.split(",")], Path(args.output))
    print(f"comparison: {path}")


def cmd_label_sheet(args, ctx):
    from dd.labels import write_sheet
    out = Path(args.output)
    n = write_sheet(ctx.store, [c.strip() for c in args.ids.split(",")], out)
    print(f"{n} statements written to {out}")


def cmd_osint(args, ctx):
    from dd.osint.run import run
    if args.download_dumps:
        from dd.osint.people import download_dumps
        print(f"{len(download_dumps())} register dump(s) downloaded to data/dataor/")
    ids = [c["id"] for c in json.loads((ROOT / "eval" / "companies.json").read_text(encoding="utf-8"))]         if args.all else args.ids
    for cid, counts in run(ctx.store, ctx, ids, network=not args.offline).items():
        print(cid, " ".join(f"{k}={v}" for k, v in counts.items()))


def cmd_label_score(args, ctx):
    from dd.labels import score
    print(score(Path(args.path)))


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")  # Windows console (cp1251)
    p = argparse.ArgumentParser(prog="dd")
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("seed")
    a = sub.add_parser("add"); a.add_argument("id"); a.add_argument("--name", required=True)
    a.add_argument("--domain"); a.add_argument("--ico")
    sub.add_parser("collectors")
    r = sub.add_parser("resolve"); r.add_argument("query")
    c = sub.add_parser("collect"); c.add_argument("id"); c.add_argument("--only"); c.add_argument("--no-cache", action="store_true")
    f = sub.add_parser("facts"); f.add_argument("id"); f.add_argument("--type")
    e = sub.add_parser("extract"); e.add_argument("id"); e.add_argument("--model")
    e.add_argument('--max-docs', type=int)
    a = sub.add_parser('analyze'); a.add_argument('id'); a.add_argument('--model')
    a.add_argument('--compare', action='store_true', help='store the run apart from the published brief')
    v = sub.add_parser('verify'); v.add_argument('id')
    sub.add_parser('eval')
    d = sub.add_parser('dossier'); d.add_argument('id'); d.add_argument('--output')
    d.add_argument('--model', help='render the comparison run of this model (see analyze --compare)')
    st = sub.add_parser("site"); st.add_argument("--output")
    ls = sub.add_parser("label-sheet"); ls.add_argument("ids", help="comma-separated company ids")
    ls.add_argument("--output", required=True)
    lsc = sub.add_parser("label-score"); lsc.add_argument("path")
    cp = sub.add_parser("compare"); cp.add_argument("id"); cp.add_argument("--models", required=True)
    cp.add_argument("--output", required=True)
    sub.add_parser("models")
    sub.add_parser("spent")
    o = sub.add_parser("osint"); o.add_argument("ids", nargs="*"); o.add_argument("--all", action="store_true")
    o.add_argument("--offline", action="store_true", help="claims against records only, no network")
    o.add_argument("--download-dumps", action="store_true", help="fetch the register open-data dumps first (~806 MB)")
    args = p.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.WARNING, format="%(levelname)s %(name)s: %(message)s")
    ctx = ctx_from_settings(getattr(args, "no_cache", False))
    {"seed": cmd_seed, "add": cmd_add, "collectors": cmd_collectors, "resolve": cmd_resolve,
     "collect": cmd_collect, "facts": cmd_facts,
     "extract": cmd_extract, "analyze": cmd_analyze, "verify": cmd_verify, "eval": cmd_eval, "dossier": cmd_dossier,
     "models": cmd_models, "spent": cmd_spent, "site": cmd_site,
     "label-sheet": cmd_label_sheet, "label-score": cmd_label_score, "compare": cmd_compare,
     "osint": cmd_osint}[args.cmd](args, ctx)


if __name__ == "__main__":
    main()
