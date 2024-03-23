from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Query, Path

from src.container import Container
from src.modules.author.domain.aggregate.id import AuthorId
from src.modules.author.usecase import router
from src.modules.author.usecase.findAuthorByTitle.impl import FindAuthorByTitleUseCase

from src.modules.author.usecase.findAuthorByTitle.command import GetAuthorCommand


@router.get(path="", name="Find auther by first_name")
@inject
async def find_author_by_id(
    first_name: str = Query(..., author="Book Title"),
    uc: FindAuthorByTitleUseCase = Depends(Provide[Container.find_author_by_id_use_case]),
):
    result = await uc.invoke(first_name)
    return result

