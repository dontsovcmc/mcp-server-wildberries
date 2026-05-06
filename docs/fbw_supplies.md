# Поставки FBW

7 действий в домене `fbw_supplies`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_fbw_acceptance_options` | Get FBW warehouse acceptance options | `goods` (array) * |
| `wb_fbw_warehouses` | Get Wildberries warehouse list | — |
| `wb_fbw_transit_tariffs` | Get transit tariffs | — |
| `wb_fbw_supplies` | Get FBW supplies list | `dates` (object), `statusIDs` (object) |
| `wb_fbw_supply` | Get FBW supply details | `supply_id` (string) * |
| `wb_fbw_supply_goods` | Get FBW supply goods | `supply_id` (string) * |
| `wb_fbw_supply_package` | Get FBW supply package info | `supply_id` (string) * |

\* — обязательный параметр
