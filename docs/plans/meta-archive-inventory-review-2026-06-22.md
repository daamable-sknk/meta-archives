# meta-archive 채널 점검 (2026-06-22)

Are.na [meta-archive](https://www.are.na/daehwan-jang/meta-archive) 채널을 API로 대조하고, 앞으로의 비평을 위한 평론 요소·다차원 매핑을 정리한 기록이다. 동기화 결과는 [meta-archives.md](meta-archives.md)와 `data/arena/meta-archive.json`에 반영했다.

---

## 1. 동기화 요약

| 항목 | 이전 (`meta-archives.md`) | 이후 (2026-06-22) |
|------|---------------------------|-------------------|
| 등재 URL | ~58개 | **125개** (전체 블록) |
| 블록 유형 | Link 위주 가정 | Link 110 / Image 8 / Text 7 |
| 로컬 CSV (`content/meta-archive/`) | 36개 (초기 익스포트) | **폐기 권장** — `data/arena/meta-archive.json` 사용 |
| 마지막 갱신 | 2026-03-25 | 2026-06-22 |

### API

```
GET https://api.are.na/v2/channels/meta-archive?per=100&page=1
GET https://api.are.na/v2/channels/meta-archive?per=100&page=2
```

### 동기화 시 주의

- **Image·Text 블록**은 `source.url`이 CDN일 수 있다. 실제 사이트 URL은 `source.url`(외부 도메인) 또는 `content_html`의 `href`에서 추출한다.
- Are.na가 CSS가 포함된 URL을 잘라 저장한 Text 블록이 있다(예: The Arquives, History of Information). 이 경우 `href` 파싱 시 `al-gradient` 이전까지만 취한다.
- 그룹 분류는 **1차 태그**다. 한 항목이 여러 축에 동시에 해당한다(아래 §4).

---

## 2. 수집본 프로필

키워드·도메인 기반 대략적 군집(중복 허용):

| 군집 | 대략 수 | 예시 |
|------|---------|------|
| 기관 아카이브 | ~25 | SeMA AA, KoRICA, MACBA, De Appel, e뮤지엄 |
| 형식 실험 | ~17 | UbuWeb, Low-Tech, Cameron's World, 404s.design |
| 분류·주제 특이 | ~15 | WWA, Takachizu, BugGuide, PublicStairs |
| 대안·운동 | ~13 | LACA, 내란대장경, Herbal Archive, BUT |
| 개인·포트폴리오 | ~9 | Jetset, Ashby, The Portal, 정성일 아카이브 |
| 통합 플랫폼 | ~8 | Europeana, Japan Search, Gallica, Monoskop |
| 한국 공공·역사 | ~7 | 제주4·3, OASIS, 조선왕조실록, 전쟁과여성인권 |
| 디자인·시각 | ~6 | Moving Poster, CMF HOW'S, Fonts In Use |
| 웹 역사 | ~4 | Web Design Museum, Below the Surface |
| 디자인 영감 (경계) | ~3 | Godly, Site of Sites, STEEP |
| 접근 불가 | 0 | (없음 — 서태지·옥희살롱은 Are.na 봇 차단 오수집, 수동 보정 완료) |

### 강점

- 지역·언어 스펙트럼이 넓어졌다(한국 기관, 일본·유럽·호주·캐나다).
- 형식 실험과 전통 기관이 섞여 **대비 비평**에 유리하다.
- 웹 아카이브(OASIS, UK), 사회운동(내란대장경), 극소 주제(PublicStairs, Ian's Shoelace)가 공존한다.

### 정리가 필요한 부분

1. **경계 사례** — Godly, Site of Sites, Discogs, Stripe Press, 404s.design 등: 아카이브인가 레퍼런스/DB인가
2. **중복·근접** — TFI 홈 + Digital Archives, LACA 홈 + Alternative Libraries
3. **블록 타입 혼재** — Image/Text는 URL 추출·동기화 스크립트에 별도 처리 필요
4. **비평 대비 메타데이터** — 125개 중 YAML 관찰 기록은 극소수(UbuWeb, WWA 등)

---

## 3. 평론 요소 (기존 글에서 추출)

이미 발행·초안에 있는 비평에서 반복되는 **관찰 축**이다. `docs/concept.md`의 네 가지 질문과 `docs/schema.md` v1.0 필드의 실전 버전으로 볼 수 있다.

| 코드 | 축 | 질문 | 대표 사례 |
|------|-----|------|-----------|
| A | 자기정의 vs 구조 | 스스로 뭐라고 부르는가, 실제로 어떻게 작동하는가 | WWA: bibliography vs taxonomy 관계 |
| B | 형식 = 내용 | UI·인프라·매체 선택이 메시지와 결합하는가 | UbuWeb 4KB, Low-Tech 태양광 |
| C | 분류 = 관계 모델 | taxonomy가 세계를 어떻게 쪼개는가 | WWA People/Glossary, Takachizu 장소 |
| D | 플랫폼 = 세계관 | CMS·스택이 어떤 배열을 강제하는가 | Omeka Item/Collection/Exhibit |
| E | 접근·발견 | 누가 어떻게 찾아오는가 | UbuWeb noindex, 서태지 403 |
| F | 수집 단위 | 최소 엔티티가 무엇인가 | 글(WWA), 종(BugGuide), 계단(PublicStairs) |
| G | 운영·커뮤니티 | 과정이 구조에 남는가 | WWA forum, Takachizu 커뮤니티 |
| H | 시간층 | 시간이 어떻게 층위화되는가 | UK Web Archive, OASIS |
| I | 부재가 형식 | 없는 것이 구조를 만드는가 | UbuWeb: 설명·검색·진본성 부재 |

실제 비평 문체는 스키마 필드를 나열하기보다 **「보통 아카이브가 하는 것 vs 이 사이트가 하는 것」** 대비 문법을 쓴다.

---

## 4. 다차원 매핑 (8축)

단일 카테고리 표 대신, 여러 축에 동시에 찍는 방식이 「분류라는 예정된 실패」의 *다시 쓰는 분류*와 맞다.

| # | 축 | 값 예시 |
|---|-----|---------|
| 1 | 운영 주체 | `institution` / `community` / `individual` / `corporate` / `hybrid` |
| 2 | 수집 단위 | `item` / `text` / `event` / `place` / `aggregate` |
| 3 | 탐색 구조 | `taxonomy` / `search` / `chronology` / `spatial` / `associative` / `none` |
| 4 | 형식 실험도 | `high` / `medium` / `low` |
| 5 | 아카이브 자기인식 | `explicit` / `implicit` / `denied` |
| 6 | 접근 체제 | `open` / `gated` / `hidden` / `defunct` |
| 7 | 기술 스택 | `Omeka` / `custom` / `wiki` / `LibGuides` / `web-crawler` / `unknown` |
| 8 | 지리·언어 | `KR` / `EN` / `multi` / `JP` … |

### 샘플 매핑

| 아카이브 | 주체 | 단위 | 탐색 | 형식 | 스택 | 비평 hook |
|----------|------|------|------|------|------|-----------|
| 퀴어락 | community | item | taxonomy | low | Omeka | 분리된 아카이브 |
| UK Web Archive | government | snapshot | chronology+search | low | crawler | 웹 시간 지층 |
| Takachizu | community | place | spatial | medium | custom | 장소=분류 |
| Low-Tech | individual | article | chronology | high | solar | 형식=지속가능성 |
| Japan Search | government | aggregate | federated | low | portal | 국가 통합 검색 |
| Monoskop | community | text+link | wiki graph | medium | MediaWiki | 위키형 아카이브 |
| Godly | corporate? | screenshot | browse | medium | — | **경계 사례** |

---

## 5. 「분류라는 예정된 실패」와의 관계

수집 단계에서 이미 다음이 재현된다.

- **퀴어락**: 퀴어 아카이브 / 시민단체 기록 / Omeka 사례 — 한 칸에 넣으면 나머지가 사라진다.
- **Godly / Discogs**: 아카이브인가 DB·마켓·레퍼런스인가.
- **건축의 아카이브 해제**: 아카이브인가 심포지엄 사이트인가.

→ 비평 전에 **「이 프로젝트가 무엇을 아카이브로 볼 것인가」** — [archive-boundary-criteria.md](archive-boundary-criteria.md) §8 선언문 참조.

### 파일럿 YAML (2026-06-22)

`data/archives/` — 8축 + schema v1.0 통합 관찰 파일:

| slug | axes 요약 | critique |
|------|-----------|----------|
| `ubuweb` | individual · item · associative · high · hidden | published |
| `women-writing-architecture` | hybrid · text · taxonomy+search · medium | published |
| `korea-queer-archive` | hybrid · item · taxonomy · Omeka | in_progress |
| `low-tech-magazine` | individual · text · chronology · high | planned |
| `oasis` | institution · aggregate · search+chronology | planned |
| `uk-government-web-archive` | institution · aggregate · web-crawler | planned |
| `takachizu` | community · place · spatial | planned |
| `japan-search` | institution · aggregate · search | planned |

---

## 6. 다음 작업 (합의된 순서)

- [x] **1.** Are.na 125개 → `meta-archives.md` 동기화 + `data/arena/meta-archive.json`
- [x] **2.** 8축 태그 `data/archives/` YAML 파일럿 (8개 — 아래 목록)
- [x] **3.** 경계 사례 「아카이브인가?」 판별 초안 → [archive-boundary-criteria.md](archive-boundary-criteria.md)
- [ ] **4.** 다음 비평 후보: 퀴어락 / OASIS·UK / Low-Tech
- [x] **탐색** — [inventory-views.md](inventory-views.md) · [observe.html](../../observe.html)

### 비평 우선순위 제안

| 순위 | 대상 | 이유 |
|------|------|------|
| 1 | 퀴어락 | Omeka 초안 있음, 진행 중 |
| 2 | OASIS 또는 UK Web Archive | 시간층(H) + 정부(E) 축 |
| 3 | Low-Tech Magazine | UbuWeb(B)과 형식 대비 |

---

## 7. 그룹별 등재 수 (동기화본)

| 그룹 | 수 |
|------|-----|
| 기관 아카이브 | 25 |
| 형식이 곧 내용인 아카이브 | 17 |
| 분류 체계가 독특한 아카이브 | 15 |
| 페미니스트·사회운동·대안 아카이브 | 13 |
| 개인 아카이브·포트폴리오 | 9 |
| 대규모 통합 플랫폼 | 8 |
| 예술가 출판·독립 플랫폼 | 8 |
| 한국 공공·지역·역사 아카이브 | 7 |
| 정부·공공 웹 아카이브 | 7 |
| 디자인·시각 아카이브 | 6 |
| 웹 역사·디지털 유산 | 4 |
| 디자인 영감·레퍼런스 (경계) | 3 |
| 접근 불가·미확인 | 2 |
| 잡지·미디어 아카이브 | 1 |
| **합계** | **125** |

---

*작성: 2026-06-22*
