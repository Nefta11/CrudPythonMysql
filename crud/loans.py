from sqlalchemy.orm import Session
import models.loans
import schemas.loans
from fastapi import HTTPException

def get_prestamo(db: Session, id: int):
    """Obtener un préstamo por ID."""
    return db.query(models.loans.Prestamo).filter(models.loans.Prestamo.id == id).first()

def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    """Obtener una lista de préstamos con paginación."""
    return db.query(models.loans.Prestamo).offset(skip).limit(limit).all()

def create_prestamo(db: Session, prestamo: schemas.loans.PrestamoCreate):
    """Crear un nuevo préstamo."""
    db_prestamo = models.loans.Prestamo(
        idUsuario=prestamo.idUsuario,
        idMaterial=prestamo.idMaterial,
        fechaPrestamo=prestamo.fechaPrestamo,
        fechaDevolucion=prestamo.fechaDevolucion,
        estadoPrestamo=prestamo.estadoPrestamo,
    )
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(db: Session, id: int, prestamo: schemas.loans.PrestamoUpdate):
    """Actualizar un préstamo existente."""
    db_prestamo = db.query(models.loans.Prestamo).filter(models.loans.Prestamo.id == id).first()
    if not db_prestamo:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    update_data = prestamo.dict(exclude_unset=True)  # Excluir campos no establecidos
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")
    for key, value in update_data.items():
        setattr(db_prestamo, key, value)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, id: int):
    """Eliminar un préstamo por ID."""
    db_prestamo = db.query(models.loans.Prestamo).filter(models.loans.Prestamo.id == id).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
