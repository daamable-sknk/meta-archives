#!/usr/bin/env bash
# meta-archives 로컬 미리보기 — inventory 빌드 후 observe.html 서버
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PORT="${PORT:-8765}"
OPEN="${OPEN:-1}"

echo "→ inventory 빌드…"
python3 scripts/build-inventory.py

URL="http://localhost:${PORT}/observe.html"
echo ""
echo "  관찰 목록  ${URL}"
echo "  메인       http://localhost:${PORT}/"
echo ""

if command -v lsof >/dev/null 2>&1 && lsof -iTCP:"${PORT}" -sTCP:LISTEN -t >/dev/null 2>&1; then
  echo "  (포트 ${PORT} 이미 사용 중 — 기존 서버에 연결)"
  echo "  종료: 해당 터미널에서 Ctrl+C"
  echo ""
  [[ "$OPEN" == "1" ]] && command -v open >/dev/null 2>&1 && open "$URL"
  exit 0
fi

echo "  종료: Ctrl+C"
echo ""

if [[ "$OPEN" == "1" ]] && command -v open >/dev/null 2>&1; then
  # 서버 기동 직전에 열면 첫 fetch가 실패할 수 있어 잠깐 뒤에 연다
  (sleep 0.4 && open "$URL") &
fi

exec python3 -m http.server "$PORT"
