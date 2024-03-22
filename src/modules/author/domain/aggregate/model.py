from dataclasses import dataclass, field
from typing import List, Optional

from modules.author.domain.value_objects import Age, AuthorBook, Biography, Name
from modules.author.usecase.addBookToAuthor.command import AddBookToAuthorCommand
from modules.author.usecase.newAuthor.command import NewAuthorCommand

from .id import AuthorId


@dataclass
class Author:
    id: AuthorId
    name: Name
    age: Age
    biography: Optional[Biography]
    book_ids: List[AuthorBook] = field(default_factory=list)

    @staticmethod
    def new_author(command: NewAuthorCommand) -> "Author":
        return Author(id=AuthorId.next_id(), **command.dict())

    def add_book(self, command: AddBookToAuthorCommand):
        self.book_ids.append(AuthorBook(author_id=self.id, book_id=command.book_id))
