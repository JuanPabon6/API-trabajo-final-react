from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from .models import Administradores
from .serializers import AdministradoresSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from App.permissions import AdminOrReadOnly

class AdministradoresViewSets(viewsets.ModelViewSet):
    queryset = Administradores.objects.all()
    serializer_class = AdministradoresSerializer
    # authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    

# Create your views here.
