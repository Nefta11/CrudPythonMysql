from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
import enum

class TipoUsuario(str, enum.Enum):
    Alumno = "Alumno"
    Profesor = "Profesor"
    secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Director = "Director"
    Administrativo = "Administrativo"

class Estatus(str, enum.Enum):
    