# Отчёты

24 действий в домене `reports`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `report-orders` | Get orders report | `date_from` (string) *, `flag` (integer) |
| `report-sales` | Get sales report | `date_from` (string) *, `flag` (integer) |
| `report-warehouse-remains-create` | Create warehouse remains report task | — |
| `report-warehouse-remains-status` | Check warehouse remains report status | `task_id` (string) * |
| `report-warehouse-remains-download` | Download warehouse remains report :floppy_disk: | `task_id` (string) * |
| `report-excise` | Get excise/marking report | `countries` (object) |
| `report-measurement-penalties` | Get dimension measurement deductions | — |
| `report-warehouse-measurements` | Get warehouse measurement data | — |
| `report-deductions` | Get substitution deductions | — |
| `report-antifraud` | Get self-purchase deductions | — |
| `report-labeling` | Get marking penalties | — |
| `report-acceptance-create` | Create acceptance report task | — |
| `report-acceptance-status` | Check acceptance report status | `task_id` (string) * |
| `report-acceptance-download` | Download acceptance report :floppy_disk: | `task_id` (string) * |
| `report-paid-storage-create` | Create paid storage report task | — |
| `report-paid-storage-status` | Check paid storage report status | `task_id` (string) * |
| `report-paid-storage-download` | Download paid storage report :floppy_disk: | `task_id` (string) * |
| `report-regional-sales` | Get regional sales report | — |
| `report-brands` | Get seller brands | — |
| `report-brand-categories` | Get brand categories | — |
| `report-brand-share` | Get brand share report | `parentID` (object), `subjectID` (object), `brandID` (object) |
| `report-blocked-products` | Get blocked products | — |
| `report-shadowed-products` | Get shadowed products | — |
| `report-returns` | Get returns report | — |

\* — обязательный параметр

:floppy_disk: — скачивание файла (использовать `wb_execute_file`)
