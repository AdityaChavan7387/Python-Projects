from sqlalchemy.orm import Session
from app.models.dept_model import Department

def create_dept(db: Session, name: str):
    dept = Department(name=name)
    db.add(dept)
    db.commit()
    return dept

def get_all_depts(db: Session):
    return db.query(Department).all()

def get_dept_by_id(db: Session, dept_id: int):
    return db.query(Department).filter(Department.id == dept_id).first()

def update_dept(db: Session, dept_id: int, name: str):
    dept = get_dept_by_id(db, dept_id)
    if dept:
        dept.name = name
        db.commit()
    return dept

def delete_dept(db: Session, dept_id: int):
    dept = get_dept_by_id(db, dept_id)
    if dept:
        db.delete(dept)
        db.commit()
    return dept