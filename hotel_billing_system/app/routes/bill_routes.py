from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.bill_schema import BillResponse
from app.services import bill_service
from app.utils.db_session import get_db

router = APIRouter(tags=["Bill"])

@router.get("/{order_id}", response_model=BillResponse)
def get_bill(order_id: int, db: Session = Depends(get_db)):
    bill = bill_service.generate_bill(db, order_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Order not found")
    return bill
