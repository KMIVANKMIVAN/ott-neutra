from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
from app.schemas import BaseAuditSchema


class SaleSchema(BaseAuditSchema):
    enterprise_id: int
    product_id: int
    sale_date: Optional[date] = None
    quantity: int

    @field_validator("sale_date", mode="before")
    @classmethod
    def default_today(cls, v):
        from datetime import date
        return v or date.today()


class SaleResponseSchema(BaseAuditSchema):
    sale_id: int
    enterprise_id: int
    product_id: int
    sale_date: Optional[date] = None
    quantity: int


class SaleCreateSchema(BaseModel):
    enterprise_id: int
    product_id: int
    sale_date: Optional[date] = None
    quantity: int

    @field_validator("sale_date", mode="before")
    @classmethod
    def default_today(cls, v):
        from datetime import date
        return v or date.today()


class SaleUpdateSchema(BaseModel):
    enterprise_id: Optional[int] = None
    product_id: Optional[int] = None
    sale_date: Optional[date] = None
    quantity: Optional[int] = None

    @field_validator("sale_date", mode="before")
    @classmethod
    def default_today(cls, v):
        from datetime import date
        return v or date.today()
