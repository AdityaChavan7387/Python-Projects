from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import attendee_schema  
from app.services import attend_service

router = APIRouter(
prefix="/attend",
tags=["Attendance"]
)

@router.post("/", response_model=attendee_schema.AttendeeDTO)
def add_attendance(
    attendance: attendee_schema.AttendeeCreate,
    db: Session = Depends(get_db)
):
  
 return attend_service.create_attendance(db, attendance)
