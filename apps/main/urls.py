from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("api_news/", SettingsApi, basename='api-news')

urlpatterns = [
    # path('SettingsApi', SettingsApi.as_view(), name='SettingsApi')
]

urlpatterns += router.urls

# urlpatterns = [
#     path('Settings', SettingsListAPI.as_view(), name="settings list api"),
#     path('create/', SettingsCreateAPI.as_view(), name="settings create api"),
#     path('<int:pk>/', SettingsRetrieveAPI.as_view(), name="settings retrieve api"),
#     path('update/<int:pk>/', SettingsUpdateAPI.as_view(), name="settings update api"),
#     path('delete/<int:pk>/', SettingsDestroyAPI.as_view(), name="settings delete api"),

#     path('list_create/', SettingsListCreateAPI.as_view(), name="settings create and list api"),
#     path('multi/<int:pk>/', SettingsMultiAPI.as_view(), name="settings multi api"),

# ]