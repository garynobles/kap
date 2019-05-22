from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.utils.translation import ugettext
# import django_filters
# from django_filters.filterset import ORDER_BY_FIELD

# from .forms import SwitchForm
# Create your views here.

from django_tables2 import RequestConfig
from django.shortcuts import render
from django_tables2 import SingleTableView


from depot.models import Sample, Container, Location, Storage, JoinSampleContainer, Friend, ContainerSamples


def SampleFliterView(request):
    qs = Sample.objects.all()
    easting_query = request.GET.get('area_easting')
    northing_query = request.GET.get('area_northing')
    context_query = request.GET.get('context_number')
    sample_number_query = request.GET.get('sample_number')
    sample_type_query = request.GET.get('sample_type')

    if easting_query != '' and easting_query is not None:
        qs = qs.filter(area_easting__icontains=easting_query)
    if northing_query != '' and northing_query is not None:
        qs = qs.filter(area_northing__icontains=northing_query)
    if context_query != '' and context_query is not None:
        qs = qs.filter(context_number__icontains=context_query)
    if sample_number_query != '' and sample_number_query is not None:
        qs = qs.filter(sample_number__icontains=sample_number_query)
    if sample_type_query != '' and sample_type_query is not None:
        qs = qs.filter(sample_type__icontains=sample_type_query)

    context = {
        'queryset': qs
    }
    return render(request, "container/filter.html", context)


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)

    return redirect('depot:allcontainer')

def change_container(request, operation, pk='', fk=''):
    container = Container.objects.get(pk=pk)
    sample = Sample.objects.get(pk=fk)

    if request.method == 'POST': # this is my guess work
        id_list = request.POST.getlist('') # this is my guess work

    if operation == 'add':
        ContainerSamples.add_to_container(container, sample)
    elif operation == 'remove':
        ContainerSamples.remove_from_container(container, sample)
    # return redirect('depot:allcontainer')

    return redirect('depot:detailcontainer', container_id=pk)



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
    container_list = Container.objects.all()
    user_list = User.objects.all()

    type = request.GET.get('type')
    name = request.GET.get('name')
    rack = request.GET.get('rack')
    shelf = request.GET.get('shelf')

    if (
    type =='' or type is None and
    name =='' or name is None and
    rack =='' or rack is None and
    shelf =='' or shelf is None
    ):
        allcontainer = allcontainer

    if type !='' and type is not None:
        allcontainer = allcontainer.filter(container_type__iexact=type)
    if name !='' and name is not None:
        allcontainer = allcontainer.filter(container_name__iexact=name)
    if rack !='' and rack is not None:
        allcontainer = allcontainer.filter(location_id__location_name__iexact=rack)
    if shelf !='' and shelf is not None:
        allcontainer = allcontainer.filter(location_id__location_sub_name__iexact=shelf)

    qs = allcontainer
    paginator = Paginator(qs, 25)
    page = request.GET.get('page')
    try:
        pub = paginator.page(page)
    except PageNotAnInteger:
        pub = paginator.page(1)
    except EmptyPage:
       pub = paginator.page(paginator.num_pages)
    # url_filter = PublicationFilter(request.GET, queryset=qs)

    context = {
    'container':allcontainer,
    'type': type,
    'pub':pub,
    # 'url_filter':url_filter
    # name
    # rack
    # shelf
    }

    return render(request, 'container/allcontainer.html', context)


    # def my_view(request):
    # filtered_qs = filters.MyModelFilter(
    #                   request.GET,
    #                   queryset=MyModel.objects.all()
    #               ).qs
    # paginator = Paginator(filtered_qs, YOUR_PAGE_SIZE)
    #
    # page = request.GET.get('page')
    # try:
    #     response = paginator.page(page)
    # except PageNotAnInteger:
    #     response = paginator.page(1)
    # except EmptyPage:
    #     response = paginator.page(paginator.num_pages)
    #
    # return render(
    #     request,
    #     'your_template.html',
    #     {'response': response}
    # )



    # Filtering solution?
    # if 'results' in request.GET and request.GET['results']:
    #         page = request.GET.get('page', 1)
    #
    #         results = request.GET['results']
    #         word = words.objects.filter(title__icontains = results).order_by('title')
    #         paginator = Paginator(word, 25) # Show 25 contacts per page
    #         word = paginator.page(page)
    #         return render_to_response('myapp/search.html',
    #                  {'word': word, 'query': results })
    #     else:
    #     return render(request, 'myapp/search.html')


def alldepotsample(request):
    alldepotsample = Sample.objects.all()
    # allrealatedcontainers = sample_id__sample_id.all()
    # joinsamplecontainer = Sample.objects.filter(sample_id__sample_id=sample_id)
    return render(request, 'depotsample/alldepotsample.html',
    {
        'alldepotsample':alldepotsample,
        # 'relcon': joinsamplecontainer,
    })


    # def my_view(request):
    # filtered_qs = filters.MyModelFilter(
    #                   request.GET,
    #                   queryset=MyModel.objects.all()
    #               ).qs
    # paginator = Paginator(filtered_qs, YOUR_PAGE_SIZE)
    #
    # page = request.GET.get('page')
    # try:
    #     response = paginator.page(page)
    # except PageNotAnInteger:
    #     response = paginator.page(1)
    # except EmptyPage:
    #     response = paginator.page(paginator.num_pages)
    #
    # return render(
    #     request,
    #     'your_template.html',
    #     {'response': response}
    # )

    # Filtering solution?
    # if 'results' in request.GET and request.GET['results']:
    #         page = request.GET.get('page', 1)
    #
    #         results = request.GET['results']
    #         word = words.objects.filter(title__icontains = results).order_by('title')
    #         paginator = Paginator(word, 25) # Show 25 contacts per page
    #         word = paginator.page(page)
    #         return render_to_response('myapp/search.html',
    #                  {'word': word, 'query': results })
    #     else:
    #     return render(request, 'myapp/search.html')


#### ADD ####



def createstorage(request):
    if request.method == "POST":
        form = StorageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            # post.modified_by = request.user
            # post.datetime = datetime.datetime.now()
            post.save()
            return redirect('depot:allstorage')
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
            return redirect('depot:alllocation')
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
            return redirect('depot:allcontainer')
    else:
        form = ContainerForm()
    return render(request, 'container/create_container.html', {'form': form})

# add
def adddepotsample(request):
    if request.method == "POST":
        form = DepotSampleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #botany_id = pk
            # post.analyst = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('depot:alldepotsample')
    else:
        form = DepotSampleForm()
    return render(request, 'depotsample/adddepotsample.html', {'form': form})

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
            return redirect('depot:allstorage')
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
            return redirect('depot:alllocation')
            #, pk=location.pk
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
            return redirect('depot:allcontainer')
            #, pk=post.pk)
    else:
        form = ContainerForm(instance=post)
    return render(request, 'container/create_container.html', {'form': form})

def editdepotsample(request, pk):
    post = get_object_or_404(Sample, pk=pk)
    if request.method == "POST":
        form = DepotSampleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('depot:alldepotsample')
            #, pk=post.pk)
    else:
        form = DepotSampleForm(instance=post)
    return render(request, 'depotsample/adddepotsample.html', {'form': form})


#### DETAILS ####

def detailstorage(request, store_id):
    detailstorage = get_object_or_404(Storage, pk=store_id)
    return render(request, 'storage/detailstorage.html', {'storage':detailstorage})

def detaillocation(request):
    pass

def detaildepotsample(request, sample_id):
    pass


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

            return redirect('depot:alldepotsamples')
            #, pk=post.pk)
    else:
        form = MultipleSampleForm(instance=post)
        # media = AssignForm2(instance=post)
    return render(request, 'depotsample/assignsample.html',
    {
        'form': form,
        'media': media
    })




def editcontainercontents(request, pk):
    post = get_object_or_404(Container, pk=pk)
    # containersamples = Container.objects.filter(container_id=pk)
    if request.method == "POST":
        form = ContainerContentsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('depot:allcontainer')
            #, pk=post.pk)
    else:
        form = ContainerContentsForm(instance=post)
    return render(request, 'container/containercontents.html',
     {
        'form': form,
        # 'containersamples': containersamples
    })



#### Forms.py

class ContainerContentsForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = (
        # 'container_id',
        'location_id',
        'container_name',
        'container_type',

        'icon_desc',

        # 'samples',
        # 'sample_number'
        )



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
        'location_sub_name',
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

from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Container, Sample
from .tables import ContainerTable, SampleTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

def detailcontainer(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    samples = container.samples.all()
    container_contents = container.samples.all()
    unassigned_samples = Sample.objects.all()

    qs = Sample.objects.all()
    easting_query = request.GET.get('area_easting')
    northing_query = request.GET.get('area_northing')
    context_query = request.GET.get('context_number')
    sample_number_query = request.GET.get('sample_number')
    sample_type_query = request.GET.get('sample_type')
    current_container_query = request.GET.get('container_name')

    if (
     easting_query == '' or easting_query is None and
     northing_query == '' or northing_query is None and
     context_query == '' or context_query is None and
     sample_number_query == '' or sample_number_query is None and
     sample_type_query == '' or sample_type_query is None
     # and
     # current_container_query == '' or current_container_query is None
     ):
        unassigned_samples = unassigned_samples.none()

    if easting_query != '' and easting_query is not None:
        unassigned_samples = unassigned_samples.filter(area_easting__iexact=easting_query)
    if northing_query != '' and northing_query is not None:
        unassigned_samples = unassigned_samples.filter(area_northing__iexact=northing_query)
    if context_query != '' and context_query is not None:
        unassigned_samples = unassigned_samples.filter(context_number__iexact=context_query)
    if sample_number_query != '' and sample_number_query is not None:
        unassigned_samples = unassigned_samples.filter(sample_number__iexact=sample_number_query)
    if sample_type_query != '' and sample_type_query is not None:
        unassigned_samples = unassigned_samples.filter(sample_type__iexact=sample_type_query)
    # if current_container_query != '' and current_container_query is not None:
    #     a=1+1
        # unassigned_samples = unassigned_samples.filter(container_set__container_name__icontains=current_container_query)
        # unassigned_samples = unassigned_samples.filter(container__container_name__contains=1)

    # qs = qs




    context = {
        # 'queryset': qs,
        'container':container,
        'container_contents': container_contents,
        'unassigned_samples': unassigned_samples,

        # 'users':users,

        'easting_query': easting_query,
        'northing_query': northing_query,
        'context_query': context_query,
        'sample_number_query': sample_number_query,
        'sample_type_query': sample_type_query,
        # 'current_container_query':current_container_query
    }
    return render(request, 'container/detailcontainer.html', context)



# class FilteredPersonListView(SingleTableMixin, FilterView):
#     table_class = SampleTable
#     model = Sample
#     template_name = 'template.html'

    # filterset_class = SampleFilter
