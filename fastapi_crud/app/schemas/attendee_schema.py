from pydantic import BaseModel, EmailStr

class AttendeeCreate(BaseModel):
    name: str
    mobile: str
    email: EmailStr
    is_attending: bool

class AttendeeDTO(AttendeeCreate):
    id: int

    class Config:
        from_attributes = True
