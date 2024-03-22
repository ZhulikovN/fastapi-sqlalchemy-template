from pymfdata.common.usecase import BaseUseCase
from pymfdata.rdb.transaction import async_transactional

from src.modules.book.domain.aggregate.model import Book
from src.modules.book.infrastructure.persistence.uow import BookPersistenceUnitOfWork
from src.modules.book.usecase.newBook.command import NewBookCommand


class NewBookUseCase(BaseUseCase[BookPersistenceUnitOfWork]):
    def __init__(self, uow: BookPersistenceUnitOfWork) -> None:
        self._uow = uow

    @async_transactional()
    async def invoke(self, command: NewBookCommand) -> Book:
        book = Book.new_book(command)
        self.uow.repository.create(book)
        return book
