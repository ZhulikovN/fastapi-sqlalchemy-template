from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton
from pymfdata.rdb.connection import AsyncSQLAlchemy

from src.modules.author.infrastructure.persistence.adapter import (
    AuthorPersistenceAdapter,
)
from src.modules.author.infrastructure.persistence.uow import (
    AuthorPersistenceUnitOfWork,
)
from src.modules.author.infrastructure.query.uow import AuthorQueryUnitOfWork
from src.modules.author.usecase.addBookToAuthor.event_handler import (
    AddBookToAuthorEventHandler,
)
from src.modules.author.usecase.addBookToAuthor.impl import AddBookToAuthorUseCase
from src.modules.author.usecase.findAuthorByTitle.impl import FindAuthorByTitleUseCase
from src.modules.author.usecase.newAuthor.impl import NewAuthorUseCase
from src.modules.book.infrastructure.persistence.adapter import BookPersistenceAdapter
from src.modules.book.infrastructure.persistence.uow import BookPersistenceUnitOfWork
from src.modules.book.infrastructure.query.uow import BookQueryUnitOfWork
from src.modules.book.usecase.addAuthor.impl import AddAuthorUseCase
from src.modules.book.usecase.deleteBook.impl import DeleteBookUseCase
from src.modules.book.usecase.findBookByTitle.impl import FindBookByTitleUseCase
from src.modules.book.usecase.newBook.impl import NewBookUseCase


class Container(DeclarativeContainer):
    db: Singleton[AsyncSQLAlchemy] = Singleton(
        AsyncSQLAlchemy,
        db_uri="{engine}://{username}:{password}@{host}:{port}/{db_name}".format(
            engine="postgresql+asyncpg",
            username="postgres",
            password="postgres",
            host="127.0.0.1",
            port=5432,
            db_name="ddd_book",
        ),
    )

    # Unit Of Work
    author_persistence_unit_of_work = Factory(
        AuthorPersistenceUnitOfWork, engine=db.provided.engine
    )
    author_query_unit_of_work = Factory(AuthorQueryUnitOfWork, engine=db.provided.engine)

    book_persistence_unit_of_work = Factory(BookPersistenceUnitOfWork, engine=db.provided.engine)
    book_query_unit_of_work = Factory(BookQueryUnitOfWork, engine=db.provided.engine)

    # Adapter (If you use traditional mapper)
    author_persistence_adapter = Factory(
        AuthorPersistenceAdapter, uow=author_persistence_unit_of_work
    )
    book_persistence_adapter = Factory(BookPersistenceAdapter, uow=book_persistence_unit_of_work)

    # Use Case
    add_book_to_author_use_case = Factory(
        AddBookToAuthorUseCase, uow=author_persistence_unit_of_work
    )
    add_book_to_author_event_handler = Factory(
        AddBookToAuthorEventHandler, uc=add_book_to_author_use_case
    )
    add_author_use_case = Factory(
        AddAuthorUseCase, uow=book_persistence_unit_of_work, event=add_book_to_author_event_handler
    )

    new_author_use_case = Factory(NewAuthorUseCase, uow=author_persistence_unit_of_work)
    delete_book_use_case = Factory(DeleteBookUseCase, uow=book_persistence_unit_of_work)
    find_book_by_title_use_case = Factory(FindBookByTitleUseCase, uow=book_query_unit_of_work)
    new_book_use_case = Factory(NewBookUseCase, uow=book_persistence_unit_of_work)
    find_author_by_id_use_case = Factory(FindAuthorByTitleUseCase, uow=author_query_unit_of_work)
