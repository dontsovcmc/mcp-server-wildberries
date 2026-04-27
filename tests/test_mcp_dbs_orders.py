import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_dbs_orders_new():
    with patch(PATCH) as M:
        M.return_value.get_dbs_orders_new.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_dbs_orders_new", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_dbs_orders():
    with patch(PATCH) as M:
        M.return_value.get_dbs_orders.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_dbs_orders", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_dbs_order_confirm():
    with patch(PATCH) as M:
        M.return_value.confirm_dbs_order.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_dbs_order_confirm", {"order_ids_json": "[1]"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_dbs_order_cancel():
    with patch(PATCH) as M:
        M.return_value.cancel_dbs_order.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_dbs_order_cancel", {"order_ids_json": "[1]"})
            assert not r.isError
