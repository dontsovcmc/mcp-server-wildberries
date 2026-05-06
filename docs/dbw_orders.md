# Заказы DBW

16 действий в домене `dbw_orders`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `dbw-orders-new` | Get new DBW assembly tasks | — |
| `dbw-orders` | Get completed DBW assembly tasks | — |
| `dbw-delivery-date` | Get DBW delivery dates | `order_ids` (array) * |
| `dbw-client` | Get DBW client info | `order_ids` (array) * |
| `dbw-orders-status` | Get DBW order statuses | `order_ids` (array) * |
| `dbw-order-confirm` | Confirm DBW order | `order_id` (integer) * |
| `dbw-stickers` | Get DBW stickers | `order_ids` (array) * |
| `dbw-order-assemble` | Move DBW order to delivery | `order_id` (integer) * |
| `dbw-courier` | Get DBW courier info | `order_ids` (array) * |
| `dbw-order-cancel` | Cancel DBW order :warning: | `order_id` (integer) * |
| `dbw-order-meta` | Get DBW order metadata | `order_id` (integer) * |
| `dbw-order-meta-delete` | Delete DBW order metadata :warning: | `order_id` (integer) * |
| `dbw-order-meta-sgtin` | Set Honest Sign codes for DBW order | `order_id` (integer) *, `sgtins` (array) * |
| `dbw-order-meta-uin` | Set UIN for DBW order | `order_id` (integer) *, `uin` (string) * |
| `dbw-order-meta-imei` | Set IMEI for DBW order | `order_id` (integer) *, `imei` (string) * |
| `dbw-order-meta-gtin` | Set GTIN for DBW order | `order_id` (integer) *, `gtin` (string) * |

\* — обязательный параметр

:warning: — деструктивное действие
