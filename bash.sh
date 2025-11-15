#!/bin/bash
set -e

# Construir contenedores
echo "Construyendo imágenes"
docker compose build

# Iniciar contenedores en segundo plano
echo "Levantando servicios"
docker compose up -d

# Mostrar estado de los contenedores
echo "Servicios en ejecución:"
docker compose ps

echo "Usuario admin por defecto: admin / adminpass"
echo "Para detener todo: docker compose down"
