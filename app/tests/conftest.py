import pytest
import pytest_asyncio
from httpx import AsyncClient
from app.main import app  

@pytest_asyncio.fixture
async def client():
    async with AsyncClient(base_url="http://127.0.0.1:8000", follow_redirects=True) as ac:
        yield ac
