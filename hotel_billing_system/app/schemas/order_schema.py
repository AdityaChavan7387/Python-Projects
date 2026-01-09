from pydantic import BaseModel, ConfigDict
from datetime import date

class OrderCreate(BaseModel):
    hotel_name: str

class OrderResponse(BaseModel):
    order_id: int
    hotel_name: str
    order_date: date

    model_config = ConfigDict(from_attributes=True)
