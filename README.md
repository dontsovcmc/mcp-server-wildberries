# mcp-server-wildberries

mcp-name: io.github.dontsovcmc/wildberries

MCP-сервер для **Wildberries Seller API** — товары, заказы, поставки, аналитика, реклама, финансы.

235 действий, покрывающих все разделы [WB API](https://dev.wildberries.ru/).

Построен по [официальной документации Wildberries API](https://dev.wildberries.ru/swagger/general).

## Архитектура

Сервер использует паттерн **search + execute** — вместо 235 отдельных инструментов предоставляет 3:

| Инструмент | Описание |
|------------|----------|
| `wb_search` | Поиск действий по описанию на естественном языке |
| `wb_execute` | Выполнение действия по ID |
| `wb_execute_file` | Выполнение действия со скачиванием файла |

Это экономит токены в контексте LLM — схемы 3 инструментов вместо 235.

### Как это работает

```
LLM: wb_search("cancel fbs order")
→ [{"id": "wb_fbs_order_cancel", "params_schema": {"order_id": "int"}, ...}]

LLM: wb_execute("wb_fbs_order_cancel", '{"order_id": 12345}')
→ {"status": "ok"}
```

## Настройка

### 1. Получите API-токен Wildberries

Откройте [Личный кабинет продавца WB](https://seller.wildberries.ru/) → Настройки → Доступ к API → Создать токен.

### 2. Установите и подключите

#### macOS / Linux

Установка:
```bash
pip install mcp-server-wildberries
```

Подключение к Claude Code (токен в командной строке):
```bash
claude mcp add wildberries -e WB_TOKEN=ваш-токен -- mcp-server-wildberries
```

Подключение к Claude Code (токен из .env файла):
```bash
source .env && claude mcp add wildberries -e WB_TOKEN -- mcp-server-wildberries
```

Удаление MCP-сервера:
```bash
claude mcp remove wildberries
```

CLI без Claude (токен в командной строке):
```bash
WB_TOKEN=ваш-токен mcp-server-wildberries ping
```

CLI без Claude (токен из .env файла):
```bash
source .env && mcp-server-wildberries ping
```

#### Windows

Установка:
```cmd
pip install mcp-server-wildberries
```

Подключение к Claude Code (токен в командной строке):
```cmd
set WB_TOKEN=ваш-токен && claude mcp add wildberries -e WB_TOKEN -- mcp-server-wildberries
```

Подключение к Claude Code (токен из .env файла):
```cmd
for /f "tokens=1,2 delims==" %a in (.env) do set %a=%b
claude mcp add wildberries -e WB_TOKEN -- mcp-server-wildberries
```

Удаление MCP-сервера:
```cmd
claude mcp remove wildberries
```

CLI без Claude (токен в командной строке):
```cmd
set WB_TOKEN=ваш-токен && mcp-server-wildberries ping
```

CLI без Claude (токен из .env файла):
```cmd
for /f "tokens=1,2 delims==" %a in (.env) do set %a=%b
mcp-server-wildberries ping
```

#### Запуск через uvx (без установки)

Если не хотите устанавливать пакет глобально, используйте `uvx` — он скачает и запустит автоматически:

```bash
# Подключение к Claude Code
claude mcp add wildberries -e WB_TOKEN=ваш-токен -- uvx mcp-server-wildberries

# CLI
WB_TOKEN=ваш-токен uvx mcp-server-wildberries ping
```

#### Запуск через --mcp-config (на одну сессию)

Подключает сервер только на время одной сессии Claude, не сохраняя в настройки. Токен хранится в отдельном `.env.mcp` файле, а не в конфиге Claude.

Из JSON-строки:
```bash
claude --mcp-config '{"wildberries":{"command":"bash","args":["-c","source ~/.env.mcp && exec uvx mcp-server-wildberries"]}}'
```

Из файла:
```bash
claude --mcp-config ~/mcp-servers.json
```

Только указанные серверы, без сохранённых:
```bash
claude --strict-mcp-config --mcp-config ~/mcp-servers.json
```

Пример `~/mcp-servers.json`:
```json
{
  "wildberries": {
    "command": "bash",
    "args": ["-c", "source ~/.env.mcp && exec uvx mcp-server-wildberries"]
  }
}
```

Пример `~/.env.mcp`:
```
WB_TOKEN=ваш-токен
```

Плюсы:
- Токены в отдельном файле `.env.mcp`, а не в настройках Claude
- Один файл `mcp-servers.json` на все проекты — легко делиться конфигом в команде
- `--strict-mcp-config` — запуск с точным набором серверов, без лишних
- Не засоряет глобальные настройки при экспериментах

Минусы:
- Сервер не сохраняется между сессиями — нужно указывать флаг при каждом запуске
- Длинная команда запуска, если без файла

После подключения перезапустите Claude Code.

### Переменные окружения

| Переменная | Обязательная | Описание |
|------------|--------------|----------|
| `WB_TOKEN` | Да | API-токен Wildberries (JWT) |

## Доступные действия (235)

Все действия доступны через `wb_search` → `wb_execute`. Подробное описание каждого действия — в документации по разделам:

| Домен | Кол-во | Описание |
|-------|--------|----------|
| [`general`](docs/general.md) | 9 | Ping, информация о продавце, пользователи |
| [`content`](docs/content.md) | 18 | Категории, карточки товаров, теги, бренды |
| [`fbs_orders`](docs/fbs_orders.md) | 31 | FBS-заказы, стикеры, поставки, пропуска, метаданные |
| [`dbw_orders`](docs/dbw_orders.md) | 16 | DBW-заказы (доставка WB) |
| [`dbs_orders`](docs/dbs_orders.md) | 20 | DBS-заказы (дропшиппинг) |
| [`pickup_orders`](docs/pickup_orders.md) | 16 | Самовывоз (click & collect) |
| [`fbw_supplies`](docs/fbw_supplies.md) | 7 | FBW-поставки на склад WB |
| [`advertising`](docs/advertising.md) | 26 | Рекламные кампании, ставки, статистика |
| [`communications`](docs/communications.md) | 22 | Вопросы, отзывы, чаты |
| [`tariffs`](docs/tariffs.md) | 5 | Комиссии, тарифы на доставку |
| [`analytics`](docs/analytics.md) | 17 | Воронка продаж, поисковые запросы, остатки |
| [`reports`](docs/reports.md) | 24 | Заказы, продажи, остатки, маркировка |
| [`finance`](docs/finance.md) | 12 | Баланс, отчёты, эквайринг, документы |
| [`wbd`](docs/wbd.md) | 12 | Цифровые товары, ключи активации |

### Примеры поиска

```
wb_search("новые заказы fbs")
wb_search("баланс")
wb_search("отзывы", domain="communications")
wb_search("download report", domain="reports")
```

## CLI

```bash
# MCP-сервер (по умолчанию, без аргументов)
mcp-server-wildberries

# Поиск действий
mcp-server-wildberries search "остатки на складах"

# Выполнение действия
mcp-server-wildberries execute wb_ping
mcp-server-wildberries execute wb_seller_info

# Выполнение с параметрами
mcp-server-wildberries execute wb_fbs_order_cancel --params '{"order_id": 12345}'

# Скачивание файла
mcp-server-wildberries execute-file wb_analytics_csv_download report.csv \
  --params '{"download_id": "abc"}'

# Прямые команды
mcp-server-wildberries ping
mcp-server-wildberries seller-info
mcp-server-wildberries fbs-orders-new
mcp-server-wildberries tariff-commissions

# Версия
mcp-server-wildberries --version
```

### Пример

```bash
$ WB_TOKEN=ваш-токен mcp-server-wildberries execute wb_ping
{"TS": "2026-05-06T18:06:30Z", "Status": "OK"}

$ WB_TOKEN=ваш-токен mcp-server-wildberries search "cancel order"
[
  {"id": "wb_fbs_order_cancel", "description": "Cancel FBS order", ...},
  {"id": "wb_dbs_order_cancel", "description": "Cancel DBS order", ...},
  ...
]
```

## Разработка

```bash
pip install -e ".[test]"
pytest tests/ -v
```

## Лицензия

MIT
