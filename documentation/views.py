from django.shortcuts import render

# Create your views here.


def documents(request):
    # alldocuments = Storage.objects.all()
    return render(request, 'documentation/docs.html',
    {
        # 'documents':documents
    })
