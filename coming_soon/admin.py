from django.contrib import admin
from .models import Settings


# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'show')


admin.site.register(Settings, SettingsAdmin)
