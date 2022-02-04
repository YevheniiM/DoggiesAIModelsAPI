release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornH11Worker neural_models_api.asgi:application
