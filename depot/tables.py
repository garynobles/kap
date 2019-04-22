import django_tables2 as tables
from .models import Container, Sample

class ContainerTable(tables.Table):
    class Meta:
        model = Container
        # template_name = 'django_tables2/bootstrap.html'

class SampleTable(tables.Table):
    class Meta:
        model = Sample
        # template_name = 'django_tables2/bootstrap.html'
