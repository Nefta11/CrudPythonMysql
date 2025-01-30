# CrudPythonMysql

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
    source .\EntornoPY\Scripts\activate  # En Windows usa `venv\Scripts\activate`
    ```

2. Inicia el servidor FastAPI:
    ```bash
    uvicorn main:app --reload
    ```

3. Abre tu navegador y navega a `http://127.0.0.1:8000/docs` para acceder a la interfaz Swagger UI.

## Migraciones

1. Crea una nueva migración:
    ```bash
    alembic revision --autogenerate -m "mensaje"
    ```

2. Aplica la migración:
    ```bash
    alembic upgrade head
    ```

## Pruebas

1. Ejecuta las pruebas:
    ```bash
    pytest
    ```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
