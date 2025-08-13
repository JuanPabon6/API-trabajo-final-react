from django.urls import path, include
from rest_framework import routers
from .views import RolesViewSets

router = routers.DefaultRouter()
router.register(r'', RolesViewSets)

urlpatterns = [
    path('', include(router.urls))
]