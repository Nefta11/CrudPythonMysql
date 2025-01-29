from fastapi import FastAPI
from routes.users import user

app = FastAPI(
    title="API de Usuarios",
    description="API de Usuarios de la Universidad",
    version="1.0.0"
)

app.include_router(user)
