from pydantic import BaseModel, Field

from src.modules.author.domain.aggregate.model import AuthorId


class GetAuthorCommand(BaseModel):
    book_id: AuthorId = Field(title="Book ID")
