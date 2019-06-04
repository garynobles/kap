from django.shortcuts import render
from sample.models import Sample
# Create your views here.

from django.db.models import Count, Q

def sample(request):

    number = Sample.objects.all().count()
    sample = Sample.objects.all()

    # botany = Sample.objects.filter(organic=True).count()

    earthen = Sample.objects.filter(sample_type='Earthen').count()
    organic = Sample.objects.filter(sample_type='Organic').count()
    vitreous = Sample.objects.filter(sample_type='Vitreous').count()
    plaster = Sample.objects.filter(sample_type='Plaster').count()
    stone = Sample.objects.filter(sample_type='Stone').count()
    ceramic = Sample.objects.filter(sample_type='Ceramic').count()
    mudbrick = Sample.objects.filter(sample_type='Mudbrick').count()
    metal = Sample.objects.filter(sample_type='Metal').count()
    plastic = Sample.objects.filter(sample_type='Plastic').count()
    soil = Sample.objects.filter(sample_type='Soil').count()


    dataset4 = {
        "earthen": earthen,
        "organic": organic,
        "vitreous": vitreous,
        "plaster": plaster,
        "stone": stone,
        "ceramic": ceramic,
        "mudbrick": mudbrick,
        "metal": metal,
        "plastic": plastic,
        "soil": soil,
    }

    return render(request, 'dashboard/samplehome.html',
    {
    'number':number,
    'dataset4': dataset4,
    'sample':sample,
    })





def overview(request):
    return render(request, 'dashboard/sampleoverview.html',
    )
