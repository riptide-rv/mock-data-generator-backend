from sqlalchemy import Boolean, Column, String, UUID
from repositories.config import Base
from sqlalchemy import Uuid
import uuid

class User(Base):
    __tablename__  = "users"
    id = Column(Uuid, primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(200))
    disabled = Column(Boolean, default = False)
    