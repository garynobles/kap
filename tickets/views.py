from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.contrib.auth.models import User
from django import forms
from tickets.models import Ticket
# Create your views here.

def alltickets(request):
    alltickets = Ticket.objects.all()
    return render(request, 'tickets_all.html',
    {
    'alltickets': alltickets,


    })

def opentickets(request):
    # current_user = request.user.id
    open = Ticket.objects.all().exclude(status='completed')
    current_user=request.user
    # open = Ticket.objects.filter(submitted_by = current_user)
    # open = Ticket.objects.filter(current_user)
    return render(request, 'open_tickets.html',
    {
    'open':open

    })

def closedtickets(request):
    alltickets = Ticket.objects.all()
    archived = Ticket.objects.all().filter(status='completed')
    open = Ticket.objects.all().filter(status='completed')
    return render(request, 'archived_tickets.html',
    {
    'archived':archived,
    })

def createticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.submitted_by = request.user
            # post.modified_by = request.user
            # post.datetime = datetime.datetime.now()
            post.save()
            return redirect('opentickets')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})

def editticket(request, pk):
    post = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user = request.user
            #post.datetime = datetime.datetime.now()
            post.save()
            return redirect('opentickets')
            #, pk=post.pk)
    else:
        form = TicketForm(instance=post)
    return render(request, 'create_ticket.html', {'form': form})


def deleteticket(request, pk):
    Ticket.objects.get(pk=pk).delete()
    return redirect('alltickets')

def detailticket(request):
    pass


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
        # 'ticket_id',
        'submitted_by',
        'subject',
        'details',
        'department',
        'system',
        'category',
        'assigned_to',
        'priority',
        'status'
        )

        widgets = {
          'details': forms.Textarea(attrs={'rows':8, 'cols':15}),
        }
