from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, 
                                     UpdateAPIView, DestroyAPIView, RetrieveAPIView,
                                     ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.viewsets import mixins, GenericViewSet
from .models import Settings
from .serializers import SettingsSerilizer, SettingsUpdateSerilizer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class Paginatoin(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class SettingsApi(GenericViewSet, mixins.ListModelMixin,     mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer
    pagination_class = Paginatoin

# class SettingsListAPI(ListAPIView):   
#     "queryset - передача объектов"
#     queryset = Settings.objects.all()
#     serializer_class = SettingsSerilizer


# class SettingsCreateAPI(CreateAPIView):
#     queryset = Settings.objects.all()
#     serializer_class = SettingsSerilizer


class SettingsRetrieveAPI(RetrieveAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer


# class SettingsUpdateAPI(UpdateAPIView):
#     queryset = Settings.objects.all()
#     serializer_class = SettingsUpdateSerilizer


# class SettingsDestroyAPI(DestroyAPIView):
#     queryset = Settings.objects.all()
#     serializer_class = SettingsSerilizer


# class SettingsListCreateAPI(ListCreateAPIView):
#     queryset = Settings.objects.all()
#     serializer_class = SettingsSerilizer


# class SettingsMultiAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Settings.objects.all()
#     serializer_class = SettingsSerilizer