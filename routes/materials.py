from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.materials
import schemas.materials
from config.db import SessionLocal
from dependencies import get_current_user

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
    return materials

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
    return crud.materials.create_material(db=db, material=material)

@router.put("/materials/{material_id}", response_model=schemas.materials.Material, tags=["Materiales"])
def update_material(material_id: int, material: schemas.materials.MaterialUpdate, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Actualizar un material existente."""
    db_material = crud.materials.get_material(db, material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.update_material(db=db, id=material_id, material=material)

@router.delete("/materials/{material_id}", response_model=schemas.materials.Material, tags=["Materiales"])
def delete_material(material_id: int, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    """Eliminar un material por ID."""
    db_material = crud.materials.get_material(db, material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return crud.materials.delete_material(db=db, id=material_id)
