from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, 
                                     UpdateAPIView, DestroyAPIView, RetrieveAPIView,
                                     ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from .models import Settings
from .serializers import SettingsSerilizer, SettingsUpdateSerilizer
# Create your views here.

class SettingsListAPI(ListAPIView):
    "queryset - передача объектов"
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer


class SettingsCreateAPI(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer


class SettingsRetrieveAPI(RetrieveAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer


class SettingsUpdateAPI(UpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsUpdateSerilizer


class SettingsDestroyAPI(DestroyAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer


class SettingsListCreateAPI(ListCreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer


class SettingsMultiAPI(RetrieveUpdateDestroyAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer