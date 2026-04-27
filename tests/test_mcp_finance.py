import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_finance_balance():
    with patch(PATCH) as M:
        M.return_value.get_finance_balance.return_value = {"balance": 50000}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_finance_balance", {})
            assert not r.isError
            assert json.loads(r.content[0].text)["balance"] == 50000


@pytest.mark.anyio
async def test_wb_finance_document_categories():
    with patch(PATCH) as M:
        M.return_value.get_finance_document_categories.return_value = {"categories": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_finance_document_categories", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_finance_sales_reports():
    with patch(PATCH) as M:
        M.return_value.get_finance_sales_reports.return_value = {"reports": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_finance_sales_reports", {"params_json": "{}"})
            assert not r.isError
