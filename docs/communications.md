# Вопросы и отзывы

22 действий в домене `communications`.

| ID действия | Описание | Параметры |
|-------------|----------|-----------|
| `wb_new_feedbacks_questions` | Get count of unread questions and reviews | — |
| `wb_questions_unanswered_count` | Get count of unanswered questions | — |
| `wb_questions_count` | Get question count for period | `date_from` (string) *, `date_to` (string) * |
| `wb_questions` | Get questions list | `is_answered` (boolean), `take` (integer), `skip` (integer) |
| `wb_question_manage` | Manage question (answer, reject, view) | `question_id` (string) *, `action` (string) *, `answer` (string) |
| `wb_question` | Get individual question | `question_id` (string) * |
| `wb_feedbacks_unanswered_count` | Get count of unprocessed reviews | — |
| `wb_feedbacks_count` | Get review count for period | `date_from` (string) *, `date_to` (string) * |
| `wb_feedbacks` | Get reviews list | `is_answered` (boolean), `take` (integer), `skip` (integer) |
| `wb_feedback_answer` | Answer review | `feedback_id` (string) *, `text` (string) * |
| `wb_feedback_answer_edit` | Edit review answer | `feedback_id` (string) *, `text` (string) * |
| `wb_feedback_return` | Request return for review | `feedback_id` (string) * |
| `wb_feedback` | Get individual review | `feedback_id` (string) * |
| `wb_feedbacks_archive` | Get archived reviews | `take` (integer), `skip` (integer) |
| `wb_feedback_pins` | Get pinned reviews for product | `nm_id` (integer) * |
| `wb_feedback_pin` | Pin review | `feedback_id` (string) *, `nm_id` (integer) * |
| `wb_feedback_unpin` | Unpin review | `feedback_id` (string) *, `nm_id` (integer) * |
| `wb_feedback_pins_count` | Get pinned review count | `nm_id` (integer) * |
| `wb_feedback_pins_limits` | Get pinning limits | — |
| `wb_chats` | Get chats list | — |
| `wb_chat_events` | Get chat events | — |
| `wb_chat_send` | Send chat message | `chat_id` (string) *, `text` (string) * |

\* — обязательный параметр
