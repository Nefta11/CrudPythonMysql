from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TipoMaterial(str, Enum):
    Canon = "Canon"
    Computadora = "Computadora"
    Extension = "Extension"

class EstadoMaterial(str, Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    EnMantenimiento = "En Mantenimiento"

class MaterialBase(BaseModel):
    tipoMaterial: TipoMaterial
    marca: str
    modelo: str
    estado: EstadoMaterial

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(BaseModel):
    tipoMaterial: Optional[TipoMaterial] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    estado: Optional[EstadoMaterial] = None

class Material(MaterialBase):
    id: int
    class Config:
        from_attributes = True
