import pytest
from asynctest import CoroutineMock
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from src.modules.author.infrastructure.query.repository.impl import AuthorAlchemyRepository
from src.modules.author.infrastructure.query.dto import AuthorDTO
from pymfdata.rdb.connection import AsyncSQLAlchemy

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from pymfdata.rdb.mapper import Base
from src.app import app
from src.container import Container
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import asyncio
import asyncpg
from src.app import app
from dataclasses import dataclass, field
from typing import List
from pymfdata.rdb.mapper import Base
from typing import List, Union
from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.orm import composite






dbname = "postgres"
user = "postgres"
password = "postgres"
host = "0.0.0.0"
test_db_name = "test_db_2"
# async_engine = create_async_engine(f"postgresql+asyncpg://{user}:{password}@{host}/{dbname}", echo=True)
# test_db_url = f"postgresql+asyncpg://{user}:{password}@{host}/{dbname}"
test_db_url = f"postgresql+asyncpg://{user}:{password}@{host}/{test_db_name}"


async def create_test_database():
    conn = await asyncpg.connect(user='postgres', password='postgres', database='postgres', host='0.0.0.0')
    try:
        res = await conn.fetch("SELECT 1 FROM pg_database WHERE datname=$1", test_db_name)
        if not res:
            await conn.execute(f'CREATE DATABASE {test_db_name}')
    except Exception as e:
        print(f'Ошибка при создании/проверке базы данных: {e}')
    finally:
        await conn.close()

asyncio.run(create_test_database())


class AuthorTest(Base):
    __tablename__ = "authortests"

    id = Column(BigInteger, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    biography = Column(String(3000), nullable=True)

@pytest.fixture(autouse=True)
async def db_session():
    # Создание асинхронного движка и сессии здесь
    async_engine = create_async_engine(test_db_url, echo=True)
    #фабрика, которая используется для создания новых экземпляров Session
    async_session_maker = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with async_session_maker() as session:
        yield session
    #закрыть все соединения в пуле
    await async_engine.dispose()


@pytest.fixture(autouse=True)
async def moc_data(db_session):
    # Вставка тестовых данных
    async for session in db_session:
        async with session.begin():
            author = AuthorTest(id=1, first_name="John", last_name="Doe", age=30, biography="Test biography")
            session.add(author)
        await session.commit()


# @pytest.fixture
# async def moc_data(db_session):
#     # Вставка тестовых данных
#     async with db_session as session:
#         async with session.begin():
#             author = AuthorTest(id=1, first_name="John", last_name="Doe", age=30, biography="Test biography")
#             session.add(author)
#         await session.commit()


# @pytest.fixture
# async def db_engine() -> AsyncEngine:
#     engine = create_async_engine(test_db_url, echo=True)
#     try:
#         yield engine
#     finally:
#         await engine.dispose()
#
#
#
# @pytest.fixture
# async def db_session(db_engine):
#     async_session_maker = sessionmaker(bind=db_engine, expire_on_commit=False, class_=AsyncSession)
#     async with async_session_maker() as session:
#         yield session
#     await db_engine.dispose()
#
#
# @pytest.fixture
# async def create_tables(db_engine):
#     async with db_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


#  async def create_tables():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
# asyncio.run(create_tables())
#
#
# @pytest.fixture
# async def db_session():
#     test_db_url = f"postgresql+asyncpg://{user}:{password}@{host}/{test_db_name}"
#     # Создание асинхронного движка и сессии здесь
#     async_engine = create_async_engine(test_db_url, echo=True)
#     #фабрика, которая используется для создания новых экземпляров Session
#     async_session_maker = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
#
#     async with async_session_maker() as session:
#         yield session
#     #закрыть все соединения в пуле
#     await async_engine.dispose()
#
#
# @pytest.fixture
# async def setup_database():
#     # Подготовка: Создание тестовой базы данных и таблиц
#     await create_test_database()
#     await create_tables()
#     yield
#
#
# @pytest.fixture
# async def moc_data(db_session, setup_database):
#     # Вставка тестовых данных
#     async with db_session as session:
#         async with session.begin():
#             author = AuthorTest(id=1, first_name="John", last_name="Doe", age=30, biography="Test biography")
#             session.add(author)
#         await session.commit()