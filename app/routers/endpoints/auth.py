from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ...database import get_db
from ...schemas.user_schema import UserCreate, UserLogin, UserResponse
from ...services.auth_service import register_user, login_user

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_data.username, user_data.email, user_data.password)


# 🚀 Swagger login: accepte "username" + "password" envoyés par OAuth2PasswordRequestForm
@router.post("/login")
def login_swagger(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # Swagger envoie "username" → toi tu utilises l'email
    return login_user(db, email=form_data.username, password=form_data.password)


# 🟩 Login JSON pour ton frontend (React/SPA/Postman)
@router.post("/login-json")
def login_json(user_credentials: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user_credentials.email, user_credentials.password)
