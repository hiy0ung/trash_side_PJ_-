# API 요청 검사용
from pydantic import BaseModel

class SignupRequest(BaseModel):
  email: str
  password: str
  nickname: str

class LoginRequest(BaseModel):
  email: str
  password: str