from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from .models import Base  # Ensure this import path is correct

DATABASE_URL = "sqlite:///fitness_management.db"  # Use SQLite for simplicity

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def check_alembic_version_table():
    """Check if the alembic_version table exists; create it if it doesn't."""
    inspector = inspect(engine)
    if 'alembic_version' not in inspector.get_table_names():
        with engine.begin() as conn:
            conn.execute("""
            CREATE TABLE alembic_version (
                version_num VARCHAR(32) NOT NULL PRIMARY KEY
            );
            """)

def init_db():
    """Initialize the database, creating tables and the alembic_version table if necessary."""
    try:
        print("Initializing database...")
        check_alembic_version_table()
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")

# Optionally, you can add a function to get the session
def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
