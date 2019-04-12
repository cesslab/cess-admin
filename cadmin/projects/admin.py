from django.contrib import admin

# Register your models here.
from .models import User, Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    filter_horizontal = ('primary_investigators', 'research_assistants',)


admin.site.register(User)
admin.site.register(Project, ProjectAdmin)
