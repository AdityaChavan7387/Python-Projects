from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.auth.jwt_utils import decode_token

security = HTTPBearer()

def require_role(*roles):
    def role_checker(credentials=Depends(security)):
        token = credentials.credentials
        payload = decode_token(token)
        if payload.get("role") not in roles:
            raise HTTPException(status_code=403, detail="Access denied")
        return payload
    return role_checker