# Самовывоз

16 действий в домене `pickup_orders`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `pickup-orders-new` | Get new pickup orders | — |
| `pickup-order-confirm` | Confirm pickup order | `order_ids` (array) * |
| `pickup-order-prepare` | Mark pickup order as ready | `order_ids` (array) * |
| `pickup-client` | Get pickup client info | `order_ids` (array) * |
| `pickup-verify-identity` | Verify pickup order ownership | `order_ids` (array) * |
| `pickup-order-receive` | Confirm pickup receipt | `order_ids` (array) * |
| `pickup-order-reject` | Record pickup rejection | `order_ids` (array) * |
| `pickup-orders-status` | Get pickup order statuses | `order_ids` (array) * |
| `pickup-orders-completed` | Get completed pickup orders | — |
| `pickup-order-cancel` | Cancel pickup order :warning: | `order_ids` (array) * |
| `pickup-order-meta` | Get pickup order metadata | `order_ids` (array) * |
| `pickup-order-meta-delete` | Delete pickup order metadata :warning: | `order_ids` (array) * |
| `pickup-order-meta-sgtin` | Set Honest Sign codes for pickup orders | `orders` (array) * |
| `pickup-order-meta-uin` | Set UIN for pickup orders | `orders` (array) * |
| `pickup-order-meta-imei` | Set IMEI for pickup orders | `orders` (array) * |
| `pickup-order-meta-gtin` | Set GTIN for pickup orders | `orders` (array) * |

\* — обязательный параметр

:warning: — деструктивное действие
