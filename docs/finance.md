# Финансы

12 действий в домене `finance`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `finance-balance` | Get seller account balance | — |
| `finance-sales-reports` | Get sales reports list | `dateFrom` (string) *, `dateTo` (string) *, `limit` (integer), `offset` (integer), `period` (object) |
| `finance-sales-report-detail` | Get detailed sales report | `report_id` (integer) * |
| `finance-sales-report-by-period` | Get sales report for period | `dateFrom` (string) *, `dateTo` (string) *, `limit` (integer), `rrdId` (integer), `period` (object), `fields` (object) |
| `finance-report-detail-by-period` | Get realization report | `date_from` (string) *, `date_to` (string) *, `limit` (integer) |
| `finance-acquiring-reports` | Get acquiring reports | `dateFrom` (string) *, `dateTo` (string) *, `limit` (integer), `offset` (integer) |
| `finance-acquiring-detail` | Get detailed acquiring report | `report_id` (integer) * |
| `finance-acquiring-by-period` | Get acquiring for period | `dateFrom` (string) *, `dateTo` (string) *, `limit` (integer), `rrdId` (integer), `fields` (object) |
| `finance-document-categories` | Get document categories | — |
| `finance-documents` | Get seller documents list | `beginTime` (object), `endTime` (object), `sort` (object), `order` (object) |
| `finance-document-download` | Download document :floppy_disk: | `doc_id` (string) * |
| `finance-documents-download` | Download multiple documents :floppy_disk: | `doc_ids` (array) * |

\* — обязательный параметр

:floppy_disk: — скачивание файла (использовать `wb_execute_file`)
