#!/bin/bash
set -e

echo "Starting Gateway..."
exec gunicorn gateway.wsgi:application --bind 0.0.0.0:8000
