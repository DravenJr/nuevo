#!/bin/bash
set -e

#Arreglar entrypoints
echo "Arreglando entrypoints"
for service in auth_service products_service orders_service cart_service gateway; do
    dos2unix $service/entrypoint.sh
    chmod +x $service/entrypoint.sh
done

#Construir contenedores
echo "Construyendo imágenes"
docker compose build

#Levantar solo bases de datos y RabbitMQ
echo "Levantando bases de datos y RabbitMQ"
docker compose up -d mysql_auth mysql_products mysql_orders rabbitmq

#Esperar 10 segundos a que las DB estén listas
echo "Esperando que MySQL esté listo..."
sleep 10

#Levantar microservicios Django y gateway
echo "Levantando microservicios y gateway"
docker compose up -d auth_service products_service cart_service orders_service gateway

#Aplicar migraciones Django
echo "Aplicando migraciones"
for service in auth_service products_service orders_service cart_service; do
    docker compose exec $service python manage.py migrate
done

#Crear superusuario (usuario admin por defecto)
echo "Creando superusuario admin / adminpass"
docker compose exec auth_service python manage.py createsuperuser --noinput --username admin --email admin@example.com

#Mostrar estado de los contenedores
echo "Servicios en ejecución:"
docker compose ps

echo "Listo! Puedes acceder al Gateway en http://localhost:8000/"
echo "Para detener todo: docker compose down"
