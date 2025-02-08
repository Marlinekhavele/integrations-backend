import asyncio

import pytest
from app.main import app
from httpx import AsyncClient

TEST_BASE_URL = "http://test"


@pytest.fixture
def client():
    return AsyncClient(app=app)


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()
