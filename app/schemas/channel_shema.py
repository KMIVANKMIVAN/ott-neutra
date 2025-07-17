from pydantic import BaseModel, Field, HttpUrl, field_validator
from typing import Optional
from app.schemas import BaseAuditSchema


class ChannelSchema(BaseAuditSchema):
    category_id: int
    name: str = Field(..., min_length=1)
    logo_url: Optional[str] = None

    @field_validator("logo_url", mode="before")
    @classmethod
    def none_to_empty(cls, v):
        return v or ""


class ChannelResponseSchema(BaseAuditSchema):
    channel_id: int
    category_id: int
    name: str
    logo_url: Optional[str] = None


class ChannelCreateSchema(BaseModel):
    category_id: int
    name: str = Field(..., min_length=1)
    logo_url: Optional[str] = None

    @field_validator("logo_url", mode="before")
    @classmethod
    def none_to_empty(cls, v):
        return v or ""


class ChannelUpdateSchema(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    logo_url: Optional[str] = None

    @field_validator("logo_url", mode="before")
    @classmethod
    def none_to_empty(cls, v):
        return v or ""
