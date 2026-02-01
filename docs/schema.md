# 메타데이터 스키마

meta-archives.xyz에서 각 아카이브를 기술할 때 사용하는 메타데이터 구조입니다.  
이 스키마 자체가 "무엇이 아카이브를 구성하는가"에 대한 우리의 가설입니다.

---

## 스키마 버전

- **현재 버전**: v1.0
- **최종 수정**: 2026-01-04

---

## 필드 구조

### 1. 기본 정보 (Basic)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `slug` | string | O | URL에 사용될 고유 식별자 (파일명과 동일) |
| `title` | string | O | 아카이브 공식 명칭 |
| `title_alt` | string | - | 대체 명칭 또는 약어 |
| `url` | string | O | 아카이브 메인 URL |
| `description` | string | O | 1~2문장 요약 설명 |

### 2. 시간 정보 (Temporal)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `year_started` | integer | - | 아카이브 시작 연도 |
| `year_started_note` | string | - | 시작 연도에 대한 부가 설명 |
| `year_ended` | integer | - | 종료 연도 (운영 중이면 null) |

### 3. 운영 주체 (Operator)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `operator.name` | string | O | 운영 기관/단체명 |
| `operator.type` | enum | O | institution / organization / individual / government / unknown |
| `operator.country` | string | - | ISO 3166-1 alpha-2 코드 (예: KR, US) |

### 4. 분류 (Classification)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `tags` | array | - | 자유 태그 |
| `category` | enum | O | cultural / scientific / governmental / personal / commercial / experimental |
| `language` | array | - | 주 사용 언어 (ISO 639-1) |
| `coverage` | string | - | 지리적/주제적 범위 |

### 5. 기술적 특성 (Technical)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `tech.platform` | string | - | 사용 플랫폼/CMS |
| `tech.metadata_standard` | string | - | 메타데이터 표준 (Dublin Core, METS, custom 등) |
| `tech.api_available` | boolean | - | API 제공 여부 |
| `tech.bulk_download` | boolean | - | 대량 다운로드 가능 여부 |
| `tech.navigation` | string | - | 탐색 방식 설명 |

### 6. 접근성 (Access)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `access.registration_required` | boolean | - | 회원가입 필요 여부 |
| `access.paywall` | boolean/string | - | true / false / partial |
| `access.license` | string | - | 콘텐츠 라이선스 |

### 7. 관찰 기록 (Observation)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `observation.observed_at` | date | O | 관찰 날짜 (YYYY-MM-DD) |
| `observation.status` | enum | O | active / inactive / partial / defunct / unknown |
| `observation.http_code` | integer | - | HTTP 응답 코드 |
| `observation.notes` | string | - | 관찰 시 특이사항 |

### 8. 사회적 맥락 (Context)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `context.social_aspect` | string | - | 사회적 성격/배경 |
| `context.source` | string | - | 주요 자료 출처 |
| `context.hidden_source` | string | - | 암묵적/추정 출처 |

### 9. 메타 정보 (Meta)

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `meta.created_at` | date | O | 파일 최초 작성일 |
| `meta.updated_at` | date | O | 파일 최종 수정일 |
| `meta.author` | string | - | 작성자 |
| `meta.note` | string | - | 선정 이유 등 부가 메모 |

---

## 값 규칙

### status 값
- `active`: 정상 운영 중
- `inactive`: 업데이트 중단, 접근은 가능
- `partial`: 일부만 접근 가능
- `defunct`: 폐쇄/접근 불가
- `unknown`: 상태 불명

### category 값
- `cultural`: 문화, 예술, 인문
- `scientific`: 과학, 학술, 연구
- `governmental`: 정부, 공공기관
- `personal`: 개인 프로젝트
- `commercial`: 상업적 목적
- `experimental`: 실험적 프로젝트

### null 처리
- 정보가 없거나 확인 불가한 경우 `null` 사용
- 빈 문자열 `""` 대신 `null` 권장

---

## 예시

```yaml
slug: "women-writing-architecture"
title: "Women Writing Architecture"
url: "https://womenwritingarchitecture.org/"
description: "An open, annotated bibliography collecting texts written by women about architecture."

year_started: 2021
year_ended: null

operator:
  name: "Women Writing Architecture editorial collective"
  type: "organization"
  country: null

tags: [women, architecture, writing, feminist archive, bibliography]
category: "cultural"
language: [en]

observation:
  observed_at: "2026-01-04"
  status: "active"
  http_code: 200

meta:
  created_at: "2026-01-04"
  updated_at: "2026-01-04"
```
