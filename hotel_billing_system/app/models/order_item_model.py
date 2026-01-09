from sqlalchemy import Column, Integer, ForeignKey, Float
from app.database import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.order_id"),
        nullable=False
    )

    item_id = Column(
        Integer,
        ForeignKey("item_master.id"),
        nullable=False
    )

    quantity = Column(Integer, nullable=False)
    rate = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
