from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.materials
import schemas.materials
from config.db import SessionLocal
from dependencies import get_current_user
from models.users import User  # Importar el modelo de usuario

router = APIRouter()

def get_db():
    """Obtener una sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/materials/", response_model=List[schemas.materials.Material], tags=["Materiales"])
def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Obtener una lista de materiales."""
    materials = crud.materials.get_materials(db, skip=skip, limit=limit)
    materials_with_usernames = []
    for material in materials:
        user = db.query(User).filter(User.id == material.idUsuario).first()
        material_dict = material.__dict__.copy()
        material_dict['usuario'] = user.nombre if user else None
        materials_with_usernames.append(material_dict)
    return materials_with_usernames

@router.get("/materials/{material_id}", response_model=schemas.materials.Material, tags=["Materiales"])
def read_material(material_id: int, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Obtener un material por ID."""
    db_material = crud.materials.get_material(db, material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@router.post("/materials/", response_model=schemas.materials.Material, tags=["Materiales"])
def create_material(material: schemas.materials.MaterialCreate, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Crear un nuevo material."""
    user = db.query(User).filter(User.id == material.idUsuario).first()
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    db_material = crud.materials.create_material(db=db, material=material)
    material_dict = db_material.__dict__
    material_dict['usuario'] = user.nombre
    return material_dict

@router.put("/materials/{material_id}", response_model=schemas.materials.Material, tags=["Materiales"])
def update_material(material_id: int, material: schemas.materials.MaterialUpdate, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Actualizar un material existente."""
    if material.idUsuario:
        user = db.query(User).filter(User.id == material.idUsuario).first()
        if not user:
            raise HTTPException(status_code=400, detail="Usuario no encontrado")
    db_material = crud.materials.get_material(db, material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return crud.materials.update_material(db=db, id=material_id, material=material)

@router.delete("/materials/{material_id}", response_model=schemas.materials.Material, tags=["Materiales"])
def delete_material(material_id: int, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Eliminar un material por ID."""
    db_material = crud.materials.get_material(db, material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.delete_material(db=db, id=material_id)
