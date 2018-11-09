from django.contrib import admin

# Register your models here.
from .models import Botany, Fraction, FractionComposition, FractionMaterialsPresent

admin.site.register(Botany)
admin.site.register(Fraction)
admin.site.register(FractionComposition)
admin.site.register(FractionMaterialsPresent)
