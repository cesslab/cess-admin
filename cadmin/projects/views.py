from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def projects(request):
    return render(request, 'projects.html')
