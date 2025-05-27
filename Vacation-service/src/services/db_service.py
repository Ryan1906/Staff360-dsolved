from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cambia la URL de conexión según tu configuración
DATABASE_URL = "mysql+pymysql://root:12345@localhost/staff360"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()