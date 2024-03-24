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




@pytest.fixture
async def mock_db_session() -> AsyncSession:
    return CoroutineMock(spec=AsyncSession)

@pytest.fixture
async def mock_db_engine() -> AsyncEngine:
    engine = CoroutineMock(spec=AsyncEngine)
    return engine

app.dependency_overrides[Container] = lambda: mock_db_engine

# @pytest.fixture
# async def mock_db_engine(mock_db_session: AsyncSession) -> AsyncEngine:
#     mock_engine = CoroutineMock(spec=AsyncEngine)
#     mock_engine.begin.return_value.__aenter__.return_value = mock_db_session
#     return mock_engine


@pytest.fixture
def overridden_app(mock_db_engine):
    # Создаем временный контейнер для тестирования
    test_container = Container()

    # Переопределяем подключение к базе данных на мокированное
    test_container.db.override(mock_db_engine)

    # Проводим "проводку" контейнера с переопределениями в приложение FastAPI
    test_container.wire(modules=[app])

    # Возвращаем приложение с переопределенными зависимостями
    return app




@pytest.fixture(autouse=True)
async def mock_fetch_by_author_first_name():
    mock_result = CoroutineMock()
    mock_result.unique.return_value.scalars.return_value.all.return_value = [
        AuthorDTO(id=1, first_name="John", last_name="Doe", age=30, biography="...")
    ]
    mock_session = CoroutineMock()
    mock_session.execute.return_value = mock_result
    mock_repository = AuthorAlchemyRepository(mock_session)
    return mock_repository
