# CrudPythonMysql

CrudPythonMysql es una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) construida con FastAPI y MySQL. Este proyecto sirve como un ejemplo de cómo construir una API RESTful utilizando FastAPI y SQLAlchemy para la gestión de la base de datos.

## Requisitos Previos

Asegúrate de tener instalados los siguientes componentes en tu sistema:
- Python 3.8 o superior
- MySQL
- Git

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/yourusername/CrudPythonMysql.git
    cd CrudPythonMysql
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. Actualiza la configuración de la base de datos en `config/db.py`:
    ```python
    SQLALCHEMY_DATABASE_URL = "mysql://<usuario>:<contraseña>@<host>:<puerto>/<base_de_datos>"
    ```

## Ejecutar la Aplicación

1. Activa el entorno virtual si no lo has hecho:
    ```bash
    .\EntornoPY\Scripts\activate  
    ```

2. Inicia el servidor FastAPI:
    ```bash
    uvicorn main:app --reload
    ```

3. Abre tu navegador y navega a `http://127.0.0.1:8000/docs` para acceder a la interfaz Swagger UI.

## APIs Disponibles

### Usuarios

- **GET /users/**: Obtiene una lista de usuarios.
- **POST /user/{id}**: Obtiene un usuario por su ID.
- **POST /users/**: Crea un nuevo usuario.
- **PUT /users/{id}**: Actualiza un usuario existente por su ID.
- **DELETE /users/{id}**: Elimina un usuario por su ID.

### Materiales

- **GET /materials/**: Obtiene una lista de materiales.
- **GET /materials/{material_id}**: Obtiene un material por su ID.
- **POST /materials/**: Crea un nuevo material.
- **PUT /materials/{material_id}**: Actualiza un material existente por su ID.
- **DELETE /materials/{material_id}**: Elimina un material por su ID.

### Préstamos

- **GET /loans/**: Obtiene una lista de préstamos.
- **GET /loans/{prestamo_id}**: Obtiene un préstamo por su ID.
- **POST /loans/**: Crea un nuevo préstamo.
- **PUT /loans/{prestamo_id}**: Actualiza un préstamo existente por su ID.
- **DELETE /loans/{prestamo_id}**: Elimina un préstamo por su ID.

## Estructura del Proyecto

El proyecto sigue la siguiente estructura de directorios:

```
CrudPythonMysql/
├── alembic/                 # Directorio de migraciones de Alembic
├── app/                     # Código fuente de la aplicación
│   ├── api/                 # Endpoints de la API
│   ├── core/                # Configuraciones y utilidades
│   ├── models/              # Modelos de la base de datos


