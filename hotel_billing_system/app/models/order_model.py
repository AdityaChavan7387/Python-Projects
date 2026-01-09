from sqlalchemy import Column, Integer, String, Date
from datetime import date
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String(150), nullable=False)
    order_date = Column(Date, default=date.today)
