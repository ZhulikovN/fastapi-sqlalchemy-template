from dataclasses import dataclass, field
from typing import List

from src.modules.book.domain.value_objects import (
    BookAuthor,
    Isbn,
    KoreanMoney,
    Page,
    Title,
    Year,
)
from src.modules.book.usecase.addAuthor.command import AddAuthorCommand
from src.modules.book.usecase.newBook.command import NewBookCommand

from .id import BookId


@dataclass
class Book:
    id: BookId
    title: Title
    isbn: Isbn
    pages: Page
    price: KoreanMoney
    publication_year: Year
    authors: List[BookAuthor] = field(default_factory=list)

    @staticmethod
    def new_book(command: NewBookCommand) -> "Book":
        return Book(id=BookId.next_id(), **command.dict())

    def add_author(self, command: AddAuthorCommand):
        self.authors.append(BookAuthor(book_id=self.id, author_id=command.author_id))
