import models.users
import schemas.users
from sqlalchemy.orm import Session


def get_user(db: Session, id: int):
    return db.query(models.users.User).filter(models.users.User.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.users.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.users.UserCreate):
    db_user = models.users.User(
        nombre=user.nombre,
        primerApellido=user.primerApellido,
        segundoApellido=user.segundoApellido,
        tipoUsuario=user.tipoUsuario,
        nombreUsuario=user.nombreUsuario,
        correoElectronico=user.correoElectronico,
        contrasena=user.contrasena,
        numeroTelefono=user.numeroTelefono,
        estatus=user.estatus,
        fechaRegistro=user.fechaRegistro,
        fechaActualizacion=user.fechaActualizacion,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        update_data = user.dict(exclude_unset=True)  # Excluir campos no establecidos
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, id: int):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.nombreUsuario == usuario).first()
