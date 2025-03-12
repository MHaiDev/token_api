from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.db.models import Token
from app.schemas.schemas import TokenCreate, TokenUpdate  # Importiere die Pydantic-Schemas

router = APIRouter()

@router.post("/tokens/")
async def create_token(token: TokenCreate, db: AsyncSession = Depends(get_db)):
    """Erstellt einen neuen Token in der Datenbank"""
    new_token = Token(name=token.name)  # Nutzt das JSON-Body-Format
    db.add(new_token)
    await db.commit()
    await db.refresh(new_token)
    return new_token

@router.get("/tokens/")
async def read_tokens(db: AsyncSession = Depends(get_db)):
    """Liest alle Tokens aus der Datenbank"""
    result = await db.execute(select(Token))
    return result.scalars().all()

@router.get("/tokens/{token_id}")
async def read_token(token_id: int, db: AsyncSession = Depends(get_db)):
    """Liest einen einzelnen Token anhand der ID"""
    result = await db.execute(select(Token).filter(Token.id == token_id))
    token = result.scalar_one_or_none()
    if token is None:
        raise HTTPException(status_code=404, detail="Token not found")
    return token

@router.put("/tokens/{token_id}")
async def update_token(token_id: int, token_data: TokenUpdate, db: AsyncSession = Depends(get_db)):
    """Aktualisiert einen bestehenden Token"""
    result = await db.execute(select(Token).filter(Token.id == token_id))
    token = result.scalar_one_or_none()
    if token is None:
        raise HTTPException(status_code=404, detail="Token not found")

    token.name = token_data.name  # Nutzt das JSON-Body-Format
    await db.commit()
    await db.refresh(token)
    return token

@router.delete("/tokens/{token_id}")
async def delete_token(token_id: int, db: AsyncSession = Depends(get_db)):
    """Löscht einen Token aus der Datenbank"""
    result = await db.execute(select(Token).filter(Token.id == token_id))
    token = result.scalar_one_or_none()
    if token is None:
        raise HTTPException(status_code=404, detail="Token not found")

    await db.delete(token)
    await db.commit()
    return {"message": "Token deleted successfully"}
