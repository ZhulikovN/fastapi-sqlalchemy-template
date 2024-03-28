import pytest
from sqlalchemy.future import select
from tests.conftest import AuthorTest


@pytest.mark.asyncio
async def test_add_and_get_author(db_session):
    new_author = AuthorTest(
        first_name="John",
        last_name="Doe",
        age=45,
        biography="Some biography of John Doe"
    )

    async for session in db_session:
        async with session.begin():
            session.add(new_author)

    async for session in db_session:
        async with session.begin():
            result = await session.execute(
                select(AuthorTest).where(AuthorTest.first_name == "John"))
            author = result.scalars().first()

            assert author is not None
            assert author.first_name == "John"
            assert author.last_name == "Doe"
            assert author.age == 45
            assert author.biography == "Some biography of John Doe"



# @pytest.mark.asyncio
# async def test_db_session(db_session):
#     # Получаем сессию из асинхронного генератора
#     async for session in db_session:
#         result = await session.execute("SELECT 1")
#         value = result.scalar()
#         assert value == 1, "Сессия не работает должным образом"