from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import dept_schema
from app.services import dept_service
from app.auth.rbac import require_role

router = APIRouter(prefix="/departments", tags=["Departments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[dept_schema.DeptResponse],
            dependencies=[Depends(require_role("admin", "user"))])
def list_departments(db: Session = Depends(get_db)):
    return dept_service.get_all_depts(db)

@router.post("/", response_model=dept_schema.DeptResponse,
             dependencies=[Depends(require_role("admin"))])
def create_department(dept: dept_schema.DeptCreate, db: Session = Depends(get_db)):
    return dept_service.create_dept(db, dept.name)

@router.put("/{dept_id}",
             dependencies=[Depends(require_role("admin"))])
def update_department(dept_id: int, dept: dept_schema.DeptCreate, db: Session = Depends(get_db)):
    updated = dept_service.update_dept(db, dept_id, dept.name)
    if not updated:
        raise HTTPException(status_code=404)
    return updated

@router.delete("/{dept_id}",
                dependencies=[Depends(require_role("admin"))])
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    deleted = dept_service.delete_dept(db, dept_id)
    if not deleted:
        raise HTTPException(status_code=404)
    return {"message": "Deleted"}