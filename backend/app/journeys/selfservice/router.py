from fastapi import APIRouter

router = APIRouter(
    prefix="/selfservice",
    tags=["Self Service"]
)


@router.get("/")
async def test():

    return {
        "message": "Self Service Works!"
    }
