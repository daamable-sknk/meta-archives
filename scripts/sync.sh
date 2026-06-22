#!/usr/bin/env bash
# Are.na → meta-archive.json → inventory-enriched.json
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

DRY=0
NO_BUILD=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    --no-build) NO_BUILD=1 ;;
  esac
done

ARGS=()
[[ "$DRY" == "1" ]] && ARGS+=(--dry-run)
[[ "$NO_BUILD" == "1" ]] && ARGS+=(--no-build)

python3 scripts/sync-arena.py "${ARGS[@]}"
