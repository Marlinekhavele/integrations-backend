from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.api.openapi import OpenApiDocumentation
import uvicorn


app = FastAPI(
    title="data-provider-service",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.openapi = OpenApiDocumentation(app).custom_openapi  # type: ignore
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

