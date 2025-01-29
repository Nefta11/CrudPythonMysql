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
        
@user.get("/users/", response_model=List[schemas.users.User], tags=["Usuarios"])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.users.get_user(db, skip=skip, limit=limit)
    return users