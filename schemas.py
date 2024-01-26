from pydantic import BaseModel,validator

def validate_disallowed_chars(value: str) -> str:
    if any(char in value for char in "`@$#%^&*="):
        raise ValueError("Disallowed character found")
    return value

class AuthorBase(BaseModel):
    name: str
    _validate_chars = validator('name', allow_reuse=True)(validate_disallowed_chars)


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
    @validator('title', 'summary', each_item=True)
    def validate_chars(cls, value):
        return validate_disallowed_chars(value)
class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

Author.update_forward_refs()
