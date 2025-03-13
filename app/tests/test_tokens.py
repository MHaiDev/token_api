import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_token(client: AsyncClient):
    response = await client.post("/tokens/", json={"name": "TestToken", "symbol": "TT"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data  
    assert data["name"] == "TestToken"
    assert data["symbol"] == "TT"

@pytest.mark.asyncio
async def test_read_tokens(client: AsyncClient):
    response = await client.get("/tokens/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_update_token(client: AsyncClient):
    # Create a token first
    response = await client.post("/tokens/", json={"name": "ToUpdate", "symbol": "UT"})
    data = response.json()
    token_id = data["id"]  

    # Then update it
    response = await client.put(f"/tokens/{token_id}", json={"name": "UpdatedToken"})
    assert response.status_code == 200
    assert response.json()["name"] == "UpdatedToken"

@pytest.mark.asyncio
async def test_delete_token(client: AsyncClient):
    # Create a token first
    response = await client.post("/tokens/", json={"name": "ToDelete", "symbol": "TD"})
    data = response.json()
    token_id = data["id"]  

    # Then delete it
    response = await client.delete(f"/tokens/{token_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Token deleted successfully"
