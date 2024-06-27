from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the connection URL for your PostgreSQL database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@localhost/postgres"

# Create an Engine instance for database interaction
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory for creating sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()
