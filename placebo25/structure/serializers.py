from rest_framework.serializers import ModelSerializer

from .models import Divisions, Permissions, Positions, Staff


class DivisionsSerializer(ModelSerializer):
    class Meta:
        model = Divisions
        fields = ["id", "name", "main_division", "subdivisions"]


class PermissionsSerializer(ModelSerializer):
    class Meta:
        model = Permissions
        fields = ["id", "name", "positions"]


class PositionPermissionsSerializer(ModelSerializer):
    class Meta:
        model = Permissions
        fields = ["name"]


class PositionsSerializer(ModelSerializer):
    permissions = PositionPermissionsSerializer(many=True, required=False)

    class Meta:
        model = Positions
        fields = ["id", "name", "divisions", "permissions"]


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = ["id", "name", "positions"]
