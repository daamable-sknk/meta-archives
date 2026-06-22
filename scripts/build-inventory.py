#!/usr/bin/env python3
"""
Are.na meta-archive.json + data/archives/*.yml → inventory-enriched.json

Usage: python3 scripts/build-inventory.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from arena_overrides import ARENA_ITEM_OVERRIDES  # noqa: E402

ARENA = ROOT / "data/arena/meta-archive.json"
ARCHIVES_DIR = ROOT / "data/archives"
OUT = ROOT / "data/arena/inventory-enriched.json"
REGISTRY = ROOT / "data/arena/id-registry.json"

# --- heuristic: 1차 그룹 → 기본 축 ---
GROUP_AXES: dict[str, dict] = {
    "형식이 곧 내용인 아카이브": {
        "form_experiment": "high",
        "self_as_archive": "explicit",
    },
    "분류 체계가 독특한 아카이브": {
        "navigation": "taxonomy",
        "form_experiment": "medium",
    },
    "대규모 통합 플랫폼": {
        "operator": "institution",
        "unit": "aggregate",
        "navigation": "search",
        "form_experiment": "low",
    },
    "정부·공공 웹 아카이브": {
        "operator": "institution",
        "unit": "aggregate",
        "navigation": ["chronology", "search"],
        "stack": "web-crawler",
        "form_experiment": "low",
    },
    "기관 아카이브": {
        "operator": "institution",
        "unit": "item",
        "navigation": "search",
        "form_experiment": "low",
    },
    "한국 공공·지역·역사 아카이브": {
        "operator": "institution",
        "unit": "item",
        "locale": ["KR"],
        "form_experiment": "low",
    },
    "페미니스트·사회운동·대안 아카이브": {
        "operator": "community",
        "unit": "item",
        "form_experiment": "medium",
    },
    "개인 아카이브·포트폴리오": {
        "operator": "individual",
        "unit": "item",
        "self_as_archive": "implicit",
    },
    "예술가 출판·독립 플랫폼": {
        "operator": "hybrid",
        "unit": "text",
        "navigation": "chronology",
    },
    "디자인·시각 아카이브": {
        "operator": "hybrid",
        "unit": "item",
        "navigation": "taxonomy",
    },
    "잡지·미디어 아카이브": {
        "operator": "corporate",
        "unit": "text",
        "navigation": "chronology",
    },
    "웹 역사·디지털 유산": {
        "operator": "institution",
        "unit": "aggregate",
        "navigation": "chronology",
        "form_experiment": "medium",
    },
    "디자인 영감·레퍼런스 (경계)": {
        "operator": "corporate",
        "unit": "item",
        "navigation": "taxonomy",
        "self_as_archive": "denied",
        "form_experiment": "medium",
    },
    "접근 불가·미확인": {
        "access_regime": "defunct",
    },
    "미분류·검토 필요": {},
}

BOUNDARY_BY_URL: dict[str, dict] = {
    "godly.website": {"grade": "C", "note": "영감 보드"},
    "siteofsites.co": {"grade": "C", "note": "영감 보드"},
    "steep.design": {"grade": "C", "note": "영감 보드"},
    "discogs.com": {"grade": "C", "note": "DB+마켓"},
    "press.stripe.com": {"grade": "C", "note": "출판 목록"},
    "404s.design": {"grade": "B", "note": "오류 페이지 수집"},
    "afoolzerrand.com": {"grade": "B", "note": "극소 주제"},
    "butbutbut.org": {"grade": "B", "note": "글 플랫폼"},
    "global-fandom.com": {"grade": "B", "note": "living archive"},
    "fontsinuse.com": {"grade": "B", "note": "searchable archive"},
    "trendlist.org": {"grade": "B", "note": "트렌드 문서화"},
    "monoskop.org": {"grade": "A", "note": "위키 지식 그래프"},
    "gutenberg.org": {"grade": "A", "note": "디지털 도서관"},
    "unarchivingarchitecture.ethz.ch": {"grade": "D", "note": "심포지엄"},
    "lacarchive.com": {"grade": "D", "note": "메타 목록(홈)"},
}

LOCALE_HINTS = [
    ([".kr", "korea", "한국", "서울", "제주", "국립", "조선", "민속", "강서", "경기"], "KR"),
    ([".jp", "japan", "일본", "히로시마", "오시마"], "JP"),
    ([".eu", "europe", "europeana", "gallica", "macba", "amsterdam", "zurich", "ethz"], "EU"),
    ([".uk", "uk ", "british", "victoria", "government web"], "GB"),
    ([".ch", "switzerland", "sitterwerk"], "CH"),
    ([".au", "australia", "victoria"], "AU"),
]

CRITIQUE_BY_HOST = {
    "ubu.com": ("published", "ubuweb"),
    "womenwritingarchitecture.org": ("published", "women-writing-architecture"),
    "europeana.eu": ("published", "europeana"),
    "queerarchive.org": ("in_progress", "korea-queer-archive"),
}


def host_key(url: str) -> str:
    host = re.sub(r"^www\.", "", re.sub(r"^https?://", "", url).split("/")[0].lower())
    return host.split(":")[0]


def slugify(title: str, url: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", host_key(url).replace(".", "-")).strip("-")


URL_AXES: dict[str, dict] = {
    "takachizu.org": {"unit": "place", "navigation": "spatial", "operator": "community"},
    "signscape.lovable.app": {"unit": "place", "navigation": "spatial"},
    "publicstairs.com": {"unit": "place", "navigation": "taxonomy"},
    "oshimaland.co.jp": {"unit": "place", "navigation": "search"},
    "belowthesurface.amsterdam": {"unit": "item", "navigation": "spatial"},
    "jiamdiary.info": {"unit": "text", "navigation": "associative", "form_experiment": "high"},
    "womenwritingarchitecture.org": {"unit": "text", "navigation": ["taxonomy", "search"]},
    "bugguide.net": {"unit": "item", "navigation": "taxonomy", "operator": "community"},
}


def norm_locale(val) -> list[str]:
    """locale은 항상 문자열 배열. YAML 스칼라 'multi' 등이 문자열로 남으면 facet에서 글자 단위 분리됨."""
    if val is None:
        return []
    if isinstance(val, list):
        return [str(x) for x in val if x]
    if isinstance(val, str):
        return [val] if val else []
    return []


def infer_locale(title: str, url: str) -> list[str]:
    blob = (title + " " + url).lower()
    found: list[str] = []
    for patterns, code in LOCALE_HINTS:
        if any(p in blob for p in patterns):
            found.append(code)
    if not found:
        if re.search(r"[\u3131-\uD79D]", title):
            found.append("KR")
        else:
            found.append("EN")
    return sorted(set(found))


def infer_boundary(url: str, group: str) -> dict:
    host = url.lower()
    for key, val in BOUNDARY_BY_URL.items():
        if key in host:
            return val
    if group == "디자인 영감·레퍼런스 (경계)":
        return {"grade": "C", "note": "경계 그룹"}
    if group == "접근 불가·미확인":
        return {"grade": "E", "note": "접근 불가"}
    return {"grade": "B", "note": None}


def infer_critique(url: str) -> dict:
    hk = host_key(url)
    if hk in CRITIQUE_BY_HOST:
        status, slug = CRITIQUE_BY_HOST[hk]
        return {"status": status, "post_slug": slug}
    return {"status": "none", "post_slug": None}


def parse_yaml_simple(path: Path) -> dict:
    """Minimal YAML subset parser for our archive files."""
    text = path.read_text(encoding="utf-8")
    data: dict = {}

    def scalar(key: str):
        m = re.search(rf"^{key}:\s*(.+)$", text, re.M)
        if not m:
            return None
        v = m.group(1).strip().strip('"')
        if v == "null":
            return None
        return v

    def block(key: str) -> dict:
        m = re.search(rf"^{key}:\n((?:  .+\n)+)", text, re.M)
        if not m:
            return {}
        out = {}
        for line in m.group(1).splitlines():
            mm = re.match(r"  (\w+):\s*(.+)", line)
            if mm:
                val = mm.group(2).strip().strip('"')
                if val.startswith("["):
                    out[mm.group(1)] = [
                        x.strip().strip('"') for x in val.strip("[]").split(",") if x.strip()
                    ]
                elif val == "null":
                    out[mm.group(1)] = None
                else:
                    out[mm.group(1)] = val
        return out

    data["slug"] = scalar("slug")
    data["axes"] = block("axes")
    data["boundary"] = block("boundary")
    data["critique"] = block("critique")
    inv = block("inventory")
    if inv:
        data["inventory"] = inv
    return data


def merge_axes(group: str, title: str, url: str, manual: dict | None) -> dict:
    axes = {
        "operator": "hybrid",
        "unit": "item",
        "navigation": "search",
        "form_experiment": "low",
        "self_as_archive": "explicit",
        "access_regime": "open",
        "stack": "unknown",
        "locale": infer_locale(title, url),
    }
    axes.update(GROUP_AXES.get(group, {}))
    hk = host_key(url)
    for host, overrides in URL_AXES.items():
        if host in hk:
            axes.update(overrides)
    if manual and manual.get("axes"):
        for k, v in manual["axes"].items():
            if v is not None:
                axes[k] = v
    if "queerarchive" in url:
        axes["stack"] = "Omeka"
    if "omeka" in url.lower():
        axes["stack"] = "Omeka"
    if "monoskop" in url:
        axes["stack"] = "wiki"
        axes["navigation"] = "associative"
    if "ubu.com" in url:
        axes["access_regime"] = "hidden"
        axes["stack"] = "static"
    axes["locale"] = norm_locale(axes.get("locale"))
    return axes


def facet_counts(items: list[dict]) -> dict:
    counts: dict[str, Counter] = defaultdict(Counter)
    axis_keys = [
        "operator", "unit", "form_experiment", "self_as_archive",
        "access_regime", "stack",
    ]
    for it in items:
        counts["group"][it["group"]] += 1
        counts["boundary"][it["boundary"]["grade"]] += 1
        counts["critique"][it["critique"]["status"]] += 1
        counts["block_class"][it["block_class"]] += 1
        for k in axis_keys:
            v = it["axes"].get(k)
            if isinstance(v, list):
                for x in v:
                    counts[k][x] += 1
            elif v:
                counts[k][v] += 1
        nav = it["axes"].get("navigation")
        if isinstance(nav, list):
            for n in nav:
                counts["navigation"][n] += 1
        elif nav:
            counts["navigation"][nav] += 1
        for loc in norm_locale(it["axes"].get("locale")):
            counts["locale"][loc] += 1
    return {k: dict(v) for k, v in counts.items()}


def rare_combos(items: list[dict]) -> list[dict]:
    """Facet combinations with n=1 — potential essay hooks."""
    combos: Counter = Counter()
    for it in items:
        a = it["axes"]
        key = (
            a.get("operator"),
            a.get("unit"),
            a.get("form_experiment"),
            a.get("stack"),
        )
        combos[key] += 1
    singles = [k for k, n in combos.items() if n == 1]
    out = []
    for it in items:
        a = it["axes"]
        key = (a.get("operator"), a.get("unit"), a.get("form_experiment"), a.get("stack"))
        if key in singles:
            out.append({
                "title": it["title"],
                "url": it["url"],
                "combo": {
                    "operator": key[0],
                    "unit": key[1],
                    "form_experiment": key[2],
                    "stack": key[3],
                },
            })
    return out[:20]


def format_inventory_id(seq: int) -> str:
    return f"MA-{seq:03d}"


def ensure_id_registry(arena_items: list[dict]) -> dict:
    """Are.na 블록 ID → 영구 inventory_id (MA-###). 신규 항목만 번호 부여."""
    if REGISTRY.exists():
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    else:
        registry = {"version": 1, "prefix": "MA", "next_seq": 1, "by_arena_id": {}}

    by_arena: dict[str, str] = registry.setdefault("by_arena_id", {})
    seq = int(registry.get("next_seq", 1))

    missing = [it for it in arena_items if str(it["id"]) not in by_arena]
    if not by_arena:
        # 최초: Are.na 수집일 → 블록 ID 순으로 일괄 부여
        missing = sorted(arena_items, key=lambda x: (x.get("connected", ""), x["id"]))
    else:
        missing = sorted(missing, key=lambda x: (x.get("connected", ""), x["id"]))

    for it in missing:
        by_arena[str(it["id"])] = format_inventory_id(seq)
        seq += 1

    registry["next_seq"] = seq
    registry["updated_at"] = __import__("datetime").date.today().isoformat()
    REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")
    return registry


def inventory_id_for(registry: dict, arena_block_id: int) -> str:
    return registry["by_arena_id"][str(arena_block_id)]


def gaps(counts: dict) -> list[dict]:
    """Underrepresented axes vs collection median."""
    notes = []
    fe = counts.get("form_experiment", {})
    if fe.get("high", 0) < 10:
        notes.append({
            "axis": "form_experiment",
            "value": "high",
            "count": fe.get("high", 0),
            "hint": "형식 실험 축이 상대적으로 적음 — UbuWeb/Low-Tech 대비 후보 탐색",
        })
    if counts.get("stack", {}).get("Omeka", 0) <= 2:
        notes.append({
            "axis": "stack",
            "value": "Omeka",
            "count": counts.get("stack", {}).get("Omeka", 0),
            "hint": "Omeka 사례가 적음 — 퀴어락 비평이 축을 채움",
        })
    if counts.get("unit", {}).get("place", 0) <= 2:
        notes.append({
            "axis": "unit",
            "value": "place",
            "count": counts.get("unit", {}).get("place", 0),
            "hint": "장소 단위 수집이 드묾 — Takachizu, SIGNSCAPE 등",
        })
    if counts.get("access_regime", {}).get("hidden", 0) <= 2:
        notes.append({
            "axis": "access_regime",
            "value": "hidden",
            "count": counts.get("access_regime", {}).get("hidden", 0),
            "hint": "발견 거부형 접근이 드묾 — UbuWeb",
        })
    nav = counts.get("navigation", {})
    if nav.get("spatial", 0) <= 3:
        notes.append({
            "axis": "navigation",
            "value": "spatial",
            "count": nav.get("spatial", 0),
            "hint": "공간 탐색 구조가 드묾",
        })
    return notes


def main():
    arena = json.loads(ARENA.read_text(encoding="utf-8"))
    manual_by_slug: dict[str, dict] = {}
    manual_by_host: dict[str, dict] = {}
    for yml in ARCHIVES_DIR.glob("*.yml"):
        if yml.name.startswith("_"):
            continue
        parsed = parse_yaml_simple(yml)
        if parsed.get("slug"):
            manual_by_slug[parsed["slug"]] = parsed
        inv = parsed.get("inventory") or {}
        # also index by url in future yml; for now match slug to known hosts
        for host, data in URL_AXES.items():
            if parsed.get("slug") and parsed["slug"] in host:
                manual_by_host[host] = parsed
    # explicit host → yaml from files
    host_yaml = {
        "ubu.com": "ubuweb",
        "womenwritingarchitecture.org": "women-writing-architecture",
        "queerarchive.org": "korea-queer-archive",
        "solar.lowtechmagazine.com": "low-tech-magazine",
        "nl.go.kr": "oasis",
        "nationalarchives.gov.uk": "uk-government-web-archive",
        "takachizu.org": "takachizu",
        "jpsearch.go.jp": "japan-search",
        "godly.website": "godly",
        "discogs.com": "discogs",
    }
    for host, slug in host_yaml.items():
        if slug in manual_by_slug:
            manual_by_host[host] = manual_by_slug[slug]

    registry = ensure_id_registry(arena["items"])

    items = []
    for raw in arena["items"]:
        overrides = ARENA_ITEM_OVERRIDES.get(raw["id"], {})
        raw = {**raw, **overrides}
        url = raw["url"]
        title = raw["title"]
        group = raw["category"]
        slug = slugify(title, url)
        hk = host_key(url)
        manual = None
        for host, data in manual_by_host.items():
            if host in hk:
                manual = data
                break
        if not manual:
            manual = manual_by_slug.get(slug)
        axes = merge_axes(group, title, url, manual)
        boundary = infer_boundary(url, group)
        if manual and manual.get("boundary", {}).get("grade"):
            boundary = {
                "grade": manual["boundary"]["grade"],
                "note": manual["boundary"].get("note"),
            }
        critique = infer_critique(url)
        if manual and manual.get("critique", {}).get("status"):
            critique = {
                "status": manual["critique"]["status"],
                "post_slug": manual["critique"].get("post_slug"),
            }
        items.append({
            "inventory_id": inventory_id_for(registry, raw["id"]),
            "arena_id": raw["id"],
            "slug": slug,
            "title": title,
            "url": url,
            "short": raw.get("short", ""),
            "group": group,
            "block_class": raw["class"],
            "connected": raw.get("connected", ""),
            "axes": axes,
            "boundary": boundary,
            "critique": critique,
            "has_manual_yaml": manual is not None,
        })

    counts = facet_counts(items)
    summary = {
        "built_at": "2026-06-22",
        "total": len(items),
        "manual_yaml_count": len(manual_by_slug),
        "facet_counts": counts,
        "gaps": gaps(counts),
        "rare_combos_sample": rare_combos(items),
        "items": sorted(items, key=lambda x: x["inventory_id"]),
    }
    OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} ({len(items)} items)")
    print(f"Registry: {REGISTRY} (next {format_inventory_id(registry['next_seq'])})")
    print("form_experiment:", counts.get("form_experiment"))
    print("operator:", counts.get("operator"))
    print("boundary:", counts.get("boundary"))
    print("gaps:", len(summary["gaps"]))


if __name__ == "__main__":
    main()
