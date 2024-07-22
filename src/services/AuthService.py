import os
from dotenv import load_dotenv

from models.Token import Token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from typing import Annotated
from datetime import datetime, timedelta, timezone 
import jwt
import services.UserService as user_service
import dependencies

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")



async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
db) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return  Token(access_token=access_token, token_type="bearer")

async def signup(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db) -> Token:
    user = user_service.create_user(form_data.username, get_password_hash(form_data.password), db)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")



def authenticate_user(username: str, password: str, db):
    user = user_service.get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def verify_password(plain_password, hashed_password):
    return dependencies.pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return dependencies.pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
