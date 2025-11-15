# Tienda de Microservicios Django - Estructura Básica

Este repositorio contiene una arquitectura básica de microservicios implementada con Django y Django REST Framework,
lista para ejecutarse con Docker Compose para pruebas locales. Incluye los siguientes servicios:

- **auth_service** — emite tokens JWT (Django + DRF + SimpleJWT). Contiene un usuario administrador inicial.
- **products_service** — gestiona productos y categorías.
- **cart_service** — gestiona los carritos de compra por usuario (carrito simple en la base de datos).
- **orders_service** — realiza pedidos y notifica a través de RabbitMQ (estructura básica de Celery).
- **gateway** — una aplicación Django mínima que muestra una página HTML con la lista de endpoints y puede usarse como marcador de posición para una puerta de enlace API.

Cada servicio utiliza su propia base de datos MySQL. El secreto JWT se comparte mediante variables de entorno para que los servicios puedan verificar los tokens.

Se incluye RabbitMQ para la mensajería (pedidos -> notificaciones).

**Importante:** Contiene:

- Dockerfiles para cada servicio

- docker-compose.yml (nodos MySQL, RabbitMQ, servicios)

- Requisitos, .gitignore

- Puntos de entrada que ejecutan las migraciones y crean un usuario/configuración inicial

## Cómo ejecutar (local/desarrollo)

1. Asegúrese de que Docker y Docker Compose estén instalados.
2. Desde la raíz del repositorio, ejecute:

```bash
./bash.sh

docker compose up --build

```
3. El HTML del gateway se sirve en `http://localhost:8000/` (servicio de gateway).
4. Tokens de autenticación: POST `/api/token/` en auth_service (host `auth:8000` internamente; el gateway muestra las URL).

## Notas / Próximos pasos

- Proteja las claves secretas (no utilice la misma SECRET_KEY en producción).
- Configura volúmenes persistentes para MySQL en producción.
- Si es necesario, reemplaza SQLite en desarrollo; esta estructura usa MySQL en docker-compose.
- Agrega CORS, limitación de velocidad, proxy inverso de API Gateway (p. ej., nginx o proxy de Django), TLS y más.