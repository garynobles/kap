from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from botany.models import Botany, Fraction, FractionComposition, Sample
from django import forms

from django.db.models import Count, Q
from django.shortcuts import render

from itertools import chain

def allbotanysample(request):
    botanysample = Sample.objects.all()
    return render(request, 'sample/sample.html',
    {
    'botanysample':botanysample,
    })

def addbotanysample(request):
        if request.method == "POST":
            form = BotanySampleFilterForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #botany_id = pk
                # post.analyst = request.user
                #post.datetime = datetime.datetime.now()

                post.save()
                return redirect('allbotanysample')
        else:
            form = BotanySampleFilterForm()
        return render(request, 'sample/createsample.html', {'form': form})



def allbotany(request):
    # number = Botany.objects..count()
    number = Botany.objects.all().count()
    fraction = Fraction.objects.all()
    fractioncomposition = FractionComposition.objects.all()
    # fractionmaterialspresent = FractionMaterialsPresent.objects.all()

    dataset = Botany.objects \
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

    a = Fraction.objects.values('roots').filter(roots=True)
    b = Fraction.objects.values('bone').filter(bone=True)
    c = Fraction.objects.values('sediment').filter(sediment=True)
    dataset4 = {"roots": a, "bone": b, "sediment": c}

    dataset5 = query2

    # dataset5 = a.filter(roots=True)| b.filter(bone=True)
    dataset6 = b.count()
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
    'dataset5': dataset5,
    'dataset6': dataset6,

    })


def allflotation(request):
    botany = Botany.objects.all()
    fraction = Fraction.objects.all()
    count = Fraction.objects.all().filter(botany_id=13).count()
    fractioncomposition = FractionComposition.objects.all()
    # fractionmaterialspresent = FractionMaterialsPresent.objects.all()
    return render(request, 'flotation/allflotation.html',
    {
    'botany':botany,
    'fraction':fraction,
    'count':count,
    'fractioncomposition':fractioncomposition,
    # 'fractionmaterialspresent':fractionmaterialspresent
    })

# def detail(request, blog_id):
#     detailblog = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog/detail.html', {'blog':detailblog})
def addflotation(request):
        if request.method == "POST":
            form = FlotationFilterForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #botany_id = pk
                # post.analyst = request.user
                #post.datetime = datetime.datetime.now()

                post.save()
                return redirect('allflotation')
        else:
            form = FlotationFilterForm()
        return render(request, 'flotation/createflotation.html', {'form': form})

class DateInput(forms.DateInput):
    input_type = 'date'

class FlotationFilterForm(forms.ModelForm):
    class Meta:
        model = Botany
        fields = (
        # 'botany_id',
        'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'entry_date',

        'analyst',
        # 'analyst_id',
        'notes',
        )

        widgets = {
            'entry_date': DateInput(attrs={'type': 'date'}),
        }

class BotanySampleFilterForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = (
        # 'botany_id',
        'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        'taken_by',

        )

        widgets = {
            'entry_date': DateInput(attrs={'type': 'date'}),
        }

def detailflotation(request, botany_id):
    detailflotation = get_object_or_404(Botany, pk=botany_id)
    #fraction = get_object_or_404(Fraction, botany_id=botany_id)
    #fraction = Fraction.objects.all()
    fraction = Fraction.objects.filter(botany_id__botany_id=botany_id)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(fraction_id__fraction_id=fraction_id)
    return render(request, 'flotation/detailflotation.html',
    {'botany':detailflotation, 'fraction':fraction,
    })

def addfraction(request, pk):
    if request.method == "POST":
    #if request.method == "GET":
        form = FractionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            botany = get_object_or_404(Botany, pk=pk)
            post.botany_id = botany
            #post.botany_id = pk
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
        #'botany_id',
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
            #post.botany_id = pk
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

def detailfraction(request, botany_id, fraction_id):


    detailfraction = get_object_or_404(Fraction, pk=fraction_id)
    fractionmaterialspresent = get_object_or_404(Fraction, pk=fraction_id)
    # detailflotation = get_object_or_404(Botany, pk=botany_id)
    fractioncomposition = FractionComposition.objects.filter(fraction_id__fraction_id=fraction_id)
    # fractionmaterialspresent = FractionMaterialsPresent.objects.filter(fraction_id__fraction_id=fraction_id)
    # detailflotation = Botany.objects.filter(botany_id__botany_id=botany_id)
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

def editfraction(request, pk):
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
        post = get_object_or_404(Botany, pk=pk)
        if request.method == "POST":
            form = FlotationFilterForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.user = request.user
                #post.datetime = datetime.datetime.now()
                post.save()
                return redirect('allflotation')
                #, pk=post.pk)
        else:
            form = FlotationFilterForm(instance=post)
        return render(request, 'flotation/createflotation.html', {'form': form})
