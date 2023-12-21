from django.contrib.admin import site, ModelAdmin

from .models import Divisions, Positions, Permissions, Staff


class DivisionsAdmin(ModelAdmin):
    fields = ["name", "main_division"]
    list_display = ["name", "main_division"]
    search_fields = ["name", "main_division"]


class PositionsAdmin(ModelAdmin):
    fields = ["name", "divisions"]
    list_display = ["name"]
    search_fields = ["name"]


class StaffAdmin(ModelAdmin):
    fields = ["name", "positions"]
    list_display = ["name"]
    search_fields = ["name"]


class PermissionsAdmin(ModelAdmin):
    fields = ["name", "positions"]
    list_display = ["name"]
    search_fields = ["name"]


site.register(Divisions, DivisionsAdmin)
site.register(Positions, PositionsAdmin)
site.register(Staff, StaffAdmin)
site.register(Permissions, PermissionsAdmin)
