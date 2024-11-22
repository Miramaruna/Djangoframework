from django.contrib import admin
from apps.Books.models import Authors, Books, Genre
# Register your models here.

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birthdate']
    list_filter = ['id', 'name', 'birthdate']
    search_fields = ['id', 'name', 'birthdate']
    # list_editable = ['is_active', ]

admin.site.register(Genre)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publication_year', 'authors']
    list_filter = ['id', 'title', 'publication_year', 'authors']
    search_fields = ['id', 'title', 'publication_year', 'authors']