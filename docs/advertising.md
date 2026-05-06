# Реклама

26 действий в домене `advertising`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_advert_campaigns_count` | Get advertising campaign counts | — |
| `wb_advert_campaigns` | Get advertising campaign details | `campaign_ids` (array) * |
| `wb_advert_min_bids` | Get minimum bid rates | `advert_id` (integer) *, `nm_ids` (array) *, `payment_type` (string) *, `placement_types` (array) * |
| `wb_advert_campaign_create` | Create advertising campaign | `name` (object), `nms` (object), `bid_type` (string), `payment_type` (string), `placement_types` (array) |
| `wb_advert_subjects` | Get available categories for advertising | — |
| `wb_advert_nms` | Get product cards for advertising | `subject_ids` (array) * |
| `wb_advert_campaign_delete` | Delete advertising campaign :warning: | `campaign_id` (integer) * |
| `wb_advert_campaign_rename` | Rename advertising campaign | `campaign_id` (integer) *, `name` (string) * |
| `wb_advert_campaign_start` | Start advertising campaign | `campaign_id` (integer) * |
| `wb_advert_campaign_pause` | Pause advertising campaign | `campaign_id` (integer) * |
| `wb_advert_campaign_stop` | Stop advertising campaign | `campaign_id` (integer) * |
| `wb_advert_placements_update` | Update advertising placements | `placements` (array) * |
| `wb_advert_bids_update` | Update advertising bids | `params` (array) * |
| `wb_advert_nms_update` | Manage product cards in campaign | `nms` (array) * |
| `wb_advert_bid_recommendations` | Get bid recommendations | `campaign_id` (integer) * |
| `wb_advert_search_bids` | Get search cluster bids | `items` (array) * |
| `wb_advert_search_bids_set` | Set search cluster bids | `bids` (array) * |
| `wb_advert_search_bids_delete` | Delete search cluster bids :warning: | `bids` (array) * |
| `wb_advert_minus_phrases` | Get negative phrases | `items` (array) * |
| `wb_advert_minus_phrases_set` | Set negative phrases | `advert_id` (integer) *, `nm_id` (integer) *, `norm_queries` (array) * |
| `wb_advert_balance` | Get advertising account balance | — |
| `wb_advert_budget` | Get advertising campaign budget | `campaign_id` (integer) * |
| `wb_advert_budget_deposit` | Replenish campaign budget | `campaign_id` (integer) *, `amount` (integer) * |
| `wb_advert_cost_history` | Get advertising cost history | `date_from` (string), `date_to` (string) |
| `wb_advert_payments` | Get advertising payment history | `date_from` (string), `date_to` (string) |
| `wb_advert_search_stats` | Get search cluster statistics | `from` (string) *, `to` (string) *, `items` (array) * |

\* — обязательный параметр

:warning: — деструктивное действие (удаление, отмена)
