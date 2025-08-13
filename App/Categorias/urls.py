from django.urls import path,include
from rest_framework import routers
from .views import CategoriasViewSets

router = routers.DefaultRouter()
router.register(r'', CategoriasViewSets)

urlpatterns = [
    path('', include(router.urls))
]