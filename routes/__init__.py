from fastapi import APIRouter
from .authors import router as authors_router
from .books import router as books_router

router = APIRouter()
router.include_router(authors_router, prefix="/authors")
router.include_router(books_router, prefix="/books")