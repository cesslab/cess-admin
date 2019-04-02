from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project


@login_required
def projects(request):
    project_list = Project.objects.filter(collaborators__in=[request.user.id])
    return render(request, 'projects.html', {'projects': project_list})


@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, user=request.user)
        if form.is_valid():
            # The project must be saved to the DB before adding the collaborator.
            project = form.save(commit=False)
            project.save()
            project.collaborators.add(request.user)
            project.save()
            return redirect('projects_home')
    form = ProjectForm(user=request.user)
    return render(request, 'add_project.html', {'form': form, 'type': 'Add'})


@login_required
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, user=request.user, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('projects_home')
    form = ProjectForm(user=request.user, instance=project)
    return render(request, 'add_project.html', {'form': form, 'type': 'Update'})
