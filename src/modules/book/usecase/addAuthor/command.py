from pydantic import BaseModel

from modules.author.domain.aggregate.id import AuthorId
from modules.book.domain.aggregate.id import BookId


class AddAuthorCommand(BaseModel):
    author_id: AuthorId
    book_id: BookId
