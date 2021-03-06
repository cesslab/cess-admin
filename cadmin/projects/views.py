from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, FileItemForm
from .models import Project, FileItem
from django.views.generic import ListView
from django.utils. decorators import method_decorator
from django.conf import settings


@method_decorator(login_required, name='dispatch')
class ProjectListView(ListView):
    template_name = 'project/list.html'

    def get_queryset(self):
        if self.request.user.is_irbadmin:
            return Project.objects.all()
        else:
            return self.request.user.pi_projects.all() | self.request.user.ra_projects.all()


@login_required
def project_delete_view(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:project-list')
    return render(request, 'project/delete.html')


@login_required
def file_add(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        form = FileItemForm(request.POST, request.FILES)
        if form.is_valid():
            if settings.S3_ENABLED:
                file = form.save(commit=False)
                file.project = project
                file.save()
            else:
                file = FileItem(file=request.FILES['file'])
                file.project = project
                file.save()
            return redirect('projects:project-list')
    form = FileItemForm()
    return render(request, 'project/add_file_item.html', {'form': form})


@login_required
def project_add_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, user=request.user)
        if form.is_valid():
            project = form.save(commit=False)
            # Save the project first
            project.save()
            # save collaborators listed, not including this user
            form.save_m2m()
            return redirect('projects:project-list')
    form = ProjectForm(user=request.user)
    return render(request, 'project/add.html', {'form': form, 'type': 'Add'})


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
            pi = project.primary_investigators.filter(id=request.user.id).exists()
            ra = project.research_assistants.filter(id=request.user.id).exists()
            # Add this user to the PI list if they didn't specify their role in this project
            if not (pi or ra):
                project.primary_investigators.add(request.user)
                project.save()
            return redirect('projects:project-list')
        else:
            print(form.errors)
    form = ProjectForm(user=request.user, instance=project)
    return render(request, 'project/add.html', {'form': form, 'type': 'Update'})
