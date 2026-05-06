"""Shared MCP instance and helpers for Wildberries tools."""

import json
import logging
import os
import sys

from mcp.server.fastmcp import FastMCP

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger(__name__)

mcp = FastMCP(
    "wildberries",
    instructions=(
        "Wildberries Seller API server. "
        "Use wb_search to discover available actions and their parameter schemas. "
        "Use wb_execute to run actions by ID. "
        "Use wb_execute_file for actions that download files (reports, documents)."
    ),
)

_api = None


def _get_api():
    global _api
    if _api is None:
        from .wb_api import WildberriesAPI

        token = os.getenv("WB_TOKEN")
        if not token:
            raise RuntimeError("WB_TOKEN environment variable is required")
        _api = WildberriesAPI(token)
    return _api


def _to_json(data) -> str:
    return json.dumps(data, ensure_ascii=False)


def _parse_json(raw: str, label: str) -> dict:
    """Parse JSON string with a user-friendly error message."""
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError) as exc:
        raise RuntimeError(f"Invalid JSON in {label}: {exc}") from exc


def _safe_output_path(path: str) -> str:
    """Validate and resolve file path for writing.

    Only allows paths under home directory or system temp.
    Rejects dotfiles/dotdirs under home.
    """
    import tempfile

    real = os.path.realpath(os.path.expanduser(path))
    home = os.path.realpath(os.path.expanduser("~"))
    tmp = os.path.realpath(tempfile.gettempdir())

    if not (real.startswith(home + os.sep) or real.startswith(tmp + os.sep) or real.startswith(tmp)):
        raise RuntimeError(f"Path not allowed: {path}. Only home directory or temp allowed.")

    if real.startswith(home + os.sep):
        relative = real[len(home):]
        if os.sep + "." in relative:
            raise RuntimeError(f"Writing to dotfiles/dotdirs is not allowed: {path}")

    return real


def _save_bytes(data: bytes, path: str) -> str:
    safe = _safe_output_path(path)
    with open(safe, "wb") as f:
        f.write(data)
    return _to_json({"path": safe, "size": len(data)})
