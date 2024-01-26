from fastapi import FastAPI, Depends, HTTPException,Request
from sqlalchemy.orm import Session
import crud, models, schemas
from typing import List

from database import SessionLocal, engine
from starlette.responses import JSONResponse


models.Base.metadata.create_all(bind=engine)
from routes import router as api_router
app = FastAPI()
app.include_router(api_router)
@app.middleware("http")
async def check_path(request: Request, call_next):
    # Check the request path is not a invalid string  
    path = request.url.path
    if any(char in path for char in "`@$#%^*"):
        return JSONResponse({"error": "format error"}, status_code=400)

    # If the path is valid, continue to the actual request handler
    response = await call_next(request)
    return response
 
# Dependency to get the DB session


def validate_disallowed_chars(value: str) -> str:
    if any(char in value for char in "`@$#%^&*="):
        raise ValueError("Disallowed character found")
    return value
