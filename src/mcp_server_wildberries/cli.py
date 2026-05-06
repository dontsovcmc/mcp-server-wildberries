"""CLI interface for Wildberries tools.

Usage: mcp-server-wildberries <command> [options]
Without arguments starts MCP server (stdio transport).
"""

import argparse
import json
import sys

from . import __version__


def _j(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def _api():
    import os
    from .wb_api import WildberriesAPI

    token = os.getenv("WB_TOKEN")
    if not token:
        print("Error: WB_TOKEN environment variable is required", file=sys.stderr)
        sys.exit(1)
    return WildberriesAPI(token)


def _load_json(raw: str) -> dict | list:
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError) as exc:
        print(f"Error: invalid JSON: {exc}", file=sys.stderr)
        sys.exit(1)


def main(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(
        prog="mcp-server-wildberries",
        description="Wildberries Seller: MCP-сервер и CLI",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command")

    # ── Search & Execute ──────────────────────────────────────────────

    p = sub.add_parser("search", help="Search available API actions")
    p.add_argument("query", nargs="+")
    p.add_argument("--domain", default="")
    p.add_argument("--limit", type=int, default=10)

    p = sub.add_parser("execute", help="Execute an action by ID")
    p.add_argument("action_id")
    p.add_argument("--params", default="{}")

    p = sub.add_parser("execute-file", help="Execute a file download action")
    p.add_argument("action_id")
    p.add_argument("output_path")
    p.add_argument("--params", default="{}")

    # ── General ────────────────────────────────────────────────────────

    sub.add_parser("ping", help="Check API availability")

    sub.add_parser("news", help="Get seller portal news")

    sub.add_parser("seller-info", help="Get seller name and profile ID")

    sub.add_parser("seller-rating", help="Get seller rating and review count")

    sub.add_parser("subscriptions", help="Get notification subscriptions")

    p = sub.add_parser("user-invite", help="Create user invitation")
    p.add_argument("email")
    p.add_argument("--permissions-json", default="[]")

    sub.add_parser("users", help="Get list of users")

    p = sub.add_parser("user-access-update", help="Update user access permissions")
    p.add_argument("user_id")
    p.add_argument("permissions_json")

    p = sub.add_parser("user-delete", help="Delete user")
    p.add_argument("user_id")

    # ── Content ────────────────────────────────────────────────────────

    sub.add_parser("content-parent-categories", help="Get parent categories")

    p = sub.add_parser("content-subjects", help="Get all subjects (categories)")
    p.add_argument("--name", default="")
    p.add_argument("--top", type=int, default=50)
    p.add_argument("--offset", type=int, default=0)

    p = sub.add_parser("content-characteristics", help="Get subject characteristics")
    p.add_argument("subject_id", type=int)

    sub.add_parser("content-colors", help="Get color directory")

    sub.add_parser("content-kinds", help="Get gender directory")

    sub.add_parser("content-countries", help="Get country of origin directory")

    sub.add_parser("content-seasons", help="Get season directory")

    sub.add_parser("content-vat", help="Get VAT rates")

    p = sub.add_parser("content-tnved", help="Get TNVED codes for subject")
    p.add_argument("subject_id", type=int)

    p = sub.add_parser("content-brands", help="Get brands")
    p.add_argument("--pattern", default="")

    sub.add_parser("content-tags", help="Get seller tags")

    p = sub.add_parser("content-tag-create", help="Create tag")
    p.add_argument("name")
    p.add_argument("--color", default="")

    p = sub.add_parser("content-tag-update", help="Update tag")
    p.add_argument("tag_id", type=int)
    p.add_argument("name")
    p.add_argument("--color", default="")

    p = sub.add_parser("content-tag-delete", help="Delete tag")
    p.add_argument("tag_id", type=int)

    p = sub.add_parser("content-tag-link", help="Link tag to products")
    p.add_argument("nm_ids_json")
    p.add_argument("tag_id", type=int)

    p = sub.add_parser("content-cards-list", help="Get product cards list")
    p.add_argument("--cursor-json", default="")
    p.add_argument("--filter-json", default="")

    sub.add_parser("content-cards-errors", help="Get card upload errors")

    p = sub.add_parser("content-cards-update", help="Update product cards")
    p.add_argument("cards_json")

    # ── FBS Orders ─────────────────────────────────────────────────────

    sub.add_parser("fbs-orders-new", help="Get new FBS assembly orders")

    p = sub.add_parser("fbs-orders", help="Get FBS orders")
    p.add_argument("--date-from", default="")
    p.add_argument("--date-to", default="")
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--next", type=int, default=0, dest="next_val")

    p = sub.add_parser("fbs-orders-status", help="Get FBS order statuses")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-order-cancel", help="Cancel FBS order")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("fbs-stickers", help="Get FBS order stickers")
    p.add_argument("order_ids_json")
    p.add_argument("--type", default="svg", dest="sticker_type")
    p.add_argument("--width", type=int, default=58)
    p.add_argument("--height", type=int, default=40)

    p = sub.add_parser("fbs-stickers-cross-border", help="Get cross-border stickers")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-orders-status-history", help="Get FBS order status history")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-orders-client", help="Get FBS order client info")
    p.add_argument("order_ids_json")

    sub.add_parser("fbs-reshipment-orders", help="Get FBS reshipment orders")

    p = sub.add_parser("fbs-order-meta", help="Get FBS order metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-order-meta-delete", help="Delete FBS order metadata")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("fbs-order-meta-sgtin", help="Set Honest Sign codes for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("sgtins_json")

    p = sub.add_parser("fbs-order-meta-uin", help="Set UIN for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("uin")

    p = sub.add_parser("fbs-order-meta-imei", help="Set IMEI for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("imei")

    p = sub.add_parser("fbs-order-meta-gtin", help="Set GTIN for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("gtin")

    p = sub.add_parser("fbs-order-meta-expiration", help="Set expiration date for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("date")

    p = sub.add_parser("fbs-order-meta-customs", help="Set customs declaration for FBS order")
    p.add_argument("order_id", type=int)
    p.add_argument("declaration")

    p = sub.add_parser("fbs-supply-create", help="Create FBS supply")
    p.add_argument("--name", default="")

    p = sub.add_parser("fbs-supplies", help="Get FBS supplies list")
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--next", type=int, default=0, dest="next_val")

    p = sub.add_parser("fbs-supply-add-orders", help="Add orders to FBS supply")
    p.add_argument("supply_id")
    p.add_argument("order_ids_json")

    p = sub.add_parser("fbs-supply", help="Get FBS supply details")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-delete", help="Delete FBS supply")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-orders", help="Get FBS supply order IDs")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-deliver", help="Deliver FBS supply")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-barcode", help="Get FBS supply barcode")
    p.add_argument("supply_id")

    p = sub.add_parser("fbs-supply-boxes", help="Get FBS supply boxes")
    p.add_argument("supply_id")

    sub.add_parser("fbs-pass-offices", help="Get warehouses requiring access pass")
    sub.add_parser("fbs-passes", help="Get all access passes")

    p = sub.add_parser("fbs-pass-create", help="Create access pass")
    p.add_argument("params_json")

    p = sub.add_parser("fbs-pass-update", help="Update access pass")
    p.add_argument("pass_id", type=int)
    p.add_argument("params_json")

    p = sub.add_parser("fbs-pass-delete", help="Delete access pass")
    p.add_argument("pass_id", type=int)

    # ── DBW Orders ─────────────────────────────────────────────────────

    sub.add_parser("dbw-orders-new", help="Get new DBW assembly tasks")
    sub.add_parser("dbw-orders", help="Get completed DBW assembly tasks")

    p = sub.add_parser("dbw-delivery-date", help="Get DBW delivery dates")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-client", help="Get DBW client info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-orders-status", help="Get DBW order statuses")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-order-confirm", help="Confirm DBW order")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-stickers", help="Get DBW stickers")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-order-assemble", help="Move DBW order to delivery")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-courier", help="Get DBW courier info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbw-order-cancel", help="Cancel DBW order")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-order-meta", help="Get DBW order metadata")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-order-meta-delete", help="Delete DBW order metadata")
    p.add_argument("order_id", type=int)

    p = sub.add_parser("dbw-order-meta-sgtin", help="Set Honest Sign codes for DBW order")
    p.add_argument("order_id", type=int)
    p.add_argument("sgtins_json")

    p = sub.add_parser("dbw-order-meta-uin", help="Set UIN for DBW order")
    p.add_argument("order_id", type=int)
    p.add_argument("uin")

    p = sub.add_parser("dbw-order-meta-imei", help="Set IMEI for DBW order")
    p.add_argument("order_id", type=int)
    p.add_argument("imei")

    p = sub.add_parser("dbw-order-meta-gtin", help="Set GTIN for DBW order")
    p.add_argument("order_id", type=int)
    p.add_argument("gtin")

    # ── DBS Orders ─────────────────────────────────────────────────────

    sub.add_parser("dbs-orders-new", help="Get new DBS orders")
    sub.add_parser("dbs-orders", help="Get completed DBS orders")

    p = sub.add_parser("dbs-groups-info", help="Get DBS paid delivery info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-client", help="Get DBS client info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-b2b-info", help="Get DBS B2B buyer info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-delivery-date", help="Get DBS delivery dates")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-orders-status", help="Get DBS order statuses")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-cancel", help="Cancel DBS order")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-confirm", help="Confirm DBS order")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-stickers", help="Get DBS stickers")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-deliver", help="Move DBS order to delivery")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-receive", help="Confirm DBS order receipt")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-reject", help="Record DBS order rejection")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-meta", help="Get DBS order metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-meta-delete", help="Delete DBS order metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("dbs-order-meta-sgtin", help="Set Honest Sign for DBS")
    p.add_argument("orders_json")

    p = sub.add_parser("dbs-order-meta-uin", help="Set UIN for DBS")
    p.add_argument("orders_json")

    p = sub.add_parser("dbs-order-meta-imei", help="Set IMEI for DBS")
    p.add_argument("orders_json")

    p = sub.add_parser("dbs-order-meta-gtin", help="Set GTIN for DBS")
    p.add_argument("orders_json")

    p = sub.add_parser("dbs-order-meta-customs", help="Set customs for DBS")
    p.add_argument("orders_json")

    # ── Pickup Orders ──────────────────────────────────────────────────

    sub.add_parser("pickup-orders-new", help="Get new pickup orders")

    p = sub.add_parser("pickup-order-confirm", help="Confirm pickup order")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-prepare", help="Mark pickup order as ready")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-client", help="Get pickup client info")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-verify-identity", help="Verify pickup ownership")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-receive", help="Confirm pickup receipt")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-reject", help="Record pickup rejection")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-orders-status", help="Get pickup statuses")
    p.add_argument("order_ids_json")

    sub.add_parser("pickup-orders-completed", help="Get completed pickups")

    p = sub.add_parser("pickup-order-cancel", help="Cancel pickup order")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-meta", help="Get pickup metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-meta-delete", help="Delete pickup metadata")
    p.add_argument("order_ids_json")

    p = sub.add_parser("pickup-order-meta-sgtin", help="Set Honest Sign for pickup")
    p.add_argument("orders_json")

    p = sub.add_parser("pickup-order-meta-uin", help="Set UIN for pickup")
    p.add_argument("orders_json")

    p = sub.add_parser("pickup-order-meta-imei", help="Set IMEI for pickup")
    p.add_argument("orders_json")

    p = sub.add_parser("pickup-order-meta-gtin", help="Set GTIN for pickup")
    p.add_argument("orders_json")

    # ── FBW Supplies ───────────────────────────────────────────────────

    p = sub.add_parser("fbw-acceptance-options", help="Get FBW acceptance options")
    p.add_argument("params_json")

    sub.add_parser("fbw-warehouses", help="Get WB warehouse list")
    sub.add_parser("fbw-transit-tariffs", help="Get transit tariffs")

    p = sub.add_parser("fbw-supplies", help="Get FBW supplies list")
    p.add_argument("--params-json", default="")

    p = sub.add_parser("fbw-supply", help="Get FBW supply details")
    p.add_argument("supply_id")

    p = sub.add_parser("fbw-supply-goods", help="Get FBW supply goods")
    p.add_argument("supply_id")

    p = sub.add_parser("fbw-supply-package", help="Get FBW supply package info")
    p.add_argument("supply_id")

    # ── Advertising ────────────────────────────────────────────────────

    sub.add_parser("advert-campaigns-count", help="Get campaign counts")

    p = sub.add_parser("advert-campaigns", help="Get campaign details")
    p.add_argument("campaign_ids_json")

    p = sub.add_parser("advert-min-bids", help="Get minimum bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-campaign-create", help="Create campaign")
    p.add_argument("params_json")

    sub.add_parser("advert-subjects", help="Get ad categories")

    p = sub.add_parser("advert-nms", help="Get product cards for ads")
    p.add_argument("params_json")

    p = sub.add_parser("advert-campaign-delete", help="Delete campaign")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-campaign-rename", help="Rename campaign")
    p.add_argument("campaign_id", type=int)
    p.add_argument("name")

    p = sub.add_parser("advert-campaign-start", help="Start campaign")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-campaign-pause", help="Pause campaign")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-campaign-stop", help="Stop campaign")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-placements-update", help="Update placements")
    p.add_argument("params_json")

    p = sub.add_parser("advert-bids-update", help="Update bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-nms-update", help="Manage cards in campaign")
    p.add_argument("params_json")

    p = sub.add_parser("advert-bid-recommendations", help="Get bid recommendations")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-search-bids", help="Get search bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-search-bids-set", help="Set search bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-search-bids-delete", help="Delete search bids")
    p.add_argument("params_json")

    p = sub.add_parser("advert-minus-phrases", help="Get minus phrases")
    p.add_argument("params_json")

    p = sub.add_parser("advert-minus-phrases-set", help="Set minus phrases")
    p.add_argument("params_json")

    sub.add_parser("advert-balance", help="Get ad balance")

    p = sub.add_parser("advert-budget", help="Get campaign budget")
    p.add_argument("campaign_id", type=int)

    p = sub.add_parser("advert-budget-deposit", help="Deposit budget")
    p.add_argument("campaign_id", type=int)
    p.add_argument("amount", type=int)

    p = sub.add_parser("advert-cost-history", help="Get ad cost history")
    p.add_argument("--date-from", default="")
    p.add_argument("--date-to", default="")

    p = sub.add_parser("advert-payments", help="Get ad payments")
    p.add_argument("--date-from", default="")
    p.add_argument("--date-to", default="")

    p = sub.add_parser("advert-search-stats", help="Get search stats")
    p.add_argument("params_json")

    # ── Communications ─────────────────────────────────────────────────

    sub.add_parser("new-feedbacks-questions", help="Get unread count")
    sub.add_parser("questions-unanswered-count", help="Unanswered questions count")

    p = sub.add_parser("questions-count", help="Question count for period")
    p.add_argument("date_from")
    p.add_argument("date_to")

    p = sub.add_parser("questions", help="Get questions list")
    p.add_argument("--is-answered", action="store_true")
    p.add_argument("--take", type=int, default=100)
    p.add_argument("--skip", type=int, default=0)

    p = sub.add_parser("question-manage", help="Manage question")
    p.add_argument("question_id")
    p.add_argument("action")
    p.add_argument("--answer", default="")

    p = sub.add_parser("question", help="Get question")
    p.add_argument("question_id")

    sub.add_parser("feedbacks-unanswered-count", help="Unprocessed reviews count")

    p = sub.add_parser("feedbacks-count", help="Review count for period")
    p.add_argument("date_from")
    p.add_argument("date_to")

    p = sub.add_parser("feedbacks", help="Get reviews list")
    p.add_argument("--is-answered", action="store_true")
    p.add_argument("--take", type=int, default=100)
    p.add_argument("--skip", type=int, default=0)

    p = sub.add_parser("feedback-answer", help="Answer review")
    p.add_argument("feedback_id")
    p.add_argument("text")

    p = sub.add_parser("feedback-answer-edit", help="Edit review answer")
    p.add_argument("feedback_id")
    p.add_argument("text")

    p = sub.add_parser("feedback-return", help="Request return")
    p.add_argument("feedback_id")

    p = sub.add_parser("feedback", help="Get review")
    p.add_argument("feedback_id")

    p = sub.add_parser("feedbacks-archive", help="Get archived reviews")
    p.add_argument("--take", type=int, default=100)
    p.add_argument("--skip", type=int, default=0)

    p = sub.add_parser("feedback-pins", help="Get pinned reviews")
    p.add_argument("nm_id", type=int)

    p = sub.add_parser("feedback-pin", help="Pin review")
    p.add_argument("feedback_id")
    p.add_argument("nm_id", type=int)

    p = sub.add_parser("feedback-unpin", help="Unpin review")
    p.add_argument("feedback_id")
    p.add_argument("nm_id", type=int)

    p = sub.add_parser("feedback-pins-count", help="Pinned count")
    p.add_argument("nm_id", type=int)

    sub.add_parser("feedback-pins-limits", help="Pinning limits")

    sub.add_parser("chats", help="Get chats list")
    sub.add_parser("chat-events", help="Get chat events")

    p = sub.add_parser("chat-send", help="Send chat message")
    p.add_argument("chat_id")
    p.add_argument("text")

    # ── Tariffs ────────────────────────────────────────────────────────

    sub.add_parser("tariff-commissions", help="Get commissions")

    p = sub.add_parser("tariff-box", help="Get box tariffs")
    p.add_argument("--date", default="")

    p = sub.add_parser("tariff-pallet", help="Get pallet tariffs")
    p.add_argument("--date", default="")

    sub.add_parser("tariff-acceptance", help="Get acceptance coefficients")
    sub.add_parser("tariff-return", help="Get return tariffs")

    # ── Analytics ──────────────────────────────────────────────────────

    p = sub.add_parser("analytics-sales-funnel", help="Sales funnel")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-sales-funnel-history", help="Funnel history")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-sales-funnel-grouped", help="Grouped funnel")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-report", help="Search report")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-groups", help="Search groups")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-details", help="Search details")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-texts", help="Search texts")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-search-orders", help="Orders by search")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-wb", help="WB warehouse stocks")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-groups", help="Grouped stocks")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-products", help="Product stocks")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-sizes", help="Stocks by size")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-stocks-offices", help="Warehouse stocks")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-csv-create", help="Create CSV report")
    p.add_argument("params_json")

    sub.add_parser("analytics-csv-list", help="List CSV reports")

    p = sub.add_parser("analytics-csv-retry", help="Retry CSV report")
    p.add_argument("params_json")

    p = sub.add_parser("analytics-csv-download", help="Download CSV report")
    p.add_argument("download_id")
    p.add_argument("output_path")

    # ── Reports ────────────────────────────────────────────────────────

    p = sub.add_parser("report-orders", help="Get orders report")
    p.add_argument("date_from")
    p.add_argument("--flag", type=int, default=0)

    p = sub.add_parser("report-sales", help="Get sales report")
    p.add_argument("date_from")
    p.add_argument("--flag", type=int, default=0)

    sub.add_parser("report-warehouse-remains-create", help="Create remains report")

    p = sub.add_parser("report-warehouse-remains-status", help="Check remains status")
    p.add_argument("task_id")

    p = sub.add_parser("report-warehouse-remains-download", help="Download remains")
    p.add_argument("task_id")
    p.add_argument("output_path")

    p = sub.add_parser("report-excise", help="Excise report")
    p.add_argument("params_json")

    sub.add_parser("report-measurement-penalties", help="Measurement deductions")
    sub.add_parser("report-warehouse-measurements", help="Warehouse measurements")
    sub.add_parser("report-deductions", help="Substitution deductions")
    sub.add_parser("report-antifraud", help="Self-purchase deductions")
    sub.add_parser("report-labeling", help="Marking penalties")
    sub.add_parser("report-acceptance-create", help="Create acceptance report")

    p = sub.add_parser("report-acceptance-status", help="Check acceptance status")
    p.add_argument("task_id")

    p = sub.add_parser("report-acceptance-download", help="Download acceptance")
    p.add_argument("task_id")
    p.add_argument("output_path")

    sub.add_parser("report-paid-storage-create", help="Create storage report")

    p = sub.add_parser("report-paid-storage-status", help="Check storage status")
    p.add_argument("task_id")

    p = sub.add_parser("report-paid-storage-download", help="Download storage")
    p.add_argument("task_id")
    p.add_argument("output_path")

    sub.add_parser("report-regional-sales", help="Regional sales report")
    sub.add_parser("report-brands", help="Seller brands")
    sub.add_parser("report-brand-categories", help="Brand categories")

    p = sub.add_parser("report-brand-share", help="Brand share report")
    p.add_argument("--params-json", default="")

    sub.add_parser("report-blocked-products", help="Blocked products")
    sub.add_parser("report-shadowed-products", help="Shadowed products")
    sub.add_parser("report-returns", help="Returns report")

    # ── Finance ────────────────────────────────────────────────────────

    sub.add_parser("finance-balance", help="Get balance")

    p = sub.add_parser("finance-sales-reports", help="Sales reports list")
    p.add_argument("params_json")

    p = sub.add_parser("finance-sales-report-detail", help="Sales report detail")
    p.add_argument("report_id", type=int)

    p = sub.add_parser("finance-sales-report-by-period", help="Sales by period")
    p.add_argument("params_json")

    p = sub.add_parser("finance-report-detail-by-period", help="Realization report")
    p.add_argument("date_from")
    p.add_argument("date_to")
    p.add_argument("--limit", type=int, default=100000)

    p = sub.add_parser("finance-acquiring-reports", help="Acquiring reports")
    p.add_argument("params_json")

    p = sub.add_parser("finance-acquiring-detail", help="Acquiring detail")
    p.add_argument("report_id", type=int)

    p = sub.add_parser("finance-acquiring-by-period", help="Acquiring by period")
    p.add_argument("params_json")

    sub.add_parser("finance-document-categories", help="Document categories")

    p = sub.add_parser("finance-documents", help="Documents list")
    p.add_argument("--params-json", default="")

    p = sub.add_parser("finance-document-download", help="Download document")
    p.add_argument("doc_id")
    p.add_argument("output_path")

    p = sub.add_parser("finance-documents-download", help="Download documents")
    p.add_argument("doc_ids_json")
    p.add_argument("output_path")

    # ── WBD (Digital) ──────────────────────────────────────────────────

    p = sub.add_parser("wbd-keys-add", help="Add activation keys")
    p.add_argument("offer_id")
    p.add_argument("keys_json")

    p = sub.add_parser("wbd-keys-delete", help="Delete activation keys")
    p.add_argument("offer_id")
    p.add_argument("keys_json")

    p = sub.add_parser("wbd-keys-redeemed", help="Get redeemed keys")
    p.add_argument("offer_id")

    p = sub.add_parser("wbd-keys-count", help="Get key count")
    p.add_argument("offer_id")

    p = sub.add_parser("wbd-keys-list", help="Get keys list")
    p.add_argument("offer_id")

    p = sub.add_parser("wbd-offer-create", help="Create digital offer")
    p.add_argument("params_json")

    p = sub.add_parser("wbd-offer-update", help="Update digital offer")
    p.add_argument("offer_id")
    p.add_argument("params_json")

    p = sub.add_parser("wbd-offer", help="Get digital offer")
    p.add_argument("offer_id")

    sub.add_parser("wbd-offers", help="Get digital offers list")

    p = sub.add_parser("wbd-offer-price", help="Update offer price")
    p.add_argument("offer_id")
    p.add_argument("price", type=int)

    p = sub.add_parser("wbd-offer-status", help="Update offer status")
    p.add_argument("offer_id")
    p.add_argument("status")

    sub.add_parser("wbd-catalog", help="Get WBD catalog")

    # ── Parse & dispatch ───────────────────────────────────────────────

    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Search & execute commands
    if args.command == "search":
        from .server import _search_actions
        print(_j(_search_actions(" ".join(args.query), args.domain, args.limit)))
        return

    if args.command == "execute":
        from .server import wb_execute
        print(wb_execute(args.action_id, args.params))
        return

    if args.command == "execute-file":
        from .server import wb_execute_file
        print(wb_execute_file(args.action_id, args.output_path, args.params))
        return

    api = _api()

    # File download helpers
    def _download(data: bytes, path: str) -> str:
        import os
        with open(path, "wb") as f:
            f.write(data)
        return _j({"path": os.path.abspath(path), "size": len(data)})

    handlers = {
        # General
        "ping": lambda: _j(api.ping()),
        "news": lambda: _j(api.get_news()),
        "seller-info": lambda: _j(api.get_seller_info()),
        "seller-rating": lambda: _j(api.get_seller_rating()),
        "subscriptions": lambda: _j(api.get_subscriptions()),
        "user-invite": lambda: _j(api.create_user_invite(args.email, _load_json(args.permissions_json))),
        "users": lambda: _j(api.get_users()),
        "user-access-update": lambda: _j(api.update_user_access(args.user_id, _load_json(args.permissions_json))),
        "user-delete": lambda: _j(api.delete_user(args.user_id)),
        # Content
        "content-parent-categories": lambda: _j(api.get_parent_categories()),
        "content-subjects": lambda: _j(api.get_subjects(args.name, args.top, args.offset)),
        "content-characteristics": lambda: _j(api.get_characteristics(args.subject_id)),
        "content-colors": lambda: _j(api.get_colors()),
        "content-kinds": lambda: _j(api.get_kinds()),
        "content-countries": lambda: _j(api.get_countries()),
        "content-seasons": lambda: _j(api.get_seasons()),
        "content-vat": lambda: _j(api.get_vat()),
        "content-tnved": lambda: _j(api.get_tnved(args.subject_id)),
        "content-brands": lambda: _j(api.get_brands(args.pattern)),
        "content-tags": lambda: _j(api.get_tags()),
        "content-tag-create": lambda: _j(api.create_tag(args.name, args.color)),
        "content-tag-update": lambda: _j(api.update_tag(args.tag_id, args.name, args.color)),
        "content-tag-delete": lambda: _j(api.delete_tag(args.tag_id)),
        "content-tag-link": lambda: _j(api.link_tags(_load_json(args.nm_ids_json), args.tag_id)),
        "content-cards-list": lambda: _j(api.get_cards_list(
            _load_json(args.cursor_json) if args.cursor_json else None,
            _load_json(args.filter_json) if args.filter_json else None,
        )),
        "content-cards-errors": lambda: _j(api.get_cards_errors()),
        "content-cards-update": lambda: _j(api.update_cards(_load_json(args.cards_json))),
        # FBS Orders
        "fbs-orders-new": lambda: _j(api.get_fbs_orders_new()),
        "fbs-orders": lambda: _j(api.get_fbs_orders(args.date_from, args.date_to, args.limit, args.next_val)),
        "fbs-orders-status": lambda: _j(api.get_fbs_orders_status(_load_json(args.order_ids_json))),
        "fbs-order-cancel": lambda: _j(api.cancel_fbs_order(args.order_id)),
        "fbs-stickers": lambda: _j(api.get_fbs_stickers(_load_json(args.order_ids_json), args.sticker_type, args.width, args.height)),
        "fbs-stickers-cross-border": lambda: _j(api.get_fbs_stickers_cross_border(_load_json(args.order_ids_json))),
        "fbs-orders-status-history": lambda: _j(api.get_fbs_orders_status_history(_load_json(args.order_ids_json))),
        "fbs-orders-client": lambda: _j(api.get_fbs_orders_client(_load_json(args.order_ids_json))),
        "fbs-reshipment-orders": lambda: _j(api.get_fbs_reshipment_orders()),
        "fbs-order-meta": lambda: _j(api.get_fbs_order_meta(_load_json(args.order_ids_json))),
        "fbs-order-meta-delete": lambda: _j(api.delete_fbs_order_meta(args.order_id)),
        "fbs-order-meta-sgtin": lambda: _j(api.set_fbs_order_sgtin(args.order_id, _load_json(args.sgtins_json))),
        "fbs-order-meta-uin": lambda: _j(api.set_fbs_order_uin(args.order_id, args.uin)),
        "fbs-order-meta-imei": lambda: _j(api.set_fbs_order_imei(args.order_id, args.imei)),
        "fbs-order-meta-gtin": lambda: _j(api.set_fbs_order_gtin(args.order_id, args.gtin)),
        "fbs-order-meta-expiration": lambda: _j(api.set_fbs_order_expiration(args.order_id, args.date)),
        "fbs-order-meta-customs": lambda: _j(api.set_fbs_order_customs(args.order_id, args.declaration)),
        "fbs-supply-create": lambda: _j(api.create_fbs_supply(args.name)),
        "fbs-supplies": lambda: _j(api.get_fbs_supplies(args.limit, args.next_val)),
        "fbs-supply-add-orders": lambda: _j(api.add_fbs_supply_orders(args.supply_id, _load_json(args.order_ids_json))),
        "fbs-supply": lambda: _j(api.get_fbs_supply(args.supply_id)),
        "fbs-supply-delete": lambda: _j(api.delete_fbs_supply(args.supply_id)),
        "fbs-supply-orders": lambda: _j(api.get_fbs_supply_orders(args.supply_id)),
        "fbs-supply-deliver": lambda: _j(api.deliver_fbs_supply(args.supply_id)),
        "fbs-supply-barcode": lambda: _j(api.get_fbs_supply_barcode(args.supply_id)),
        "fbs-supply-boxes": lambda: _j(api.get_fbs_supply_boxes(args.supply_id)),
        "fbs-pass-offices": lambda: _j(api.get_fbs_pass_offices()),
        "fbs-passes": lambda: _j(api.get_fbs_passes()),
        "fbs-pass-create": lambda: _j(api.create_fbs_pass(_load_json(args.params_json))),
        "fbs-pass-update": lambda: _j(api.update_fbs_pass(args.pass_id, _load_json(args.params_json))),
        "fbs-pass-delete": lambda: _j(api.delete_fbs_pass(args.pass_id)),
        # DBW Orders
        "dbw-orders-new": lambda: _j(api.get_dbw_orders_new()),
        "dbw-orders": lambda: _j(api.get_dbw_orders()),
        "dbw-delivery-date": lambda: _j(api.get_dbw_delivery_date(_load_json(args.order_ids_json))),
        "dbw-client": lambda: _j(api.get_dbw_client(_load_json(args.order_ids_json))),
        "dbw-orders-status": lambda: _j(api.get_dbw_orders_status(_load_json(args.order_ids_json))),
        "dbw-order-confirm": lambda: _j(api.confirm_dbw_order(args.order_id)),
        "dbw-stickers": lambda: _j(api.get_dbw_stickers(_load_json(args.order_ids_json))),
        "dbw-order-assemble": lambda: _j(api.assemble_dbw_order(args.order_id)),
        "dbw-courier": lambda: _j(api.get_dbw_courier(_load_json(args.order_ids_json))),
        "dbw-order-cancel": lambda: _j(api.cancel_dbw_order(args.order_id)),
        "dbw-order-meta": lambda: _j(api.get_dbw_order_meta(args.order_id)),
        "dbw-order-meta-delete": lambda: _j(api.delete_dbw_order_meta(args.order_id)),
        "dbw-order-meta-sgtin": lambda: _j(api.set_dbw_order_sgtin(args.order_id, _load_json(args.sgtins_json))),
        "dbw-order-meta-uin": lambda: _j(api.set_dbw_order_uin(args.order_id, args.uin)),
        "dbw-order-meta-imei": lambda: _j(api.set_dbw_order_imei(args.order_id, args.imei)),
        "dbw-order-meta-gtin": lambda: _j(api.set_dbw_order_gtin(args.order_id, args.gtin)),
        # DBS Orders
        "dbs-orders-new": lambda: _j(api.get_dbs_orders_new()),
        "dbs-orders": lambda: _j(api.get_dbs_orders()),
        "dbs-groups-info": lambda: _j(api.get_dbs_groups_info(_load_json(args.order_ids_json))),
        "dbs-client": lambda: _j(api.get_dbs_client(_load_json(args.order_ids_json))),
        "dbs-b2b-info": lambda: _j(api.get_dbs_b2b_info(_load_json(args.order_ids_json))),
        "dbs-delivery-date": lambda: _j(api.get_dbs_delivery_date(_load_json(args.order_ids_json))),
        "dbs-orders-status": lambda: _j(api.get_dbs_orders_status(_load_json(args.order_ids_json))),
        "dbs-order-cancel": lambda: _j(api.cancel_dbs_order(_load_json(args.order_ids_json))),
        "dbs-order-confirm": lambda: _j(api.confirm_dbs_order(_load_json(args.order_ids_json))),
        "dbs-stickers": lambda: _j(api.get_dbs_stickers(_load_json(args.order_ids_json))),
        "dbs-order-deliver": lambda: _j(api.deliver_dbs_order(_load_json(args.order_ids_json))),
        "dbs-order-receive": lambda: _j(api.receive_dbs_order(_load_json(args.order_ids_json))),
        "dbs-order-reject": lambda: _j(api.reject_dbs_order(_load_json(args.order_ids_json))),
        "dbs-order-meta": lambda: _j(api.get_dbs_order_meta(_load_json(args.order_ids_json))),
        "dbs-order-meta-delete": lambda: _j(api.delete_dbs_order_meta(_load_json(args.order_ids_json))),
        "dbs-order-meta-sgtin": lambda: _j(api.set_dbs_order_sgtin(_load_json(args.orders_json))),
        "dbs-order-meta-uin": lambda: _j(api.set_dbs_order_uin(_load_json(args.orders_json))),
        "dbs-order-meta-imei": lambda: _j(api.set_dbs_order_imei(_load_json(args.orders_json))),
        "dbs-order-meta-gtin": lambda: _j(api.set_dbs_order_gtin(_load_json(args.orders_json))),
        "dbs-order-meta-customs": lambda: _j(api.set_dbs_order_customs(_load_json(args.orders_json))),
        # Pickup
        "pickup-orders-new": lambda: _j(api.get_pickup_orders_new()),
        "pickup-order-confirm": lambda: _j(api.confirm_pickup_order(_load_json(args.order_ids_json))),
        "pickup-order-prepare": lambda: _j(api.prepare_pickup_order(_load_json(args.order_ids_json))),
        "pickup-client": lambda: _j(api.get_pickup_client(_load_json(args.order_ids_json))),
        "pickup-verify-identity": lambda: _j(api.verify_pickup_identity(_load_json(args.order_ids_json))),
        "pickup-order-receive": lambda: _j(api.receive_pickup_order(_load_json(args.order_ids_json))),
        "pickup-order-reject": lambda: _j(api.reject_pickup_order(_load_json(args.order_ids_json))),
        "pickup-orders-status": lambda: _j(api.get_pickup_orders_status(_load_json(args.order_ids_json))),
        "pickup-orders-completed": lambda: _j(api.get_pickup_orders_completed()),
        "pickup-order-cancel": lambda: _j(api.cancel_pickup_order(_load_json(args.order_ids_json))),
        "pickup-order-meta": lambda: _j(api.get_pickup_order_meta(_load_json(args.order_ids_json))),
        "pickup-order-meta-delete": lambda: _j(api.delete_pickup_order_meta(_load_json(args.order_ids_json))),
        "pickup-order-meta-sgtin": lambda: _j(api.set_pickup_order_sgtin(_load_json(args.orders_json))),
        "pickup-order-meta-uin": lambda: _j(api.set_pickup_order_uin(_load_json(args.orders_json))),
        "pickup-order-meta-imei": lambda: _j(api.set_pickup_order_imei(_load_json(args.orders_json))),
        "pickup-order-meta-gtin": lambda: _j(api.set_pickup_order_gtin(_load_json(args.orders_json))),
        # FBW
        "fbw-acceptance-options": lambda: _j(api.get_fbw_acceptance_options(_load_json(args.params_json))),
        "fbw-warehouses": lambda: _j(api.get_fbw_warehouses()),
        "fbw-transit-tariffs": lambda: _j(api.get_fbw_transit_tariffs()),
        "fbw-supplies": lambda: _j(api.get_fbw_supplies(_load_json(args.params_json) if args.params_json else None)),
        "fbw-supply": lambda: _j(api.get_fbw_supply(args.supply_id)),
        "fbw-supply-goods": lambda: _j(api.get_fbw_supply_goods(args.supply_id)),
        "fbw-supply-package": lambda: _j(api.get_fbw_supply_package(args.supply_id)),
        # Advertising
        "advert-campaigns-count": lambda: _j(api.get_advert_campaigns_count()),
        "advert-campaigns": lambda: _j(api.get_advert_campaigns(_load_json(args.campaign_ids_json))),
        "advert-min-bids": lambda: _j(api.get_advert_min_bids(_load_json(args.params_json))),
        "advert-campaign-create": lambda: _j(api.create_advert_campaign(_load_json(args.params_json))),
        "advert-subjects": lambda: _j(api.get_advert_subjects()),
        "advert-nms": lambda: _j(api.get_advert_nms(_load_json(args.params_json))),
        "advert-campaign-delete": lambda: _j(api.delete_advert_campaign(args.campaign_id)),
        "advert-campaign-rename": lambda: _j(api.rename_advert_campaign(args.campaign_id, args.name)),
        "advert-campaign-start": lambda: _j(api.start_advert_campaign(args.campaign_id)),
        "advert-campaign-pause": lambda: _j(api.pause_advert_campaign(args.campaign_id)),
        "advert-campaign-stop": lambda: _j(api.stop_advert_campaign(args.campaign_id)),
        "advert-placements-update": lambda: _j(api.update_advert_placements(_load_json(args.params_json))),
        "advert-bids-update": lambda: _j(api.update_advert_bids(_load_json(args.params_json))),
        "advert-nms-update": lambda: _j(api.update_advert_nms(_load_json(args.params_json))),
        "advert-bid-recommendations": lambda: _j(api.get_advert_bid_recommendations(args.campaign_id)),
        "advert-search-bids": lambda: _j(api.get_advert_search_bids(_load_json(args.params_json))),
        "advert-search-bids-set": lambda: _j(api.set_advert_search_bids(_load_json(args.params_json))),
        "advert-search-bids-delete": lambda: _j(api.delete_advert_search_bids(_load_json(args.params_json))),
        "advert-minus-phrases": lambda: _j(api.get_advert_minus_phrases(_load_json(args.params_json))),
        "advert-minus-phrases-set": lambda: _j(api.set_advert_minus_phrases(_load_json(args.params_json))),
        "advert-balance": lambda: _j(api.get_advert_balance()),
        "advert-budget": lambda: _j(api.get_advert_budget(args.campaign_id)),
        "advert-budget-deposit": lambda: _j(api.deposit_advert_budget(args.campaign_id, args.amount)),
        "advert-cost-history": lambda: _j(api.get_advert_cost_history(args.date_from, args.date_to)),
        "advert-payments": lambda: _j(api.get_advert_payments(args.date_from, args.date_to)),
        "advert-search-stats": lambda: _j(api.get_advert_search_stats(_load_json(args.params_json))),
        # Communications
        "new-feedbacks-questions": lambda: _j(api.get_new_feedbacks_questions()),
        "questions-unanswered-count": lambda: _j(api.get_unanswered_questions_count()),
        "questions-count": lambda: _j(api.get_questions_count(args.date_from, args.date_to)),
        "questions": lambda: _j(api.get_questions(args.is_answered, args.take, args.skip)),
        "question-manage": lambda: _j(api.manage_question(args.question_id, args.action, args.answer)),
        "question": lambda: _j(api.get_question(args.question_id)),
        "feedbacks-unanswered-count": lambda: _j(api.get_unanswered_feedbacks_count()),
        "feedbacks-count": lambda: _j(api.get_feedbacks_count(args.date_from, args.date_to)),
        "feedbacks": lambda: _j(api.get_feedbacks(args.is_answered, args.take, args.skip)),
        "feedback-answer": lambda: _j(api.answer_feedback(args.feedback_id, args.text)),
        "feedback-answer-edit": lambda: _j(api.edit_feedback_answer(args.feedback_id, args.text)),
        "feedback-return": lambda: _j(api.request_feedback_return(args.feedback_id)),
        "feedback": lambda: _j(api.get_feedback(args.feedback_id)),
        "feedbacks-archive": lambda: _j(api.get_feedbacks_archive(args.take, args.skip)),
        "feedback-pins": lambda: _j(api.get_pinned_feedbacks(args.nm_id)),
        "feedback-pin": lambda: _j(api.pin_feedback(args.feedback_id, args.nm_id)),
        "feedback-unpin": lambda: _j(api.unpin_feedback(args.feedback_id, args.nm_id)),
        "feedback-pins-count": lambda: _j(api.get_pinned_feedbacks_count(args.nm_id)),
        "feedback-pins-limits": lambda: _j(api.get_pinned_feedbacks_limits()),
        "chats": lambda: _j(api.get_chats()),
        "chat-events": lambda: _j(api.get_chat_events()),
        "chat-send": lambda: _j(api.send_chat_message(args.chat_id, args.text)),
        # Tariffs
        "tariff-commissions": lambda: _j(api.get_tariff_commissions()),
        "tariff-box": lambda: _j(api.get_tariff_box(args.date)),
        "tariff-pallet": lambda: _j(api.get_tariff_pallet(args.date)),
        "tariff-acceptance": lambda: _j(api.get_tariff_acceptance()),
        "tariff-return": lambda: _j(api.get_tariff_return()),
        # Analytics
        "analytics-sales-funnel": lambda: _j(api.get_analytics_sales_funnel(_load_json(args.params_json))),
        "analytics-sales-funnel-history": lambda: _j(api.get_analytics_sales_funnel_history(_load_json(args.params_json))),
        "analytics-sales-funnel-grouped": lambda: _j(api.get_analytics_sales_funnel_grouped(_load_json(args.params_json))),
        "analytics-search-report": lambda: _j(api.get_analytics_search_report(_load_json(args.params_json))),
        "analytics-search-groups": lambda: _j(api.get_analytics_search_groups(_load_json(args.params_json))),
        "analytics-search-details": lambda: _j(api.get_analytics_search_details(_load_json(args.params_json))),
        "analytics-search-texts": lambda: _j(api.get_analytics_search_texts(_load_json(args.params_json))),
        "analytics-search-orders": lambda: _j(api.get_analytics_search_orders(_load_json(args.params_json))),
        "analytics-stocks-wb": lambda: _j(api.get_analytics_stocks_wb(_load_json(args.params_json))),
        "analytics-stocks-groups": lambda: _j(api.get_analytics_stocks_products_groups(_load_json(args.params_json))),
        "analytics-stocks-products": lambda: _j(api.get_analytics_stocks_products(_load_json(args.params_json))),
        "analytics-stocks-sizes": lambda: _j(api.get_analytics_stocks_sizes(_load_json(args.params_json))),
        "analytics-stocks-offices": lambda: _j(api.get_analytics_stocks_offices(_load_json(args.params_json))),
        "analytics-csv-create": lambda: _j(api.create_analytics_csv_report(_load_json(args.params_json))),
        "analytics-csv-list": lambda: _j(api.get_analytics_csv_reports()),
        "analytics-csv-retry": lambda: _j(api.retry_analytics_csv_report(_load_json(args.params_json))),
        "analytics-csv-download": lambda: _download(api.download_analytics_csv_report(args.download_id), args.output_path),
        # Reports
        "report-orders": lambda: _j(api.get_report_orders(args.date_from, args.flag)),
        "report-sales": lambda: _j(api.get_report_sales(args.date_from, args.flag)),
        "report-warehouse-remains-create": lambda: _j(api.create_report_warehouse_remains()),
        "report-warehouse-remains-status": lambda: _j(api.get_report_warehouse_remains_status(args.task_id)),
        "report-warehouse-remains-download": lambda: _download(api.download_report_warehouse_remains(args.task_id), args.output_path),
        "report-excise": lambda: _j(api.get_report_excise(_load_json(args.params_json))),
        "report-measurement-penalties": lambda: _j(api.get_report_measurement_penalties()),
        "report-warehouse-measurements": lambda: _j(api.get_report_warehouse_measurements()),
        "report-deductions": lambda: _j(api.get_report_deductions()),
        "report-antifraud": lambda: _j(api.get_report_antifraud()),
        "report-labeling": lambda: _j(api.get_report_labeling()),
        "report-acceptance-create": lambda: _j(api.create_report_acceptance()),
        "report-acceptance-status": lambda: _j(api.get_report_acceptance_status(args.task_id)),
        "report-acceptance-download": lambda: _download(api.download_report_acceptance(args.task_id), args.output_path),
        "report-paid-storage-create": lambda: _j(api.create_report_paid_storage()),
        "report-paid-storage-status": lambda: _j(api.get_report_paid_storage_status(args.task_id)),
        "report-paid-storage-download": lambda: _download(api.download_report_paid_storage(args.task_id), args.output_path),
        "report-regional-sales": lambda: _j(api.get_report_regional_sales()),
        "report-brands": lambda: _j(api.get_report_brands()),
        "report-brand-categories": lambda: _j(api.get_report_brand_categories()),
        "report-brand-share": lambda: _j(api.get_report_brand_share(_load_json(args.params_json) if args.params_json else None)),
        "report-blocked-products": lambda: _j(api.get_report_blocked_products()),
        "report-shadowed-products": lambda: _j(api.get_report_shadowed_products()),
        "report-returns": lambda: _j(api.get_report_returns()),
        # Finance
        "finance-balance": lambda: _j(api.get_finance_balance()),
        "finance-sales-reports": lambda: _j(api.get_finance_sales_reports(_load_json(args.params_json))),
        "finance-sales-report-detail": lambda: _j(api.get_finance_sales_report_detail(args.report_id)),
        "finance-sales-report-by-period": lambda: _j(api.get_finance_sales_report_by_period(_load_json(args.params_json))),
        "finance-report-detail-by-period": lambda: _j(api.get_finance_report_detail_by_period(args.date_from, args.date_to, args.limit)),
        "finance-acquiring-reports": lambda: _j(api.get_finance_acquiring_reports(_load_json(args.params_json))),
        "finance-acquiring-detail": lambda: _j(api.get_finance_acquiring_detail(args.report_id)),
        "finance-acquiring-by-period": lambda: _j(api.get_finance_acquiring_by_period(_load_json(args.params_json))),
        "finance-document-categories": lambda: _j(api.get_finance_document_categories()),
        "finance-documents": lambda: _j(api.get_finance_documents(_load_json(args.params_json) if args.params_json else None)),
        "finance-document-download": lambda: _download(api.download_finance_document(args.doc_id), args.output_path),
        "finance-documents-download": lambda: _download(api.download_finance_documents(_load_json(args.doc_ids_json)), args.output_path),
        # WBD
        "wbd-keys-add": lambda: _j(api.add_wbd_keys(args.offer_id, _load_json(args.keys_json))),
        "wbd-keys-delete": lambda: _j(api.delete_wbd_keys(args.offer_id, _load_json(args.keys_json))),
        "wbd-keys-redeemed": lambda: _j(api.get_wbd_redeemed_keys(args.offer_id)),
        "wbd-keys-count": lambda: _j(api.get_wbd_keys_count(args.offer_id)),
        "wbd-keys-list": lambda: _j(api.get_wbd_keys_list(args.offer_id)),
        "wbd-offer-create": lambda: _j(api.create_wbd_offer(_load_json(args.params_json))),
        "wbd-offer-update": lambda: _j(api.update_wbd_offer(args.offer_id, _load_json(args.params_json))),
        "wbd-offer": lambda: _j(api.get_wbd_offer(args.offer_id)),
        "wbd-offers": lambda: _j(api.get_wbd_offers()),
        "wbd-offer-price": lambda: _j(api.update_wbd_offer_price(args.offer_id, args.price)),
        "wbd-offer-status": lambda: _j(api.update_wbd_offer_status(args.offer_id, args.status)),
        "wbd-catalog": lambda: _j(api.get_wbd_catalog()),
    }

    print(handlers[args.command]())
