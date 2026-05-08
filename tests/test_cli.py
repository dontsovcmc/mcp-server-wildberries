"""Tests for CLI entry point."""

import subprocess
import sys


def test_help_flag():
    """--help should print usage and exit 0."""
    result = subprocess.run(
        [sys.executable, "-m", "mcp_server_wildberries", "--help"],
        capture_output=True, text=True, timeout=5,
    )
    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()


def test_h_flag():
    """-h should print usage and exit 0."""
    result = subprocess.run(
        [sys.executable, "-m", "mcp_server_wildberries", "-h"],
        capture_output=True, text=True, timeout=5,
    )
    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()


def test_version_flag():
    """--version should print version and exit 0."""
    result = subprocess.run(
        [sys.executable, "-m", "mcp_server_wildberries", "--version"],
        capture_output=True, text=True, timeout=5,
    )
    assert result.returncode == 0
    assert "mcp-server-wildberries" in result.stdout
