from fastapi import FastAPI

# db 연결 객체 가져오기 (engine - Postgre 연결, Base - 모델 부모 클래스)
from app.database.connection import Base, engine

from app.models.user import User

from app.routers.auth_router import router as auth_router

app = FastAPI()

# 모델 기반으로 테이블 생성
Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(auth_router)

# 서버 실행
# uvicorn main:app --reload

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs (API 테스트 가능, 버튼 클릭으로 요청 확인 가능)