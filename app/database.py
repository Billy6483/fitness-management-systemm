from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from .models import Base  # Adjust the import based on your project structure

DATABASE_URL = "sqlite:///fitness_management.db"  # Use SQLite for simplicity

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def check_alembic_version_table():
    inspector = inspect(engine)
    if 'alembic_version' not in inspector.get_table_names():
        # Create alembic_version table if it doesn't exist
        with engine.begin() as conn:
            conn.execute("""
            CREATE TABLE alembic_version (
                version_num VARCHAR(32) NOT NULL PRIMARY KEY
            );
            """)

def init_db():
    # Check if alembic_version table exists, create if it doesn't
    check_alembic_version_table()
    
    # Create all tables defined in Base
    Base.metadata.create_all(bind=engine)
