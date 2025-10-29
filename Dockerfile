FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps (psycopg needs build deps when using binary wheels fallback)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

# Default workers/port can be overridden by Koyeb env vars
ENV PORT=8000 \
    WORKERS=3 \
    DJANGO_SETTINGS_MODULE=social_insight_app.settings

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]


