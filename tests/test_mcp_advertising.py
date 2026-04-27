import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_advert_campaigns_count():
    with patch(PATCH) as M:
        M.return_value.get_advert_campaigns_count.return_value = {"all": 5}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_advert_campaigns_count", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_advert_balance():
    with patch(PATCH) as M:
        M.return_value.get_advert_balance.return_value = {"balance": 1000}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_advert_balance", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_advert_campaign_start():
    with patch(PATCH) as M:
        M.return_value.start_advert_campaign.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_advert_campaign_start", {"campaign_id": 1})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_advert_campaign_pause():
    with patch(PATCH) as M:
        M.return_value.pause_advert_campaign.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_advert_campaign_pause", {"campaign_id": 1})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_advert_subjects():
    with patch(PATCH) as M:
        M.return_value.get_advert_subjects.return_value = {"subjects": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_advert_subjects", {})
            assert not r.isError
