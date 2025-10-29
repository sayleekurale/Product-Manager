# Products Manager (Django + DRF + Chart.js)

Production-ready CRUD app with Products, REST APIs, inventory dashboard, and an external USD→INR rate.

## Features
- Product CRUD: name, description, category, price, stock
- REST API: list/create/update/delete
- Reports: inventory by category (Chart.js)
- External API: USD→INR exchange rate

## Tech
- Django 4.2, DRF, Bootstrap, Chart.js
- PostgreSQL-ready (Supabase) via DATABASE_URL
- Whitenoise + Gunicorn for deployment

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_products    # sample data
python manage.py runserver
```
Open: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin (user: admin, pass: adminpass)

## API
- GET/POST /api/products/products/
- GET /api/products/reports/inventory/
- GET /api/products/external/usd_inr/

## Deploy (Render)
- Build: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- Start: `gunicorn social_insight_app.wsgi:application --preload --workers=3 --timeout=60`
- Env: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `DATABASE_URL` (Supabase URI)
