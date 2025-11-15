#!/bin/bash
set -e

echo "Esperando a MySQL en $DB_HOST:$DB_PORT..."
until mysqladmin ping -h"$DB_HOST" -P"$DB_PORT" --silent; do
  sleep 1
done
echo "MySQL está listo!"

echo "Aplicando migraciones..."
python manage.py migrate --noinput

echo "Iniciando Gunicorn..."
exec gunicorn products_service.wsgi:application --bind 0.0.0.0:8000
