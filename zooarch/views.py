from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms

# from .forms import QnispForm
from .models import QnispForm
# from .forms import ZooarchForm
from zooarch.models import Qnisp





# Create your views here.

def allzooarch(request):
    # qnisp = Qnisp.objects.all()
    return render(request, 'zooarch/zooarch.html',
    {
        # 'zooarch':zooarch
    }
    )


#########
# qnisp #
#########
def allqnisp(request):
    qnisp = Qnisp.objects.all()
    return render(request, 'qnisp/allqnisp.html', {'qnisp':qnisp})

#
# # class QnispListView(FilterMixin, django_filters.views.FilterView):
# #     model = Qnisp
# #     paginate_by = 16
# #     filterset_class = QnispFilter
#
def createqnisp(request):
    if request.method == "POST":
        form = QnispForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by= request.user
            #post.datetime = datetime.datetime.now()

            post.save()
            return redirect('allqnisp')
    else:
        form = QnispForm()
    return render(request, 'qnisp/create_qnisp.html', {'form': form})
#
def removeqnisp(request, pk):
    Qnisp.objects.get(pk=pk).delete()
    return redirect('/zooarch/qnisp')
#
def editqnisp(request, pk):
    post = get_object_or_404(Qnisp, pk=pk)
    if request.method == "POST":
        form = QnispForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('allqnisp')
            #, pk=post.pk)
    else:
        form = QnispForm(instance=post)
    return render(request, 'qnisp/create_qnisp.html', {'form': form})
#
#
def detailqnisp(request, qnisp_id):
    detailqnisp = get_object_or_404(Qnisp, pk=qnisp_id)
    return render(request, 'qnisp/detailqnisp.html', {'qnisp':detailqnisp})
