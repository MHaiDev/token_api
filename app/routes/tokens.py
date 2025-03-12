from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import Token
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.post("/tokens/")
def create_token(name: str, db: Session = Depends(get_db)):
    new_token = Token(name=name)
    db.add(new_token)
    db.commit()
    db.refresh(new_token)
    return new_token

@router.get("/tokens/")
async def read_tokens(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Token)) 
    return result.scalars().all()  