from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class EstadoPrestamo(str, Enum):
    """Enumeración para los estados de préstamo."""
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class PrestamoBase(BaseModel):
    """Modelo base para los préstamos."""
    idUsuario: int
    idMaterial: int
    fechaPrestamo: datetime
    fechaDevolucion: datetime
    estadoPrestamo: EstadoPrestamo

class PrestamoCreate(PrestamoBase):
    """Modelo para la creación de préstamos."""
    pass

class PrestamoUpdate(BaseModel):
    """Modelo para la actualización de préstamos."""
    idUsuario: Optional[int] = None
    idMaterial: Optional[int] = None
    fechaPrestamo: Optional[datetime] = None
    fechaDevolucion: Optional[datetime] = None
    estadoPrestamo: Optional[EstadoPrestamo] = None

class Prestamo(PrestamoBase):
    """Modelo para representar un préstamo con ID."""
    id: int
    class Config:
        from_attributes = True
