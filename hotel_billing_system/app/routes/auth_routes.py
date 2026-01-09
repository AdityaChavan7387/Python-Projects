from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user_schema import UserRegister, UserLogin
from app.services import user_service
from app.auth.jwt_utils import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    return user_service.register_user(db, user.username, user.password, user.role)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    auth_user = user_service.authenticate_user(db, user.username, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({
        "sub": auth_user.username,
        "role": auth_user.role
    })
    return {"access_token": token}