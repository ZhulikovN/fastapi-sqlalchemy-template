import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import clear_mappers

from src.container import Container
from src.core.fastapi.error import init_error_handler
from src.core.fastapi.event.middleware import EventHandlerMiddleware
from src.core.fastapi.responses import ORJSONResponse
from src.core.fastapi.routes import add_routes
from src.modules.author.infrastructure.persistence import (
    mapper as author_persistence_mapper,
)
from src.modules.author.infrastructure.query import mapper as author_query_mapper
from src.modules.author.usecase import router as author_router
from src.modules.author.usecase.newAuthor import api as new_author_api
from src.modules.book.infrastructure.persistence import (
    mapper as book_persistence_mapper,
)
from src.modules.book.infrastructure.query import mapper as book_query_mapper
from src.modules.book.usecase import router as book_router
from src.modules.book.usecase.addAuthor import api as add_author_api
from src.modules.book.usecase.deleteBook import api as delete_book_api
from src.modules.book.usecase.findBookByTitle import api as find_book_api
from src.modules.book.usecase.newBook import api as new_book_api
from src.settings import settings

app = FastAPI(default_response_class=ORJSONResponse)
add_routes([author_router, book_router], app)

# Insert Container (IoC)
container = Container()
container.wire(
    modules=[new_author_api, new_book_api, add_author_api, delete_book_api, find_book_api]
)

app.container = container
db = container.db()

app.add_middleware(EventHandlerMiddleware)
init_error_handler(app, "")


@app.on_event("startup")
async def on_startup():
    await db.connect(echo=True)
    await db.create_database()

    author_persistence_mapper.start_mapper()
    author_query_mapper.start_mapper()

    book_persistence_mapper.start_mapper()
    book_query_mapper.start_mapper()


@app.on_event("shutdown")
async def on_shutdown():
    clear_mappers()

    await db.disconnect()


if __name__ == "__main__":
    config = uvicorn.Config(app, host=settings.API_HOST, port=settings.API_PORT, log_level="info")
    server = uvicorn.Server(config)
    server.run()
