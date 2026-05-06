# Отчёты

24 действий в домене `reports`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_report_orders` | Get orders report | `date_from` (string) *, `flag` (integer) |
| `wb_report_sales` | Get sales report | `date_from` (string) *, `flag` (integer) |
| `wb_report_warehouse_remains_create` | Create warehouse remains report task | — |
| `wb_report_warehouse_remains_status` | Check warehouse remains report status | `task_id` (string) * |
| `wb_report_warehouse_remains_download` | Download warehouse remains report :floppy_disk: | `task_id` (string) * |
| `wb_report_excise` | Get excise/marking report | `countries` (object) |
| `wb_report_measurement_penalties` | Get dimension measurement deductions | — |
| `wb_report_warehouse_measurements` | Get warehouse measurement data | — |
| `wb_report_deductions` | Get substitution deductions | — |
| `wb_report_antifraud` | Get self-purchase deductions | — |
| `wb_report_labeling` | Get marking penalties | — |
| `wb_report_acceptance_create` | Create acceptance report task | — |
| `wb_report_acceptance_status` | Check acceptance report status | `task_id` (string) * |
| `wb_report_acceptance_download` | Download acceptance report :floppy_disk: | `task_id` (string) * |
| `wb_report_paid_storage_create` | Create paid storage report task | — |
| `wb_report_paid_storage_status` | Check paid storage report status | `task_id` (string) * |
| `wb_report_paid_storage_download` | Download paid storage report :floppy_disk: | `task_id` (string) * |
| `wb_report_regional_sales` | Get regional sales report | — |
| `wb_report_brands` | Get seller brands | — |
| `wb_report_brand_categories` | Get brand categories | — |
| `wb_report_brand_share` | Get brand share report | `parentID` (object), `subjectID` (object), `brandID` (object) |
| `wb_report_blocked_products` | Get blocked products | — |
| `wb_report_shadowed_products` | Get shadowed products | — |
| `wb_report_returns` | Get returns report | — |

\* — обязательный параметр

:floppy_disk: — скачивание файла (использовать `wb_execute_file`)
