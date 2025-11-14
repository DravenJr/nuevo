
#!/bin/bash
set -e
python manage.py migrate --noinput
# create default user if not exists (username: admin, password: adminpass)
python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); if not User.objects.filter(username='admin').exists(): User.objects.create_superuser('admin','admin@example.com','adminpass')"
# collectstatic if needed
exec gunicorn products_service.wsgi:application --bind 0.0.0.0:8000
