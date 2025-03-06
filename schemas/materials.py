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
    idUsuario: int  # Añadir idUsuario para la creación

class MaterialUpdate(BaseModel):
    """Modelo para la actualización de materiales."""
    tipoMaterial: Optional[TipoMaterial] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    estado: Optional[EstadoMaterial] = None
    idUsuario: Optional[int] = None  # Añadir idUsuario como opcional

class Material(MaterialBase):
    """Modelo para representar un material con nombre de usuario."""
    id: int
    usuario: Optional[str] = None  # Añadir el nombre del usuario
    idUsuario: Optional[int] = None  # Hacer idUsuario opcional para la representación
    class Config:
        from_attributes = True
