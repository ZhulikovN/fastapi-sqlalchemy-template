import pytest



@pytest.mark.asyncio
async def test_db_session(db_session):
    # Получаем сессию из асинхронного генератора
    async for session in db_session:
        result = await session.execute("SELECT 1")
        value = result.scalar()
        assert value == 1, "Сессия не работает должным образом"