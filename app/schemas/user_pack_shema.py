from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
from app.schemas import BaseAuditSchema


class UserPackSchema(BaseAuditSchema):
    package_id: int
    user_id: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def none_to_null(cls, v):
        return v or None


class UserPackResponseSchema(BaseAuditSchema):
    user_pack_id: int
    package_id: int
    user_id: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class UserPackCreateSchema(BaseModel):
    package_id: int
    user_id: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def none_to_null(cls, v):
        return v or None


class UserPackUpdateSchema(BaseModel):
    package_id: Optional[int] = None
    user_id: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

    @field_validator("start_date", "end_date", mode="before")
    @classmethod
    def none_to_null(cls, v):
        return v or None
