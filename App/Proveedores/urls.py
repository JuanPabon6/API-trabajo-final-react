from django.urls import path,include
from rest_framework import routers
from .views import ProveedoresViewSets

router = routers.DefaultRouter()
router.register(r'', ProveedoresViewSets)

urlpatterns = [
    path('', include(router.urls))
]