from fastapi import APIRouter, HTTPException, Query, Body, Depends
from typing import List

from app.services import userService

from app.schemas.users_shema import (
    UserResponseSchema,
    user_createSchema,
)
from app.schemas.base_shema import BaseFilterShema

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/",
    response_model=List[UserResponseSchema],
    summary="API para obtener todos los usuarios",
)
async def get_user_all():
    return await userService.get_user_all()


@router.get(
    "/search",
    response_model=List[UserResponseSchema],
    summary="API para obtener usuarios por filtro (query params)",
)
async def get_users_by_filter(filtros: BaseFilterShema = Depends()):
    return await userService.get_users_by_filter(filtros)


@router.get(
    "/by_email",
    response_model=UserResponseSchema,
    summary="API para obtener usuario por email",
)
async def get_user_by_email(
    email: str = Query(..., description="Correo electrónico del usuario")
):
    return await userService.get_user_by_email(email)


@router.post(
    "/",
    response_model=UserResponseSchema,
    summary="API para crear un nuevo usuario",
)
async def post_user_create(
    usuario: user_createSchema = Body(
        ..., description="Datos necesarios para crear un nuevo usuario"
    )
):
    return await userService.post_user_create(usuario)
