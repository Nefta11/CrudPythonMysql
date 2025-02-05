from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class EstadoPrestamo(str, Enum):
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class PrestamoBase(BaseModel):
    idUsuario: int
    idMaterial: int
    fechaPrestamo: datetime
    fechaDevolucion: datetime
    estadoPrestamo: EstadoPrestamo

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoUpdate(BaseModel):
    idUsuario: Optional[int] = None
    idMaterial: Optional[int] = None
    fechaPrestamo: Optional[datetime] = None
    fechaDevolucion: Optional[datetime] = None
    estadoPrestamo: Optional[EstadoPrestamo] = None

class Prestamo(PrestamoBase):
    id: int
    class Config:
        from_attributes = True
