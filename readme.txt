# Описание проекта

1. Технологический стэк:
1.1 Бэкэнд (серверная часть)
- Python - язык программирования
- Django - web-фреймворк, написанный на языке Python
  Дополнительные зависимости Django:
  - psycopg2-binary - библиотека для работы с PostgreSQL
  - django-registration - библиотека предоставляющая функционал регистрации на сайте
  - django-bootstrap5 - библиотека подключающая Bootstrap5
- PostgreSQL - система управления реляционными базами данных (в облаке, сервис elephantsql.com)
  - Схема БД

1.2 Фронтэнд (клиентская часть)
- HTML (HyperText Markup Language) - язык гипертекстовой разметки
- CSS (Cascading Style Sheets) - каскадные таблицы стилей
- JS (javascript) - язык программирования работающий в броузере
- Bootstrap5 - CSS фреймворк


2. Структура проекта Django
.
|-item              # приложение для работы с Товарами
|-mysite            # базовое приложение сайта (содержит основные настройки)
|-warehouse         # приложение для работы со Складом
manage.py           # утилита для управления Django проектом
requirements.txt    # файл с зависимостями


3. Команды Django:
python3 manage.py makemigrations # создание файлов миграций (которые создают в итоге SQL-запросы к БД)
python3 manage.py migrate # применение файлов миграций
python3 manage.py collectstatic --no-input
python3 manage.py runserver 0:8001 # Запуск тестового сервера http://89.108.102.43:8001/