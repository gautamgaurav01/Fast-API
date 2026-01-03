# Import SQLAlchemy engine and ORM utilities
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings

DATABASE_URL = f"postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory for database interactions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# Base class for all SQLAlchemy models
class Base(DeclarativeBase):
    pass


# Dependency to provide a database session per request
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield session to the request
        yield db
    finally:
        # Close session after request completes
        db.close()
