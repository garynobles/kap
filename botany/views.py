from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from botany.models import Flotation, LightResidue, Composition, Sample, Book
from django import forms

from django.db.models import Count, Q
from django.shortcuts import render

from itertools import chain

from dal import autocomplete


def allsample(request):
    allsample = Sample.objects.all()
    return render(request, 'sample/sample.html',
    {
    'allsample':allsample,
    })

def allflotation(request, sample_id='', flotation_id=''):
    flotation = Flotation.objects.all()
    lightresidue = LightResidue.objects.all()
    count = LightResidue.objects.all().count()
    composition = Composition.objects.all()
    return render(request, 'flotation/allflotation.html',
    {
    'flotation':flotation,
    'lightresidue':lightresidue,
    'count':count,
    'composition':composition,
    })


#### add ####

            #post.flotation_id = pk
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
def addsample(request):
    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('samplelist')
    else:
        form = SampleForm()
    return render(request, 'sample/createsample.html', {'form': form})

def addflotation(request, pk, fk=''):
        if request.method == "POST":
            form = FlotationForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                sample = get_object_or_404(Sample, pk=pk)
                post.sample_id = sample
                post.save()
                return redirect('allflotation')
        else:
            form = FlotationForm()
        return render(request, 'flotation/createflotation.html',
        {
            'form': form
        })

def addlightresidue(request, pk, fk=''):
    if request.method == "POST":
        form = LightResidueForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            flotation = get_object_or_404(Flotation, pk=pk)
            post.flotation_id = flotation
            post.save()
            #return redirect('allfraction')
            return redirect('allflotation')
    else:
        form = LightResidueForm()
    return render(request, 'lightresidue/create_lightresidue.html',
    {'form': form})

def addcomposition(request, pk, fk):
    if request.method == "POST":
    #if request.method == "GET":
        form = CompositionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            lightresidue = get_object_or_404(LightResidue, pk=pk)
            post.lightresidue_id = lightresidue
            post.save()
            #return redirect('allfraction')
            return redirect('allflotation')
    else:
        #import pdb; pdb.set_trace()
        form = CompositionForm()
    return render(request, 'composition/create_composition.html', {'form': form})

#### EDIT ####
def editlightresidue(request, pk, fk=''):
        post = get_object_or_404(LightResidue, pk=pk)
        if request.method == "POST":
            form = LightResidueForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('allflotation')
        else:
            form = LightResidueForm(instance=post)
        return render(request, 'lightresidue/create_lightresidue.html', {'form': form})

def editfraction(request):
    pass

def editflotation(request, pk):
        post = get_object_or_404(Flotation, pk=pk)
        if request.method == "POST":
            form = FlotationForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('allflotation')
        else:
            form = FlotationForm(instance=post)
        return render(request, 'flotation/createflotation.html', {'form': form})


def editsample(request, pk):
        post = get_object_or_404(Sample, pk=pk)
        if request.method == "POST":
            form = SampleForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('allsample')
        else:
            form = SampleForm(instance=post)
        return render(request, 'sample/createsample.html', {'form': form})



#### DETAIL ####

def detailsample(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    flotation = Flotation.objects.filter(sample_id__sample_id=sample_id)
    return render(request, 'sample/detailsample.html',
    {
        'sample':sample,
        'flotation':flotation,
    })

def detailflotation(request, flotation_id):
    flotation = get_object_or_404(Flotation, pk=flotation_id)
    lightresidue = LightResidue.objects.filter(flotation_id__flotation_id=flotation_id)
    return render(request, 'flotation/detailflotation.html',
    {
        'flotation':flotation,
        'lightresidue':lightresidue,
    })

def detaillightresidue(request, lightresidue_id):
    detaillightresidue = get_object_or_404(LightResidue, pk=lightresidue_id)
    composition = Composition.objects.filter(lightresidue_id__lightresidue_id=lightresidue_id)
    return render(request, 'lightresidue/detaillightresidue.html',
    {
        'lightresidue':detaillightresidue,
        'composition':composition,
    })




def allbotany(request, sample_id=''):
    # number = Botany.objects..count()
    number = Flotation.objects.all().count()
    lightresidue = LightResidue.objects.all()
    composition = Composition.objects.all()
    # fractionmaterialspresent = FractionMaterialsPresent.objects.all()

    dataset = Flotation.objects \
        .values('context_number') \
        .order_by('context_number')

    query1 = LightResidue.objects \
        .values('soil_volume')

    query2 = LightResidue.objects.values('soil_volume')
    query3 = LightResidue.objects.values('sample_volume')

    # query2 = LightResidue.objects \
    #     .values('sample_volume')
    dataset2 = LightResidue.objects.values('soil_volume')
    dataset3 = query3

    # a = LightResidue.objects.values('roots').filter(roots=True)
    # b = LightResidue.objects.values('bone').filter(bone=True)
    # c = LightResidue.objects.values('sediment').filter(sediment=True)
    # dataset4 = {"roots": a, "bone": b, "sediment": c}
    text = Flotation.objects.values('notes')



    roots = LightResidue.objects.filter(roots=True).count()
    bone = LightResidue.objects.filter(bone=True).count()
    sediment = LightResidue.objects.filter(sediment=True).count()
    shell = LightResidue.objects.filter(shell=True).count()
    stone = LightResidue.objects.filter(stone=True).count()
    leaves = LightResidue.objects.filter(leaves=True).count()
    insect_parts = LightResidue.objects.filter(insect_parts=True).count()
    charred_dung = LightResidue.objects.filter(charred_dung=True).count()
    dataset4 ={
        "roots": roots,
        "bone": bone,
        "sediment": sediment,
        "shell": shell,
        "stone": stone,
        "leaves": leaves,
        "insect parts": insect_parts,
        "charred dung": charred_dung}

    # import datetime
    timeseries = Flotation.objects.values('flotation_date')

    # .strftime("%Y-%m-%dT%H:%M:%S.%f")



# date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    # roots = LightResidue.objects \
    #     .values('roots').filter(roots=True)
    # bone = LightResidue.objects \
    #     .values('bone').filter(bone=True).count()
    bone=5


    # dataset5 = a.filter(roots=True)| b.filter(bone=True)
    # dataset6 = b.count()
    # dataset3 = LightResidue.objects.values('soil_volume')
    # matches = pages | articles | posts


        # query2 = LightResidue.objects.count('bone')
        #
        # sumquery = query1 + query2

            # .values('soil_volume') \
            # .annotate(num_values=Count('value'), average=Avg('value'))\
            # .order_by('soil_volume')


    return render(request, 'dashboard/botanyhome.html',
    {
    # 'botany':botany,
    'number':number,
    'lightresidue':lightresidue,
    'composition':composition,
    # 'fractionmaterialspresent':fractionmaterialspresent,

    'dataset': dataset,
    'dataset2': dataset2,
    'dataset3': dataset3,
    'dataset4': dataset4,
    # 'dataset5': dataset5,
    # 'dataset6': dataset6,
    'text': text,

    'roots': roots,
    'timeseries': timeseries,
    # 'bone': bone,

    })







class DateInput(forms.DateInput):
    input_type = 'date'

class FlotationForm(forms.ModelForm):
    class Meta:
        model = Flotation
        fields = (

        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'flotation_date',
        'entry_date',
        'analyst_id',
        'notes',
        )

        widgets = {
            'entry_date': DateInput(attrs={'type': 'date'}),
            'flotation_date': DateInput(attrs={'type': 'date'}),
        }

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = (

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



class LightResidueForm(forms.ModelForm):
    class Meta:
        model = LightResidue
        fields = (
    'proportion_analysed',
        'soil_volume',
        'sample_volume',
        'sample_weight',
        'sediment',
        'stone',
        'roots',
        'leaves',
        'insect_parts',
        'charred_dung',
        'bone',
        'shell'
        )



class CompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = (
        'material_type',
        'type_count',
        'whole_weight',
        'fragment_weight',
        )





from django.views import generic
import django_filters


class SampleListView(generic.ListView):
    template_name = 'sample/sample_list.html'
    model = Sample
    paginate_by = 50
    queryset = Sample.objects.filter(sample_type='Organic')


    # context_object_name = 'sample'  # Default: object_list
    #
    # queryset = sample.objects.all()  # Default: Model.objects.all()


    #
    # def get_queryset(self):
    #     return LightResidue.objects.all().count()
        # return LightResidue.objects.filter().count()
