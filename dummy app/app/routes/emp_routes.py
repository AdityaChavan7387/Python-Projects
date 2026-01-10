from fastapi import APIRouter
from app.services import emp_service

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)

@router.get("/")
def get_employees():
    return emp_service.list_employees()

@router.get("/{emp_id}")
def get_employee(emp_id: int):
    return emp_service.get_employee(emp_id)