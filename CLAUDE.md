# CLAUDE.md

## Разработка

**CRITICAL: Все правила разработки описаны в [development.md](development.md). Всегда следовать им при любых изменениях кода, тестов и документации.**

### Запуск из исходников

```bash
pip install -e ".[test]"
```

### Загрузка переменных из файла

```bash
# MCP-сервер с env-файлом
mcp-server-wildberries --env /path/to/.env

# CLI с env-файлом
mcp-server-wildberries --env /path/to/.env <command>
```

`--env` загружает переменные через `python-dotenv` до инициализации сервера. Без `--env` — стандартные переменные окружения.

### Запуск тестов

```bash
ruff check src/ tests/
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
├── _shared.py           # FastMCP instance, хелперы (_get_api, _to_json, _parse_json, _safe_output_path, _save_bytes)
├── server.py            # 3 MCP tools: wb_search, wb_execute, wb_execute_file
├── actions.py           # Каталог 235 действий (Action dataclass, ACTIONS dict)
├── models.py            # Pydantic модели параметров (62 класса)
├── wb_api.py            # HTTP-клиент Wildberries Seller API
└── cli.py               # CLI-интерфейс (search/execute + прямые команды)
```

### Паттерн Search + Execute

Сервер предоставляет 3 MCP-инструмента вместо 235 отдельных. Все 235 действий доступны через каталог:

- `wb_search(query, domain?, limit?)` — поиск действий по ключевым словам
- `wb_execute(action, params_json)` — выполнение действия по ID
- `wb_execute_file(action, file_path, params_json)` — скачивание файла

Каталог (`actions.py`) хранит для каждого действия: ID, домен, описание, Pydantic-модель параметров, имя метода API, флаги (destructive, file), ключевые слова для поиска.

### Добавление нового действия

1. Добавить метод в `wb_api.py`
2. Если нужна новая модель параметров — добавить в `models.py`
3. Добавить `Action(...)` в `_ACTIONS_LIST` в `actions.py`
4. Добавить CLI-команду в `cli.py` (subparser + handler)

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

### README.md

При изменениях в коде обновлять [README.md](README.md):
- **Новый инструмент** — добавить строку в таблицу «Возможности» (MCP tool + CLI команда + описание).
- **Новая CLI-команда** — добавить в раздел «CLI-режим» → «Команды».
- **Новая переменная окружения** — добавить в таблицу «Переменные окружения».
- **Новый релиз** — обновить версию в бейджике.

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
- **В КАЖДОМ PR** обновлять версию в `pyproject.toml`, `src/mcp_server_wildberries/__init__.py` и `server.json` (patch для фиксов, minor для новых фич).
- **ПЕРЕД публикацией в MCP-реестр** обязательно запускать `mcp-publisher validate` — проверяет `server.json` на соответствие схеме реестра.

### Публикация версии

Валидация, сборка, загрузка в PyPI и публикация в MCP Registry — одной командой:

```bash
mcp-publisher validate && python3 -m build && twine upload dist/* && rm -rf ./dist && mcp-publisher login github && mcp-publisher publish
```
