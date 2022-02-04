release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornH11Worker neural_models_api.asgi:application
worker: celery -A neural_models_api worker -P solo --loglevel=INFO