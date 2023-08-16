#!/bin/sh

until cd /home/app/; do
    echo "Waiting for server volume..."
done

# run beats :)
celery -A core beat -l info