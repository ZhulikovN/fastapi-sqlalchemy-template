from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from src.modules.author.domain.aggregate.id import AuthorId
from src.modules.author.infrastructure.query.dto import AuthorDTO
from src.modules.author.infrastructure.query.uow import AuthorQueryUnitOfWork
from src.modules.author.usecase.findAuthorByTitle.command import GetAuthorCommand

# from .command import GetAuthorCommand


class FindAuthorByTitleUseCase(BaseUseCase[AuthorQueryUnitOfWork]):
    def __init__(self, uow: AuthorQueryUnitOfWork) -> None:
        self._uow = uow

# -> AuthorDTO
    @async_transactional(read_only=True)
    async def invoke(self, first_name: str) -> AuthorDTO:
        # book = await self.uow.repository.find_by_pk(command.author_id)
        # return book

        # author_id = AuthorId(command.author_id)
        # return await self.uow.repository.fetch_by_id(author_id)
        return await self.uow.repository.fetch_by_title_first_name(first_name)
