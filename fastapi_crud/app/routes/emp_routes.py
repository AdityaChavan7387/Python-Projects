from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import emp_schema
from app.services import emp_service

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/", response_model=emp_schema.EmployeeOut)
def add_employee(
    employee: emp_schema.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return emp_service.create_employee(db, employee)

@router.get("/", response_model=List[emp_schema.EmployeeOut])
def list_employees(db: Session = Depends(get_db)):
    return emp_service.get_all_employees(db)
