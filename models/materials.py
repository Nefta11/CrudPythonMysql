from sqlalchemy import Column, Integer, String, Enum
from config.db import Base
import enum

class TipoMaterial(str, enum.Enum):
    Canon = "Canon"
    Computadora = "Computadora"
    Extension = "Extension"

class EstadoMaterial(str, enum.Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    EnMantenimiento = "En Mantenimiento"

class Material(Base):
    __tablename__ = "tbb_materials"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipoMaterial = Column(Enum(TipoMaterial))
    marca = Column(String(60))
    modelo = Column(String(60))
    estado = Column(Enum(EstadoMaterial))
    # idUsuario = Column(Integer, ForeignKey("tbb_users.id"))
