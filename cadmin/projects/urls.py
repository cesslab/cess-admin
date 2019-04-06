from django.urls import path
from .views import project_list_view, project_add_view, project_edit_view, project_delete_view


urlpatterns = [
    path('', project_list_view, name='projects_home'),
    path('add/', project_add_view, name='project_add_view'),
    path('edit/<int:id>/', project_edit_view, name='project_edit_view'),
    path('delete/<int:id>/', project_delete_view, name='project_delete_view'),
]
