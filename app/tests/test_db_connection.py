import pytest
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text  
from app.db.session import engine

@pytest.mark.asyncio
async def test_db_connection():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))  
        print("Database connection successful!")
    except Exception as e:
        print("Database connection failed:", e)
        assert False 
