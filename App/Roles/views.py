from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Roles
from .serializers import RolesSerializers
from App.permissions import AdminOrReadOnly

class RolesViewSets(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers
    permission_classes = [AdminOrReadOnly]
    authentication_classes = [JWTAuthentication]

# Create your views here.
