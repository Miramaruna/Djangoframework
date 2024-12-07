from django.shortcuts import render
from rest_framework.generics import ListAPIView
from apps.main.models import Settings
from .serializers import SettingsSerilizer
# Create your views here.

def setting(request):
    setting = Settings.objects.latest('id')
    return render(request, 'index.html', locals())

"""

APIview

ViewSets

"""

class SettingsListApi(ListAPIView):
    "queryset - передача обьектов"   
    queryset = Settings.objects.all()
    serializer_class = SettingsSerilizer

class SettingsCreateApi(CreateApiView):
    queryset = Settings.objects.all()
    