# mcp-server-wildberries

mcp-name: io.github.dontsovcmc/wildberries

MCP-сервер для **Wildberries Seller API** — товары, заказы, поставки, аналитика, реклама, финансы.

200+ инструментов, покрывающих все разделы [WB API](https://dev.wildberries.ru/).

## Настройка

### 1. Получите API-токен

Создайте токен в [Личном кабинете продавца WB](https://seller.wildberries.ru/) → Настройки → Доступ к API.

### 2. Установка

```bash
pip install mcp-server-wildberries
```

### 3. Подключение

**Claude Code** (`~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "wildberries": {
      "command": "mcp-server-wildberries",
      "env": {
        "WB_TOKEN": "ваш-токен"
      }
    }
  }
}
```

**Claude Desktop** (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "wildberries": {
      "command": "uvx",
      "args": ["mcp-server-wildberries"],
      "env": {
        "WB_TOKEN": "ваш-токен"
      }
    }
  }
}
```

## Переменные окружения

| Переменная | Обязательная | Описание |
|------------|--------------|----------|
| `WB_TOKEN` | Да | API-токен Wildberries (JWT) |

## Инструменты

### Общее (9)

| Инструмент | Описание |
|------------|----------|
| `wb_ping` | Проверить доступность API |
| `wb_news` | Новости портала продавцов |
| `wb_seller_info` | Имя продавца и ID профиля |
| `wb_seller_rating` | Рейтинг продавца |
| `wb_subscriptions` | Подписки на уведомления |
| `wb_user_invite` | Пригласить пользователя |
| `wb_users` | Список пользователей |
| `wb_user_access_update` | Обновить права пользователя |
| `wb_user_delete` | Удалить пользователя |

### Работа с товарами (~20)

| Инструмент | Описание |
|------------|----------|
| `wb_content_parent_categories` | Родительские категории |
| `wb_content_subjects` | Все предметы (категории) с ID |
| `wb_content_characteristics` | Характеристики предмета |
| `wb_content_colors` | Справочник цветов |
| `wb_content_kinds` | Справочник полов |
| `wb_content_countries` | Справочник стран |
| `wb_content_seasons` | Справочник сезонов |
| `wb_content_vat` | Ставки НДС |
| `wb_content_tnved` | Коды ТНВЭД |
| `wb_content_brands` | Бренды |
| `wb_content_tags` | Теги продавца |
| `wb_content_tag_create` | Создать тег |
| `wb_content_tag_update` | Обновить тег |
| `wb_content_tag_delete` | Удалить тег |
| `wb_content_tag_link` | Привязать теги к товарам |
| `wb_content_cards_list` | Список карточек товаров |
| `wb_content_cards_errors` | Ошибки загрузки карточек |
| `wb_content_cards_update` | Обновить карточки товаров |

### Заказы FBS (~35)

| Инструмент | Описание |
|------------|----------|
| `wb_fbs_orders_new` | Новые заказы FBS |
| `wb_fbs_orders` | Список заказов FBS |
| `wb_fbs_orders_status` | Статусы заказов |
| `wb_fbs_order_cancel` | Отменить заказ |
| `wb_fbs_stickers` | Стикеры заказов |
| `wb_fbs_orders_status_history` | История статусов |
| `wb_fbs_orders_client` | Данные клиента |
| `wb_fbs_order_meta` | Метаданные заказа |
| `wb_fbs_order_meta_sgtin` | Коды Честный Знак |
| `wb_fbs_order_meta_uin` | Привязать УИН |
| `wb_fbs_order_meta_imei` | Привязать IMEI |
| `wb_fbs_order_meta_gtin` | Привязать GTIN |
| `wb_fbs_supply_create` | Создать поставку |
| `wb_fbs_supplies` | Список поставок |
| `wb_fbs_supply` | Детали поставки |
| `wb_fbs_supply_deliver` | Передать в доставку |
| `wb_fbs_passes` | Пропуска на склад |
| ... | и другие |

### Заказы DBW (~16)

Доставка силами WB: `wb_dbw_orders_new`, `wb_dbw_order_confirm`, `wb_dbw_order_assemble`, `wb_dbw_courier`, `wb_dbw_stickers`, инструменты метаданных.

### Заказы DBS (~21)

Доставка продавцом (дропшиппинг): `wb_dbs_orders_new`, `wb_dbs_order_confirm`, `wb_dbs_order_deliver`, `wb_dbs_order_receive`, `wb_dbs_stickers`, инструменты метаданных.

### Заказы Самовывоз (~17)

`wb_pickup_orders_new`, `wb_pickup_order_confirm`, `wb_pickup_order_prepare`, `wb_pickup_verify_identity`, инструменты метаданных.

### Поставки FBW (7)

| Инструмент | Описание |
|------------|----------|
| `wb_fbw_acceptance_options` | Варианты приёмки |
| `wb_fbw_warehouses` | Список складов WB |
| `wb_fbw_transit_tariffs` | Тарифы транзита |
| `wb_fbw_supplies` | Список поставок FBW |
| `wb_fbw_supply` | Детали поставки |
| `wb_fbw_supply_goods` | Товары поставки |
| `wb_fbw_supply_package` | Информация об упаковке |

### Маркетинг и продвижение (~28)

| Инструмент | Описание |
|------------|----------|
| `wb_advert_campaigns_count` | Количество кампаний |
| `wb_advert_campaigns` | Детали кампаний |
| `wb_advert_campaign_create` | Создать кампанию |
| `wb_advert_campaign_start` | Запустить кампанию |
| `wb_advert_campaign_pause` | Поставить на паузу |
| `wb_advert_campaign_stop` | Завершить кампанию |
| `wb_advert_bids_update` | Обновить ставки |
| `wb_advert_bid_recommendations` | Рекомендации по ставкам |
| `wb_advert_balance` | Баланс рекламного счёта |
| `wb_advert_search_stats` | Статистика по поиску |
| ... | и другие |

### Общение с покупателями (~24)

| Инструмент | Описание |
|------------|----------|
| `wb_questions` | Список вопросов |
| `wb_question_manage` | Ответить/отклонить вопрос |
| `wb_feedbacks` | Список отзывов |
| `wb_feedback_answer` | Ответить на отзыв |
| `wb_feedback_pin` | Закрепить отзыв |
| `wb_chats` | Список чатов |
| `wb_chat_send` | Отправить сообщение |
| ... | и другие |

### Тарифы (5)

| Инструмент | Описание |
|------------|----------|
| `wb_tariff_commissions` | Комиссии |
| `wb_tariff_box` | Тарифы на коробки |
| `wb_tariff_pallet` | Тарифы на паллеты |
| `wb_tariff_acceptance` | Коэффициенты приёмки |
| `wb_tariff_return` | Тарифы на возвраты |

### Аналитика и данные (~18)

| Инструмент | Описание |
|------------|----------|
| `wb_analytics_sales_funnel` | Воронка продаж |
| `wb_analytics_search_report` | Отчёт по поисковым запросам |
| `wb_analytics_stocks_wb` | Остатки на складах WB |
| `wb_analytics_csv_create` | Создать CSV-отчёт |
| `wb_analytics_csv_download` | Скачать CSV-отчёт |
| ... | и другие |

### Отчёты (~24)

| Инструмент | Описание |
|------------|----------|
| `wb_report_orders` | Отчёт по заказам |
| `wb_report_sales` | Отчёт по продажам |
| `wb_report_warehouse_remains_create` | Создать отчёт по остаткам |
| `wb_report_paid_storage_create` | Создать отчёт по хранению |
| `wb_report_regional_sales` | Региональные продажи |
| `wb_report_brand_share` | Доля бренда |
| `wb_report_returns` | Отчёт по возвратам |
| ... | и другие |

### Документы и бухгалтерия (~13)

| Инструмент | Описание |
|------------|----------|
| `wb_finance_balance` | Баланс продавца |
| `wb_finance_sales_reports` | Список отчётов о продажах |
| `wb_finance_sales_report_detail` | Детальный отчёт о продажах |
| `wb_finance_acquiring_reports` | Отчёты по эквайрингу |
| `wb_finance_document_categories` | Категории документов |
| `wb_finance_documents` | Список документов |
| `wb_finance_document_download` | Скачать документ |
| ... | и другие |

### Цифровые товары WBD (~12)

| Инструмент | Описание |
|------------|----------|
| `wb_wbd_keys_add` | Добавить ключи активации |
| `wb_wbd_keys_delete` | Удалить ключи активации |
| `wb_wbd_keys_list` | Список ключей |
| `wb_wbd_offers` | Список цифровых офферов |
| `wb_wbd_offer_create` | Создать оффер |
| `wb_wbd_offer_price` | Обновить цену оффера |
| `wb_wbd_catalog` | Каталог WBD |
| ... | и другие |

## CLI

Пакет также предоставляет интерфейс командной строки:

```bash
# Режим MCP-сервера (по умолчанию, без аргументов)
mcp-server-wildberries

# Режим CLI
mcp-server-wildberries ping
mcp-server-wildberries seller-info
mcp-server-wildberries tariff-commissions
mcp-server-wildberries fbs-orders-new
mcp-server-wildberries report-sales --date-from 2024-01-01

# Версия
mcp-server-wildberries --version
```

## Разработка

```bash
pip install -e ".[test]"
pytest tests/ -v
```

## Лицензия

MIT
