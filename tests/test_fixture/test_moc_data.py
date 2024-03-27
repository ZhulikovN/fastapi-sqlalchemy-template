import pytest
from tests.conftest import create_test_database, create_tables
import asyncio

#
# @pytest.fixture
# async def setup_database():
#     # Подготовка: Создание тестовой базы данных и таблиц
#     await create_test_database()
#     await create_tables()
#     yield

@pytest.mark.asyncio
async def test_moc_data(db_session, moc_data):
    # await create_test_database()
    async for session in db_session:
        result = await session.execute("SELECT * FROM authortests WHERE first_name = 'John'")
        author = result.fetchone()
        assert author is not None, "Тестовые данные не были вставлены"

# async def check_table_exists(engine, table_name):
#     async with engine.connect() as conn:
#         result = await conn.execute(
#             "SELECT to_regclass('public.%s')" % table_name
#         )
#         table_exists = await result.scalar()
#         return table_exists is not None