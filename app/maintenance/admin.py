from django.contrib import admin
from .models import MaintenanceMode


@admin.register(MaintenanceMode)
class MaintenanceModeAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'updated_at')
    list_editable = ('is_active',)
    list_display_links = None
