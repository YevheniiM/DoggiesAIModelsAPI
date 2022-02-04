release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 3 --worker-class uvicorn.workers.UvicornWorker neural_models_api.asgi:application
