from sqlmodel import Field
from datetime import datetime


class AuditModel:
    status: bool = Field(..., description="Estado activo/inactivo")
    user_create: int = Field(..., description="ID del usuario que creó el registro")
    user_update: int = Field(..., description="ID del usuario que actualizó el registro")
    date_create: datetime = Field(..., description="Fecha de creación")
    date_update: datetime = Field(..., description="Fecha de actualización")
