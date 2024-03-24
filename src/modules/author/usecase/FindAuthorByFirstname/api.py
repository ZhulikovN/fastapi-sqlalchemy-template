from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Query

from src.container import Container
from src.modules.author.usecase import router
from src.modules.author.usecase.FindAuthorByFirstname.impl import FindAuthorByFirstname


@router.get("", name="Find auther by first_name")
@inject
async def find_author_by_first_name(
    first_name: str = Query(..., author="Auther first name"),
    uc: FindAuthorByFirstname = Depends(Provide[Container.find_author_by_first_name_use_case]),
):
    result = await uc.invoke(first_name)
    return result
