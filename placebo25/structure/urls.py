from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    DivisionsViewSet,
    PositionsViewSet,
    StaffViewSet,
    PermissionsViewSet,
)


router = DefaultRouter()
router.register(r"divisions", DivisionsViewSet, basename="divisions")
router.register(r"positions", PositionsViewSet, basename="positions")
router.register(r"permissions", PermissionsViewSet, basename="permissions")
router.register(r"staff", StaffViewSet, basename="staff")

urlpatterns = [
    path("", include(router.urls)),
]
