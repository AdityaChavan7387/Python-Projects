from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base   

class Attendee(Base):
    __tablename__ = "attendees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    mobile = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    is_attending = Column(Boolean, default=False)
