# 작업 가이드

meta-archives.xyz 프로젝트의 작업 방식과 워크플로우를 정의합니다.

---

## 역할 분담

### 작성자 (콘텐츠 담당)
- 아카이브 선정 및 관찰
- 메타데이터 작성 (`data/posts/*.yml`)
- 비평 글 작성 (`content/posts/*.md`)
- 스키마 준수 확인

### OpenCode (구현 담당)
- 웹사이트 구조 설계 및 구현
- 콘텐츠 → HTML 변환
- 스타일 및 레이아웃 관리
- 배포 자동화

---

## 디렉토리 구조

```
meta-archives/
├── index.html                    # 메인 페이지 (글 목록 + 카테고리 필터)
├── about.html                    # About 페이지
├── CNAME
├── README.md
│
├── assets/                       # 정적 자산
│   ├── css/style.css            # 공통 스타일
│   ├── favicon.ico              # 파비콘
│   └── images/                  # OG 이미지 등
│
├── posts/                        # 개별 글 HTML
│   ├── women-writing-architecture/index.html      # 비평
│   └── against-interpretation-for-archives/index.html  # 에세이
│
├── content/                      # 원본 콘텐츠
│   └── posts/*.md               # 비평/에세이 글 (Markdown)
│
├── data/                         # 구조화된 데이터
│   ├── posts/*.yml              # 글별 메타데이터
│   └── site.yml                 # 사이트 전역 설정
│
└── docs/                         # 프로젝트 문서
    ├── concept.md               # 컨셉 & 철학
    ├── guide.md                 # 작업 가이드 (이 파일)
    ├── schema.md                # 메타데이터 스키마
    └── changelog.md             # 작업 내역
```

---

## 카테고리 체계

### 비평 (critique)
- 특정 아카이브를 대상으로 한 비평글
- 아카이브의 구조, 메타데이터, 분류 체계 분석
- 예: Women Writing Architecture

### 에세이 (essay)
- 비평 방법론, 관점에 대한 글
- 아카이브 일반에 대한 사색적 글
- 예: 해석에 반대한다, 아카이브에 대해서도

---

## 새 글 작성 워크플로우

### 1. 아카이브 선정
- 관심 있는 디지털 아카이브 발견
- 선정 이유 간략히 메모

### 2. 메타데이터 작성
파일: `data/posts/<slug>.yml`

```yaml
slug: "archive-name"
title: "Archive Name"
url: "https://..."
description: "한두 문장 설명"
# ... (schema.md 참조)
```

### 3. 비평 글 작성
파일: `content/posts/<slug>.md`

권장 구조:
```markdown
# 1차 기술
(아카이브가 스스로를 어떻게 설명하는지)

## 섹션 제목
(분석 내용)

## 관찰 메모
- YYYY-MM-DD: 메모 내용
```

### 4. HTML 생성 요청
OpenCode에게 빌드 요청

### 5. 검토 및 커밋
- 결과물 확인
- 커밋 & 푸시

---

## 비평 글 작성 가이드

### 필수 요소
1. **1차 기술**: 아카이브가 스스로를 어떻게 설명하는지
   - 공식 소개문, About 페이지 인용
   - 출처 명시

2. **구조 분석**: 아카이브의 형식적 특징
   - 메타데이터 구조
   - 분류 체계
   - 탐색 방식

3. **비평**: 왜 이 아카이브가 흥미로운가
   - 무엇을 기억하고 무엇을 배제하는가
   - 기술적 선택의 함의
   - 한계, 모순, 특이점

4. **관찰 메모**: 날짜별 기록
   - 발견한 사실
   - 의문점
   - 후속 조사 필요 사항

### 권장 사항
- 원문 인용 시 출처 URL 명시
- 추측과 관찰을 구분
- 관찰 시점 명시 (아카이브는 변한다)

---

## 빌드 및 배포

### 현재 방식
- 수동 HTML 생성
- GitHub Pages 배포
- 커스텀 도메인: meta-archives.xyz

### 향후 자동화 (예정)
- GitHub Actions CI/CD
- YAML + MD → HTML 자동 빌드
- 커밋 시 자동 배포

---

## 설계 원칙

1. **단순함 유지**: 정적 사이트, 최소한의 의존성
2. **콘텐츠 중심**: 글이 먼저, 구현은 나중
3. **Git 히스토리 활용**: 변경 이력 = 관찰의 역사
4. **투명성**: 모든 소스 공개
5. **점진적 확장**: 필요할 때 기능 추가

---

## 장기 확장 (현재는 구현하지 않음)

- [ ] 메타데이터 기반 비교 뷰
- [ ] 상태 변화 히스토리 시각화
- [ ] 스키마 버전 관리
- [ ] CSV/JSON export
- [ ] 연구용 데이터셋 공개
- [ ] RSS 피드
- [ ] GitHub Actions CI/CD (YAML + MD → HTML 자동 빌드)

---

## 관련 문서

- [컨셉 문서](concept.md) — 프로젝트 철학과 방향
- [메타데이터 스키마](schema.md) — YAML 필드 정의
- [작업 내역](changelog.md) — 변경 이력
