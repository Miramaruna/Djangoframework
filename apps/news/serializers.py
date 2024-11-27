from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

from apps.news.models import ToDo, User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'user', 'is_completed', 'created_at', 'image']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password', 'confirm_password']

    def create(self, validated_data): 
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        phone_number = attrs.get('phone_number')

        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Пароли не совпадают"})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password': "Минимум 8 символов"})
        if "+996" or "+(996)" not in phone_number:
            raise serializers.ValidationError({'phone_number':"ти кыргыз или нет шо?"})
        return attrs
    
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'created_at', 'email', 'phone_number']

class DeleteToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

class CreateToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'is_comleted', 'user', 'image']

    def create(self, validated_data):
        todo = ToDo.objects.create(
            title = validated_data['title']
        )
        todo.save()
        return todo
    
    # def validate(self, attrs):
        
    #     return attrs