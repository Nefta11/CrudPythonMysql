from fastapi import APIRouter, HTTPException, Depends
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
    db_users = crud.users.get_user(db, skip=skip, limit=limit)
    return db_users


@user.get("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
async def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
