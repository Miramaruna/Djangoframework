from django.urls import path
from apps.main.views import setting

urlpatterns = [
    path('', setting, name='setting'),
]