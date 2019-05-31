from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django import forms
from tickets.models import Ticket
# Create your views here.

def allconservation(request):
    # allcon = Conservation.objects.all()
    return render(request, 'conservation/allconservation.html',
    # {
    # 'allcon': allcon,
    # }
    )
