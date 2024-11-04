from django.contrib import admin
from .models import Settings

# Register your models here.

# admin.site.register(Settings)
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    field = ['id', 'titile', 'desription', 'logo']