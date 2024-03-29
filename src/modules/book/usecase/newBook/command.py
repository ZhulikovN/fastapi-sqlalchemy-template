from pydantic import BaseModel, Field

from src.modules.book.domain.value_objects import Isbn, KoreanMoney, Page, Title, Year


class NewBookCommand(BaseModel):
    title: Title = Field(title="Book Title")
    isbn: Isbn = Field(title="Book Isbn")
    pages: Page = Field(title="Book Page")
    price: KoreanMoney = Field(title="Book Price")
    publication_year: Year = Field(title="Book publication year")
