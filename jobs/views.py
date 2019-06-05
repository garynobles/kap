from django.shortcuts import render

from .models import Job, Announcements

def home(request):
    jobs = Job.objects.all()[:6]
    announcements = Announcements.objects.all()[:5]
    return render(request, 'jobs/home.html',
    {
      'jobs':jobs,
      'announcements':announcements,
     })
