from pydantic import BaseModel
from typing import Optional

class TokenCreate(BaseModel):
    name: str
    symbol: str 

class TokenUpdate(BaseModel):
    name: Optional[str] = None 
    symbol: Optional[str] = None
