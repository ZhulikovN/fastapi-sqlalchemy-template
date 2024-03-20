from pydantic import BaseModel

from src.modules.author.domain.aggregate.id import AuthorId
from src.modules.book.domain.aggregate.id import BookId


class AddBookToAuthorCommand(BaseModel):
    book_id: BookId
    author_id: AuthorId
