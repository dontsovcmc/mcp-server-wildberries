import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_wbd_offers():
    with patch(PATCH) as M:
        M.return_value.get_wbd_offers.return_value = {"offers": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_wbd_offers", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_wbd_catalog():
    with patch(PATCH) as M:
        M.return_value.get_wbd_catalog.return_value = {"categories": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_wbd_catalog", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_wbd_keys_count():
    with patch(PATCH) as M:
        M.return_value.get_wbd_keys_count.return_value = {"count": 10}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_wbd_keys_count", {"offer_id": "o1"})
            assert not r.isError
