from app.core.config import settings
from fastapi import APIRouter

router = APIRouter(prefix="/host-api")

@router.post("/mint-token")
async def mint_token():
    return {"token": "testing"}



