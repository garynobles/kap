from django.shortcuts import render, get_object_or_404, render_to_response, redirect

# Create your views here.
def teams(request):
    # allteams = Teams.objects.all()
    return render(request, 'teams/teams.html',
    {
        'teams':teams
    })
