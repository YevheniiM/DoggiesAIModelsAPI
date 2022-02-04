release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 3 --threads 12 --max_requests 1000 neural_models_api.wsgi:application
