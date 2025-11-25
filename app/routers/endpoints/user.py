from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.core.security import require_role
from app.schemas.user_schema import UserResponse, UserUpdate
from app.models.user import User
from app.services import user_service

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    """Get the current logged-in user's information."""
    return current_user

@router.get("/", response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    """List all users (admin only)."""
    return user_service.get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    """Get a user by ID (admin only)."""
    return user_service.get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    update_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    """Update user info (admin only)."""
    return user_service.update_user(db, user_id, update_data)

@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    """Delete a user by ID (admin only)."""
    return user_service.delete_user(db, user_id)

@router.put("/{user_id}/promote", response_model=UserResponse)
def promote_user_to_admin(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    """Promote a user to admin (admin only)."""
    return user_service.promote_user_to_admin(db, user_id)
