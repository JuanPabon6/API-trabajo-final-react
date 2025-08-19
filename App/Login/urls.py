from django.urls import path,include
from .views import CustomTokenObtainPairView
from rest_framework import routers

urlpatterns =[
    path('', CustomTokenObtainPairView.as_view(), name='login')
]