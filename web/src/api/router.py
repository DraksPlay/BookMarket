from fastapi import APIRouter


router = APIRouter()


@router.get("/book", tags=["Book"])
async def get_book(user_id):
    return {"data": 1}