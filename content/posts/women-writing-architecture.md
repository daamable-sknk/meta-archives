# Women Writing Architecture
— 아카이브의 형식을 사용하는 커뮤니티에 대한 비평

---

## 1차 기술

Women Writing Architecture는 스스로를  
“an open, annotated bibliography collecting texts written by women about architecture”라고 정의한다.  
이 자기 정의에서 핵심은 **women**, **writing**, **architecture**라는 세 단어의 병치다.

이 프로젝트가 수집하는 최소 단위는 ‘아카이브’나 ‘프로젝트’가 아니라,  
**건축에 대해 쓰인 하나의 글(text)**이다.  
원문 텍스트는 이곳에 저장되지 않는다. 대신 각 글은 서지 정보와 함께  
요약, 주석(annotation), 분류 정보로 재구성된다.

웹사이트의 기본 화면은 index에 노출된 글 목록이다.  
→ https://womenwritingarchitecture.org/

사용자는 Glossary, Type, Language 등의 필터를 통해 이 목록을 탐색한다.  
이는 전통적인 데이터베이스 검색이라기보다,  
개별 글보다 **개념어(glossary)**를 중심으로 한 의미론적 탐색을 유도하는 구조다.  
→ https://womenwritingarchitecture.org/glossary/

---

## 아이템보다 중요한 것: 맥락의 구조

이 사이트에서 중요한 것은 개별 글(item) 자체보다,  
**글이 어떤 맥락 속에 놓이는가**이다.

각 아이템 페이지는 두 개의 축으로 구성된다.

- 왼쪽에는 **컬렉션(collection)**  
  → https://womenwritingarchitecture.org/collections/
- 오른쪽에는 **주석(annotation)**  
  → 개별 글 상세 페이지 내 annotation 영역

이 배치는 우연이 아니다.  
글은 이 구조 안에서만 접근 가능하며,  
항상 **어떤 묶음에 속한 상태**이자 **어떤 해석을 동반한 상태**로 제시된다.

이 아카이브에서 글은 독립적인 객체가 아니라,  
항상 관계와 해석 속에 위치한 존재다.

---

## 보이지 않는 엔티티: 사람과 역할

아이템 페이지에는 명시적으로 드러나지 않지만,  
이 구조를 가능하게 하는 중요한 엔티티가 있다.  
바로 **사람**이다.

- 컬렉션은 누군가가 만든 것이다.
- 주석은 누군가가 쓴 것이다.
- glossary의 용어 역시 누군가의 선택과 합의의 결과다.

그러나 이 ‘사람’은 아이템의 속성으로 등장하지 않는다.  
대신 People and Organisations 페이지를 통해  
**taxonomy 형태로 관리**된다.  
→ https://womenwritingarchitecture.org/people-and-organisations/

이 설계는 개인을 전면에 드러내기보다,  
사람을 **역할과 관계의 집합**으로 위치시키는 선택이다.  
저자는 숭배되지 않고,  
대신 누가 어떤 방식으로 개입했는지만이 구조 속에 남는다.

---

## 구조로서의 관계: 이 아카이브가 작동하는 방식

Women Writing Architecture에서 글(item)은 중심에 놓이지만,  
의미의 출발점은 아니다.  
이 아카이브는 개별 글이 아니라,  
글을 둘러싼 **사람, 역할, 분류 체계, 해석의 관계**를 통해 작동한다.

이 구조를 단순화하면 다음과 같이 그릴 수 있다.

```
[ Person / Organisation ]
↓ (taxonomy)
[ Collection ] [ Annotation ]
\ /
\ /
[ Item: Text ]
```

여기서 중요한 점은,  
사람(Person / Organisation)이 아이템에 직접 연결되지 않는다는 것이다.  
사람은 taxonomy를 통해 컬렉션을 만들고,  
주석을 작성하며,  
그 결과가 아이템을 둘러싼 맥락을 형성한다.

글은 이 구조의 중심에 있지만,  
결코 단독으로 존재하지 않는다.  
항상 **누군가의 선택과 해석이 만들어낸 자리(position)** 속에서만  
접근 가능하다.

---

## taxonomy는 분류가 아니라 관계 모델이다

People, Organisations, Glossary는 모두 taxonomy로 운영된다.

- People / Organisations  
  → https://womenwritingarchitecture.org/people-and-organisations/
- Glossary  
  → https://womenwritingarchitecture.org/glossary/

이는 이 사이트에서 taxonomy가 단순한 분류 체계가 아님을 보여준다.

taxonomy는 글을 설명하지 않는다.  
대신 글이 놓일 수 있는 **맥락의 풀(pool)**을 만든다.

- 사람은 글의 저자가 아니라 관계의 노드로 존재한다.
- 개념은 정의가 아니라 연결의 장치로 기능한다.

이 아카이브에서 의미는 고정되지 않고,  
taxonomy를 통해 **계속 재배치**된다.

---

## forum이 드러내는 이 사이트의 성격

/forum 페이지는 이 사이트의 정체성을 결정적으로 드러낸다.  
→ https://womenwritingarchitecture.org/forum/

이 공간은 자유 토론 게시판이 아니다.  
이곳에는 이 사람들, 이 모임이 **함께 작업한 결과물**이 축적된다.

forum은 과정 그 자체를 기록하지 않는다.  
대신 공동체의 실천이 일정한 형식으로 정리된 결과만이 남는다.  
그리고 이 결과물은 다시 bibliography와 taxonomy로 흡수된다.

즉, 이 사이트는 외부에서 생산된 지식을 모으는 곳이 아니라,  
**커뮤니티의 집단적 실천을 정제해 공개하는 플랫폼**이다.

---

## 아카이브처럼 보이는 이유

Women Writing Architecture는 아카이브의 외형을 적극적으로 차용한다.

- 목록(index) → https://womenwritingarchitecture.org/
- 서지 정보와 아이템 페이지
- 분류 체계(taxonomy)
- 주석(annotation)
- 용어집(glossary)

그러나 이 모든 요소는  
자료를 보존하기 위해서가 아니라,  
**커뮤니티의 실천을 지식의 형식으로 격상시키기 위해** 사용된다.

이 사이트는 커뮤니티이지만,  
커뮤니티처럼 보이기를 선택하지 않는다.  
대신 아카이브의 언어로 자신을 말한다.

---

## 아카이브는 결과가 아니라 과정이다

이 구조에서 아카이브는 완성될 수 없다.

- glossary는 계속 추가되고
- taxonomy는 재배치되며
- forum의 결과는 다시 글 목록으로 편입된다

운영 주체는 단일하지 않고,  
복수의 운영진이 서로를 참조하며 작업을 이어간다.  
권위는 중앙에 있지 않고,  
**상호 참조(reference)** 속에서 생성된다.

이 아카이브는 결과물이 아니라,  
**아카이빙이 지속되는 과정 그 자체**다.

---

## 관찰 메모

- 2026-01-04: 자동화된 웹 요청 시 403 응답, 브라우저 접근 시 HTTP 200.
- 2026-01-04: People and Organisations는 개별 아이템과 직접 연결되지 않고 taxonomy로만 연동됨.
- 2026-01-04: forum은 토론 기록이 아니라 공동체 실천의 결과물 저장소에 가까움.
- 2026-01-04: glossary는 정의의 집합이 아니라 합의의 흔적으로 보임.
