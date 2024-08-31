import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# 데이터베이스 URL 설정
DATABASE_URL = os.getenv("DATABASE_URL")

# 추가적인 설정이 필요하다면 여기에 작성
