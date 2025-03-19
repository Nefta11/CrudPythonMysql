from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routes import users
from routes.materials import router as materials_router
from routes.loans import router as loans_router
from config.db import Base, engine
import os

app = FastAPI(
    title="API de Usuarios",
    description="API de Usuarios de la Universidad",
    version="1.0.0"
)

# Permitir peticiones desde http://localhost:5173/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

# Incluir los routers
app.include_router(users.user)
app.include_router(materials_router, prefix="/api")
app.include_router(loans_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
