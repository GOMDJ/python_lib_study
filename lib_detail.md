# Python 라이브러리 상세 설명

## 1단계: Python 내장 기초

### json
- **기능**: JSON 형식 데이터 직렬화/역직렬화
- **용도**: API 통신, 설정 파일, 데이터 저장
- **핵심**: `json.dumps()`, `json.loads()`, `json.dump()`, `json.load()`

### datetime
- **기능**: 날짜와 시간 처리
- **용도**: 타임스탬프, 날짜 계산, 시간대 변환
- **핵심**: `datetime.now()`, `timedelta`, `strftime()`, `strptime()`

### time
- **기능**: 시간 관련 저수준 함수
- **용도**: sleep, 성능 측정, 유닉스 타임스탬프
- **핵심**: `time.sleep()`, `time.time()`, `time.perf_counter()`

### os
- **기능**: 운영체제 관련 기능 (파일/디렉토리, 환경변수)
- **용도**: 파일 경로 조작, 환경변수 읽기, 프로세스 관리
- **핵심**: `os.path.join()`, `os.environ`, `os.listdir()`

### pathlib
- **기능**: 객체 지향적 파일 경로 처리 (os.path의 현대적 대체)
- **용도**: 파일/디렉토리 생성, 존재 확인, 경로 조작
- **핵심**: `Path()`, `.exists()`, `.mkdir()`, `.glob()`

### typing
- **기능**: 타입 힌팅 (코드에 타입 정보 명시)
- **용도**: 코드 가독성, IDE 자동완성, 런타임 검증(pydantic)
- **핵심**: `List`, `Dict`, `Optional`, `Union`, `Tuple`

### collections
- **기능**: 특수 컨테이너 자료구조
- **용도**: 데이터 집계, 큐/스택, 기본값 딕셔너리
- **핵심**: `Counter`, `defaultdict`, `deque`, `namedtuple`

### re
- **기능**: 정규표현식 패턴 매칭
- **용도**: 텍스트 검색, 치환, 추출, 검증
- **핵심**: `re.search()`, `re.findall()`, `re.sub()`, `re.match()`

### python-dotenv
- **기능**: .env 파일에서 환경변수 로드
- **용도**: API 키, DB 비밀번호 등 민감 정보 관리
- **핵심**: `load_dotenv()`, 환경변수 분리

### sys
- **기능**: 시스템 관련 파라미터와 함수
- **용도**: 커맨드라인 인자, 종료 코드, 파이썬 버전 확인
- **핵심**: `sys.argv`, `sys.exit()`, `sys.version`, `sys.path`

### subprocess
- **기능**: 외부 프로그램 실행 및 제어
- **용도**: git, docker 등 외부 명령어 실행, 파이프 처리
- **핵심**: `subprocess.run()`, `subprocess.Popen()`, 표준 입출력 캡처

### shutil
- **기능**: 고급 파일/폴더 작업
- **용도**: 파일 복사, 이동, 삭제, 압축/해제
- **핵심**: `shutil.copy()`, `shutil.move()`, `shutil.rmtree()`, `shutil.copytree()`, `shutil.make_archive()`

---

## 2단계: 데이터 처리 핵심

### numpy
- **기능**: 다차원 배열 연산 (수치 계산 기반)
- **용도**: 배열 연산, 선형대수, 통계, ML 기초
- **핵심**: 배열 생성, 인덱싱, 브로드캐스팅, 수학 함수

### pandas
- **기능**: 테이블 형태 데이터 분석 (엑셀 같은 느낌)
- **용도**: CSV/엑셀 읽기, 데이터 정제, 필터링, 그룹화
- **핵심**: `DataFrame`, `read_csv()`, `.loc[]`, `.groupby()`, `.merge()`

### matplotlib
- **기능**: 2D 그래프 시각화
- **용도**: 선 그래프, 막대 그래프, 히스토그램, 산점도
- **핵심**: `plt.plot()`, `plt.bar()`, `plt.scatter()`, `plt.savefig()`

---

## 3단계: 외부 통신 & 테스트

### requests
- **기능**: HTTP 요청/응답 (API 호출)
- **용도**: REST API 통신, 웹 페이지 다운로드, 파일 업로드
- **핵심**: `requests.get()`, `requests.post()`, 헤더/파라미터 설정

### pytest
- **기능**: 테스트 프레임워크
- **용도**: 단위 테스트, 통합 테스트, 자동화 테스트
- **핵심**: `assert`, `fixture`, `parametrize`, 테스트 발견

### logging
- **기능**: 로그 기록 및 관리
- **용도**: 디버깅, 에러 추적, 운영 모니터링
- **핵심**: `logging.info()`, 로그 레벨, 파일/콘솔 출력

---

## 4단계: 개발 환경 & 품질

### poetry
- **기능**: 프로젝트 의존성 관리 및 패키징
- **용도**: 가상환경 생성, 패키지 설치, 버전 관리
- **핵심**: `poetry init`, `poetry add`, `poetry.lock` 파일

### black
- **기능**: 자동 코드 포매터
- **용도**: 코드 스타일 통일 (들여쓰기, 줄바꿈, 따옴표)
- **핵심**: 설정 없이 일관된 포맷 강제

### ruff
- **기능**: 빠른 린터 (코드 품질 검사)
- **용도**: 버그 가능성, 스타일 위반, 안티패턴 검출
- **핵심**: flake8 + pylint 기능 통합, 매우 빠름

---

## 5단계: 웹 개발

### FastAPI
- **기능**: 현대적인 웹 프레임워크 (비동기 지원)
- **용도**: REST API 서버, 백엔드 개발
- **핵심**: 라우팅, 자동 문서화, Pydantic 통합, async

### uvicorn
- **기능**: ASGI 웹 서버 (FastAPI 실행)
- **용도**: FastAPI 애플리케이션 배포/실행
- **핵심**: 비동기 요청 처리, 리로드 기능

### pydantic
- **기능**: 데이터 검증 및 파싱
- **용도**: API 요청/응답 검증, 설정 관리
- **핵심**: 타입 기반 자동 검증, 명확한 에러 메시지

### python-multipart
- **기능**: 멀티파트 폼 데이터 파싱
- **용도**: FastAPI에서 파일 업로드 처리
- **핵심**: 이미지, 동영상 등 파일 수신

### SQLAlchemy
- **기능**: ORM (데이터베이스를 객체처럼 다룸)
- **용도**: DB 쿼리, 모델 정의, 관계 관리
- **핵심**: 모델 클래스, 세션, 쿼리 빌더

### alembic
- **기능**: 데이터베이스 마이그레이션 도구
- **용도**: 스키마 변경 이력 관리, 버전 관리
- **핵심**: `alembic revision`, `alembic upgrade`

### asyncio
- **기능**: 비동기 프로그래밍 (여러 작업 동시 처리)
- **용도**: I/O 대기 최적화, 동시성 처리
- **핵심**: `async/await`, 이벤트 루프, 코루틴

---

## 6단계: 비동기 통신

### httpx
- **기능**: 비동기 HTTP 클라이언트 (requests의 async 버전)
- **용도**: FastAPI 내에서 외부 API 호출
- **핵심**: `async with httpx.AsyncClient()`, 동기/비동기 모두 지원

### aiohttp
- **기능**: 비동기 HTTP 서버/클라이언트
- **용도**: 대량 HTTP 요청, 웹소켓, 비동기 서버
- **핵심**: `aiohttp.ClientSession()`, 웹소켓 지원

---

## 7단계: 특화 기능

### Pillow
- **기능**: 이미지 처리 라이브러리
- **용도**: 리사이징, 포맷 변환, 필터, 썸네일 생성
- **핵심**: `Image.open()`, `.resize()`, `.save()`

### BeautifulSoup4
- **기능**: HTML/XML 파싱
- **용도**: 웹 스크래핑, 데이터 추출
- **핵심**: `BeautifulSoup()`, `.find()`, `.select()`, CSS 선택자

---

## 8단계: 백그라운드 작업

### redis
- **기능**: 인메모리 데이터 저장소
- **용도**: 캐싱, 메시지 큐, 세션 저장
- **핵심**: 키-값 저장, pub/sub, 빠른 읽기/쓰기

### celery
- **기능**: 분산 작업 큐 (백그라운드 작업 처리)
- **용도**: 무거운 작업 비동기 실행, 스케줄링
- **핵심**: `@task` 데코레이터, 워커, 브로커(redis)

---

## 9단계: ML 기초

### scikit-learn
- **기능**: 전통적인 머신러닝 알고리즘
- **용도**: 분류, 회귀, 클러스터링, 전처리
- **핵심**: `fit()`, `predict()`, 파이프라인, 모델 평가

### PyTorch
- **기능**: 딥러닝 프레임워크
- **용도**: 신경망 구축, 학습, GPU 연산
- **핵심**: 텐서, autograd, `nn.Module`, 옵티마이저

---

## 선택 라이브러리

### 내장 라이브러리

#### argparse
- **기능**: 커맨드라인 인자 파싱
- **용도**: CLI 도구 제작, 스크립트 옵션 처리

#### functools
- **기능**: 고급 함수 도구
- **용도**: 데코레이터, 캐싱(`@lru_cache`), partial

#### itertools
- **기능**: 반복자 생성/조작
- **용도**: 조합, 순열, 무한 반복자, 체이닝

#### uuid
- **기능**: 고유 ID 생성
- **용도**: 데이터베이스 키, 파일명, 세션 ID

#### hashlib
- **기능**: 해시 생성 (MD5, SHA256 등)
- **용도**: 데이터 무결성 검증, 비밀번호 해싱

#### base64
- **기능**: Base64 인코딩/디코딩
- **용도**: 바이너리 데이터 텍스트 변환, 이미지 임베딩

#### sqlite3
- **기능**: SQLite 데이터베이스 내장 드라이버
- **용도**: 파일 기반 경량 DB, 로컬 데이터 저장

#### configparser
- **기능**: INI 파일 파싱
- **용도**: 설정 파일 읽기/쓰기

#### concurrent.futures
- **기능**: 멀티스레드/멀티프로세스 고수준 인터페이스
- **용도**: 병렬 처리, ThreadPoolExecutor, ProcessPoolExecutor

#### glob
- **기능**: 파일 패턴 매칭 (와일드카드)
- **용도**: `*.txt`, `**/*.py` 같은 패턴으로 파일 검색

---

### 웹 프레임워크

#### Flask
- **기능**: 경량 웹 프레임워크
- **용도**: 간단한 웹 앱, REST API
- **핵심**: 라우팅, 템플릿, 확장 가능

#### Django
- **기능**: 풀스택 웹 프레임워크
- **용도**: 대규모 웹 애플리케이션, 관리자 페이지
- **핵심**: ORM, 인증, 폼, 템플릿 엔진

#### starlette
- **기능**: ASGI 웹 프레임워크 (FastAPI 기반)
- **용도**: 저수준 비동기 웹 앱
- **핵심**: 라우팅, 미들웨어, 웹소켓

---

### 데이터 시각화

#### seaborn
- **기능**: 통계 시각화 (matplotlib 기반)
- **용도**: 예쁜 그래프, 통계 플롯, 히트맵

#### plotly
- **기능**: 인터랙티브 시각화
- **용도**: 웹용 대시보드, 3D 그래프, 줌/팬 기능

---

### 데이터베이스 드라이버

#### psycopg2
- **기능**: PostgreSQL 드라이버 (동기)
- **용도**: SQLAlchemy와 함께 PostgreSQL 연결

#### asyncpg
- **기능**: PostgreSQL 드라이버 (비동기)
- **용도**: 고성능 비동기 DB 쿼리

#### aiomysql
- **기능**: MySQL 드라이버 (비동기)
- **용도**: 비동기 MySQL 연결

#### pymongo
- **기능**: MongoDB 드라이버
- **용도**: NoSQL 문서 데이터베이스 조작

#### motor
- **기능**: MongoDB 비동기 드라이버
- **용도**: 비동기 MongoDB 연결 (asyncio 기반)

---

### 웹 크롤링 고급

#### selenium
- **기능**: 브라우저 자동화 (실제 브라우저 조작)
- **용도**: 동적 웹페이지 크롤링, 테스트 자동화

#### playwright
- **기능**: 최신 브라우저 자동화 (selenium보다 빠름)
- **용도**: headless 브라우저, 멀티 브라우저 지원

#### scrapy
- **기능**: 크롤링 프레임워크
- **용도**: 대규모 웹 스크래핑, 파이프라인, 미들웨어

---

### 파일 처리

#### openpyxl
- **기능**: 엑셀 파일 읽기/쓰기
- **용도**: .xlsx 파일 조작, 셀 스타일, 차트

#### PyPDF2
- **기능**: PDF 조작
- **용도**: PDF 병합, 분할, 텍스트 추출

#### pdfplumber
- **기능**: PDF 텍스트/표 추출 (PyPDF2보다 강력)
- **용도**: 정확한 표 데이터 추출

#### python-docx
- **기능**: Word 문서 생성/수정
- **용도**: .docx 파일 자동 생성, 텍스트 삽입

#### pyyaml
- **기능**: YAML 파일 읽기/쓰기
- **용도**: 설정 파일 관리 (.yml, .yaml)

---

### 웹 관련

#### jinja2
- **기능**: 템플릿 엔진
- **용도**: HTML 동적 생성, 이메일 템플릿

#### websockets
- **기능**: 웹소켓 통신
- **용도**: 실시간 양방향 통신 (채팅, 알림)

#### sse-starlette
- **기능**: Server-Sent Events
- **용도**: 서버→클라이언트 실시간 푸시

---

### 인증/보안

#### PyJWT
- **기능**: JWT 토큰 생성/검증
- **용도**: 사용자 인증, API 토큰

#### python-jose
- **기능**: JWT 대안 (더 많은 알고리즘 지원)
- **용도**: 보안 토큰 처리

#### passlib
- **기능**: 비밀번호 해싱
- **용도**: bcrypt, argon2 등 안전한 암호화

---

### 배포/모니터링

#### gunicorn
- **기능**: WSGI 서버 (Flask용)
- **용도**: 프로덕션 배포, 워커 관리

#### sentry-sdk
- **기능**: 에러 트래킹 서비스
- **용도**: 실시간 에러 모니터링, 스택 추적

#### prometheus-client
- **기능**: 메트릭 수집
- **용도**: 서버 모니터링, 성능 측정

---

### ML/딥러닝 고급

#### transformers
- **기능**: 사전학습 모델 (BERT, GPT 등)
- **용도**: NLP, 텍스트 생성, 임베딩

#### TensorFlow
- **기능**: 딥러닝 프레임워크 (PyTorch 대안)
- **용도**: 신경망, 프로덕션 배포

#### opencv-python
- **기능**: 컴퓨터 비전
- **용도**: 이미지/영상 처리, 객체 인식

#### librosa
- **기능**: 오디오 분석
- **용도**: 음성 처리, 음악 분석, 특징 추출

---

### API 클라이언트

#### openai
- **기능**: OpenAI API 클라이언트
- **용도**: GPT, DALL-E, Whisper 사용

#### anthropic
- **기능**: Claude API 클라이언트
- **용도**: Claude 모델 사용

#### stripe
- **기능**: 결제 처리
- **용도**: 카드 결제, 구독 관리

#### boto3
- **기능**: AWS SDK
- **용도**: S3, EC2, Lambda 등 AWS 서비스 제어

---

### 유틸리티

#### tqdm
- **기능**: 진행바 표시
- **용도**: 반복문 진행 상황 시각화

#### click
- **기능**: CLI 프레임워크 (argparse 대안)
- **용도**: 복잡한 명령줄 도구, 서브커맨드

#### rich
- **기능**: 터미널 꾸미기
- **용도**: 컬러 텍스트, 테이블, 진행바

#### schedule
- **기능**: 간단한 스케줄러
- **용도**: 주기적 작업 실행

#### APScheduler
- **기능**: 고급 스케줄러
- **용도**: cron, interval, date 스케줄링

---

## 분야별 추천 조합

### 데이터 분석/과학
**필수**: numpy, pandas, matplotlib  
**선택**: seaborn, plotly, scipy

### 웹 백엔드
**필수**: FastAPI, SQLAlchemy, redis  
**선택**: celery, jwt, sentry-sdk

### 크롤링/자동화
**필수**: requests, BeautifulSoup4  
**선택**: selenium, playwright, scrapy

### ML/AI
**필수**: numpy, pandas, scikit-learn  
**선택**: PyTorch, transformers, opencv

### CLI 도구
**필수**: argparse, json  
**선택**: click, rich, tqdm