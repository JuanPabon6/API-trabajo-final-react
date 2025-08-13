from django.urls import path,include
from .views import loginApiView
from rest_framework import routers

urlpatterns =[
    path('', loginApiView.as_view(), name='login')
]