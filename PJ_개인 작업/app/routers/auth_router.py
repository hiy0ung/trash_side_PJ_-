# API (요청 받기 > service 호출, 응답 반환)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import SesscionLocal
from app.models.user import User
from app.schemas.user_schema import SignupRequest, LoginRequest
from app.services.auth_service import signup_service, login_service

from utils.security import verify_password
from utils.jwt_handler import (
  create_access_token,
  create_refresh_token
)

router = APIRouter()

# db 세선 생성/정리 함수
# 로그인 요청 들어올 때마다 Sesscion 생성 > db 작업 > 자동 close 
def get_db():
  db = SesscionLocal()

  try:
    yield db
  
  finally:
    db.close()

# 회원가입 API
@router.post("/signup")
def signup(
  request: SignupRequest, # 요청 들어온 body 미리 검증
  db: Session = Depends(get_db) # 의존성 주입 (db 세션 넣어줌)
):
  
  return signup_service(request, db)

# 로그인 API
@router.post("/login")
def login(
  request: LoginRequest, 
  db: Session = Depends(get_db) 
):
  
  return login_service(request, db)