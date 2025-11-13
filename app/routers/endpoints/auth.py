from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...database import get_db
from ...schemas.user_schema import UserCreate, UserLogin, UserResponse
from ...services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_data.username, user_data.email, user_data.password)


@router.post("/login")
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user_credentials.email, user_credentials.password)
