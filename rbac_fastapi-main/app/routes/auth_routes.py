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
    new_user = user_service.register_user(
        db,
        user.username,
        user.password,
        user.role
    )

    token = create_access_token({
        "sub": new_user.username,
        "role": new_user.role
    })

    return {
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "role": new_user.role
        },
        "access_token": token
    }
    
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