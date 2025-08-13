from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Producto
from .serializers import ProductosSerializers
from App.permissions import AdminOrReadOnly

class ProductosViewSets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializers
    permission_classes = [AdminOrReadOnly]
    authentication_classes = [JWTAuthentication]

# Create your views here.
