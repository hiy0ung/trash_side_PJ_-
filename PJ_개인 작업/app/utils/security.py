# 비밀번호 암호화 전용

# 암호화 설정 객체 만드는 클래스
from passlib.context import CryptContext

# 비밀번호 암호화 관리 객체 생성
pwd_context = CryptContext(
  schemes=["bcrypt"], # 암호화 알고리즘 지정
  deprecated="auto", # bcrypt 최신 방식 자동 사용
)

# hash 사용한 비밀번호로 변경하는 함수
def hash_password(password: str):
  return pwd_context.hash(password)

# 사용자가 입력한 비밀번호, 해시 비밀번호 비교 함수
def verify_password(
  plain_password,
  hashed_password
):
  return pwd_context.verify(
    plain_password,
    hashed_password
  )
