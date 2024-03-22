from src.common.protocols.event import BaseEvent
from src.modules.author.domain.aggregate.id import AuthorId
from src.modules.book.domain.aggregate.id import BookId
from src.modules.book.domain.event import AuthorAddedToBookDomainEvent

from .command import AddBookToAuthorCommand
from .impl import AddBookToAuthorUseCase


class AddBookToAuthorEventHandler(BaseEvent):
    def __init__(self, uc: AddBookToAuthorUseCase) -> None:
        self.uc = uc

    async def handle(self, param: AuthorAddedToBookDomainEvent = None) -> None:
        command = AddBookToAuthorCommand(
            book_id=BookId(param.book_id), author_id=AuthorId(param.author_id)
        )
        await self.uc.invoke(command)
