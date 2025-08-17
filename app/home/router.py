
from typing import List
from fastapi import APIRouter, Depends
from fastapi_versioning import version
from prisma.models import User
from app.home.service import HomeService
from core.app import App

router = App.get_instance().create_router(prefix="/home")

@router.get("/")
async def root(service: HomeService = Depends(HomeService)):
    users = await service.get_all_users();
    return users  

App.get_instance().include_router(router)