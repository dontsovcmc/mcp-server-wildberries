import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_fbs_orders_new():
    with patch(PATCH) as M:
        M.return_value.get_fbs_orders_new.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbs_orders_new", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_fbs_orders():
    with patch(PATCH) as M:
        M.return_value.get_fbs_orders.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbs_orders", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_fbs_order_cancel():
    with patch(PATCH) as M:
        M.return_value.cancel_fbs_order.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbs_order_cancel", {"order_id": 123})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_fbs_stickers():
    with patch(PATCH) as M:
        M.return_value.get_fbs_stickers.return_value = {"stickers": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbs_stickers", {"order_ids_json": "[123]"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_fbs_supply_create():
    with patch(PATCH) as M:
        M.return_value.create_fbs_supply.return_value = {"id": "WB-GI-123"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbs_supply_create", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_fbs_supplies():
    with patch(PATCH) as M:
        M.return_value.get_fbs_supplies.return_value = {"supplies": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbs_supplies", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_fbs_passes():
    with patch(PATCH) as M:
        M.return_value.get_fbs_passes.return_value = {"passes": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbs_passes", {})
            assert not r.isError
