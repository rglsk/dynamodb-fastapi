FROM python:3.9.3-buster

RUN mkdir -p /app
WORKDIR /app

RUN apt-get update && apt-get install libpq-dev python3-dev -y

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-root

COPY ./app ./app

ENV PYTHONPATH=/app