from django.contrib import admin

# Register your models here.
from .models import Storage, Container, Location, Icon, Sample, Container


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
from django import forms

class ContainerAdminForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        form = super().__init__(*args, **kwargs)
        # Limit samples to 10
        self.fields['samples'].queryset = Sample.objects.all()[:10]

class ContainerAdmin(admin.ModelAdmin):
    list_display = ('container_name',)
    search_fields = ['container_name']
    filter_horizontal = ('samples',)
    # form = ContainerAdminForm
    #list_per_page = 5 # No of records per page

class SampleAdmin(admin.ModelAdmin):
    list_display = ('area_easting','area_northing','context_number','sample_number',)
    search_fields = ['sample_number']
    ordering = ('sample_number', 'area_easting', 'context_number')
    list_per_page = 20 # No of records per page


admin.site.register(Container, ContainerAdmin)
admin.site.register(Sample, SampleAdmin)
