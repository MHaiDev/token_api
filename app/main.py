from fastapi import FastAPI
from app.routes import tokens

app = FastAPI()

app.include_router(tokens.router)
