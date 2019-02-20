from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms
# from django.utils.translation import ugettext
# import django_filters
# from django_filters.filterset import ORDER_BY_FIELD

# from .forms import SwitchForm
# Create your views here.

from depot.models import Sample, Container, Location, Storage, JoinSampleContainer

#### ALL RECORDS ####
def allstorage(request):
    allstorage = Storage.objects.all()
    return render(request, 'storage/allstorage.html',
    {
        'storage':allstorage
    })

def alllocation(request):
    alllocation = Location.objects.all()
    return render(request, 'location/alllocation.html',
    {
        'location':alllocation
    })

def allcontainer(request):
    allcontainer = Container.objects.all()
    return render(request, 'container/allcontainer.html',
     {
        'container':allcontainer
    })

def alldepotsample(request):
    alldepotsample = Sample.objects.all()
    # allrealatedcontainers = sample_id__sample_id.all()
    # joinsamplecontainer = Sample.objects.filter(sample_id__sample_id=sample_id)
    return render(request, 'depotsample/alldepotsample.html',
    {
        'alldepotsample':alldepotsample,
        # 'relcon': joinsamplecontainer,
    })

#### DETAILS ####

def detailstorage(request, store_id):
    detailstorage = get_object_or_404(Storage, pk=store_id)
    return render(request, 'storage/detailstorage.html', {'storage':detailstorage})

def detaillocation(request):
    pass

def detailcontainer(request, container_id):
    detailcontainer = get_object_or_404(Container, pk=container_id)
    #samples = Samples.objects.filter(sample_id__container_id=container.pk)
    #samples = JoinSampleContainer.objects.filter(sample_id__container_id=container.pk)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(container_id = 4)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(container_id = 4)
    joinsamplecontainer = JoinSampleContainer.objects.filter(container_id__container_id=container_id)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(container__id = container_id)
    #samples = Samples.objects.filter(container__pk=samples.pk)
    # location = location.container_set.all()
    return render(request, 'container/detailcontainer.html',
    {'container':detailcontainer,
    'joinsamplecontainer':joinsamplecontainer
    })

def detaildepotsample(request, sample_id):
    pass


# def containercontentsdetail(request):
#     # containercontentsdetail = Container.objects.all()
#     # samplecontentdetail = Sample.objects.all()
#     return render(request, 'container/containercontents.html',
#     {
#         'containercontentdetail':containercontentsdetail
#     })



#### CREATE ####

def createstorage(request):
    if request.method == "POST":
        form = StorageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.modified_by = request.user
            post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allstorage')
    else:
        form = StorageForm()
    return render(request, 'storage/create_storage.html', {'form': form})

def createlocation(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('alllocation')
    else:
        form = LocationForm()
    return render(request, 'location/createlocation.html', {'form': form})

def createcontainer(request):
    if request.method == "POST":
        form = ContainerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allcontainer')
    else:
        form = ContainerForm()
    return render(request, 'container/create_container.html', {'form': form})

def create_join_sample_container(request):
    if request.method == "POST":

        form = JoinSampleContainerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('all_sample_container_joins')
    else:
        form = JoinSampleContainerForm()
    return render(request, 'join_sample_container/create_join_sample_container.html', {'form': form})


def adddepotsample(request):
    if request.method == "POST":
        form = DepotSampleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #botany_id = pk
            # post.analyst = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('alldepotsample')
    else:
        form = DepotSampleForm()
    return render(request, 'depotsample/adddepotsample.html', {'form': form})


# def assignsample(request):
#     media = Container.objects.all()
#     if request.method == "POST":
#         form = AssignForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.user = request.user
#             #post.datetime = datetime.datetime.now()
#
#             post.save()
#             return redirect('alldepotsamples')
#     else:
#         form = AssignForm()
#     return render(request, 'depotsample/assignsample.html',
#     {
#         'form': form,
#         'media': media
#     })




#### EDIT ####

def editstorage(request, pk):
    post = get_object_or_404(Storage, pk=pk)
    if request.method == "POST":
        form = StorageForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allstorage')
            #, pk=post.pk)
    else:
        form = StorageForm(instance=post)
    return render(request, 'storage/create_storage.html', {'form': form})


def editlocation(request, pk):
    post = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('alllocation', pk=location.pk)
            #, pk=post.pk)
    else:
        form = LocationForm(instance=post)
    return render(request, 'location/createlocation.html', {'form': form})

def editcontainer(request, pk):
    post = get_object_or_404(Container, pk=pk)
    if request.method == "POST":
        form = ContainerForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allcontainer')
            #, pk=post.pk)
    else:
        form = ContainerForm(instance=post)
    return render(request, 'container/create_container.html', {'form': form})

def edit_join_sample_container(request, pk):
    post = get_object_or_404(JoinSampleContainer, pk=pk)
    if request.method == "POST":
        form = JoinSampleContainerForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('all_sample_container_joins')
            #, pk=post.pk)
    else:
        form = JoinSampleContainerForm(instance=post)
    return render(request, 'join_sample_container/create_join_sample_container.html', {'form': form})

def editdepotsample(request, pk):
    post = get_object_or_404(Sample, pk=pk)
    if request.method == "POST":
        form = DepotSampleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('alldepotsample')
            #, pk=post.pk)
    else:
        form = DepotSampleForm(instance=post)
    return render(request, 'depotsample/adddepotsample.html', {'form': form})

def assignsample(request, pk, container=''):
    post = get_object_or_404(Sample, pk=pk)
    media = Container.objects.all()
    if request.method == "POST":
        form = MultipleSampleForm(request.POST, instance=post)
        # media = AssignForm2(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        # if media.is_valid():
        #     post2 = media.save(commit=False)
        #     post2.save()
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            return redirect('alldepotsamples')
            #, pk=post.pk)
    else:
        form = MultipleSampleForm(instance=post)
        # media = AssignForm2(instance=post)
    return render(request, 'depotsample/assignsample.html',
    {
        'form': form,
        'media': media
    })

# def containercontents(request, pk):
#     post = get_object_or_404(Container, pk=pk)
#         # objects = Container.samples.all()
#     if request.method == "POST":
#         form = ContainerContentsForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.user = request.user
#             #post.datetime = datetime.datetime.now()
#             post.save()
#             return redirect('allcontainer')
#             #, pk=post.pk)
#     else:
#         form = ContainerContentsForm(instance=post)
#     return render(request, 'container/containercontents.html', {'form': form})


# def containercontents(request, pk):
#     post = get_object_or_404(Container, pk=pk)
#     if request.method == "POST":
#         form = ContainerContentsForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.user = request.user
#             #post.datetime = datetime.datetime.now()
#             post.save()
#             return redirect('allcontainer')
#             #, pk=post.pk)
#     else:
#         form = ContainerContentsForm(instance=post)
#     return render(request, 'container/containercontents.html', {'form': form})














# def containercontents(request, pk):
#     containercontents = get_object_or_404(Container, pk=pk)
#     # samples = Sample.containers
#
#     samples = forms.ModelMultipleChoiceField(
#         queryset = Sample.objects.all()
#         )
#         # filter(...)
#     if request.method == "POST":
#         form = ContainerContentsForm(request.POST, instance=post)
#
#     return render(request, 'container/containercontents.html',
#     {
#         'containercontents':containercontents,
#         'samples':samples,
#     })


def containercontents(request, pk):
    post = get_object_or_404(Container, pk=pk)
    if request.method == "POST":
        form = ContainerContentsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allcontainer')
            #, pk=post.pk)
    else:
        form = ContainerContentsForm(instance=post)
    return render(request, 'container/containercontents.html', {'form': form})





class ContainerContentsForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = (
        # 'container_id',
        'location_id',
        'container_name',
        'container_type',

        'icon_desc',

        'samples',
        # 'sample_number'
        )


# class ContainerContentsForm(forms.ModelForm):
#     containers = forms.ModelChoiceField(queryset=Sample.objects.all())
#
#     class Meta:
#         model = Container
#         fields = [
#         'container_name',
#
#         ]

# def containercontents(request, pk):
#     containercontents = get_object_or_404(Container, pk=pk)
#     samples = forms.ModelMultipleChoiceField(
#         queryset = Sample.objects.all()
#         )
#     # samples = Sample.objects.all()
#
#     return render(request, 'container/containercontents.html',
#     {
#         'containercontents':containercontents,
#         'samples':samples,
#     })


# class ContainerContentsForm(forms.ModelForm):
#     class Meta:
#         # same code here
#
#     samples = forms.ModelMultipleChoiceField(
#         queryset = Sample.objects.all()
#     )


















#### DETAILS ####



# def alllocation_grid(request):
#     alllocation = Location.objects
#     return render(request, 'location/alllocation_grid.html', {'location':alllocation_grid})



#

#
#
#
#
#

#
#
#
# def checked_out(request, container_id):
#     post = get_object_or_404(Container, pk=pk)
#     if request.method == "POST":
#         form = ContainerForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.user = request.user
#             #post.datetime = datetime.datetime.now()
#             post.save()
#             return redirect('allcontainer', pk=container.pk)
#             #, pk=post.pk)
#     else:
#         form = ContainerForm(instance=post)
#     return render(request, 'container/create_container.html', {'form': form})
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
# # def allstorage(request):
# #     store = Store.objects
# #     return render(request, 'store/allstorage.html', {'store':store})
#

#


#
#
#
#
#
#
#
#
#
# def samplesearch(request):
#     pass
#
# def containerpage(request):
#     pass
#
# def listing(request):
#     pass
#
# #def alldepotsamples(request):
# #    return render(request,'samples/alldepotsamples.html',{})
#

#
#
#
#
#
#
# def containersearch(request):
#     container_list = Container.objects.all()
#     container_filter = ContainerFilter(request.GET, queryset=container_list)
#     return render(request, 'search/container_filter.html', {'filter': container_filter})
#
#
#
# def editcontainersearch(request, pk):
#     post = get_object_or_404(Container, pk=pk)
#     if request.method == "POST":
#         form = ContainerForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.user = request.user
#             #post.datetime = datetime.datetime.now()
#             post.save()
#             return redirect('containersearch')
#             #, pk=post.pk)
#     else:
#         form = ContainerForm(instance=post)
#     return render(request, 'container/create_container.html', {'form': form})
#
#
#

class DateInput(forms.DateInput):
    input_type = 'date'

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = (
        #'id',
        #'location_id',
        'store_id',
        'icon_desc',
        'location_type',
        'location_name',
        'orderby',

        )

class StorageForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = (
        #'id',
        'store_id',
        'store_name',
        'address_1',
        'address_2',
        'region',
        'zip',
        'city',
        'country',
        'icon_desc',

        )

class ContainerForm(forms.ModelForm):

    class Meta:
        model = Container
        fields = (
        # 'container_id',
        'location_id',
        'container_name',
        'container_type',
        'icon_desc'
        )

# class ContainerContentsForm(forms.ModelForm):
#     class Meta:
#         model = Container
#         fields = (
#         # 'container_id',
#         'location_id',
#         'container_name',
#         'container_type',
#
#         'icon_desc',
#
#         'samples',
#         # 'sample_number'
#         )

# class ContainerContentsForm(forms.ModelForm):
#     class Meta:
#         # same code here
#
#         samples = forms.ModelMultipleChoiceField(
#         queryset = sample.objects.filter(sample_id)
#         )

# class ProductForm(forms.ModelForm):
#     materials = forms.ModelMultipleChoiceField(Material.objects.all(), required=False)
#
#     class Meta:
#         model = Product
#         fields = ('product_field_1', 'product_field_2',...)

class JoinSampleContainerForm(forms.ModelForm):

    class Meta:
        model = JoinSampleContainer
        fields = (
        'id',
        'sample_id',
        # 'area_easting',
        # 'area_northing',
        # 'context_number',
        # 'sample_number',
        #container_id = models.ForeignKey(Container, db_column='container_id', on_delete = models.PROTECT)
        'container_id',

        )
#
# class SampleDepotForm(forms.ModelForm):
#     class Meta:
#         model = Sample
#         fields = (
#         # 'botany_id',
#         'sample_id',
#         'area_easting',
#         'area_northing',
#         'context_number',
#         'sample_number',
#         'sample_type',
#         'weight',
#         'description',
#         'recovery_method',
#         'taken_by',
#         'comments'
#
#         )
#
#         widgets = {
#             'entry_date': DateInput(attrs={'type': 'date'}),
#         }

class AssignForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = (
        # 'botany_id',
        'container_id',
        # 'area_easting',
        # 'area_northing',
        # 'context_number',
        # 'sample_number',
        # 'material_type',
        # 'weight',
        # 'description',
        # 'recovery_method',
        # # 'taken_by',
        # 'comments',
        'samples'


        )

        widgets = {
            'entry_date': DateInput(attrs={'type': 'date'}),
        }

class AssignForm2(forms.ModelForm):
    class Meta:
        model = Container
        fields = (
        # 'botany_id',
        'container_id',
        # 'area_easting',
        # 'area_northing',
        # 'context_number',
        # 'sample_number',
        # 'material_type',
        # 'weight',
        # 'description',
        # 'recovery_method',
        # # 'taken_by',
        # 'comments',
        'samples'


        )

        widgets = {
            'entry_date': DateInput(attrs={'type': 'date'}),
        }


class DepotSampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = (
        # 'botany_id',
        'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'sample_type',
        'weight',
        'description',
        'recovery_method',
        'taken_by',
        'comments'

        )

        widgets = {
            'entry_date': DateInput(attrs={'type': 'date'}),
        }


# class MultipleSampleForm(forms.ModelForm):
#     samples = forms.ModelMultipleChoiceField(Sample.objects.all(), required=False)
#
#     class Meta:
#         model = Sample
#         fields = ('sample_number',)
