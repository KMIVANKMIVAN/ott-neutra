from fastapi import HTTPException

from app.repository import enterpriseRepository
from app.schemas.enterprise_shema import (
    EnterpriseCreateSchema,
    EnterpriseUpdateSchema,
    EnterpriseResponseSchema,
)
from app.schemas.base_shema import BaseFilterShema


async def get_enterprise_all() -> list[EnterpriseResponseSchema]:
    enterprise_data = await enterpriseRepository.get_enterprise_all()
    if not enterprise_data:
        raise HTTPException(status_code=404, detail="Sin empresas registradas")
    return [EnterpriseResponseSchema(**row) for row in enterprise_data]


async def get_enterprises_by_filter(filters: BaseFilterShema) -> list[EnterpriseResponseSchema]:
    enterprise_rows = await enterpriseRepository.get_enterprise_by_filter(filters)
    return [EnterpriseResponseSchema(**row) for row in enterprise_rows]


async def get_enterprise_by_id(id: int) -> EnterpriseResponseSchema:
    data = await enterpriseRepository.get_enterprise_by_id(id)
    if not data:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return EnterpriseResponseSchema(**data)


async def post_enterprise_create(data: EnterpriseCreateSchema) -> EnterpriseResponseSchema:
    new_data = await enterpriseRepository.post_enterprise_create(data)
    return EnterpriseResponseSchema(**new_data)


async def patch_enterprise_by_id_update(id: int, data: EnterpriseUpdateSchema) -> EnterpriseResponseSchema:
    updated_data = await enterpriseRepository.patch_enterprise_by_id_update(id, data)
    if not updated_data:
        raise HTTPException(status_code=404, detail="Empresa no encontrada o sin cambios")
    return EnterpriseResponseSchema(**updated_data)


class EnterpriseService:
    get_enterprise_all = staticmethod(get_enterprise_all)
    get_enterprises_by_filter = staticmethod(get_enterprises_by_filter)
    get_enterprise_by_id = staticmethod(get_enterprise_by_id)
    post_enterprise_create = staticmethod(post_enterprise_create)
    patch_enterprise_by_id_update = staticmethod(patch_enterprise_by_id_update)


enterpriseService = EnterpriseService()
