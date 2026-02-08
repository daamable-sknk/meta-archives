# 웹 이후의 기록학 1회차 — 작업 노트

## 기본 정보

- **제목**: 웹은 처음부터 아카이브였다
- **회차**: 1/6
- **역할**: 연재 선언문
- **분량**: 1,200-1,800자
- **발행처**: 기록과사회 뉴스레터
- **예상 발행**: 2026년 3-4월

---

## 핵심 질문

- 웹은 왜 '정보 전달 도구'로만 기억되는가?
- 웹의 초기 설계에서 기록학은 무엇을 놓쳤는가?

---

## 주요 관점

웹의 목적을 **출판이 아닌 참조 시스템**으로 재해석

---

## 필수 읽기 자료

### 1순위 (반드시 읽기)
- [ ] Tim Berners-Lee, [Information Management: A Proposal (1989)](https://www.w3.org/History/1989/proposal.html)
- [ ] [World Wide Web 역사 (W3C)](https://www.w3.org/History.html)

### 2순위 (참고)
- [ ] [Wikipedia: World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web)

---

## 인용 후보 메모

### Information Management: A Proposal (1989)에서

**제목과 문제의식**
- 제목이 "Information Management"임 - 웹 페이지나 출판이 아님
- 처음 이름은 "Mesh", 1990년에야 "World Wide Web"으로 결정

**핵심 문제: 기억의 손실**
> "A problem, however, is the high turnover of people. When two years is a typical length of stay, information is constantly being lost."

> "Often, the information has been recorded, it just cannot be found."

**웹의 목적: 정보의 풀**
> "the hope would be to allow a pool of information to develop which could grow and evolve with the organisation and the projects it describes."

**왜 트리가 아닌 웹인가**
> "The system we need is like a diagram of circles and arrows, where circles and arrows can stand for anything."

> "A tree has the practical advantage of giving every node a unique name. However, it does not allow the system to model the real world."

**링크의 본질: 관계의 기록**
- 링크가 표현하는 관계 유형들:
  - depends on (의존)
  - is part of (부분)
  - made (제작)
  - refers to (참조)
  - uses (사용)
  - is an example of (예시)

**결론 문장**
> "We should work toward a universal linked information system, in which generality and portability are more important than fancy graphics techniques and complex extra facilities."

### World Wide Web 역사에서

**1980: ENQUIRE (Enquire-Within-Upon-Everything)**
- Tim Berners-Lee가 CERN에서 만든 개인용 정보 관리 프로그램
- 임의의 노드들 간에 링크 생성 가능
- 각 노드는 제목, 타입, 양방향 타입 링크 목록을 가짐
- **이미 1980년에 링크의 타입화와 양방향성이 구현됨**

**1989년 3월: 제안서 회람**
- "Information Management: A Proposal" 작성 및 CERN 내부 회람
- 배경 문서: "HyperText and CERN" 생산

**1990년 10월: "WorldWideWeb"이라는 이름**
- Tim이 NeXTStep 환경에서 하이퍼텍스트 GUI 브라우저+에디터 개발 시작
- 프로그램 이름으로 "WorldWideWeb" 고안
- 프로젝트 이름 후보: Information Mesh, Mine of Information, Information Mine
- **최종 선택: "World Wide Web"**

**1990년 11월: 첫 웹 서버와 웹 페이지**
- 첫 웹 서버: nxoc01.cern.ch (나중에 info.cern.ch)
- 첫 웹 페이지: http://nxoc01.cern.ch/hypertext/WWW/TheProject.html
- WorldWideWeb 프로그램: WYSIWYG 브라우저/에디터, 직접 인라인 링크 생성 가능

**1990년 크리스마스: 시연 가능**
- Line mode browser와 WorldWideWeb browser/editor 시연
- 하이퍼텍스트 파일, CERNVM "FIND" 인덱스, 인터넷 뉴스 기사에 접근 가능

**1991년 8월: 공개**
- 파일들이 FTP로 네트워크에 공개됨
- alt.hypertext, comp.sys.next.announce 등에 게시

**1993년 4월 30일: CERN의 선언**
- CERN 이사진이 WWW 기술을 누구나 무료로 사용할 수 있다고 선언
- 중요한 이정표 문서

**핵심 통찰**
- 웹의 기원은 **개인 정보 관리 시스템** (ENQUIRE, 1980)
- 웹은 처음부터 **브라우저이자 에디터**였음 (읽기+쓰기)
- 웹의 초기 이름 후보들이 모두 **정보의 구조**를 가리킴 (Mesh, Mine, Web)

---

## 글 구조 (수정안 - 옵션 1: 웹 vs 기록학 병치)

### 1. 도입 (200-250자)
- 우리는 웹을 어떻게 기억하는가
- 제목은 "Information Management"였다

### 2. 1989년: 두 개의 평행 우주 (500-600자)
- CERN에서 Berners-Lee가 제안한 것
  - "정보는 기록되었다. 그러나 찾을 수 없다"
  - circles and arrows: 타입화된 관계의 네트워크
- 동시에 기록학계는
  - "Easy to byte, harder to chew" - 전자기록 위기
  - RAD, ISAD(G) - 계층 구조 표준화

### 3. 구조적 유사성: circles and arrows (400-500자)
- Berners-Lee의 다이어그램: depends on, is part of, made, refers to
- 2023년 RiC가 도달한 곳: Entities-Relations 그래프
- 중간의 ISAD(G): Fonds→Series→File→Item 계층

### 4. 왜 만나지 못했나: 34년의 지연 (200-250자)
- 1996: Internet Archive (기술자가 시작)
- 2003: IIPC (제도화)
- 2013-2023: RiC (구조적 함의 인식)

### 5. 질문 (150-200자)
- 웹은 처음부터 아카이브였다
- 무엇을 다시 배워야 하는가

**목표 분량: 1,450-1,800자**

---

## 초고 (수정 4차 - 2026-02-08, CERN 아이러니 강화)

### 웹은 처음부터 아카이브였다

우리는 웹을 무엇으로 기억하는가. 홈페이지, 블로그, 소셜미디어. 정보를 전달하는 플랫폼. 그러나 1989년 3월, Tim Berners-Lee가 CERN에 제출한 제안서의 제목은 "Information Management: A Proposal"—정보 관리였다.

**1989년, 두 개의 평행 우주가 있었다.** CERN에서 Berners-Lee는 문제를 이렇게 정의했다. "정보는 기록되었다. 그러나 찾을 수 없다." 문제는 기록의 부재가 아니라 **참조의 불가능**이었다. 그가 제안한 것은 진화하는 정보의 풀이었다. 왜 트리가 아닌 웹인가? "A tree does not allow the system to model the real world." 그가 그린 다이어그램은 "circles and arrows"였고, 그 화살표는 **관계의 타입**을 표현했다. depends on, is part of, made, refers to. 링크는 **의미의 기록**이었다.

같은 시기, 기록학계는 다른 위기를 겪고 있었다. Terry Cook은 1991년 논문을 "Easy to byte, harder to chew"라 제목 붙였다. 기록학은 전자기록을 어떻게 다룰지 몰랐다. 1990년 RAD, 1993년 ISAD(G). 둘 다 엄격한 계층이었다. Fonds → Series → File → Item. 웹이 공개된 1991년, 기록학 문헌에서 "network structure"는 거의 보이지 않았다.

흥미로운 것은 **둘이 같은 구조에 도달했다는 사실**이다. Berners-Lee의 1989년 다이어그램과 2023년 ICA의 RiC를 비교해보라. 둘 다 circles and arrows다. 둘 다 entities와 relations의 그래프다. 차이는 **34년의 시간**이다. Emily Maemura가 지적한 것처럼, RiC는 개별 객체가 아니라 **집합 수준**에서 관계의 네트워크를 기술한다.

그 사이 무슨 일이 있었나. 1996년, Internet Archive가 설립되었다. 설립자는 기술자였지만, 역설적으로 **도서관 프레임워크**를 이식했다. Katie Hegarty가 밝힌 것처럼, 웹은 "출판물"로 다뤄졌고 네트워크 구조의 본질은 놓쳤다. 웹 아카이빙은 "보존 문제"가 되었다. 크롤러, WARC 파일. **구조적 함의**는 논의되지 않았다.

아이러니는 더 깊다. 웹을 발명한 CERN조차 자신의 웹 역사를 제대로 아카이빙하지 못했다. Fomasi의 2023년 연구가 밝힌 CERN WWW 컬렉션의 실상: 1992년 Robert Cailliau의 **아내가 권유**해서 시작되었고, Cailliau는 "역사적 측면은 무시되었다"고 회고한다. Tim Berners-Lee의 문서 대부분은 MIT로 가져가 **부재**하고, 1993년 공개 도메인 선언문 원본 같은 핵심 문서들은 **사라졌다**. CERN 아카이브 정책은 웹 공개 6년 후인 **1997년에야** 수립되었다. 정보 관리 시스템을 만든 곳이 정보를 관리하지 못했다.

2013년이 되어서야 ICA는 RiC 개발을 시작했다. 그리고 2023년, 웹 발명 34년 후, 기록학은 드디어 **네트워크 기반 기술 모델**에 도달했다. 웹은 처음부터 아카이브였다. 문제는 우리가 그것을 읽지 못했다는 것이다. 질문은 이것이다. 왜 두 세계는 만나지 못했는가. 그리고 지금, RiC가 웹의 구조를 닮아가는 이 순간, 기록학은 웹으로부터 무엇을 다시 배워야 하는가.

#### 참고문헌

- Berners-Lee, T. (1989). *Information Management: A Proposal*. CERN. https://www.w3.org/History/1989/proposal.html
- Cook, T. (1991). Easy to byte, harder to chew: The second generation of electronic records archives. *Archivaria*, 33, 202-216.
- Fomasi, M., Barcella, D., Benecchi, E., & Balbi, G. (2023). Genealogy of an archive: The birth, construction, and development of the World Wide Web collection at CERN. *Internet Histories*, 7(3-4), 277-294. https://doi.org/10.1080/24701475.2023.2188448
- Hegarty, K. (2022). The invention of the archived web: Tracing the influence of library frameworks on web archiving infrastructure. *Internet Histories*, 6(4), 432-451. https://doi.org/10.1080/24701475.2022.2103592
- Maemura, E. (2025). Conceptualizing aggregate-level description in web archives. *Archival Science*, 25, 119-143. https://doi.org/10.1007/s10502-024-09441-3
- International Council on Archives. (2023). *Records in Contexts (RiC) Ontology Version 1.0*. https://www.ica.org/standards/RiC/

---

## 리서치 노트

### 기록학 타임라인 (1989-1993)

**웹이 등장하는 동안 기록학은 무엇을 하고 있었나?**

- **1989**: 웹 발명 (3월) / Terry Cook의 전자기록 연구 시작
- **1990**: RAD (Rules for Archival Description) 발행 (캐나다)
  - 첫 번째 포괄적 기술표준
  - 여전히 계층 구조 (fonds → series → file → item)
- **1991**: 웹 공개 (8월) / Terry Cook "Easy to byte, harder to chew" 발표
  - 제목부터 "전자기록 다루기 어렵다"
- **1992-1993**: EAD (Encoded Archival Description) 프로젝트 시작 (UC Berkeley, Daniel Pitti)
  - SGML 사용 (HTML의 사촌)
  - 그러나 여전히 계층적 구조
- **1993**: ISAD(G) 초안 승인 (ICA) / Mosaic 브라우저 출시 (4월)
  - 국제 기록 기술 표준
  - Multi-level description (상위→하위)

**핵심 발견:**
- 기록학은 "전자기록 위기"에 압도당하고 있었음
- 웹/하이퍼텍스트에 대한 인식이 **거의 없었음**
- 다른 커뮤니티: 물리학/컴퓨터과학 vs 인문학 훈련받은 아키비스트
- 인프라 부재: 대부분의 아카이브에 컴퓨터/인터넷 접근 없음

### 기록학의 웹 인식 타임라인

**언제 기록학이 웹을 알아차렸나?**

- **1996**: Internet Archive 설립 (Brewster Kahle, 기술자이지 아키비스트 아님)
- **Mid-1990s**: 웹 아카이빙 프로젝트들 시작
  - 그러나 **기술적 보존 문제**로만 다뤄짐
  - 구조적/패러다임적 함의는 놓침
- **2003**: IIPC (International Internet Preservation Consortium) 설립
  - 이때서야 웹 아카이빙이 기록학에서 제도화됨

**웹을 어떻게 받아들였나?**
- **"새로운 매체"** - 보존해야 할 대상
- **"기술적 도전"** - 크롤러, 저장 포맷, WARC 파일
- **놓친 것**: 웹의 **네트워크 구조**가 기록학 원칙에 주는 도전

### RiC vs 초기 웹의 구조적 유사성

**Berners-Lee의 1989년 다이어그램:**
- "circles and arrows" - 원과 화살표
- 각 화살표는 **관계의 타입**을 표현
  - depends on, is part of, made, refers to, uses, is example of
- **양방향 링크** (1980년 ENQUIRE부터)
- **비계층적 네트워크**

**RiC (Records in Contexts):**
- **개발 시작**: 2013 (웹 발명으로부터 24년 후)
- **Version 1.0**: 2023 (34년 후)
- **핵심 특징**:
  - 비계층적 네트워크 모델
  - Entities와 Relations의 그래프
  - Record, Agent, Activity, Rule, Place, Date
  - 복잡한 관계 표현 (created by, used by, subject of, related to)
  - Record vs Instantiation 구분

**ISAD(G) (1994):**
- 엄격한 계층 구조
- Fonds → Subfonds → Series → Files → Items
- 부모-자식 관계만
- 단일 출처 (single provenance)
- 26개 요소, 7개 영역

**왜 30년이 걸렸나?**
- 제도적 관성: 수세기의 계층적 실천
- 기술적 초점: 초기 웹 아카이빙은 보존, 이론 아님
- 분리된 커뮤니티: 기술자 (Internet Archive) vs 아키비스트 (ICA)
- 표준은 시간이 걸림: 국제적 합의 형성 느림

### 핵심 통찰

**27-34년의 지연:**
- Internet Archive 설립 (1996) → RiC 개념 작업 시작 (2013): **17년**
- 웹 발명 (1989) → RiC 1.0 (2023): **34년**

**기록학은 웹을:**
1. **처음엔**: 새로운 매체/보존 도전으로 봄 (1990년대 중반)
2. **나중에**: 구조적/패러다임적 함의 인식 (2013년 이후 RiC)
3. **결과**: RiC의 네트워크 모델은 본질적으로 **웹에서 영감받음**

---

## 학술 레퍼런스 (2026-02-08 추가)

### 핵심 논문

**웹 아카이브와 기록학의 간극**

1. **Maemura, E. (2025).** "Conceptualizing aggregate-level description in web archives." *Archival Science*, 25.
   - 핵심: 웹 아카이브는 **집합 수준(aggregate-level)에서 기술**되어야 함
   - 전통적 기록학의 개별 객체 중심 기술로는 웹의 구조를 포착할 수 없음
   - RiC가 도달한 지점: 다중 표현, 네트워크 기반 기술
   - **초고와의 연결**: "왜 34년이 걸렸나" - 집합 수준 사고로의 전환

2. **Hegarty, K. (2022).** "The invention of the archived web: tracing the influence of library frameworks on web archiving infrastructure." *Internet Histories*, 6, 432-451.
   - 핵심: 웹 아카이빙이 **도서관 프레임워크의 영향**을 받음
   - Internet Archive가 서지 중심, 출판물 메타데이터를 이식
   - 웹을 "출판물"로 다루며 네트워크 구조의 본질을 놓침
   - **초고와의 연결**: "보존 문제로 다뤄짐" - 도서관 패러다임의 한계

3. **Fomasi, M., Barcella, D., Benecchi, E., & Balbi, G. (2023).** "Genealogy of an archive. The birth, construction, and development of the World Wide Web collection at CERN." *Internet Histories*, 7, 277-294.
   - 핵심: CERN의 WWW 컬렉션조차 **부분적·우연적 수집**
   - 웹을 발명한 곳도 웹을 체계적으로 아카이빙하지 못함
   - 개인적 노력, 출판 목표, 역사적 감각의 뒤섞임
   - **초고와의 연결**: "웹은 처음부터 아카이브였다"의 아이러니

4. **Maemura, E., Worby, N., Milligan, I., & Becker, C. (2018).** "If these crawls could talk: Studying and documenting web archives provenance." *Journal of the Association for Information Science and Technology*, 69.
   - 핵심: 크롤링 프로세스 자체를 **프로비넌스로 문서화**해야 함
   - 수집·선정·기술 인프라의 결정 과정 체계화
   - **초고와의 연결**: 기록학이 웹으로부터 배워야 할 것

5. **Maemura, E. (2023).** "Sorting URLs out: seeing the web through infrastructural inversion of archival crawling." *Internet Histories*, 7, 386-401.
   - 핵심: URL·도메인·HTTP의 유동성
   - 전통 기록학의 **원질서·계층 구조** 개념이 웹에서 흔들림
   - **초고와의 연결**: "트리가 아닌 웹" - 계층이 실제 세계를 모델링하지 못함

### 웹과 기록학의 충돌 지점 요약

| 충돌 지점 | 웹 아카이브의 특성 | 전통 기록학의 한계 |
|-----------|-------------------|-------------------|
| 원질서·계층 | URL 유동적, 다중 경로, 네트워크 구조 | 단일 계층, Fonds→Series→File |
| 완전성 | 크롤링·기술 제약으로 부분적 보존 | 전체 기록 전제 |
| 기술 수준 | 대규모·데이터 중심·그래프 분석 | 개별 객체 중심 기술 |
| 프로비넌스 | 크롤러, WARC, 플랫폼 정책에 의해 규정 | 생산자 출처 중심 |

**출처:** Maemura (2025), Hegarty (2022), Maemura (2023), Ruest et al. (2022)

### 추가 참고 문헌

- **Costa, M., Gomes, D., & Silva, M. (2017).** "The evolution of web archiving." *International Journal on Digital Libraries*, 18, 191-205.
- **Ruest, N., Fritz, S., & Milligan, I. (2022).** "Creating order from the mess: web archive derivative datasets and notebooks." *Archives and Records*, 43, 316-331.
- **Ogden, J., Summers, E., & Walker, S. (2023).** "Know(ing) Infrastructure: The Wayback Machine as object and instrument of digital research." *Convergence*, 30, 167-189.
- **Winters, J. (2018).** "Web Archives and (Digital) History: A Troubled Past and a Promising Future?" *The SAGE Handbook of Web History*.

### 초고 3차 작성을 위한 핵심 포인트

**추가/강화할 논점:**

1. **CERN의 아이러니** (Fomasi 2023)
   - 웹을 만든 곳조차 웹을 제대로 아카이빙하지 못함
   - "부분적·우연적 수집"
   - 초고 위치: 도입부 또는 4번 섹션(34년의 지연)

2. **도서관 프레임워크의 이식** (Hegarty 2022)
   - Internet Archive가 "기술자"가 시작했지만
   - 실제로는 서지 중심, 출판물 메타데이터 이식
   - "보존 문제"로 축소 = 도서관 패러다임의 한계
   - 초고 위치: 4번 섹션(1996 Internet Archive)

3. **집합 수준 기술의 필요성** (Maemura 2025)
   - RiC = aggregate-level description
   - 개별 객체 중심에서 집합·관계 중심으로
   - 왜 34년 걸렸나 = 사고 전환의 시간
   - 초고 위치: 3번 섹션(구조적 유사성)

4. **원질서 개념의 붕괴** (Maemura 2023)
   - URL·도메인의 유동성
   - "A tree does not allow the system to model the real world"의 구체화
   - 초고 위치: 2번 섹션(1989년 평행 우주)

## 편집 노트

### 유저 피드백 (2026-02-08)

**핵심 질문 재정의:**
- 웹은 자연발생적 필요성 (인수인계 잘하기)에서 하이퍼텍스트-네트워크 방식으로 진화
- **기록학은 그동안 무엇을 하고 있었나?** (손놓고, 관심없고, 나중에 받아들임)
- Tim Berners-Lee 초기 이미지 ≈ RiC 모델 유사성
- 왜 기록학은 이걸 놓쳤나?

**초고의 문제점:**
- 현재: "웹은 아카이브였다" 선언에 가까움
- 부족: **기록학이 실제로 무엇을 했는지/안 했는지** 구체적 언급 없음
- 부족: 웹-RiC 구조적 유사성 비교 없음

**수정 방향:**
1. 기록학 타임라인 추가 (1989-1993, RiC 2013-2023)
2. 구조적 유사성 강조 (Berners-Lee diagram vs RiC)
3. 질문 구체화: "놓쳤다"→"무엇을 하고 있었나?", "어떻게 받아들였나?"

**다음 작업:**
- 리서치 완료됨 ✓
- 초고 재작성 필요 (기록학 병치, 구조 비교 추가)

---

## 체크리스트

- [x] 필수 자료 읽기 완료
- [x] 리서치: 기록학 1989-1993 타임라인
- [x] 리서치: 기록학의 웹 인식 (1996-2023)
- [x] 리서치: Berners-Lee vs RiC 구조 비교
- [x] 학술 레퍼런스 추가 (Maemura, Hegarty, Fomasi 등)
- [x] 초고 1차 작성 (1,487자)
- [x] 초고 2차 재작성 (1,610자 - 기록학 병치)
- [x] 초고 3차 재작성 (1,667자 - 학술 레퍼런스 반영)
- [x] 분량 확인 (1,200-1,800자)
- [ ] 질문이 명확하게 드러나는가?
- [ ] 연재 전체의 톤 설정이 되었는가?
- [ ] 최종 편집 완료
- [ ] 기록과사회 제출

---

*작업 시작일: 2026-02-08*
