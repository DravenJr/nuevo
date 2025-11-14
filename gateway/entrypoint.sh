
#!/bin/bash
set -e
python manage.py migrate --noinput || true
exec gunicorn gateway.wsgi:application --bind 0.0.0.0:8000
