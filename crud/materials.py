import models.materials
import schemas.materials
from sqlalchemy.orm import Session

def get_material(db: Session, id: int):
    return db.query(models.materials.Material).filter(models.materials.Material.id == id).first()

def get_materials(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.materials.Material).offset(skip).limit(limit).all()

def create_material(db: Session, material: schemas.materials.MaterialCreate):
    db_material = models.materials.Material(
        tipoMaterial=material.tipoMaterial,
        marca=material.marca,
        modelo=material.modelo,
        estado=material.estado,
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, id: int, material: schemas.materials.MaterialUpdate):
    db_material = db.query(models.materials.Material).filter(models.materials.Material.id == id).first()
    if db_material:
        update_data = material.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_material, key, value)
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db: Session, id: int):
    db_material = db.query(models.materials.Material).filter(models.materials.Material.id == id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
