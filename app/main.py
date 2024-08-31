from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# 데이터베이스 설정
Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

@app.on_event("startup")
async def startup():
    # DB 연결 및 초기화 작업
    pass

@app.on_event("shutdown")
async def shutdown():
    # DB 연결 종료 작업
    pass
