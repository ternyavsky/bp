from ninja import Router

from config.urls import app

# Create your views here.

router = Router()


@router.get("users", tags=["users"])
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


@router.get("/user", tags=["users"])
def index(request):
    return {"result": "default"}
