from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL
DATABASE_URL = "postgresql+psycopg2://postgres:postgres123@127.0.0.1:5432/interviewflow"

# create database engine (core connection to postgreSQL)
engine = create_engine(DATABASE_URL)

# Session factory (used to talk to DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

# Dependency function to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()