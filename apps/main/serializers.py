from rest_framework import serializers

from .models import Settings

class SettingsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'title', 'description', 'logo']  # можно ввиде списка, кортежа  или '__all__"