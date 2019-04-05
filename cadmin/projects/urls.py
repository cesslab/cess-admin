from django.urls import path
from .views import project_list, add_project, edit_project, delete_project


urlpatterns = [
    path('', project_list, name='projects_home'),
    path('add/', add_project, name='add_project'),
    path('edit/<int:id>/', edit_project, name='edit_project'),
    path('delete/<int:id>/', delete_project, name='delete_project'),
]
