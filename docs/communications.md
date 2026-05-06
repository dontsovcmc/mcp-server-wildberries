# Вопросы и отзывы

22 действий в домене `communications`.

| Команда | Описание | Параметры |
|---------|----------|-----------|
| `new-feedbacks-questions` | Get count of unread questions and reviews | — |
| `questions-unanswered-count` | Get count of unanswered questions | — |
| `questions-count` | Get question count for period | `date_from` (string) *, `date_to` (string) * |
| `questions` | Get questions list | `is_answered` (boolean), `take` (integer), `skip` (integer) |
| `question-manage` | Manage question (answer, reject, view) | `question_id` (string) *, `action` (string) *, `answer` (string) |
| `question` | Get individual question | `question_id` (string) * |
| `feedbacks-unanswered-count` | Get count of unprocessed reviews | — |
| `feedbacks-count` | Get review count for period | `date_from` (string) *, `date_to` (string) * |
| `feedbacks` | Get reviews list | `is_answered` (boolean), `take` (integer), `skip` (integer) |
| `feedback-answer` | Answer review | `feedback_id` (string) *, `text` (string) * |
| `feedback-answer-edit` | Edit review answer | `feedback_id` (string) *, `text` (string) * |
| `feedback-return` | Request return for review | `feedback_id` (string) * |
| `feedback` | Get individual review | `feedback_id` (string) * |
| `feedbacks-archive` | Get archived reviews | `take` (integer), `skip` (integer) |
| `feedback-pins` | Get pinned reviews for product | `nm_id` (integer) * |
| `feedback-pin` | Pin review | `feedback_id` (string) *, `nm_id` (integer) * |
| `feedback-unpin` | Unpin review | `feedback_id` (string) *, `nm_id` (integer) * |
| `feedback-pins-count` | Get pinned review count | `nm_id` (integer) * |
| `feedback-pins-limits` | Get pinning limits | — |
| `chats` | Get chats list | — |
| `chat-events` | Get chat events | — |
| `chat-send` | Send chat message | `chat_id` (string) *, `text` (string) * |

\* — обязательный параметр
