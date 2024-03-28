from abc import abstractmethod
from typing import List, Protocol

from src.modules.author.infrastructure.query.dto import AuthorDTO


class AuthorQueryRepository(Protocol):
    @abstractmethod
    async def fetch_by_id(self, _id: int) -> AuthorDTO: ...

    @abstractmethod
    async def fetch_by_author_first_name(self, first_name: str) -> List[AuthorDTO]: ...
