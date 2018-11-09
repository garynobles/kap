from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext
import django_filters
from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.

from zooarch.models import Zooarch,Qnisp
from filters.views import FilterMixin



class ZooarchFilter(django_filters.FilterSet):

    def __init__(self, data={}, *args, **kwargs):
        super(ZooarchFilterForm, self).__init__(data, *args, **kwargs)  # NOQA
        try:
            self.fields[ORDER_BY_FIELD].widget.attrs = {
                'onchange': "this.form.submit();",
            }
        except KeyError:
            pass

    class Meta:  # pylint: disable=C1001
        form = ZooarchFilterForm
        model = Zooarch
        fields = [
        'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'portion',
        'element',
        'side',
        'sex',
        'taxonomic_description',
        'fusion',
        'age_estimation',
        'tooth_wear',
        'status',

        ]
        order_by = (
            ('sample_number', ugettext("A-Z")),
            ('-sample_number', ugettext("Z-A")),
        )


class QnispFilter(django_filters.FilterSet):

    def __init__(self, data={}, *args, **kwargs):
        super(QnispFilterForm, self).__init__(data, *args, **kwargs)  # NOQA
        try:
            self.fields[ORDER_BY_FIELD].widget.attrs = {
                'onchange': "this.form.submit();",
            }
        except KeyError:
            pass

    class Meta:  # pylint: disable=C1001
        form = QnispFilterForm
        model = Qnisp
        fields = [
        'qnisp_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'collection_method',
        'mandible_with_teeth',
        'bt',
        'ss',
        'oc_tje',
        'ch',
        'oa',
        'equid',
        'cer',
        'lp',
        'meles',
        'pesc',
        'brd',
        'canis',
        'unio',
        'cerastoderma',
        'landsnail',
        'shell_other',
        'rodent',
        'comments',
        'ursus',
        'big_feline_lynx_size',

        ]
        order_by = (
            ('sample_number', ugettext("A-Z")),
            ('-sample_number', ugettext("Z-A")),
        )
