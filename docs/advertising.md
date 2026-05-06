# Реклама

26 действий в домене `advertising`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `advert-campaigns-count` | Get advertising campaign counts | — |
| `advert-campaigns` | Get advertising campaign details | `campaign_ids` (array) * |
| `advert-min-bids` | Get minimum bid rates | `advert_id` (integer) *, `nm_ids` (array) *, `payment_type` (string) *, `placement_types` (array) * |
| `advert-campaign-create` | Create advertising campaign | `name` (object), `nms` (object), `bid_type` (string), `payment_type` (string), `placement_types` (array) |
| `advert-subjects` | Get available categories for advertising | — |
| `advert-nms` | Get product cards for advertising | `subject_ids` (array) * |
| `advert-campaign-delete` | Delete advertising campaign :warning: | `campaign_id` (integer) * |
| `advert-campaign-rename` | Rename advertising campaign | `campaign_id` (integer) *, `name` (string) * |
| `advert-campaign-start` | Start advertising campaign | `campaign_id` (integer) * |
| `advert-campaign-pause` | Pause advertising campaign | `campaign_id` (integer) * |
| `advert-campaign-stop` | Stop advertising campaign | `campaign_id` (integer) * |
| `advert-placements-update` | Update advertising placements | `placements` (array) * |
| `advert-bids-update` | Update advertising bids | `params` (array) * |
| `advert-nms-update` | Manage product cards in campaign | `nms` (array) * |
| `advert-bid-recommendations` | Get bid recommendations | `campaign_id` (integer) * |
| `advert-search-bids` | Get search cluster bids | `items` (array) * |
| `advert-search-bids-set` | Set search cluster bids | `bids` (array) * |
| `advert-search-bids-delete` | Delete search cluster bids :warning: | `bids` (array) * |
| `advert-minus-phrases` | Get negative phrases | `items` (array) * |
| `advert-minus-phrases-set` | Set negative phrases | `advert_id` (integer) *, `nm_id` (integer) *, `norm_queries` (array) * |
| `advert-balance` | Get advertising account balance | — |
| `advert-budget` | Get advertising campaign budget | `campaign_id` (integer) * |
| `advert-budget-deposit` | Replenish campaign budget | `campaign_id` (integer) *, `amount` (integer) * |
| `advert-cost-history` | Get advertising cost history | `date_from` (string), `date_to` (string) |
| `advert-payments` | Get advertising payment history | `date_from` (string), `date_to` (string) |
| `advert-search-stats` | Get search cluster statistics | `from` (string) *, `to` (string) *, `items` (array) * |

\* — обязательный параметр

:warning: — деструктивное действие
