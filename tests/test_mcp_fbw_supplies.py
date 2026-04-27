import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_fbw_warehouses():
    with patch(PATCH) as M:
        M.return_value.get_fbw_warehouses.return_value = {"warehouses": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbw_warehouses", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_fbw_transit_tariffs():
    with patch(PATCH) as M:
        M.return_value.get_fbw_transit_tariffs.return_value = {"tariffs": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbw_transit_tariffs", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_fbw_supply():
    with patch(PATCH) as M:
        M.return_value.get_fbw_supply.return_value = {"id": "123"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_fbw_supply", {"supply_id": "123"})
            assert not r.isError
