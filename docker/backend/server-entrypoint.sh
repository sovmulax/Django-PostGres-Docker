#!/bin/sh

until cd /home/app/; do
    echo "Waiting for server volume..."
done

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3 manage.py migrate
python3 manage.py migrate django_celery_results
python3 manage.py collectstatic --noinput

python3 manage.py createsuperuser --noinput

gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
