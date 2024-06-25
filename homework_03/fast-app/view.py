from fastapi import (
    APIRouter,
)

router = APIRouter(
    prefix="/ping",
    tags=["ping"],
)

@router.get("/", status_code=200)
def ping():
    return {
        "message": "pong",
    }
