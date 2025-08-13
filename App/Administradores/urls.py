from django.urls import path,include
from .views import AdministradoresViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', AdministradoresViewSets)

urlpatterns = [
    path('', include(router.urls))
]