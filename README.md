--Personal Finance API

Backend-приложение для учёта личных финансов: доходов, расходов, аналитики по категориям и месяцам. Реализовано на Django + Django REST Framework с авторизацией через JWT.

--Функциональность

- Регистрация и авторизация пользователей
- CRUD-операции для категорий (доходы и расходы)
- CRUD-операции для транзакций
- Аналитика по категориям и по месяцам
- JWT авторизация через SimpleJWT
- Swagger-документация
- Фильтрация и сортировка транзакций
- PostgreSQL в качестве основной БД
- Автоматические тесты на ключевые функции

--Стек

- Python 3.11+
- Django 5.2+
- Django REST Framework
- SimpleJWT
- PostgreSQL
- Swagger (drf-yasg)
- Django Filter

--Установка и запуск

1. Клонировать репозиторий:

```bash
git clone https://github.com/Skwozz/personal-finance-api.git
cd personal-finance-api
```

2. Создать и активировать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Настроить `.env` (опционально) или прописать БД в `settings.py`

5. Применить миграции и запустить сервер:

```bash
python manage.py migrate
python manage.py runserver
```

--Авторизация

1. Зарегистрироваться через `POST /api/register/`
2. Получить JWT токен по `POST /api/token/`:
```json
{
  "username": "user",
  "password": "pass"
}
```
3. Подставить токен в заголовок:
```
Authorization: Bearer <access_token>
```

--Эндпоинты

--Категории
- `GET /api/categories/`
- `POST /api/categories/`
- `PUT /api/categories/<id>/`
- `DELETE /api/categories/<id>/`

--Транзакции
- `GET /api/transactions/`
- `POST /api/transactions/`
- `GET /api/transactions/?type=IN&ordering=-amount`

--Аналитика
- `GET /api/analytics/monthly/` — сумма по месяцам
- `GET /api/analytics/category/` — сумма по категориям

--Документация

Swagger доступен по адресу:
```
/swagger/
```

--Тестирование

```bash
python manage.py test
```

Покрыты: регистрация, логин, CRUD, аналитика, защита авторизацией.

--Автор

[Skwozz (GitHub)](https://github.com/Skwozz)
