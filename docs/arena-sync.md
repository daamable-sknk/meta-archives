# Are.na 연동 구조

비평 대상 아카이브 목록은 [Are.na meta-archive](https://www.are.na/daehwan-jang/meta-archive) 채널에서 수집한다. 새로운 아카이브를 발견하면 Are.na에 먼저 추가하고, 비정기적으로 이 채널의 내용을 `meta-archives.md` 비평 계획에 동기화한다.

---

## 채널 정보

| 항목 | 값 |
|------|-----|
| 채널 | [meta-archive](https://www.are.na/daehwan-jang/meta-archive) |
| slug | `meta-archive` |
| 소유자 | Daehwan Jang |
| 공개 | ✓ (인증 없이 읽기 가능) |

---

## API 엔드포인트

Are.na는 공개 채널에 대해 인증 없이 읽기 접근을 허용한다.

### 채널 조회 (블록 포함)

```
GET https://api.are.na/v2/channels/meta-archive
```

**페이지네이션 파라미터:**

| 파라미터 | 설명 | 기본값 |
|----------|------|--------|
| `page` | 페이지 번호 (1부터) | 1 |
| `per` | 페이지당 블록 수 | 20 |

예시:

```
https://api.are.na/v2/channels/meta-archive?page=1&per=50
```

`per=100`으로 설정하고 `page=1`, `page=2` … 를 순회한다. 2026-06-22 기준 채널 길이는 **125블록**(Link 110 / Image 8 / Text 7)이다.

동기화 결과물:

| 파일 | 설명 |
|------|------|
| [plans/meta-archives.md](plans/meta-archives.md) | 비평 계획·그룹별 전체 목록 |
| [data/arena/meta-archive.json](../data/arena/meta-archive.json) | API 원본 기반 머신-readable 인벤토리 |
| [data/archives/](../data/archives/) | 아카이브별 관찰 YAML (8축 파일럿) |
| [data/arena/overrides](../data/arena/) | — |
| [scripts/arena_overrides.py](../scripts/arena_overrides.py) | Are.na 오수집 수동 보정 |
| [scripts/sync-arena.py](../scripts/sync-arena.py) | API → meta-archive.json |
| [inventory-enriched.json](../data/arena/inventory-enriched.json) | 8축 추론·패싯 집계 (build-inventory.py) |
| [id-registry.json](../data/arena/id-registry.json) | 영구 inventory ID (`MA-###`) ↔ Are.na 블록 |

### 응답 구조 (주요 필드)

```json
{
  "title": "meta-archive",
  "length": 43,
  "updated_at": "2026-02-20T12:32:50.114Z",
  "contents": [
    {
      "title": "the moving poster – We like to move it!",
      "class": "Link",
      "description": "...",
      "source": {
        "url": "https://themovingposter.com/",
        "title": "the moving poster – We like to move it!",
        "provider": {
          "name": "themovingposter.com",
          "url": "themovingposter.com"
        }
      },
      "connected_at": "2025-08-20T11:16:07.550Z",
      "id": 38907376
    }
  ]
}
```

### 블록별 핵심 필드

| 필드 | 설명 | 활용 |
|------|------|------|
| `title` | 블록 제목 (보통 사이트 타이틀) | 아카이브 이름 |
| `class` | 블록 유형 (`Link`, `Text`, `Image` 등) | `Link`만 필터링 |
| `source.url` | 원본 URL | 아카이브 주소 |
| `source.provider.name` | 도메인명 | 테이블의 URL 컬럼 |
| `description` | 사용자가 추가한 메모 | 특징 참고 |
| `connected_at` | 채널에 추가된 시점 | 신규 항목 판별 |
| `id` | 블록 고유 ID | 중복 확인 |

---

## 동기화 흐름

```
Are.na 채널에 아카이브 추가
        ↓
bash scripts/sync.sh              # API fetch → diff → meta-archive.json
        ↓
diff 리포트 검토 (신규·API drift·의심 제목)
        ↓
필요 시 scripts/arena_overrides.py · category 수동 수정
        ↓
inventory-enriched.json 빌드 (sync에 포함, --no-build로 생략 가능)
        ↓
observe.html 에서 확인
```

### 반자동 원칙

| 단계 | 자동 | 수동 |
|------|------|------|
| API fetch | ✓ | |
| 신규 MA-ID 부여 | ✓ (`build-inventory.py`) | |
| 기존 title/url/short/category | | 로컬 유지 |
| 연결일·블록 유형 갱신 | ✓ | |
| 봇 차단 오수집 보정 | | `arena_overrides.py` |
| 1차 그룹 배치 (신규) | | `미분류·검토 필요` → 수정 |
| YAML | | 비평 시작 시만 |

### 실행

```bash
# fetch + diff + 저장 + inventory 빌드 (일반)
bash scripts/sync.sh

# diff만 (파일 미저장)
bash scripts/sync.sh --dry-run

# JSON만, 빌드 생략
bash scripts/sync.sh --no-build
```

로컬 미리보기:

```bash
bash scripts/serve.sh    # inventory 빌드 + http://localhost:8765/observe.html
```

### 신규 항목 판별

1. API 응답의 `contents` 배열에서 **모든 블록**을 검사 (`Link`뿐 아니라 `Image`, `Text` 포함)
2. URL 추출: `Link`/`Text`는 `source.url` 또는 `content_html`의 `href`; `Image`는 외부 도메인 `source.url`
3. 각 URL을 기존 `meta-archives.md` 또는 `data/arena/meta-archive.json`과 대조
4. 기존 목록에 없는 URL이 신규 항목

### 그룹 배치

신규 항목은 아카이브의 성격에 따라 10개 그룹 중 하나에 배치한다:

- 형식이 곧 내용인 아카이브
- 분류 체계가 독특한 아카이브
- 대규모 통합 플랫폼
- 기관 아카이브
- 정부·공공 웹 아카이브
- 개인 아카이브·포트폴리오
- 예술가 출판·독립 플랫폼
- 디자인 아카이브
- 대안·실험적 아카이브
- 접근 불가·미확인

어느 그룹에도 명확히 속하지 않는 경우, 가장 가까운 그룹에 배치하거나 새 그룹을 만든다.

---

## 실행 방법

### 방법 1: 브라우저에서 직접 확인

```
https://api.are.na/v2/channels/meta-archive?per=100
```

브라우저에서 위 URL을 열면 JSON 응답을 바로 확인할 수 있다.

### 방법 2: curl

```bash
curl -s "https://api.are.na/v2/channels/meta-archive?per=100" | python3 -m json.tool
```

### 방법 3: 링크 블록만 추출

```bash
curl -s "https://api.are.na/v2/channels/meta-archive?per=100" \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)
for block in data['contents']:
    if block.get('class') == 'Link' and block.get('source'):
        url = block['source'].get('url', '')
        title = block.get('title', '(no title)')
        print(f'{title}\t{url}')
"
```

이 명령은 채널의 모든 Link 블록을 `제목\tURL` 형식으로 출력한다. 출력 결과를 `meta-archives.md`의 기존 목록과 비교하면 신규 항목을 빠르게 찾을 수 있다.

---

## 참고

- Are.na API 문서: [dev.are.na/documentation](https://dev.are.na/documentation)
- 공개 채널은 인증 없이 읽기 가능. 쓰기/비공개 채널 접근 시 Personal Access Token 필요
- Rate limit: 명시적 제한은 없으나 과도한 호출은 자제
- 채널의 `length` 필드로 총 블록 수를 먼저 확인하면 필요한 페이지 수를 계산할 수 있다

---

*Last updated: 2026-06-22*
