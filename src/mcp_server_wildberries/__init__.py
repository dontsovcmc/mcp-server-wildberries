"""MCP server for Wildberries Seller API."""

import logging
import sys

__version__ = "0.2.1"


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        stream=sys.stderr,
    )
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        from .cli import main as cli_main
        cli_main()
    elif "--version" in sys.argv:
        print(f"mcp-server-wildberries {__version__}")
    elif len(sys.argv) == 1:
        from .server import mcp
        mcp.run(transport="stdio")
    else:
        from .cli import main as cli_main
        cli_main()


if __name__ == "__main__":
    main()
