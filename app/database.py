from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # Adjust the import if necessary

DATABASE_URL = "sqlite:///fitness_management.db"  # Use SQLite for simplicity

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
