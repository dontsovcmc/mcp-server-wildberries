# Заказы FBS

31 действий в домене `fbs_orders`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_fbs_orders_new` | Get new FBS assembly orders | — |
| `wb_fbs_orders` | Get FBS orders | `date_from` (string), `date_to` (string), `limit` (integer), `next_val` (integer) |
| `wb_fbs_orders_status` | Get FBS order statuses | `order_ids` (array) * |
| `wb_fbs_order_cancel` | Cancel FBS order :warning: | `order_id` (integer) * |
| `wb_fbs_stickers` | Get FBS order stickers | `order_ids` (array) *, `sticker_type` (string), `width` (integer), `height` (integer) |
| `wb_fbs_stickers_cross_border` | Get cross-border stickers | `order_ids` (array) * |
| `wb_fbs_orders_status_history` | Get FBS order status history | `order_ids` (array) * |
| `wb_fbs_orders_client` | Get FBS order client info | `order_ids` (array) * |
| `wb_fbs_reshipment_orders` | Get FBS reshipment orders | — |
| `wb_fbs_order_meta` | Get FBS order metadata | `order_ids` (array) * |
| `wb_fbs_order_meta_delete` | Delete FBS order metadata :warning: | `order_id` (integer) * |
| `wb_fbs_order_meta_sgtin` | Set Honest Sign codes for FBS order | `order_id` (integer) *, `sgtins` (array) * |
| `wb_fbs_order_meta_uin` | Set UIN for FBS order | `order_id` (integer) *, `uin` (string) * |
| `wb_fbs_order_meta_imei` | Set IMEI for FBS order | `order_id` (integer) *, `imei` (string) * |
| `wb_fbs_order_meta_gtin` | Set GTIN for FBS order | `order_id` (integer) *, `gtin` (string) * |
| `wb_fbs_order_meta_expiration` | Set expiration date for FBS order | `order_id` (integer) *, `date` (string) * |
| `wb_fbs_order_meta_customs` | Set customs declaration for FBS order | `order_id` (integer) *, `declaration` (string) * |
| `wb_fbs_supply_create` | Create FBS supply | `name` (string) |
| `wb_fbs_supplies` | Get FBS supplies list | `limit` (integer), `next_val` (integer) |
| `wb_fbs_supply_add_orders` | Add orders to FBS supply | `supply_id` (string) *, `order_ids` (array) * |
| `wb_fbs_supply` | Get FBS supply details | `supply_id` (string) * |
| `wb_fbs_supply_delete` | Delete FBS supply :warning: | `supply_id` (string) * |
| `wb_fbs_supply_orders` | Get FBS supply order IDs | `supply_id` (string) * |
| `wb_fbs_supply_deliver` | Deliver FBS supply | `supply_id` (string) * |
| `wb_fbs_supply_barcode` | Get FBS supply barcode | `supply_id` (string) * |
| `wb_fbs_supply_boxes` | Get FBS supply boxes | `supply_id` (string) * |
| `wb_fbs_pass_offices` | Get warehouses requiring access pass | — |
| `wb_fbs_passes` | Get all access passes | — |
| `wb_fbs_pass_create` | Create access pass | `firstName` (string) *, `lastName` (string) *, `carModel` (string) *, `carNumber` (string) *, `officeId` (integer) * |
| `wb_fbs_pass_update` | Update access pass | `pass_id` (integer) *, `params` (object) * |
| `wb_fbs_pass_delete` | Delete access pass :warning: | `pass_id` (integer) * |

\* — обязательный параметр

:warning: — деструктивное действие (удаление, отмена)
