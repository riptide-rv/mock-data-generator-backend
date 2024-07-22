from fastapi import APIRouter, Depends
from typing import Annotated
from models.User import UserBase

import services.UserService as user_service

router = APIRouter(prefix="/users")

@router.get("/me/")
async def read_users_me(
    current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)],
):
    return current_user


@router.get("/me/items/")
async def read_own_items(
    current_user: Annotated[UserBase, Depends(user_service.get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]

