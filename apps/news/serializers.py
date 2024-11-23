from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

from apps.news.models import Students, Transaction

class TransactionSerializers(serializers.ModelSerializer):
    # geekcoin = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Transaction
        fields = ['id', 'fromuser', 'touser', 'amount', 'created_at']

    def validate(self, attrs):
        fromuser = attrs.get('fromuser')
        touser = attrs.get('touser')
        amount = attrs.get('amount')
        # geekcoin = attrs.get('geekcoin')

        if fromuser.geekcoin is None:
            raise serializers.ValidationError('чота ты бомж')

        if fromuser == touser:
            raise serializers.ValidationError('Ти чо куку одинаковых делать??')

        babki = fromuser.geekcoin

        if babki < amount:
            raise serializers.ValidationError('У тебя недостаточно Geekcoins для этой транзакции.')

        return attrs

    def create(self, validated_data):
        fromuser = validated_data['fromuser']
        touser = validated_data['touser']
        amount = validated_data['amount']
        # geekcoin = validated_data['geekcoin']

        # fromuser_balance = fromuser.geekcoin  

        fromuser.geekcoin -= amount
        touser.geekcoin += amount

        fromuser.save()
        touser.save()

        transaction = Transaction.objects.create(
            fromuser=fromuser,
            touser=touser,
            amount=amount
        )

        return transaction

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'username', 'geekcoin']

class StudentsRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)
    class Meta:
        model = Students
        fields = ['id', 'username', 'email', 'password', 'confirm_password']

    def create(self, validated_data): 
        user = Students.objects.create(
            username=validated_data['username']
        )

        # user = Students.objects.create_user(
        # password=validated_data['password'],
        # username=validated_data['username']
        # )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Пароли не совпадают"})
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({'password': "Минимум 8 символов"})
        return attrs
    
class StudentBalanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'username', 'geekcoin']