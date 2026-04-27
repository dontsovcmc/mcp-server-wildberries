# CLAUDE.md

## Разработка

**CRITICAL: Все правила разработки описаны ниже. Всегда следовать им при любых изменениях кода, тестов и документации.**

### Запуск из исходников

```bash
pip install -e ".[test]"
```

### Запуск тестов

```bash
pytest tests/ -v
```

Тесты мокают API Wildberries — `WB_TOKEN` не нужен. Все тесты проходят локально без доступа к реальному API.

### CI

GitHub Actions: `.github/workflows/test.yml`, `runs-on: self-hosted`. Токен не требуется.

### Структура

```
src/mcp_server_wildberries/
├── __init__.py          # main(), версия
├── __main__.py          # python -m entry point
├── _shared.py           # FastMCP instance, хелперы (_get_api, _j, _save_bytes)
├── server.py            # импорт всех tools/, реэкспорт mcp
├── wb_api.py            # HTTP-клиент Wildberries Seller API
├── cli.py               # CLI-интерфейс
└── tools/
    ├── general.py       # Общее: ping, seller-info, rating
    ├── content.py       # Контент: категории, карточки, медиа, теги
    ├── fbs_orders.py    # FBS-заказы, стикеры, поставки, пропуска
    ├── dbw_orders.py    # DBW-заказы (доставка WB)
    ├── dbs_orders.py    # DBS-заказы (dropship)
    ├── pickup_orders.py # Самовывоз (click & collect)
    ├── fbw_supplies.py  # FBW-поставки на склад WB
    ├── advertising.py   # Реклама: кампании, ставки, статистика
    ├── communications.py # Отзывы, вопросы, чат
    ├── tariffs.py       # Тарифы и комиссии
    ├── analytics.py     # Аналитика: воронка, поисковые запросы
    ├── reports.py       # Отчёты: остатки, продажи, возвраты
    ├── finance.py       # Финансы: баланс, отчёты, документы
    └── wbd.py           # Цифровые товары WBD
```

### API Wildberries

- Документация: https://dev.wildberries.ru/
- OpenAPI спецификации: https://openapi.wildberries.ru/
- Авторизация: заголовок `Authorization` с JWT-токеном
- Base URL: разные домены по разделам (см. `BASES` в `wb_api.py`)

### Работа с заказами

Wildberries поддерживает несколько схем доставки:
- **FBS** (Fulfillment by Seller) — продавец собирает, WB доставляет
- **DBW** (Delivery by Wildberries) — WB забирает у продавца и доставляет
- **DBS** (Dropship by Seller) — продавец и собирает, и доставляет
- **Click & Collect** — самовывоз из магазина продавца
- **FBW** (Fulfillment by Wildberries) — товар хранится на складе WB

### ID-шники

- WB API привязан к одному аккаунту продавца через JWT-токен
- Дополнительных ID (campaign, business) не требуется — токен определяет продавца

### Обновление MCP-сервера

Когда пользователь просит "обнови mcp wildberries":

1. Определить способ установки:
   ```bash
   which mcp-server-wildberries && pip show mcp-server-wildberries
   ```
2. Обновить пакет:
   - **pip:** `pip install --upgrade mcp-server-wildberries`
   - **uvx:** `uvx --upgrade mcp-server-wildberries`
3. Проверить версию:
   ```bash
   mcp-server-wildberries --version
   ```
4. Сообщить пользователю новую версию и попросить перезапустить Claude Code.

### Правила

- **CRITICAL: НИКОГДА не коммить в master/main!** Все коммиты — только в рабочую ветку.
- **Все изменения — через Pull Request в main.** Создать ветку, закоммитить, сделать rebase на свежий main, запушить, создать PR.
- **ПЕРЕД КОММИТОМ проверить, не слита ли текущая ветка в main.** Если ветка уже слита (merged) — создать новую ветку от свежего main и делать новый PR. Никогда не пушить в уже слитую ветку.
- **MANDATORY BEFORE EVERY `git push`: rebase onto fresh main:**
  ```bash
  git checkout main && git remote update && git pull && git checkout - && git rebase main
  ```
- **NEVER use `git stash`.**
- **NEVER use merge commits. ALWAYS rebase.**
- **CRITICAL: НИКОГДА не читать содержимое `.env` файлов** — запрещено использовать `cat`, `Read`, `grep`, `head`, `tail` и любые другие способы чтения `.env`. Для загрузки переменных использовать **только** `source <path>/.env`.
- Не хардкодить токены и секреты в коде.
- stdout в MCP сервере занят JSON-RPC — для логов использовать только stderr.
- **ПЕРЕД КАЖДЫМ КОММИТОМ** проверять все файлы на наличие реальных персональных данных. Заменять на вымышленные.
- **В КАЖДОМ PR** обновлять версию в `pyproject.toml` и `src/mcp_server_wildberries/__init__.py` (patch для фиксов, minor для новых фич).
- **ПЕРЕД публикацией в MCP-реестр** обязательно запускать `mcp-publisher validate` — проверяет `server.json` на соответствие схеме реестра.
