from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
from fastapi.params import Depends
from jose import jwt
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

from app.core.deps import get_current_user

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def require_role(required_role: str):
    """Return a dependency that checks the user's role."""
    def role_checker(current_user = Depends(get_current_user)):
        if current_user.role is None or current_user.role.name != required_role:
            raise HTTPException(
                status_code=
                status.HTTP_403_FORBIDDEN,
                detail=f"Access denied: requires {required_role} role"
            )
        return current_user
    return role_checker