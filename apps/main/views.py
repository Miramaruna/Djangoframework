from django.shortcuts import render
from apps.main.models import Settings
# Create your views here.

def setting(request):
    setting = Settings.objects.latest('id')
    return render(request, 'index.html', locals())
