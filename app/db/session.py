from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

# Database connection URL (using asyncpg driver)
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/token_db"

# Create an asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Dependency to get database session
async def get_db():
    async with SessionLocal() as session:
        yield session
