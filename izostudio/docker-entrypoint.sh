#!/bin/sh
set -e

# Каталог для SQLite (на случай запуска без bind-mount)
mkdir -p /app/data

echo "[entrypoint] применяю миграции..."
python manage.py migrate --noinput

echo "[entrypoint] собираю статику..."
python manage.py collectstatic --noinput

echo "[entrypoint] запускаю: $*"
exec "$@"
