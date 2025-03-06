from sqlalchemy.orm import Session
import models.materials
import schemas.materials

def get_material(db: Session, id: int):
    """Obtener un material por ID."""
    return db.query(models.materials.Material).filter(models.materials.Material.id == id).first()

def get_materials(db: Session, skip: int = 0, limit: int = 10):
    """Obtener una lista de materiales con paginación."""
    return db.query(models.materials.Material).offset(skip).limit(limit).all()

def create_material(db: Session, material: schemas.materials.MaterialCreate):
    """Crear un nuevo material."""
    db_material = models.materials.Material(
        tipoMaterial=material.tipoMaterial,
        marca=material.marca,
        modelo=material.modelo,
        estado=material.estado,
        idUsuario=material.idUsuario  # Añadir idUsuario al crear el material
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, id: int, material: schemas.materials.MaterialUpdate):
    """Actualizar un material existente."""
    db_material = db.query(models.materials.Material).filter(models.materials.Material.id == id).first()
    if db_material:
        update_data = material.dict(exclude_unset=True)  # Excluir campos no establecidos
        if update_data:  # Verificar si hay datos para actualizar
            for key, value in update_data.items():
                setattr(db_material, key, value)
            db.commit()
            db.refresh(db_material)
    return db_material

def delete_material(db: Session, id: int):
    """Eliminar un material por ID."""
    db_material = db.query(models.materials.Material).filter(models.materials.Material.id == id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
