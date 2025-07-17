from pydantic import BaseModel, Field, field_validator
from typing import Optional
from app.schemas import BaseAuditSchema


class ProductSchema(BaseAuditSchema):
    name: str = Field(..., min_length=1)
    price: float
    description: Optional[str] = None
    characteristics: Optional[str] = None

    @field_validator("description", "characteristics", mode="before")
    @classmethod
    def none_to_empty(cls, v):
        return v or ""


class ProductResponseSchema(BaseAuditSchema):
    product_id: int
    name: str
    price: float
    description: Optional[str] = None
    characteristics: Optional[str] = None


class ProductCreateSchema(BaseModel):
    name: str = Field(..., min_length=1)
    price: float
    description: Optional[str] = None
    characteristics: Optional[str] = None

    @field_validator("description", "characteristics", mode="before")
    @classmethod
    def none_to_empty(cls, v):
        return v or ""


class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    characteristics: Optional[str] = None

    @field_validator("description", "characteristics", mode="before")
    @classmethod
    def none_to_empty(cls, v):
        return v or ""
