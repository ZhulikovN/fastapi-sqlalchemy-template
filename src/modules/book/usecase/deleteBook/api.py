from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Path
from starlette import status

from src.container import Container
from src.modules.book.domain.aggregate.id import BookId
from src.modules.book.usecase import router
from src.modules.book.usecase.deleteBook.impl import (
    DeleteBookCommand,
    DeleteBookUseCase,
)


@router.delete(path="/{id}", name="Delete Book", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_book(
    book_id: BookId = Path(..., title="Book ID"),
    uc: DeleteBookUseCase = Depends(Provide[Container.delete_book_use_case]),
):
    await uc.invoke(DeleteBookCommand(book_id=book_id))
