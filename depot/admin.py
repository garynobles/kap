from django.contrib import admin

# Register your models here.
from .models import Storage, Container, Location, Icon

admin.site.register(Storage)
admin.site.register(Container)
admin.site.register(Location)
admin.site.register(Icon)
