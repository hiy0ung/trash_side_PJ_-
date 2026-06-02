# JWT 생성 / 검증

# timedeIta - 시간 더하는 객체 (timeIta(minutes=nn))
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 30분 뒤 만료
REFRESH_TOKEN_EXPIRE_DAYS = 7 # 7일 뒤 만료

# Access Token 생성 함수
def create_access_token(data: dict):

  to_encode = data.copy() # 원본 데이터 보호용 복사

  expire = datetime.utcnow() + timedelta(
    minutes=ACCESS_TOKEN_EXPIRE_MINUTES
  ) # 만료 시간은 현재 시간 + 30분

  to_encode.update({"exp": expire})
  # jwt 생성 시작
  encoded_jwt = jwt.encode(
    # jwt 안에 넣을 데이터
    to_encode,
    SECRET_KEY,
    algorithm=ALGORITHM

  )
  return encoded_jwt # 최종 jwt 문자열 반환

# Refresh Toekn 생성 함수
def create_refresh_token(data: dict):

  to_encode = data.copy()

  expire = datetime.utcnow() + timedelta(
    day=REFRESH_TOKEN_EXPIRE_DAYS
  ) 

  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(
    to_encode,
    SECRET_KEY,
    algorithm=ALGORITHM
  )

  return encoded_jwt
