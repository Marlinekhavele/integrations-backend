from app.api.endpoints import dashboard, meta
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(meta.router, tags=["meta"])
api_router.include_router(dashboard.router, tags=["dashboard"])
