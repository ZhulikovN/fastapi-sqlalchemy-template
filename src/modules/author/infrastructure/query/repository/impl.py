from typing import List

from pymfdata.rdb.repository import AsyncSession, BaseAsyncRepository
from sqlalchemy import select

from src.modules.author.infrastructure.query.dto import AuthorDTO
from src.modules.author.infrastructure.query.repository.protocol import (
    AuthorQueryRepository,
)


class AuthorAlchemyRepository(BaseAsyncRepository, AuthorQueryRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def fetch_by_author_first_name(self, first_name: str) -> List[AuthorDTO]:
        stmt = select(AuthorDTO).where(AuthorDTO.first_name == first_name)
        result = await self.session.execute(stmt)
        return result.unique().scalars().all()

    async def fetch_by_id(self, _id: int) -> AuthorDTO:
        stmt = select(AuthorDTO).where(AuthorDTO.id == _id)

        result = await self.session.execute(stmt)
        return result.unique().scalars().one_or_none()
