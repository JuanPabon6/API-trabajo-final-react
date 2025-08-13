from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Clientes
from .serializers import ClientesSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.permissions import AdminOrReadOnly

class ClientesViewSets(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializers
    permission_classes = [permissions.AllowAny]
    # authentication_classes = [JWTAuthentication]

# Create your views here.
