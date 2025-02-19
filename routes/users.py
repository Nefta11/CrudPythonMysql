from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.users
import config.db
import schemas.users
import models.users
from auth import create_access_token

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

@user.post("/login", tags=["Usuarios"])
def login(user: schemas.users.UserLogin, db: Session = Depends(get_db)):
    """
    Iniciar sesión y obtener un token JWT.
    Args:
        user (schemas.users.UserLogin): Objeto que contiene los datos de inicio de sesión del usuario.
        db (Session, optional): Sesión de la base de datos. Se obtiene automáticamente mediante la dependencia `Depends(get_db)`.
    Returns:
        dict: Un diccionario que contiene un mensaje de bienvenida y el token de acceso JWT.
    Raises:
        HTTPException: Si el correo electrónico o la contraseña son incorrectos, se lanza una excepción con código de estado 401.
    """
    """Iniciar sesión y obtener un token JWT."""
    db_user = crud.users.get_user_by_email(db, email=user.correoElectronico)
    if not db_user or db_user.contrasena != user.contrasena:
        raise HTTPException(status_code=401, detail="Correo electrónico o contraseña incorrectos")
    
    access_token = create_access_token(data={"sub": user.correoElectronico})
    return {"message": "Bienvenido, te has logeado exitosamente", "access_token": access_token}
