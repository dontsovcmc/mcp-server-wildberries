import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_tariff_commissions():
    with patch(PATCH) as M:
        M.return_value.get_tariff_commissions.return_value = {"report": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_tariff_commissions", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_tariff_box():
    with patch(PATCH) as M:
        M.return_value.get_tariff_box.return_value = {"response": {"data": []}}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_tariff_box", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_tariff_pallet():
    with patch(PATCH) as M:
        M.return_value.get_tariff_pallet.return_value = {"response": {"data": []}}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_tariff_pallet", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_tariff_acceptance():
    with patch(PATCH) as M:
        M.return_value.get_tariff_acceptance.return_value = {"report": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_tariff_acceptance", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_tariff_return():
    with patch(PATCH) as M:
        M.return_value.get_tariff_return.return_value = {"report": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_tariff_return", {})
            assert not r.isError
