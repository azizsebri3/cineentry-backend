from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None

class UserResponse(UserBase):
    id: int
    created_at: datetime | None = None

    model_config = {
    "from_attributes": True
}