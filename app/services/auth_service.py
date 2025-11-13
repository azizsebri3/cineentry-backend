from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.role import Role
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, username: str, email: str, password: str) -> User:
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    role = db.query(Role).filter(Role.name == "user").first()
    new_user = User(
    username=username,
    email=email,
    password_hash=hash_password(password),
    role=role
)

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


def login_user(db: Session, email: str, password: str) -> dict:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
