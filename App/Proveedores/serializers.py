from rest_framework import serializers
from .models import Proveedores
from django.contrib.auth.models import User


class UserProveedoresSereializers(serializers.ModelSerializer):
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

class ProveedoresSerializers(serializers.ModelSerializer):
    user = UserProveedoresSereializers()

    class Meta:
        model = Proveedores
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserProveedoresSereializers.create(UserProveedoresSereializers(), validated_data=user_data)
        cliente = Proveedores.objects.create(user=user, **validated_data)
        return cliente