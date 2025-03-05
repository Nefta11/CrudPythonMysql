from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.loans
import schemas.loans
from config.db import SessionLocal
from dependencies import get_current_user
from models.users import User
from models.materials import Material

router = APIRouter()

def get_db():
    """Obtener una sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/loans/", response_model=List[schemas.loans.Prestamo], tags=["Prestamos"])
def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Obtener una lista de préstamos."""
    prestamos = crud.loans.get_prestamos(db, skip=skip, limit=limit)
    prestamos_with_details = []
    for prestamo in prestamos:
        user = db.query(User).filter(User.id == prestamo.idUsuario).first()
        material = db.query(Material).filter(Material.id == prestamo.idMaterial).first()
        prestamo_dict = prestamo.__dict__
        prestamo_dict['nombreUsuario'] = user.nombre if user else None
        prestamo_dict['tipoMaterial'] = material.tipoMaterial if material else None
        prestamos_with_details.append(prestamo_dict)
    return prestamos_with_details

@router.get("/loans/{prestamo_id}", response_model=schemas.loans.Prestamo, tags=["Prestamos"])
def read_prestamo(prestamo_id: int, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Obtener un préstamo por ID."""
    db_prestamo = crud.loans.get_prestamo(db, prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo

@router.post("/loans/", response_model=schemas.loans.Prestamo, tags=["Prestamos"])
def create_prestamo(prestamo: schemas.loans.PrestamoCreate, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Crear un nuevo préstamo."""
    return crud.loans.create_prestamo(db=db, prestamo=prestamo)

@router.put("/loans/{prestamo_id}", response_model=schemas.loans.Prestamo, tags=["Prestamos"])
def update_prestamo(prestamo_id: int, prestamo: schemas.loans.PrestamoUpdate, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Actualizar un préstamo existente."""
    db_prestamo = crud.loans.get_prestamo(db, prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return crud.loans.update_prestamo(db=db, id=prestamo_id, prestamo=prestamo)

@router.delete("/loans/{prestamo_id}", response_model=schemas.loans.Prestamo, tags=["Prestamos"])
def delete_prestamo(prestamo_id: int, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Eliminar un préstamo por ID."""
    db_prestamo = crud.loans.get_prestamo(db, prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return crud.loans.delete_prestamo(db=db, id=prestamo_id)
