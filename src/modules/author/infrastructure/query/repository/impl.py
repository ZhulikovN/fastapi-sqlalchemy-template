from pymfdata.rdb.repository import AsyncSession, BaseAsyncRepository
from sqlalchemy import select

from src.modules.author.domain.aggregate.id import AuthorId
from src.modules.author.infrastructure.query.dto import AuthorDTO
from src.modules.author.infrastructure.query.repository.protocol import (
    AuthorQueryRepository,
)


class AuthorAlchemyRepository(BaseAsyncRepository, AuthorQueryRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def fetch_id(self, _id: AuthorId) -> AuthorDTO:
        stmt = select(AuthorDTO).where(AuthorDTO.id == _id)

        result = await self.session.execute(stmt)
        print(result)
        return result.unique().scalars().one_or_none()

    async def fetch_by_id(self, _id: int) -> AuthorDTO:
        stmt = select(AuthorDTO).where(AuthorDTO.id == _id)

        result = await self.session.execute(stmt)
        return result.unique().scalars().one_or_none()
