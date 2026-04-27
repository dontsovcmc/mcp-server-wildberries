import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_analytics_sales_funnel():
    with patch(PATCH) as M:
        M.return_value.get_analytics_sales_funnel.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_analytics_sales_funnel", {"params_json": "{}"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_analytics_search_report():
    with patch(PATCH) as M:
        M.return_value.get_analytics_search_report.return_value = {"data": {}}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_analytics_search_report", {"params_json": "{}"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_analytics_csv_list():
    with patch(PATCH) as M:
        M.return_value.get_analytics_csv_reports.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_analytics_csv_list", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_analytics_stocks_wb():
    with patch(PATCH) as M:
        M.return_value.get_analytics_stocks_wb.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_analytics_stocks_wb", {"params_json": "{}"})
            assert not r.isError
