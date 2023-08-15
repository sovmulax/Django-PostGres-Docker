#!/bin/sh

until cd /usr/src/app/backend; do
    echo "Waiting for server volume..."
done

# run beats :)
celery -A core beat -l info