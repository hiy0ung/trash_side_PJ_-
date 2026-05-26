from fastapi import HTTPException

from models.user import User

from utils.security import hash_password
from utils.security import verify_password

from utils.jwt_handler import (
  create_access_token,
  create_refresh_token
)

def signup_service(request, db):

  # 이메일 존재 확인 조회
  exist_user = db.query(User).filter(
    User.EMAIL == request.email
  ).first()

  # 존재 했을 떄 400 오류 처리
  if exist_user:
    raise HTTPException(
      status_code=400,
      detail="이미 존재하는 이메일입니다."
    )
  
  # 비밀번호 암호화
  hashed_password = hash_password(
    request.password
  )

  new_user = User(
    EMAIL=request.email,
    PASSWORD=hashed_password, # 암호화된 비밀번호 저장
    NICKNAME=request.nickname
  )

  db.add(new_user)

  db.commit() # db 반영

  return {
    "message": "회원가입 성공했습니다."
  }

def login_service(request, db):

  # 테이블 조회하여 이메일 있나 필터 걸어주고, 조회 결과 중 제일 처음 거 가져오기
  user = db.query(User).filter(
    User.EMAIL == request.email
  ).first()

  # 이메일 존재하지 않으면 401 에러 발생
  if not user:
    raise HTTPException(
      status_code=401,
      detail="이메일 또는 비밀번호가 틀렸습니다."
    )
  
  # 비밀번호 검증 
  is_valid = verify_password(
    request.password, # 원본 비밀번호
    user.PASSWORD # db에 저장된 해시값
  )

# 비밀번호 맞지 않으면 401 에러 발생
  if not is_valid:
    raise HTTPException(
      status_code=401,
      detail="이메일 또는 비밀번호가 틀렸습니다."
    )
  
  # 로그인 되면서 토큰 생성 시작
  access_token = create_access_token(
    {"user_id": user.USER_ID}
  )

  refresh_token = create_refresh_token(
    {"user_id": user.USER_ID}
  )

  return {
    "access_token": access_token,
    "refresh_token": refresh_token
  }