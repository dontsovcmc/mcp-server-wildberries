# Товары и контент

18 действий в домене `content`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `content-parent-categories` | Get parent categories | — |
| `content-subjects` | Get subjects (categories) list | `name` (string), `top` (integer), `offset` (integer) |
| `content-characteristics` | Get subject characteristics | `subject_id` (integer) * |
| `content-colors` | Get color directory | — |
| `content-kinds` | Get gender directory | — |
| `content-countries` | Get country directory | — |
| `content-seasons` | Get season directory | — |
| `content-vat` | Get VAT rates | — |
| `content-tnved` | Get TNVED codes for subject | `subject_id` (integer) * |
| `content-brands` | Get brands | `pattern` (string) |
| `content-tags` | Get seller tags | — |
| `content-tag-create` | Create tag | `name` (string) *, `color` (string) |
| `content-tag-update` | Update tag | `tag_id` (integer) *, `name` (string) *, `color` (string) |
| `content-tag-delete` | Delete tag :warning: | `tag_id` (integer) * |
| `content-tag-link` | Link tag to products | `nm_ids` (array) *, `tag_id` (integer) * |
| `content-cards-list` | Get product cards list | `cursor` (object), `filter_params` (object) |
| `content-cards-errors` | Get card upload errors | — |
| `content-cards-update` | Update product cards | `cards` (array) * |

\* — обязательный параметр

:warning: — деструктивное действие
