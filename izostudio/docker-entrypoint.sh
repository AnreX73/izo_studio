#!/bin/sh
set -e

echo "[entrypoint] применяю миграции..."
python manage.py migrate --noinput

echo "[entrypoint] собираю статику..."
python manage.py collectstatic --noinput

echo "[entrypoint] запускаю: $*"
exec "$@"
