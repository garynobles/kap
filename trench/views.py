from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from trench.models import Trench
from django import forms
# Create your views here.

def alltrenches(request):
    alltrenches = Trench.objects.all()
    return render(request, 'trench/trench.html',
    {
    'alltrenches':alltrenches,
    })

def addtrench(request):
    if request.method == "POST":
        form = TrenchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('alltrenches')
    else:
        form = TrenchForm()
    return render(request, 'trench/create_trench.html', {'form': form})

def edittrench(request, pk):
        post = get_object_or_404(Trench, pk=pk)
        if request.method == "POST":
            form = TrenchForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('alltrenches')
        else:
            form = TrenchForm(instance=post)
        return render(request, 'trench/create_trench.html', {'form': form})

def detailtrench(request, trench_id):
    trench = get_object_or_404(Trench, pk=trench_id)
    return render(request, 'trench/detail_trench.html',
    {
        'trench':trench,
    })



# forms
class TrenchForm(forms.ModelForm):
    class Meta:
        model = Trench
        fields = (
        'trench_id',
        'trench_name',
        'area_easting',
        'area_northing',
        )

        # widgets = {
        #     'entry_date': DateInput(attrs={'type': 'date'}),
        # }
