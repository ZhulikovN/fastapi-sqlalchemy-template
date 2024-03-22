from pydantic import BaseModel

from src.modules.author.domain.aggregate.id import AuthorId
from src.modules.book.domain.aggregate.id import BookId


class AddAuthorCommand(BaseModel):
    author_id: AuthorId
    book_id: BookId
