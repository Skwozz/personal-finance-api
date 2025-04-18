
# Personal Finance API 

Проект представляет собой REST API для управления личными финансами: доходами, расходами, категориями и аналитикой. Построен на Django + DRF + JWT.

##  Стек технологий

- Python 3.x
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt (JWT авторизация)
- SQLite (по умолчанию)
- Swagger (drf-yasg)

##  Возможности API

###  Аутентификация
- Регистрация: `POST /api/register/`
- JWT токен: `POST /api/token/`
- Обновление токена: `POST /api/token/refresh/`

###  Категории
- `GET /api/categories/` — список
- `POST /api/categories/` — создать
- `GET /api/categories/<id>/` — получить
- `PATCH /api/categories/<id>/` — обновить
- `DELETE /api/categories/<id>/` — удалить

###  Транзакции
- `GET /api/transactions/` — список
- `POST /api/transactions/` — создать
- `GET /api/transactions/<id>/` — получить
- `PATCH /api/transactions/<id>/` — обновить
- `DELETE /api/transactions/<id>/` — удалить

###  В планах
- `/analytics/monthly/` — отчёт по месяцам
- `/analytics/category/` — суммы по категориям
- PostgreSQL + Docker
- Автотесты

##  Документация
Swagger доступен по адресу:  
`/swagger/`

##  Автор
GitHub: [Skwozz](https://github.com/Skwozz)
