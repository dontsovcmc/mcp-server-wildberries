# Аналитика

17 действий в домене `analytics`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `analytics-sales-funnel` | Get product sales funnel | `selectedPeriod` (object) *, `pastPeriod` (object), `nmIds` (object), `brandNames` (object), `subjectIds` (object), `tagIds` (object), `skipDeletedNm` (object), `orderBy` (object), `limit` (integer), `offset` (integer) |
| `analytics-sales-funnel-history` | Get sales funnel history | `selectedPeriod` (object) *, `nmIds` (array) *, `skipDeletedNm` (object), `aggregationLevel` (object) |
| `analytics-sales-funnel-grouped` | Get grouped sales funnel | `selectedPeriod` (object) *, `brandNames` (object), `subjectIds` (object), `tagIds` (object), `skipDeletedNm` (object), `aggregationLevel` (object) |
| `analytics-search-report` | Get search queries report | `selectedPeriod` (object) *, `pastPeriod` (object), `nmIds` (object), `brandNames` (object), `subjectIds` (object), `tagIds` (object), `skipDeletedNm` (object), `orderBy` (object), `limit` (integer), `offset` (integer) |
| `analytics-search-groups` | Get search query groups | `selectedPeriod` (object) *, `brandNames` (object), `subjectIds` (object), `tagIds` (object), `skipDeletedNm` (object), `aggregationLevel` (object) |
| `analytics-search-details` | Get search query details | `currentPeriod` (object) *, `pastPeriod` (object), `nmIds` (object), `subjectIds` (object), `brandNames` (object), `tagIds` (object), `orderBy` (object) *, `limit` (integer), `offset` (integer) |
| `analytics-search-texts` | Get search phrases for product | `currentPeriod` (object) *, `nmIds` (array) *, `topOrderBy` (string) * |
| `analytics-search-orders` | Get orders by search phrase | `period` (object) *, `nmId` (integer) *, `searchTexts` (array) * |
| `analytics-stocks-wb` | Get WB warehouse stock data | `nmIds` (object), `chrtIds` (object), `limit` (integer), `offset` (integer) |
| `analytics-stocks-groups` | Get grouped inventory data | `currentPeriod` (object) *, `pastPeriod` (object), `nmIds` (object), `subjectIds` (object), `brandNames` (object), `tagIds` (object), `orderBy` (object) *, `limit` (integer), `offset` (integer) |
| `analytics-stocks-products` | Get product inventory data | `currentPeriod` (object) *, `stockType` (string) *, `skipDeletedNm` (boolean) *, `orderBy` (object) *, `availabilityFilters` (array) *, `offset` (integer), `nmIDs` (object), `subjectID` (object), `brandName` (object), `tagID` (object), `limit` (integer) |
| `analytics-stocks-sizes` | Get inventory by size | `nmID` (integer) *, `currentPeriod` (object) *, `stockType` (string) *, `orderBy` (object) *, `includeOffice` (boolean) * |
| `analytics-stocks-offices` | Get warehouse inventory data | `currentPeriod` (object) *, `stockType` (string) *, `skipDeletedNm` (boolean) *, `nmIDs` (object), `subjectIDs` (object), `brandNames` (object), `tagIDs` (object) |
| `analytics-csv-create` | Create analytics CSV report | `selectedPeriod` (object) *, `nmIds` (object), `brandNames` (object), `subjectIds` (object), `tagIds` (object) |
| `analytics-csv-list` | Get list of analytics CSV reports | — |
| `analytics-csv-retry` | Retry CSV report generation | `downloadId` (string) * |
| `analytics-csv-download` | Download analytics CSV report :floppy_disk: | `download_id` (string) * |

\* — обязательный параметр

:floppy_disk: — скачивание файла (использовать `wb_execute_file`)
