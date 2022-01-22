from typing import Generator, Any

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from app.tables import ProductTable


@pytest.fixture(autouse=True)
def init_tables() -> Generator[None, None, None]:
    if not ProductTable.exists():
        ProductTable.create_table(
            read_capacity_units=1, write_capacity_units=1, wait=True
        )
    yield
    ProductTable.delete_table()


@pytest.fixture
def app() -> FastAPI:
    from app.main import app as api_app

    return api_app


@pytest.fixture()
def client(app: FastAPI, init_tables: Any) -> Generator[TestClient, None, None]:
    yield TestClient(app=app)
