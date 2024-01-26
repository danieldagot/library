from pydantic import BaseModel

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: list['Book'] = []

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    summary: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

Author.update_forward_refs()
