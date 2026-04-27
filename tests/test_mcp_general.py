import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_ping():
    with patch(PATCH) as M:
        M.return_value.ping.return_value = {"status": "ok"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_ping", {})
            assert not r.isError
            assert json.loads(r.content[0].text)["status"] == "ok"


@pytest.mark.anyio
async def test_wb_seller_info():
    with patch(PATCH) as M:
        M.return_value.get_seller_info.return_value = {"name": "Test", "sid": "123"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_seller_info", {})
            assert not r.isError
            assert json.loads(r.content[0].text)["name"] == "Test"


@pytest.mark.anyio
async def test_wb_seller_rating():
    with patch(PATCH) as M:
        M.return_value.get_seller_rating.return_value = {"rating": 4.5}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_seller_rating", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_news():
    with patch(PATCH) as M:
        M.return_value.get_news.return_value = {"news": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_news", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_subscriptions():
    with patch(PATCH) as M:
        M.return_value.get_subscriptions.return_value = {"subscriptions": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_subscriptions", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_users():
    with patch(PATCH) as M:
        M.return_value.get_users.return_value = {"users": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_users", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_user_invite():
    with patch(PATCH) as M:
        M.return_value.create_user_invite.return_value = {"status": "ok"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_user_invite", {"email": "test@test.com"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_user_access_update():
    with patch(PATCH) as M:
        M.return_value.update_user_access.return_value = {"status": "ok"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_user_access_update", {"user_id": "u1", "permissions_json": "[]"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_user_delete():
    with patch(PATCH) as M:
        M.return_value.delete_user.return_value = {"status": "ok"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_user_delete", {"user_id": "u1"})
            assert not r.isError
