from typing import List

from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from src.modules.author.infrastructure.query.dto import AuthorDTO
from src.modules.author.infrastructure.query.uow import AuthorQueryUnitOfWork


class FindAuthorByFirstname(BaseUseCase[AuthorQueryUnitOfWork]):
    def __init__(self, uow: AuthorQueryUnitOfWork) -> None:
        self._uow = uow

    @async_transactional(read_only=True)
    async def invoke(self, first_name: str) -> List[AuthorDTO]:

        return await self.uow.repository.fetch_by_author_first_name(first_name)
