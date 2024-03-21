from dataclasses import dataclass
from typing import FrozenSet

from sqlalchemy.ext.associationproxy import association_proxy


@dataclass
class AuthorDTO:
    id: int
    first_name: str
    last_name: str
    age: int
    biography: str
    books: FrozenSet[int] = association_proxy("author_books", "book_id")
