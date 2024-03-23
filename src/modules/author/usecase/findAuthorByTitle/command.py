from pydantic import BaseModel, Field

from src.modules.author.domain.aggregate.model import AuthorId


class GetAuthorCommand(BaseModel):
    first_name: AuthorId = Field(title="Book ID")
