from fastapi import APIRouter, Depends
from typing import Annotated
from models.User import User

import services.UserService as user_service

router = APIRouter()

@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(user_service.get_current_active_user)],
):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(user_service.get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]