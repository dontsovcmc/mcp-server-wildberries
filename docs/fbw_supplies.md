# Поставки FBW

7 действий в домене `fbw_supplies`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `fbw-acceptance-options` | Get FBW warehouse acceptance options | `goods` (array) * |
| `fbw-warehouses` | Get Wildberries warehouse list | — |
| `fbw-transit-tariffs` | Get transit tariffs | — |
| `fbw-supplies` | Get FBW supplies list | `dates` (object), `statusIDs` (object) |
| `fbw-supply` | Get FBW supply details | `supply_id` (string) * |
| `fbw-supply-goods` | Get FBW supply goods | `supply_id` (string) * |
| `fbw-supply-package` | Get FBW supply package info | `supply_id` (string) * |

\* — обязательный параметр
