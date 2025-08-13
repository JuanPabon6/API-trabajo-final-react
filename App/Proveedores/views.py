from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Proveedores
from .serializers import ProveedoresSerializers
from App.permissions import AdminOrReadOnly

class ProveedoresViewSets(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializers
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [JWTAuthentication]

# Create your views here.
