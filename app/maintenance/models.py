from django.db import models


class MaintenanceMode(models.Model):
    # Stocke l'état du mode maintenance
    is_active = models.BooleanField(default=False, verbose_name="Mode maintenance activé")
    # Optionnel : permet de suivre la dernière mise à jour
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    def __str__(self):
        return "Mode maintenance actif" if self.is_active else "Mode maintenance inactif"