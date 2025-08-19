#!/bin/bash

# Script pour rediriger les logs supervisor vers stdout/stderr pour Docker

# Créer les fichiers de logs s'ils n'existent pas
mkdir -p /var/log/supervisor
touch /var/log/supervisor/celery-worker.log
touch /var/log/supervisor/celery-beat.log
touch /var/log/supervisor/celery-worker-error.log
touch /var/log/supervisor/celery-beat-error.log

# Fonction pour préfixer les logs
prefix_logs() {
    local prefix="$1"
    local file="$2"
    tail -f "$file" 2>/dev/null | while IFS= read -r line; do
        echo "[$prefix] $line"
    done
}

# Lancer la surveillance des fichiers de logs en arrière-plan
prefix_logs "CELERY-WORKER" "/var/log/supervisor/celery-worker.log" &
prefix_logs "CELERY-BEAT" "/var/log/supervisor/celery-beat.log" &
prefix_logs "CELERY-WORKER-ERROR" "/var/log/supervisor/celery-worker-error.log" >&2 &
prefix_logs "CELERY-BEAT-ERROR" "/var/log/supervisor/celery-beat-error.log" >&2 &

# Attendre que tous les processus en arrière-plan se terminent
wait
