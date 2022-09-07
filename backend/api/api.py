from fastapi import APIRouter

from api.endpoints import traininglogs

api_router = APIRouter()
api_router.include_router(traininglogs.router, prefix="/traininglogs", tags=["traininglogs"])
