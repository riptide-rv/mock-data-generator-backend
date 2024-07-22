from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from models.Token import Token
import services.AuthService as auth_service
from repositories.config import db_dependency


router = APIRouter()

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
) -> Token:
    
    return await auth_service.login_for_access_token(form_data, db=db)

@router.post("/signup")
async def signup(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    return await auth_service.signup(form_data, db)
    