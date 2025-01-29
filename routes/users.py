from fastApi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.users
import config.db
import schemas.users
import models.users
from typing import List

user = APIRouter()

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()