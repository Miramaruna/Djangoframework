from django.contrib import admin
from apps.news.models import Students, Transaction
# Register your models here.

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'geekcoin']
    list_filter = ['id', 'username', 'geekcoin']
    search_fields = ['id', 'username', 'geekcoin']
    # list_editable = ['is_active', ]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'fromuser', 'amount', 'created_at']
    list_filter = ['id', 'amount', 'created_at']
    search_fields = ['id', 'fromuser', 'amount', 'created_at']