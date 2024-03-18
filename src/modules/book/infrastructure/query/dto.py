from dataclasses import dataclass
from typing import FrozenSet

from sqlalchemy.ext.associationproxy import association_proxy


@dataclass
class BookDTO:
    id: int
    title: str
    isbn: str
    pages: int
    authors: FrozenSet[int] = association_proxy("book_authors", "author_id")
