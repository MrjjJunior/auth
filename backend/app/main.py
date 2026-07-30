from app.core.config import settings

from fastapi import FastAPI

from app.host_api.router import router as host_router
from app.journeys.selfservice.router import router as self_router

app = FastAPI()

app.include_router(host_router)
app.include_router(self_router)


@app.get("/")
def root():
    return {"status": "active"}


