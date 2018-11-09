from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from spatial3d.models import Photobatch
from django import forms

from .forms import PhotobatchForm

# Create your views here.
def allphotobatch(request):
    photobatch = Photobatch.objects.all()
    return render(request, 'photobatch/allphotobatch.html', {'photobatch':photobatch})

# Create your views here.
def createphotobatch(request):
    # Photobatch.photobatchphotos_set.all()
    if request.method == "POST":
        form = PhotobatchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allphotobatch')
    else:
        form = PhotobatchForm()
    return render(request, 'photobatch/create_photobatch.html', {'form': form})


def editphotobatch(request, pk):
    post = get_object_or_404(Photobatch, pk=pk)
    if request.method == "POST":
        form = PhotobatchForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allphotobatch')
            #, pk=post.pk)
    else:
        form = PhotobatchForm(instance=post)
    return render(request, 'photobatch/create_photobatch.html', {'form': form})

def detailphotobatch():
    pass

# def detailphotobatch(request, pb_id):
#      detailphotobatch = get_object_or_404(Photobatch, pk=pb_id)
#      return render(request, 'photobatch/detailphotobatch.html', {'photobatch':detailphotobatch})

# def remove_photobatch(request):
#     if request.method == 'POST':
#         form = PhotobatchForm()
#         photobatch = Photobatch.objects.all()
#         id = int(request.POST.get('id'))
#         photobatch = Photobatch.objects.get(id=id)
#         photobatch.delete()
#
# article1 = Article(name='article1')
#
#         return render_to_response('allphotobatch.html', {
#             'form':form , 'photobatch':photobatch,
#             }, RequestContext(request))

#VeryImportantSomething.objects.get(pk=123).delete()

def removephotobatch(request, pk):
    Photobatch.objects.get(pk=pk).delete()
    return redirect('/spatial3d/photobatch')

# class PhotobatchFilterForm(forms.ModelForm):
#     class Meta:
#         model = Photobatch
#         fields = (
#         'photobatch_id',
#         'prefix',
#         'area_easting',
#         'area_northing',
#         'context_number',
#         'number_of_photos',
#         # 'number_targets',
#         # 'processed_on',
#         'processed_by',
#         # 'camera_model',
#         'imported_photoscan',
#         #
#         'aligned',
#         # 'align_accuracy',
#         # 'align_pair_selection',
#         # 'align_keypoint_limit',
#         # 'align_tiepoint_limit',
#         'detected_targets',
#         # 'target_type',
#         # 'target_tolerance',
#         # 'target_origional_error',
#         # 'target_optimised_error',
#         'dense_pointcloud',
#         'mesh',
#         # 'mesh_type',
#         # 'mesh_face_count',
#         # 'mesh_interpolation',
#         #
# 		'texture',
#         # 'texture_defaults',
#         'dem',
#         # 'dem_coordinate_system',
#         # 'dem_source_data',
#         # 'dem_interpolation',
#         'orthomosaic',
#         # 'orthomosaic_type',
#         # 'orthomosaic_pixel_size',
#         # 'export_points',
#         # 'export_points_filename',
#         # 'export_points_offsets',
#         #
# 		# 'export_report_pdf',
#         # 'export_orthophoto',
#         # 'export_dem',
#         # 'export_dem_pixel_size',
#         # 'export_dem_geodatabase',
#         'folder_processed',
#         # 'processing_notes',
#         # #'image',
#         # #'created_timestamp',
#         'created_by'
#         # #'container_id'
#
#         )



# class PhotobatchFilter(django_filters.FilterSet):
#
#     class Meta:  # pylint: disable=C1001
#         model = Photobatch
#         fields = [
#         'photobatch_id',
#         'prefix',
#         'area_easting',
#         'area_northing',
#         'context_number',
#         'number_of_photos',
#         # 'number_targets',
#         # 'processed_on',
#         'processed_by',
#         # 'camera_model',
#         'imported_photoscan',
#         #
#         'aligned',
#         # 'align_accuracy',
#         # 'align_pair_selection',
#         # 'align_keypoint_limit',
#         # 'align_tiepoint_limit',
#         'detected_targets',
#         # 'target_type',
#         # 'target_tolerance',
#         # 'target_origional_error',
#         # 'target_optimised_error',
#         'dense_pointcloud',
#         'mesh',
#         # 'mesh_type',
#         # 'mesh_face_count',
#         # 'mesh_interpolation',
#         #
# 		'texture',
#         # 'texture_defaults',
#         'dem',
#         # 'dem_coordinate_system',
#         # 'dem_source_data',
#         # 'dem_interpolation',
#         'orthomosaic',
#         # 'orthomosaic_type',
#         # 'orthomosaic_pixel_size',
#         # 'export_points',
#         # 'export_points_filename',
#         # 'export_points_offsets',
#         #
# 		# 'export_report_pdf',
#         # 'export_orthophoto',
#         # 'export_dem',
#         # 'export_dem_pixel_size',
#         # 'export_dem_geodatabase',
#         'folder_processed',
#         # 'processing_notes',
#         # #'image',
#         # #'created_timestamp',
#         'created_by'
#         # #'container_id'
#
#         ]
#         # order_by = (
#         #     ('sample_number', ugettext("A-Z")),
#         #     ('-sample_number', ugettext("Z-A")),
#         # )
#
#
#
# class PhotobatchListView(FilterMixin, django_filters.views.FilterView):
#     model = Photobatch
#     paginate_by = 8
#     filterset_class = PhotobatchFilter
