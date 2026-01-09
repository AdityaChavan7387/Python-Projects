from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.order_schema import (
    OrderCreate,
    OrderResponse
)
from app.schemas.order_item_schema import (
    OrderItemCreate,
    OrderItemResponse
)
from app.services import order_service
from app.utils.db_session import get_db

router = APIRouter(tags=["Orders"])

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return order_service.create_order(db, order)


@router.post("/{order_id}/items", response_model=OrderItemResponse)
def add_item_to_order(
    order_id: int,
    item: OrderItemCreate,
    db: Session = Depends(get_db)
):
    order_item = order_service.add_item_to_order(db, order_id, item)
    if not order_item:
        raise HTTPException(status_code=404, detail="Item not found")

    return {
        "item_name": "added",
        "quantity": order_item.quantity,
        "rate": order_item.rate,
        "total": order_item.total
    }
