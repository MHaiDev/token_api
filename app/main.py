from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import tokens
from app.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(tokens.router)
