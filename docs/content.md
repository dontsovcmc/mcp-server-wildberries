# Товары и контент

18 действий в домене `content`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_content_parent_categories` | Get parent categories | — |
| `wb_content_subjects` | Get subjects (categories) list | `name` (string), `top` (integer), `offset` (integer) |
| `wb_content_characteristics` | Get subject characteristics | `subject_id` (integer) * |
| `wb_content_colors` | Get color directory | — |
| `wb_content_kinds` | Get gender directory | — |
| `wb_content_countries` | Get country directory | — |
| `wb_content_seasons` | Get season directory | — |
| `wb_content_vat` | Get VAT rates | — |
| `wb_content_tnved` | Get TNVED codes for subject | `subject_id` (integer) * |
| `wb_content_brands` | Get brands | `pattern` (string) |
| `wb_content_tags` | Get seller tags | — |
| `wb_content_tag_create` | Create tag | `name` (string) *, `color` (string) |
| `wb_content_tag_update` | Update tag | `tag_id` (integer) *, `name` (string) *, `color` (string) |
| `wb_content_tag_delete` | Delete tag :warning: | `tag_id` (integer) * |
| `wb_content_tag_link` | Link tag to products | `nm_ids` (array) *, `tag_id` (integer) * |
| `wb_content_cards_list` | Get product cards list | `cursor` (object), `filter_params` (object) |
| `wb_content_cards_errors` | Get card upload errors | — |
| `wb_content_cards_update` | Update product cards | `cards` (array) * |

\* — обязательный параметр

:warning: — деструктивное действие (удаление, отмена)
