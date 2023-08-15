#!/bin/sh

until cd /usr/src/app/backend; do
    echo "Waiting for server volume..."
done

# run worker :)
celery -A core worker -l info