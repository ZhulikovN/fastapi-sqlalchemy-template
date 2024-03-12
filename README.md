# Проект №6: FastAPI + SQLAlchemy Template (название репозитория - fastapi-sqlalchemy-template)

## Описание

`FastAPI + SQLAlchemy Template` - это шаблон для создания проектов на FastAPI с использованием
SQLAlchemy. В этом проекте тебе предстоит научиться работать с SQLAlchemy, в
качестве основы для проекта предлагается взять
репозиторий [fastapi-ddd-example](https://github.com/NEONKID/fastapi-ddd-example). Также в этом
проекте тебе предстоит потренироваться в чтении и понимании чужого кода, а также в переносе кода из
одного проекта в другой.

Начиная с этого проекта ты будешь работать с репозиторием так, как это делают профессионалы -
использую pull request'ы и code review. Перед тем как начать работу над проектом, тебе нужно будет
созвониться со мной, чтобы я помог тебе настроить проект и объяснить, как работать с merge
request'ами и code review.

## Рекомендуемая структура проекта

```
/fastapi-sqlalchemy-template
|-- src  # Исходный код
|   |-- common ...  # копия папки common из fastapi-ddd-example
|   |-- core ...  # копия папки core из fastapi-ddd-example
|   |-- modules ...  # копия папки modules из fastapi-ddd-example
|   |-- persistence ...  # копия папки persistence из fastapi-ddd-example
|   |-- main.py  # переименованный файл app.py
|   |-- container.py  
|   `-- settings.py
`-- tests  # Тесты
    |-- __init__.py
    `-- tests.py
```

## Этапы выполнения проекта

1. Сделать `git clone` репозитория `fastapi-ddd-example` и научиться запускать его.
2. Внимательно прочитать README.md в проекте `fastapi-ddd-example` и разобраться с тем, как
   работает `SQLAlchemy` на примере этого проекта.
3. Сделать скелет проекта как в прошлом проекте.
4. Перенести все файлы из `fastapi-ddd-example` в папку `src` (папка `images` не нужна) и
   добавить `settings.py`.
5. Настроить зависимости проекта в файле `pyproject.toml`, добавить все необходимые зависимости
   в `[tool.poetry.dependencies]` и все вспомогательные зависимости
   в `[tool.poetry.group.dev.dependencies]` (isort, black и т.д.).
6. Внести правки в файлы проекта, чтобы команда `make dev` выполнялась без ошибок.
7. Настроить `docker-compose.yml` и `Dockerfile` для запуска проекта в контейнере.
8. Настроить `GitHub Actions` для автоматической проверки кода и тестирования проекта.
9. Добавить эндпоинт `GET /authors` в соответствии с тем, как в проекте сделан эндпоинт
   `GET /books`.
10. Написать тесты для эндпоинта `GET /authors`.

## ❗❗❗ Новые технологии ❗❗❗

- [SQLAlchemy](https://www.sqlalchemy.org/)
- Pull Request (Merge Request)

## Список используемых технологий

- [poetry](https://python-poetry.org/)
- [black](https://github.com/psf/black)
- [isort](https://github.com/PyCQA/isort)
- [pylint](https://github.com/pylint-dev/pylint)
- [flake8](https://github.com/PyCQA/flake8)
- [mypy](https://mypy.readthedocs.io/en/stable/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [Swagger](https://swagger.io/)
- [Postman](https://www.postman.com/)
- [JSON](https://www.json.org/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)
- [psycopg3](https://www.psycopg.org/psycopg3/docs/index.html)
- [Pytest](https://docs.pytest.org/en/8.0.x/)
- [GitHub Actions](https://github.com/features/actions)
- [Logging](https://docs.python.org/3/library/logging.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## Полезные ссылки

- [fastapi-backend-template](https://github.com/yar-jul/fastapi-backend-template) - шаблон для
  работы с FastAPI и SQLAlchemy, который я делал когда-то в качестве тестового задания для
  одной из работ, куда меня, кстати, в итоге взяли.
