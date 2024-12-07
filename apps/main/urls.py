from django.urls import path
from apps.main.views import SettingsListApi

urlpatterns = [
    path('', SettingsListApi.as_view(), name='settings_list_api'),
]