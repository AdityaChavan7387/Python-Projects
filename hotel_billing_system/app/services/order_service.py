from sqlalchemy.orm import Session
from app.models.order_model import Order
from app.models.order_item_model import OrderItem
from app.models.item_model import ItemMaster
from app.schemas.order_schema import OrderCreate
from app.schemas.order_item_schema import OrderItemCreate

def create_order(db: Session, order: OrderCreate):
    db_order = Order(
        hotel_name=order.hotel_name
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def add_item_to_order(
    db: Session,
    order_id: int,
    item_data: OrderItemCreate
):
    item = db.query(ItemMaster).filter(
        ItemMaster.id == item_data.item_id
    ).first()

    if not item:
        return None

    total = item_data.quantity * item.rate

    order_item = OrderItem(
        order_id=order_id,
        item_id=item.id,
        quantity=item_data.quantity,
        rate=item.rate,
        total=total
    )

    db.add(order_item)
    db.commit()
    db.refresh(order_item)
    return order_item
