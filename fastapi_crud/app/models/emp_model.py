from sqlalchemy import Column, Integer, String
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    eid = Column(Integer, primary_key=True, index=True)
    ename = Column(String(50), nullable=False)