import json
import pytest
from unittest.mock import patch
from mcp.shared.memory import create_connected_server_and_client_session
from mcp_server_wildberries.server import mcp


PATCH = "mcp_server_wildberries.wb_api.WildberriesAPI"


@pytest.mark.anyio
async def test_wb_new_feedbacks_questions():
    with patch(PATCH) as M:
        M.return_value.get_new_feedbacks_questions.return_value = {"data": {}}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_new_feedbacks_questions", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_questions():
    with patch(PATCH) as M:
        M.return_value.get_questions.return_value = {"data": {"questions": []}}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_questions", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_feedbacks():
    with patch(PATCH) as M:
        M.return_value.get_feedbacks.return_value = {"data": {"feedbacks": []}}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_feedbacks", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_chats():
    with patch(PATCH) as M:
        M.return_value.get_chats.return_value = {"chats": []}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_chats", {})
            assert not r.isError


@pytest.mark.anyio
async def test_wb_feedback_pins_limits():
    with patch(PATCH) as M:
        M.return_value.get_pinned_feedbacks_limits.return_value = {"limits": {}}
        async with create_connected_server_and_client_session(mcp._mcp_server) as s:
            r = await s.call_tool("wb_feedback_pins_limits", {})
            assert not r.isError
