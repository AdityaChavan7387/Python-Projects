from pydantic import BaseModel

class DeptCreate(BaseModel):
    name: str

class DeptResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True