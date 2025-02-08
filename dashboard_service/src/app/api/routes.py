from app.api.endpoints import meta
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(meta.router, tags=["meta"])
