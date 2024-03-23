FROM python:3.9-slim

RUN mkdir -p  /usr/src/app/

WORKDIR /usr/src/app


RUN pip install poetry
COPY pyproject.toml /usr/src/app/
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

RUN pip install asyncpg sqlalchemy


COPY . /usr/src/app/


COPY wait-for-it.sh .
RUN chmod +x wait-for-it.sh


ENV PYTHONPATH=/usr/src/app

EXPOSE 5000


CMD ["uvicorn", "src.app:app", "--host=0.0.0.0", "--loop=uvloop", "--port=5000"]