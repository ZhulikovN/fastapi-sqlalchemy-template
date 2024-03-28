from fastapi.testclient import TestClient
from src.app import app
import pytest
from httpx import AsyncClient
from httpx import AsyncClient
# from httpx._transports.asgi import ASGITransport

# from sqlalchemy.ext.asyncio import AsyncSession
# from unittest.mock import patch
# from fastapi.testclient import TestClient
# from unittest.mock import MagicMock
import pytest
# from src.modules.author.infrastructure.query.dto import AuthorDTO

# from src.container import Container
from src.app import app
# from tests.conftest  import  test_db_session, test_db_session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import asyncio
import asyncpg
from tests.conftest import test_db_name


@pytest.mark.asyncio
async def test_find_author_by_first_name(db_session, moc_data):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://0.0.0.0:8000") as ac:
        response = await ac.get("/authors?first_name=John")

    assert response.status_code == 200




    # assert response.json() == [
    #     {"id": 1, "first_name": "John", "last_name": "Doe", "age": 30,
    #      "biography": "Test biography", "books": [1, 2]}
    # ]

# @pytest.fixture
# def mock_fetch_by_author_first_name():
#     # Эмулируем результат запроса к базе данных
#     return [AuthorDTO(id=1, first_name="John", last_name="Doe", age=30, biography="Test biography",
#                       books=[1, 2])]


# @pytest.mark.asyncio
# # @patch("app.AsyncClient.get")
# async def test_find_author_by_first_name(mock_get, mock_fetch_by_author_first_name):
#     mock_get.return_value.status_code = 200
#     mock_get.return_value.json.return_value = mock_fetch_by_author_first_name
#
#     # Тестируем эндпоинт с помощью мока
#     response = await app.client.get("/authors?first_name=John")
#
#     assert response.status_code == 200
#     assert response.json() == [
#         {"id": 1, "first_name": "John", "last_name": "Doe", "age": 30,
#          "biography": "Test biography", "books": [1, 2]}
#     ]
# @pytest.mark.asyncio
# async def test_find_author_by_first_name(test_db_session):
#     # Создаем асинхронную сессию с помощью фабрики
#     # async with await test_db_session() as session:
#     async for session in test_db_session:  # Используем асинхронный цикл для получения асинхронной сессии
#         async with session as session:
#         # Создаем экземпляр DTO
#             author = AuthorDTO(id=7170253137725493000, first_name="John", last_name="Doe", age=30, biography="Test biography", books = [1, 2])
#
#         # Добавляем объект в сессию и коммитим транзакцию
#         session.add(author)
#         await session.commit()
#         await session.refresh(author)  # Обновляем состояние объекта после коммита
#
#         # После подготовки тестовых данных, можно продолжить с тестированием эндпоинта
#         async with AsyncClient(app=app, base_url="http://test") as ac:
#             response = await ac.get(f"/authors?first_name={author.first_name}")
#             assert response.status_code == 200

# @pytest.mark.asyncio
# async def test_find_author_by_first_name(test_db_session):
#     # Предварительное заполнение тестовой базы данными
#     async with test_db_session() as session:
#         session.add_all([
#             AuthorDTO(first_name="John", last_name="Doe", age=30, biography="Test biography"),
#             # Добавьте необходимые тестовые данные
#         ])
#         await session.commit()
#
#     # Тестирование эндпоинта
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/authors?first_name=John")
#         assert response.status_code == 200
#         assert response.json() == [{"id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "biography": "..."}]
# @pytest.mark.asyncio
# async def test_find_author_by_first_name(mock_db_engine, mock_fetch_by_author_first_name):
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/authors?first_name=John")
#         assert response.status_code == 200
#         assert response.json() == [
#             {"id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "biography": "..."}]
#         app.dependency_overrides = {}

    # with pytest.raises(TypeError):
    #     response = client.get("/authors?first_name=John")
    #     assert response.status_code == 200
    #     assert response.json() == [{"id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "biography": "..."}]


#
# # Мок для создания сессии базы данных
# @pytest.fixture
# async def mock_db_session():
#     with patch("src.modules.author.infrastructure.query.uow.AuthorQueryUnitOfWork") as MockUnitOfWork:
#         async with AsyncSession() as session:
#             # Возвращаем моканную сессию базы данных
#             mock_uow_instance = MockUnitOfWork.return_value
#             mock_uow_instance.session = session
#             yield session

# @pytest.mark.asyncio
# async def test_find_author_by_first_name(mock_fetch_by_author_first_name):
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/authors?first_name=John")
#         assert response.status_code == 200
#         assert response.json() == [
#             {"id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "biography": "..."}]

    # with pytest.raises(TypeError):
    #     response = client.get("/authors?first_name=John")
    #     assert response.status_code == 200
    #     assert response.json() == [{"id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "biography": "..."}]



# # Мокируем функцию, которая будет использоваться для замены реального вызова базы данных
# mocked_find_author_by_first_name = MagicMock(
#     return_value=[{"id": 1, "first_name": "John", "last_name": "Doe"}])
#
#
# @pytest.fixture
# def client():
#     # Здесь мы создаем тестовый клиент для нашего приложения
#     with TestClient(app) as client:
#         yield client
#
#
#
# @pytest.mark.asyncio
# async def test_find_author_by_first_name(client, mocker):
#
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/authors?first_name=John")
#         assert response.status_code == 200
#         assert response.json() == [
#             {"id": 1, "first_name": "John", "last_name": "Doe", "age": 30, "biography": "..."}]
#
# def test_find_author_by_first_name(client, mocker):
#     # Используем mocker для замены реальной функции, обращающейся к базе данных, на нашу мокирующую функцию
#     mocker.patch(
#         "src.modules.author.usecase.FindAuthorByFirstname.impl.FindAuthorByFirstname.invoke",
#         mocked_find_author_by_first_name
#     )
#
#     # Отправляем GET запрос на наш эндпоинт с именем автора
#     response = client.get("/author?first_name=John")
#
#     # Проверяем статус-код ответа
#     assert response.status_code == 200
#     # Убеждаемся, что в ответе содержится ожидаемая информация
#     assert response.json() == [{"id": 1, "first_name": "John", "last_name": "Doe"}]
#
#     # Проверяем, что мокирующая функция была вызвана с правильными аргументами
#     mocked_find_author_by_first_name.assert_called_once_with("John")

# httpx = "^0.27.0"
# asynctest = "^0.13.0"
# requests = "^2.31.0"
# pytest-asyncio = "^0.23.6"