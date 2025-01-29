# CrudPythonMysql

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CrudPythonMysql.git
    cd CrudPythonMysql
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Update the database configuration in `config/db.py`:
    ```python
    SQLALCHEMY_DATABASE_URL = "mysql://<username>:<password>@<host>:<port>/<database>"
    ```

## Running the Application

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI.

## Migrations

1. Create a new migration:
    ```bash
    alembic revision --autogenerate -m "message"
    ```

2. Apply the migration:
    ```bash
    alembic upgrade head
    ```

## Testing

1. Run the tests:
    ```bash
    pytest
    ```

## License

This project is licensed under the MIT License.
