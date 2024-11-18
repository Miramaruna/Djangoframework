from django.contrib import admin
from apps.news.models import Recipe
# Register your models here.

@admin.register(Recipe)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ingredients', 'instruction', 'prep_time', 'is_vegetarian', 'created_at']
    list_filter = ['id', 'name','is_vegetarian' ,  'created_at']
    search_fields = ['id', 'name', 'is_vegetarian', 'created_at']
    # list_editable = ['is_active', ]