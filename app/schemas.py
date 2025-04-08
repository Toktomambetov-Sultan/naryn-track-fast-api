from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    username: str
    car_number: Optional[str] = None
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    car_number: Optional[str] = None
    is_admin: Optional[bool] = None


class UserResponse(BaseModel):
    id: int
    username: str
    car_number: Optional[str] = None
    is_password_changed: bool
    is_admin: bool

    class Config:
        from_attributes = True


class LoginData(BaseModel):
    username: str
    password: str


class ChangePasswordData(BaseModel):
    old_password: str
    new_password: str
