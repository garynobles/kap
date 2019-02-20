from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from botany.models import Flotation, Fraction, FractionComposition, Sample
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

def addsample(request):
    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #flotation_id = pk
            # post.analyst = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allsample')
    else:
        form = SampleForm()
    return render(request, 'sample/createsample.html', {'form': form})

# def detailsample(request, sample_id):
#     detailsample = get_object_or_404(Sample, pk=sample_id)
#     return render(request, 'sample/detailsample.html',
#     {'detailsample':detailsample,
#     })





def allbotany(request, sample_id=''):
    # number = Botany.objects..count()
    number = Flotation.objects.all().count()
    fraction = Fraction.objects.all()
    fractioncomposition = FractionComposition.objects.all()
    # fractionmaterialspresent = FractionMaterialsPresent.objects.all()

    dataset = Flotation.objects \
        .values('context_number') \
        .order_by('context_number')

    query1 = Fraction.objects \
        .values('soil_volume')

    query2 = Fraction.objects.values('soil_volume')
    query3 = Fraction.objects.values('sample_volume')

    # query2 = Fraction.objects \
    #     .values('sample_volume')
    dataset2 = Fraction.objects.values('soil_volume')
    dataset3 = query3

    # a = Fraction.objects.values('roots').filter(roots=True)
    # b = Fraction.objects.values('bone').filter(bone=True)
    # c = Fraction.objects.values('sediment').filter(sediment=True)
    # dataset4 = {"roots": a, "bone": b, "sediment": c}
    text = Flotation.objects.values('notes')



    roots = Fraction.objects.filter(roots=True).count()
    bone = Fraction.objects.filter(bone=True).count()
    sediment = Fraction.objects.filter(sediment=True).count()
    shell = Fraction.objects.filter(shell=True).count()
    stone = Fraction.objects.filter(stone=True).count()
    leaves = Fraction.objects.filter(leaves=True).count()
    insect_parts = Fraction.objects.filter(insect_parts=True).count()
    charred_dung = Fraction.objects.filter(charred_dung=True).count()
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

    # roots = Fraction.objects \
    #     .values('roots').filter(roots=True)
    # bone = Fraction.objects \
    #     .values('bone').filter(bone=True).count()
    bone=5


    # dataset5 = a.filter(roots=True)| b.filter(bone=True)
    # dataset6 = b.count()
    # dataset3 = Fraction.objects.values('soil_volume')
    # matches = pages | articles | posts


        # query2 = Fraction.objects.count('bone')
        #
        # sumquery = query1 + query2

            # .values('soil_volume') \
            # .annotate(num_values=Count('value'), average=Avg('value'))\
            # .order_by('soil_volume')


    return render(request, 'dashboard/botanyhome.html',
    {
    # 'botany':botany,
    'number':number,
    'fraction':fraction,
    'fractioncomposition':fractioncomposition,
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


def allflotation(request, sample_id='', flotation_id='', fraction_id=''):
    flotation = Flotation.objects.all()
    fraction = Fraction.objects.all()
    count = Fraction.objects.all().count()
    # .filter(flotation_id=6).count()
    fractioncomposition = FractionComposition.objects.all()
    # fractionmaterialspresent = FractionMaterialsPresent.objects.all()
    return render(request, 'flotation/allflotation.html',
    {
    'flotation':flotation,
    'fraction':fraction,
    'count':count,
    'fractioncomposition':fractioncomposition,
    # 'fractionmaterialspresent':fractionmaterialspresent
    })





def addflotation(request, pk='', sample_id='', flotation_id=''):
        if request.method == "POST":
            form = FlotationForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #flotation_id = pk
                # post.analyst = request.user
                #post.datetime = datetime.datetime.now()

                post.save()
                return redirect('allflotation')
        else:
            form = FlotationForm()
        return render(request, 'flotation/createflotation.html', {'form': form})

class DateInput(forms.DateInput):
    input_type = 'date'

class FlotationForm(forms.ModelForm):
    class Meta:
        model = Flotation
        fields = (
        # 'flotation_id',
        'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'flotation_date',
        'entry_date',
        'analyst_id',
        # 'analyst_id',
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
        # 'flotation_id',
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

def detailsample(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    # fraction = get_object_or_404(Fraction, flotation_id=flotation_id)
    #fraction = Fraction.objects.all()
    flotation = Flotation.objects.filter(sample_id__sample_id=sample_id)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(fraction_id__fraction_id=fraction_id)
    return render(request, 'sample/detailsample.html',
    {'sample':sample, 'flotation':flotation,
    })


def detailflotation(request, flotation_id):
    flotation = get_object_or_404(Flotation, pk=flotation_id)
    #fraction = get_object_or_404(Fraction, flotation_id=flotation_id)
    #fraction = Fraction.objects.all()
    fraction = Fraction.objects.filter(flotation_id__flotation_id=flotation_id)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(fraction_id__fraction_id=fraction_id)
    return render(request, 'flotation/detailflotation.html',
    {'flotation':flotation, 'fraction':fraction,
    })

def addfraction(request, pk, fk=''):
    if request.method == "POST":
    #if request.method == "GET":
        form = FractionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            flotation = get_object_or_404(Flotation, pk=pk)
            post.flotation_id = flotation
            #post.flotation_id = pk
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            #return redirect('allfraction')
            return redirect('allflotation')
    else:
        #import pdb; pdb.set_trace()
        form = FractionForm()
    return render(request, 'fraction/create_fraction.html', {'form': form})

class FractionForm(forms.ModelForm):
    class Meta:
        model = Fraction
        fields = (
        #'fraction_id',
        #'flotation_id',
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

def addcomposition(request, pk, fk):
    if request.method == "POST":
    #if request.method == "GET":
        form = FractionCompositionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            fraction = get_object_or_404(Fraction, pk=pk)
            post.fraction_id = fraction
            #post.flotation_id = pk
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            #return redirect('allfraction')
            return redirect('allflotation')
    else:
        #import pdb; pdb.set_trace()
        form = FractionCompositionForm()
    return render(request, 'fractioncomposition/create_fractioncomposition.html', {'form': form})

class FractionCompositionForm(forms.ModelForm):
    class Meta:
        model = FractionComposition
        fields = (
        # 'fract_comp_id',
        # 'fraction_id',
        'material_type',
        'fraction',
        'type_count',
        'whole_weight',
        'fragment_weight',
        )

def detailfraction(request, flotation_id, fraction_id):
    detailfraction = get_object_or_404(Fraction, pk=fraction_id)
    fractionmaterialspresent = get_object_or_404(Fraction, pk=fraction_id)
    # detailflotation = get_object_or_404(Botany, pk=flotation_id)
    fractioncomposition = FractionComposition.objects.filter(fraction_id__fraction_id=fraction_id)
    # fractionmaterialspresent = FractionMaterialsPresent.objects.filter(fraction_id__fraction_id=fraction_id)
    # detailflotation = Botany.objects.filter(flotation_id__flotation_id=flotation_id)
    #fractionmaterialspresent = FractionMaterialsPresent.objects.filter(fraction_id__fraction_id=fraction_id)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(fraction_id__fraction_id=fraction_id)
    return render(request, 'fraction/detailfraction.html',
    {'fraction':detailfraction,
    'fractioncomposition':fractioncomposition,
    # 'botany':botany,
    'fractionmaterialspresent':fractionmaterialspresent,
    #'joinsamplecontainer':joinsamplecontainer,
    # 'botany':botany,
    })

def editfraction(request, pk, fk=''):
        post = get_object_or_404(Fraction, pk=pk)
        # pk=pk
        if request.method == "POST":
            form = FractionForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.user = request.user
                #post.datetime = datetime.datetime.now()
                post.save()
                return redirect('allflotation')

                # return redirect('allfraction')
                #, pk=post.pk)
        else:
            form = FractionForm(instance=post)
        return render(request, 'fraction/create_fraction.html', {'form': form})

def editflotation(request, pk):
        post = get_object_or_404(Flotation, pk=pk)
        if request.method == "POST":
            form = FlotationForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.user = request.user
                #post.datetime = datetime.datetime.now()
                post.save()
                return redirect('allflotation')
                #, pk=post.pk)
        else:
            form = FlotationForm(instance=post)
        return render(request, 'flotation/createflotation.html', {'form': form})


def editsample(request, pk):
        post = get_object_or_404(Sample, pk=pk)
        if request.method == "POST":
            form = SampleForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.user = request.user
                #post.datetime = datetime.datetime.now()
                post.save()
                return redirect('allsample')
                #, pk=post.pk)
        else:
            form = SampleForm(instance=post)
        return render(request, 'sample/createsample.html', {'form': form})
