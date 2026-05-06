# Финансы

12 действий в домене `finance`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_finance_balance` | Get seller account balance | — |
| `wb_finance_sales_reports` | Get sales reports list | `dateFrom` (string) *, `dateTo` (string) *, `limit` (integer), `offset` (integer), `period` (object) |
| `wb_finance_sales_report_detail` | Get detailed sales report | `report_id` (integer) * |
| `wb_finance_sales_report_by_period` | Get sales report for period | `dateFrom` (string) *, `dateTo` (string) *, `limit` (integer), `rrdId` (integer), `period` (object), `fields` (object) |
| `wb_finance_report_detail_by_period` | Get realization report | `date_from` (string) *, `date_to` (string) *, `limit` (integer) |
| `wb_finance_acquiring_reports` | Get acquiring reports | `dateFrom` (string) *, `dateTo` (string) *, `limit` (integer), `offset` (integer) |
| `wb_finance_acquiring_detail` | Get detailed acquiring report | `report_id` (integer) * |
| `wb_finance_acquiring_by_period` | Get acquiring for period | `dateFrom` (string) *, `dateTo` (string) *, `limit` (integer), `rrdId` (integer), `fields` (object) |
| `wb_finance_document_categories` | Get document categories | — |
| `wb_finance_documents` | Get seller documents list | `beginTime` (object), `endTime` (object), `sort` (object), `order` (object) |
| `wb_finance_document_download` | Download document :floppy_disk: | `doc_id` (string) * |
| `wb_finance_documents_download` | Download multiple documents :floppy_disk: | `doc_ids` (array) * |

\* — обязательный параметр

:floppy_disk: — скачивание файла (использовать `wb_execute_file`)
