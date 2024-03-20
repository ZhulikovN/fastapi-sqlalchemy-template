from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Path

from src.container import Container
from src.modules.author.domain.aggregate.id import AuthorId
from src.modules.author.usecase import router
from src.modules.author.usecase.findAuthorByTitle.impl import FindAuthorByTitleUseCase

from src.modules.author.usecase.findAuthorByTitle.command import GetAuthorCommand


@router.get(path="/{id}", name="Find auther by id")
@inject
async def find_author_by_id(
    id: AuthorId = Path(..., title="Book id"),
    uc: FindAuthorByTitleUseCase = Depends(Provide[Container.find_author_by_id_use_case]),
):
    return await uc.invoke(GetAuthorCommand(author_id=id))
