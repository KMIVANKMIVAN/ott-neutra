from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from app.schemas import BaseAuditSchema


class EnterpriseSchema(BaseAuditSchema):
    name: str = Field(..., min_length=1)
    nit: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    url_icon: Optional[str] = None
    color: Optional[str] = None
    rep_name: Optional[str] = None
    rep_email: Optional[EmailStr] = None
    rep_cellphone: Optional[str] = None

    @field_validator("nit", "address", "phone", "url_icon", "color", "rep_name", "rep_cellphone", mode="before")
    @classmethod
    def none_to_empty_str(cls, v):
        return v or ""


class EnterpriseResponseSchema(BaseAuditSchema):
    enterprise_id: int
    name: str
    nit: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    url_icon: Optional[str] = None
    color: Optional[str] = None
    rep_name: Optional[str] = None
    rep_email: Optional[EmailStr] = None
    rep_cellphone: Optional[str] = None


class EnterpriseCreateSchema(BaseModel):
    name: str = Field(..., min_length=1)
    nit: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    url_icon: Optional[str] = None
    color: Optional[str] = None
    rep_name: Optional[str] = None
    rep_email: Optional[EmailStr] = None
    rep_cellphone: Optional[str] = None

    @field_validator("nit", "address", "phone", "url_icon", "color", "rep_name", "rep_cellphone", mode="before")
    @classmethod
    def none_to_empty_str(cls, v):
        return v or ""


class EnterpriseUpdateSchema(BaseModel):
    name: Optional[str] = None
    nit: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    url_icon: Optional[str] = None
    color: Optional[str] = None
    rep_name: Optional[str] = None
    rep_email: Optional[EmailStr] = None
    rep_cellphone: Optional[str] = None

    @field_validator("nit", "address", "phone", "url_icon", "color", "rep_name", "rep_cellphone", mode="before")
    @classmethod
    def none_to_empty_str(cls, v):
        return v or ""
