web: gunicorn udemy-weather.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
