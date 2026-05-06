# Заказы DBS

20 действий в домене `dbs_orders`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `dbs-orders-new` | Get new DBS orders | — |
| `dbs-orders` | Get completed DBS orders | — |
| `dbs-groups-info` | Get DBS paid delivery info | `order_ids` (array) * |
| `dbs-client` | Get DBS client info | `order_ids` (array) * |
| `dbs-b2b-info` | Get DBS B2B buyer info | `order_ids` (array) * |
| `dbs-delivery-date` | Get DBS delivery dates | `order_ids` (array) * |
| `dbs-orders-status` | Get DBS order statuses | `order_ids` (array) * |
| `dbs-order-cancel` | Cancel DBS order :warning: | `order_ids` (array) * |
| `dbs-order-confirm` | Confirm DBS order | `order_ids` (array) * |
| `dbs-stickers` | Get DBS stickers | `order_ids` (array) * |
| `dbs-order-deliver` | Move DBS order to delivery | `order_ids` (array) * |
| `dbs-order-receive` | Confirm DBS order receipt | `order_ids` (array) * |
| `dbs-order-reject` | Record DBS order rejection | `order_ids` (array) * |
| `dbs-order-meta` | Get DBS order metadata | `order_ids` (array) * |
| `dbs-order-meta-delete` | Delete DBS order metadata :warning: | `order_ids` (array) * |
| `dbs-order-meta-sgtin` | Set Honest Sign codes for DBS orders | `orders` (array) * |
| `dbs-order-meta-uin` | Set UIN for DBS orders | `orders` (array) * |
| `dbs-order-meta-imei` | Set IMEI for DBS orders | `orders` (array) * |
| `dbs-order-meta-gtin` | Set GTIN for DBS orders | `orders` (array) * |
| `dbs-order-meta-customs` | Set customs for DBS orders | `orders` (array) * |

\* — обязательный параметр

:warning: — деструктивное действие
