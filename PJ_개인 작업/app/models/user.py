from sqlalchemy import Column, BigInteger, String, DateTime
from datetime import datetime 

class User(Base):
  __tablename__ = "USER"

  USER_ID = Column(BigInteger, primary_key=True)
  EMAIL = Column(String(30), unique=True, nullable=False)
  PASSWORD = Column(String(255), nullable=False)
  NICKNAME = Column(String(30), nullable=False)
  CREATED_AT = Column(DateTime, default=datetime.utcnow)