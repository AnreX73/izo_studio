FROM python:3.11-slim

# Python: без .pyc и с небуферизованным выводом (логи сразу в docker logs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DJANGO_SETTINGS_MODULE=izostudio.settings

WORKDIR /app

# Системные зависимости для сборки mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Сначала зависимости — слой кэшируется, пока не меняется requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Код приложения
COPY . .

# Каталоги под тома (media/staticfiles) и запуск entrypoint
RUN mkdir -p /app/media /app/staticfiles \
    && chmod +x /app/docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# gunicorn запускается строкой, чтобы работали переменные окружения
CMD ["sh", "-c", "exec gunicorn izostudio.wsgi:application --bind 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-3} --timeout ${GUNICORN_TIMEOUT:-120} --max-requests 1000 --max-requests-jitter 100 --access-logfile - --error-logfile -"]
