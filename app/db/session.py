from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL  # We'll define this in config.py

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL queries

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()