from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from typing import List

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
from routes import router as api_router
app = FastAPI()
app.include_router(api_router)
# Dependency to get the DB session


