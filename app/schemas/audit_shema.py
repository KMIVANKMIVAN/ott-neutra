from pydantic import BaseModel, Field
from datetime import datetime  # <-- Corregido aquí


class BaseAuditSchema(BaseModel):
    status: bool = Field(..., description="Estado activo/inactivo")
    user_create: int = Field(..., description="ID del usuario que creó el registro")
    user_update: int = Field(..., description="ID del usuario que actualizó el registro")
    date_create: datetime = Field(..., description="Fecha en la que se creó el registro")
    date_update: datetime = Field(
        ..., description="Fecha en la que se actualizó el registro"
    )
