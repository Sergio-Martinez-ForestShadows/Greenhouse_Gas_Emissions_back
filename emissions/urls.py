from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmissionViewSet

router = DefaultRouter()
router.register("emissions", EmissionViewSet, basename="emission")

urlpatterns = [
    path("", include(router.urls)),
]
