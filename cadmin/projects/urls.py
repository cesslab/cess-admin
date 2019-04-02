from django.urls import path
from .views import projects, add_project, edit_project


urlpatterns = [
    path('', projects, name='projects_home'),
    path('add/', add_project, name='add_project'),
    path('edit/<int:id>/', edit_project, name='edit_project'),
]
