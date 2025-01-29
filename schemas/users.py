from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    nombre: str
    primerApellido: str
    segundoApellido: str
    TipoUsuario: str
    nombreUsuario: str
    correoElectronico: str
    contrasena: str
    numeroTelefono: str
    estatus: str
    fechaRegistro: datetime
    fechaActualizacion: datetime