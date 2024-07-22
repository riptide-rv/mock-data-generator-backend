from pydantic import BaseModel, Field
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean
from repositories import config
from uuid import UUID, uuid4

class UserBase(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    disabled: bool = None

class UserInDB(UserBase):
    hashed_password: str
