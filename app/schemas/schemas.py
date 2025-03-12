from pydantic import BaseModel

class TokenCreate(BaseModel):
    name: str

class TokenUpdate(BaseModel):
    name: str
