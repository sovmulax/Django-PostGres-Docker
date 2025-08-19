# maintenance/tasks.py
from celery import shared_task
from .models import MaintenanceMode
import logging

logger = logging.getLogger(__name__)


@shared_task
def activate_maintenance_mode():
    """
    Planned task to activate maintenance mode (Celery Beat).
    """
    try:
        maintenance_mode, created = MaintenanceMode.objects.get_or_create(pk=1)
        maintenance_mode.is_active = True 
        maintenance_mode.save()
        message = "Maintenance mode successfully activated."
        logger.info(message)
        return message
    except Exception as e:
        logger.error(f"Error activating maintenance mode: {e}")
        return str(e)


@shared_task
def deactivate_maintenance_mode():
    """
    Planned task to deactivate maintenance mode (Celery Beat).
    """
    try:
        maintenance_mode, created = MaintenanceMode.objects.get_or_create(pk=1)
        maintenance_mode.is_active = False
        maintenance_mode.save()
        message = "Maintenance mode successfully deactivated."
        logger.info(message)
        return message
    except Exception as e:
        logger.error(f"Error deactivating maintenance mode: {e}")
        return str(e)
