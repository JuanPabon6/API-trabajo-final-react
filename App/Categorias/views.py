from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Categorias
from .serializers import CategoriasSerializers 
from App.permissions import AdminOrReadOnly

class CategoriasViewSets(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializers
    permission_classes = [AdminOrReadOnly]
    authentication_classes = [JWTAuthentication]

# Create your views here.
