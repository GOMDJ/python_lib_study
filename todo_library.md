Tier 1: 무조건 알아야 함 (지금 당장)
1. requests

용도: HTTP 요청 (API 호출, 웹 크롤링)
왜 중요: 외부 API 연동 필수
배울 것:

GET, POST 요청
헤더, 파라미터 설정
응답 처리 (JSON)



pythonimport requests

# GET 요청
response = requests.get('https://api.example.com/data')
data = response.json()

# POST 요청
response = requests.post('https://api.example.com/create', 
                        json={'key': 'value'},
                        headers={'Authorization': 'Bearer token'})
2. json

용도: JSON 데이터 파싱/생성
왜 중요: API는 거의 다 JSON 씀
배울 것:

json.loads() (문자열 → 딕셔너리)
json.dumps() (딕셔너리 → 문자열)



pythonimport json

# 문자열 → 파이썬 객체
data = json.loads('{"name": "John", "age": 30}')

# 파이썬 객체 → 문자열
json_string = json.dumps({'name': 'John', 'age': 30})
3. datetime

용도: 날짜/시간 처리
왜 중요: 로그, 스케줄링, 데이터 필터링
배울 것:

현재 시간 가져오기
날짜 계산
포맷 변환



pythonfrom datetime import datetime, timedelta

# 현재 시간
now = datetime.now()

# 3일 후
future = now + timedelta(days=3)

# 포맷 변환
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
4. os / pathlib

용도: 파일/디렉토리 관리
왜 중요: 파일 업로드, 설정 파일 읽기
배울 것:

파일 존재 확인
경로 조작
환경 변수



pythonimport os
from pathlib import Path

# 환경 변수
api_key = os.getenv('API_KEY')

# 파일 존재 확인
if Path('data.json').exists():
    # 파일 읽기
    pass
5. dotenv (python-dotenv)

용도: 환경 변수 관리
왜 중요: API 키 같은 민감 정보 관리
배울 것:

.env 파일 로드



pythonfrom dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

Tier 2: 웹 개발 필수 (1개월 내)
6. FastAPI / Flask

용도: 백엔드 웹 프레임워크
왜 중요: SaaS 백엔드 만들기
추천: FastAPI (최신, 빠름, 문서 좋음)

pythonfrom fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/items")
def create_item(name: str):
    return {"name": name}
7. pydantic

용도: 데이터 검증
왜 중요: FastAPI랑 같이 씀, API 입력 검증
배울 것:

모델 정의
자동 검증



pythonfrom pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

# 자동으로 타입 체크, 검증
user = User(name="John", age=30, email="john@example.com")
8. SQLAlchemy / Databases

용도: 데이터베이스 ORM
왜 중요: DB 없이 SaaS 못 만듦
배울 것:

모델 정의
CRUD 작업
관계 설정



pythonfrom sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
9. asyncio

용도: 비동기 프로그래밍
왜 중요: FastAPI가 비동기 기반
배울 것:

async/await 기본
비동기 함수 호출



pythonimport asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())

Tier 3: 데이터 처리 (필요시)
10. pandas

용도: 데이터 분석, CSV/Excel 처리
왜 중요: 대시보드, 리포트 만들 때
배울 것:

DataFrame 다루기
필터링, 그룹화
CSV 읽기/쓰기



pythonimport pandas as pd

# CSV 읽기
df = pd.read_csv('data.csv')

# 필터링
filtered = df[df['age'] > 30]

# 그룹화
grouped = df.groupby('category').sum()
11. openpyxl / xlsxwriter

용도: Excel 파일 읽기/쓰기
왜 중요: 비즈니스 유저들이 Excel 씀
배울 것:

엑셀 읽기/쓰기
스타일링




Tier 4: AI/자동화 (너 강점)
12. openai

용도: OpenAI API 사용
왜 중요: AI 기능 넣을 때
배울 것:

Chat Completions API
스트리밍



pythonfrom openai import OpenAI

client = OpenAI(api_key="your-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
13. anthropic

용도: Claude API (이거)
왜 중요: Claude 활용한 기능

14. selenium / playwright

용도: 브라우저 자동화
왜 중요: 복잡한 웹 스크래핑, 자동화
배울 것:

페이지 열기
요소 클릭
스크린샷




Tier 5: 유틸리티 (알아두면 좋음)
15. collections

용도: 고급 자료구조
배울 것:

deque (양방향 큐)
Counter (카운팅)
defaultdict (기본값 딕셔너리)



pythonfrom collections import Counter, defaultdict

# 카운팅
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# Counter({'a': 3, 'b': 2, 'c': 1})

# 기본값 딕셔너리
d = defaultdict(list)
d['key'].append('value')  # KeyError 안 남
16. itertools

용도: 반복자 도구
배울 것:

combinations, permutations
chain, cycle



17. functools

용도: 함수형 프로그래밍 도구
배울 것:

@lru_cache (메모이제이션)
partial (부분 적용)



18. logging

용도: 로그 관리
왜 중요: 디버깅, 모니터링
배울 것:

로그 레벨 (DEBUG, INFO, ERROR)
파일 로깅



pythonimport logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("This is info")
logger.error("This is error")

Tier 6: 배포/운영 (나중에)
19. uvicorn

용도: FastAPI 서버 실행
왜 중요: 프로덕션 배포

20. python-multipart

용도: 파일 업로드 처리
왜 중요: 이미지, 문서 업로드

21. redis-py

용도: Redis 캐싱
왜 중요: 성능 최적화

학습 우선순위:
이번 달 (필수):

requests
json
datetime
os/pathlib
dotenv

다음 달 (웹 개발):

FastAPI
pydantic
SQLAlchemy
asyncio

3개월차 (프로젝트 고도화):

pandas (필요시)
openai/anthropic
logging
collections
