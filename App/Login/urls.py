from django.urls import path,include
from .views import CustomTokenObtainPairView, LogoutView
from rest_framework import routers

urlpatterns =[
    path('', CustomTokenObtainPairView.as_view(), name='login')
]