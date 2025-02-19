from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from config.db import Base
import enum

class EstadoPrestamo(str, enum.Enum):
    """Enumeración para los estados de préstamo."""
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class Prestamo(Base):
    """Modelo de préstamo para la base de datos."""
    __tablename__ = "tbb_loans"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey("tbb_users.id"))
    idMaterial = Column(Integer, ForeignKey("tbb_materials.id"))
    fechaPrestamo = Column(DateTime)
    fechaDevolucion = Column(DateTime)
    estadoPrestamo = Column(Enum(EstadoPrestamo))
