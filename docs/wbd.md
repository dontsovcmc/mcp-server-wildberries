# Цифровые товары WBD

12 действий в домене `wbd`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_wbd_keys_add` | Add activation keys | `offer_id` (string) *, `keys` (array) * |
| `wb_wbd_keys_delete` | Delete activation keys :warning: | `offer_id` (string) *, `keys` (array) * |
| `wb_wbd_keys_redeemed` | Get redeemed keys | `offer_id` (string) * |
| `wb_wbd_keys_count` | Get key count | `offer_id` (string) * |
| `wb_wbd_keys_list` | Get keys list | `offer_id` (string) * |
| `wb_wbd_offer_create` | Create digital offer | — |
| `wb_wbd_offer_update` | Update digital offer | `offer_id` (string) *, `params` (object) * |
| `wb_wbd_offer` | Get digital offer info | `offer_id` (string) * |
| `wb_wbd_offers` | Get digital offers list | — |
| `wb_wbd_offer_price` | Update digital offer price | `offer_id` (string) *, `price` (integer) * |
| `wb_wbd_offer_status` | Update digital offer status | `offer_id` (string) *, `status` (string) * |
| `wb_wbd_catalog` | Get WBD catalog | — |

\* — обязательный параметр

:warning: — деструктивное действие (удаление, отмена)
