# Заказы DBW

16 действий в домене `dbw_orders`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_dbw_orders_new` | Get new DBW assembly tasks | — |
| `wb_dbw_orders` | Get completed DBW assembly tasks | — |
| `wb_dbw_delivery_date` | Get DBW delivery dates | `order_ids` (array) * |
| `wb_dbw_client` | Get DBW client info | `order_ids` (array) * |
| `wb_dbw_orders_status` | Get DBW order statuses | `order_ids` (array) * |
| `wb_dbw_order_confirm` | Confirm DBW order | `order_id` (integer) * |
| `wb_dbw_stickers` | Get DBW stickers | `order_ids` (array) * |
| `wb_dbw_order_assemble` | Move DBW order to delivery | `order_id` (integer) * |
| `wb_dbw_courier` | Get DBW courier info | `order_ids` (array) * |
| `wb_dbw_order_cancel` | Cancel DBW order :warning: | `order_id` (integer) * |
| `wb_dbw_order_meta` | Get DBW order metadata | `order_id` (integer) * |
| `wb_dbw_order_meta_delete` | Delete DBW order metadata :warning: | `order_id` (integer) * |
| `wb_dbw_order_meta_sgtin` | Set Honest Sign codes for DBW order | `order_id` (integer) *, `sgtins` (array) * |
| `wb_dbw_order_meta_uin` | Set UIN for DBW order | `order_id` (integer) *, `uin` (string) * |
| `wb_dbw_order_meta_imei` | Set IMEI for DBW order | `order_id` (integer) *, `imei` (string) * |
| `wb_dbw_order_meta_gtin` | Set GTIN for DBW order | `order_id` (integer) *, `gtin` (string) * |

\* — обязательный параметр

:warning: — деструктивное действие (удаление, отмена)
