from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from config.db import SessionLocal
import crud.users
from auth import decode_access_token

security = HTTPBearer()

def get_db():
    """Obtener una sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    """
    Obtener el usuario actual a partir del token JWT.

    Parámetros:
    - credentials (HTTPAuthorizationCredentials): Credenciales de autorización HTTP que contienen el token JWT.
    - db (Session): Sesión de la base de datos proporcionada por la dependencia.

    Retorna:
    - user (User): El usuario correspondiente al token JWT.

    Lanza:
    - HTTPException: Si el token es inválido o expirado (código de estado 401).
    - HTTPException: Si no se encuentra un usuario con el email proporcionado en el token (código de estado 401).
    """
    token = credentials.credentials
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    user = crud.users.get_user_by_email(db, email=payload.get("sub"))
    if user is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return user
