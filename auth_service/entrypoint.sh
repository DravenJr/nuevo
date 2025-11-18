#!/bin/bash
set -e

echo "Esperando a MySQL..."
until mysqladmin ping -h"$DB_HOST" -P"$DB_PORT" --silent; do
  sleep 1
done

echo "MySQL listo!"

# Crear superusuario si no existe
echo "Creando superusuario por defecto si no existe..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
EOF

# Iniciar Gunicorn
echo "Iniciando Gunicorn..."
exec gunicorn auth_service.wsgi:application --bind 0.0.0.0:8000
