
from fastapi import APIRouter
import schemas, crud
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from database import get_db
from typing import List

router = APIRouter()



@router.post("", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)

@router.get("/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author
@router.get("", response_model=List[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    db_authors = crud.get_authors(db)
    return db_authors

@router.post("/{author_id}/book", response_model=schemas.Book)
def create_book_for_author(
    author_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)
):
    # Check if the author exists
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        # If not, raise an HTTPException with a 404 status code
        raise HTTPException(status_code=404, detail="Author not found")
    
    # If the author exists, create the book using the CRUD function
    db_book = crud.create_author_book(db=db, book=book, author_id=author_id)
    return db_book


