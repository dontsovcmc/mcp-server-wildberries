# Заказы FBS

31 действий в домене `fbs_orders`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `fbs-orders-new` | Get new FBS assembly orders | — |
| `fbs-orders` | Get FBS orders | `date_from` (string), `date_to` (string), `limit` (integer), `next_val` (integer) |
| `fbs-orders-status` | Get FBS order statuses | `order_ids` (array) * |
| `fbs-order-cancel` | Cancel FBS order :warning: | `order_id` (integer) * |
| `fbs-stickers` | Get FBS order stickers | `order_ids` (array) *, `sticker_type` (string), `width` (integer), `height` (integer) |
| `fbs-stickers-cross-border` | Get cross-border stickers | `order_ids` (array) * |
| `fbs-orders-status-history` | Get FBS order status history | `order_ids` (array) * |
| `fbs-orders-client` | Get FBS order client info | `order_ids` (array) * |
| `fbs-reshipment-orders` | Get FBS reshipment orders | — |
| `fbs-order-meta` | Get FBS order metadata | `order_ids` (array) * |
| `fbs-order-meta-delete` | Delete FBS order metadata :warning: | `order_id` (integer) * |
| `fbs-order-meta-sgtin` | Set Honest Sign codes for FBS order | `order_id` (integer) *, `sgtins` (array) * |
| `fbs-order-meta-uin` | Set UIN for FBS order | `order_id` (integer) *, `uin` (string) * |
| `fbs-order-meta-imei` | Set IMEI for FBS order | `order_id` (integer) *, `imei` (string) * |
| `fbs-order-meta-gtin` | Set GTIN for FBS order | `order_id` (integer) *, `gtin` (string) * |
| `fbs-order-meta-expiration` | Set expiration date for FBS order | `order_id` (integer) *, `date` (string) * |
| `fbs-order-meta-customs` | Set customs declaration for FBS order | `order_id` (integer) *, `declaration` (string) * |
| `fbs-supply-create` | Create FBS supply | `name` (string) |
| `fbs-supplies` | Get FBS supplies list | `limit` (integer), `next_val` (integer) |
| `fbs-supply-add-orders` | Add orders to FBS supply | `supply_id` (string) *, `order_ids` (array) * |
| `fbs-supply` | Get FBS supply details | `supply_id` (string) * |
| `fbs-supply-delete` | Delete FBS supply :warning: | `supply_id` (string) * |
| `fbs-supply-orders` | Get FBS supply order IDs | `supply_id` (string) * |
| `fbs-supply-deliver` | Deliver FBS supply | `supply_id` (string) * |
| `fbs-supply-barcode` | Get FBS supply barcode | `supply_id` (string) * |
| `fbs-supply-boxes` | Get FBS supply boxes | `supply_id` (string) * |
| `fbs-pass-offices` | Get warehouses requiring access pass | — |
| `fbs-passes` | Get all access passes | — |
| `fbs-pass-create` | Create access pass | `firstName` (string) *, `lastName` (string) *, `carModel` (string) *, `carNumber` (string) *, `officeId` (integer) * |
| `fbs-pass-update` | Update access pass | `pass_id` (integer) *, `params` (object) * |
| `fbs-pass-delete` | Delete access pass :warning: | `pass_id` (integer) * |

\* — обязательный параметр

:warning: — деструктивное действие
