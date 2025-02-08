from fastapi import APIRouter
from app.api.endpoints import meta,events

api_router = APIRouter()
api_router.include_router(events.router, tags=["event"])
api_router.include_router(meta.router, tags=["meta"])
