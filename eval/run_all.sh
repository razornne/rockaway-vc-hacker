#!/usr/bin/env bash
# Full pipeline for every company in eval/companies.json. Logs to .dd/run_all.log
cd "$(dirname "$0")/.." || exit 1
LOG=.dd/run_all.log
: > "$LOG"
uv run dd seed >> "$LOG" 2>&1
for c in $(uv run python -c "import json;print(' '.join(c['id'] for c in json.load(open('eval/companies.json',encoding='utf-8'))))"); do
  start=$(date +%s)
  echo "=== $c $(date +%H:%M:%S)" >> "$LOG"
  uv run dd collect "$c" >> "$LOG" 2>&1
  uv run dd extract "$c" >> "$LOG" 2>&1
  uv run dd verify "$c" >> "$LOG" 2>&1
  uv run dd analyze "$c" >> "$LOG" 2>&1
  uv run dd dossier "$c" --output .dd/briefs >> "$LOG" 2>&1
  echo "--- $c done in $(( $(date +%s) - start ))s" >> "$LOG"
done
uv run dd spent >> "$LOG" 2>&1
echo "ALL DONE" >> "$LOG"
