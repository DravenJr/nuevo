#!/bin/bash
set -e

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null
then
    echo "Docker no está instalado o no está en el PATH."
    echo "Instálalo desde: https://docs.docker.com/get-docker/"
    exit 1
fi

# Verificar si Docker Compose está disponible
if ! docker compose version &> /dev/null
then
    echo "Docker Compose no está disponible."
    echo "Asegúrate de tener Docker Compose V2 (usa 'docker compose', no 'docker-compose')."
    exit 1
fi

# Construir contenedores
echo "Construyendo imágenes..."
docker compose build

# Iniciar contenedores en segundo plano
echo "Levantando servicios..."
docker compose up -d

# Esperar a que los servicios estén listos
echo ""
echo "Esperando a que los contenedores se inicialicen..."
sleep 10

# Mostrar estado de los contenedores
echo ""
echo "Servicios en ejecución:"
docker compose ps

echo ""
echo "Accede al API Gateway en: http://localhost:8000/"
echo "Usuario admin por defecto: admin / adminpass"
echo "RabbitMQ panel: http://localhost:15672/ (guest / guest)"
echo ""
echo "Para detener todo: docker compose down"
