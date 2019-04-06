from django.urls import path
from .views import project_list_view, project_add_view, project_edit_view, project_delete_view, ProjectListView

app_name = 'projects'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('add/', project_add_view, name='project-add'),
    path('edit/<int:id>/', project_edit_view, name='project-edit'),
    path('delete/<int:id>/', project_delete_view, name='project-delete'),
]
