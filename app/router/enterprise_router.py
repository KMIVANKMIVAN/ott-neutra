from fastapi import APIRouter, Query, Body, Path, Depends
from typing import List

from app.services import enterpriseService
from app.schemas.enterprise_shema import (
    EnterpriseCreateSchema,
    EnterpriseUpdateSchema,
    EnterpriseResponseSchema,
)
from app.schemas.base_shema import BaseFilterShema

router = APIRouter(prefix="/enterprises", tags=["enterprises"])


@router.get(
    "/",
    response_model=List[EnterpriseResponseSchema],
    summary="API para obtener todas las empresas",
)
async def get_enterprise_all():
    return await enterpriseService.get_enterprise_all()


@router.get(
    "/search",
    response_model=List[EnterpriseResponseSchema],
    summary="API para obtener empresas por filtro (query params)",
)
async def get_enterprises_by_filter(
    filtros: BaseFilterShema = Depends()
):
    return await enterpriseService.get_enterprises_by_filter(filtros)


@router.get(
    "/{id}",
    response_model=EnterpriseResponseSchema,
    summary="API para obtener empresa por ID",
)
async def get_enterprise_by_id(
    id: int = Path(..., description="ID de la empresa")
):
    return await enterpriseService.get_enterprise_by_id(id)


@router.post(
    "/",
    response_model=EnterpriseResponseSchema,
    summary="API para crear una nueva empresa",
)
async def post_enterprise_create(
    empresa: EnterpriseCreateSchema = Body(
        ..., description="Datos necesarios para crear una nueva empresa"
    )
):
    return await enterpriseService.post_enterprise_create(empresa)


@router.patch(
    "/{id}",
    response_model=EnterpriseResponseSchema,
    summary="API para actualizar una empresa",
)
async def patch_enterprise_by_id_update(
    id: int,
    data: EnterpriseUpdateSchema = Body(...)
):
    return await enterpriseService.patch_enterprise_by_id_update(id, data)
