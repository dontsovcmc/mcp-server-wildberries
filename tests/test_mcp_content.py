import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_content_parent_categories():
    with patch(PATCH) as M:
        M.return_value.get_parent_categories.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_content_parent_categories", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_content_subjects():
    with patch(PATCH) as M:
        M.return_value.get_subjects.return_value = {"data": [{"id": 1}]}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_content_subjects", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_content_characteristics():
    with patch(PATCH) as M:
        M.return_value.get_characteristics.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_content_characteristics", {"subject_id": 1})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_content_colors():
    with patch(PATCH) as M:
        M.return_value.get_colors.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_content_colors", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_content_tags():
    with patch(PATCH) as M:
        M.return_value.get_tags.return_value = {"data": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_content_tags", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_content_tag_create():
    with patch(PATCH) as M:
        M.return_value.create_tag.return_value = {"id": 1}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_content_tag_create", {"name": "test"})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_content_cards_list():
    with patch(PATCH) as M:
        M.return_value.get_cards_list.return_value = {"cards": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_content_cards_list", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_content_cards_errors():
    with patch(PATCH) as M:
        M.return_value.get_cards_errors.return_value = {"errors": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_content_cards_errors", {})
            assert not r.isError
