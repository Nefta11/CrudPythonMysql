import models.users
import schemas.users
from sqlalchemy.orm import Session


def get_user(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.users.User).offset(skip).limit(limit).all()


def get_user(db: Session, id: int):
    return db.query(models.users.User).filter(models.users.User, id=id).first()
