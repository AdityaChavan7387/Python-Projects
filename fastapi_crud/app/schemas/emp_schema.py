from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    ename: str

class EmployeeOut(BaseModel):
    eid: int
    ename: str

    class Config:
        orm_mode = True