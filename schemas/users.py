from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TipoUsuario(str, Enum):
    """Enumeración para los tipos de usuario."""
    Alumno = "Alumno"
    Profesor = "Profesor"
    Secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Director = "Director"
    Administrativo = "Administrativo"

class Estatus(str, Enum):
    """Enumeración para los estatus de usuario."""
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

class UserBase(BaseModel):
    """Modelo base para los usuarios."""
    nombre: str
    primerApellido: str
    segundoApellido: str
    tipoUsuario: TipoUsuario
    nombreUsuario: str
    correoElectronico: str
    contrasena: str
    numeroTelefono: str
    estatus: Estatus
    fechaRegistro: datetime
    fechaActualizacion: datetime
    
class UserCreate(UserBase):
    """Modelo para la creación de usuarios."""
    pass

class UserUpdate(BaseModel):
    """Modelo para la actualización de usuarios."""
    nombre: Optional[str] = None
    primerApellido: Optional[str] = None
    segundoApellido: Optional[str] = None
    tipoUsuario: Optional[TipoUsuario] = None
    nombreUsuario: Optional[str] = None
    correoElectronico: Optional[str] = None
    contrasena: Optional[str] = None
    numeroTelefono: Optional[str] = None
    estatus: Optional[Estatus] = None
    fechaRegistro: Optional[datetime] = None
    fechaActualizacion: Optional[datetime] = None

class User(UserBase):
    """Modelo para representar un usuario con ID."""
    id: int
    class Config:
        from_attributes = True
