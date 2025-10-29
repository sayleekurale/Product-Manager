#!/bin/sh
set -e

# Run migrations and collect static files at container start
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn social_insight_app.wsgi:application \
  --bind 0.0.0.0:"${PORT:-8000}" \
  --preload \
  --workers "${WORKERS:-3}" \
  --timeout 60


