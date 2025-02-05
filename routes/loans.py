from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.loans
import schemas.loans
from config.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/loans/", response_model=List[schemas.loans.Prestamo])
def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    prestamos = crud.loans.get_prestamos(db, skip=skip, limit=limit)
    return prestamos

@router.get("/loans/{prestamo_id}", response_model=schemas.loans.Prestamo)
def read_prestamo(prestamo_id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.loans.get_prestamo(db, prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo

@router.post("/loans/", response_model=schemas.loans.Prestamo)
def create_prestamo(prestamo: schemas.loans.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.loans.create_prestamo(db=db, prestamo=prestamo)

@router.put("/loans/{prestamo_id}", response_model=schemas.loans.Prestamo)
def update_prestamo(prestamo_id: int, prestamo: schemas.loans.PrestamoUpdate, db: Session = Depends(get_db)):
    db_prestamo = crud.loans.get_prestamo(db, prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return crud.loans.update_prestamo(db=db, id=prestamo_id, prestamo=prestamo)

@router.delete("/loans/{prestamo_id}", response_model=schemas.loans.Prestamo)
def delete_prestamo(prestamo_id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.loans.get_prestamo(db, prestamo_id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return crud.loans.delete_prestamo(db=db, id=prestamo_id)
