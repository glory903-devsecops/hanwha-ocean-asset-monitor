from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Using SQLite for immediate local execution, but path is configurable for PostgreSQL
DATABASE_URL = "sqlite:///./asset_monitor.db"

from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
