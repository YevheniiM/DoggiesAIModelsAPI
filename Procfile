release: python manage.py collectstatic --no-input; python manage.py migrate --noinput
web: gunicorn --bind :$PORT neural_models_api.wsgi:application -c gunicorn.py.ini
