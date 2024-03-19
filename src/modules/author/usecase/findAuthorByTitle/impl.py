from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from src.modules.author.infrastructure.query.dto import AuthorDTO
from src.modules.author.infrastructure.query.uow import AuthorQueryUnitOfWork

from .command import GetAuthorCommand


class FindAuthorByTitleUseCase(BaseUseCase[AuthorQueryUnitOfWork]):
    def __init__(self, uow: AuthorQueryUnitOfWork) -> None:
        self._uow = uow

    @async_transactional(read_only=True)
    async def invoke(self, command: GetAuthorCommand) -> AuthorDTO:
        return await self.uow.repository.fetch_by_id(command.book_id)