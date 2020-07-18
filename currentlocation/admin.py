from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import *

# Register your models here.
@admin.register(AllEmployees)
class AllEmployeesAdmin(OSMGeoAdmin):
    list_display = ('user', 'name')

@admin.register(PersonelLocation)
class PersonelLocationAdmin(OSMGeoAdmin):
    list_display = ('rep', 'address', 'docname', 'timestamp')
