from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
from app.schemas import BaseAuditSchema


class PackageSchema(BaseAuditSchema):
    enterprise_id: int
    total_credits: int
    used_credits: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def none_to_null(cls, v):
        return v or None


class PackageResponseSchema(BaseAuditSchema):
    package_id: int
    enterprise_id: int
    total_credits: int
    used_credits: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class PackageCreateSchema(BaseModel):
    enterprise_id: int
    total_credits: int
    used_credits: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def none_to_null(cls, v):
        return v or None


class PackageUpdateSchema(BaseModel):
    enterprise_id: Optional[int] = None
    total_credits: Optional[int] = None
    used_credits: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def none_to_null(cls, v):
        return v or None
