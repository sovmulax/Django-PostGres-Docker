from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.prod")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "Task_one_schedule": {
        "task": "appname.tasks.task_one",
        "schedule": crontab(hour=8, minute=0),  # Tous les jours à 8h00
        "options": {"expires": 60 * 60},  # Expire après 1 heure si pas exécutée
    },
}
