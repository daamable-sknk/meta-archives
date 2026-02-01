# 디자인 명세

meta-archives.xyz의 시각적 디자인 원칙과 스타일 가이드.

---

## 컨셉

**순수 인덱스 (Pure Index)**

책 뒤의 색인(index)이나 서지 목록(bibliography)처럼 텍스트만으로 구성된 최소한의 디자인. 아카이브를 비평하는 사이트답게, 장식을 배제하고 정보의 구조만 드러낸다.

### 핵심 원칙

1. **텍스트가 전부** — 이미지, 아이콘, 장식 요소 없음
2. **장식 배제** — 박스, 카드, 그림자 없음. 구분선만 사용
3. **계층은 들여쓰기로** — 메타데이터는 제목 아래 들여쓰기
4. **호버는 밑줄만** — 색상 변화 없이 밑줄 추가
5. **여백으로 호흡** — 넉넉한 행간과 여백

### 레퍼런스

- [gwern.net](https://gwern.net) — 학술 서지 목록 스타일
- [solar.lowtechmagazine.com](https://solar.lowtechmagazine.com) — 브루탈리즘 웹
- 실제 책의 색인/참고문헌 페이지

---

## 컬러 팔레트

```
--bg:       #fff        배경 (순백)
--text:     #111        본문 텍스트 (거의 검정)
--muted:    #666        보조 텍스트 (날짜, 메타데이터)
--border:   #111        구분선 (본문과 동일)
--hover-bg: #f5f5f5     호버 시 배경 (선택적)
```

무채색만 사용. 강조색 없음.

---

## 타이포그래피

### 폰트

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, 
             "Helvetica Neue", Arial, sans-serif;
```

시스템 폰트 사용. 외부 폰트 로드 없음.

### 크기

| 요소 | 크기 | 비고 |
|------|------|------|
| 사이트 제목 | 1rem | 본문과 동일, bold |
| 글 제목 | 1rem | 본문과 동일 |
| 본문 | 1rem (16px) | 기준 |
| 메타데이터 | 0.875rem | 약간 작게, muted 색상 |
| 날짜 | 0.875rem | 우측 정렬 또는 리더 닷 연결 |

### 행간

```css
line-height: 1.6;  /* 본문 */
line-height: 1.4;  /* 제목 */
```

---

## 레이아웃

### 기본 구조

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  meta-archives.xyz                              │
│  아카이브를 비평하는 아카이브                    │
│                                                 │
│  ───────────────────────────────────────────    │
│                                                 │
│  [전체]  비평  에세이                            │
│                                                 │
│  ───────────────────────────────────────────    │
│                                                 │
│  해석에 반대한다, 아카이브에 대해서도     2026.02 │
│      에세이                                      │
│                                                 │
│  Women Writing Architecture              2026.01 │
│      비평 · Active                               │
│                                                 │
│  ───────────────────────────────────────────    │
│                                                 │
│  About · GitHub                                 │
│                                                 │
└─────────────────────────────────────────────────┘
```

### 너비

```css
max-width: 640px;  /* 좁은 단일 컬럼 */
margin: 0 auto;
padding: 2rem 1.5rem;
```

### 글 목록 항목

```
제목                                        날짜
    카테고리 · 태그 · 상태
```

- 제목과 날짜는 같은 줄, 양 끝 정렬
- 메타데이터는 들여쓰기 (padding-left)
- 항목 간 여백으로 구분 (border 없음)

---

## 컴포넌트

### 헤더

```html
<header>
  <h1>meta-archives.xyz</h1>
  <p>아카이브를 비평하는 아카이브</p>
</header>
```

- 중앙 정렬 또는 좌측 정렬
- 구분선으로 본문과 분리

### 카테고리 필터

```html
<nav class="filter">
  <a href="#" class="active">전체</a>
  <a href="#">비평</a>
  <a href="#">에세이</a>
</nav>
```

- 텍스트 링크, 공백으로 구분
- 활성 상태: bold 또는 밑줄
- 숫자 표시 선택적: `전체 (3)`

### 글 목록

```html
<ul class="index">
  <li>
    <a href="...">
      <span class="title">글 제목</span>
      <span class="date">2026.02</span>
    </a>
    <div class="meta">에세이</div>
  </li>
</ul>
```

### 링크 스타일

```css
a {
  color: var(--text);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
```

색상 변화 없음. 호버 시 밑줄만.

### 구분선

```css
hr, .divider {
  border: none;
  border-top: 1px solid var(--text);
  margin: 2rem 0;
}
```

얇은 검은 선. 점선 아님.

---

## 상세 페이지

### 구조

```
meta-archives.xyz                    ← 홈 링크

───────────────────────────────────

글 제목
    카테고리 · 날짜 · 상태

───────────────────────────────────

본문 내용...

## 섹션 제목

본문...

───────────────────────────────────

About · GitHub
```

### 메타데이터 박스

상세 페이지에서는 구조화된 메타데이터를 코드 블록 또는 정의 목록으로 표시:

```
title:    Women Writing Architecture
url:      https://womenwritingarchitecture.org/
status:   Active
observed: 2026-01-04
```

---

## 반응형

### 브레이크포인트

- 모바일: ~480px
- 태블릿: 481px~768px  
- 데스크탑: 769px~

### 모바일 조정

```css
@media (max-width: 480px) {
  body {
    padding: 1.5rem 1rem;
  }
  
  /* 제목-날짜 세로 배치 */
  .index li a {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .date {
    margin-top: 0.25rem;
  }
}
```

---

## 하지 않는 것

- 카드 UI
- 그림자 (box-shadow)
- 둥근 모서리 (border-radius)
- 그라데이션
- 아이콘
- 이미지
- 애니메이션/트랜지션 (호버 밑줄 제외)
- 외부 폰트 로드
- 컬러 강조

---

## 참고: 스큐어모피즘으로서의 인덱스

이 디자인은 **책의 색인 페이지**를 스큐어모픽하게 웹으로 옮긴 것이다.

- 리더 닷(leader dots)은 선택적으로 사용 가능
- 알파벳순/날짜순 정렬
- 페이지 번호 대신 날짜
- 들여쓰기로 계층 표현

web-archivists.xyz가 "종이 팜플렛"이라면,  
meta-archives.xyz는 "책 뒤의 색인"이다.

---

Last updated: 2026.02.01
