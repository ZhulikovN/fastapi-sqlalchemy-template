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
async_engine = create_async_engine(f"postgresql+asyncpg://{user}:{password}@{host}/{dbname}", echo=True)
test_db_url = f"postgresql+asyncpg://{user}:{password}@{host}/{dbname}"

async def create_test_database():
    conn = await asyncpg.connect(user='postgres', password='postgres', database='postgres', host='127.0.0.1')
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



async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_tables())


@pytest.fixture
async def db_session():
    test_db_url = f"postgresql+asyncpg://{user}:{password}@{host}/{test_db_name}"
    # Создание асинхронного движка и сессии здесь
    async_engine = create_async_engine(test_db_url, echo=True)
    #фабрика, которая используется для создания новых экземпляров Session
    async_session_maker = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session_maker() as session:
        yield session
    #закрыть все соединения в пуле
    await async_engine.dispose()


@pytest.fixture
async def setup_database():
    # Подготовка: Создание тестовой базы данных и таблиц
    await create_test_database()
    await create_tables()
    yield


@pytest.fixture
async def moc_data(db_session, setup_database):
    # Вставка тестовых данных
    async with db_session as session:
        async with session.begin():
            author = AuthorTest(id=1, first_name="John", last_name="Doe", age=30, biography="Test biography")
            session.add(author)
        await session.commit()

# @dataclass
# class AuthorDTO:
#     id: int
#     first_name: str
#     last_name: str
#     age: int
#     biography: str
#     books: List[int] = field(default_factory=list)


# @pytest.fixture
# async def moc_data(db_session):
#     # Вставка тестовых данных
#     async with db_session.begin():
#         author = AuthorDTO(id=1, first_name="John", last_name="Doe", age=30, biography="Test biography", books=[1, 2])
#         db_session.add(author)
#     await db_session.commit()

# @pytest.fixture
# async def test_db_session():
#     # Строка подключения к тестовой базе данных
#     test_db_url = f"postgresql+asyncpg://{user}:{password}@{host}/{test_db_name}"
#     engine = create_async_engine(test_db_url, echo=True)
#     async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
#
#     # Возвращаем сессию
#     yield await async_session
#
#     # Закрываем движок после теста
#     await engine.dispose()

# @pytest.fixture
# async def test_db_session():
#     # Создание асинхронного движка для тестовой базы данных
#     engine = create_async_engine(url, echo=True)
#     async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#
#     # async with engine.begin() as conn:
#
#     yield async_session
#
#     await engine.dispose()
# SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     poolclass=StaticPool,
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# Base.metadata.create_all(bind=engine)
#
#
# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()


# container = Container()
# container.register_singleton(TestingSessionLocal, override_get_db)
# app.container = container
# client = TestClient(app)




# @pytest.fixture
# async def mock_db_session() -> AsyncSession:
#     return CoroutineMock(spec=AsyncSession)
#
# @pytest.fixture
# async def mock_db_engine() -> AsyncEngine:
#     engine = CoroutineMock(spec=AsyncEngine)
#     return engine
#
# app.dependency_overrides[Container] = lambda: mock_db_engine
#
# # @pytest.fixture
# # async def mock_db_engine(mock_db_session: AsyncSession) -> AsyncEngine:
# #     mock_engine = CoroutineMock(spec=AsyncEngine)
# #     mock_engine.begin.return_value.__aenter__.return_value = mock_db_session
# #     return mock_engine
#
#
# @pytest.fixture
# def overridden_app(mock_db_engine):
#     # Создаем временный контейнер для тестирования
#     test_container = Container()
#
#     # Переопределяем подключение к базе данных на мокированное
#     test_container.db.override(mock_db_engine)
#
#     # Проводим "проводку" контейнера с переопределениями в приложение FastAPI
#     test_container.wire(modules=[app])
#
#     # Возвращаем приложение с переопределенными зависимостями
#     return app
#
#
#
#
# @pytest.fixture(autouse=True)
# async def mock_fetch_by_author_first_name():
#     mock_result = CoroutineMock()
#     mock_result.unique.return_value.scalars.return_value.all.return_value = [
#         AuthorDTO(id=1, first_name="John", last_name="Doe", age=30, biography="...")
#     ]
#     mock_session = CoroutineMock()
#     mock_session.execute.return_value = mock_result
#     mock_repository = AuthorAlchemyRepository(mock_session)
#     return mock_repository
