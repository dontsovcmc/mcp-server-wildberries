"""Pydantic models for Wildberries MCP action parameters.

Each model validates parameters for one or more wb_execute actions.
Models use Field(description=...) so JSON schema is auto-generated for the LLM.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


# ── Shared / Reusable ──────────────────────────────────────────────────


class OrderIdParams(BaseModel):
    """Single order ID."""

    order_id: int = Field(..., description="Order ID")


class OrderIdsParams(BaseModel):
    """List of order IDs."""

    order_ids: list[int] = Field(..., description="List of order IDs")


class SupplyIdParams(BaseModel):
    """Single supply ID."""

    supply_id: str = Field(..., description="Supply ID (string, e.g. 'WB-GI-1234567')")


class CampaignIdParams(BaseModel):
    """Single advertising campaign ID."""

    campaign_id: int = Field(..., description="Advertising campaign ID")


class TaskIdParams(BaseModel):
    """Async report task ID."""

    task_id: str = Field(..., description="Report task ID returned by the create-report action")


class PassThroughParams(BaseModel):
    """Generic pass-through params for complex API calls.

    Any additional fields are forwarded as-is to the Wildberries API.
    Used for analytics, advertising, and other endpoints with large
    or frequently changing request schemas.
    """

    model_config = ConfigDict(extra="allow")


class DateRangeParams(BaseModel):
    """Date range filter."""

    date_from: str = Field("", description="Start date (RFC3339 or YYYY-MM-DD)")
    date_to: str = Field("", description="End date (RFC3339 or YYYY-MM-DD)")


# ── Content ────────────────────────────────────────────────────────────


class SubjectIdParams(BaseModel):
    """Subject (category) identifier."""

    subject_id: int = Field(..., description="Subject (category) ID")


class SubjectsListParams(BaseModel):
    """Parameters for listing subjects (categories)."""

    name: str = Field("", description="Filter subjects by name (substring match)")
    top: int = Field(50, description="Number of results to return")
    offset: int = Field(0, description="Offset for pagination")


class BrandsParams(BaseModel):
    """Parameters for listing brands."""

    pattern: str = Field("", description="Filter brands by name (substring match)")


class TagCreateParams(BaseModel):
    """Parameters for creating a tag."""

    name: str = Field(..., description="Tag name")
    color: str = Field("", description="Tag color (hex code or name, optional)")


class TagUpdateParams(BaseModel):
    """Parameters for updating a tag."""

    tag_id: int = Field(..., description="Tag ID to update")
    name: str = Field(..., description="New tag name")
    color: str = Field("", description="New tag color (hex code or name, optional)")


class TagIdParams(BaseModel):
    """Single tag identifier."""

    tag_id: int = Field(..., description="Tag ID")


class TagLinkParams(BaseModel):
    """Parameters for linking tags to products."""

    nm_ids: list[int] = Field(..., description="List of nomenclature IDs (product IDs)")
    tag_id: int = Field(..., description="Tag ID to link")


class CardsListParams(BaseModel):
    """Parameters for listing product cards.

    Both cursor and filter_params accept arbitrary dicts matching
    the Wildberries API schema for /content/v2/get/cards/list.
    """

    cursor: dict | None = Field(None, description="Cursor object for pagination (e.g. {'limit': 100, 'updatedAt': '...', 'nmID': 0})")
    filter_params: dict | None = Field(None, description="Filter object (e.g. {'textSearch': '...', 'withPhoto': -1})")


class CardsUpdateParams(BaseModel):
    """Parameters for updating product cards."""

    cards: list[dict] = Field(..., description="List of card objects to update (WB card schema)")


# ── FBS Orders ─────────────────────────────────────────────────────────


class FbsOrdersParams(BaseModel):
    """Parameters for listing FBS orders."""

    date_from: str = Field("", description="Start date filter (RFC3339 or YYYY-MM-DD)")
    date_to: str = Field("", description="End date filter (RFC3339 or YYYY-MM-DD)")
    limit: int = Field(100, description="Number of orders to return (max 1000)")
    next_val: int = Field(0, description="Cursor for pagination (value from previous response)")


class FbsStickersParams(BaseModel):
    """Parameters for getting FBS order stickers."""

    order_ids: list[int] = Field(..., description="List of order IDs")
    sticker_type: str = Field("svg", description="Sticker format: 'svg' or 'png'")
    width: int = Field(58, description="Sticker width in mm")
    height: int = Field(40, description="Sticker height in mm")


class FbsSupplyCreateParams(BaseModel):
    """Parameters for creating an FBS supply."""

    name: str = Field("", description="Supply name (optional)")


class FbsSuppliesParams(BaseModel):
    """Parameters for listing FBS supplies."""

    limit: int = Field(100, description="Number of supplies to return")
    next_val: int = Field(0, description="Cursor for pagination")


class FbsSupplyAddOrdersParams(BaseModel):
    """Parameters for adding orders to an FBS supply."""

    supply_id: str = Field(..., description="Supply ID")
    order_ids: list[int] = Field(..., description="List of order IDs to add")


class FbsPassUpdateParams(BaseModel):
    """Parameters for updating an FBS pass.

    The params dict is forwarded to the WB API as the request body.
    """

    pass_id: int = Field(..., description="Pass ID to update")
    params: dict = Field(..., description="Pass update parameters (WB pass schema)")


class PassIdParams(BaseModel):
    """Single pass identifier."""

    pass_id: int = Field(..., description="Pass ID")


# ── FBS/DBW Order Metadata ─────────────────────────────────────────────


class OrderSgtinParams(BaseModel):
    """Parameters for setting SGTIN (Chestniy Znak) codes on an order."""

    order_id: int = Field(..., description="Order ID")
    sgtins: list[str] = Field(..., description="List of SGTIN codes (Chestniy Znak / product marking)")


class OrderUinParams(BaseModel):
    """Parameters for setting UIN on an order."""

    order_id: int = Field(..., description="Order ID")
    uin: str = Field(..., description="Unique Identification Number (UIN)")


class OrderImeiParams(BaseModel):
    """Parameters for setting IMEI on an order."""

    order_id: int = Field(..., description="Order ID")
    imei: str = Field(..., description="IMEI number of the device")


class OrderGtinParams(BaseModel):
    """Parameters for setting GTIN on an order."""

    order_id: int = Field(..., description="Order ID")
    gtin: str = Field(..., description="Global Trade Item Number (GTIN / barcode)")


class OrderExpirationParams(BaseModel):
    """Parameters for setting expiration date on an FBS order."""

    order_id: int = Field(..., description="Order ID")
    date: str = Field(..., description="Expiration date (YYYY-MM-DD)")


class OrderCustomsParams(BaseModel):
    """Parameters for setting customs declaration on an FBS order."""

    order_id: int = Field(..., description="Order ID")
    declaration: str = Field(..., description="Customs declaration number")


# ── DBS / Pickup Batch Metadata ─────────────────────────────────────────


class OrdersBatchParams(BaseModel):
    """Batch parameters for DBS/Pickup order metadata operations.

    Used for set_dbs_order_sgtin, set_dbs_order_uin, set_dbs_order_imei,
    set_dbs_order_gtin, set_dbs_order_customs, and their Pickup equivalents.
    Each dict in the list must contain order_id plus metadata fields
    per WB API schema.
    """

    orders: list[dict] = Field(..., description="List of order metadata objects (schema varies by action)")


# ── Advertising ────────────────────────────────────────────────────────


class CampaignIdsParams(BaseModel):
    """List of advertising campaign IDs."""

    campaign_ids: list[int] = Field(..., description="List of advertising campaign IDs")


class CampaignRenameParams(BaseModel):
    """Parameters for renaming an advertising campaign."""

    campaign_id: int = Field(..., description="Advertising campaign ID")
    name: str = Field(..., description="New campaign name")


class CampaignBudgetDepositParams(BaseModel):
    """Parameters for depositing budget into an advertising campaign."""

    campaign_id: int = Field(..., description="Advertising campaign ID")
    amount: int = Field(..., description="Amount to deposit (in kopecks)")


class AdvertBidsUpdateParams(BaseModel):
    """Parameters for updating advertising bids."""

    params: list[dict] = Field(..., description="List of bid update objects (WB bid schema)")


class AdvertDateRangeParams(BaseModel):
    """Date range for advertising cost/payment history."""

    date_from: str = Field("", description="Start date (YYYY-MM-DD)")
    date_to: str = Field("", description="End date (YYYY-MM-DD)")


# ── Communications (Feedbacks & Questions) ──────────────────────────────


class QuestionsParams(BaseModel):
    """Parameters for listing questions."""

    is_answered: bool = Field(False, description="Filter: True = answered, False = unanswered")
    take: int = Field(100, description="Number of questions to return")
    skip: int = Field(0, description="Number of questions to skip")


class QuestionsCountParams(BaseModel):
    """Parameters for getting question count by date range."""

    date_from: str = Field(..., description="Start date (YYYY-MM-DD)")
    date_to: str = Field(..., description="End date (YYYY-MM-DD)")


class QuestionManageParams(BaseModel):
    """Parameters for managing a question (answer, reject, mark viewed)."""

    question_id: str = Field(..., description="Question ID")
    action: str = Field(..., description="Action to perform: 'wbRu' (answer), 'rejected' (reject), 'viewed' (mark viewed)")
    answer: str = Field("", description="Answer text (required when action='wbRu')")


class QuestionIdParams(BaseModel):
    """Single question identifier."""

    question_id: str = Field(..., description="Question ID")


class FeedbacksParams(BaseModel):
    """Parameters for listing feedbacks (reviews)."""

    is_answered: bool = Field(False, description="Filter: True = answered, False = unanswered")
    take: int = Field(100, description="Number of feedbacks to return")
    skip: int = Field(0, description="Number of feedbacks to skip")


class FeedbacksCountParams(BaseModel):
    """Parameters for getting feedback count by date range."""

    date_from: str = Field(..., description="Start date (YYYY-MM-DD)")
    date_to: str = Field(..., description="End date (YYYY-MM-DD)")


class FeedbackAnswerParams(BaseModel):
    """Parameters for answering or editing a feedback response."""

    feedback_id: str = Field(..., description="Feedback (review) ID")
    text: str = Field(..., description="Answer text")


class FeedbackIdParams(BaseModel):
    """Single feedback identifier."""

    feedback_id: str = Field(..., description="Feedback (review) ID")


class FeedbacksArchiveParams(BaseModel):
    """Parameters for listing archived feedbacks."""

    take: int = Field(100, description="Number of feedbacks to return")
    skip: int = Field(0, description="Number of feedbacks to skip")


class NmIdParams(BaseModel):
    """Single nomenclature (product) ID."""

    nm_id: int = Field(..., description="Nomenclature ID (product ID)")


class FeedbackPinParams(BaseModel):
    """Parameters for pinning/unpinning a feedback to a product."""

    feedback_id: str = Field(..., description="Feedback (review) ID")
    nm_id: int = Field(..., description="Nomenclature ID (product ID)")


class ChatSendParams(BaseModel):
    """Parameters for sending a chat message."""

    chat_id: str = Field(..., description="Chat ID")
    text: str = Field(..., description="Message text")


# ── Tariffs ────────────────────────────────────────────────────────────


class TariffDateParams(BaseModel):
    """Optional date filter for tariff queries."""

    date: str = Field("", description="Date for tariff lookup (YYYY-MM-DD, optional, defaults to today)")


# ── Reports ────────────────────────────────────────────────────────────


class ReportOrdersParams(BaseModel):
    """Parameters for orders/sales report."""

    date_from: str = Field(..., description="Start date (YYYY-MM-DD or RFC3339)")
    flag: int = Field(0, description="Report flag: 0 = updated since date, 1 = created since date")


class FinanceReportDetailParams(BaseModel):
    """Parameters for detailed finance report by period (deprecated v5 endpoint)."""

    date_from: str = Field(..., description="Start date (YYYY-MM-DD)")
    date_to: str = Field(..., description="End date (YYYY-MM-DD)")
    limit: int = Field(100000, description="Maximum number of rows to return")


class ReportIdParams(BaseModel):
    """Single report identifier."""

    report_id: int = Field(..., description="Report ID")


# ── Finance ────────────────────────────────────────────────────────────


class DocIdParams(BaseModel):
    """Single document identifier."""

    doc_id: str = Field(..., description="Document ID")


class DocIdsParams(BaseModel):
    """List of document identifiers (for batch download)."""

    doc_ids: list[str] = Field(..., description="List of document IDs")


# ── Users ──────────────────────────────────────────────────────────────


class UserInviteParams(BaseModel):
    """Parameters for inviting a user."""

    email: str = Field(..., description="Email address of the user to invite")
    permissions: list[dict] = Field(..., description="List of permission objects (WB permissions schema)")


class UserAccessUpdateParams(BaseModel):
    """Parameters for updating user access."""

    user_id: str = Field(..., description="User ID")
    permissions: list[dict] = Field(..., description="List of permission objects (WB permissions schema)")


class UserIdParams(BaseModel):
    """Single user identifier."""

    user_id: str = Field(..., description="User ID")


# ── WBD (Wildberries Digital) ──────────────────────────────────────────


class WbdOfferIdParams(BaseModel):
    """Single WBD offer identifier."""

    offer_id: str = Field(..., description="WBD digital offer ID")


class WbdKeysParams(BaseModel):
    """Parameters for adding/deleting activation keys."""

    offer_id: str = Field(..., description="WBD digital offer ID")
    keys: list[str] = Field(..., description="List of activation keys")


class WbdOfferUpdateParams(BaseModel):
    """Parameters for updating a WBD offer.

    The params dict is forwarded to the WB API as the request body.
    """

    offer_id: str = Field(..., description="WBD digital offer ID")
    params: dict = Field(..., description="Offer update parameters (WB offer schema)")


class WbdOfferPriceParams(BaseModel):
    """Parameters for updating a WBD offer price."""

    offer_id: str = Field(..., description="WBD digital offer ID")
    price: int = Field(..., description="New price (in kopecks)")


class WbdOfferStatusParams(BaseModel):
    """Parameters for updating a WBD offer status."""

    offer_id: str = Field(..., description="WBD digital offer ID")
    status: str = Field(..., description="New offer status")


# ── File Downloads ─────────────────────────────────────────────────────


class DownloadIdParams(BaseModel):
    """Download identifier for analytics CSV reports."""

    download_id: str = Field(..., description="Download ID returned by the CSV report creation action")


# ── FBS Pass ──────────────────────────────────────────────────────────


class FbsPassCreateParams(BaseModel):
    """Create FBS access pass."""

    firstName: str = Field(..., description="Driver first name")
    lastName: str = Field(..., description="Driver last name")
    carModel: str = Field(..., description="Car model")
    carNumber: str = Field(..., description="Car number plate (6-9 chars)")
    officeId: int = Field(..., description="Warehouse ID")


# ── FBW ───────────────────────────────────────────────────────────────


class FbwAcceptanceOptionsParams(BaseModel):
    """FBW acceptance options — array of goods."""

    goods: list[dict] = Field(..., description="Array of {quantity: int, barcode: str}")


class FbwSuppliesFilterParams(BaseModel):
    """FBW supplies list filter."""

    dates: list[dict] | None = Field(None, description="Date filters [{from, till, type}]")
    statusIDs: list[int] | None = Field(None, description="Status: 1=unplanned 2=planned 3=shipping 4=accepting 5=accepted 6=shipped")


# ── Advertising ───────────────────────────────────────────────────────


class AdvertMinBidsParams(BaseModel):
    """Get minimum bid rates."""

    advert_id: int = Field(..., description="Campaign ID")
    nm_ids: list[int] = Field(..., description="WB article numbers (max 100)")
    payment_type: str = Field(..., description="Payment type: cpm or cpc")
    placement_types: list[str] = Field(..., description="Placement types: combined, search, recommendation")


class AdvertCampaignCreateParams(BaseModel):
    """Create advertising campaign."""

    name: str | None = Field(None, description="Campaign name")
    nms: list[int] | None = Field(None, description="WB article numbers (max 50)")
    bid_type: str = Field("manual", description="Bid type: manual or unified")
    payment_type: str = Field("cpm", description="Payment type: cpm or cpc")
    placement_types: list[str] = Field(default_factory=lambda: ["search"], description="search, recommendations")


class AdvertNmsParams(BaseModel):
    """Get product cards for advertising — array of subject IDs."""

    subject_ids: list[int] = Field(..., description="Subject IDs (max 100)")


class AdvertPlacementsUpdateParams(BaseModel):
    """Update advertising placements."""

    placements: list[dict] = Field(..., description="[{advert_id, placements: {search: bool, recommendations: bool}}]")


class AdvertNmsUpdateParams(BaseModel):
    """Manage product cards in campaign."""

    nms: list[dict] = Field(..., description="[{advert_id, nms: {add: [int], delete: [int]}}]")


class AdvertSearchBidsGetParams(BaseModel):
    """Get search cluster bids."""

    items: list[dict] = Field(..., description="[{advert_id: int, nm_id: int}]")


class AdvertSearchBidsSetParams(BaseModel):
    """Set or delete search cluster bids."""

    bids: list[dict] = Field(..., description="[{advert_id, nm_id, norm_query, bid}]")


class AdvertMinusPhraseGetParams(BaseModel):
    """Get negative phrases."""

    items: list[dict] = Field(..., description="[{advert_id: int, nm_id: int}]")


class AdvertMinusPhraseSetParams(BaseModel):
    """Set negative phrases."""

    advert_id: int = Field(..., description="Campaign ID")
    nm_id: int = Field(..., description="WB article number")
    norm_queries: list[str] = Field(..., description="Minus phrases (max 1000)")


class AdvertSearchStatsParams(BaseModel):
    """Get search cluster statistics."""

    model_config = ConfigDict(populate_by_name=True)

    date_from: str = Field(..., alias="from", description="Start date YYYY-MM-DD")
    date_to: str = Field(..., alias="to", description="End date YYYY-MM-DD")
    items: list[dict] = Field(..., description="[{advert_id, nm_id}]")


# ── Analytics — Sales Funnel ──────────────────────────────────────────


class AnalyticsSalesFunnelParams(BaseModel):
    """Sales funnel by products."""

    selectedPeriod: dict = Field(..., description="{start: 'YYYY-MM-DD', end: 'YYYY-MM-DD'}")
    pastPeriod: dict | None = Field(None, description="{start, end} comparison")
    nmIds: list[int] | None = Field(None, description="Product IDs (max 1000)")
    brandNames: list[str] | None = Field(None, description="Brand names")
    subjectIds: list[int] | None = Field(None, description="Subject IDs")
    tagIds: list[int] | None = Field(None, description="Tag IDs")
    skipDeletedNm: bool | None = Field(None, description="Hide deleted")
    orderBy: dict | None = Field(None, description="{field, mode: asc|desc}")
    limit: int = Field(50, description="Max 1000")
    offset: int = Field(0, description="Offset")


class AnalyticsSalesFunnelHistoryParams(BaseModel):
    """Sales funnel history."""

    selectedPeriod: dict = Field(..., description="{start, end}")
    nmIds: list[int] = Field(..., description="Product IDs (1-20)")
    skipDeletedNm: bool | None = Field(None, description="Hide deleted")
    aggregationLevel: str | None = Field(None, description="day or week")


class AnalyticsSalesFunnelGroupedParams(BaseModel):
    """Grouped sales funnel."""

    selectedPeriod: dict = Field(..., description="{start, end}")
    brandNames: list[str] | None = Field(None, description="Brand names")
    subjectIds: list[int] | None = Field(None, description="Subject IDs")
    tagIds: list[int] | None = Field(None, description="Tag IDs")
    skipDeletedNm: bool | None = Field(None, description="Hide deleted")
    aggregationLevel: str | None = Field(None, description="day or week")


# ── Analytics — Search Report ─────────────────────────────────────────


class AnalyticsSearchReportParams(BaseModel):
    """Search report by products."""

    selectedPeriod: dict = Field(..., description="{start, end}")
    pastPeriod: dict | None = Field(None, description="{start, end}")
    nmIds: list[int] | None = Field(None, description="Product IDs (max 1000)")
    brandNames: list[str] | None = Field(None, description="Brand names")
    subjectIds: list[int] | None = Field(None, description="Subject IDs")
    tagIds: list[int] | None = Field(None, description="Tag IDs")
    skipDeletedNm: bool | None = Field(None, description="Hide deleted")
    orderBy: dict | None = Field(None, description="{field, mode}")
    limit: int = Field(50, description="Max 1000")
    offset: int = Field(0, description="Offset")


class AnalyticsSearchGroupsParams(BaseModel):
    """Search query groups."""

    selectedPeriod: dict = Field(..., description="{start, end}")
    brandNames: list[str] | None = Field(None, description="Brand names")
    subjectIds: list[int] | None = Field(None, description="Subject IDs")
    tagIds: list[int] | None = Field(None, description="Tag IDs")
    skipDeletedNm: bool | None = Field(None, description="Hide deleted")
    aggregationLevel: str | None = Field(None, description="day or week")


class AnalyticsSearchDetailsParams(BaseModel):
    """Search query details."""

    currentPeriod: dict = Field(..., description="{start, end}")
    pastPeriod: dict | None = Field(None, description="{start, end}")
    nmIds: list[int] | None = Field(None, description="Product IDs")
    subjectIds: list[int] | None = Field(None, description="Subject IDs")
    brandNames: list[str] | None = Field(None, description="Brand names")
    tagIds: list[int] | None = Field(None, description="Tag IDs")
    orderBy: dict = Field(..., description="{field, mode: asc|desc}")
    limit: int = Field(100, description="Max 1000")
    offset: int = Field(0, description="Offset")


class AnalyticsSearchTextsParams(BaseModel):
    """Search phrases for product."""

    currentPeriod: dict = Field(..., description="{start, end}")
    nmIds: list[int] = Field(..., description="Product article IDs")
    topOrderBy: str = Field(..., description="openCard|addToCart|openToCart|orders|cartToOrder")


class AnalyticsSearchOrdersParams(BaseModel):
    """Orders by search phrase."""

    period: dict = Field(..., description="{start, end}")
    nmId: int = Field(..., description="Product article ID")
    searchTexts: list[str] = Field(..., description="Search phrases (1-30)")


# ── Analytics — Stocks ────────────────────────────────────────────────


class AnalyticsStocksWbParams(BaseModel):
    """WB warehouse stock data."""

    nmIds: list[int] | None = Field(None, description="Product IDs (max 1000)")
    chrtIds: list[int] | None = Field(None, description="Size IDs")
    limit: int = Field(250000, description="Max rows")
    offset: int = Field(0, description="Offset")


class AnalyticsStocksProductsParams(BaseModel):
    """Product inventory."""

    currentPeriod: dict = Field(..., description="{start, end}")
    stockType: str = Field(..., description="'' (all), 'wb', 'mp' (seller)")
    skipDeletedNm: bool = Field(..., description="Hide deleted")
    orderBy: dict = Field(..., description="{field, mode}")
    availabilityFilters: list[str] = Field(..., description="deficient|actual|balanced|nonActual|nonLiquid|invalidData")
    offset: int = Field(0, description="Offset")
    nmIDs: list[int] | None = Field(None, description="Product IDs")
    subjectID: int | None = Field(None, description="Subject ID")
    brandName: str | None = Field(None, description="Brand name")
    tagID: int | None = Field(None, description="Tag ID")
    limit: int = Field(100, description="Max 1000")


class AnalyticsStocksGroupsParams(BaseModel):
    """Grouped inventory."""

    currentPeriod: dict = Field(..., description="{start, end}")
    pastPeriod: dict | None = Field(None, description="{start, end}")
    nmIds: list[int] | None = Field(None, description="Product IDs")
    subjectIds: list[int] | None = Field(None, description="Subject IDs")
    brandNames: list[str] | None = Field(None, description="Brand names")
    tagIds: list[int] | None = Field(None, description="Tag IDs")
    orderBy: dict = Field(..., description="{field, mode}")
    limit: int = Field(100, description="Max 1000")
    offset: int = Field(0, description="Offset")


class AnalyticsStocksSizesParams(BaseModel):
    """Inventory by size."""

    nmID: int = Field(..., description="Product article ID")
    currentPeriod: dict = Field(..., description="{start, end}")
    stockType: str = Field(..., description="'' | 'wb' | 'mp'")
    orderBy: dict = Field(..., description="{field, mode}")
    includeOffice: bool = Field(..., description="Include warehouse details")


class AnalyticsStocksOfficesParams(BaseModel):
    """Warehouse inventory."""

    currentPeriod: dict = Field(..., description="{start, end}")
    stockType: str = Field(..., description="'' | 'wb' | 'mp'")
    skipDeletedNm: bool = Field(..., description="Hide deleted")
    nmIDs: list[int] | None = Field(None, description="Product IDs")
    subjectIDs: list[int] | None = Field(None, description="Subject IDs")
    brandNames: list[str] | None = Field(None, description="Brand names")
    tagIDs: list[int] | None = Field(None, description="Tag IDs")


# ── Analytics — CSV ───────────────────────────────────────────────────


class AnalyticsCsvCreateParams(BaseModel):
    """Create analytics CSV report."""

    selectedPeriod: dict = Field(..., description="{start, end}")
    nmIds: list[int] | None = Field(None, description="Product IDs")
    brandNames: list[str] | None = Field(None, description="Brand names")
    subjectIds: list[int] | None = Field(None, description="Subject IDs")
    tagIds: list[int] | None = Field(None, description="Tag IDs")


class AnalyticsCsvRetryParams(BaseModel):
    """Retry CSV report generation."""

    downloadId: str = Field(..., description="Download ID of failed report")


# ── Reports ───────────────────────────────────────────────────────────


class ReportExciseParams(BaseModel):
    """Excise/marking report."""

    countries: list[str] | None = Field(None, description="ISO codes: AM, BY, KG, KZ, RU, UZ")


class ReportBrandShareParams(BaseModel):
    """Brand share report."""

    parentID: int | None = Field(None, description="Parent category ID")
    subjectID: int | None = Field(None, description="Subject ID")
    brandID: int | None = Field(None, description="Brand ID")


# ── Finance ───────────────────────────────────────────────────────────


class FinanceSalesReportsListParams(BaseModel):
    """Sales reports list."""

    dateFrom: str = Field(..., description="Start date (RFC3339)")
    dateTo: str = Field(..., description="End date (RFC3339)")
    limit: int = Field(1000, description="Max 1000")
    offset: int = Field(0, description="Offset")
    period: str | None = Field(None, description="daily or weekly")


class FinanceSalesReportByPeriodParams(BaseModel):
    """Sales report for period."""

    dateFrom: str = Field(..., description="Start date (RFC3339)")
    dateTo: str = Field(..., description="End date (RFC3339)")
    limit: int = Field(100000, description="Max rows")
    rrdId: int = Field(0, description="Row ID for pagination")
    period: str | None = Field(None, description="daily or weekly")
    fields: list[str] | None = Field(None, description="Fields to return")


class FinanceAcquiringReportsListParams(BaseModel):
    """Acquiring reports list."""

    dateFrom: str = Field(..., description="Start date (RFC3339)")
    dateTo: str = Field(..., description="End date (RFC3339)")
    limit: int = Field(1000, description="Max 1000")
    offset: int = Field(0, description="Offset")


class FinanceAcquiringByPeriodParams(BaseModel):
    """Acquiring for period."""

    dateFrom: str = Field(..., description="Start date (RFC3339)")
    dateTo: str = Field(..., description="End date (RFC3339)")
    limit: int = Field(100000, description="Max rows")
    rrdId: int = Field(0, description="Row ID for pagination")
    fields: list[str] | None = Field(None, description="Fields to return")


class FinanceDocumentsListParams(BaseModel):
    """Seller documents list."""

    beginTime: str | None = Field(None, description="Period start YYYY-MM-DD")
    endTime: str | None = Field(None, description="Period end YYYY-MM-DD")
    sort: str | None = Field(None, description="date or category")
    order: str | None = Field(None, description="desc or asc")
