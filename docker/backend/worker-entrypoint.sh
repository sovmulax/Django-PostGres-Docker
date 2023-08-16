#!/bin/sh

until cd /home/app/; do
    echo "Waiting for server volume..."
done

# run worker :)
celery -A core worker -l info