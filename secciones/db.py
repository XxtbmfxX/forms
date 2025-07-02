import os
from sqlalchemy import create_engine

# Lee las variables de entorno para mayor seguridad
DB_USER = os.getenv("POSTGRES_USER", "usuario")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "contraseña")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "postgres")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            print("Conexión exitosa a la base de datos.")
            return True
    except Exception as e:
        print(f"Error de conexión: {e}")
        return False

if __name__ == "__main__":
    test_connection()
