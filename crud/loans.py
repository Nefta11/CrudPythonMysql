import models.loans
import schemas.loans
from sqlalchemy.orm import Session

def get_prestamo(db: Session, id: int):
    return db.query(models.loans.Prestamo).filter(models.loans.Prestamo.id == id).first()

def get_prestamos(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.loans.Prestamo).offset(skip).limit(limit).all()

def create_prestamo(db: Session, prestamo: schemas.loans.PrestamoCreate):
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
    db_prestamo = db.query(models.loans.Prestamo).filter(models.loans.Prestamo.id == id).first()
    if db_prestamo:
        update_data = prestamo.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_prestamo, key, value)
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, id: int):
    db_prestamo = db.query(models.loans.Prestamo).filter(models.loans.Prestamo.id == id).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
