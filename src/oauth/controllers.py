from typing import Optional

from ninja import Router, Schema

from common.schemes import BaseOutSchema
from config.urls import app

# Create your views here.

router = Router()


class UserOut(BaseOutSchema):
    username: str
    password: str


@router.get("users", tags=["users"], response=UserOut)
def all_users(request):
    return {"users": "users"}


@router.post("users", tags=["users"])
def create_user(request):
    pass


@router.patch("user/{user_id}", tags=["users"])
def update_user(request, user_id: int):
    return {"data": user_id}


@router.delete("user/{user_id}", tags=["users"])
def delete_user(request, user_id: int):
    return {"data": user_id}
