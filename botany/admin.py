from django.contrib import admin

# Register your models here.
from .models import Flotation, LightFraction, FractionComposition, FractionMaterialsPresent

admin.site.register(Flotation)
admin.site.register(LightFraction)
admin.site.register(FractionComposition)
admin.site.register(FractionMaterialsPresent)
