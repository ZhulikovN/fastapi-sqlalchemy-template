from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Query

from src.container import Container
from src.modules.book.usecase import router
from src.modules.book.usecase.findBookByTitle.impl import FindBookByTitleUseCase


@router.get(path="", name="Find book by title")
@inject
async def find_book_by_title(
    title: str = Query(..., title="Book Title"),
    uc: FindBookByTitleUseCase = Depends(Provide[Container.find_book_by_title_use_case]),
):
    return await uc.invoke(title)
