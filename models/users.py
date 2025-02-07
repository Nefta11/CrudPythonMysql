from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
import enum

class TipoUsuario(str, enum.Enum):
    """Enumeración para los tipos de usuario."""
    Alumno = "Alumno"
    Profesor = "Profesor"
    Secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Director = "Director"
    Administrativo = "Administrativo"

class Estatus(str, enum.Enum):
    """Enumeración para los estatus de usuario."""
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"
    
class User(Base):
    """Modelo de usuario para la base de datos."""
    __tablename__ = "tbb_users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60))
    primerApellido = Column(String(60))
    segundoApellido = Column(String(60))
    tipoUsuario = Column(Enum(TipoUsuario))
    nombreUsuario = Column(String(60))
    correoElectronico = Column(String(100))
    contrasena = Column(String(100))
    numeroTelefono = Column(String(20))
    estatus = Column(Enum(Estatus))
    fechaRegistro = Column(DateTime)
    fechaActualizacion = Column(DateTime)

