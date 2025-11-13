from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserUpdate
from sqlalchemy.exc import SQLAlchemyError

def get_user_by_id(db: Session, user_id: int) -> User:
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")


def get_user_by_email(db: Session, email: str) -> User:
    try:
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")


def update_user(db: Session, user_id: int, update_data: UserUpdate) -> User:
    try:
        user = get_user_by_id(db, user_id)
        user.username = update_data.username or user.username
        user.email = update_data.email or user.email

        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update user")


def delete_user(db: Session, user_id: int):
    try:
        user = get_user_by_id(db, user_id)
        db.delete(user)
        db.commit()
        return {"detail": "User deleted successfully"}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to delete user")


def get_all_users(db: Session):
    try:
        return db.query(User).all()
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")
def promote_user_to_admin(db: Session, user_id: int) -> User:
    try:
        user = get_user_by_id(db, user_id)
        user.role = "admin"

        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to promote user")