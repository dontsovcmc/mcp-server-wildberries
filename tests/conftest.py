import os

import pytest

os.environ.setdefault("WB_TOKEN", "test-fake-token")


@pytest.fixture(autouse=True)
def _reset_api_cache():
    """Reset cached API instance between tests."""
    import mcp_server_wildberries._shared as shared
    import mcp_server_wildberries.server as srv
    shared._api = None
    srv._api = None
    yield
    shared._api = None
    srv._api = None
