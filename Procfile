web: gunicorn Reader_XML.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
release: python manage.py makemigrations
release: python manage.py migrate