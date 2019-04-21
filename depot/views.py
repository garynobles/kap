from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms
from django.contrib.auth.models import User
# from django.utils.translation import ugettext
# import django_filters
# from django_filters.filterset import ORDER_BY_FIELD

# from .forms import SwitchForm
# Create your views here.

from depot.models import Sample, Container, Location, Storage, JoinSampleContainer, Friend, ContainerSamples


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)

    return redirect('depot:allcontainer')

def change_container(request, operation, pk='', fk=''):
    # pk = 12
    container = Container.objects.get(pk=pk)
    # container = Container.objects.all().filter(container_id=container.pk)
    # sample_id=29265881
    sample = Sample.objects.get(pk=fk)

    samplex = ContainerSamples.objects.all().filter(container_id=pk, sample_id=fk)
    # sample = sample.sample_id

    # sample = Container.objects.get(container.sample_id=sample_id)
    if operation == 'add':
        ContainerSamples.add_to_container(container, sample)
    elif operation == 'remove':
        ContainerSamples.remove_from_container(container, sample)
    return redirect('depot:allcontainer')

    # return redirect('depot:detailcontainer')


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
            return redirect('alldepotsample')
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
            return redirect('alllocation')
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
            return redirect('alldepotsample')
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

# def detail(request, place_id):
#     place = Place.objects.get(pk=place_id)
#     areas = place.area.all()

def detailcontainer(request, container_id):
    container = get_object_or_404(Container, pk=container_id)
    samples = container.samples.all()
    # allsamples = container.samples.exclude(sample_id=samples.sample_id)
    # allsamples = container.samples.all()
    users = User.objects.exclude(id=request.user.id).order_by('-id')
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all().order_by('-id')
    # container_contents = Container.objects.get(current_container=samples)
    container_contents = container.samples.all()
    # sample = ContainerSamples.objects.get(sample_id=s)
    # s = ContainerSamples.objects.all().filter(sample_id=29265877, container_id=13)
    unassigned_samples = Sample.objects.all()[:10]


    return render(request, 'container/detailcontainer.html',
    {'container':container,
    # 'samples':samples,
    'users': users,
    'friends': friends,
    # 'allsamples': allsamples,
    'container_contents': container_contents,
    'unassigned_samples': unassigned_samples

    })

# def containercontents(request, container_id):
#     container = get_object_or_404(Container, pk=container_id)
#     samples = container.samples.all()
#
#     container_contents = container.samples.all()[:20]
#
#     unassigned = Sample.objects.all()[:5]
#     return render(request, 'container/containercontents.html',
#     {'container':container,
#     'samples': samples,
#
#     'container_contents': container_contents,
#     'unassigned': unassigned
#     })

    # 'related_sample_list': related_samples_list,

    # 'unrelated_sample_list': unrelated_samples_list,


    # returns the container
    # container_contents = Container.objects.get(container_id=container.container_id)

    # related_samples_list = container_contents.samples.all()
    # unrelated_samples_list = related_samples_list.samples.all()

    # samples = Sample.objects.filter(sample_id__container_id=container.pk)
    #samples = JoinSampleContainer.objects.filter(sample_id__container_id=container.pk)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(container_id = 4)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(container_id = 4)
    # samples = Container.objects.filter(container_id__container_id=container_id)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(container__id = container_id)
    # samples = Samples.objects.filter(container__pk=samples.pk)
    # location = location.container_set.all()
    # samples = Container.objects.filter(container_id__container_id=container_id)


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
