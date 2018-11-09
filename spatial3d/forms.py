from django.shortcuts import render
from django import forms
# from django.utils.translation import ugettext
# import django_filters
# from django_filters.filterset import ORDER_BY_FIELD
# Create your views here.


from .models import Photobatch
# from filters.views import FilterMixin


class PhotobatchForm(forms.ModelForm):

    class Meta:
        model = Photobatch
        fields = (
        #'sample_id',
        'photobatch_id',
        'prefix',
        'area_easting',
        'area_northing',
        'context_number',
        'number_of_photos',
        'number_targets',
        'processed_on',
        'processed_by',
        'camera_model',
        'imported_photoscan',
        #
        'aligned',
        'align_accuracy',
        'align_pair_selection',
        'align_keypoint_limit',
        'align_tiepoint_limit',
        'detected_targets',
        'target_type',
        'target_tolerance',
        'target_origional_error',
        'target_optimised_error',
        'dense_pointcloud',
        'mesh',
        'mesh_type',
        'mesh_face_count',
        'mesh_interpolation',
        #
        'texture',
        'texture_defaults',
        'dem',
        'dem_coordinate_system',
        'dem_source_data',
        'dem_interpolation',
        'orthomosaic',
        'orthomosaic_type',
        'orthomosaic_pixel_size',
        'export_points',
        'export_points_filename',
        'export_points_offsets',
        #
        'export_report_pdf',
        'export_orthophoto',
        'export_dem',
        'export_dem_pixel_size',
        'export_dem_geodatabase',
        'folder_processed',
        'processing_notes',
        #'image',
        # #'created_timestamp',
        'created_by'
        # #'container_id'

        )
