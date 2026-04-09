import pytest


@pytest.mark.asyncio
async def test_health_check_returns_200(client):
    response = await client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["status"] == "ok"


@pytest.mark.asyncio
async def test_health_check_has_request_id(client):
    response = await client.get("/api/v1/health")
    assert "x-request-id" in response.headers
    request_id = response.headers["x-request-id"]
    assert len(request_id) == 36  # UUID format
