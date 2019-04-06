from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project
from django.views.generic import ListView


class ProjectListView(ListView):
    template_name = 'projects.html'

    def get_queryset(self):
        print(self.request.user.projects.all())
        return self.request.user.projects.all()


@login_required
def project_list_view(request):
    projects = request.user.projects.all()
    return render(request, 'projects.html', {'projects': projects})


@login_required
def project_delete_view(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:project-list')
    return render(request, 'project_delete.html')


@login_required
def project_add_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            project = form.save(commit=False)
            # Save the project first
            project.save()
            # save collaborators listed, not including this user
            form.save_m2m()
            # add this user to the list of collaborators
            project.collaborators.add(request.user)
            project.save()
            return redirect('projects:project-list')
    form = ProjectForm(user=request.user)
    return render(request, 'add_project.html', {'form': form, 'type': 'Add'})


@login_required
def project_edit_view(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, user=request.user, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            # Save the project first
            project.save()
            # save collaborators listed, not including this user
            form.save_m2m()
            # add this user to the list of collaborators
            project.collaborators.add(request.user)
            project.save()
            return redirect('projects:project-list')
    form = ProjectForm(user=request.user, instance=project)
    return render(request, 'add_project.html', {'form': form, 'type': 'Update'})
