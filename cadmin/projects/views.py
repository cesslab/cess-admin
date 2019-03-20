from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project


@login_required
def projects(request):
    project_list = Project.objects.all()
    return render(request, 'projects.html', {'projects': project_list})


@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            project.users.add(request.user)
            project.save()
            return redirect('projects_home')
    form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


