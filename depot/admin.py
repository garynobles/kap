from django.contrib import admin

# Register your models here.
from .models import Storage, Container, Location, Icon, Sample, Container
# from .views import SampleListView

admin.site.register(Storage)

admin.site.register(Location)
admin.site.register(Icon)





# class SampleAdmin(admin.ModelAdmin):
#     form = SampleListView
# admin.site.register(Sample, SampleAdmin)

# class ContainerAdmin(admin.ModelAdmin):
#     list_display = ('container_name',)
#     search_fields = ['container_name']
#     # filter_horizontal = ('samples',)
#
# class SampleAdmin(admin.ModelAdmin):
#     list_display = ('sample_number',)
#     search_fields = ['sample_number']
#
#
# admin.site.register(Container, ContainerAdmin)
# admin.site.register(Sample, SampleAdmin)



class ContainerAdmin(admin.ModelAdmin):
    list_display = ('container_name',)
    search_fields = ['container_name']
    filter_horizontal = ('samples',)
    list_per_page = 5 # No of records per page

class SampleAdmin(admin.ModelAdmin):
    list_display = ('sample_number',)
    search_fields = ['sample_number']
    list_per_page = 5 # No of records per page


admin.site.register(Container, ContainerAdmin)
admin.site.register(Sample, SampleAdmin)
