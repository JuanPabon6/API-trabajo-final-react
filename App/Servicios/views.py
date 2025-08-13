from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Servicios
from .serializers import ServiciosSerialziers
from App.permissions import AdminOrReadOnly

class ServiciosViewSets(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerialziers
    permission_classes = [AdminOrReadOnly]
    authentication_classes = [JWTAuthentication]
# Create your views here.
