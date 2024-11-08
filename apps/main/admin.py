from django.contrib import admin
from .models import Settings

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created')
    search_fields = ('title', 'description', 'created')
    list_filter = ('id', 'title', 'created')


# admin.site.register(Settings)
