#!/bin/bash
set -e

echo "Arreglando entrypoints"
for service in auth_service products_service orders_service cart_service gateway; do
    if [ -f "$service/entrypoint.sh" ]; then
        dos2unix $service/entrypoint.sh
        chmod +x $service/entrypoint.sh
    fi
done

echo "Construyendo imágenes"
docker compose build

echo "Levantando bases de datos y RabbitMQ"
docker compose up -d mysql_auth mysql_products mysql_orders mysql_cart rabbitmq

echo "Esperando que MySQL esté listo..."
for db_service in mysql_auth mysql_products mysql_orders mysql_cart; do
    echo "Esperando que $db_service esté listo..."
    until docker compose exec $db_service mysqladmin ping -h "localhost" --silent; do
        echo "Esperando $db_service..."
        sleep 2
    done
done


echo "Levantando microservicios y gateway"
docker compose up -d auth_service products_service cart_service orders_service gateway

echo "Aplicando migraciones"
for service in auth_service products_service orders_service cart_service; do
    docker compose exec $service python manage.py migrate || true
done

echo "Creando superusuario admin / adminpass"
docker compose exec auth_service python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); \
if not User.objects.filter(username='admin').exists(): \
    User.objects.create_superuser('admin','admin@example.com','adminpass')"

docker compose ps
echo "Listo! Puedes acceder al Gateway en http://localhost:8000/"
