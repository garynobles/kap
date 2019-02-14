from django.contrib import admin

# Register your models here.
from .models import Flotation, Fraction, FractionComposition, FractionMaterialsPresent

admin.site.register(Flotation)
admin.site.register(Fraction)
admin.site.register(FractionComposition)
admin.site.register(FractionMaterialsPresent)
