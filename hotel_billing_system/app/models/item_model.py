from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class ItemMaster(Base):
    __tablename__ = "item_master"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    rate = Column(Float, nullable=False)
