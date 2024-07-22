from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean
from repositories import config


class UserBase(BaseModel):
    username: str
    disabled: bool = None

class UserInDB(UserBase):
    hashed_password: str
