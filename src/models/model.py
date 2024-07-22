from sqlalchemy import Boolean, Column, String
from repositories.config import Base

class User(Base):
    __tablename__  = "users"
    username = Column(String(50), primary_key=True, index=True)
    hashed_password = Column(String(200))
    disabled = Column(Boolean, default = False)
    