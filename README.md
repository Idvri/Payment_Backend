# Payment_Backend
Django + Stripe API бэкенд для осуществления оплаты.

### Stack: 
- Python 3.11;
- Django 5.0;
- Stripe;
- Docker;
- Gunicorn;
- Nginx.

### Environment variables:
- зарегистрируйтесь на сервисе Stripe для получения 'Publishable key' (STRIPE_PK) и 'Secret key' (STRIPE_SK);
- вам понадобиться ссылка: https://dashboard.stripe.com/test/apikeys;
- создайте файл .env и пропишите туда 'Publishable key' (STRIPE_PK) и 'Secret key' (STRIPE_SK) по аналогии с файлом env_example.

### Установка и запуск (Docker):
- docker-compose up --build - в первый раз;
- docker-compose up.

### Доступность (адреса):
- при деплое по адресу ВМ (нужно указать его в .env в переменной CSRF_TRUSTED_ORIGINS в формате http://0.0.0.0)

### Команды (локально):
###### Если запуск через Docker, то все команды будут выполнены автоматически.
- python manage.py csu - создать администратора. Логин и пароль: admin;
###### Важно!!! Выполняйте следующие команды в рамках описанной очереди ниже.
- python manage.py loaddata order_fixtures.json - наполнить БД данными из фикстур для заказов (Order);
- python manage.py loaddata items_fixtures.json - наполнить БД данными из фикстур для товаров (Item).

### Карты для тестирования:
- https://stripe.com/docs/testing#cards

### Функционал:
- localhost:8000/buy/{id} или localhost:8000/buy_order/{id} - создание сессии Stripe для дальнейшего осуществления покупки (GET);
- localhost:8000/item/{id} - отображение информации о выбранном товаре (GET);
- localhost:8000/order/{id} - отображение информации о выбранном заказе (GET);
- возможность осуществить покупку одного (Item) или нескольких (Order) товаров по кнопке "Buy" (происходит редирект на Checkout форму).