from abc import abstractmethod
from typing import Protocol

from src.modules.author.infrastructure.query.dto import AuthorDTO


class AuthorQueryRepository(Protocol):
    @abstractmethod
    async def fetch_by_id(self, _id: int) -> AuthorDTO: ...
