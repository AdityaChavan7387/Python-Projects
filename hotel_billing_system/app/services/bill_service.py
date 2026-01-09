from sqlalchemy.orm import Session
from app.models.order_model import Order
from app.models.order_item_model import OrderItem
from app.models.item_model import ItemMaster

def generate_bill(db: Session, order_id: int):
    order = db.query(Order).filter(
        Order.order_id == order_id
    ).first()

    if not order:
        return None

    items = (
        db.query(OrderItem, ItemMaster)
        .join(ItemMaster, OrderItem.item_id == ItemMaster.id)
        .filter(OrderItem.order_id == order_id)
        .all()
    )

    bill_items = []
    total_bill = 0

    for order_item, item in items:
        bill_items.append({
            "item_name": item.name,
            "qty": order_item.quantity,
            "rate": order_item.rate,
            "total": order_item.total
        })
        total_bill += order_item.total

    return {
        "hotel_name": order.hotel_name,
        "date": order.order_date,
        "order_id": order.order_id,
        "items": bill_items,
        "total_bill": total_bill
    }
