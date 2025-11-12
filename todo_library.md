## 1단계: Python 내장 기초 (1주)
json, datetime/time, os/pathlib/shutil
typing, collections, re
python-dotenv, sys, subprocess

## 2단계: 데이터 처리 핵심 (3주)
numpy → pandas → matplotlib

## 3단계: 외부 통신 & 테스트 (2주)
requests → pytest → logging

## 4단계: 개발 환경 & 품질 (1주)
poetry, black, ruff

## 5단계: 웹 개발 (4주)
FastAPI + uvicorn
pydantic + python-multipart
SQLAlchemy + alembic
asyncio

## 6단계: 비동기 통신 (1주)
httpx, aiohttp

## 7단계: 특화 기능 (2주)
Pillow, BeautifulSoup4

## 8단계: 백그라운드 작업 (2주)
redis, celery

## 9단계: ML 기초 (4주+)
scikit-learn → PyTorch 기초

---

## 선택 라이브러리 (필요시 추가)

### 내장 라이브러리
- **argparse** - CLI 도구 만들 때
- **functools** - 데코레이터, 고급 함수 패턴
- **itertools** - 반복자 조합/최적화
- **uuid** - 고유 ID 생성
- **hashlib** - 해시 생성 (MD5, SHA256)
- **base64** - 인코딩/디코딩
- **sqlite3** - 간단한 내장 DB
- **configparser** - ini 파일 파싱
- **concurrent.futures** - 멀티스레드/프로세스
- **glob** - 파일 패턴 매칭

### 데이터 시각화
- **seaborn** - matplotlib보다 예쁜 그래프
- **plotly** - 인터랙티브 시각화

### 웹 프레임워크
- **Flask** - 간단한 웹 프레임워크
- **Django** - 풀스택 프레임워크
- **starlette** - FastAPI 기반 저수준 프레임워크

### 데이터베이스 드라이버
- **psycopg2** or **asyncpg** - PostgreSQL
- **aiomysql** - MySQL (async)
- **pymongo** - MongoDB
- **motor** - MongoDB (async)

### 웹 크롤링 고급
- **selenium** - 브라우저 자동화 (느림)
- **playwright** - 최신 브라우저 자동화 (빠름)
- **scrapy** - 대규모 크롤링 프레임워크

### 파일 처리
- **openpyxl** - 엑셀 읽기/쓰기
- **PyPDF2** or **pdfplumber** - PDF 처리
- **python-docx** - Word 문서
- **pyyaml** - YAML 파일 읽기/쓰기

### 웹 관련
- **jinja2** - HTML 템플릿 엔진
- **websockets** - 웹소켓 통신
- **sse-starlette** - Server-Sent Events

### 인증/보안
- **jwt** (PyJWT) - JWT 토큰
- **python-jose** - JWT 대안
- **passlib** - 비밀번호 해싱
- **python-multipart** - 파일 업로드 (FastAPI)

### 배포/모니터링
- **gunicorn** - WSGI 서버 (Flask용)
- **sentry-sdk** - 에러 트래킹
- **prometheus-client** - 메트릭 수집

### ML/딥러닝 고급
- **transformers** - LLM 파인튜닝
- **TensorFlow** - PyTorch 대안
- **opencv-python** - 컴퓨터 비전
- **librosa** - 오디오 처리

### API 클라이언트
- **openai** - OpenAI API
- **anthropic** - Claude API
- **stripe** - 결제 연동
- **boto3** - AWS SDK

### 유틸리티
- **tqdm** - 진행바
- **click** - CLI 프레임워크 (argparse 대안)
- **rich** - 터미널 예쁘게
- **schedule** - 스케줄링 (간단)
- **APScheduler** - 스케줄링 (고급)

---

## 분야별 추천 조합

### 데이터 분석/과학
필수: numpy, pandas, matplotlib
선택: seaborn, plotly, scipy

### 웹 백엔드
필수: FastAPI, SQLAlchemy, redis
선택: celery, jwt, sentry-sdk

### 크롤링/자동화
필수: requests, BeautifulSoup4
선택: selenium, playwright, scrapy

### ML/AI
필수: numpy, pandas, scikit-learn
선택: PyTorch, transformers, opencv

### CLI 도구
필수: argparse, json
선택: click, rich, tqdm
