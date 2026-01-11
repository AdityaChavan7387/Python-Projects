from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    qty: int
    rate: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True