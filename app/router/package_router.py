from fastapi import APIRouter, Query, Body, Path, Depends
from typing import List

from app.services import packageService
from app.schemas.package_shema import (
    PackageCreateSchema,
    PackageUpdateSchema,
    PackageResponseSchema,
)
from app.schemas.base_shema import BaseFilterShema

router = APIRouter(prefix="/packages", tags=["packages"])


@router.get(
    "/",
    response_model=List[PackageResponseSchema],
    summary="API para obtener todos los paquetes",
)
async def get_package_all():
    return await packageService.get_package_all()


@router.get(
    "/search",
    response_model=List[PackageResponseSchema],
    summary="API para obtener paquetes por filtro (query params)",
)
async def get_packages_by_filter(
    filtros: BaseFilterShema = Depends()
):
    return await packageService.get_packages_by_filter(filtros)


@router.get(
    "/{id}",
    response_model=PackageResponseSchema,
    summary="API para obtener paquete por ID",
)
async def get_package_by_id(
    id: int = Path(..., description="ID del paquete")
):
    return await packageService.get_package_by_id(id)


@router.post(
    "/",
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
    "/{id}",
    response_model=PackageResponseSchema,
    summary="API para actualizar un paquete",
)
async def patch_package_by_id_update(
    id: int,
    data: PackageUpdateSchema = Body(...)
):
    return await packageService.patch_package_by_id_update(id, data)
