#!/usr/bin/env python3
"""
Are.na meta-archive 채널 → data/arena/meta-archive.json 동기화.

기존 항목의 category·note·status는 로컬 값을 유지한다.
신규 항목은 category=「미분류·검토 필요」로 넣고 diff 리포트를 출력한다.
arena_overrides.py 보정은 API 병합 후 적용.

Usage:
  python3 scripts/sync-arena.py              # fetch + 저장 + inventory 빌드
  python3 scripts/sync-arena.py --dry-run    # diff만
  python3 scripts/sync-arena.py --no-build   # JSON만 갱신
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from arena_overrides import ARENA_ITEM_OVERRIDES, SUSPICIOUS_TITLE_PATTERNS  # noqa: E402

ARENA_JSON = ROOT / "data/arena/meta-archive.json"
REGISTRY = ROOT / "data/arena/id-registry.json"
BUILD_SCRIPT = SCRIPT_DIR / "build-inventory.py"

CHANNEL_SLUG = "meta-archive"
API_BASE = "https://api.are.na/v2/channels"
PER_PAGE = 100
NEW_ITEM_CATEGORY = "미분류·검토 필요"
# 기존 항목: 로컬 메타 유지. API는 연결일·블록 유형만 반영.
PRESERVE_ON_SYNC = ("title", "url", "short", "category", "note", "status")
API_TOUCH_KEYS = ("connected", "class")


def fetch_channel_blocks() -> tuple[dict, list[dict]]:
    """페이지네이션으로 채널 메타 + 전체 블록 수집."""
    blocks: list[dict] = []
    channel_meta: dict = {}
    page = 1

    while True:
        url = f"{API_BASE}/{CHANNEL_SLUG}?per={PER_PAGE}&page={page}"
        req = urllib.request.Request(url, headers={"User-Agent": "meta-archives-sync/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode())
        except urllib.error.URLError as e:
            raise SystemExit(f"Are.na API 요청 실패: {e}") from e

        if page == 1:
            channel_meta = {
                "channel": data.get("slug", CHANNEL_SLUG),
                "channel_length": data.get("length", 0),
            }

        contents = data.get("contents") or []
        if not contents:
            break
        blocks.extend(contents)
        if len(contents) < PER_PAGE:
            break
        page += 1

    return channel_meta, blocks


def extract_url(block: dict) -> str | None:
    """Link / Image / Text 블록에서 대표 URL 추출."""
    source = block.get("source") or {}
    if source.get("url"):
        return source["url"].strip()

    html = block.get("content_html") or ""
    m = re.search(r'href=["\'](https?://[^"\']+)["\']', html, re.I)
    if m:
        return m.group(1).strip()

    return None


def extract_short(block: dict, url: str) -> str:
    source = block.get("source") or {}
    provider = source.get("provider") or {}
    if provider.get("name"):
        name = provider["name"].strip()
        if name.startswith("http"):
            return re.sub(r"^https?://", "", name).rstrip("/")
        return name
    if url:
        return re.sub(r"^https?://(www\.)?", "", url).split("?")[0].rstrip("/")
    return ""


def connected_date(block: dict) -> str:
    raw = block.get("connected_at") or block.get("created_at") or ""
    return raw[:10] if raw else ""


def infer_status_from_title(title: str) -> str:
    t = title.lower()
    if "403" in t or "forbidden" in t:
        return "403"
    if "404" in t or "not found" in t:
        return "404"
    if "prove that you are human" in t:
        return "미확인"
    return ""


def norm_url(u: str | None) -> str:
    if not u:
        return ""
    u = u.strip().lower().rstrip("/")
    return re.sub(r"^https?://www\.", "https://", u)


def meaningful_drift(fresh: dict, local: dict) -> list[str]:
    drift = []
    if (fresh.get("title") or "").strip() != (local.get("title") or "").strip():
        drift.append(f"API title: {fresh.get('title')!r}")
    if norm_url(fresh.get("url")) != norm_url(local.get("url")):
        drift.append(f"API url: {fresh.get('url')!r}")
    return drift


def is_suspicious(item: dict) -> bool:
    title = (item.get("title") or "").lower()
    if any(p in title for p in SUSPICIOUS_TITLE_PATTERNS):
        return True
    # 도메인만 제목인 경우 (예: okeesalon.org)
    short = (item.get("short") or "").lower()
    if short and title.replace("www.", "") in (short, short.split("/")[0]):
        if len(title) < 40 and "." in title and " " not in title.strip():
            return True
    return False


def api_fresh_item(block: dict) -> dict | None:
    """API에서만 읽은 값 (diff·신규용)."""
    url = extract_url(block)
    if not url:
        return None

    title = (block.get("title") or block.get("generated_title") or url).strip()
    return {
        "id": block["id"],
        "title": title,
        "url": url,
        "short": extract_short(block, url),
        "class": block.get("class", "Link"),
        "connected": connected_date(block),
        "status": infer_status_from_title(title),
        "category": NEW_ITEM_CATEGORY,
        "note": (block.get("description") or "").strip()[:200],
    }


def block_to_item(block: dict, existing: dict | None) -> dict | None:
    fresh = api_fresh_item(block)
    if not fresh:
        return None

    if existing:
        item = dict(existing)
        for key in API_TOUCH_KEYS:
            if fresh.get(key):
                item[key] = fresh[key]
    else:
        item = fresh

    overrides = ARENA_ITEM_OVERRIDES.get(block["id"], {})
    item.update(overrides)
    return item


def load_existing() -> dict:
    if not ARENA_JSON.exists():
        return {"items": []}
    return json.loads(ARENA_JSON.read_text(encoding="utf-8"))


def inventory_id_for(arena_id: int) -> str | None:
    if not REGISTRY.exists():
        return None
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    return reg.get("by_arena_id", {}).get(str(arena_id))


def merge_blocks(blocks: list[dict], existing_by_id: dict[int, dict]) -> list[dict]:
    items: list[dict] = []
    for block in blocks:
        bid = block["id"]
        item = block_to_item(block, existing_by_id.get(bid))
        if item:
            items.append(item)
    return items


def diff_report(old_items: list[dict], new_items: list[dict], blocks: list[dict]) -> dict:
    old_by_id = {it["id"]: it for it in old_items}
    new_by_id = {it["id"]: it for it in new_items}
    fresh_by_id = {b["id"]: api_fresh_item(b) for b in blocks}
    fresh_by_id = {k: v for k, v in fresh_by_id.items() if v}

    report = {
        "new": [],
        "removed": [],
        "changed": [],
        "api_drift": [],
        "suspicious": [],
        "review_category": [],
    }

    for it in new_items:
        iid = inventory_id_for(it["id"])
        label = f"{iid or '?'} · {it['title'][:50]}"
        if it["id"] not in old_by_id:
            report["new"].append({**it, "_label": label})
        else:
            old = old_by_id[it["id"]]
            changes = []
            for field in API_TOUCH_KEYS:
                if old.get(field) != it.get(field):
                    changes.append(f"{field}: {old.get(field)!r} → {it.get(field)!r}")
            if changes:
                report["changed"].append({"id": it["id"], "label": label, "changes": changes})

            fresh = fresh_by_id.get(it["id"])
            if fresh and it["id"] not in ARENA_ITEM_OVERRIDES:
                drift = meaningful_drift(fresh, old)
                if drift:
                    report["api_drift"].append({
                        "id": it["id"],
                        "label": label,
                        "local_url": old.get("url"),
                        "drift": drift,
                    })

        check = fresh_by_id.get(it["id"]) or it
        if is_suspicious(check) and it["id"] not in ARENA_ITEM_OVERRIDES:
            report["suspicious"].append({
                "id": it["id"],
                "label": label,
                "title": check["title"],
                "url": check["url"],
            })
        if it.get("category") == NEW_ITEM_CATEGORY:
            report["review_category"].append({"id": it["id"], "label": label})

    for oid, old in old_by_id.items():
        if oid not in new_by_id:
            iid = inventory_id_for(oid)
            report["removed"].append({
                "id": oid,
                "label": f"{iid or '?'} · {old.get('title', '')[:50]}",
                "url": old.get("url"),
            })

    return report


def print_report(report: dict) -> None:
    def section(title: str, rows: list, fmt):
        if not rows:
            return
        print(f"\n{title} ({len(rows)})")
        print("-" * 40)
        for row in rows:
            print(fmt(row))

    print("=" * 40)
    print("Are.na sync diff")
    print("=" * 40)

    section("신규", report["new"], lambda r: f"  {r['_label']}\n    {r['url']}")
    section("제거됨 (채널에서 사라짐)", report["removed"], lambda r: f"  {r['label']}\n    {r.get('url')}")
    section("변경 (로컬 반영)", report["changed"], lambda r: f"  {r['label']}\n    " + "\n    ".join(r["changes"]))
    section(
        "API와 다름 (로컬 유지 — overrides 검토)",
        report["api_drift"],
        lambda r: f"  {r['label']}\n    local: {r.get('local_url')}\n    " + "\n    ".join(r["drift"]),
    )
    section("검토 권장 (의심 제목·URL)", report["suspicious"], lambda r: f"  {r['label']}\n    {r['url']}")
    section("그룹 미배치 (category 수정 필요)", report["review_category"], lambda r: f"  {r['label']}")

    if not any(report[k] for k in report):
        print("\n변경 없음 — API와 로컬이 일치합니다.")


def block_type_counts(items: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for it in items:
        cls = it.get("class", "Link")
        counts[cls] = counts.get(cls, 0) + 1
    return counts


def build_inventory() -> None:
    subprocess.run([sys.executable, str(BUILD_SCRIPT)], check=True, cwd=ROOT)


def main() -> None:
    parser = argparse.ArgumentParser(description="Are.na → meta-archive.json 동기화")
    parser.add_argument("--dry-run", action="store_true", help="diff만 출력, 파일 미저장")
    parser.add_argument("--no-build", action="store_true", help="inventory-enriched.json 빌드 생략")
    args = parser.parse_args()

    print("→ Are.na API fetch…")
    channel_meta, blocks = fetch_channel_blocks()
    print(f"  블록 {len(blocks)}개 (채널 length={channel_meta.get('channel_length')})")

    existing_doc = load_existing()
    existing_items = existing_doc.get("items", [])
    existing_by_id = {it["id"]: it for it in existing_items}

    new_items = merge_blocks(blocks, existing_by_id)
    report = diff_report(existing_items, new_items, blocks)
    print_report(report)

    if args.dry_run:
        print("\n(dry-run — 파일 저장·빌드 생략)")
        return

    out = {
        "synced_at": date.today().isoformat(),
        **channel_meta,
        "block_types": block_type_counts(new_items),
        "items": new_items,
    }
    ARENA_JSON.parent.mkdir(parents=True, exist_ok=True)
    ARENA_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n→ 저장: {ARENA_JSON.relative_to(ROOT)}")

    if report["new"] or report["review_category"] or report["suspicious"]:
        print("\n⚠ 수동 검토 후 category·arena_overrides.py 를 확인하세요.")

    if not args.no_build:
        print("\n→ inventory 빌드…")
        build_inventory()
        print("  완료: data/arena/inventory-enriched.json")


if __name__ == "__main__":
    main()
