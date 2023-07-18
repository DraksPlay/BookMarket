from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_session
from models import (User, Author, Category,
                    Book, Cart, Order)

router = APIRouter()


@router.get("/book", tags=["Book"])
async def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get("/books", tags=["Book"])
async def get_book(limit: int = 100, offset: int = 0, session: Session = Depends(get_session)):
    books = session.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books

