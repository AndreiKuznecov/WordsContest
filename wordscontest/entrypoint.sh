python manage.py makemigrations
python manage.py migrate
DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_EMAIL=ak.kuznetsow@yandex.ru python manage.py createsuperuser --noinput
python manage.py runserver 0.0.0.0:8000