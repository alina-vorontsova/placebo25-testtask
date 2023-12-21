from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet

from .models import Divisions, Positions, Staff, Permissions
from .serializers import (
    DivisionsSerializer,
    PositionsSerializer,
    StaffSerializer,
    PermissionsSerializer,
)


def home_view(request):
    return redirect("/api/")


class DivisionsViewSet(ModelViewSet):
    queryset = Divisions.objects.all()
    serializer_class = DivisionsSerializer


class PositionsViewSet(ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer


class PermissionsViewSet(ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer


class StaffViewSet(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
