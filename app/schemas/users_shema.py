from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from app.schemas import BaseAuditSchema


class UserSchema(BaseAuditSchema):
    email: EmailStr
    name: str = Field(..., min_length=1)
    ci: str = Field(..., min_length=5)
    enterprise_id: int


class UserResponseSchema(BaseAuditSchema):
    user_id: int
    enterprise_id: int
    email: EmailStr
    name: str
    ci: str


class user_createSchema(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1)
    ci: str = Field(..., min_length=5)
    enterprise_id: int


class user_updateSchema(BaseModel):
    name: Optional[str] = None
    ci: Optional[str] = None
    enterprise_id: Optional[int] = None
    email: Optional[EmailStr] = None  # solo si permites actualizar email
