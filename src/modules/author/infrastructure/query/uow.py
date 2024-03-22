from pymfdata.rdb.connection import AsyncEngine
from pymfdata.rdb.usecase import AsyncSQLAlchemyUnitOfWork

from src.modules.author.infrastructure.query.repository.impl import (
    AuthorAlchemyRepository,
    AuthorQueryRepository,
)


class AuthorQueryUnitOfWork(AsyncSQLAlchemyUnitOfWork):
    def __init__(self, engine: AsyncEngine) -> None:
        super().__init__(engine)

    async def __aenter__(self) -> "AuthorQueryUnitOfWork":
        await super().__aenter__()

        self.repository: AuthorQueryRepository = AuthorAlchemyRepository(self.session)
        return self
