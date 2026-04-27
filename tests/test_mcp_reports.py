import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_report_orders():
    with patch(PATCH) as M:
        M.return_value.get_report_orders.return_value = [{"orderId": 1}]
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_report_orders", {"date_from": "2024-01-01"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_report_sales():
    with patch(PATCH) as M:
        M.return_value.get_report_sales.return_value = [{"saleID": "s1"}]
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_report_sales", {"date_from": "2024-01-01"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_report_warehouse_remains_create():
    with patch(PATCH) as M:
        M.return_value.create_report_warehouse_remains.return_value = {"data": {"taskId": "t1"}}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_report_warehouse_remains_create", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_report_regional_sales():
    with patch(PATCH) as M:
        M.return_value.get_report_regional_sales.return_value = {"report": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_report_regional_sales", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_report_returns():
    with patch(PATCH) as M:
        M.return_value.get_report_returns.return_value = {"report": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_report_returns", {})
            assert not r.isError
