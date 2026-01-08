from sqlalchemy.orm import Session
from app.models.attendee_model import Attendee
from app.schemas import attendee_schema
from app.schemas.attendee_schema import AttendeeCreate

def create_attendance(db: Session, attendance: AttendeeCreate):
	db_attended = Attendee(
		name=attendance.name,
		mobile=attendance.mobile,
		email=attendance.email,
		is_attending=attendance.is_attending 
	)
	db.add(db_attended)
	db.commit()
	db.refresh(db_attended)
	return db_attended

