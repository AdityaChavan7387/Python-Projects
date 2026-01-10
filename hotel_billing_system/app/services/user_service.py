from sqlalchemy.orm import Session
from app.models.user_model import User
from app.auth.security import hash_password, verify_password

def register_user(db: Session, username, password, role):
    user = User(
        username=username,
        password=hash_password(password),
        role=role
    )
    db.add(user)
    db.commit()
    return user

def authenticate_user(db: Session, username, password):
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.password): # type: ignore
        return user
    return None