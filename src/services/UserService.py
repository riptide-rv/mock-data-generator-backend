from typing import Annotated
from fastapi import Depends, HTTPException, status

from models.Token import TokenData
from models.User import UserBase

import repositories.UserRepository as user_repository
import jwt
from jwt import InvalidTokenError
from dependencies import oauth2_scheme
from repositories.config import db_dependency

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


    
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = user_repository.get_user(username=token_data.username, db=db)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[UserBase, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_user(username: str, db: db_dependency):
    return user_repository.get_user(username, db)

def create_user(username: str, password: str, db):
    duplicate_user_exception = HTTPException(status_code=400, detail="Username already registered")
    if get_user(username, db):
        raise duplicate_user_exception
    return user_repository.create_user(username, password, db)