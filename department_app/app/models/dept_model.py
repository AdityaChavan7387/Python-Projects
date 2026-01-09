from sqlalchemy import Column, Integer, String
from app.database import Base

class Department(Base):
    __tablename__ = "dept"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)