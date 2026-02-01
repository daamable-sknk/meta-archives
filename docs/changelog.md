# Changelog

meta-archives.xyz 프로젝트의 작업 내역을 기록합니다.

---

## 2026-02-01

### WWA 비평글 줄글 스타일로 수정 및 plan.md 보완
`7fcda8b`

**비평글 스타일 변경**
- WWA 비평글을 줄글 형식으로 전면 수정
- 섹션 제목(h2) 제거, 자연스러운 문단 흐름으로 변경
- `<hr>` 구분선으로 문단 분리
- 관찰 메모 1개 추가 (glossary 관련)
- `content/posts/women-writing-architecture.md` 및 `posts/women-writing-architecture/index.html` 동기화

**비평 계획 보완**
- `docs/plan.md` — 아카이브 특징 테이블 형식으로 정리

---

### 비평 계획 추가 및 에세이 글 수정
`8f2738b`

**새 문서**
- `docs/plan.md` 신규 작성 — 36개 아카이브 비평 우선순위
- 월 2회 발행 일정 수립
- 우선순위 기준: 형식이 곧 내용인 아카이브 우선

**에세이 수정**
- "해석에 반대한다" 에세이 표현 개선

---

### About 페이지 간결화 및 메타데이터 스키마 통일
`c9e5773`

**About 페이지**
- "미션", "비전" 섹션 제거
- 에세이 톤으로 재작성 (해석에 반대한다 에세이 기반)
- 메타데이터 스키마 단일 섹션으로 통합

**스키마 통일**
- About의 스키마와 실제 비평글(WWA) 메타데이터 일치
- 필드: url, status, year_started, observed, operator, type, language, access

---

### 푸터 개선
`7cb5f5b`

- 크레딧 문구 추가: "이 프로젝트는 Archive Mate ↬에서 시작되었습니다."
- 링크 분리 (점 구분자 제거)
- 외부 링크에 ↬ 화살표 추가
- Last updated 날짜 추가

---

### Pure Index 디자인으로 전면 개편
`b7162d4`

**디자인 철학**
- 브루탈리즘/인덱스 스타일 채택
- "아카이브를 비평하는 아카이브"의 성격을 형식으로 체화

**스타일 변경**
- 시스템 폰트만 사용
- 모노크롬 팔레트 (#fff, #111, #666)
- 카드, 그림자, 장식 요소 제거
- 모든 페이지 구조 간소화

**문서화**
- `docs/design.md` 신규 작성 — 디자인 명세

---

### 작업 내역 문서화
`11fcf4d`

- `docs/changelog.md` 신규 작성
- `docs/guide.md` 업데이트

---

### 새 에세이 글 추가 및 카테고리 필터 구현
`88634ef`

**새 콘텐츠**
- 새 에세이: "해석에 반대한다, 아카이브에 대해서도"
  - 수잔 손택의 「해석에 반대한다」를 아카이브 비평에 적용
  - 아카이브를 내용이 아닌 형식으로 읽어야 한다는 주장
  - 아카이브가 "나를 표현하는 방식"이 되었다는 관점
  - 파일: `content/posts/against-interpretation-for-archives.md`
  - 메타데이터: `data/posts/against-interpretation-for-archives.yml`
  - HTML: `posts/against-interpretation-for-archives/index.html`

**기능 추가**
- index.html에 카테고리 필터 메뉴 추가 (전체 | 비평 | 에세이)
- JavaScript 기반 필터링 구현
- 각 글에 `data-category` 속성 부여 (critique / essay)

**스타일**
- `assets/css/style.css`에 `.category-filter` 스타일 추가

**문서**
- `docs/concept.md` 업데이트 — 아카이브 철학에 대한 상세 설명 추가

---

## 2026-01-31

### 블로그 워크플로우를 위한 사이트 구조 재구성
`59bd03a`

**구조 변경**
기존 구조에서 블로그 워크플로우에 맞게 전면 재구성:

```
meta-archives/
├── index.html                    # 메인 페이지
├── about.html                    # About 페이지
├── assets/
│   ├── css/style.css            # 공용 스타일시트 (인라인에서 분리)
│   ├── favicon.ico              # 파비콘
│   └── images/                  # OG 이미지용
├── posts/                        # 개별 글 HTML
│   └── <slug>/index.html
├── content/posts/               # 비평 글 원본 (Markdown)
├── data/posts/                  # 메타데이터 (YAML)
├── data/site.yml                # 사이트 전역 설정
└── docs/                        # 프로젝트 문서
    ├── concept.md
    ├── guide.md
    ├── schema.md
    └── changelog.md             # 이 파일
```

**카테고리 체계 도입**
- **critiques**: 아카이브 비평글 (예: Women Writing Architecture)
- **essays**: 비평 방법론, 관점에 대한 글 (예: 해석에 반대한다...)

**워크플로우 문서화**
- `docs/guide.md` 신규 작성 — 역할 분담, 새 글 작성 워크플로우
- `docs/schema.md` 신규 작성 — 메타데이터 스키마 정의

---

## 2026-01-30

### Women Writing Architecture 비평문 대폭 보강
`595867d`, `5cbe353`, `61fcf66`

**비평 내용 확장**
- "Structure as Relation" 섹션 추가
- 전체 비평문 HTML에 반영
- 구조적 분석 심화

---

## 2026-01-29

### 메타 태그 및 About 페이지 추가
`7aae17c`, `9024322`

**SEO 개선**
- Open Graph 메타 태그 추가
- Twitter Card 메타 태그 추가

**페이지 추가**
- `about.html` 페이지 신규 작성
- 헤더에 About 링크 추가

---

## 2026-01-28

### 파비콘 추가
`6a01d3f`

- favicon.io에서 생성한 파비콘 추가
- `assets/favicon.ico`

---

## 2026-01-27

### 사이트 구조 개편 및 커스텀 도메인 설정
`7c2ac96`

**도메인**
- meta-archives.xyz 커스텀 도메인 설정
- CNAME 파일 추가

**구조**
- 정적 사이트 기본 구조 확립
- GitHub Pages 배포 설정

---

## 2026-01-26

### Women Writing Architecture 상세 페이지 추가
`c831960`

- 첫 번째 아카이브 비평 상세 페이지 HTML 작성
- `posts/women-writing-architecture/index.html`

---

## 2026-01-25

### 첫 번째 아카이브 비평 추가
`3993a8c`

**Women Writing Architecture**
- 첫 번째 비평 대상 아카이브 선정
- 메타데이터 작성: `data/posts/women-writing-architecture.yml`
- 비평 글 작성: `content/posts/women-writing-architecture.md`

---

## 2026-01-24

### 프로젝트 시작
`2d816a3`

- Initial commit
- 프로젝트 초기 설정

---

## 컨벤션

### 커밋 메시지
- 언어: 한국어
- 형식: Conventional Commits
  - `feat:` — 새 기능
  - `refactor:` — 구조 변경
  - `docs:` — 문서
  - `fix:` — 버그 수정
  - `style:` — 스타일/포맷팅

### 문서 작성
- 작업 완료 후 이 changelog에 기록
- 날짜는 역순 (최신이 위)

### 커밋 타이밍
- 사용자가 직접 요청할 때만 커밋
- 푸시는 별도 요청 시에만

---

## 향후 계획

- [ ] RSS 피드 추가
- [ ] 메타데이터 기반 비교 뷰
- [ ] 상태 변화 히스토리 시각화
- [ ] CSV/JSON export
- [ ] GitHub Actions CI/CD (YAML + MD → HTML 자동 빌드)
