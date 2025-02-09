from fastapi import APIRouter
from src.app.api.endpoints import dashboard, meta

api_router = APIRouter()
api_router.include_router(meta.router, tags=["meta"])
api_router.include_router(dashboard.router, tags=["dashboard"])
