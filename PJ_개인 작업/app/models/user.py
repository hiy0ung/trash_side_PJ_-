from sqlalchemy import Column, BigInteger, String, DateTime, Identity
from datetime import datetime

from app.database.connection import Base

class User(Base):
  __tablename__ = "USER"

  USER_ID = Column(BigInteger, Identity(start=1), primary_key=True)
  EMAIL = Column(String(30), unique=True, nullable=False)
  PASSWORD = Column(String(255), nullable=False)
  NICKNAME = Column(String(30), nullable=False)
  CREATED_AT = Column(DateTime, default=datetime.utcnow)