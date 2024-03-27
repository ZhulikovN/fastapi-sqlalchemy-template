import pytest
from tests.conftest import test_db_name
import asyncpg
from tests.conftest import create_test_database


@pytest.mark.asyncio
async def test_create_test_database():
    await create_test_database()
    conn = await asyncpg.connect(user='postgres', password='postgres', database='postgres', host='127.0.0.1')
    created = False
    try:
        test_conn = await asyncpg.connect(user='postgres', password='postgres', database=test_db_name, host='127.0.0.1')
        await test_conn.close()
        created = True
    except Exception as e:
        print(f'Ошибка при подключении к базе данных: {e}')
    finally:
        await conn.close()

    assert created, "Тестовая база данных не была создана"
