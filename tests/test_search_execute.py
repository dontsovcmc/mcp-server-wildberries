"""Tests for search + execute MCP tools."""

import json

import pytest
from unittest.mock import patch, MagicMock

from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


# ── wb_search ──────────────────────────────────────────────────────


@pytest.mark.anyio
async def test_search_returns_results():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_search", {"query": "cancel fbs order"})
        assert not r.isError
        results = json.loads(r.content[0].text)
        assert len(results) > 0
        assert results[0]["id"] == "wb_fbs_order_cancel"


@pytest.mark.anyio
async def test_search_with_domain_filter():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_search", {"query": "orders", "domain": "fbs_orders"})
        results = json.loads(r.content[0].text)
        for item in results:
            assert item["domain"] == "fbs_orders"


@pytest.mark.anyio
async def test_search_returns_params_schema():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_search", {"query": "wb_fbs_order_cancel"})
        results = json.loads(r.content[0].text)
        top = results[0]
        assert "params_schema" in top
        assert top["params_schema"] is not None
        assert "properties" in top["params_schema"]
        assert "order_id" in top["params_schema"]["properties"]


@pytest.mark.anyio
async def test_search_empty_query():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_search", {"query": ""})
        results = json.loads(r.content[0].text)
        assert results == []


@pytest.mark.anyio
async def test_search_no_match():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_search", {"query": "xyznonexistent123"})
        results = json.loads(r.content[0].text)
        assert results == []


@pytest.mark.anyio
async def test_search_file_actions():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_search", {"query": "download warehouse remains"})
        results = json.loads(r.content[0].text)
        file_results = [r for r in results if r["is_file"]]
        assert len(file_results) > 0


@pytest.mark.anyio
async def test_search_destructive_flag():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_search", {"query": "wb_fbs_order_cancel"})
        results = json.loads(r.content[0].text)
        assert results[0]["is_destructive"] is True


# ── wb_execute — no-param actions ──────────────────────────────────


@pytest.mark.anyio
async def test_execute_ping():
    with patch(PATCH) as M:
        M.return_value.ping.return_value = {"status": "ok"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_execute", {
                "action": "wb_ping",
                "params_json": "{}",
            })
            assert not r.isError
            data = json.loads(r.content[0].text)
            assert data["status"] == "ok"


@pytest.mark.anyio
async def test_execute_seller_info():
    with patch(PATCH) as M:
        M.return_value.get_seller_info.return_value = {"name": "Test", "sid": "123"}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_execute", {
                "action": "wb_seller_info",
                "params_json": "{}",
            })
            assert not r.isError
            data = json.loads(r.content[0].text)
            assert data["name"] == "Test"


# ── wb_execute — actions with params ───────────────────────────────


@pytest.mark.anyio
async def test_execute_fbs_order_cancel():
    with patch(PATCH) as M:
        M.return_value.cancel_fbs_order.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_execute", {
                "action": "wb_fbs_order_cancel",
                "params_json": '{"order_id": 12345}',
            })
            assert not r.isError
            M.return_value.cancel_fbs_order.assert_called_once_with(order_id=12345)


@pytest.mark.anyio
async def test_execute_fbs_orders_status():
    with patch(PATCH) as M:
        M.return_value.get_fbs_orders_status.return_value = {"orders": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_execute", {
                "action": "wb_fbs_orders_status",
                "params_json": '{"order_ids": [1, 2, 3]}',
            })
            assert not r.isError
            M.return_value.get_fbs_orders_status.assert_called_once_with(order_ids=[1, 2, 3])


@pytest.mark.anyio
async def test_execute_content_subjects():
    with patch(PATCH) as M:
        M.return_value.get_subjects.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_execute", {
                "action": "wb_content_subjects",
                "params_json": '{"name": "обувь", "top": 10}',
            })
            assert not r.isError
            M.return_value.get_subjects.assert_called_once_with(name="обувь", top=10, offset=0)


@pytest.mark.anyio
async def test_execute_advert_campaign_rename():
    with patch(PATCH) as M:
        M.return_value.rename_advert_campaign.return_value = {}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_execute", {
                "action": "wb_advert_campaign_rename",
                "params_json": '{"campaign_id": 100, "name": "New Name"}',
            })
            assert not r.isError
            M.return_value.rename_advert_campaign.assert_called_once_with(campaign_id=100, name="New Name")


@pytest.mark.anyio
async def test_execute_analytics_sales_funnel():
    with patch(PATCH) as M:
        M.return_value.get_analytics_sales_funnel.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_execute", {
                "action": "wb_analytics_sales_funnel",
                "params_json": '{"selectedPeriod": {"start": "2025-01-01", "end": "2025-01-31"}}',
            })
            assert not r.isError


# ── wb_execute — error cases ───────────────────────────────────────


@pytest.mark.anyio
async def test_execute_unknown_action():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_execute", {
            "action": "nonexistent_action",
            "params_json": "{}",
        })
        assert not r.isError  # returns error in JSON, not MCP error
        data = json.loads(r.content[0].text)
        assert "error" in data


@pytest.mark.anyio
async def test_execute_file_action_via_execute():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_execute", {
            "action": "wb_analytics_csv_download",
            "params_json": '{"download_id": "test"}',
        })
        data = json.loads(r.content[0].text)
        assert "error" in data
        assert "wb_execute_file" in data["error"]


# ── wb_execute_file ────────────────────────────────────────────────


@pytest.mark.anyio
async def test_execute_file_download(tmp_path):
    with patch(PATCH) as M:
        M.return_value.download_analytics_csv_report.return_value = b"col1,col2\n1,2\n"
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            out = str(tmp_path / "report.csv")
            r = await s.call_tool("wb_execute_file", {
                "action": "wb_analytics_csv_download",
                "file_path": out,
                "params_json": '{"download_id": "dl123"}',
            })
            assert not r.isError
            data = json.loads(r.content[0].text)
            assert data["size"] == 14
            assert (tmp_path / "report.csv").read_bytes() == b"col1,col2\n1,2\n"


@pytest.mark.anyio
async def test_execute_file_non_file_action():
    async with create_connected_server_and_client_session(mcp._mcp_server) as s:
        r = await s.call_tool("wb_execute_file", {
            "action": "wb_ping",
            "file_path": "/tmp/test.bin",
            "params_json": "{}",
        })
        data = json.loads(r.content[0].text)
        assert "error" in data
        assert "wb_execute" in data["error"]


# ── Catalog completeness ───────────────────────────────────────────


def test_catalog_has_235_actions():
    from mcp_server_wildberries.actions import ACTIONS
    assert len(ACTIONS) == 235


def test_all_actions_have_api_method():
    from mcp_server_wildberries.actions import ACTIONS
    from mcp_server_wildberries.wb_api import WildberriesAPI

    api_methods = {name for name in dir(WildberriesAPI) if not name.startswith("_")}
    for action in ACTIONS.values():
        assert action.api_method in api_methods, (
            f"Action {action.id} references missing API method: {action.api_method}"
        )


def test_tools_registered():
    """Verify exactly 3 MCP tools are registered."""
    from mcp_server_wildberries.server import mcp
    tool_names = set()
    for tool in mcp._tool_manager._tools.values():
        tool_names.add(tool.name)
    assert "wb_search" in tool_names
    assert "wb_execute" in tool_names
    assert "wb_execute_file" in tool_names
    assert len(tool_names) == 3
