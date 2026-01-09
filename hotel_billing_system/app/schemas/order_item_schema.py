from pydantic import BaseModel

class OrderItemCreate(BaseModel):
    item_id: int
    quantity: int

class OrderItemResponse(BaseModel):
    item_name: str
    quantity: int
    rate: float
    total: float
