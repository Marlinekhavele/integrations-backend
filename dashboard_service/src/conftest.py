import asyncio

import pytest
from app.main import app
from httpx import ASGITransport, AsyncClient

TEST_BASE_URL = "http://test"


@pytest.fixture
async def client():
    """
    Fixture to provide an AsyncClient instance configured for testing.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url=TEST_BASE_URL
    ) as client:
        yield client


@pytest.fixture(scope="session")
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()
