from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from starlette import status

from src.container import Container
from src.modules.book.usecase import router
from src.modules.book.usecase.newBook.impl import NewBookUseCase

from .impl import NewBookCommand


@router.post(path="", name="New Book", status_code=status.HTTP_201_CREATED)
@inject
async def new_book(
    command: NewBookCommand, uc: NewBookUseCase = Depends(Provide[Container.new_book_use_case])
):
    book = await uc.invoke(command)
    return book.id
