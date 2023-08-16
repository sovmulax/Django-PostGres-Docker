#!/bin/sh

until cd /home/app/; do
    echo "Waiting for server volume..."
done

supervisord -n -c /etc/supervisor/conf.d/supervisord.conf

# run daemons :)
#supervisorctl reread
#supervisorctl update
#supervisorctl status all
