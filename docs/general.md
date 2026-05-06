# Общее

9 действий в домене `general`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_ping` | Check Wildberries API availability | — |
| `wb_news` | Get seller portal news | — |
| `wb_seller_info` | Get seller name and profile ID | — |
| `wb_seller_rating` | Get seller rating | — |
| `wb_subscriptions` | Get notification subscriptions | — |
| `wb_user_invite` | Create user invitation | `email` (string) *, `permissions` (array) * |
| `wb_users` | Get list of users | — |
| `wb_user_access_update` | Update user access permissions | `user_id` (string) *, `permissions` (array) * |
| `wb_user_delete` | Delete user :warning: | `user_id` (string) * |

\* — обязательный параметр

:warning: — деструктивное действие (удаление, отмена)
