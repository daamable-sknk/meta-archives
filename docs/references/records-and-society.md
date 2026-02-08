# 웹 이후의 기록학 — 연구자료 & 레퍼런스

본 문서는 연재 **〈웹 이후의 기록학〉**을 집필하기 위해 참고할 연구 자료, 원문 텍스트, 웹 아카이브 링크를 회차별로 정리한 레퍼런스 문서입니다.

---

## 1회차. 웹은 처음부터 아카이브였다

### Tim Berners-Lee 초기 문서

**Information Management: A Proposal** (1989)

- [초기 제안서 (W3C)](https://www.w3.org/History/1989/proposal.html)
- [World Wide Web 역사](https://www.w3.org/History.html)
- [Wikipedia: World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web)

### 기록학 타임라인 자료

**웹 동시기 기록학계 (1989-1993)**

- Terry Cook (1991-1992) "Easy to byte, harder to chew: the second generation of electronic records archives" - *Archivaria* 33
- Rules for Archival Description (RAD) - 캐나다, 1990
- ISAD(G) 초안 - ICA, 1993
- EAD (Encoded Archival Description) 프로젝트 개시 - UC Berkeley, 1992-1993

**웹 아카이빙과 RiC**

- Internet Archive 설립 - 1996
- IIPC (International Internet Preservation Consortium) - 2003
- [Records in Contexts (RiC) - ICA](https://www.ica.org/en/records-in-contexts-conceptual-model) - 2013-2023
- ISAD(G)2 - ICA, 2000

### 핵심 비교 포인트

**Berners-Lee 1989 구조:**
- "circles and arrows" (제안서 다이어그램)
- 타입화된 관계: depends on, is part of, made, refers to, uses, is example of
- 양방향 링크 (ENQUIRE, 1980)
- 비계층적 네트워크

**ISAD(G) 1994 구조:**
- Fonds → Subfonds → Series → Files → Items
- 부모-자식 관계 (parent-child)
- 단일 출처 (single provenance)
- 계층적 다단계 기술 (multilevel description)

**RiC 2023 구조:**
- Entities와 Relations의 그래프
- Record, Agent, Activity, Rule, Place, Date
- 복잡한 관계 타입 (created by, used by, subject of, related to)
- 비계층적, 웹에서 영감받은 모델

### 학술 논문 (2026-02-08 추가)

**웹 아카이브와 기록학의 간극을 다룬 최신 연구**

1. **Maemura, E. (2025).** "Conceptualizing aggregate-level description in web archives." *Archival Science*, 25.
   - DOI: https://doi.org/10.1007/s10502-025-09475-z
   - 핵심: 웹 아카이브는 집합 수준(aggregate-level)에서 기술되어야 함
   - 전통 기록학의 개별 객체 중심 기술로는 웹 구조 포착 불가
   - RiC = 집합 수준 기술 모델

2. **Hegarty, K. (2022).** "The invention of the archived web: tracing the influence of library frameworks on web archiving infrastructure." *Internet Histories*, 6, 432-451.
   - DOI: https://doi.org/10.1080/24701475.2022.2103988
   - 핵심: 웹 아카이빙이 도서관 프레임워크를 이식
   - Internet Archive가 서지 중심, 출판물 메타데이터 사용
   - 웹을 "출판물"로 다루며 네트워크 본질 놓침

3. **Fomasi, M., Barcella, D., Benecchi, E., & Balbi, G. (2023).** "Genealogy of an archive. The birth, construction, and development of the World Wide Web collection at CERN." *Internet Histories*, 7, 277-294.
   - DOI: https://doi.org/10.1080/24701475.2023.2238254
   - 핵심: CERN WWW 컬렉션조차 "부분적·우연적 수집"
   - 웹을 발명한 곳도 웹을 체계적으로 아카이빙 못 함
   - 개인 노력, 출판 목표, 역사적 감각의 뒤섞임

4. **Maemura, E., Worby, N., Milligan, I., & Becker, C. (2018).** "If these crawls could talk: Studying and documenting web archives provenance." *Journal of the Association for Information Science and Technology*, 69.
   - DOI: https://doi.org/10.1002/asi.24048
   - 핵심: 크롤링 프로세스 자체를 프로비넌스로 문서화
   - 수집·선정·기술 인프라의 결정 과정 체계화

5. **Maemura, E. (2023).** "Sorting URLs out: seeing the web through infrastructural inversion of archival crawling." *Internet Histories*, 7, 386-401.
   - DOI: https://doi.org/10.1080/24701475.2023.2258697
   - 핵심: URL·도메인·HTTP의 유동성
   - 전통 기록학의 원질서·계층 구조 개념이 웹에서 흔들림

**추가 참고 문헌**

- Costa, M., Gomes, D., & Silva, M. (2017). "The evolution of web archiving." *International Journal on Digital Libraries*, 18, 191-205.
- Ruest, N., Fritz, S., & Milligan, I. (2022). "Creating order from the mess: web archive derivative datasets and notebooks." *Archives and Records*, 43, 316-331.
- Ogden, J., Summers, E., & Walker, S. (2023). "Know(ing) Infrastructure: The Wayback Machine as object and instrument of digital research." *Convergence*, 30, 167-189.
- Winters, J. (2018). "Web Archives and (Digital) History: A Troubled Past and a Promising Future?" *The SAGE Handbook of Web History*.

**웹과 기록학의 충돌 지점 요약**

| 충돌 지점 | 웹 아카이브 특성 | 전통 기록학 한계 |
|-----------|-----------------|-----------------|
| 원질서·계층 | URL 유동적, 다중 경로, 네트워크 | 단일 계층, Fonds→Series→File |
| 완전성 | 크롤링·기술 제약으로 부분 보존 | 전체 기록 전제 |
| 기술 수준 | 집합·데이터·그래프 중심 | 개별 객체 중심 |
| 프로비넌스 | 크롤러, WARC, 플랫폼 정책 | 생산자 출처 중심 |

---

## 2회차. 미멕스는 왜 아직도 실현되지 않았는가

### Vannevar Bush, *As We May Think* (1945)

**개요**: 정보 과잉 시대에 기억과 지식을 어떻게 다룰 것인가에 대한 문제 제기

- [원문 (Atlantic)](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/)
- [Wikipedia 정리](https://en.wikipedia.org/wiki/As_We_May_Think)
- [Internet Archive PDF](https://archive.org/details/AsWeMayThink)

### Memex 개념

**개요**: 연상 경로(trail)를 기반으로 한 개인 기억 장치

- [Wikipedia: Memex](https://en.wikipedia.org/wiki/Memex)
- [Memex–Hypertext 계보 정리](https://en.wikipedia.org/wiki/History_of_hypertext)

---

## 3회차. 하이퍼텍스트는 왜 기억이 되지 못했는가

### Douglas Engelbart, *Augmenting Human Intellect* (1962)

**개요**: 문서, 링크, 주석, 협업을 통한 사고 증강

- [PDF 원문](https://www.dougengelbart.org/pubs/augment-3906.html)
- [NLS Demo (The Mother of All Demos)](https://archive.org/details/DouglasEngelbart1968Demo)

### Ted Nelson, Project Xanadu

**개요**: 영구 참조와 출처 보존을 목표로 한 하이퍼텍스트 시스템

- [Wikipedia: Project Xanadu](https://en.wikipedia.org/wiki/Project_Xanadu)
- [Wired: The Curse of Xanadu](https://www.wired.com/1995/06/xanadu/)

---

## 4회차. 우부웹은 왜 여전히 웹에 남아 있는가

### UbuWeb

**개요**: 전위 예술 자료 디지털 아카이브

- [공식 웹사이트](https://www.ubu.com/)
- [Wikipedia: UbuWeb](https://en.wikipedia.org/wiki/UbuWeb)
- [OpenCulture 소개 글](https://www.openculture.com/2010/03/avant-garde_media_the_ubuweb_collection.html)
- [VISLA 비평 기사](https://visla.kr/article/art/293336/)

---

## 5회차. 웹은 왜 스스로를 보존하지 못하는가

### Internet Archive / Wayback Machine

- [Internet Archive](https://archive.org/)
- [Wayback Machine](https://web.archive.org/)
- [Wayback 사용 가이드](https://help.archive.org/help/using-the-wayback-machine/)

### 웹 아카이빙 연구

- [Understanding Web Archiving Services and Their (Mis)Use on Social Media](https://arxiv.org/abs/1801.10396)
- [Who and What Links to the Internet Archive](https://arxiv.org/abs/1309.4016)

---

## 6회차. 웹 이후, 기록학은 무엇을 다시 배워야 하는가

**종합 회차**: 앞선 5회차 전체를 아우르는 내용

### 추가 참고: 선사적 아카이브 계보

**Paul Otlet / Mundaneum**

**개요**: 웹 이전의 세계 지식 아카이브 구상

- [Wikipedia: Mundaneum](https://en.wikipedia.org/wiki/Mundaneum)
- [Monoskop: Paul Otlet](https://monoskop.org/Paul_Otlet)

---

## 7. 참고용 읽기 자료 (선택)

### 서적

- *The New Media Reader* (MIT Press)
- *Memex to Hypertext: Vannevar Bush and the Mind's Machine*
- 웹 아카이빙 개론서 및 사례 연구 논문 모음

---

## 빠른 링크 모음

| 주제 | 링크 |
|------|------|
| As We May Think (Bush) | https://en.wikipedia.org/wiki/As_We_May_Think |
| Memex (사상 개요) | https://en.wikipedia.org/wiki/Memex |
| Hyperlink/하이퍼텍스트 배경 | https://en.wikipedia.org/wiki/Hyperlink |
| Wayback Machine | https://web.archive.org/ |
| Internet Archive | https://archive.org/ |
| UbuWeb 디지털 아카이브 | https://www.ubu.com/ |
| UbuWeb (Wikipedia) | https://en.wikipedia.org/wiki/UbuWeb |
| Mundaneum | https://en.wikipedia.org/wiki/Mundaneum |

---

## 추천 읽기 순서

1. **사상/개념 기반 세팅**
   - Bush *As We May Think* 원문 및 Wikipedia 요약
   - Memex 배경 이해

2. **하이퍼텍스트/링크 구조**
   - Hypertext/Hyperlink 역사
   - Xanadu 프로젝트

3. **웹 아카이브 사례**
   - Wayback Machine 공식 안내
   - 웹 아카이빙 연구 논문

4. **비제도적 아카이브**
   - UbuWeb 탐색 및 비평 기사

5. **심화/응용**
   - 웹 아카이브 분석 논문

---

*본 문서는 연재 집필 과정에서 지속적으로 업데이트 가능한 레퍼런스 노트입니다.*
## 7. 참고용 읽기 자료 (선택)

### 서적

- *The New Media Reader* (MIT Press)
- *Memex to Hypertext: Vannevar Bush and the Mind's Machine*
- 웹 아카이빙 개론서 및 사례 연구 논문 모음

---

## 빠른 링크 모음

| 회차 | 주제 | 주요 링크 |
|------|------|-----------|
| 1회차 | WWW 제안서 | https://www.w3.org/History/1989/proposal.html |
| 2회차 | As We May Think | https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/ |
| 2회차 | Memex | https://en.wikipedia.org/wiki/Memex |
| 3회차 | Engelbart Demo | https://archive.org/details/DouglasEngelbart1968Demo |
| 3회차 | Project Xanadu | https://en.wikipedia.org/wiki/Project_Xanadu |
| 4회차 | UbuWeb | https://www.ubu.com/ |
| 5회차 | Internet Archive | https://archive.org/ |
| 5회차 | Wayback Machine | https://web.archive.org/ |
| 6회차 | Mundaneum | https://en.wikipedia.org/wiki/Mundaneum |

---

## 회차별 필수 읽기

### 1회차
- [x] Tim Berners-Lee, Information Management: A Proposal
- [x] W3C World Wide Web History
- [x] 기록학 1989-1993 타임라인 (로컬 리서치)

### 2회차
- [ ] Vannevar Bush, As We May Think 원문
- [ ] Memex 개념 정리 (Wikipedia)

### 3회차
- [ ] Douglas Engelbart, Augmenting Human Intellect
- [ ] Project Xanadu 배경 (Wikipedia + Wired 기사)

### 4회차
- [ ] UbuWeb 웹사이트 탐색
- [ ] UbuWeb 관련 비평 기사 (OpenCulture, VISLA)

### 5회차
- [ ] Internet Archive 공식 문서
- [ ] 웹 아카이빙 연구 논문 1-2편

### 6회차
- [ ] 전체 회차 복습
- [ ] Mundaneum 배경 자료

---

*본 문서는 연재 집필 과정에서 지속적으로 업데이트 가능한 레퍼런스 노트입니다.*
