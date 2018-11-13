from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from botany.models import Botany, Fraction, FractionComposition, FractionMaterialsPresent
from django import forms

# Create your views here.
def allflotation(request):
    botany = Botany.objects.all()
    fraction = Fraction.objects.all()
    fractioncomposition = FractionComposition.objects.all()
    fractionmaterialspresent = FractionMaterialsPresent.objects.all()
    return render(request, 'botany/allflotation.html',
    {'botany':botany,
    'fraction':fraction,
    'fractioncomposition':fractioncomposition,
    'fractionmaterialspresent':fractionmaterialspresent
    })

# def detail(request, blog_id):
#     detailblog = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog/detail.html', {'blog':detailblog})
def addflotation(request):
        if request.method == "POST":
            form = BotanyFilterForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #botany_id = pk
                #post.user = request.user
                #post.datetime = datetime.datetime.now()

                post.save()
                return redirect('allflotation')
        else:
            form = BotanyFilterForm()
        return render(request, 'botany/createflotation.html', {'form': form})

class BotanyFilterForm(forms.ModelForm):
    class Meta:
        model = Botany
        fields = (
        # 'botany_id',
        'sample_id',
        'area_easting',
        'area_northing',
        'context_number',
        'sample_number',
        # 'entry_date',
        # 'analysis_date',
        'analyst',
        'notes',
        )

def detailbotany(request, botany_id):
    detailbotany = get_object_or_404(Botany, pk=botany_id)
    #fraction = get_object_or_404(Fraction, botany_id=botany_id)
    #fraction = Fraction.objects.all()
    fraction = Fraction.objects.filter(botany_id__botany_id=botany_id)
    #joinsamplecontainer = JoinSampleContainer.objects.filter(fraction_id__fraction_id=fraction_id)
    return render(request, 'botany/detailbotany.html',
    {'botany':detailbotany, 'fraction':fraction,
    })

###########################################
#
# def allfraction(request):
#     fraction = Fraction.objects
#     return render(request, 'fraction/allfraction.html', {'fraction':fraction})
#
# #def createfraction(request, pk):
#
#def addfraction(request, pk):
#def addfraction(request, *args, **kwargs):
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
        )

######################################
#
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

# def addcomposition(request, pk):
#     if request.method == "POST":
#         form = FractionCompositionForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             fraction = get_object_or_404(Fraction, pk=pk)
#             post.fraction_id = fraction
#             #post.user = request.user
#             #post.datetime = datetime.datetime.now()
#
#             post.save()
#             return redirect('allfractioncomposition')
#     else:
#         form = FractionCompositionForm()
#     return render(request, 'fractioncomposition/create_fractioncomposition.html', {'form': form})

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


def addmaterialpresent(request, pk, fk):
    if request.method == "POST":
        form = FractionMaterialPresentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            fraction = get_object_or_404(Fraction, pk=pk)
            post.fraction_id = fraction
            #post.user = request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allflotation')
    else:
        form = FractionMaterialPresentForm()
    return render(request, 'fractionmaterialpresent/create_fractionmateralpresent.html', {'form': form})


class FractionMaterialPresentForm(forms.ModelForm):
    class Meta:
        model = FractionMaterialsPresent
        fields = (
        # 'material_id',
        # 'fraction_id',
        'material',
        )

def detailfraction(request, botany_id, fraction_id):

    detailfraction = get_object_or_404(Fraction, pk=fraction_id)
    fractionmaterialspresent = get_object_or_404(Fraction, pk=fraction_id)
    # detailbotany = get_object_or_404(Botany, pk=botany_id)
    fractioncomposition = FractionComposition.objects.filter(fraction_id__fraction_id=fraction_id)
    fractionmaterialspresent = FractionMaterialsPresent.objects.filter(fraction_id__fraction_id=fraction_id)
    # detailbotany = Botany.objects.filter(botany_id__botany_id=botany_id)
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

# def editbotany(request):
#     pass
#
#
#
# def allfractioncomposition(request):
#     fractioncomposition = FractionComposition.objects
#     return render(request, 'fractioncomposition/allfractioncomposition.html', {'fractioncomposition':fractioncomposition})
#
# def editfractioncomposition(request):
#     pass
#
# def allfractionmaterialpresent(request):
#     fractionmaterialpresent = FractionMaterialsPresent.objects
#     return render(request, 'fractionmaterialpresent/allfractionmaterialpresent.html', {'fractionmaterialpresent':fractionmaterialpresent})
#
# def editfractionmaterialpresent(request):
#     pass
#
#
#
# def detailfractioncomposition(request, fract_comp_id):
#     detailfractioncomposition = get_object_or_404(FractionComposition, pk=fract_comp_id)
#     #joinsamplecontainer = JoinSampleContainer.objects.filter(fraction_id__fraction_id=fraction_id)
#     return render(request, 'fractioncomposition/detailfractioncomposition.html',
#     {'fractioncomposition':detailfractioncomposition,
#     #'joinsamplecontainer':joinsamplecontainer
#     })
#
# def detailfractionmaterialpresent(request, material_id):
#     detailfractionmaterialpresent = get_object_or_404(FractionMaterialsPresent, pk=material_id)
#     #joinsamplecontainer = JoinSampleContainer.objects.filter(fraction_id__fraction_id=fraction_id)
#     return render(request, 'fractionmaterialpresent/detailfractionmaterialpresent.html',
#     {'fractionmaterialpresent':detailfractionmaterialpresent,
#     #'joinsamplecontainer':joinsamplecontainer
#     })
#

#
#
#

#
# def editfraction(request, fraction_id):
#         post = get_object_or_404(Fraction, pk=fraction_id)
#         if request.method == "POST":
#             form = FractionFilterForm(request.POST, instance=post)
#             if form.is_valid():
#                 post = form.save(commit=False)
#                 #post.user = request.user
#                 #post.datetime = datetime.datetime.now()
#                 post.save()
#                 return redirect('allfraction')
#                 #, pk=post.pk)
#         else:
#             form = FractionFilterForm(instance=post)
#         return render(request, 'fraction/create_fraction.html', {'form': form})
