from django.contrib import admin

# Register your models here.
from .models import Flotation, LightResidue, Composition

admin.site.register(Flotation)
admin.site.register(LightResidue)
admin.site.register(Composition)
