from pydantic import BaseModel
from typing import List
from datetime import date

class BillItem(BaseModel):
    item_name: str
    qty: int
    rate: float
    total: float

class BillResponse(BaseModel):
    hotel_name: str
    date: date
    order_id: int
    items: List[BillItem]
    total_bill: float
