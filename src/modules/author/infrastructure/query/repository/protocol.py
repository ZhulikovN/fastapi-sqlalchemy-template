from abc import abstractmethod
from typing import Protocol

from src.modules.author.infrastructure.query.dto import AuthorDTO
from src.modules.author.domain.aggregate.id import AuthorId


class AuthorQueryRepository(Protocol):
    @abstractmethod
    async def fetch_by_id(self, _id: int) -> AuthorDTO: ...

    @abstractmethod
    async def fetch_id(self, _id: AuthorId) -> AuthorDTO: ...