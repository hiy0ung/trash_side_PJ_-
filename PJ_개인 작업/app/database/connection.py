# FastAPI <-> PostgreSQL 연결 통로 만들기
from sqlalchemy import create_engine
# model의 부모 클래스 생성(class User(Base)~ 에서 Base 생성)
from sqlalchemy.ext.declarative import declarative_base
# DB 작업용 Session 생성 (DB연결, 쿼리 실행, 저장(commit), 조회(select))
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgre://유저명:비밀번호@localhost:포트번호/DB명"

DATABASE_URL = "postgresql://hayoung:gkdud989898!@localhost:5432/trash_diary_개인"

# 실제 내 DB 주소로 실제 연결 엔진 생성
engine = create_engine(DATABASE_URL)

# DB 작업 객체 만드는 설정
SessionLocal = sessionmaker(
  autocommit=False, # 자동 저장 금지 (db.add(user)로 바로 저장 안됨 > db.commit 해야됨)
  autoflush=False, # 자동으로 DB 반영 하는 기능 끔
  bind=engine # session이 어떤 engine 쓸 건지 연결 하는 것
)

# Base 생성
Base = declarative_base()