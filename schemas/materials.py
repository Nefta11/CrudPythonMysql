from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TipoMaterial(str, Enum):
    """Enumeración para los tipos de material."""
    Canon = "Canon"
    Computadora = "Computadora"
    Extension = "Extension"

class EstadoMaterial(str, Enum):
    """Enumeración para los estados de material."""
    Disponible = "Disponible"
    Prestado = "Prestado"
    EnMantenimiento = "En Mantenimiento"

class MaterialBase(BaseModel):
    """Modelo base para los materiales."""
    tipoMaterial: TipoMaterial
    marca: str
    modelo: str
    estado: EstadoMaterial

class MaterialCreate(MaterialBase):
    """Modelo para la creación de materiales."""
    pass

class MaterialUpdate(BaseModel):
    """Modelo para la actualización de materiales."""
    tipoMaterial: Optional[TipoMaterial] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    estado: Optional[EstadoMaterial] = None

class Material(MaterialBase):
    """Modelo para representar un material con ID."""
    id: int
    class Config:
        from_attributes = True
