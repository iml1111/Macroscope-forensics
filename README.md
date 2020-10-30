# matzip-forensics
차세대 정보보안 리더 양성 프로그램 BEST OF THE BEST 6기 프로젝트
현장 기반 Mac 포렌식 도구(MACroscope) 개발

## 프로젝트 요약

최근 MAC OS (이하 OS X)사용자의 점유율이 급증함에 따라 MAC 포렌식 기술의 중요성이 대두되고 있으나 그에 반해 MAC 포렌식 산업의 발전이 부진 하다는 평을 많이 받고 있다. 실제로 기존의 포렌식 분석 도구들은 수사관이 현장에서 MAC 포렌식을 수행할 때, 우리나라의 증거 수집 정책인 선별압수에 배려가 되어있지 않고, 또 분석 도구 자체의 완성도나 현재 운영체제 버전과의 호환 문제 또한 거론되고 있다.

본 프로젝트는 이 문제점을 해결하기 위해 기존 MAC 포렌식 수행에 있어 이와 같은 문제점에 대해 분석 및 개선 방안을 도출하여 분석 도구의 사용성을 증대시키고, 현장수사 정책인 선별압수에 초점을 맞추어 효율적인 수사에 임할 수 있도록 돕는 분석 도구의 제작을 목표로 한다. 현장 기반 Mac 포렌식 도구는 OS X를 사용하는 기기를 현장에서 즉시 분석하여 선별 압수 진행을 자동화함으로 기존의 수사의 증거 수집 시간을 크게 단축시킬 수 있을 것이고 타겟 디스크 모드 및 PE환경에서의 증거 수집으로 무결성을 보존시키면서 온보드 형식으로 내장된 디스크를 직접 분해하지 않고 쉽게 데이터에 접근할 수 있도록 한다.

본 프로젝트를 수행함으로써, 향후 기업 및 수사기관에서 MAC 포렌식 수행에 있어 보다 효율적이고 신속한 수행이 가능할 것이라 기대한다.



## 운영 환경

본 분석 도구는 설치 프로그램으로 이동형 HDD 또는 USB 저장장치에 탑재하여 구동되며, 운영체제는 Win dows OS 및 Mac OS X 두 개를 모두 지원한다. 지원하는 버전은 다음과 같다.

\- Windows: Windows 7, Windows 8, 8.1, Windows 10

\- Mac OS X: OS X 10.9, 10.10, 10.11, 10.12
 \* 단 일부 버전의 경우 도구 내의 구동되지 않는 세부 기능이 있을 수 있다.

\- 메모리: 512Mbytes 이상



## System Architecture
![image](https://user-images.githubusercontent.com/29897277/97703497-12854b80-1af4-11eb-9d3c-1c7d5286c3e4.png)




## 기능 명세

디지털 포렌식 도구는 조사 대상 매체의 다양화에 대비하기 위하여 확장성 높게 S/W 컴퍼넌트를 접합할 수

있는 구조로 설계되어야 한다. 이를 위하여 유사한 기능을 계층화하여 계층 간 인터페이스를 만족하는 경우 어떤 컴포넌트도 정합할 수 있는 형태로 개발되어야 한다.

Macroscope의 프레임워크는 가상 접근 모듈(Virtual Access)과 분석 모듈(Analyzing), 현장 조사 모듈(Field I nvestigation), 획득 모듈(Acquisition)로 총 4개의 모듈로 구성된다. Macroscope 도구의 프레임워크는 다음 그림과 같다.

### 가상 접근 모듈

조사 대상 Device 가 로컬 접속 등을 통해 물리적 데이터를 읽기 위한 기능을 제공.

### 분석 모듈

(1) HFS/HFS+ 파일시스템을 분석하여 파일 및 디렉터리 목록 식별.
 (2) 파일에 투명하게 접근하기 위한 인터페이스 제공
 (3) 주요 수사 대상이 되는 문서 파일, 압축 파일, 등 사용자 생성 파일과 로그 및 히스토리 등 시스템 생성 파일에 대한 식별 작업 수행
 (4) 수사관이 주목할 만한 정보를 자동으로 분석하여 생성.

### 현장 수사 모듈

(1) 분석 모듈에서 식별한 파일에 대한 테이블 형태의 목록 보기 및 파일에 대한 부가 기능을 제공 (2) 파일 검색 및 정렬을 통하여 사건 유사 자료 식별.
 (3) 파일에 대한 HEX 코드, 그림, 텍스트 추출, 요약정보에 대한 뷰 기능
 (4) 수사 사건과 관련 있는 파일에 대한 북마크 기능

### 획득 모듈

(1) 수사 진행 결과에 대한 리포트 생성 기능
 (2) 추출한 데이터에 대한 목록 및 해시 생성
 (3) 북마크로 선택된 파일을 식별하여 논리적 이미지를 생성



## References

1) “디지털 증거의 수집,분석 및 관리 규정” 발행처: 대검찰청, 2016년, 개정 대검예규 제876호

2) 김범연 “Encase Basic 기술문서” 발행처: 경찰대학 사이버범죄 연구회 CRG, 2010년

3) Derrick J. Farmer. “A FORENSIC ANALYSIS OF THE WINDOWS REGISTRY”, 2008년 

4) “EnCase Portable Document" 발행처: Guidance Software, 2012년, EP BR 0130-12002 

5) “디지털 증거 처리 가이드라인” 발행처: 고려대학교 디지털포렌식연구센터

6) 강대명 “HFSX" 출처: http://www.forensic.kr/tc/(charsyam@naver.com)

7) 방승규 ”HFS+ 저널 파일 파싱 알고리즘을 이용한 삭제된 파일 복구 기법 향상 방안“ 발행처:
한국정보처리학회, 2016년, 정보처리학회논문지/컴퓨터 통신 시스템 제5권 제12호

8) 이경식 ”macOS 격리 기능을 이용한 악성코드 진입 경로 추정“ 발행처:Forensic Insight, 2015년

9) 이경식 ”Mac os X 디지털 포렌식 분석기법“ 발행처: 한국국방과학연구소, 2010년

10) The Sumuri RECON Team "RECON for Mac OS X Manual & Guide" 발행처: Sumuri, 2014년

11) Michael Cook ”Mac OS X Forensic Artifact Locations“ 발행처: Champlain College, 2015년

12) Sarah Edwards ”Analysis & Correlation of Mac Logs“ 출처:oompa@csh.rit.edu

13) 김주석 ”압수·수색 절차의 개선방안에 관한 연구“ 발행처:사법정책연구원, 2016년, 32-9741568-00089-01

14) 양승태 ”전원 합의체 결정“ 발행처: 대법원 2015년, 2011모1839

15) 김주석 ”디지털 증거의 증거능력 판단에 관한 연구“ 발행처: 사법정책연구원, 2014년, 32-9741568-000811-01

16) 원용기 ”디지털증거에 대한 계층적 접근 방안 연구“ 발행처: 서울대학교 융합과학기술대학원, 2016년

17) 신동휘 ”신규 운영체제 환경에서의 Forensic 기법 연구“ 발행처: 한국인터넷진흥원, 2012년

18) 이상미 ”관련성 없는 디지털증거 삭제시 이중해쉬를 이용한 무결성 입증 방안“ 발행처: 서울대학교 융합과학기술대학원, 2016년

19) 차한성 ”준항고 기각 결정에 재항고“ 발행처: 대법원, 2011년, 2009모1190

20) “mac-os-x-file-extensions“ 출처: https://www.file-extensions.org/mac-os-x-file-extensions

21) “Pincodes, Passcodes, & TouchID on iOS - An Introduction to the Aggregate Dictionary Database” https://www.mac4n6.com/blog/2017/3/12/introduction-to-the-aggregate-dictionary-database-addatastoresqlite, 2017년

22) “[Forensics] FAT32 파일추적 및 복구” 출처:http://ethan-ncs.tistory.com/41, 2017년

23) “How to Audit/log file access events on MAC OS X”, 2014년출처: https://community.spiceworks.com/topic/562291-how-to-audit-log-file-access-events-on-mac-os-x

24) “FILE SIGNATURES TABLE” 출처: https://www.garykessler.net/library/file_sigs.html, 2017년
