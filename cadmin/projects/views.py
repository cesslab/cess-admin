from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm


@login_required
def projects(request):
    return render(request, 'projects.html')


def add_project(request):
    if request.method == 'POST':
        pass
    form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


