from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BaseFilterShema(BaseModel):
    status: Optional[bool] = Field(None, description="Estado activo/inactivo")
    limit: Optional[int] = Field(10, ge=1, le=100, description="Cantidad de resultados por página")
    page: Optional[int] = Field(1, ge=1, description="Número de página")
    user_create: Optional[int] = Field(None, description="ID del usuario que creó el registro")
    user_update: Optional[int] = Field(None, description="ID del usuario que actualizó el registro")
    date_create: Optional[datetime] = Field(None, description="Fecha en la que se creó el registro")
    date_update: Optional[datetime] = Field(None, description="Fecha en la que se actualizó el registro")
