from pydantic import BaseModel, ConfigDict
from pydantic import BaseModel

class ItemNameUpdate(BaseModel):
    name: str

class ItemCreate(BaseModel):
    name: str
    rate: float

class ItemUpdate(BaseModel):
    rate: float

class ItemResponse(BaseModel):
    id: int
    name: str
    rate: float

    model_config = ConfigDict(from_attributes=True)
