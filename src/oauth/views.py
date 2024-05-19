from django.shortcuts import render
from ninja import Router
from config.urls import app


# Create your views here.

router = Router()


@router.get("/")
def index(request):
    return {"result": "workedwrer"}
