from django.contrib import admin

# Register your models here.
from .models import Flotation, LightResidue, Composition, FractionMaterialsPresent

admin.site.register(Flotation)
admin.site.register(LightResidue)
admin.site.register(Composition)
admin.site.register(FractionMaterialsPresent)
