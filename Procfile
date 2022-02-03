release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT neural_models_api.asgi:application
