from fastapi import FastAPI
from app.routes import tokens
from app.db.session import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(tokens.router)
