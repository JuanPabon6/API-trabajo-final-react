from rest_framework import serializers
from .models import Administradores
from django.contrib.auth.models import User

class UserAdministradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=True
        )
        return user

class AdministradoresSerializer(serializers.ModelSerializer):
    user = UserAdministradoresSerializer()

    class Meta:
        model = Administradores
        fields = ['IdAdmin', 'user', 'NameAdmin', 'EmailAdmin', 'PhoneAdmin', 'RoleAdmin']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserAdministradoresSerializer.create(UserAdministradoresSerializer(), validated_data=user_data)
        admin = Administradores.objects.create(user=user, **validated_data)
        return admin