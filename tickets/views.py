from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django import forms
from tickets.models import Ticket
# Create your views here.

def alltickets(request):
    alltickets = Ticket.objects.all()
    return render(request, 'tickets_all.html',
    {
    'alltickets': alltickets,
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
            return redirect('alltickets')
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
            return redirect('alltickets')
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
        'category',
        'assigned_to',
        'status'
        )

        widgets = {
          'details': forms.Textarea(attrs={'rows':8, 'cols':15}),
        }
