from sqlalchemy.orm import Session
from app.models.emp_model import Employee
from app.schemas import emp_schema


def create_employee(db: Session, employee: emp_schema.EmployeeCreate):
    db_employee = Employee(ename=employee.ename)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee_by_id(db: Session, eid: int):
    return db.query(Employee).filter(Employee.eid == eid).first()

