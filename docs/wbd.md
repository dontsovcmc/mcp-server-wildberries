# Цифровые товары WBD

12 действий в домене `wbd`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `wbd-keys-add` | Add activation keys | `offer_id` (string) *, `keys` (array) * |
| `wbd-keys-delete` | Delete activation keys :warning: | `offer_id` (string) *, `keys` (array) * |
| `wbd-keys-redeemed` | Get redeemed keys | `offer_id` (string) * |
| `wbd-keys-count` | Get key count | `offer_id` (string) * |
| `wbd-keys-list` | Get keys list | `offer_id` (string) * |
| `wbd-offer-create` | Create digital offer | — |
| `wbd-offer-update` | Update digital offer | `offer_id` (string) *, `params` (object) * |
| `wbd-offer` | Get digital offer info | `offer_id` (string) * |
| `wbd-offers` | Get digital offers list | — |
| `wbd-offer-price` | Update digital offer price | `offer_id` (string) *, `price` (integer) * |
| `wbd-offer-status` | Update digital offer status | `offer_id` (string) *, `status` (string) * |
| `wbd-catalog` | Get WBD catalog | — |

\* — обязательный параметр

:warning: — деструктивное действие
