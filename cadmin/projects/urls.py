from django.urls import path
from .views import projects, add_project


urlpatterns = [
    path('', projects, name='projects_home'),
    path('add/', add_project, name='add_project'),
]
