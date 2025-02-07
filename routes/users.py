from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.users
import config.db
import schemas.users
import models.users

user = APIRouter()

# Crear todas las tablas
models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """Obtener una sesión de base de datos."""
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/users/", response_model=List[schemas.users.User], tags=["Usuarios"])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtener una lista de usuarios."""
    db_users = crud.users.get_users(db, skip=skip, limit=limit)
    return db_users

@user.get("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
async def read_user(id: int, db: Session = Depends(get_db)):
    """Obtener un usuario por ID."""
    db_user = crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/users/", response_model=schemas.users.User, tags=["Usuarios"])
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    """Crear un nuevo usuario."""
    db_user = crud.users.get_user_by_usuario(db, usuario=user.nombreUsuario)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Usuario existente, intente nuevamente"
        )
    return crud.users.create_user(db=db, user=user)

@user.put("/users/{id}", response_model=schemas.users.User, tags=["Usuarios"])
async def update_user(id: int, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    """Actualizar un usuario existente."""
    db_user = crud.users.update_user(db=db, id=id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.delete("/users/{id}", response_model=schemas.users.User, tags=["Usuarios"])
async def delete_user(id: int, db: Session = Depends(get_db)):
    """Eliminar un usuario por ID."""
    db_user = crud.users.delete_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
