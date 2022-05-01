web: waitress-serve --port=$PORT Reader_XML.wsgi:application
python manage.py collectstatic --noinput
release: python manage.py makemigrations
release: python manage.py migrate