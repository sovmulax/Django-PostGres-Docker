from maintenance_mode.backends import AbstractStateBackend
from django.contrib.auth.models import AnonymousUser
from django.urls import resolve
from core.settings.base import MAINTENANCE_MODE_IGNORE_SUPERUSER, MAINTENANCE_MODE_IGNORE_ADMIN_SITE

from .models import MaintenanceMode

class DatabaseBackend(AbstractStateBackend):
    def get_value(self, request=None):
        # Récupère l'état de maintenance depuis la base de données
        try:
            maintenance = MaintenanceMode.objects.first()
            is_active = maintenance.is_active if maintenance else False

            # Ignorer le mode maintenance pour les superutilisateurs
            if request and hasattr(request, 'user'):
                if request.user.is_superuser and MAINTENANCE_MODE_IGNORE_SUPERUSER:
                    return False

            # Ignorer le mode maintenance pour l'administration
            if request and resolve(request.path_info).app_name == 'admin' and MAINTENANCE_MODE_IGNORE_ADMIN_SITE:
                return False

            return is_active
        except MaintenanceMode.DoesNotExist:
            return False

    def set_value(self, val):
        # Met à jour ou crée l'état de maintenance dans la base de données
        maintenance, _ = MaintenanceMode.objects.get_or_create(pk=1)
        maintenance.is_active = val
        maintenance.save()

