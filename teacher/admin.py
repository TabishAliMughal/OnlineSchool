from django.contrib import admin
from .models import *
from mapwidgets.widgets import GooglePointFieldWidget

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocation", [24.835052, 67.153083]),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'uk'}}),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyACgTHo7SLBqnZANd406ZF6h2xNMH58Flw"
}

class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        p.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }
    

admin.site.register(TeacherClass,CityAdmin)
admin.site.register(TeacherClassStudents)
