
from fastapi import APIRouter
import schemas, crud
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from typing import List
from database import get_db

router = APIRouter()




@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.get("", response_model=List[schemas.Book])
def read_book(db: Session = Depends(get_db)):
    db_book = crud.get_books(db)
    return db_book

