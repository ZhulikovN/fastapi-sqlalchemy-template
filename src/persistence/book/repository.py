from pymfdata.rdb.repository import AsyncRepository, AsyncSession
from sqlalchemy import inspect

from src.modules.book.domain.aggregate.model import Book


class BookRepository(AsyncRepository[Book, int]):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
