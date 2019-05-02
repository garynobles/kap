from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from .models import Sample
from .tables import SampleTable

class FilteredSampleListView(SingleTableMixin, FilterView):
    table_class = SampleTable
    model = Sample
    template_name = 'template.html'

    filterset_class = SampleFilter
