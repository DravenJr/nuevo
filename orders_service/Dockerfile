FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependencias necesarias para mysqlclient y mysqladmin
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    default-mysql-client \
    gcc \
    pkg-config \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /orders_service

# Instalar dependencias de Python primero (para cache)
COPY requirements.txt /orders_service/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar proyecto completo
COPY . /orders_service/

# Dar permisos al entrypoint
RUN chmod +x /orders_service/entrypoint.sh

# Exponer puerto para Gunicorn
EXPOSE 8000

# Iniciar el entrypoint
ENTRYPOINT ["/orders_service/entrypoint.sh"]
