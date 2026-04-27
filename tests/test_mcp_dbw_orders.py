import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_dbw_orders_new():
    with patch(PATCH) as M:
        M.return_value.get_dbw_orders_new.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_dbw_orders_new", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_dbw_orders():
    with patch(PATCH) as M:
        M.return_value.get_dbw_orders.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_dbw_orders", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_dbw_order_confirm():
    with patch(PATCH) as M:
        M.return_value.confirm_dbw_order.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_dbw_order_confirm", {"order_id": 1})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_dbw_order_cancel():
    with patch(PATCH) as M:
        M.return_value.cancel_dbw_order.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_dbw_order_cancel", {"order_id": 1})
            assert not r.isError
