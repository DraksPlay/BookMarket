from fastapi import APIRouter


router = APIRouter()


@router.get("/test")
async def get_book():
    return {"data": 1}