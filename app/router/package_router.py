from fastapi import APIRouter, Query, Body
from typing import List

from app.services import packageService
from app.schemas.package_schema import (
    PackageCreateSchema,
    PackageUpdateSchema,
    PackageResponseSchema,
)
from app.schemas.base_shema import BaseFilterShema

router = APIRouter(prefix="/packages", tags=["packages"])


@router.get(
    "/all",
    response_model=List[PackageResponseSchema],
    summary="API para obtener todos los paquetes",
)
async def get_package_all():
    return await packageService.get_package_all()


@router.post(
    "/by-filter",
    response_model=List[PackageResponseSchema],
    summary="API para obtener paquetes por filtro",
)
async def get_packages_by_filter(
    filtros: BaseFilterShema = Body(..., description="Filtros para buscar paquetes")
):
    return await packageService.get_packages_by_filter(filtros)


@router.get(
    "/{id}",
    response_model=PackageResponseSchema,
    summary="API para obtener paquete por ID",
)
async def get_package_by_id(
    id: int = Query(..., description="ID del paquete")
):
    return await packageService.get_package_by_id(id)


@router.post(
    "/crear",
    response_model=PackageResponseSchema,
    summary="API para crear un nuevo paquete",
)
async def post_package_create(
    paquete: PackageCreateSchema = Body(
        ..., description="Datos necesarios para crear un nuevo paquete"
    )
):
    return await packageService.post_package_create(paquete)


@router.patch(
    "/update/{id}",
    response_model=PackageResponseSchema,
    summary="API para actualizar un paquete",
)
async def patch_package_by_id_update(
    id: int,
    data: PackageUpdateSchema = Body(...)
):
    return await packageService.patch_package_by_id_update(id, data)
