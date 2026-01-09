from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import dept_schema
from app.services import dept_service

router = APIRouter(prefix="/departments", tags=["Departments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dept_schema.DeptResponse)
def create_department(dept: dept_schema.DeptCreate, db: Session = Depends(get_db)):
    return dept_service.create_dept(db, dept.name)

@router.get("/", response_model=list[dept_schema.DeptResponse])
def list_departments(db: Session = Depends(get_db)):
    return dept_service.get_all_dept(db)

@router.get("/{dept_id}", response_model=dept_schema.DeptResponse)
def get_department(dept_id: int, db: Session = Depends(get_db)):
    dept = dept_service.get_dept_by_id(db, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept

@router.put("/{dept_id}", response_model=dept_schema.DeptResponse)
def update_department(dept_id: int, dept: dept_schema.DeptCreate, db: Session = Depends(get_db)):
    updated = dept_service.update_dept(db, dept_id, dept.name)
    if not updated:
        raise HTTPException(status_code=404, detail="Department not found")
    return updated

@router.delete("/{dept_id}")
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    deleted = dept_service.delete_dept(db, dept_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Department not found")
    return {"message": "Department deleted"}