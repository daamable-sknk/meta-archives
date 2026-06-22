"""
Are.na Link 블록이 403·봇 차단 등으로 잘못 수집된 항목 — arena_id로 수동 보정.

sync-arena.py · build-inventory.py 공통.
"""

ARENA_ITEM_OVERRIDES: dict[int, dict] = {
    38907883: {
        "title": "생애문화연구소 옥희살롱 아카이브",
        "url": "http://okeesalon.org/",
        "short": "okeesalon.org",
        "category": "페미니스트·사회운동·대안 아카이브",
        "status": "",
        "note": "Are.na Link 블록 — 봇 차단 페이지, 실제 URL 정상",
    },
    40258043: {
        "title": "서태지 아카이브",
        "url": "https://www.seotaiji-archive.com/xe/",
        "short": "seotaiji-archive.com/xe",
        "category": "한국 공공·지역·역사 아카이브",
        "status": "",
        "note": "Are.na Link 블록 — 크롤러 403, 실제 URL 정상",
    },
}

# API 제목이 이런 패턴이면 수동 검토 권장 (diff 리포트용)
SUSPICIOUS_TITLE_PATTERNS = (
    "403 forbidden",
    "404 not found",
    "please prove that you are human",
    "access denied",
    "just a moment",  # cloudflare
)
