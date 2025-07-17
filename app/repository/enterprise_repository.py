from typing import List, Optional
from sqlmodel import select
from app.core.database import get_session
from app.model.enterprise_model import EnterpriseModel
from app.schemas.enterprise_shema import EnterpriseCreateSchema, EnterpriseUpdateSchema
from app.schemas.base_shema import BaseFilterShema


async def get_enterprise_all() -> List[EnterpriseModel]:
    async for session in get_session():
        statement = select(EnterpriseModel)
        result = await session.exec(statement)
        return result.all()


async def get_enterprise_by_filter(filters: BaseFilterShema) -> List[EnterpriseModel]:
    async for session in get_session():
        statement = select(EnterpriseModel)
        if filters.status is not None:
            statement = statement.where(EnterpriseModel.status == filters.status)
        if filters.userCreate is not None:
            statement = statement.where(EnterpriseModel.userCreate == filters.userCreate)
        if filters.userUpdate is not None:
            statement = statement.where(EnterpriseModel.userUpdate == filters.userUpdate)
        if filters.dateCreate is not None:
            statement = statement.where(EnterpriseModel.dateCreate == filters.dateCreate)
        if filters.dateUpdate is not None:
            statement = statement.where(EnterpriseModel.dateUpdate == filters.dateUpdate)

        limit = filters.limit or 10
        offset = ((filters.page or 1) - 1) * limit
        statement = statement.offset(offset).limit(limit)

        result = await session.exec(statement)
        return result.all()


async def get_enterprise_by_id(id: int) -> Optional[EnterpriseModel]:
    async for session in get_session():
        statement = select(EnterpriseModel).where(EnterpriseModel.enterprise_id == id)
        result = await session.exec(statement)
        return result.first()


async def post_enterprise_create(data: EnterpriseCreateSchema) -> EnterpriseModel:
    async for session in get_session():
        db_enterprise = EnterpriseModel.model_validate(data)
        session.add(db_enterprise)
        await session.commit()
        await session.refresh(db_enterprise)
        return db_enterprise


async def patch_enterprise_by_id_update(id: int, data: EnterpriseUpdateSchema) -> Optional[EnterpriseModel]:
    async for session in get_session():
        statement = select(EnterpriseModel).where(EnterpriseModel.enterprise_id == id)
        result = await session.exec(statement)
        enterprise = result.first()

        if not enterprise:
            return None

        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(enterprise, key, value)

        session.add(enterprise)
        await session.commit()
        await session.refresh(enterprise)
        return enterprise


class EnterpriseRepository:
    get_enterprise_all = staticmethod(get_enterprise_all)
    get_enterprise_by_filter = staticmethod(get_enterprise_by_filter)
    get_enterprise_by_id = staticmethod(get_enterprise_by_id)
    post_enterprise_create = staticmethod(post_enterprise_create)
    patch_enterprise_by_id_update = staticmethod(patch_enterprise_by_id_update)


enterpriseRepository = EnterpriseRepository()
