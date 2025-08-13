from rest_framework import serializers
from .models import Servicios

class ServiciosSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'