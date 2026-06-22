# 인벤토리를 어떻게 볼 것인가

Are.na API, 1차 그룹, 8축, 경계 등급, YAML 관찰을 **한 흐름으로 읽는 방법**을 정리한다.  
「패싯 목록」은 그중 하나일 뿐이다 — 고정관념 점검용으로 다른 시각도 나란히 둔다.

구현: [`observe.html`](../../observe.html) · [`scripts/build-inventory.py`](../../scripts/build-inventory.py) · [`data/arena/inventory-enriched.json`](../../data/arena/inventory-enriched.json)

*2026-06-22*

---

## 1. 지금 가진 데이터 층

```
Are.na API (125 blocks)
        ↓
meta-archive.json          ← 원본 동기화
        ↓
build-inventory.py         ← 1차 그룹 + 8축 추론 + YAML 병합
        ↓
inventory-enriched.json    ← 패싯 집계·공백·목록
        ↓
observe.html               ← 탐색 UI (로컬/배포)
        ↓
data/archives/*.yml        ← 수동 정밀 관찰 (10개, 점점 증가)
```

**중요:** 125개 중 **10개만** 수동 YAML이다. 나머지 축 값은 **가설**이다. 분포 숫자는 방향을 보여주지만, 틀릴 수 있다. YAML이 늘어날수록 추론층이 교정된다.

---

## 2. 현재 분포 스냅샷 (추론 병합 기준)

| 축 | 많음 | 적음 |
|----|------|------|
| 형식 실험 | low 74, medium 34 | **high 17** |
| 운영 주체 | institution 50, hybrid 44 | corporate 5, individual 11 |
| 수집 단위 | item 97 | text 9, aggregate 19, **place 4** |
| 탐색 | search 87 | **associative 1**, **spatial 3** |
| 접근 | open 122 | **hidden 1**, defunct 2 |
| 스택 | unknown 115 | Omeka 1, wiki 1, static 1 |
| 비평 | none **121** | published 3, in_progress 1 |
| 1차 그룹 | 기관 25, 형식 17, 분류 15 | 잡지 1, 경계 3 |

### 드문 축 (시스템이 표시하는 gap)

- **Omeka** — 퀴어락 비평이 이 축을 대표
- **hidden** — UbuWeb
- **spatial** — Takachizu, SIGNSCAPE, Below the Surface 등 소수
- **place** 단위 — 지도·장소 아카이브는 희소

### 해석

수집본은 **기관형·검색형·저실험**에 치우쳐 있다. 이건 Are.na에 *딸깍*할 때 눈에 띄는 것이 기관 아카이브·플랫폼이기 때문일 수 있다. 반대로 **형식 실험 high·접근 hidden·공간 탐색**은 드물어, 여기에 글을 쓰면 *수집 전체에서의 위치*가 분명해진다.

---

## 3. 보는 방법 여섯 가지 (패싯 말고도)

### A. 패싯 목록 (Faceted index)

- 축별 칩을 조합해 목록을 줄인다.
- 도서관 OPAC·쇼핑몰 필터에 익숙하면 생각이 빠르다.
- **위험:** 축을 고정하면 「분류라는 예정된 실패」가 말한 1차원 붕괴가 UI에 재현된다.

→ [`observe.html`](../../observe.html) 기본 모드.

### B. 공백 우선 (Gap-first)

- “무엇이 **많은가**”보다 “무엇이 **없는가**”부터 본다.
- Omeka 1건, spatial 3건 → **다음 비평이 채울 빈칸**.
- 퀴어락·Takachizu·OASIS는 각각 다른 gap을 메운다.

→ `inventory-enriched.json`의 `gaps` 배열 · observe 상단.

### C. 교차표 (Matrix)

- 두 축만 놓고 셀에 개수 (예: **운영 주체 × 형식 실험**).
- institution+low가 팽창하는지, community+high가 비어 있는지 한눈에.
- 3축 이상은 표가 아니라 **네트워크·평행좌표**가 맞지만, 2축은 종이에도 잘 그려진다.

→ observe의 matrix 테이블.

### D. 꼬리 (Long tail) / 희소 조합

- `operator+unit+form+stack` 조합이 **1건**인 항목 = 분류 체계의 꼬리.
- 퀴어락(hybrid·item·low·**Omeka**)처럼 유일한 조합은 비평 hook.
- `rare_combos_sample` in JSON.

### E. 시간 (Connected_at)

- Are.na `connected_at`으로 **수집의 연대기**.
- 2025-08 초기 36건 → 2026 상반기 급증. 최근에 모인 것이 디자인·웹역사·한국 기관에 치우쳤는지 볼 수 있다.
- (아직 UI 미구현 — JSON에 `connected` 있음.)

### F. 등급·비평 상태 (Workflow)

- [archive-boundary-criteria.md](archive-boundary-criteria.md) 등급 A·B만 켜고 + 미비평만 → **글 후보 113건 중 실질 후보**.
- C는 비교·에세이용, D·E는 제외.

→ observe 체크박스 `A·B만` / `미비평만`.

---

## 4. 패싯이 아닐 때 — 고정관념 점검

| 고정관념 | 대안 |
|----------|------|
| “카테고리 트리가 정답” | 1차 그룹은 **태그 하나**일 뿐. 8축이 본체. |
| “모든 항목에 축을 채워야 한다” | unknown 115는 **미관찰**이지 결함이 아님. |
| “많은 축 = 중요” | institution 50은 **비평 밀도**가 낮을 수 있음. |
| “아카이브만 모았다” | 등급 C 5+α는 **레퍼런스** — 비평은 ‘차이’를 위해 남김. |
| “다음 글 = 가장 흥미로운 것” | **gap을 메우는 글**이 수집 전체 지도를 바꿈. |

---

## 5. 비평 우선순위를 재구성하는 질문

글을 고를 때 패싯 대신 이 질문을 쓸 수 있다.

1. **어느 축이 비어 있는가?** → 퀴어락(Omeka), OASIS(웹 시간), Takachizu(spatial)
2. **어느 조합이 유일한가?** → rare_combos
3. **이미 쓴 글과 어떤 대비를 만드는가?** → UbuWeb ↔ Low-Tech, Europeana ↔ Japan Search, WWA ↔ 퀴어락
4. **등급 A·B인가?** → C는 비교용
5. **YAML을 깊게 쓸 의지가 있는가?** → 없으면 짧은 에세이, 있으면 본격 비평

### 데이터가 제안하는 다음 3편 (이전 계획과 정합)

| 순서 | 대상 | 채우는 gap / 대비 |
|------|------|-------------------|
| 1 | 퀴어락 | Omeka, hybrid, KR, in_progress |
| 2 | OASIS 또는 UK Web Archive | chronology+search, institution, 웹 시간층 |
| 3 | Low-Tech | form high, UbuWeb 대비 |

**추가 후보 (희소 축):** Takachizu(place+spatial), Monoskop(wiki+associative), 404s.design(형식 B).

---

## 6. 운영 루틴 제안

1. Are.na에 추가 → `bash scripts/sync.sh` (또는 `sync.sh --dry-run`으로 diff 확인)
2. diff 검토 → `arena_overrides.py` · 신규 `category` 수정
3. `observe.html`에서 분포·필터 확인 (`bash scripts/serve.sh`)
4. 비평 시작할 항목만 `data/archives/<slug>.yml` 수동 작성 → 추론 교정
5. 글 발행 후 `critique.status` YAML·`CRITIQUE_BY_HOST` 갱신

---

## 8. YAML vs 필터 UI — 무엇을 먼저?

**125개 YAML을 먼저 다 만들 필요는 없다.**

| 층 | 역할 | 규모 |
|----|------|------|
| **추론** (`build-inventory.py`) | 탐색·분포·후보 찾기 | 125개 전부 (가설) |
| **YAML** (`data/archives/`) | 비평·정밀 관찰의 근거 | 글 쓸 때만, 점진적 |
| **축 정의 문서** | 각 카테고리가 무엇을 의미하는지 | 스키마·경계 기준 — 지금 병행 가능 |

권장 순서:

1. **필터 UI·축 정의를 다듬는다** — observe에서 쓰기 불편한 축 이름·값·그룹을 고친다 (지금 단계).
2. **비평할 아카이브만 YAML** — 퀴어락 → 다음 후보 1~2개. 글과 YAML은 한 세트.
3. **YAML이 쌓이면** `build-inventory.py` 규칙을 교정 — 수동이 추론을 덮어쓴다 (이미 구현됨).
4. **나머지 100+는** 추론으로 두고, 필터로 훑다가 “이건 손봐야겠다” 싶을 때만 YAML.

즉: **분류 필터를 먼저 다듬고**, YAML은 **해설 파이프라인**으로만 늘린다. 전수 YAML은 목표가 아니다.

---

## 9. 이후 확장 (선택)

- **연대기 뷰:** `connected` 타임라인
- **2D scatter:** form_experiment × self_as_archive 버블 차트
- **Are.na 채널과 양방향:** block id로 observe ↔ Are.na 링크
- **경계 C 전용:** “아카이브 vs DB” 비교 모드

패싯이 답이 아니라 **여러 뷰를 오가며 수집을 거울로 보는 것**이 목표다.

---

*Last updated: 2026-06-22*
