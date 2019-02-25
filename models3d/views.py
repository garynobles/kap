from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from models3d.models import Models3d

# Create your views here.
def models3d(request):
    models3d = Models3d.objects.all()
    return render(request, 'models3d/index.html',
        {
            'models3d': models3d,
        }
    )

# def allsample(request):
#     models3d = Models3d.objects.all()
#     # filter(sample_type='Botanical')
#     return render(request, 'models3d/index.html',
#     {
#     'allsample':allsample,
#     })
