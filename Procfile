release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker neural_models_api.asgi:application
worker: celery -A dtb worker -P solo --loglevel=INFO