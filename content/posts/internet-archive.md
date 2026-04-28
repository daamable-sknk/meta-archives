# Internet Archive

![Internet Archive logo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Internet_Archive_logo_and_wordmark.svg/500px-Internet_Archive_logo_and_wordmark.svg.png)

## 100일

웹페이지의 평균 수명은 100일이다. 도메인 만료, 서버 종료, 리뉴얼, 정책 변경 등 이유는 다양하지만 결과는 같다. 사라진다. [Pew Research Center(2024)](https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/)에 따르면 2013년에서 2023년 사이 존재했던 웹페이지 중 25%가 더 이상 접근할 수 없다고 한다. 10년 전 페이지로 좁히면 38%가 사라졌다.

웹은 기록이 쌓이는 공간이 아니다. 현재로 계속 덮어씌워지는 공간이다. 어제의 뉴스 기사, 지난달의 블로그 포스트, 작년의 정부 문서. 링크를 클릭하면 404[^17]가 뜬다. 웹은 기억하지 않는다.[^14]

1996년, [브루스터 케일(Brewster Kahle)](https://en.wikipedia.org/wiki/Brewster_Kahle)은 이 문제를 인식했다. "웹이 알렉산드리아 도서관처럼 사라질 수 있다." 그는 [인터넷 아카이브](https://archive.org)를 설립했다. 미션은 단순하다: *Universal Access to All Knowledge. 모든 지식에 대한 보편적 접근.* 30년이 지난 2025년, 인터넷 아카이브는 1조 개의 웹페이지를 저장했다.[^15]

그런데 이름에 '아카이브'가 붙었다고 아카이브인가?

## Wayback Machine

인터넷 아카이브의 핵심 서비스는 [Wayback Machine](https://web.archive.org)이다. 2001년 공개된 이 도구는 과거 웹페이지의 스냅샷을 보여준다. URL을 입력하면 해당 주소가 언제 어떤 모습이었는지 타임라인으로 확인할 수 있다.

작동 방식은 이렇다. [Heritrix](https://github.com/internetarchive/heritrix3)[^1]라는 크롤러가 웹을 돌아다니며 페이지를 수집한다. 수집된 데이터는 WARC[^2] 포맷으로 저장된다. HTTP 요청과 응답 전체, 타임스탬프, 원본 URI, 무결성 해시까지 포함하는 국제 표준(ISO 28500) 형식이다. 누구나 [Save Page Now](https://web.archive.org/save) 버튼을 눌러 원하는 페이지를 즉시 아카이빙할 수도 있다.[^16]

그러나 저장되지 않는 것이 있다. 크롤러가 가져가는 것은 HTML, 즉 사용자에게 보여지는 최종 결과물 뿐이다. 최종적인 HTML을 동적으로 만들어내는 JavaScript, 외부에서 데이터를 불러오는 API 호출, 로그인 뒤에서 작동하는 서버 인증은 HTML 코드 바깥에 있다. 즉, 크롤러의 손이 닿지 않는다. robots.txt[^3]로 차단된 페이지, 삭제 요청을 받은 콘텐츠도 마찬가지다.

Wayback Machine은 "과거를 저장"하는 것이 아니다. 특정 시점에 특정 방식으로 수집된 복제본의 집합이다. 연속적인 타임라인이 아니라 단절된 스냅샷들. 인터넷 아카이브 스스로도 이를 인정한다: "그 당시 페이지가 보였던 모습의 사본(a copy of a page as it appeared at the time)."[^18]

## 사라지는, 부서지기 쉬운 문화

2026년, 인터넷 아카이브는 [*Vanishing Culture: A Report on Our Fragile Cultural Record*](https://archive.org/details/vanishing-culture-2026)라는 책을 발간했다. 웹에 올라온 정보들이 얼마나 쉽게, 갑자기, 대규모로 사라지는지를 기록한 책이다. 몇 가지 사례를 보자.

2024년 6월, Paramount는 MTV News와 CMT의 웹사이트를 삭제했다.[^19] 수십 년간 축적된 음악 저널리즘이 하룻밤 사이에 사라졌다. 같은 달 Comedy Central 웹사이트도 삭제됐다.[^21] The Daily Show 25년치 클립, Colbert Report 전 시즌이 증발했다. Paramount+로 유도하겠다는 명목이었지만, 정작 Paramount+에는 해당 콘텐츠가 없다.

2019년, Myspace는 1,400만 아티스트가 업로드한 5,000만 곡을 "실수로" 삭제했다.[^20] 서버 마이그레이션 과정의 사고였다. 복구되지 않았다. 같은 해 4월, Twitter는 Vine 아카이브를 폐쇄했다.[^22] 2017년 서비스 종료 후 2년간 유지되던 아카이브마저 사라졌다.

패턴이 보인다. 기업의 전략 변경, 서버 이전 중 실수, 비용 절감, 서비스 종료. 디지털 콘텐츠는 물리적 매체와 달리 "삭제" 한 번이면 흔적 없이 사라진다. 기술이 발전할수록 데이터의 양은 늘어나지만, 그만큼 대규모 손실의 가능성도 커진다.

이것은 새로운 현상이 아니다. 1950년 이전 무성영화의 50%가 손실됐다. 스튜디오들의 "대량 폐기(wholesale junking)" 때문이었다. 1890년에서 1964년 사이 저작권 보호를 받는 음반 중 CD로 재발행된 것은 36%에 불과하다. 특히 "ethnic"으로 분류된 음악의 재발행률은 1%. 유색인종 음악가들의 기록이 불균형적으로 사라졌다. [Video Game History Foundation(2023)](https://gamehistory.org/87percent/)에 따르면 1960년에서 2009년 사이 출시된 클래식 게임 중 87%가 상업적으로 접근 불가능하다.

MTV News 사례로 돌아가자. Wayback Machine이 55만 페이지를 보존하고 있었기에 완전한 소실은 면했다. 인터넷 아카이브가 없었다면? *Vanishing Culture*는 Pew Research 데이터를 인용한다: 2013년에서 2023년 사이 존재했던 웹페이지 중 25%가 이미 접근 불가능하다. 이 중 62%는 Wayback Machine 덕분에 여전히 볼 수 있다. Wayback Machine이 없었다면 16%는 완전히 사라졌을 것이다.

보존은 때로 새로운 의미를 만들어낸다. *It's a Wonderful Life*(1946)는 개봉 당시 상업적으로 실패했다. 저작권 갱신을 놓쳐 퍼블릭 도메인[^5]이 됐고, TV 방송국들이 무료로 반복 방영하면서 크리스마스 명작으로 재발견, AFI 선정 미국 영화 역사상 11위에 올랐다. 1993년 영화보존위원회는 "보존 없는 접근은 무의미하다(preservation without access is pointless)"고 말했다. 역으로, 접근이 보존을 만들기도 한다.

## 원칙을 거스르기 : 인터넷 아카이브의 경우

그래서, 인터넷 아카이브는 정말 아카이브인가?

기록학에는 아카이브를 정의하는 원칙들이 있다. 출처(provenance)[^6], 원질서(original order)[^7], 진본성(authenticity)[^8]. 놀랍게도, 인터넷 아카이브는 이 모든 것을 위반한다.

출처부터 보자. 기록은 누가, 왜, 어떤 맥락에서 만들었는지가 중요하다. 인터넷 아카이브에서 이 관계는 끊어져 있다. 웹사이트 운영자가 기록을 "이관"한 적이 없다. 크롤러가 일방적으로 "포획"했다. 생산자와 수집자가 다르다. 동의도 없고, 절차도 없다.

원질서는 더 심각하다. 기록은 생산된 맥락과 구조 속에서 보존되어야 한다. Wayback Machine에서 2010년 뉴욕타임스를 열어보면 링크 절반은 깨져 있다. 댓글은 로드되지 않는다. 광고 영역은 비어 있다. 검색은 작동하지 않는다. 2010년에 그 페이지를 방문했던 경험과 전혀 다르다. 껍데기만 남았다.

진본성은 어떤가. 기록은 변경되지 않은 원본 상태여야 한다. 반면, WARC 파일에 저장된 것은 그 시점의 HTTP 응답이다. 바이트 단위로 동일하다. 그런데 그것을 렌더링하는 브라우저는 2025년 것이다. CSS 해석이 달라졌고, JavaScript 엔진이 바뀌었고, 폰트가 다르다. 화면에 보이는 것은 "원본"인가? 원본의 재현인가? 재현의 실패인가?

시간 문제도 있다. 전통적 아카이브는 시간의 연속성을 전제한다. 기록이 생산되고, 관리되고, 이관되는 흐름이 보존된다. 웹 아카이브는 다르다. 크롤러가 방문한 순간만 기록된다. 그 사이의 시간은 없다. 연속적인 타임라인이 아니라 단절된 스냅샷들. 웹 아카이브는 시간을 보존하지 않는다. 시간을 절단한다.

그렇다면 인터넷 아카이브는 아카이브가 아닌가? 아니면 기록학의 원칙들이 웹 시대에 맞지 않는 것인가?

## 원본을 지키는 것과 허물을 벗는 것

인터넷 아카이브의 필요성은 점점 커지고 있다. 전통적 아카이브 개념으로 웹을 담을 수 없다면, 개념을 확장하거나 새로운 개념이 필요하다. 인터넷 아카이브는 "사라지는 (웹) 문화에 대한 대응"이라는 기능적 정의로 자신을 정당화한다.

그러나 더 근본적인 질문이 있다. 이것이 "보존"의 문제인가?

하버드 도서관의 Dale Flecker는 이렇게 썼다[^24]: "미래 세대를 위해 디지털 자원을 유지하려면 의식적인 노력과 지속적인 투자가 필요하다(Keeping digital resources accessible for use by future generations will require conscious effort and continual investment)."

전통적 보존과 디지털 보존은 방향이 다르다. 전통적 보존은 원본을 그 자체로 유지하는 것이다. 서고를 짓고, 항온항습을 유지하고, 산성화를 막는다. 조건만 맞으면 물리적 객체는 수백 년을 버틴다. 디지털 보존은 다르다. 포맷이 바뀌고, 재생 환경이 바뀌고, 저장 매체가 바뀐다. 보존하려면 끊임없이 변환하고 이전해야 한다. 원본을 유지하는 게 아니라 주기적으로 새로운 형태로 옮겨가는 것이다.

그래서 웹 아카이빙은 마치 뱀이 허물을 벗으며 살아가는 것과 같다. 파일 포맷이 구식이 되면 새 포맷으로 변환하고(마이그레이션[^9]), 과거 브라우저에서만 작동하는 페이지는 그 환경을 재현해야 한다(에뮬레이션[^10]). 서버와 스토리지를 유지하고, 접근 경로가 바뀌면 메타데이터를 갱신한다. WARC 파일에 저장된 데이터는 그 자체로는 열어볼 수 없다. Wayback Machine 같은 재생 시스템이 있어야 비로소 웹페이지로 보인다.

이것은 보존이 아니라 유지(maintenance)다. 아니, 더 정확히 말하면 시간과 기술과 애정으로 가꾸어 나가는 돌봄(care)에 가깝다.

## 막대기 위의 1조 페이지

![One Trillion Web Pages Archived](https://blog.archive.org/wp-content/uploads/2025/08/TWWB_16_9_BANNER_1920.png)

2024년 10월, 인터넷 아카이브가 해킹당했다.[^11] 3,100만 개 계정 정보가 유출됐다. 해커는 사이트에 메시지를 남겼다: "인터넷 아카이브가 막대기 위에서 돌아가고 있다고 느낀 적 있는가? 언제든 보안 사고가 터질 것 같다고? 방금 터졌다(Have you ever felt like the Internet Archive runs on sticks and is constantly on the verge of suffering a catastrophic security breach? It just happened)."

같은 해, 4대 출판사가 인터넷 아카이브를 상대로 제기한 저작권 소송에서 인터넷 아카이브가 패소했다.[^12] 도서관이 소장한 물리적 책을 디지털로 대출하는 CDL(Controlled Digital Lending) 모델이 저작권 침해로 판결됐다. 전자책 대출 서비스의 법적 근거가 무너졌다. 음반사들의 소송도 진행 중이다. 해커만 인터넷 아카이브를 공격하는 게 아니다.

인터넷 아카이브는 비영리 단체다. 약 150명의 직원, 대부분 기부와 재단 지원으로 운영된다. 기부가 줄거나, 재단이 관심을 잃거나, 핵심 인력이 떠나면 1조 개의 웹페이지가 위험해진다.

그렇다면 누가 돌봄의 주체가 될 수 있을까? 미국에서는 아키비스트들이 직접 웹 아카이빙을 실천하려 한다. 워크숍[^23]에서 도구 사용법을 배우고, 웹 전문가가 아니어도 자기 손으로 웹을 저장한다. 한국은 다르다. 웹 아카이빙은 [OASIS](https://oasis.go.kr)[^13] 같은 국가 기관의 몫이다. 아키비스트 개인이 웹을 아카이빙한다는 발상 자체가 낯설다.

![NYC Archivists Round Table - Web Archiving Workshop](https://nycarchivists.org/resources/Pictures/Web%20Archiving.jpg)

## 완벽하지 않아도 일단 저장한다

인터넷 아카이브는 기성 아카이브의 실패를 보여준다. 출처도, 원질서도, 진본성도, 시간의 연속성도 보장하지 않는다. 기록학이 아카이브에 요구하는 것을 충족하지 못한다.

동시에 인터넷 아카이브는 아카이브가 무엇이어야 하는지 질문하게 만든다. 전통적 개념을 고수하면 웹은 아카이브될 수 없다. 웹의 속성—불안정성, 동적 변화, 분산된 생산—이 전통적 아카이브 개념과 충돌하기 때문이다. 그렇다면 개념을 바꿔야 하는가, 웹을 포기해야 하는가.

인터넷 아카이브는 세 번째 길을 선택했다. 완벽하지 않더라도 일단 저장한다. 불완전하더라도 접근 가능하게 만든다. 이것은 보존이 아니다. 사라짐의 지연이다.

우리는 웹을 아카이브한다고 믿지만, 실제로는 사라짐을 늦추고 있을 뿐이다. 그리고 그 지연조차 누군가의 돌봄에 의존한다.

---

## 각주

[^1]: [Heritrix](https://en.wikipedia.org/wiki/Heritrix)는 인터넷 아카이브가 개발한 오픈소스 웹 크롤러다. 시드(seed) URL에서 시작해 링크를 따라가며 재귀적으로 페이지를 수집한다.

[^2]: [WARC(Web ARChive)](https://en.wikipedia.org/wiki/WARC_(file_format))는 웹 아카이빙을 위한 국제 표준 파일 포맷(ISO 28500)이다. HTTP 요청/응답 헤더와 본문, 타임스탬프, 원본 URI, 무결성 해시 등을 함께 저장한다. 이전 포맷인 ARC를 대체했다.

[^3]: [robots.txt](https://en.wikipedia.org/wiki/Robots.txt)는 웹사이트 루트에 위치하는 텍스트 파일로, 검색엔진 크롤러나 웹 아카이브 수집기에게 어떤 페이지를 수집하지 말라고 지시한다. 법적 구속력은 없으나 대부분의 크롤러가 이를 존중한다.

[^5]: [퍼블릭 도메인(public domain)](https://ko.wikipedia.org/wiki/%ED%8D%BC%EB%B8%94%EB%A6%AD_%EB%8F%84%EB%A9%94%EC%9D%B8)은 저작권이 만료되었거나, 저작권자가 권리를 포기했거나, 애초에 저작권 보호 대상이 아닌 창작물을 가리킨다. 누구나 자유롭게 사용, 복제, 배포, 수정할 수 있다.

[^6]: [출처(provenance)](https://en.wikipedia.org/wiki/Provenance#Archival_science)는 기록학의 핵심 원칙이다. 기록은 그것을 생산한 개인이나 조직과의 관계 속에서 이해되어야 하며, 동일한 출처의 기록은 함께 유지되어야 한다.

[^7]: [원질서(original order)](https://en.wikipedia.org/wiki/Original_order)는 기록학의 핵심 원칙이다. 기록은 생산자가 만들고 사용한 원래의 배열과 구조를 유지해야 하며, 이를 통해 기록 간의 맥락적 관계가 보존된다.

[^8]: [진본성(authenticity)](https://dictionary.archivists.org/entry/authenticity.html)은 기록학에서 기록이 주장하는 바 그대로임을 증명할 수 있는 성질이다. 기록이 변경되지 않았고, 출처가 확인 가능하며, 신뢰할 수 있음을 의미한다.

[^9]: [마이그레이션(migration)](https://en.wikipedia.org/wiki/Digital_preservation#Migration)은 디지털 보존 전략의 하나다. 오래된 파일 포맷을 새로운 포맷으로 변환하여 접근성을 유지한다.

[^10]: [에뮬레이션(emulation)](https://en.wikipedia.org/wiki/Digital_preservation#Emulation)은 디지털 보존 전략의 하나다. 과거의 하드웨어나 소프트웨어 환경을 현대 시스템에서 모방하여 원본 파일을 원래 환경처럼 실행한다.

[^11]: 2024년 10월 9일, 인터넷 아카이브가 DDoS 공격과 데이터 유출을 동시에 당했다. Emma Bowman, "[Hackers steal information from 31 million Internet Archive users](https://www.npr.org/2024/10/20/nx-s1-5159000/internet-archive-hack-leak-wayback-machine)," *NPR*, 2024-10-21.

[^12]: [CDL(Controlled Digital Lending)](https://en.wikipedia.org/wiki/Controlled_digital_lending)은 도서관이 소장한 물리적 책 한 권당 디지털 사본 한 부를 한 번에 한 명에게만 대출하는 모델이다. 2024년 *Hachette v. Internet Archive* 항소심에서 저작권 침해로 최종 판결됐다.

[^13]: [OASIS](https://oasis.go.kr)는 국립중앙도서관이 운영하는 한국의 웹 아카이브 서비스(Online Archiving & Searching Internet Sources)다. 2004년부터 국내 웹 자원을 수집·보존하고 있다.

[^14]: 기억하지 "못하는" 게 아니라 "않는" 것이다. HTTP는 stateless—요청에 응답하고 끝난다. 버전 관리도, 히스토리도, 아카이빙도 웹의 기본 사양이 아니다. 팀 버너스리가 1989년에 제안한 것은 "정보 관리 시스템"이었지, "정보 보존 시스템"이 아니었다. 웹은 기억할 수 없는 게 아니라, 기억하도록 설계되지 않은 것이다.

[^15]: 2025년 10월 31일 달성. Internet Archive Blog, "[One Trillion Web Pages Archived](https://blog.archive.org/2025/10/31/one-trillion-web-pages-archived-internet-archive-celebrates-a-civilization-scale-milestone/)".

[^16]: 인터넷 아카이브는 논문이나 연구에 웹페이지를 인용할 경우, 링크가 사라질 것에 대비해 Save Page Now로 미리 저장해두라고 권장한다. "[How to use the Internet Archive](https://youtu.be/dCBy9z3f9Mw?t=247)" 영상 참고.

[^17]: 404 Not Found. HTTP 상태 코드 중 하나로, 서버가 요청한 페이지를 찾을 수 없을 때 반환한다. 웹에서 콘텐츠가 사라졌음을 알리는 가장 흔한 신호다.

[^18]: Wayback Machine에서 아카이브된 페이지를 열면 상단 배너에 표시되는 문구다.

[^19]: 2024년 6월 말, Paramount는 MTV News와 CMT 웹사이트의 아카이브를 삭제했다. 인터넷 아카이브가 MTV News 약 48만 페이지, CMT 약 7만 페이지를 보존하고 있었다. Todd Spangler, "[MTV News Archive Preserved on Internet Archive's Wayback Machine After Paramount Pulled the Plug](https://variety.com/2024/digital/news/mtv-news-articles-internet-archive-wayback-machine-1236058997/)," *Variety*, 2024-07-02.

[^20]: 2019년 3월 밝혀진 바에 따르면, Myspace는 서버 마이그레이션 과정에서 2003년부터 2015년 사이 업로드된 음악 파일을 손실했다. 공식 입장은 "서버 마이그레이션 중 파일이 손상되어 복구할 수 없다"였다. "[Myspace says it lost years of user-uploaded music](https://www.npr.org/2019/03/18/704458168/myspace-says-it-lost-years-of-user-uploaded-music)," *NPR*, 2019-03-18.

[^21]: 2024년 6월 26일, Paramount는 Comedy Central 웹사이트에서 25년 이상의 아카이브를 삭제했다. The Daily Show(1999–), The Colbert Report(2005–2014) 전 시즌이 포함됐다. Paramount+에는 최근 2시즌만 제공된다. "[Paramount Axes Comedy Central Website, Show Clips Library](https://latenighter.com/news/paramount-axes-comedy-central-website-show-clips-library/)," *LateNighter*, 2024-06-26.

[^22]: Vine은 2016년 10월 서비스 종료를 발표하고, 2017년 1월 앱을 중단했다. vine.co에 아카이브가 유지됐으나 2019년 4월 공식 폐쇄됐다. "[Vine (service)](https://en.wikipedia.org/wiki/Vine_(service))," *Wikipedia*.

[^23]: 2026년 5월, [뉴욕 아키비스트 라운드테이블](https://nycarchivists.org)이 개최하는 [웹 아카이빙 워크숍](https://nycarchivists.org/event-6665217). 이틀간 12시간, 참가비 20달러. 핵심 메시지는 "The web isn't forever, but it doesn't forget."

[^24]: Dale Flecker는 하버드 도서관 기획시스템 부관장(Associate Director for Planning and Systems)을 역임하며 디지털 보존 인프라를 설계했다. Dale Flecker, "[Preserving Scholarly E-Journals](https://www.dlib.org/dlib/september01/flecker/09flecker.html)," *D-Lib Magazine*, September 2001.

---

## 관찰 메모

- 2026-04-28: Vanishing Culture(2026) 보고서, Pew Research 데이터, 국제 기록학 연구 동향, 미국 아키비스트 교육 사례를 종합하여 초안 작성.

---

## 레퍼런스

- [Internet Archive](https://archive.org)
- [Wayback Machine](https://web.archive.org)
- [Heritrix (GitHub)](https://github.com/internetarchive/heritrix3)
- [OASIS (국립중앙도서관 웹 아카이브)](https://oasis.go.kr)
- Messarra, L., Freeland, C., & Ziskina, J. (2026). *Vanishing Culture: A Report on Our Fragile Cultural Record*. Internet Archive Press. ([link](https://archive.org/details/vanishing-culture-2026))
- Pew Research Center (2024). "When Online Content Disappears." ([link](https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/))
- Video Game History Foundation (2023). "87% of Classic Games Are Out of Print." ([link](https://gamehistory.org/87percent/))
- Brügger, N. (2018). *The Archived Web: Doing History in the Digital Age*. MIT Press.
- Maemura, E., Worby, N., Milligan, I., & Becker, C. (2018). "If These Crawls Could Talk: Studying and Documenting Web Archives Provenance." *JASIST*, 69(10): 1223-1233.
- Ruest, N., Fritz, S., & Milligan, I. (2022). "Creating order from the mess: web archive derivative datasets and notebooks." *Archives and Records*.
- Summers, E. (2020). "Appraisal Talk in Web Archives." *Archivaria*, 89(1): 70-102.
- NYC Archivists Round Table (2026). "Foundations of Web Archiving: Tools, Techniques, & Practice." ([link](https://nycarchivists.org/event-6665217))
