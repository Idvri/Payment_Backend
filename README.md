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

### Доступность (адреса):
- по адресу ВМ (нужно указать его в .env в переменной CSRF_TRUSTED_ORIGINS в формате http://0.0.0.0).

### Установка и запуск (Docker):
- git clone --single-branch -b nginx https://github.com/Idvri/Payment_Backend.git;
- docker-compose up --build - в первый раз;
- docker-compose up.

### Команды (локально):
###### Если запуск через Docker, то все команды будут выполнены автоматически.
- python manage.py csu - создать администратора. Логин и пароль: admin;
###### Важно!!! Выполняйте следующие команды в рамках описанной очереди ниже.
- python manage.py loaddata order_fixtures.json - наполнить БД данными из фикстур для заказов (Order);
- python manage.py loaddata items_fixtures.json - наполнить БД данными из фикстур для товаров (Item).

### Карты для тестирования:
- https://stripe.com/docs/testing#cards

### Функционал:
- http://your.site/buy/{id} или http://your.site/buy_order/{id} - создание сессии Stripe для дальнейшего осуществления покупки (GET);
- http://your.site/item/{id} - отображение информации о выбранном товаре (GET);
- http://your.site/order/{id} - отображение информации о выбранном заказе (GET);
- возможность осуществить покупку одного (Item) или нескольких (Order) товаров по кнопке "Buy" (происходит редирект на Checkout форму).
