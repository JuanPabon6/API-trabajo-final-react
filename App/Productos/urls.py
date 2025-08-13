from django.urls import path, include
from rest_framework import routers
from .views import ProductosViewSets

router = routers.DefaultRouter()
router.register(r'', ProductosViewSets)

urlpatterns = [
    path('', include(router.urls))
]