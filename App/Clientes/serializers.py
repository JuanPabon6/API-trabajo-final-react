from rest_framework import serializers
from .models import Clientes
from django.contrib.auth.models import User


class UserClientesSereializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs ={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=True
        )
        return user

class ClientesSerializers(serializers.ModelSerializer):
    user = UserClientesSereializers()

    class Meta:
        model = Clientes
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserClientesSereializers.create(UserClientesSereializers(), validated_data=user_data)
        cliente = Clientes.objects.create(user=user, **validated_data)
        return cliente