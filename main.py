from fastapi import FastAPI
from routes import users
from routes.materials import router as materials_router
from routes.loans import router as loans_router
from config.db import Base, engine

app = FastAPI(
    title="API de Usuarios",
    description="API de Usuarios de la Universidad",
    version="1.0.0"
)

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

# Incluir los routers
app.include_router(users.user)
app.include_router(materials_router, prefix="/api")
app.include_router(loans_router, prefix="/api")
