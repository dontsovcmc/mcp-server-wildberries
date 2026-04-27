import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_pickup_orders_new():
    with patch(PATCH) as M:
        M.return_value.get_pickup_orders_new.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_pickup_orders_new", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_pickup_order_confirm():
    with patch(PATCH) as M:
        M.return_value.confirm_pickup_order.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_pickup_order_confirm", {"order_ids_json": "[1]"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_pickup_orders_completed():
    with patch(PATCH) as M:
        M.return_value.get_pickup_orders_completed.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_pickup_orders_completed", {})
            assert not r.isError
