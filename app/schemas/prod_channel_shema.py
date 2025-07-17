from pydantic import BaseModel, Field
from app.schemas import BaseAuditSchema


class ProdChannelSchema(BaseAuditSchema):
    product_id: int
    channel_id: int


class ProdChannelResponseSchema(BaseAuditSchema):
    product_id: int
    channel_id: int


class ProdChannelCreateSchema(BaseModel):
    product_id: int
    channel_id: int


class ProdChannelUpdateSchema(BaseModel):
    # Si algún campo fuera actualizable (poco común en tablas de relación), sería aquí.
    product_id: int
    channel_id: int
