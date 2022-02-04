release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --timeout-keep-alive 15 neural_models_api.asgi:application
