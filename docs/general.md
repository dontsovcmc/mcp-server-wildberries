# Общее

9 действий в домене `general`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `ping` | Check Wildberries API availability | — |
| `news` | Get seller portal news | — |
| `seller-info` | Get seller name and profile ID | — |
| `seller-rating` | Get seller rating | — |
| `subscriptions` | Get notification subscriptions | — |
| `user-invite` | Create user invitation | `email` (string) *, `permissions` (array) * |
| `users` | Get list of users | — |
| `user-access-update` | Update user access permissions | `user_id` (string) *, `permissions` (array) * |
| `user-delete` | Delete user :warning: | `user_id` (string) * |

\* — обязательный параметр

:warning: — деструктивное действие
