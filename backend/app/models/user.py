from sqlalchemy import Column, Integer, String
from app.db.database import Base

# user table model
class user(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # Email must be unique for login
    email = Column(String, unique=True, index=True, nullable=False)