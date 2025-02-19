from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from config.db import Base
import enum

class TipoMaterial(str, enum.Enum):
    """Enumeración para los tipos de material."""
    Canon = "Canon"
    Computadora = "Computadora"
    Extension = "Extension"

class EstadoMaterial(str, enum.Enum):
    """Enumeración para los estados de material."""
    Disponible = "Disponible"
    Prestado = "Prestado"
    EnMantenimiento = "En Mantenimiento"

class Material(Base):
    """Modelo de material para la base de datos."""
    __tablename__ = "tbb_materials"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipoMaterial = Column(Enum(TipoMaterial))
    marca = Column(String(60))
    modelo = Column(String(60))
    idUsuario = Column(Integer, ForeignKey("tbb_users.id"))
    estado = Column(Enum(EstadoMaterial))
