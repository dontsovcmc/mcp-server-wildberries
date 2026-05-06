# Аналитика

17 действий в домене `analytics`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_analytics_sales_funnel` | Get product sales funnel | `selectedPeriod` (object) *, `pastPeriod` (object), `nmIds` (object), `brandNames` (object), `subjectIds` (object), `tagIds` (object), `skipDeletedNm` (object), `orderBy` (object), `limit` (integer), `offset` (integer) |
| `wb_analytics_sales_funnel_history` | Get sales funnel history | `selectedPeriod` (object) *, `nmIds` (array) *, `skipDeletedNm` (object), `aggregationLevel` (object) |
| `wb_analytics_sales_funnel_grouped` | Get grouped sales funnel | `selectedPeriod` (object) *, `brandNames` (object), `subjectIds` (object), `tagIds` (object), `skipDeletedNm` (object), `aggregationLevel` (object) |
| `wb_analytics_search_report` | Get search queries report | `selectedPeriod` (object) *, `pastPeriod` (object), `nmIds` (object), `brandNames` (object), `subjectIds` (object), `tagIds` (object), `skipDeletedNm` (object), `orderBy` (object), `limit` (integer), `offset` (integer) |
| `wb_analytics_search_groups` | Get search query groups | `selectedPeriod` (object) *, `brandNames` (object), `subjectIds` (object), `tagIds` (object), `skipDeletedNm` (object), `aggregationLevel` (object) |
| `wb_analytics_search_details` | Get search query details | `currentPeriod` (object) *, `pastPeriod` (object), `nmIds` (object), `subjectIds` (object), `brandNames` (object), `tagIds` (object), `orderBy` (object) *, `limit` (integer), `offset` (integer) |
| `wb_analytics_search_texts` | Get search phrases for product | `currentPeriod` (object) *, `nmIds` (array) *, `topOrderBy` (string) * |
| `wb_analytics_search_orders` | Get orders by search phrase | `period` (object) *, `nmId` (integer) *, `searchTexts` (array) * |
| `wb_analytics_stocks_wb` | Get WB warehouse stock data | `nmIds` (object), `chrtIds` (object), `limit` (integer), `offset` (integer) |
| `wb_analytics_stocks_groups` | Get grouped inventory data | `currentPeriod` (object) *, `pastPeriod` (object), `nmIds` (object), `subjectIds` (object), `brandNames` (object), `tagIds` (object), `orderBy` (object) *, `limit` (integer), `offset` (integer) |
| `wb_analytics_stocks_products` | Get product inventory data | `currentPeriod` (object) *, `stockType` (string) *, `skipDeletedNm` (boolean) *, `orderBy` (object) *, `availabilityFilters` (array) *, `offset` (integer), `nmIDs` (object), `subjectID` (object), `brandName` (object), `tagID` (object), `limit` (integer) |
| `wb_analytics_stocks_sizes` | Get inventory by size | `nmID` (integer) *, `currentPeriod` (object) *, `stockType` (string) *, `orderBy` (object) *, `includeOffice` (boolean) * |
| `wb_analytics_stocks_offices` | Get warehouse inventory data | `currentPeriod` (object) *, `stockType` (string) *, `skipDeletedNm` (boolean) *, `nmIDs` (object), `subjectIDs` (object), `brandNames` (object), `tagIDs` (object) |
| `wb_analytics_csv_create` | Create analytics CSV report | `selectedPeriod` (object) *, `nmIds` (object), `brandNames` (object), `subjectIds` (object), `tagIds` (object) |
| `wb_analytics_csv_list` | Get list of analytics CSV reports | — |
| `wb_analytics_csv_retry` | Retry CSV report generation | `downloadId` (string) * |
| `wb_analytics_csv_download` | Download analytics CSV report :floppy_disk: | `download_id` (string) * |

\* — обязательный параметр

:floppy_disk: — скачивание файла (использовать `wb_execute_file`)
