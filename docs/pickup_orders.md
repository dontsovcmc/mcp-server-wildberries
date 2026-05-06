# Самовывоз

16 действий в домене `pickup_orders`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_pickup_orders_new` | Get new pickup orders | — |
| `wb_pickup_order_confirm` | Confirm pickup order | `order_ids` (array) * |
| `wb_pickup_order_prepare` | Mark pickup order as ready | `order_ids` (array) * |
| `wb_pickup_client` | Get pickup client info | `order_ids` (array) * |
| `wb_pickup_verify_identity` | Verify pickup order ownership | `order_ids` (array) * |
| `wb_pickup_order_receive` | Confirm pickup receipt | `order_ids` (array) * |
| `wb_pickup_order_reject` | Record pickup rejection | `order_ids` (array) * |
| `wb_pickup_orders_status` | Get pickup order statuses | `order_ids` (array) * |
| `wb_pickup_orders_completed` | Get completed pickup orders | — |
| `wb_pickup_order_cancel` | Cancel pickup order :warning: | `order_ids` (array) * |
| `wb_pickup_order_meta` | Get pickup order metadata | `order_ids` (array) * |
| `wb_pickup_order_meta_delete` | Delete pickup order metadata :warning: | `order_ids` (array) * |
| `wb_pickup_order_meta_sgtin` | Set Honest Sign codes for pickup orders | `orders` (array) * |
| `wb_pickup_order_meta_uin` | Set UIN for pickup orders | `orders` (array) * |
| `wb_pickup_order_meta_imei` | Set IMEI for pickup orders | `orders` (array) * |
| `wb_pickup_order_meta_gtin` | Set GTIN for pickup orders | `orders` (array) * |

\* — обязательный параметр

:warning: — деструктивное действие (удаление, отмена)
