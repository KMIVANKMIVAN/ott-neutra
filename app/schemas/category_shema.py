from pydantic import BaseModel, Field
from typing import Optional
from app.schemas import BaseAuditSchema


class CategorySchema(BaseAuditSchema):
    name: str = Field(..., min_length=1)


class CategoryResponseSchema(BaseAuditSchema):
    category_id: int
    name: str


class CategoryCreateSchema(BaseModel):
    name: str = Field(..., min_length=1)


class CategoryUpdateSchema(BaseModel):
    name: Optional[str] = None
