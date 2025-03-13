from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.models.token import Base  
import os

# Check whether the environment is running in Docker or locally
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # If no environment variable is set, check whether the application is running in Docker.
    # Within Docker, the host name "db" is used, otherwise "localhost" for local development.
    hostname = "db" if os.getenv("DOCKER_ENV") else "localhost"
    DATABASE_URL = f"postgresql+asyncpg://user:password@{hostname}/token_db"

# Create an asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Create database tables (only needed once)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency to get database session
async def get_db():
    async with SessionLocal() as session:
        yield session
