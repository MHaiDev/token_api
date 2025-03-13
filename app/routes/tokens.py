from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.token import Token
from app.schemas.schemas import TokenCreate, TokenUpdate  

router = APIRouter()

@router.post("/tokens/")
async def create_token(token: TokenCreate, db: AsyncSession = Depends(get_db)):
    """Creates a new token in the database"""
    print("Received data:", token.dict())  

    new_token = Token(name=token.name, symbol=token.symbol)
    db.add(new_token)
    await db.commit()
    await db.refresh(new_token)
    return new_token



@router.get("/tokens/")
async def read_tokens(db: AsyncSession = Depends(get_db)):
    """Reads all tokens from the database"""
    result = await db.execute(select(Token))
    return result.scalars().all()

@router.get("/tokens/{token_id}")
async def read_token(token_id: int, db: AsyncSession = Depends(get_db)):
    """Reads a single token based on the ID"""
    result = await db.execute(select(Token).filter(Token.id == token_id))
    token = result.scalar_one_or_none()
    if token is None:
        raise HTTPException(status_code=404, detail="Token not found")
    return token

@router.put("/tokens/{token_id}")
async def update_token(token_id: int, token_data: TokenUpdate, db: AsyncSession = Depends(get_db)):
    """Updates an existing token"""
    result = await db.execute(select(Token).filter(Token.id == token_id))
    token = result.scalar_one_or_none()
    
    if token is None:
        raise HTTPException(status_code=404, detail="Token not found")

    if token_data.name is not None:
        token.name = token_data.name
    if token_data.symbol is not None:
        token.symbol = token_data.symbol
    
    await db.commit()
    await db.refresh(token)
    return token


@router.delete("/tokens/{token_id}")
async def delete_token(token_id: int, db: AsyncSession = Depends(get_db)):
    """Deletes a token from the database"""
    result = await db.execute(select(Token).filter(Token.id == token_id))
    token = result.scalar_one_or_none()
    if token is None:
        raise HTTPException(status_code=404, detail="Token not found")

    await db.delete(token)
    await db.commit()
    return {"message": "Token deleted successfully"}
