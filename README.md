# Stripe.com тестовое задание

Пример создания простого API для работы с [stripe.com](stripe.com).  

## Как установить и запустить

Скачайте код с репозитория.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

### Переменные окружения

Для работы сайта понадобятся следующие переменные окружения:

```bash
SECRET_KEY=YOUR_SECRET_KEY
ALLOWED_HOSTS=your_host_name_example.com
STRIPE_API_KEY=YOUR_STRIPE_API_KEY
```

### Как запустить

- Накатите миграции и создайте суперпользователя:

```bash
python manage.py migrate
python manage.py createsuperuser
```

- запуск сайта:

```bash
python manage.py runserver
```

### Методы API

- /buy/{id} - создание запроса на оплату
- /item/{id} - иформация о товаре

## Цели проекта

Выполнение тестового задание на должность Python Developer (Junior)

Тестовый сайт можно посмотреть [на pythonanywhere](https://kruser.pythonanywhere.com/)

Для оплаты используйте карту 4242 4242 4242 4242
