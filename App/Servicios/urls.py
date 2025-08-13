from django.urls import path, include
from rest_framework import routers
from .views import ServiciosViewSets

router = routers.DefaultRouter()
router.register(r'', ServiciosViewSets)

urlpatterns = [
    path('', include(router.urls))
]