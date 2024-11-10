from django.contrib import admin
from apps.news.models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'date',]
    list_filter = ['id', 'author', 'date',]
    search_fields = ['id', 'author', 'date',]