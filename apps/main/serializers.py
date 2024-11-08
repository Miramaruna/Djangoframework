from rest_framework import serializers

from .models import Settings

class SettingsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'title', 'description', 'created']
        # fields = ('id', 'title', 'description')
        # fields = '__all__'
    
class SettingsUpdateSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'description', 'created']