from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet

router = DefaultRouter()
router.register("clients", ClientViewSet, basename="clients")

urlpatterns = [
    path("", include(router.urls)),
]
