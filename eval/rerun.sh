#!/usr/bin/env bash
# Partial re-run after a fix: RECOLLECT="a b" re-collects/extracts those companies; ONLY=<collector> re-runs one collector; EXTRACT=1 re-extracts
# for everyone; then everyone gets verify/analyze/dossier, eval and the spend line.
cd "$(dirname "$0")/.." || exit 1
LOG=.dd/rerun.log
: > "$LOG"
uv run dd seed >> "$LOG" 2>&1
for c in $RECOLLECT; do
  echo "=== collect $c $(date +%H:%M:%S)" >> "$LOG"
  uv run dd collect "$c" >> "$LOG" 2>&1
  uv run dd extract "$c" >> "$LOG" 2>&1
done
for c in $(uv run python -c "import json;print(' '.join(c['id'] for c in json.load(open('eval/companies.json',encoding='utf-8'))))"); do
  echo "=== $c $(date +%H:%M:%S)" >> "$LOG"
  [ -n "$ONLY" ] && uv run dd collect "$c" --only "$ONLY" >> "$LOG" 2>&1
  [ -n "$EXTRACT" ] && uv run dd extract "$c" >> "$LOG" 2>&1
  uv run dd verify "$c" >> "$LOG" 2>&1
  uv run dd analyze "$c" >> "$LOG" 2>&1
  uv run dd dossier "$c" --output .dd/briefs >> "$LOG" 2>&1
done
uv run dd eval >> "$LOG" 2>&1
uv run dd spent >> "$LOG" 2>&1
echo "ALL DONE" >> "$LOG"
