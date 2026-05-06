# Заказы DBS

20 действий в домене `dbs_orders`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_dbs_orders_new` | Get new DBS orders | — |
| `wb_dbs_orders` | Get completed DBS orders | — |
| `wb_dbs_groups_info` | Get DBS paid delivery info | `order_ids` (array) * |
| `wb_dbs_client` | Get DBS client info | `order_ids` (array) * |
| `wb_dbs_b2b_info` | Get DBS B2B buyer info | `order_ids` (array) * |
| `wb_dbs_delivery_date` | Get DBS delivery dates | `order_ids` (array) * |
| `wb_dbs_orders_status` | Get DBS order statuses | `order_ids` (array) * |
| `wb_dbs_order_cancel` | Cancel DBS order :warning: | `order_ids` (array) * |
| `wb_dbs_order_confirm` | Confirm DBS order | `order_ids` (array) * |
| `wb_dbs_stickers` | Get DBS stickers | `order_ids` (array) * |
| `wb_dbs_order_deliver` | Move DBS order to delivery | `order_ids` (array) * |
| `wb_dbs_order_receive` | Confirm DBS order receipt | `order_ids` (array) * |
| `wb_dbs_order_reject` | Record DBS order rejection | `order_ids` (array) * |
| `wb_dbs_order_meta` | Get DBS order metadata | `order_ids` (array) * |
| `wb_dbs_order_meta_delete` | Delete DBS order metadata :warning: | `order_ids` (array) * |
| `wb_dbs_order_meta_sgtin` | Set Honest Sign codes for DBS orders | `orders` (array) * |
| `wb_dbs_order_meta_uin` | Set UIN for DBS orders | `orders` (array) * |
| `wb_dbs_order_meta_imei` | Set IMEI for DBS orders | `orders` (array) * |
| `wb_dbs_order_meta_gtin` | Set GTIN for DBS orders | `orders` (array) * |
| `wb_dbs_order_meta_customs` | Set customs for DBS orders | `orders` (array) * |

\* — обязательный параметр

:warning: — деструктивное действие (удаление, отмена)
